@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion





:: Log file setup
set "LOGFILE=%TEMP%\ensure_pk_enabled_log.txt"
echo. > "%LOGFILE%"

:: Initial state
set "CURRENT_STEP="
set "D_PKG_WINDOWS=%USERPROFILE%\Downloads\pk_system\pkg_windows"


call "%D_PKG_WINDOWS%\ensure_pk_os_constants_enabled.cmd"


:: Step 0: Start message
powershell -Command "Write-Host '📢 ensure_pk_enabled.cmd started' -ForegroundColor Cyan"
echo 📢 ensure_pk_enabled.cmd started >> "%LOGFILE%"

:: Step 1: Import pk_alias
echo ──────────────────────────────────────────────────────────
set "CURRENT_STEP=Importing pk_alias"
powershell -Command "Write-Host '[1/6] %CURRENT_STEP%' -ForegroundColor Cyan"
echo [STEP] %CURRENT_STEP% >> "%LOGFILE%"
call "%D_PKG_WINDOWS%\ensure_pk_alias_enabled.cmd"
if errorlevel 1 (
    powershell -Command "Write-Host '❌ Failed: %CURRENT_STEP%' -ForegroundColor Red"
    echo ❌ Failed: %CURRENT_STEP% >> "%LOGFILE%"
    goto END
)

:: Step 2: Import shortcut
echo ──────────────────────────────────────────────────────────
set "CURRENT_STEP=Importing shortcut"
powershell -Command "Write-Host '[2/6] %CURRENT_STEP%' -ForegroundColor Cyan"
echo [STEP] %CURRENT_STEP% >> "%LOGFILE%"
call "%D_PKG_WINDOWS%\ensure_pk_ahk_enabled.cmd"
if errorlevel 1 (
    powershell -Command "Write-Host '❌ Failed: %CURRENT_STEP%' -ForegroundColor Red"
    echo ❌ Failed: %CURRENT_STEP% >> "%LOGFILE%"
    goto END
)

:: Step 3: Installing uv
echo ──────────────────────────────────────────────────────────
set "CURRENT_STEP=Installing uv"
powershell -Command "Write-Host '[3/6] %CURRENT_STEP%' -ForegroundColor Cyan"
echo [STEP] %CURRENT_STEP% >> "%LOGFILE%"
call "%D_PKG_WINDOWS%\ensure_uv_enabled.cmd"
if errorlevel 1 (
    powershell -Command "Write-Host '❌ Failed: %CURRENT_STEP%' -ForegroundColor Red"
    echo ❌ Failed: %CURRENT_STEP% >> "%LOGFILE%"
    goto END
)

:: Step 4: Syncing uv
echo ──────────────────────────────────────────────────────────
set "CURRENT_STEP=Syncing uv packages"
powershell -Command "Write-Host '[4/6] %CURRENT_STEP%' -ForegroundColor Cyan"
echo [STEP] %CURRENT_STEP% >> "%LOGFILE%"
call "%D_PKG_WINDOWS%\ensure_uv_synced.cmd"
if errorlevel 1 (
    powershell -Command "Write-Host '❌ Failed: %CURRENT_STEP%' -ForegroundColor Red"
    echo ❌ Failed: %CURRENT_STEP% >> "%LOGFILE%"
    goto END
)

:: Step 5: Delete AutoRun key
echo ──────────────────────────────────────────────────────────
set "CURRENT_STEP=Deleting previous AutoRun key"
powershell -Command "Write-Host '[5/6] %CURRENT_STEP%' -ForegroundColor Yellow"
echo [STEP] %CURRENT_STEP% >> "%LOGFILE%"
reg delete "HKCU\Software\Microsoft\Command Processor" /v AutoRun /f >nul 2>&1

:: Step 6: Register pk_alias to AutoRun
echo ──────────────────────────────────────────────────────────
set "CURRENT_STEP=Registering pk_alias to AutoRun"
powershell -Command "Write-Host '[6/6] %CURRENT_STEP%' -ForegroundColor Cyan"
echo [STEP] %CURRENT_STEP% >> "%LOGFILE%"
reg add "HKCU\Software\Microsoft\Command Processor" /v AutoRun /t REG_SZ /d "\"%D_PKG_WINDOWS%\ensure_alias_enabled.cmd\"" /f
if errorlevel 1 (
    powershell -Command "Write-Host '❌ Failed: %CURRENT_STEP%' -ForegroundColor Red"
    echo ❌ Failed: %CURRENT_STEP% >> "%LOGFILE%"
    goto END
)

:: Step 7: Import token key
echo ──────────────────────────────────────────────────────────
set "CURRENT_STEP=Importing token key"
powershell -Command "Write-Host '[7/7] %CURRENT_STEP%' -ForegroundColor Cyan"
echo [STEP] %CURRENT_STEP% >> "%LOGFILE%"
call "%D_PKG_WINDOWS%\ensure_pk_token_key_enabled.cmd"
if errorlevel 1 (
    powershell -Command "Write-Host '❌ Failed: %CURRENT_STEP%' -ForegroundColor Red"
    echo ❌ Failed: %CURRENT_STEP% >> "%LOGFILE%"
    goto END
)

:: ✅ Completed
set "CURRENT_STEP=All steps completed successfully"
powershell -Command "Write-Host '✅ %CURRENT_STEP%' -ForegroundColor Green"
echo ✅ %CURRENT_STEP% >> "%LOGFILE%"

:END
pause
exit /b 0
