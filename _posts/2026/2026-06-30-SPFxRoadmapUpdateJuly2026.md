---
title: "SPFx 로드맵 업데이트 (2026년 7월): SharePoint Copilot Apps 공식화와 1.23.2 출시"
date: 2026-06-30T00:00:00 KST
categories:
  - Copilot
tags:
  - SPFx
  - SharePoint
  - SharePointCopilotApps
  - Microsoft365Copilot
  - Roadmap
  - MCPApps
  - React18
excerpt: "2026년 6월 SPFx 로드맵의 최대 뉴스는 SharePoint Copilot Apps의 공식 발표입니다. 수백만 개발자가 매일 쓰는 SPFx 모델에 Copilot 연결형 AI 경험을 더하며, 품질 중심의 1.23.2도 함께 출시됐습니다. 1.24 공개 미리 보기는 7월, 정식 출시는 9월로 예정됐습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# SPFx 로드맵 업데이트 (2026년 7월): SharePoint Copilot Apps 공식화와 1.23.2 출시

2026년 6월은 최근 몇 년간의 [SharePoint Framework(SPFx)](https://aka.ms/spfx) 업데이트 중 가장 의미 있는 달로 기록될 만합니다. 5월이 SPFx 1.23 정식 출시로 '기반'을 다지는 시기였다면, 6월은 그 기반이 '다음'을 향하도록 방향을 잡는 달이기 때문입니다. 그 헤드라인은 바로 [SharePoint Copilot Apps](https://devblogs.microsoft.com/microsoft365dev/going-beyond-text-in-microsoft-365-copilot-introducing-sharepoint-copilot-apps/)의 공식 발표입니다.

SharePoint Copilot Apps는 수백만 개발자가 매일 빌드하는 바로 그 SPFx 모델에, **AI 우선(AI-first)·Copilot 연결형** 경험을 더하는 새로운 장(chapter)입니다. 그리고 이와 함께 품질에 집중한 **SPFx 1.23.2**도 출시되어, 향후 '새로 만들기/편집 패널 재정의' 기능을 위한 토대를 다졌습니다.

이번 로드맵은 여전히 **커뮤니티 주도**의 여정입니다. 봄 시즌 내내 이어진 이슈 제보, 오픈소스 기여, 커뮤니티 콜 참여, 피드백이 지금 발표하는 방향을 그대로 형성했습니다.

---

## SharePoint Copilot Apps 공식 발표 🎉

이번 달 최대 뉴스는 **SharePoint Copilot Apps**입니다. 개발자가 SharePoint 플랫폼 위에서 지능형·Copilot 연결형 경험을 직접 빌드하는 방식에 대한 비전으로, 그동안 AI·Copilot 관련해 예고해 온 방향이 구체적으로 형체를 갖춘 것입니다.

SharePoint Copilot Apps로 개발자는 다음을 할 수 있습니다.

- **기본적으로 Copilot 준비 완료(Copilot-ready by default)** — 데이터와 액션을 Microsoft 365 Copilot에 노출
- **기존 SPFx 역량·도구·투자 재사용** — AI 기반 시나리오에 더 빠르게 도달
- **비즈니스 데이터와 사용자 경험을 지능형 워크플로로 연결** — SharePoint, Teams, Viva 전반에서
- **앱의 도달 범위 확장** — 사용자가 이미 일하는 곳으로, Copilot을 일급(first-class) 표면으로

> 참고: "SharePoint Copilot Apps"는 공개 미리 보기 동안의 작업 명칭이며, 정식 출시 전에 변경될 수 있습니다.

아래는 곧 공개될 SharePoint Copilot Apps로 만들 수 있는 것을 보여 주는 소개 영상입니다. "My Day"는 만들 수 있는 시나리오의 한 예시입니다.

{% include video id="VCkoAucaodw" provider="youtube" %}

공개 미리 보기는 **2026년 7월** 시작, 정식 출시는 **2026년 하반기**가 목표입니다. 더 자세한 내용은 다음 자료에서 확인할 수 있습니다.

- [Going beyond text in Microsoft 365 Copilot – Introducing SharePoint Copilot Apps](https://devblogs.microsoft.com/microsoft365dev/going-beyond-text-in-microsoft-365-copilot-introducing-sharepoint-copilot-apps/) (블로그)
- [Introducing SharePoint Copilot Apps](https://www.youtube.com/watch?v=mpSVo47LDHE) (영상)
- [Introduction to SharePoint Copilot Apps developer experience](https://www.youtube.com/watch?v=ofgERb5Zlbo) (영상)

---

## SPFx 1.23.2 출시

1.23 정식 출시(GA) 이정표에 이어, **SPFx 1.23.2**가 출시됐습니다. 품질·안정성, 그리고 다음 확장성 기능을 위한 준비에 집중한 의도적으로 '좁은' 릴리스입니다.

주요 내용은 다음과 같습니다.

- **이슈 수정 및 플랫폼 품질**: 제보된 이슈들을 해결해 엔터프라이즈 규모에서 솔루션 안정성 강화
- **새로 만들기/편집 패널 재정의 준비**: 목록·라이브러리의 새로 만들기/편집 패널을 재정의(override)할 수 있도록 하는 기반 작업(서버 측 지원은 7월 예정)
- **보안·의존성 위생**: npm audit 취약점 이슈를 해결해 빌드 파이프라인을 깨끗하게 유지

자세한 내용은 [SharePoint Framework 1.23.2 릴리스 노트](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/release-1.23.2)를 참고하세요.

---

## 앞으로의 방향 — AI, Copilot, 그리고 향후 투자 💡

SharePoint Copilot Apps가 발표되면서, SPFx의 투자 방향은 그 어느 때보다 명확히 **AI 기반 솔루션과 지능형 경험**에 초점이 맞춰졌습니다. 로드맵 투자는 다음에 집중합니다.

- **Copilot 준비형·AI 강화 애플리케이션** 빌드 지원
- Microsoft 365 데이터·서비스와의 **통합 단순화**
- 개발을 가속하는 **더 유연하고 현대적인 도구** 제공
- 확장성을 통한 **실제 비즈니스 시나리오 확대**

SPFx는 이제 단순한 개발 모델을 넘어, **AI 시대의 지능형·엔터프라이즈급 솔루션**을 위한 핵심 기반으로 진화하고 있습니다.

---

## 로드맵 📅

SPFx는 예측 가능한 분기 중심 릴리스 주기로 계속 진화하고 있습니다. 현재 계획된 투자는 다음과 같습니다.

| 버전 | 시점 | 주요 내용 |
|------|------|-----------|
| **1.23.2** | 2026년 6월 (출시됨) | 이슈 수정·품질 개선, 새로 만들기/편집 패널 재정의 준비(서버 측 7월), npm 취약점 대응 |
| **1.24 공개 미리 보기** | 2026년 7월 | SharePoint Copilot Apps 공개 미리 보기, npm 취약점 대응 |
| **1.24 정식 출시(GA)** | 2026년 9월 | SharePoint Copilot Apps GA, SPFx CLI GA(오픈소스 템플릿 갱신 포함), 내비게이션 커스터마이저, npm 취약점 대응 |

> 로드맵 항목은 현재 계획이며 개발 진행과 고객 피드백에 따라 변경될 수 있습니다.

### 최우선 관심 항목 (Top of mind)

- **SPFx 솔루션의 React 18 지원**: 기본 제공 웹 파트를 React 18 수준으로 업데이트하는 작업이 진행 중입니다. 이 작업이 완료되어야 전면 활성화가 가능하며, 그전까지는 커스텀 웹 파트에 적용됩니다. 현재 내부 진행 상황 기준으로 **SPFx 1.24 GA** 무렵 지원될 전망입니다.

![SPFx 2026년 6월 로드맵](/mwkorea/assets/images/2026-06-30-SPFxRoadmapUpdateJuly2026/image1.webp)

---

## 무엇이 다음인가 (What's next)

Microsoft는 SharePoint 플랫폼을 계속 확장하고 있습니다.

- **SharePoint Framework(SPFx)**: 풍부하고 AI 기반이며 비즈니스 통합형인 솔루션을, Microsoft 365 안에서 커스텀 UI로 빌드 — 이제 **SharePoint Copilot Apps** 포함
- **SharePoint Embedded**: Microsoft 365 외부에서 호스팅하는 자체 앱에 SharePoint 콘텐츠를 자체 UI로 통합
- **Agents and AI**: 콘텐츠·비즈니스 정보에 효율적으로 접근하는 지능형·적응형 경험을 만들고, 최종 사용자에게 쉽게 노출

Copilot·Microsoft 365·Power Platform 경험을 빌드할 계획이라면 [Microsoft 365 & Power Platform 커뮤니티](https://aka.ms/community/home) 활동과 커뮤니티 콜 참여를 권장합니다.

> 참고: 여름 시즌으로 7월 말 로드맵 업데이트는 건너뛰고 8월 말에 돌아옵니다. 그동안 피드백은 GitHub·커뮤니티 콜·소셜 미디어로 계속 받습니다.

---

## 한국 개발자를 위한 시사점

- **인트라넷 자산의 Copilot 확장 경로**: 이미 구축한 SPFx 웹 파트·컴포넌트를 SharePoint Copilot Apps로 재사용해 Copilot 표면까지 확장할 수 있습니다. 국내 대기업·공공의 방대한 인트라넷 투자에 특히 유리합니다.
- **일정 체크**: 1.24 공개 미리 보기(7월)와 GA(9월) 일정을 기준으로 PoC·도입 계획을 세우면 좋습니다.
- **React 18 준비**: 기본 웹 파트의 React 18 전면 지원은 1.24 GA 무렵으로 예상되므로, 커스텀 웹 파트부터 단계적으로 점검하세요.
- **품질 기반 업그레이드**: 1.23.2는 품질·보안 중심 릴리스이므로, npm audit 대응과 안정성 관점에서 업그레이드 가치를 검토할 만합니다.

---

> **원문**: [SharePoint Framework (SPFx) roadmap update – July 2026 (Microsoft 365 Developer Blog)](https://devblogs.microsoft.com/microsoft365dev/sharepoint-framework-spfx-roadmap-update-july-2026/) · 자세한 내용은 원문을 참조하세요.