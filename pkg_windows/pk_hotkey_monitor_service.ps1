# PK System Hotkey Monitor Service (PowerShell)
# Windows 시작 프로그램으로 등록하여 백그라운드에서 단축키 모니터링

param(
    [string]$Hotkey = "ctrl+alt+p",
    [string]$ProjectPath = $env:D_PK_SYSTEM
)

# 프로젝트 경로 설정
if (-not $ProjectPath) {
    $ProjectPath = "C:\Users\wjdgn\Downloads\pk_system"
}

# 작업 디렉토리 변경
Set-Location $ProjectPath

Write-Host "🎯 PK System 단축키 모니터링 서비스 시작..." -ForegroundColor Green
Write-Host "💡 단축키: $Hotkey" -ForegroundColor Cyan
Write-Host "💡 종료하려면 Ctrl+C를 누르세요" -ForegroundColor Yellow
Write-Host ""

# Python 가상환경 경로
$PythonPath = Join-Path $ProjectPath ".venv\Scripts\python.exe"
$ScriptPath = Join-Path $ProjectPath "pkg_py\functions_split\ensure_hotkey_monitor_started.py"

# 스크립트 실행
try {
    & $PythonPath $ScriptPath $Hotkey
}
catch {
    Write-Host "❌ 모니터링 서비스 오류 발생: $_" -ForegroundColor Red
    Read-Host "계속하려면 Enter를 누르세요"
} 