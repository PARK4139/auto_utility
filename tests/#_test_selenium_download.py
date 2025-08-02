"""
Selenium을 사용한 YouTube 직접 다운로드 테스트
"""

import sys
import os
import time
import requests

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.map_massages import PkMessages2025


def test_selenium_direct_download():
    """Selenium을 사용한 직접 다운로드 테스트"""
    ensure_printed(f"🧪 {PkMessages2025.SELENIUM_DIRECT_DOWNLOAD_TEST}", print_color="cyan")
    
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        # Chrome 옵션 설정
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--start-maximized")
        
        # 다운로드 경로 설정
        download_dir = r"C:\Users\wjdgn\Downloads\pk_working"
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        
        ensure_printed(f"🚀 {PkMessages2025.CHROME_BROWSER_STARTING}...", print_color="yellow")
        driver = webdriver.Chrome(options=chrome_options)
        
        try:
            # YouTube 비디오 페이지로 이동
            test_url = "https://www.youtube.com/watch?v=6jQOQQA7-eA"
            ensure_printed(f"📱 {PkMessages2025.YOUTUBE_PAGE_MOVING}: {test_url}", print_color="yellow")
            driver.get(test_url)
            
            # 페이지 로딩 대기
            time.sleep(5)
            
            # 현재 페이지 정보 확인
            title = driver.title
            ensure_printed(f"📄 {PkMessages2025.PAGE_TITLE}: {title}", print_color="cyan")
            
            # 나이 확인 버튼이 있는지 확인
            try:
                age_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'I'm 18 or older')]"))
                )
                ensure_printed(f"🔞 {PkMessages2025.AGE_VERIFICATION_BUTTON_FOUND}", print_color="yellow")
                age_button.click()
                ensure_printed(f"✅ {PkMessages2025.AGE_VERIFICATION_BUTTON_CLICKED}", print_color="green")
                time.sleep(3)
            except:
                ensure_printed(f"ℹ️ {PkMessages2025.AGE_VERIFICATION_BUTTON_NOT_FOUND}", print_color="cyan")
            
            # 비디오 플레이어 확인
            try:
                video_player = driver.find_element(By.TAG_NAME, "video")
                ensure_printed(f"🎬 {PkMessages2025.VIDEO_PLAYER_FOUND}", print_color="green")
                
                # 비디오 소스 URL 가져오기
                video_src = video_player.get_attribute("src")
                if video_src:
                    ensure_printed(f"🔗 {PkMessages2025.VIDEO_URL}: {video_src[:100]}...", print_color="cyan")
                else:
                    ensure_printed(f"⚠️ {PkMessages2025.VIDEO_URL_UNAVAILABLE}", print_color="yellow")
                    
            except Exception as e:
                ensure_printed(f"❌ {PkMessages2025.VIDEO_PLAYER_NOT_FOUND}: {e}", print_color="red")
            
            # 페이지 소스에서 비디오 URL 찾기
            page_source = driver.page_source
            ensure_printed(f"📊 {PkMessages2025.PAGE_SIZE}: {len(page_source)} bytes", print_color="cyan")
            
            # 잠시 대기 (사용자가 확인할 수 있도록)
            ensure_printed(f"⏳ {PkMessages2025.KEEPING_BROWSER_OPEN}...", print_color="yellow")
            time.sleep(10)
            
        finally:
            driver.quit()
            ensure_printed(f"🔒 {PkMessages2025.BROWSER_CLOSED}", print_color="green")
            
    except ImportError:
        ensure_printed(f"❌ {PkMessages2025.SELENIUM_NOT_INSTALLED}", print_color="red")
        ensure_printed(f"💡 {PkMessages2025.INSTALL_SELENIUM}", print_color="yellow")
    except Exception as e:
        ensure_printed(f"❌ {PkMessages2025.SELENIUM_TEST_FAILED}: {e}", print_color="red")


