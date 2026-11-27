---
title: "에이전트를 찾지 않아도 뜨는 업무 화면: Copilot Cowork와 SPFx 플러그인"
date: 2026-11-24T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365
  - CopilotCowork
  - SPFx
  - Plugins
  - SharePoint
excerpt: "Copilot UX components를 플러그인으로 배포하면 일반 Copilot 채팅과 Cowork에서 사용자 요청에 맞는 업무 화면을 제공할 수 있습니다. SPFx의 현재 지원 범위, 중앙 관리 방식, 앞으로 공개될 SharePoint SPA 모델을 구분해 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트를 찾지 않아도 뜨는 업무 화면: Copilot Cowork와 SPFx 플러그인

직원에게 업무용 에이전트를 배포해도, 사용자가 어떤 에이전트를 열어야 하는지 모르면 활용이 어렵습니다. 휴가 승인이나 회의실 예약처럼 간단한 업무도 앱과 에이전트를 찾아다니는 단계에서 흐름이 끊길 수 있습니다.

Microsoft의 2026년 11월 24일 SPFx 로드맵 업데이트는 이 문제를 줄이는 변화를 소개합니다. **Copilot UX components를 플러그인으로 패키징하면 일반 Copilot 채팅과 Copilot Cowork에서 요청의 의도에 맞는 컴포넌트를 제공할 수 있습니다.** 사용자가 별도의 에이전트로 전환하지 않아도 되는 방식입니다.

이번 글에서는 이미 지원되는 플러그인 기능과 앞으로 예정된 SharePoint single page app(SPA) 모델을 나눠 설명합니다. 아래 버전과 일정은 원문 발표 시점의 정보이며, 계획을 현재 제공되는 기능으로 해석하면 안 됩니다.

---

## 새로운 점: 에이전트 중심에서 사용자 요청 중심으로

Copilot UX components는 SPFx 1.24가 공개된 10월 28일 정식 출시(GA)됐습니다. 기존 모델에서는 선언형 에이전트와 컴포넌트를 하나의 SPFx 솔루션으로 배포하고, 사용자가 해당 에이전트를 열면 대화 안에서 화면이 렌더링됩니다.

플러그인 방식은 컴포넌트와 skills 등 관련 자산을 함께 패키징합니다. 플러그인이 배포되고 해당 컨텍스트에서 활성화되면 Copilot이 요청 의도를 파악해 적절한 컴포넌트를 불러옵니다. 사용자에게 별도의 설치나 수동 에이전트 전환을 요구하지 않는 것이 핵심입니다.

이는 단순한 카드 표시 기능이 아닙니다. **실제로 동작하는 React와 JavaScript 컴포넌트**이므로 대시보드, 입력 폼, 상호작용 차트 등 개발자가 구현한 UX를 제공할 수 있습니다. 컴포넌트는 여전히 SPFx로 개발하고 조직의 Microsoft 365 테넌트에서 호스팅합니다.

## 데모로 보는 업무 활용 시나리오

{% include video id="EJskzYACUsA" provider="youtube" %}

원문 데모는 특정 에이전트에 연결되지 않은 일반 Copilot 채팅에서 시작합니다. 관리자가 회사 플러그인을 전 직원에게 중앙 배포한 상태에서 다음과 같은 경험을 보여줍니다.

| 요청 | 제공되는 업무 화면 |
|---|---|
| 오늘 무엇에 집중하면 좋을까? | 학습 정보, 우선순위 메일, Outlook 이동 기능을 포함한 개인 대시보드 |
| 승인 대기 중인 휴가 요청을 보여줘 | 대화 안에서 검토하고 승인하는 컴포넌트 |
| 회사 주가를 확인하고 싶어 | 지난주부터 지난 1년까지 확인하는 상호작용 차트 |
| 헬싱키 사무실 점심 메뉴는? | 요청에 포함된 지역을 반영한 메뉴 화면과 다른 지역 비교 |
| Johanna에게 칭찬을 보내고 싶어 | 해당 직원이 미리 선택된 인정·칭찬 컴포넌트 |
| 14시에 네 명이 쓸 방을 찾아줘 | 시간, 날짜, 인원, 프로필의 사무실 정보를 반영한 예약 화면 |

음성 입력과 전체 화면 모드도 데모에 포함됩니다. Cowork는 컴포넌트를 불러오는 동안 측면 패널에 어떤 플러그인이 자동 감지돼 사용됐는지 표시합니다.

