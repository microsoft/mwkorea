---
title: "Copilot 캔버스 안에 진짜 앱을: SharePoint Copilot Apps 퍼블릭 프리뷰 공개"
date: 2026-07-09T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - SharePoint
  - SPFx
  - MCPApps
  - CopilotApps
  - Developer
  - PublicPreview
excerpt: "SharePoint Copilot Apps가 퍼블릭 프리뷰로 공개되었습니다. 채팅으로 텍스트를 주고받는 대신, 승인·인시던트 처리·온보딩 체크리스트 같은 업무를 실제 인터랙티브 앱으로 Copilot 캔버스 안에서 바로 완료할 수 있습니다. SPFx 1.24 프리뷰 기반이며 전 세계 사용자 대상 롤아웃은 2026년 7월 20일까지 완료될 예정입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 캔버스 안에 진짜 앱을: SharePoint Copilot Apps 퍼블릭 프리뷰 공개

드디어 공개되었습니다. 오늘부터 **SharePoint Copilot Apps가 퍼블릭 프리뷰**로 제공되며, 이는 Copilot이 사용자를 위해 할 수 있는 일의 범위를 근본적으로 바꿉니다. 지금까지는 작업을 처리하려면 채팅으로 주거니 받거니 설명을 해야 했다면, 이제는 비용 승인, 인시던트 트리아지(triage), 온보딩 체크리스트 같은 업무를 **텍스트 벽이 아니라 실제 인터랙티브 앱**으로 Copilot 캔버스 안에서 바로 처리할 수 있습니다.

핵심은 이것입니다. **거의 모든 인터랙티브 UX 컴포넌트를 캔버스에 직접 표면화**할 수 있습니다 — 필터링 가능한 데이터 그리드, 다단계 폼, 인터랙티브 지도, 실시간 차트와 KPI 대시보드, 스케줄러, 목적에 맞게 만든 승인 패널까지. 모두 완전히 인터랙티브하며, 팀이 이미 알고 있는 **웹 스택**으로 만들고, 새로운 플랫폼이나 호스팅을 구축할 필요가 없습니다. **웹에서 만들 수 있다면, Copilot 안으로 그대로 가져올 수 있습니다.**

![Copilot Apps 소개 슬라이드](/mwkorea/assets/images/2026-07-09-SharePointCopilotApps/image1.webp)

이는 Copilot의 다음 물결입니다. 더 나은 답변뿐 아니라, 사람들이 **의도(intent)에서 결과(outcome)로** 나아가도록 돕는 것 — 한쪽에는 자연어 추론이, 다른 한쪽에는 실제 안내형 경험과 비즈니스 액션이 자리합니다.

---

## 발표 개요

