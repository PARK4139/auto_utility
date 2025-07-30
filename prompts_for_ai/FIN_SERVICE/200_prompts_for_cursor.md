# prompts_for_cursor.md

## 🎯 프로젝트 개요
나는 재테크에 필요한 정보(금융 뉴스, 자산 가격, 공공 금융 API 등)를 수집하여
투자자에게 유의미한 정보를 분석·추천해주는 핀테크 서비스를 만들고 있다.

서비스 구조는 Python 기반 MSA(Microservice Architecture)이며,
각 마이크로서비스는 FastAPI로, 웹 프론트는 Django로 구성된다.

---

## 📦 프로젝트 구조

모든 코드는 다음 디렉토리 아래에 구성되어 있다:

```
pkg_finance_invest_assist/
├── gateway/                 # FastAPI 기반 API Gateway
├── user-service/           # 사용자 인증/정보 처리
├── news-crawler/           # 뉴스 크롤링 서비스
├── finance-api-client/     # 공공 금융 API 연동
├── recommend-engine/       # 추천 기능 (투입/회수 시점 등)
├── django-web/             # Django 프론트엔드 (관리자/대시보드)
├── shared/                 # 공통 유틸: 로깅, DB, 인증, config
├── infra/                  # docker-compose, nginx, SSL 구성
├── scripts/                # 배포 자동화 스크립트
└── docs/                   # 명세, 설계 문서
```

---

## ⚙️ 기술 스택 및 환경

| 항목         | 내용 |
|--------------|------|
| 언어         | Python 3.11+
| 백엔드       | FastAPI
| 프론트엔드   | Django
| DB           | PostgreSQL (Docker 컨테이너로 EC2에서 운영)
| 가상환경     | `uv` 사용
| 배포         | AWS EC2 + Docker
| 통신         | HTTP 기반, 추후 HTTPS로 전환 예정

---

## ✅ 함수 작성 규칙

- 함수명은 항상 `ensure_`로 시작하고, **완료형 동사**를 접미사로 사용한다.
- 예:
  - `ensure_string_printed()`
  - `ensure_user_authenticated()`
  - `ensure_investing_timing_guided()`
  - `ensure_asset_price_fetched()`

---

## 📌 기능 예시

### recommmend_투입_timming
- `/recommend/invest-timing` (FastAPI)
- 자산명을 기반으로 현재가, 이동평균선 등을 분석하여 "지금 투자할 시점인지" 판단

### recommend_harvesting_timming
- `/recommend/harvest-timing` (FastAPI)
- 수익률, 고점 패턴, 경제 뉴스 기반으로 "지금 팔 시점인지" 판단

---

## 🔧 개발 스타일 가이드

- 설명은 **한국어**, 코드 및 주석은 **영어**로 작성
- Windows / Linux / WSL 모두에서 **호환되는 코드** 작성
- 코드 스타일은 명확하게 분리된 구조 선호:
  - `/main.py` : FastAPI 진입점
  - `/services/logic.py` : 기능 로직
  - `/models/schemas.py` : Pydantic 모델
  - `/database/session.py` : DB 연결
- `shared/` 모듈을 통해 logging, DB, 인증, config 등 재사용

---

## 📎 요청 예시

> `recommend-engine` 안에 `/recommend/invest-timing` 엔드포인트를 FastAPI로 만들어줘.  
> PostgreSQL에서 자산 가격을 조회해서 단순 이동평균 기반으로 "지금 투자할 타이밍인지" 추천해줘.  
> 로직은 `services/invest_timing.py`로 분리하고 함수명은 `ensure_investing_timing_guided()` 형식으로.