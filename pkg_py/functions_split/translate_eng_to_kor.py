import winreg

import win32con
import urllib
import tqdm
import tomllib
import threading
import shutil
import re
import random
import os.path
import json
import ipdb
import importlib
import functools
import colorama
import colorama
import clipboard
import chardet
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import quote, urlparse
from urllib.parse import quote
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.get_list_calculated import get_list_calculated

from passlib.context import CryptContext
from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial
from datetime import timedelta
from datetime import date
from cryptography.hazmat.backends import default_backend
from collections import defaultdict, Counter
from bs4 import ResultSet
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def translate_eng_to_kor(question: str):
    import sys
    import traceback

    import pyautogui
    if not is_internet_connected():
        raise
    try:
        while 1:
            try:
                question = question.strip('""')
            except AttributeError:
                break
            ensure_pressed("win", "m")

            # 구글 번역 페이지로 이동
            url = "https://www.google.com/search?q=eng+to+kor"
            cmd = f'explorer "{url}" >nul'
            ensure_command_excuted_to_os_like_person_as_admin(cmd)

            # 크롬 창 활성화
            target_pid: int = get_pids(process_img_n="chrome.exe")  # chrome.exe pid 가져오기
            ensure_window_to_front(pid=target_pid)

            # 텍스트를 입력하세 클릭
            f_png = rf"{D_PROJECT}\pkg_image\eng to kor.png"
            click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, is_zoom_toogle_mode=True, loop_limit_cnt=100)

            # 번역할 내용 작성
            ensure_writen_fast(question)

            # 글자수가 많으면 text to voice icon 이 잘려서 보이지 않음. 이는 이미지의 객체 인식이 불가능해지는데
            # 스크롤를 내려서 이미지 인식을 가능토록
            if len(question) > 45:
                pyautogui.vscroll(-15)
            ensure_slept(30)

            # text to voice icon
            f_png = rf"{D_PROJECT}\pkg_image\text to voice icon.png"
            click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, is_zoom_toogle_mode=True, loop_limit_cnt=100)

            # 종료
            break
    except:
        traceback.print_exc(file=sys.stdout)