def test_requests_direct_download():
    """requests를 사용한 직접 다운로드 테스트"""
    ensure_printed(f"🧪 {PkMessages2025.REQUESTS_DIRECT_DOWNLOAD_TEST}", print_color="cyan")
    
    test_url = "https://www.youtube.com/watch?v=6jQOQQA7-eA"
    
    # YouTube 쿠키 파일 읽기
    cookies = {}
    if os.path.exists(r"pkg_txt/youtube_cookies.txt"):
        with open(r"pkg_txt/youtube_cookies.txt", 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('#') or not line.strip():
                    continue
                parts = line.strip().split('\t')
                if len(parts) >= 7:
                    domain = parts[0]
                    name = parts[5]
                    value = parts[6]
                    if '.youtube.com' in domain:
                        cookies[name] = value
        
        ensure_printed(f"🍪 {PkMessages2025.COOKIES_LOADED}: {len(cookies)}개", print_color="cyan")
    else:
        ensure_printed(f"⚠️ {PkMessages2025.COOKIE_FILE_MISSING}", print_color="yellow")
    
    # 헤더 설정
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        ensure_printed(f"📥 {PkMessages2025.YOUTUBE_PAGE_REQUEST}: {test_url}", print_color="yellow")
        response = requests.get(test_url, headers=headers, cookies=cookies, timeout=30)
        
        if response.status_code == 200:
            ensure_printed(f"✅ {PkMessages2025.PAGE_REQUEST_SUCCESS}", print_color="green")
            ensure_printed(f"📊 {PkMessages2025.RESPONSE_SIZE}: {len(response.text)} bytes", print_color="cyan")
            
            # 응답 내용에서 비디오 관련 정보 찾기
            content = response.text
            if "age restricted" in content.lower():
                ensure_printed(f"🔞 {PkMessages2025.AGE_RESTRICTED_CONTENT_DETECTED}", print_color="yellow")
            if "video" in content.lower():
                ensure_printed(f"🎬 {PkMessages2025.VIDEO_RELATED_CONTENT_FOUND}", print_color="green")
            
            # 응답 내용 저장
            output_file = r"C:\Users\wjdgn\Downloads\pk_working\youtube_page.html"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(response.text)
            ensure_printed(f"💾 {PkMessages2025.PAGE_CONTENT_SAVED}: {output_file}", print_color="cyan")
            
        else:
            ensure_printed(f"❌ {PkMessages2025.PAGE_REQUEST_FAILED}: {response.status_code}", print_color="red")
            
    except Exception as e:
        ensure_printed(f"❌ {PkMessages2025.REQUESTS_TEST_FAILED}: {e}", print_color="red")


def test_yt_dlp_force_download():
    """yt-dlp 강제 다운로드 테스트"""
    ensure_printed(f"🧪 {PkMessages2025.FORCE_DOWNLOAD_TEST}", print_color="cyan")
    
    test_url = "https://www.youtube.com/watch?v=6jQOQQA7-eA"
    output_dir = r"C:\Users\wjdgn\Downloads\pk_working"
    
    # 가장 강력한 옵션으로 테스트
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s [%(id)s].%(ext)s'),
        'cookiefile': r"pkg_txt/youtube_cookies.txt",
        'age_limit': 0,
        'no_check_age': True,
        'ignoreerrors': True,
        'quiet': False,
        'force_generic_extractor': True,  # 일반 추출기 강제 사용
        'extract_flat': False,
        'no_check_certificate': True,
        'prefer_insecure': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.youtube.com/',
        }
    }
    
    try:
        import yt_dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ensure_printed(f"📥 {PkMessages2025.FORCE_DOWNLOAD_START}: {test_url}", print_color="yellow")
            ydl.download([test_url])
            ensure_printed(f"✅ {PkMessages2025.FORCE_DOWNLOAD_COMPLETE}", print_color="green")
    except Exception as e:
        ensure_printed(f"❌ {PkMessages2025.FORCE_DOWNLOAD_FAILED}: {str(e)[:100]}", print_color="red")


def main():
    """메인 테스트 함수"""
    ensure_printed(f"🚀 {PkMessages2025.SELENIUM_TEST_START}", print_color="cyan")
    ensure_printed("=" * 60, print_color="white")
    
    # 1. requests 직접 다운로드 테스트
    test_requests_direct_download()
    ensure_printed("", print_color="white")
    
    # 2. yt-dlp 강제 다운로드 테스트
    test_yt_dlp_force_download()
    ensure_printed("", print_color="white")
    
    # 3. Selenium 직접 다운로드 테스트
    test_selenium_direct_download()
    
    ensure_printed("=" * 60, print_color="white")
    ensure_printed(f"🏁 {PkMessages2025.ALL_SELENIUM_TESTS_COMPLETE}", print_color="cyan")


if __name__ == "__main__":
    main() 