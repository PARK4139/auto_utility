def ensure_command_excuted_to_os_v6(cmd: str, mode="", encoding=None, mode_with_window=1):
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.encodings import Encoding
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
    from pkg_py.functions_split.is_os_linux import is_os_linux
    from pkg_py.functions_split.is_os_windows import is_os_windows

    def decode_with_fallback(byte_data, primary_encoding):
        try:
            return byte_data.decode(primary_encoding)
        except UnicodeDecodeError:
            if is_os_windows():
                return byte_data.decode('cp949', errors='replace')
            else:
                return byte_data.decode('utf-8', errors='replace')

    if encoding is None:
        encoding = Encoding.UTF8
    if mode == "":
        mode = 'sync'
    if mode == "a":
        mode = 'async'
    if LTA:
        ensure_printed(rf'''"[ ATTEMPTED ]" {cmd} encoding={encoding:5s} mode={mode}''')
    std_list = []
    
    if mode == "async":
        if mode_with_window:
            import subprocess
            if is_os_windows():
                subprocess.Popen(args=cmd, shell=True)
            else:
                # Linux/macOS에서는 CREATE_NO_WINDOW 플래그가 없음
                subprocess.Popen(args=cmd, shell=True)
            return
        else:
            import subprocess
            if is_os_windows():
                subprocess.Popen(args=cmd, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                # Linux/macOS에서는 백그라운드로 실행
                subprocess.Popen(args=cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return
    else:
        try:
            process = None
            if mode_with_window:
                import subprocess
                process = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                import subprocess
                if is_os_windows():
                    process = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
                else:
                    process = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout_bytes, stderr_bytes = process.communicate()
            stdout = None
            stderr = None
            try:
                stdout = decode_with_fallback(stdout_bytes, encoding.value)
                stderr = decode_with_fallback(stderr_bytes, encoding.value)
            except AttributeError:
                stdout = decode_with_fallback(stdout_bytes, encoding)
                stderr = decode_with_fallback(stderr_bytes, encoding)

            if stdout:
                std_list.extend(line.strip() for line in stdout.splitlines())
            if stderr:
                std_list.extend(line.strip() for line in stderr.splitlines())

            ensure_iterable_printed_as_vertical(item_iterable=std_list, item_iterable_n=rf'{cmd}')

        except Exception:
            import traceback
            ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

        finally:
            try:
                if process and process.poll() is None:
                    process.terminate()

                # 필터링
                # useless_list = get_list_from_f(f=F_ALIAS_CMD) + [" {'%%%FOO%%%' if LTA else ''}", ""]
                # std_list = [x for x in std_list if x not in useless_list]

            except Exception:
                import traceback
                ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

        return std_list