오늘 Microsoft는 **SharePoint Copilot Apps의 퍼블릭 프리뷰**를 발표했습니다. [SharePoint Framework(SPFx)](https://aka.ms/spfx) 1.24 프리뷰의 일부로 제공되며, 사용자가 Copilot 흐름을 벗어나지 않고도 업무를 검토·검증·결정·**완료**할 수 있도록 안내형·액션 지향적 경험을 Microsoft 365 Copilot 안으로 가져오는 새로운 방식입니다.

역할 구분은 단순합니다. **Copilot**은 사용자가 의도를 표현하고 맥락을 추론하도록 돕고, **SharePoint Copilot Apps**는 실제로 일을 완료시키는 UX·권한·검증·안정적인 운영을 제공합니다. 그리고 이를 만드는 방식은 업계 표준 웹 스택, **MCP Apps**, 그리고 검증된 SPFx 패키징 모델입니다 — **Microsoft 365 테넌트에 자동으로 호스팅**되므로 별도 인프라를 구축하거나 운영할 필요가 없습니다.

## 왜 중요한가

많은 엔터프라이즈 워크플로는 생성된 응답 하나로 끝날 수 없습니다. 승인, 업데이트, 제출, 라인 오브 비즈니스(line-of-business) 액션에는 구조, 책임성, 예측 가능한 실행이 필요합니다. SharePoint Copilot Apps는 자연어의 유연함과 거버넌스된 비즈니스 운영의 신뢰성을 연결합니다.

이는 다음과 같은 새로운 기회를 엽니다.

- **전환(Turn)**: 사용자 의도를 단순히 생성된 응답이 아니라 실제 비즈니스 결과로 바꿉니다.
- **결합(Combine)**: Copilot의 추론과 승인·업데이트·제출·검증·워크플로 액션 같은 신뢰할 수 있는 운영을 결합합니다.
- **향상(Increase)**: 액션을 취하기 *전에* 올바른 데이터, 선택지, 제약, 결과를 보여줌으로써 사용자의 확신을 높입니다.
- **감소(Reduce)**: 운영 경험을 별도 도구·포털로 보내는 대신 Copilot 안으로 가져와 컨텍스트 전환을 줄입니다.

### 여러분의 컴포넌트만 가져오면 됩니다

개발자가 반길 부분은 이것입니다. **여러분은 하나에만 집중하면 됩니다 — 바로 UX 컴포넌트. 나머지는 플랫폼이 처리합니다.** Microsoft 365가 호스팅, 도구 라우팅, 보안, 거버넌스를 자동으로 처리합니다. 따로 연결하거나 운영할 것이 없습니다. SPFx 1.24를 설치하면 오늘 오후에라도 테넌트에서 첫 앱을 실행할 수 있습니다.

독점 런타임이 아니라 **오픈 웹 표준** 위에 구축되었기 때문에, **여러분의 AI 코딩 에이전트는 이미 이런 컴포넌트를 만드는 법을 알고 있습니다.** GitHub Copilot, Claude, Codex 같은 도구가 팀이 이미 사용하는 JavaScript 스택으로 IDE 안에서 바로 이런 컴포넌트를 스캐폴딩·생성·리팩터링·디버깅할 수 있습니다.

### 한 번 작성하고, 어디서나 도달

동일한 UX 컴포넌트는 하나의 표면에만 묶이지 않습니다. **한 번 만들어서 Microsoft 365 전반 — Copilot, SharePoint, Microsoft Teams — 에 노출**할 수 있습니다. 사람들이 이미 일하고 있는 모든 곳에서 단일 컴포넌트를 재사용하는 것입니다. 기존 SPFx 투자는 다시 만들 필요 없이 그대로 이어집니다.

## 무엇을 만들 수 있나

SharePoint Copilot Apps는 사용자가 단순히 답을 얻는 것이 아니라 **결과를 완료해야** 할 때 빛을 발합니다 — 데이터를 검토하고, 결정을 내리고, 입력을 검증하고, 신뢰할 수 있는 액션을 실행하는 것입니다. 각 솔루션은 사용자 의도에 따라 표면화되는 **여러 인라인 경험과 여러 전체 화면 경험**을 렌더링할 수 있습니다.

**예시로는** 승인, 운영 대시보드, 인시던트 대응, 온보딩 어시스턴트, CRM 작업 창(task pane), 프로젝트 리뷰, 현장 운영, 근무일 허브(workday hub), 조달 요청, 지원 트리아지, 재무 업데이트, 그리고 파트너가 구축한 산업별 솔루션 등이 있습니다.

![SharePoint Copilot Apps 활용 시나리오](/mwkorea/assets/images/2026-07-09-SharePointCopilotApps/image2.webp)

**Work IQ**로 구동되는 **My Day** 시나리오는 사용자에게 개인화된 계획과 관련 맥락을 제공하는 실제 동작 예시입니다.

![My Day 시나리오 소개 화면](/mwkorea/assets/images/2026-07-09-SharePointCopilotApps/image3.webp)

### 실제 동작 확인: My Day 솔루션

{% include video id="VCkoAucaodw" provider="youtube" %}

데모를 보면 고객 가치가 명확해집니다. Copilot이 의도를 이해하고, 앱이 구조를 제공하며, 사용자는 Copilot 경험을 벗어나지 않고 결과를 완료합니다.

## 엔터프라이즈 개발자와 파트너를 위해 구축

SharePoint Copilot Apps는 SPFx와 **현대적인 웹 스택** — JavaScript, **TypeScript**, React(또는 Angular, Vue, Svelte 중 선택), **MCP Apps**, 그리고 이미 익숙한 도구들 — 위에 구축됩니다. 검증된 SPFx 모델로 **하나의 패키지**를 만들어 **Microsoft 365 테넌트 내에 배포**하면, Copilot·SharePoint·Teams 전반에서 재사용됩니다 — 핵심 상호작용 패턴을 다시 만들 필요도, 별도 호스팅을 운영할 필요도 없습니다.

그리고 이것은 검증되지 않은 기반이 아닙니다. SPFx 생태계는 이미 **매일 수천만 명의 최종 사용자**에게 서비스를 제공하고 있습니다. 이번 프리뷰는 그 설치 기반을 Copilot 캔버스로 그대로 확장하는 것입니다.

## 모든 개발자에게 열려 있습니다

퍼블릭 프리뷰 기간 동안, **전 세계 모든 Microsoft 365 테넌트의 모든 개발자가 Microsoft 365 Copilot 라이선스 없이도 SharePoint Copilot Apps를 만들 수 있습니다.** 이는 의도적으로 설계된 가장 낮은 진입 장벽입니다. 모든 지역의 고객, 파트너, MVP, ISV가 오늘 바로 시작할 수 있습니다. *(라이선스 정책은 정식 출시 전까지 변경될 수 있습니다.)*

## 퍼블릭 프리뷰: 고려사항과 제공 현황

시작하기 전에 알아두어야 할 몇 가지입니다.

- **오늘부터 빌드 가능**: Copilot Workbench와 전체 개발자 경험은 오늘부터 누구나 이용할 수 있습니다 — 지금 바로 SharePoint Copilot Apps를 만들고 테스트할 수 있습니다.
- **전 세계 순차 롤아웃 진행 중**: 최종 사용자 대상 제공은 전 세계적으로 순차 롤아웃되고 있으며, **2026년 7월 20일까지 전 세계에서 완전히 동작**할 예정입니다. 테넌트에서 아직 일부 기능이 보이지 않는다면 곧 제공될 예정입니다.
- **프리뷰 소프트웨어**: 이것은 퍼블릭 프리뷰입니다 — 기능, API, 그리고 "SharePoint Copilot Apps"라는 작업명 자체가 정식 출시 전까지 변경될 수 있습니다. 이 점을 감안해 빌드하고, 발견한 내용을 알려 주세요.

## 시작하기

**SPFx 1.24 프리뷰를 설치**하세요 — 지금 npm에서 이용 가능합니다.

- [SharePoint Framework v1.24.0 프리뷰 릴리스 노트](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/release-1.24.0)

실제 시나리오를 구축하는 개발자, 파트너, MVP, 엔터프라이즈 팀, ISV의 의견을 기다립니다. 프리뷰를 사용해 보고, 무엇이 잘 동작하는지 공유하며, 다음 단계를 함께 만들어 가시길 바랍니다. [SharePoint Framework 이슈 목록](https://aka.ms/spfx/issues)으로 의견을 보내 주시고, 매주 열리는 [커뮤니티 콜](https://aka.ms/community/calls)에 참여하시거나 LinkedIn과 X에서 최신 Microsoft 365 플랫폼 발표를 팔로우하세요.

### 더 자세한 내용과 문서

- [Going beyond text in Microsoft 365 Copilot: Introducing SharePoint Copilot Apps](https://devblogs.microsoft.com/microsoft365dev/going-beyond-text-in-microsoft-365-copilot-introducing-sharepoint-copilot-apps/) — 공식 발표
- [SharePoint Copilot Apps 개요 문서](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/copilot/overview-copilot-apps)
- [첫 SharePoint Copilot App 만들기 튜토리얼](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/copilot/get-started/build-your-first-copilot-app) — 문서
- [GitHub 샘플 저장소](https://github.com/pnp/spfx-copilot-apps) — 샘플 데이터가 포함된 4개 시나리오 샘플(데모용 sppkg 파일 포함)로 시작하며, 기여를 환영합니다

## 도입 관점 체크포인트

- SPFx 기반 자산을 이미 보유한 조직이라면, 기존 웹 파트를 Copilot Apps로 확장할 수 있는지 우선 검토
- 승인·인시던트 대응처럼 **감사 추적(audit trail)이 중요한 워크플로**부터 파일럿 대상으로 선정
- 프리뷰 기간 중 라이선스 정책이 변경될 수 있으므로, 정식 출시 시점의 라이선스 요구사항을 지속적으로 모니터링
- AI 코딩 에이전트(GitHub Copilot, Claude, Codex 등)를 활용한 컴포넌트 개발 워크플로를 사내 개발 표준에 반영할지 검토

## 마무리

SharePoint Copilot Apps는 Copilot을 "의도에서 신뢰할 수 있는 결과로" 이동하는 공간으로 만드는 중요한 한 걸음입니다. SPFx 위에 구축되고 현대적 웹 기술로 구동되며 Microsoft 365에 호스팅되는 이번 프리뷰는, 전 세계 고객·파트너·개발자에게 실제 비즈니스 운영을 Copilot 캔버스 안으로 가져올 실질적인 경로를 제공합니다.

사용자를 의도에서 결과로 이동시키세요. SPFx 1.24 프리뷰를 설치하세요. 오늘 첫 SharePoint Copilot App을 만들어 보세요.

---

> ※ "SharePoint Copilot Apps"는 퍼블릭 프리뷰 기간의 작업명이며, 정식 출시 전까지 변경될 수 있습니다.
>
> **원문**: [SharePoint Copilot Apps Now in Public Preview: From Intent to Action in Microsoft 365 Copilot (Microsoft 365 Developer Blog, 2026-07-09)](https://devblogs.microsoft.com/microsoft365dev/sharepoint-copilot-apps-now-in-public-preview-from-intent-to-action-in-microsoft-365-copilot/)
>
> 자세한 내용은 원문을 참조하세요.
