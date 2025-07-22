# import win32gui
import win32con
import traceback
import tqdm
import tomllib
import toml
import toml
import timeit
import time
import threading
import subprocess
import string
import random
import pygetwindow
import psutil
import paramiko
import importlib
import datetime
from telethon import TelegramClient, events
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern

from pkg_py.pk_system_object.stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from PIL import Image
from paramiko import SSHClient, AutoAddPolicy
from bs4 import ResultSet
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.pk_system_object.etc import PK_UNDERLINE
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.pk_print import pk_print


def get_all_ngram_list(f_nx, max_n, token_splitter_pattern):
    import os
    import re
    f_n, _ = os.path.splitext(f_nx)
    tokens = re.split(token_splitter_pattern, f_n)
    tokens = [t for t in tokens if t]  # 빈 문자열 제거
    all_ngram_list = []

    for n in range(max_n, 0, -1):
        if len(tokens) >= n:
            ngrams = [' '.join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]
            all_ngram_list.extend(ngrams)
    return all_ngram_list
