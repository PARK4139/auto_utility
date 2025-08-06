# Smart Person AI

현명한 사람들의 AI - AI 산출물 공급 서비스

## 프로젝트 개요

**Smart Person AI**는 AI를 모르는 사람들과 AI 공부가 귀찮은 사람들을 위한 AI 산출물 공급 서비스입니다.

### 핵심 가치 제안
- **마차를 끄는 마차시대의 현명한 마부는 자동차시대가 되자 자동차의 운전수가 되었다**
- **AI 시대의 현명한 사람들은 AI 사용자가 될 것을 나는 믿는다**

## 서비스 라인업

### AI 콘텐츠 제품
- AI 이미지 모음집 (Stable Diffusion 산출물, 12시간 단위 업데이트)
- AI 동화책 모음집 (Claude Sonnet 4 산출물)

### 자동화 도구
- AI 일반사무업무 자동화툴 (엑셀파일 병합/폴더 생성)
- AI 서비스 물품 자동업로더
- AI 웹크롤러 (미국주가/주식뉴스)
- AI 유튜브 다운로더 (주식뉴스)

## 기술 스택

### 🌐 하이브리드 프론트엔드 아키텍처
- **마케팅 사이트**: Astro 4.0 + TypeScript (hyeonsa-ai.com)
- **웹 애플리케이션**: Next.js 15 + React 19 + TypeScript (app.hyeonsa-ai.com)
- **백엔드**: FastAPI + Python 3.12+ (api.hyeonsa-ai.com)

### 🛠️ 상세 기술 스택
- **AI APIs**: Claude Sonnet 4, Stable Diffusion, Cursor API
- **Database**: PostgreSQL, Redis, MongoDB
- **Infrastructure**: Docker, AWS EC2 + Nvidia AGX Xavier, Nginx
- **Monitoring**: Prometheus + Grafana (자체 구현)
- **CI/CD**: GitHub Actions (자체 구현)
- **Load Testing**: K6/JMeter (자체 구현)

## 아키텍처

### 🏗️ 하이브리드 시스템 구조

```
🌍 현사AI 생태계
┌─────────────────────────────────────────────────────────────┐
│                    사용자 인터페이스                          │
├─────────────────────────────────────────────────────────────┤
│  📱 마케팅 사이트 (Astro 4.0)   │   🖥️ 웹 애플리케이션 (Next.js 15) │
│  hyeonsa-ai.com                │   app.hyeonsa-ai.com           │
│  ┌─────────────────────────┐   │   ┌─────────────────────────┐   │
│  │ 🏠 랜딩페이지             │   │   │ 📊 사용자 대시보드         │   │
│  │ 💰 가격표               │   │   │ 🤖 AI 생성 도구          │   │
│  │ 📦 제품 카탈로그          │   │   │ 💳 결제 관리            │   │
│  │ 📝 블로그/교육           │   │   │ ⚙️ 설정                 │   │
│  │ 📞 고객 지원             │   │   │ 📈 사용량 분석           │   │
│  └─────────────────────────┘   │   └─────────────────────────┘   │
├─────────────────────────────────────────────────────────────┤
│                    🔌 API Gateway (Kong/AWS)                 │
├─────────────────────────────────────────────────────────────┤
│            🐍 백엔드 서비스 (FastAPI + Python)                │
│   🤖 AI Services   💳 Payment   👤 User   📊 Analytics      │
└─────────────────────────────────────────────────────────────┘
```

### 📱 마케팅 사이트 (Astro 4.0)
**도메인**: hyeonsa-ai.com
- **성능 최적화**: Islands Architecture로 3-5배 빠른 로딩
- **SEO 완벽**: 정적 생성으로 검색엔진 최적화
- **콘텐츠 관리**: MDX + Content Collections
- **멀티 프레임워크**: Astro + React Islands

**주요 페이지**:
- 🏠 `/` - 랜딩페이지 (현명한 사람들의 AI)
- 💰 `/pricing` - 구독 요금제 (기본 5,555원/월)
- 📦 `/products/*` - AI 산출물 카탈로그
- 📝 `/blog/*` - 블로그 및 교육 콘텐츠
- 📞 `/contact` - 고객 지원 및 상담
- 🔗 `/app` → app.hyeonsa-ai.com 리다이렉트

### 🖥️ 웹 애플리케이션 (Next.js 15)
**도메인**: app.hyeonsa-ai.com
- **Server Components**: React 19 최신 기능
- **실시간 기능**: WebSocket + SSE
- **상태 관리**: Zustand + TanStack Query
- **UI 컴포넌트**: shadcn/ui v2

