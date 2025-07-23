import win32com.client
import traceback
import tqdm
import tomllib
import string
import pywintypes
import platform
import os.path
import nest_asyncio
import hashlib
import cv2
from zipfile import BadZipFile
from PySide6.QtWidgets import QApplication
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
from pkg_py.pk_system_object.get_list_calculated import get_list_calculated
from passlib.context import CryptContext
from os import path
from mutagen.mp3 import MP3
from functools import partial
from enum import Enum
from dirsync import sync
from dataclasses import dataclass
from bs4 import BeautifulSoup
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def merge_f_excel_list(d):
    import inspect
    import os
    import traceback

    func_n = inspect.currentframe().f_code.co_name
    try:
        # xls 에서 xlsx로 변환 # openpyxl 은 xls 지원안함.  xlsx 가 더 최신기술.
        f_to_merge_ext = ".xls"
        f_list = [rf"{d}\{file}" for file in os.listdir(d) if f_to_merge_ext in get_x(file)]
        for f in f_list:
            convert_xls_to_xlsx(f)

        # 합병할 f의 목록을 리스트에 저장
        f_to_merge_ext = ".xlsx"
        f_list_to_merge = [f"{d}/{file}" for file in os.listdir(d) if f_to_merge_ext in get_x(file)]
        [print(item) for item in f_list_to_merge]
        print(rf'type(file_list) : {type(f_list_to_merge)}')
        print(rf'len(file_list) : {len(f_list_to_merge)}')

        # f합병할 작업공간 제어
        # wb_new=openpyxl.Workbook()
        # ws1=wb_new.active
        # ws2=wb_new.create_sheet("result")
        # files_cnt=len(files_to_merge)

        # 엑셀 병합 및 저장
        f_merged = F_MERGED_EXCEL_FILE
        merged_cnt = 0
        import pandas as pd
        merged_df = pd.DataFrame()
        for file_path in f_list_to_merge:
            # df=pd.read_excel(file_path, engine="openpyxl")  # 엑셀 f 읽기
            # df=pd.read_excel(file_path, engine="openpyxl", header=0, usecols=[0, 1, 2,3])  # fail, sheet_name="Sheet1"  여러 시트가 있을 경우 시트명을 직접 입력하여 dataframe화 # usecols=[0, 2]  컬럼선택
            # df=pd.read_excel(file_path, engine="openpyxl", header=0, usecols=[1, 2,3])  # fail,   sheet_name="Sheet1"  여러 시트가 있을 경우 시트명을 직접 입력하여 dataframe화 # usecols=[0, 2]  컬럼선택
            df = pd.read_excel(file_path, engine="openpyxl")  # success, 근데 sheet1 만 되고 sheet2 는 무시 된다.

            # 첫줄 remove
            # df=df.iloc[1:]  # 이번 데이터 구조상, 첫줄 을 제외한 나머지 데이터 선택

            # 마지막줄 remove
            # df=df.iloc[:-1]  # 이번 데이터 구조상, 마지막줄 제외한 나머지 데이터 선택

            merged_df = pd.concat([merged_df, df], ignore_index=True)  # 두 데이터프레임 병합

            merged_cnt = merged_cnt + 1

        print(rf'''merge_files_cnt : {merged_cnt + 1}''')
        print(rf'''merged_df : ''')
        print(rf'''{merged_df}''')
        print(rf'''merged_cnt : {merged_cnt}''')
        print(rf'''merged_file : {f_merged}''')
        try:
            merged_df.to_excel(f_merged)  # success
            # pd.ExcelWriter(merged_file, engine= "openpyxl") # fail, 확장자 잘못 저장했나?
            # open_pnx(merged_file)
            open_pnx_by_ext(pnx=f_merged)
        except PermissionError:
            pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            pk_print(f"{func_n}() 엑셀f이 열려있을 수 있습니다. 닫고 머지를 다시 시도해 주세요", print_color='red')
        except Exception as e:
            pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            pk_print(f"{func_n}() \n {traceback.format_exc()}", print_color='red')
    except:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
