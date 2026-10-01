---
title: "Copilot UX 컴포넌트, 2026년 10월 정식 출시 확정 — SPFx 9월 로드맵 업데이트"
date: 2026-10-01T00:00:00 KST
categories:
  - Copilot
tags:
  - SharePointFramework
  - SPFx
  - CopilotUXComponents
  - Microsoft365Copilot
  - React
excerpt: "Microsoft 365 Copilot 대화 안에서 차트·폼·승인 화면을 직접 렌더링하는 Copilot UX 컴포넌트가 2026년 10월 전 세계 모든 고객 대상으로 정식 출시됩니다. SPFx 9월 로드맵 업데이트를 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot UX 컴포넌트, 2026년 10월 정식 출시 확정 — SPFx 9월 로드맵 업데이트

몇 달 전만 해도 작업 중인 이름(working name)으로 불리던 기능이 이제 최종 이름을 갖추고, 모든 테넌트에 배포되어 있으며, 샘플만으로 몇 분 안에 체험할 수 있는 단계까지 왔습니다. Microsoft 365 Developer Blog가 공개한 **SharePoint Framework(SPFx) 9월 로드맵 업데이트**는 **Copilot UX 컴포넌트(Copilot UX components)**가 2026년 10월 전 세계 모든 고객 대상으로 정식 출시(GA)된다는 소식을 전합니다.

이번 글은 해당 원문을 기준으로 정리하며, 자세한 내용은 원문을 참조하시기 바랍니다.

---

## 텍스트의 벽을 넘어서는 Copilot UX 컴포넌트

이번 분기 로드맵의 핵심은 한 문장으로 요약됩니다.

> *"AI for intent. UX for action. Humans in control."*

사용자가 "이번 분기 매출 보여줘"라고 물으면 탐색 가능한 **라이브 차트**가, "휴가 신청해줘"라고 하면 **날짜를 검토하고 제출하는 폼**이 대화 안에서 바로 뜹니다. 별도 시스템으로 링크를 타고 나갈 필요가 없습니다.

![Copilot UX 컴포넌트의 인라인·전체화면 표시 모드](/mwkorea/assets/images/2026-10-01-SPFxCopilotUXComponents/image1.webp)

Copilot UX 컴포넌트는 에이전트가 차트, 지도, KPI, 폼, 승인 화면, 실시간 비즈니스 데이터를 Microsoft 365 Copilot 캔버스 안에 직접 렌더링하도록 해줍니다. 상황에 따라 **인라인(inline)**으로 짧게 표시되거나, 더 많은 공간이 필요하면 **전체 화면(full screen)**으로 확장됩니다.

{% include video id="BoPNG32cdoc" provider="youtube" %}

### 사람이 결정을 내리는 구조

에이전트는 요청을 해석하고 다음 단계를 제안하는 데 뛰어나지만, 승인·주문 확인·제출 전 데이터 수정처럼 업무에서 정말 중요한 순간에는 사람이 통제권을 쥐어야 합니다. Copilot UX 컴포넌트는 이런 순간을 위한 전용 UI를 제공합니다.

1. **Copilot이 의도를 이해**합니다 — 사용자가 자연어로 요청하면 에이전트가 필요한 것을 파악합니다.
2. **컴포넌트가 사실을 보여줍니다** — 생성된 텍스트가 아니라, 여러분의 코드가 렌더링하는 결정론적이고 정확한 비즈니스 데이터와 선택지입니다.
3. **사람이 결정합니다** — 사용자가 검토·조정·확인하면, 그 동작은 여러분의 솔루션이 호출하는 API를 통해 비즈니스 시스템으로 전달됩니다.

### 이미 알고 있는 기술 위에 구축

- 이미 운영 중인 SPFx 호스팅 모델에 그대로 배포되므로 새 인프라가 필요 없습니다.
- 로그인한 사용자의 권한을 사용하는 **클라이언트 측 SSO·보안**이 내장되어 있습니다.
- **React·표준 JavaScript 라이브러리**, MCP Apps 모델을 구현하되 호스팅·라우팅 작업 부담은 없습니다.
- 표준 SPFx 솔루션 패키지이므로 **한 번 빌드해 여러 테넌트에 배포**할 수 있습니다.
- Minimal/No framework/React 템플릿과 **Copilot Workbench**로 로컬 테스트가 가능합니다.

