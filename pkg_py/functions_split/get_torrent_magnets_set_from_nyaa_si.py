

import zlib
import shutil
import pyglet
from tkinter import UNDERLINE
from selenium.common.exceptions import WebDriverException
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
from pkg_py.pk_system_object.is_os_windows import is_os_windows

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def get_torrent_magnets_set_from_nyaa_si(title_to_search, driver_selenium, exclude_elements_all=None,
                                         include_elements_any=None, include_elements_all=None):
    import urllib.parse

    import inspect
    exclude_elements_all = exclude_elements_all or []
    include_elements_any = include_elements_any or []
    include_elements_all = include_elements_all or []
    func_n = inspect.currentframe().f_code.co_name
    pk_print(working_str=rf'''{PK_UNDERLINE}{func_n}()  {'%%%FOO%%%' if LTA else ''}''', print_color='blue')
    f_func_n_txt = rf'{D_PROJECT}\pkg_txt\{func_n}.txt'
    query = urllib.parse.quote(f"{title_to_search}")
    url = f'https://nyaa.si/?f=0&c=0_0&q={query}'
    pk_print(working_str=rf'''url="{url}"  {'%%%FOO%%%' if LTA else ''}''')
    url_decoded = get_str_url_decoded(str_working=url)
    pk_print(working_str=rf'''url_decoded="{url_decoded}"  {'%%%FOO%%%' if LTA else ''}''')
    driver_selenium.get(url)

    # 페이지 소스 RAW
    page_src = driver_selenium.page_source
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page_src, "html.parser")

    magnets_list = []
    magnets_set = set()

    # 문자열에서 마지막 숫자 remove
    title_to_search = get_str_removed_last_digit(title_to_search).strip()

    # 페이지에서 모든 링크 추출
    lines = soup.find_all(name="a")
    for line in lines:
        magnet = line.get('href')
        if magnet:
            magnets_list.append(magnet)

    for magnet in magnets_list:
        decoded_magnet = get_str_url_decoded(magnet)
        # pk_print(string = rf'''decoded_magnet="{decoded_magnet}"  {'%%%FOO%%%' if LTA else ''}''')

        # 검색 문자열이 URL에 포함되어 있는지 확인
        if is_pattern_in_prompt(prompt=decoded_magnet, pattern=title_to_search):
            if exclude_elements_all and include_elements_any and include_elements_all:

                # 필터링 조건 평가
                include_all_check = all(include in decoded_magnet for include in include_elements_all)
                exclude_check = not any(exclude in decoded_magnet for exclude in exclude_elements_all)
                include_any_check = any(include in decoded_magnet for include in include_elements_any)

                # 필터링 조건이 만족되면
                if include_all_check and exclude_check and include_any_check:
                    magnets_set.add(magnet)
            else:
                magnets_set.add(magnet)
    return magnets_set
