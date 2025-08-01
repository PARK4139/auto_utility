# Finance Investment Assistant - 개발 로드맵

## 🎯 다음 단계

### Phase 1: 핵심 API 구현 (우선순위)
1. **투자 타이밍 추천 로직** - 기술적 지표 기반 분석 알고리즘
2. **자산 가격 조회** - 외부 금융 API 연동 (Yahoo Finance, Alpha Vantage 등)
3. **뉴스 크롤링** - BeautifulSoup/Selenium을 활용한 뉴스 수집

### Phase 2: 고급 기능 구현
1. **머신러닝 모델** - 예측 알고리즘 및 감정 분석
2. **포트폴리오 최적화** - 자산 배분 및 리스크 관리
3. **실시간 알림** - WebSocket을 활용한 실시간 데이터 전송

### Phase 3: 프론트엔드 및 보안
1. **Django 웹 인터페이스** - 관리자 대시보드 및 사용자 인터페이스
2. **인증/인가 시스템** - JWT 토큰 기반 보안
3. **API 문서화** - 자동화된 API 문서 생성

### Phase 4: 운영 및 모니터링
1. **로깅 시스템** - 구조화된 로그 수집 및 분석
2. **모니터링 대시보드** - Prometheus + Grafana 연동
3. **CI/CD 파이프라인** - GitHub Actions를 활용한 자동 배포

## 📝 최신 작업 내용 (2025-08-01)

### ✅ 완료된 작업

#### 1. 🏗️ 코드베이스 구조 개선 - ensure_ 패턴 적용
- ✅ **API Gateway 리팩토링**: `main.py` → `ensure_app_started.py`
- ✅ **Investment Advisor 리팩토링**: 서비스 파일명 `ensure_` 패턴 적용
- ✅ **Market Data 리팩토링**: API 엔드포인트 구조화
- ✅ **News Analyzer 리팩토링**: 크롤러/분석기 모듈 분리

#### 2. 📁 일관된 디렉토리 구조 적용
- ✅ **API Layer**: `api/v1/` - API 엔드포인트 분리
- ✅ **Core Layer**: `core/` - 설정, 미들웨어 등 핵심 모듈
- ✅ **Services Layer**: `services/` - 비즈니스 로직
- ✅ **Utils Layer**: `utils/` - 공통 유틸리티
- ✅ **Models Layer**: `models/` - 데이터 모델
- ✅ **Providers Layer**: `providers/` - 외부 서비스 연동 (Market Data)
- ✅ **Crawlers Layer**: `crawlers/` - 웹 크롤링 (News Analyzer)
- ✅ **Analyzers Layer**: `analyzers/` - 분석 엔진 (News Analyzer)

#### 3. 🎯 ensure_ 네이밍 컨벤션 적용
- ✅ **파일명 패턴**: `ensure_[목적]_[동작].py`
- ✅ **함수명 패턴**: `ensure_[기능]_[동작]()`
- ✅ **명확한 의도 표현**: 파일명만 봐도 기능 파악 가능
- ✅ **일관성 유지**: 모든 서비스가 동일한 패턴 사용

#### 4. 🔧 실제 리팩토링 완료
- ✅ **API Gateway**: 4개 API 엔드포인트 분리
- ✅ **Investment Advisor**: 3개 API 엔드포인트 분리
- ✅ **Market Data**: 3개 API 엔드포인트 분리
- ✅ **News Analyzer**: 3개 API 엔드포인트 분리
- ✅ **Core 모듈**: 설정, 미들웨어, 로깅 모듈 분리
- ✅ **Utils 모듈**: 예외 처리, 유틸리티 함수 분리

#### 5. 📋 문서화 개선
- ✅ **NAMING_CONVENTION.md**: ensure_ 패턴 가이드라인
- ✅ **REFACTORING_EXAMPLES.md**: 실제 리팩토링 예시
- ✅ **API_VERSIONING.md**: API 버전 관리 전략
- ✅ **ARCHITECTURE.md**: 전체 아키텍처 문서

### 🎯 개선된 점

#### 1. **가독성 향상**
- 파일명만 봐도 기능을 알 수 있음
- `ensure_` 접두사로 목적이 명확함
- 일관된 구조로 코드 탐색이 쉬워짐

#### 2. **유지보수성 향상**
- 기능별로 명확히 분리
- 새로운 기능 추가 시 적절한 위치 파악 용이
- 코드 중복 최소화

#### 3. **확장성 개선**
- API 버전 관리 준비 완료 (`v1/`, `v2/`)
- 마이크로서비스 간 의존성 명확화
- 새로운 서비스 추가 시 템플릿 제공

#### 4. **개발 효율성 향상**
- 팀 전체가 이해하기 쉬운 구조
- 자동화된 문서 생성 가능
- 테스트 작성이 용이한 구조

## 📝 이전 작업 내용 (2024-01-XX)

### ✅ 완료된 작업

#### 1. MSA 환경 구축
- ✅ **Docker Compose**: 모든 마이크로서비스 컨테이너화
- ✅ **API Gateway**: FastAPI 기반 게이트웨이 구현
- ✅ **데이터베이스**: PostgreSQL + Redis 연결
- ✅ **Nginx**: 리버스 프록시 설정

#### 2. 의존성 관리 개선
- ✅ **pyproject.toml**: requirements.txt → pyproject.toml 마이그레이션
- ✅ **uv 도입**: pip → uv로 패키지 관리 개선
- ✅ **Python 호환성**: 3.8.1+ 버전 지원
- ✅ **Hatchling 설정**: 패키지 빌드 시스템 구성

#### 3. 개발 환경 통합
- ✅ **WSL + Windows**: "Windows에서 편집, WSL에서 실행" 방식
- ✅ **Docker 자동화**: 컨테이너 빌드 및 실행 자동화
- ✅ **API 테스트**: Swagger UI를 통한 실시간 테스트
- ✅ **네트워크 연결**: WSL IP를 통한 Windows 브라우저 접속

#### 4. 문제 해결
- ✅ **Python 버전 충돌**: flake8 호환성 문제 해결
- ✅ **Hatchling 패키지 경로**: 실제 디렉토리 구조 반영
- ✅ **의존성 충돌**: numpy/pandas 버전 호환성 해결
- ✅ **uv sync**: 자동 lock 파일 생성 및 의존성 해결 