한국 조직에서는 인사 승인, IT 지원, 출장·경비 처리, 사내 포털을 이런 모델로 설계할 수 있습니다. 다만 위 화면은 샘플의 구현 결과입니다. 플러그인 배포만으로 자사 업무 시스템과 자동 연결되는 것은 아니며, 백엔드 연동과 업무 로직은 솔루션에서 구현해야 합니다.

## 중앙 배포와 접근 제어는 기존 관리 도구로

플러그인은 Teams 앱, Copilot 에이전트, Office 추가 기능과 같은 Microsoft 365 앱 패키지 형식을 사용합니다. 관리자는 Microsoft 365 관리 센터의 **Agents > Tools**에서 대상을 관리합니다.

- 전체 조직 또는 특정 사용자·그룹에 배포할 수 있습니다. 배포된 플러그인은 자동으로 획득되므로 직원이 직접 찾아 설치할 필요가 없습니다.
- 사용 가능 범위를 전체 사용자 또는 선택한 사용자·보안 그룹으로 설정할 수 있습니다.
- 플러그인을 차단해 테넌트 내 사용을 막을 수 있습니다.

도입 담당자는 “누가 플러그인을 사용할 수 있는가”와 “그 사용자가 연결된 데이터에서 무엇을 읽고 실행할 수 있는가”를 함께 검토하는 편이 좋습니다. 중앙 배포는 사용자에게 경험을 전달하는 방법이지, 업무 데이터의 권한 검토를 대신하는 절차는 아닙니다.