## 어떤 시나리오에 쓸 수 있나요?

지금 웹 파트나 포털 페이지로 존재하는 시나리오라면 무엇이든 Copilot UX 컴포넌트 후보가 될 수 있습니다.

- 매출 대시보드, 고객 360도 뷰, 재고, 경비, 급여명세서 같은 **기간계 데이터**
- 휴가 신청, 헬프데스크, 출장 예약, 온보딩 업무 같은 **직원 서비스**
- 최신 뉴스·업무·하루 일정을 보여주는 **개인 대시보드**
- 사이트 프로비저닝, 정책 점검, 사이트 대시보드 같은 **거버넌스·운영** (관리자가 각 단계를 확인)

![Copilot UX 컴포넌트 활용 시나리오 예시](/mwkorea/assets/images/2026-10-01-SPFxCopilotUXComponents/image2.webp)

## 2026년 10월 정식 출시 — 모든 고객 대상

목표는 **SharePoint Framework 1.24**와 함께 2026년 10월 Copilot UX 컴포넌트를 모든 고객 대상 정식 출시(GA)하는 것입니다. 정식 출시 전까지는 다음과 같습니다.

- 프리뷰는 전 세계 모든 테넌트에서 별도 링·가입·허용 목록 없이 활성화돼 있습니다.
- 프리뷰 기간 중 개발·테스트에 **Microsoft 365 Copilot 라이선스가 필요 없고**, 사용량 기반 비용도 없습니다.
- GA 시점 라이선스 정책은 아직 확정되지 않았으며, 확정되는 대로 공유할 예정입니다.

### 코드 없이도 몇 분 만에 체험

