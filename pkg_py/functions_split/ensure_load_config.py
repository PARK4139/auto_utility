import urllib
import toml
import toml
import timeit
import threading
import sqlite3
import secrets
import psutil
import paramiko
import pandas as pd
import os.path
import mysql.connector
import json
import ipdb
import easyocr
import clipboard
import browser_cookie3
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.map_massages import PkMessages2025

from PIL import Image, ImageFilter
from os.path import dirname
from moviepy import VideoFileClip
from functools import partial as functools_partial
from functools import lru_cache
from dirsync import sync
from dataclasses import dataclass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


def ensure_load_config():
    container = get_pk_config("db_container_name", "nyaa_mariadb")
    name = get_pk_config("db_name", "nyaa_db")
    pwd = get_pk_config("db_password", "example")
    port = int(get_pk_config("db_port", "3306"))
    return container, name, pwd, port