관리 방법은 [Manage plugins for Copilot Cowork](https://learn.microsoft.com/en-us/copilot/cowork/cowork-manage-plugins)를 참고하세요.

## 개발 시작하기: 현재는 수동 패키징

원문 시점에는 플러그인 패키지를 **수동으로 제작**해야 합니다. SPFx 1.25에서 빌드 설정으로 플러그인 패키징을 선택하도록 지원하는 방안은 검토 중이며, 확정된 제공 기능으로 소개되지 않았습니다.

1. SPFx 기반 Copilot UX component를 구현합니다.
2. [수동 플러그인 패키징 문서](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/copilot/package-copilot-ux-component-as-plugin)에 따라 컴포넌트와 skills 등 자산을 구성합니다.
3. 관리 센터에서 대상 사용자·그룹에 배포하고 요청 의도에 맞게 화면이 나타나는지 확인합니다.

데모의 [Zava One Hub 샘플 플러그인 구성](https://github.com/pnp/spfx-copilot-components/tree/main/samples/zava-one-hub/zava-one-hub-plugin)도 참고할 수 있습니다. 원문은 사용자가 Microsoft Copilot 라이선스를 갖춰야 한다고 안내하므로, 실제 적용 전 대상 사용자와 클라이언트의 라이선스·지원 조건을 확인해야 합니다.

## 다음 변화: SharePoint 페이지 전체를 앱으로

![SPFx로 구현할 수 있는 포털과 업무 앱 화면 예시](/mwkorea/assets/images/2026-11-24-CopilotCoworkSPFxPlugins/image1.webp)

현재 SPFx 웹 파트는 SharePoint 페이지의 섹션 안에 들어갑니다. 예정된 SPA 모델은 **사이트의 첫 화면 전체를 SPFx 솔루션이 제어**하도록 합니다. 작은 업무 앱부터 몰입형 포털과 인트라넷 홈까지, 웹 파트 영역에 한정되지 않은 화면을 만들 수 있다는 의미입니다.

사이트 자체가 사라지는 것은 아닙니다. 문서 라이브러리, 목록, 권한, 공유, 검색 등 SharePoint 기능은 유지됩니다. 원문은 같은 경험을 Teams에 노출하거나 Copilot UX components를 통해 Copilot의 전체 화면으로 제공하는 방향도 설명합니다.

기술적으로는 다음 기반을 활용합니다.

![웹 파트 영역과 페이지 전체를 제어하는 SPA 모델 비교](/mwkorea/assets/images/2026-11-24-CopilotCoworkSPFxPlugins/image2.webp)

- SharePoint 목록·라이브러리를 저장소로 사용하고 권한, 버전 관리, 검색, Microsoft Purview 정책을 활용합니다.
- Microsoft Graph와 SharePoint API 외에 Entra ID로 보호되는 웹 API, Azure Functions, Dataverse 등과 연동할 수 있습니다.
- 로그인한 사용자를 대신하는 위임 권한으로 동작합니다. 초기에는 다른 SPFx 솔루션과 같은 API 권한·범위를 사용하며, 솔루션별 고유 Entra ID 앱 등록 지원은 검토 사항입니다.
- SPFx와 SharePoint의 호스팅·인증 기반을 활용합니다. 별도 호스팅 운영 부담은 줄지만, 직접 연결하는 외부 API의 구성과 운영까지 없어지는 것은 아닙니다.

**SPA 프리뷰는 SPFx 1.25, GA는 SPFx 1.26에서 제공하는 계획**입니다. 현재 플러그인 지원과 달리 아직 앞으로의 로드맵 항목입니다.

## 버전별 일정과 업그레이드 체크포인트

| 버전 | 원문 시점 상태 | 주요 내용 |
|---|---|---|
| 1.24 | 2026년 10월 28일 출시 | Copilot UX components GA, React 18.3.1, 기존 Node.js 22에 더해 24·26 지원, SharePoint Store 배포, 빌드 시 선언형 에이전트 검증·표시 모드 개선·동적 도구 검색 |
| 1.24.1 | 11월 2일 출시 | 기본 프로젝트 생성 시 안정 버전 패키지 참조, 보고된 npm 의존성 취약점 대응 |
| 1.24.2 | 11월 20일 출시 | React 18 이미지 도우미의 npm 설치 충돌과 pnpm 사용 시 TypeScript 빌드 실패 수정 |
| 1.25 | 2026년 12월~2027년 1월 계획 | SPA 프리뷰, SPFx CLI GA 및 Yeoman generator에서의 전환 계획, 플러그인 빌드 설정 검토 |
| 1.26 | 계획. 본문에는 날짜 미제시, 로드맵 이미지에는 2027년 2~3월 표기 | SPA GA, Copilot UX 경험 확장과 의존성·품질 개선 |

![SPFx 후속 버전 로드맵](/mwkorea/assets/images/2026-11-24-CopilotCoworkSPFxPlugins/image3.webp)

원문 본문과 이미지의 일정 표현에는 차이가 있습니다. 이미지의 SPFx 1.26 목표 시기는 확정 출시일이 아니라 계획으로 읽어야 합니다.

React 18 업그레이드 중 설치나 빌드 문제가 발생했다면 [SPFx 1.24.2 릴리스 노트](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/release-1.24.2)를 먼저 확인하세요. 원문은 SPFx Dev Skills v1.1.2가 SPFx 1.24.1과 React 18 마이그레이션을 반영했으며, **7개 에이전트·모델 조합에서 105회 평가**해 모든 조합의 업그레이드 품질을 개선했다고 소개합니다. 이것이 모든 실제 프로젝트의 업그레이드 성공을 보장하는 수치는 아닙니다.

모바일도 완료와 배포를 구분해야 합니다. Android·iOS 및 Teams 모바일의 Copilot UX components 지원은 변경 작업을 완료하고 프로덕션에 순차 배포 중이라고 설명합니다. SPFx Teams 기능과 컴포넌트를 함께 쓰는 솔루션의 자동 Sync to Teams는 후속 계획이므로, 그전에는 수동 Teams 패키지를 사용해야 합니다.

개발자 설문은 2026년 12월 2일까지 [SPFx feedback](https://aka.ms/spfx/feedback)에서 진행합니다. 더 장기적인 navigation customizers와 목록의 SPFx 기반 뷰는 탐색 중이며 목표 릴리스는 정해지지 않았습니다.

## 마무리

이번 업데이트의 실용적인 변화는 직원이 앱 이름을 기억하기보다 **업무를 말하면 필요한 화면이 나타나는 경험**에 있습니다. 지금은 플러그인의 수동 패키징과 중앙 배포를 바탕으로 좁은 업무 시나리오부터 구현하고, SharePoint SPA 모델은 별도의 프리뷰 계획으로 준비하는 것이 좋겠습니다.

> 출처: Microsoft 365 Developer Blog, [Copilot UX components now available in Cowork with plugins – SPFx roadmap update for November 2026](https://devblogs.microsoft.com/microsoft365dev/copilot-ux-components-now-available-in-cowork-with-plugins-spfx-roadmap-update-for-november-2026/). 자세한 내용은 원문 참조. 버전별 로드맵은 원문 발표 시점의 계획이며 변경될 수 있습니다.