**주요 기능**:
- 🔐 `/auth` - 로그인/회원가입 (NextAuth.js)
- 📊 `/dashboard` - 사용자 대시보드
- 🤖 `/generate` - AI 생성 도구
  - 이미지 생성 (Stable Diffusion)
  - 동화책 생성 (Claude Sonnet 4)
  - 사무 자동화 (Cursor + Claude)
- 📁 `/library` - 내 AI 산출물 라이브러리
- 💳 `/billing` - 구독 및 결제 관리
- ⚙️ `/settings` - 계정 설정
- 🛠️ `/admin` - 관리자 패널

### 🐍 백엔드 서비스 (FastAPI)
**도메인**: api.hyeonsa-ai.com

**Domain-driven MSA 구조**:
- **AI Content Domain**: 이미지, 동화책, 자동화 도구 생성
- **Custom Pipeline Domain**: 맞춤형 AI 파이프라인 (500만원/건)
- **Customer Domain**: 사용자 관리, 구독, 세그멘테이션
- **Billing Domain**: 결제, 구독 관리, 사용량 과금
- **Education Domain**: 교육 콘텐츠, 진도 관리
- **Support Domain**: A/S, 기술 지원 (월 50만원)

**컨테이너 구조 (SDR 기반)**:
- **Public Service Container**: 공개 서비스 (포트 8000-8099)
- **Public Database Container**: PostgreSQL + Redis
- **Private Service Container**: 인증 필요 서비스 (포트 8100-8199)
- **Private Database Container**: PostgreSQL + MongoDB + Elasticsearch

## 개발 로드맵

### 🚀 Phase 1 - 하이브리드 아키텍처 구축 (진행 중)
- [x] 백엔드 MSA 구조 설정 (FastAPI)
- [ ] 마케팅 사이트 구축 (Astro 4.0 + TypeScript)
- [ ] 웹 애플리케이션 구축 (Next.js 15 + React 19 + TypeScript)
- [ ] 도메인 라우팅 설정 (hyeonsa-ai.com, app.hyeonsa-ai.com)
- [ ] 서비스 간 통합 (Cross-domain 인증/통신)

### 🎯 Phase 2 - 핵심 AI 서비스 (2-3개월)
- [ ] AI 이미지 생성 서비스 (Stable Diffusion, 12시간 업데이트)
- [ ] AI 동화책 생성 서비스 (Claude Sonnet 4)
- [ ] 사무 자동화 도구 (Cursor + Claude, 엑셀 병합/폴더 생성)
- [ ] 웹크롤러 서비스 (미국주가, 주식뉴스)
- [ ] 유튜브 다운로더 (주식뉴스)

### 💳 Phase 3 - 비즈니스 시스템 (3-4개월)
- [ ] 구독 시스템 (기본 5,555원/월, 프리미엄 15,555원/월)
- [ ] 결제 시스템 (토스페이먼츠 + Stripe)
- [ ] 사용량 기반 과금 시스템
- [ ] 고객 관리 시스템 (세그멘테이션)
- [ ] 커스텀 AI 파이프라인 주문 시스템 (500만원/건)

### 🔧 Phase 4 - 운영 시스템 (4-5개월)
- [ ] 모니터링 시스템 (Prometheus + Grafana, 자체 구현)
- [ ] CI/CD 파이프라인 (GitHub Actions, 자체 구현)
- [ ] 로드 테스트 시스템 (K6/JMeter, 자체 구현)
- [ ] 백업 자동화 (데이터베이스 백업)
- [ ] Services Controller (외부 컨테이너 제어)

### 🌍 Phase 5 - 확장 및 최적화 (5-6개월)
- [ ] AWS + Nvidia AGX Xavier 하이브리드 배포
- [ ] A/S 시스템 (1달 무료, 월 50만원)
- [ ] 교육 시스템 (업무 파이프라인 제작법)
- [ ] 성능 최적화 및 스케일링
- [ ] 목표 달성: 월 2,000명 × 5,555원 = 1,110만원 매출

## 🚀 개발 환경 설정

