---
title: "Copilot 안의 대시보드와 업무 액션, SPFx의 다음 방향에 개발자 의견을 보태세요"
date: 2026-11-04T00:00:00 KST
categories:
  - Copilot
tags:
  - SPFx
  - CopilotUXComponents
  - SharePoint
  - Developer
excerpt: "Copilot UX components의 GA 이후 Microsoft가 SPFx 개발자 설문을 시작했습니다. SPFx 1.24의 React·Node.js 지원 변화와 향후 CLI 계획을 짚고 한국 개발팀이 의견을 정리할 포인트를 소개합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 안의 대시보드와 업무 액션, SPFx의 다음 방향에 개발자 의견을 보태세요

업무 에이전트의 결과가 항상 긴 텍스트일 필요는 없습니다. 대시보드, 입력 폼, 업무 액션이 대화 안에 들어오면 사용자가 결과를 확인하고 다음 단계로 넘어가는 방식도 달라집니다.

Microsoft는 Copilot UX components의 GA 이후 SPFx 개발자 설문을 열었습니다. 단순 만족도 조사만이 아니라 Microsoft 365 확장 개발의 다음 투자 우선순위를 정하기 위한 의견 수집입니다.

![SPFx 개발자 설문 안내](/mwkorea/assets/images/2026-11-04-SPFxDeveloperSurvey/image1.webp)

---

## Copilot 개발자에게 SPFx가 중요한 이유

원문은 SPFx를 Copilot, SharePoint, Teams, Viva Connections, Outlook 경험을 확장하는 pro-code 경로로 소개합니다. **Copilot UX components는 SPFx 1.24와 함께 2026년 10월 28일 GA**에 도달했습니다.

에이전트는 익숙한 웹 기술로 만든 대시보드·폼·비즈니스 액션을 Microsoft Copilot 대화에 제공할 수 있고, 호스팅은 Microsoft 365가 자동 처리한다고 설명합니다. 관련 내용은 [Copilot UX components 안내](https://aka.ms/spfx/copilot)에서 확인할 수 있습니다.

## 지난 1년의 변경 사항

| 버전·시점 | 원문이 강조한 내용 |
|---|---|
| SPFx 1.24 | React 기반 솔루션을 **React 18.3.1**로 전환, Node.js **22와 함께 24·26 지원** |
| SPFx 1.23, 2026년 5월 | 목록 보기 command set 개선, 오픈소스 SPFx CLI 프리뷰 |
| SPFx 1.22.2~1.24.1 | 보고된 npm 의존성 취약점 대응을 위한 유지관리 릴리스 |
| SPFx 1.24.1, 2026년 11월 2일 | 원문 시점의 최신 유지관리 릴리스 |

버전 지원과 CLI 상태를 혼동하지 않는 것이 중요합니다. 새 CLI의 GA는 이번 글의 완료 사항이 아니라 향후 계획에 포함됩니다.

## 설문 참여와 버그 신고는 구분

[SPFx 개발자 설문](https://aka.ms/spfx/feedback)은 **2026년 12월 2일 수요일까지** 열립니다. Copilot UX components뿐 아니라 웹 파트, 확장, Teams 앱과 Viva Connections 카드를 만드는 개발자도 대상입니다.

구체적인 버그나 기능 요청은 계속 [sp-dev-docs의 SPFx 이슈 목록](https://github.com/SharePoint/sp-dev-docs/issues)을 이용하도록 안내합니다. 설문은 개발 경험과 투자 방향에 대한 의견, 이슈 목록은 재현 가능한 문제와 요구사항 전달이라는 역할 차이가 있습니다.

## 앞으로의 계획과 한국 개발팀의 체크포인트

원문 시점 [SPFx 로드맵](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/roadmap)은 **SPFx 1.25를 2026년 12월~2027년 1월 목표**로 제시합니다. Copilot UX components 추가 발전과 오픈소스 CLI GA 등이 계획이며 일정은 바뀔 수 있습니다.

국내 개발팀은 기존 확장 솔루션의 런타임·React 전환 부담, 대화형 UI의 실제 업무 가치, 배포와 유지관리 경험을 구체적으로 정리해 의견을 보탤 수 있습니다. 매주 열리는 [커뮤니티 콜](https://aka.ms/community/calls)과 [데모 참여 신청](https://aka.ms/community/request/demo)도 별도의 참여 경로입니다.

> **출처**: [Your voice shapes SPFx: take our developer survey — Microsoft 365 Developer Blog](https://devblogs.microsoft.com/microsoft365dev/your-voice-shapes-spfx-take-our-developer-survey/). 자세한 내용은 원문 참조.
