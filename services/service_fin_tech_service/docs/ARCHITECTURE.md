# Finance Investment Assistant - Architecture Guide

## 🏗️ 개선된 프로젝트 구조

```
pkg_finance_invest_assist/
├── 📁 api_gateway/                 # API Gateway 서비스
│   ├── 📁 api/                     # API 라우터
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── recommend.py        # 투자 추천 API
│   │   │   ├── market.py           # 시장 데이터 API
│   │   │   ├── news.py             # 뉴스 분석 API
│   │   │   └── health.py           # 헬스체크 API
│   │   └── __init__.py
│   ├── 📁 core/                    # 핵심 설정
│   │   ├── __init__.py
│   │   ├── config.py               # 설정 관리
│   │   ├── security.py             # 보안 설정
│   │   └── middleware.py           # 미들웨어
│   ├── 📁 services/                # 비즈니스 로직
│   │   ├── __init__.py
│   │   ├── gateway_service.py      # 게이트웨이 서비스
│   │   └── proxy_service.py        # 프록시 서비스
│   ├── 📁 models/                  # 데이터 모델
│   │   ├── __init__.py
│   │   ├── request.py              # 요청 모델
│   │   └── response.py             # 응답 모델
│   ├── 📁 utils/                   # 유틸리티
│   │   ├── __init__.py
│   │   ├── logger.py               # 로깅
│   │   └── exceptions.py           # 예외 처리
│   ├── main.py                     # 애플리케이션 진입점
│   └── __init__.py
│
├── 📁 investment_advisor/           # 투자 추천 엔진
│   ├── 📁 api/                     # API 라우터
│   │   ├── __init__.py
│   │   ├── recommend.py            # 추천 API
│   │   └── health.py               # 헬스체크
│   ├── 📁 core/                    # 핵심 설정
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   ├── 📁 services/                # 비즈니스 로직
│   │   ├── __init__.py
│   │   ├── invest_timing.py        # 투자 타이밍 분석
│   │   ├── harvest_timing.py       # 회수 타이밍 분석
│   │   ├── technical_analysis.py   # 기술적 분석
│   │   └── risk_analysis.py        # 리스크 분석
│   ├── 📁 models/                  # 데이터 모델
│   │   ├── __init__.py
│   │   ├── schemas.py              # Pydantic 스키마
│   │   └── enums.py                # 열거형
│   ├── 📁 utils/                   # 유틸리티
│   │   ├── __init__.py
│   │   ├── indicators.py           # 기술적 지표
│   │   ├── calculations.py         # 계산 유틸리티
│   │   └── validators.py           # 데이터 검증
│   ├── main.py
│   └── __init__.py
│
├── 📁 market_data/                 # 시장 데이터 서비스
│   ├── 📁 api/                     # API 라우터
│   │   ├── __init__.py
│   │   ├── price.py                # 가격 API
│   │   ├── market.py               # 시장 데이터 API
│   │   └── health.py               # 헬스체크
│   ├── 📁 core/                    # 핵심 설정
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   ├── 📁 services/                # 비즈니스 로직
│   │   ├── __init__.py
│   │   ├── price_service.py        # 가격 서비스
│   │   ├── market_data_service.py  # 시장 데이터 서비스
│   │   ├── data_provider.py        # 데이터 제공자
│   │   └── cache_service.py        # 캐시 서비스
│   ├── 📁 models/                  # 데이터 모델
│   │   ├── __init__.py
│   │   ├── schemas.py
│   │   └── enums.py
│   ├── 📁 providers/               # 외부 API 제공자
│   │   ├── __init__.py
│   │   ├── yahoo_finance.py        # Yahoo Finance
│   │   ├── alpha_vantage.py        # Alpha Vantage
│   │   └── base_provider.py        # 기본 제공자
│   ├── 📁 utils/                   # 유틸리티
│   │   ├── __init__.py
│   │   ├── data_processor.py       # 데이터 처리
│   │   └── formatters.py           # 데이터 포맷터
│   ├── main.py
│   └── __init__.py
│
├── 📁 news_analyzer/               # 뉴스 분석 서비스
│   ├── 📁 api/                     # API 라우터
│   │   ├── __init__.py
│   │   ├── news.py                 # 뉴스 API
│   │   ├── analysis.py             # 분석 API
│   │   └── health.py               # 헬스체크
│   ├── 📁 core/                    # 핵심 설정
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   ├── 📁 services/                # 비즈니스 로직
│   │   ├── __init__.py
│   │   ├── crawler_service.py      # 크롤링 서비스
│   │   ├── analysis_service.py     # 분석 서비스
│   │   ├── sentiment_service.py    # 감정 분석
│   │   └── content_service.py      # 콘텐츠 서비스
│   ├── 📁 models/                  # 데이터 모델
│   │   ├── __init__.py
│   │   ├── schemas.py
│   │   └── enums.py
│   ├── 📁 crawlers/                # 크롤러
│   │   ├── __init__.py
│   │   ├── base_crawler.py         # 기본 크롤러
│   │   ├── news_crawler.py         # 뉴스 크롤러
│   │   └── finance_crawler.py      # 금융 크롤러
│   ├── 📁 analyzers/               # 분석기
│   │   ├── __init__.py
│   │   ├── sentiment_analyzer.py   # 감정 분석기
│   │   ├── keyword_analyzer.py     # 키워드 분석기
│   │   └── trend_analyzer.py       # 트렌드 분석기
│   ├── 📁 utils/                   # 유틸리티
│   │   ├── __init__.py
│   │   ├── text_processor.py       # 텍스트 처리
│   │   └── url_utils.py            # URL 유틸리티
│   ├── main.py
│   └── __init__.py
│
├── 📁 shared/                      # 공통 모듈
│   ├── 📁 core/                    # 공통 핵심
│   │   ├── __init__.py
│   │   ├── config.py               # 공통 설정
│   │   ├── database.py             # 데이터베이스 연결
│   │   ├── logging.py              # 로깅 설정
│   │   └── security.py             # 보안 설정
│   ├── 📁 models/                  # 공통 모델
│   │   ├── __init__.py
│   │   ├── base.py                 # 기본 모델
│   │   └── enums.py                # 공통 열거형
│   ├── 📁 utils/                   # 공통 유틸리티
│   │   ├── __init__.py
│   │   ├── decorators.py           # 데코레이터
│   │   ├── exceptions.py           # 예외 처리
│   │   ├── validators.py           # 검증 유틸리티
│   │   └── helpers.py              # 헬퍼 함수
│   ├── 📁 middleware/              # 공통 미들웨어
│   │   ├── __init__.py
│   │   ├── auth.py                 # 인증 미들웨어
│   │   ├── logging.py              # 로깅 미들웨어
│   │   └── cors.py                 # CORS 미들웨어
│   └── __init__.py
│
├── 📁 tests/                       # 테스트 코드
│   ├── 📁 unit/                    # 단위 테스트
│   │   ├── test_api_gateway/
│   │   ├── test_investment_advisor/
│   │   ├── test_market_data/
│   │   └── test_news_analyzer/
│   ├── 📁 integration/             # 통합 테스트
│   │   ├── test_api_integration.py
│   │   └── test_service_integration.py
│   ├── 📁 e2e/                     # E2E 테스트
│   │   └── test_end_to_end.py
│   ├── 📁 fixtures/                # 테스트 픽스처
│   │   ├── data.py
│   │   └── mocks.py
│   └── conftest.py                 # pytest 설정
│
├── 📁 deployment/                  # 배포 설정
│   ├── 📁 docker/                  # Docker 설정
│   │   ├── Dockerfile.api_gateway
│   │   ├── Dockerfile.investment_advisor
│   │   ├── Dockerfile.market_data
│   │   └── Dockerfile.news_analyzer
│   ├── 📁 nginx/                   # Nginx 설정
│   │   ├── nginx.conf
│   │   └── ssl/
│   ├── 📁 scripts/                 # 배포 스크립트
│   │   ├── deploy.sh
│   │   ├── deploy.bat
│   │   └── docker_uv_dev.sh
│   └── docker-compose.yml
│
├── 📁 docs/                        # 문서
│   ├── 📁 api/                     # API 문서
│   │   ├── api_gateway.md
│   │   ├── investment_advisor.md
│   │   ├── market_data.md
│   │   └── news_analyzer.md
│   ├── 📁 architecture/            # 아키텍처 문서
│   │   ├── overview.md
│   │   ├── data_flow.md
│   │   └── security.md
│   ├── 📁 development/             # 개발 가이드
│   │   ├── setup.md
│   │   ├── coding_standards.md
│   │   └── testing.md
│   └── 📁 deployment/              # 배포 가이드
│       ├── docker.md
│       └── production.md
│
├── 📁 scripts/                     # 유틸리티 스크립트
│   ├── setup_dev.sh                # 개발 환경 설정
│   ├── run_tests.sh                # 테스트 실행
│   ├── lint_code.sh                # 코드 린팅
│   └── format_code.sh              # 코드 포맷팅
│
├── pyproject.toml                  # 프로젝트 설정
├── README.md                       # 프로젝트 개요
├── ARCHITECTURE.md                 # 아키텍처 가이드 (이 파일)
└── CONTRIBUTING.md                 # 기여 가이드
```