[시나리오 샘플](https://aka.ms/spfx/copilot/samples)에는 바로 배포 가능한 솔루션 패키지, 데모 데이터, 설정 안내가 포함돼 있어 어떤 Microsoft 365 테넌트에서든 몇 분 안에 체험할 수 있습니다.

{% include video id="4asOZi4PNUQ" provider="youtube" %}

직접 만들려면 네 단계만 거치면 됩니다.

```
npm install @microsoft/generator-sharepoint@next --global
```

1. SPFx 1.24 프리뷰를 설치합니다 (위 명령).
2. Minimal, No framework, React 템플릿 중 하나로 새 Copilot UX 컴포넌트를 스캐폴딩합니다.
3. **Copilot Workbench**에서 로컬로 실행·테스트합니다.
4. 테넌트에 배포하고 Copilot에 노출합니다.

참고 자료: [문서](https://aka.ms/SPFx/Copilot/docs) · [샘플 갤러리](https://aka.ms/spfx/copilot/samples) · [영상](https://aka.ms/SPFx/Copilot/Videos) · [SPFx 1.24 릴리스 노트](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/release-1.24.0)

### 비즈니스 가치를 확인하고 싶다면

{% include video id="3wacPcqFuKw" provider="youtube" %}

위 영상은 동일한 공개 샘플을 기반으로 한 엔드투엔드 비즈니스 시나리오 워크스루로, 사용자가 무엇을 보고 무엇을 대체하며 왜 중요한지를 보여줍니다. 테넌트에서 직접 재현하고 비즈니스에 맞게 조정할 수 있습니다.

### 공식 명칭: Copilot UX components

이 기능은 6월에 "SharePoint Copilot Apps", 8월에는 "Copilot Components"라는 작업명으로 소개된 바 있습니다. 최종 이름은 **Copilot UX components**이며, 앞으로 문서·템플릿·샘플에서 이 이름으로 표기됩니다. 과거 이름이 쓰인 콘텐츠를 보더라도 동일한 기능입니다.

## 프리뷰 프로그램: 폭발적 관심으로 마감

9월 업데이트에서 소개된 핸즈온 프리뷰 프로그램은 전 세계 고객·파트너의 관심이 지원 가능한 규모를 훌쩍 넘어서면서 **신규 신청을 마감**했습니다. 선정된 참가자들과 실제 비즈니스 시나리오로 협업 중이며, 신청했지만 선정되지 못한 경우에도 Copilot UX 컴포넌트는 이미 테넌트에서 사용 가능하고 샘플도 공개돼 있습니다.

## SharePoint Framework 1.24 현황

9월에는 **베타 4(9월 17일)**, **베타 5(9월 23일)**가 출시됐습니다(베타 4의 작은 문제는 베타 5에서 해결). 다음은 **릴리스 후보(RC)**이며, 10월에 정식 출시됩니다.

1.24 프리뷰의 주요 변경 사항:

- Copilot 캔버스 내 컴포넌트의 **예측 가능한 기본 표시 모드**
- 컴포넌트 업데이트 시 Teams 매니페스트 핫픽스 버전 자동 증가로 **버전 충돌 제거**
- **빌드 타임 선언적 에이전트 매니페스트 검증** — 런타임이 아닌 빌드 시점에 문제 발견
- 선언적 에이전트 매니페스트 v1.8로 스캐폴딩되는 신규 컴포넌트

자세한 내용은 [SharePoint Framework 1.24 릴리스 노트](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/release-1.24.0)를 참조하세요.

## React 18 및 Node.js 플랫폼 업데이트

- **React 18**이 SharePoint Framework 1.24의 기본 React 버전이 됩니다. 1.24 프리뷰에서 이미 사용 가능하며 1.24 GA와 함께 출시됩니다. 더 엄격해진 렌더링 동작, 빌드·번들링·타입 정의 이슈, React 18과 아직 호환되지 않는 서드파티 컴포넌트 라이브러리 등을 미리 테스트해 보고 [sp-dev-docs 이슈 목록](https://aka.ms/spfx/issues)으로 공유해 달라고 안내합니다.
- **Node.js 24 및 Node.js 26 지원**이 1.24 릴리스 후보에 포함되어 GA에 함께 반영될 예정입니다.

## 로드맵

| 버전 | 시기 | 상태 |
|---|---|---|
| 1.23.2 | 2026년 6월 | 출시 완료 |
| 1.24 Beta 5 | 2026년 9월 | 출시 완료 — Copilot UX 컴포넌트 프리뷰 업데이트, React 18 지원 |
| 1.24 GA | 2026년 10월 | 예정 — Copilot UX 컴포넌트 정식 출시, React 18, Node.js 24/26 |
| 1.25 | 2026년 12월 ~ 2027년 1월 | 예정 — Copilot UX 컴포넌트 모델 고도화, SPFx CLI GA(Yeoman 생성기 대체), 내비게이션 커스터마이저 |

![SharePoint Framework 분기별 로드맵](/mwkorea/assets/images/2026-10-01-SPFxCopilotUXComponents/image3.webp)

> 로드맵 항목은 현재 계획을 나타내며 개발 진행과 고객 피드백에 따라 변경될 수 있습니다.

## 당장 챙겨야 할 것들

- **GA 시점 라이선스 정책** — 확정되는 대로 공지 예정이므로 예산 계획에 영향이 있는 조직은 추적이 필요합니다.
- **Node.js 24/26 지원** — 1.24 GA에 반영됩니다.
- **React 18 업그레이드 가이드** — 1.24로 이전하는 솔루션을 위한 공통 업그레이드 경로·서드파티 라이브러리 고려사항 가이드가 공개될 예정입니다.
- **더 많은 곳에서의 Copilot UX 컴포넌트** — Teams, Cowork, Word, Excel, PowerPoint, Outlook의 Copilot까지 확장될 예정입니다.

## 참고로 함께 보면 좋은 소식

- **Copilot in SharePoint**가 정식 출시(GA)되어 2026년 9월 30일부터 롤아웃이 시작됐습니다. 자세한 내용은 ["SharePoint AI innovations hit GA, powering new Copilot app and agents"](https://aka.ms/CopilotinSP/blog/GA)를 참고하세요.
- SharePoint Embedded, Copilot Studio 등 Microsoft 365 전반의 에이전트·AI 확장 소식은 [커뮤니티 콜](https://aka.ms/community/home)에서 계속 공유됩니다.

## 마무리

Copilot UX 컴포넌트는 "AI가 의도를 이해하고, UI가 행동을 담당하며, 사람이 결정한다"는 구조로 에이전트를 데모 단계에서 실제 업무 프로세스로 끌어올리려는 시도입니다. SPFx를 이미 다루고 있는 조직이라면 10월 GA 전에 샘플 갤러리부터 체험해 보는 것을 추천합니다.

> 출처: **SharePoint Framework (SPFx) roadmap update – September 2026**
> 원문: https://devblogs.microsoft.com/microsoft365dev/sharepoint-framework-spfx-roadmap-update-september-2026/
> 자세한 내용은 원문 참조