### 📁 프로젝트 구조 (하이브리드)
```
hyeonsa-ai-hybrid/
├── 📁 packages/
│   ├── 📁 marketing-site/          # Astro 4.0 마케팅 사이트
│   │   ├── src/pages/
│   │   │   ├── index.astro         # 랜딩페이지
│   │   │   ├── pricing.astro       # 가격표
│   │   │   ├── products/           # AI 산출물 카탈로그
│   │   │   ├── blog/              # 블로그/교육
│   │   │   └── contact.astro       # 고객 지원
│   │   ├── src/components/
│   │   │   ├── astro/             # 정적 컴포넌트
│   │   │   └── react/             # 인터랙티브 Islands
│   │   └── astro.config.mjs
│   │
│   ├── 📁 web-app/                # Next.js 15 웹 애플리케이션
│   │   ├── src/app/
│   │   │   ├── (auth)/            # 인증 페이지
│   │   │   ├── (dashboard)/       # 대시보드
│   │   │   ├── (admin)/           # 관리자
│   │   │   └── api/               # API Routes
│   │   ├── src/components/
│   │   │   ├── ui/                # shadcn/ui
│   │   │   ├── ai/                # AI 생성 도구
│   │   │   └── billing/           # 결제 관리
│   │   └── next.config.mjs
│   │
│   └── 📁 shared/                 # 공유 라이브러리
│       ├── types/                 # TypeScript 타입
│       ├── components/            # 공통 컴포넌트
│       └── api/                   # API 클라이언트
│
├── 📁 backend/                    # FastAPI 백엔드 (기존)
│   └── smart_person_ai/
│
├── package.json                   # Monorepo 루트
├── pnpm-workspace.yaml           # pnpm 워크스페이스
└── turbo.json                    # Turborepo 설정
```

### 🛠️ 개발 환경 구축

#### 1. 프론트엔드 설정 (Monorepo)
```bash
# 프로젝트 루트에서
npm install -g pnpm turbo

# 마케팅 사이트 (Astro 4.0)
cd packages/marketing-site
npm create astro@latest . --template=blog --typescript
npx astro add react tailwind

# 웹 애플리케이션 (Next.js 15)
cd packages/web-app
npx create-next-app@latest . --typescript --tailwind --app
npm install zustand @tanstack/react-query next-auth

# 공유 라이브러리
cd packages/shared
npm init -y
npm install typescript @types/node
```

#### 2. 백엔드 설정 (기존)
```bash
cd backend/smart_person_ai
pip install uv
uv sync

# 환경 설정
cp shared/env.example .env
# API 키들 설정: CLAUDE_API_KEY, STABLE_DIFFUSION_API_KEY 등
```

### 🚀 개발 서버 실행

#### 전체 개발 환경 시작
```bash
# 루트에서 모든 서비스 시작
pnpm dev  # Turborepo로 병렬 실행

# 개별 서비스 시작
pnpm dev:marketing  # http://localhost:4321 (Astro)
pnpm dev:webapp     # http://localhost:3000 (Next.js)

# 백엔드 서비스
cd backend && python tests/start_services.py  # 포트 8000+
```

#### 도메인별 접속
```bash
# 개발 환경 URL
마케팅 사이트: http://localhost:4321
웹 애플리케이션: http://localhost:3000
API 서버: http://localhost:8000

# 프로덕션 URL (예정)
마케팅 사이트: https://hyeonsa-ai.com
웹 애플리케이션: https://app.hyeonsa-ai.com
API 서버: https://api.hyeonsa-ai.com
```

### 🔧 SDR 기반 컨테이너 제어

#### Services Controller 사용
```bash
# 컨테이너 제어 API
curl -X POST http://localhost:8080/control \
  -H "Content-Type: application/json" \
  -d '{
    "service_name": "public-services",
    "action": "start",
    "options": {"build": true}
  }'

# 헬스 체크
curl http://localhost:8080/health

# 시스템 상태 모니터링
http://localhost:9090  # Prometheus
http://localhost:3000  # Grafana
```

### 📊 서비스 엔드포인트

#### 마케팅 사이트 (Astro)
- **홈페이지**: http://localhost:4321/
- **가격표**: http://localhost:4321/pricing
- **제품 카탈로그**: http://localhost:4321/products
- **블로그**: http://localhost:4321/blog

#### 웹 애플리케이션 (Next.js)
- **대시보드**: http://localhost:3000/dashboard
- **AI 생성**: http://localhost:3000/generate
- **라이브러리**: http://localhost:3000/library
- **결제 관리**: http://localhost:3000/billing

#### 백엔드 API (FastAPI)
- **API Gateway**: http://localhost:8000
- **API 문서**: http://localhost:8000/docs
- **헬스 체크**: http://localhost:8000/health
- **AI 이미지**: http://localhost:8001
- **AI 동화책**: http://localhost:8002

## 라이선스

MIT License