## 🎯 개선 사항

### 1. 일관된 디렉토리 구조
- 모든 서비스가 동일한 구조를 따름
- `api/`, `core/`, `services/`, `models/`, `utils/` 패턴 통일
- 명확한 책임 분리

### 2. 계층별 분리
- **API Layer**: HTTP 요청/응답 처리
- **Service Layer**: 비즈니스 로직
- **Data Layer**: 데이터 접근 및 모델
- **Utility Layer**: 공통 유틸리티

### 3. 테스트 구조 개선
- 단위 테스트, 통합 테스트, E2E 테스트 분리
- 각 서비스별 테스트 디렉토리
- 공통 픽스처 및 모킹

### 4. 문서화 강화
- API 문서
- 아키텍처 문서
- 개발 가이드
- 배포 가이드

### 5. 공통 모듈 체계화
- 설정, 데이터베이스, 로깅 등 공통 기능
- 미들웨어 분리
- 유틸리티 함수 모듈화

## 🚀 구현 우선순위

### Phase 1: 구조 정리 (1-2주)
1. 디렉토리 구조 재구성
2. 공통 모듈 분리
3. 기본 테스트 구조 설정

### Phase 2: 코드 품질 향상 (2-3주)
1. 일관된 코딩 스타일 적용
2. 타입 힌트 추가
3. 문서화 개선

### Phase 3: 테스트 강화 (1-2주)
1. 단위 테스트 작성
2. 통합 테스트 구현
3. CI/CD 파이프라인 구축

이러한 구조 개선을 통해 코드의 가독성, 유지보수성, 확장성을 크게 향상시킬 수 있습니다. 