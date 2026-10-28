---
title: "Copilot 대화 안에서 휴가 신청과 승인까지: Copilot UX components 정식 출시"
date: 2026-10-28T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotUXComponents
  - SharePointFramework
  - SPFx
  - MCPApps
  - DeclarativeAgents
  - React
excerpt: "Copilot UX components가 SharePoint Framework 1.24와 함께 정식 출시됐습니다. 대화 안에서 대시보드와 업무 폼을 조작하는 방식, 라이선스·지원 클라이언트 조건, 테넌트 배포와 개발 시작 방법을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 대화 안에서 휴가 신청과 승인까지: Copilot UX components 정식 출시

Copilot에게 휴가 신청 방법을 물었는데 결국 인사 포털을 열어 날짜를 다시 입력해야 한다면, 대화는 업무의 출발점에 그칩니다. 매출 현황도 마찬가지입니다. 숫자 요약을 받은 뒤 조건을 바꿔 분석하려면 별도 대시보드로 이동해야 하죠.

Microsoft는 2026년 10월 28일 Microsoft 365 Developer Blog에서 **Copilot UX components의 정식 출시(GA)**를 발표했습니다. SharePoint Framework(SPFx) 1.24를 이용해 대시보드, 입력 폼, 승인 화면 같은 웹 UI를 Microsoft Copilot 캔버스에 넣는 기능입니다. 사용자는 대화의 맥락을 유지한 채 데이터를 살펴보고 다음 작업을 실행할 수 있습니다.

개발팀 입장에서는 기존 웹 기술과 업무 API를 활용하면서 Microsoft 365가 컴포넌트 호스팅을 맡는다는 점이 중요합니다. 다만 UI를 쉽게 배포하는 것과 업무 시스템의 권한·승인 설계를 생략하는 것은 다릅니다. 이번 발표에서 확인해야 할 지원 범위와 구현 책임을 함께 정리합니다.

![Copilot 에이전트와 UX components의 개념](/mwkorea/assets/images/2026-10-28-CopilotUXComponentsGA/image1.webp)

---

## 대답을 읽는 화면에서 업무를 처리하는 화면으로

Copilot UX component는 사용자의 요청에 맞춰 에이전트가 불러오는 대화형 웹 경험입니다. 예를 들어 분기 실적을 물으면 필터가 있는 매출 대시보드를 보여 주고, 휴가를 신청하면 잔여 일수·신청 날짜·제출 버튼을 한 화면에 배치할 수 있습니다. 원문이 제시한 활용 예이며, 모든 조직에 완성된 업무 기능이 기본 제공된다는 뜻은 아닙니다.

핵심은 **자연어로 업무를 찾는 단계와 실제로 처리하는 단계를 같은 흐름으로 연결하는 것**입니다. Copilot은 의도를 해석하고, 컴포넌트는 개발자가 연결한 시스템의 데이터와 조작 화면을 제공합니다.

![긴 텍스트 안내 대신 업무에 맞는 조작 화면을 제공하는 방식](/mwkorea/assets/images/2026-10-28-CopilotUXComponentsGA/image2.webp)

원문 데모: Copilot 안에서 동작하는 대화형 UI

{% include video id="BoPNG32cdoc" provider="youtube" %}

## 인라인과 전체 화면, 업무에 맞춰 선택

짧은 확인이나 간단한 입력은 대화 안의 **인라인 모드**로, 넓은 공간이 필요한 대시보드·다단계 폼·지도·상세 조회는 **전체 화면 모드**로 구성할 수 있습니다. 개발자는 컴포넌트가 지원할 모드와 각 모드에서 표시할 내용을 결정하며, Copilot의 밝은 테마와 어두운 테마에도 대응할 수 있습니다.

React뿐 아니라 TypeScript, 표준 JavaScript 라이브러리 등 익숙한 웹 기술을 사용할 수 있습니다. 원문의 예제가 주로 React를 사용하더라도 React가 필수 조건은 아닙니다. 기존 차트나 그리드, 사내 디자인 시스템을 활용할 여지도 있습니다.

![Copilot UX components의 인라인 및 전체 화면 경험](/mwkorea/assets/images/2026-10-28-CopilotUXComponentsGA/image3.webp)

## 업무 변경 전 확인 절차는 개발자가 설계해야 합니다

에이전트가 요청을 이해했다고 해서 곧바로 업무 시스템의 데이터를 바꾸도록 만들 필요는 없습니다. 원문은 중요한 변경을 보내기 전에 사용자가 내용을 검토하고 확인할 수 있도록 컴포넌트를 설계하라고 안내합니다.

역할을 나누면 구현 기준이 분명해집니다. Copilot은 요청에 맞는 컴포넌트를 찾고, 애플리케이션 코드는 데이터·선택지·입력 검증·실행 기능을 구현합니다. **검토와 확인 단계 역시 코드의 책임**입니다. 승인이나 제출처럼 결과가 남는 작업은 사용자가 무엇을 확정하는지 화면에서 이해할 수 있어야 합니다.

한국 조직에서 첫 도입 과제를 고른다면 기존 포털의 한 가지 업무를 대상으로 시작하는 편이 현실적입니다. 다음은 원문에 나온 활용 범위입니다.

| 업무 영역 | 구성할 수 있는 경험 |
|---|---|
| 현업 데이터 | 매출 현황, 고객 종합 조회, 재고, 경비, 급여 명세 |
| 직원 서비스 | 휴가 신청, 헬프데스크, 출장 예약, 온보딩, 직원 인정·포상 |
| 개인 업무 | 관련 뉴스, 최근 할 일, 하루 업무 대시보드 |
| 관리·거버넌스 | 사이트 생성, 정책 점검, 관리자 확인을 거치는 사이트 운영 |

기존 업무 규칙이나 API를 버리고 다시 만드는 접근은 아닙니다. 이미 운영하는 업무의 일부를 Copilot에서도 사용할 수 있게 연결하는 방식입니다. Microsoft는 기존 SPFx 솔루션 생태계가 전 세계 수만 개 조직에서 매일 수천만 명의 최종 사용자를 지원한다고 설명합니다. 이 수치는 새 UX components의 도입 실적이 아니라 **기존 SPFx 생태계의 규모**입니다.

![현업 데이터와 직원 서비스를 비롯한 업무 시나리오](/mwkorea/assets/images/2026-10-28-CopilotUXComponentsGA/image4.webp)

원문 데모: 텍스트 응답에서 대화형 업무 처리로 이어지는 경험

{% include video id="3wacPcqFuKw" provider="youtube" %}

## MCP Apps 기반 UI, 호스팅은 Microsoft 365에서

Copilot UX components는 대화형 UI를 위한 **Model Context Protocol(MCP) Apps 모델**을 사용합니다. 외부 호스팅 MCP App과 기반 모델은 같지만, 컴포넌트를 배포하고 운영하는 방식에 차이가 있습니다.

SPFx 솔루션 패키지를 고객 테넌트에 배포하면 플랫폼이 컴포넌트의 JavaScript와 CSS를 호스팅하고 Copilot 등록·라우팅을 처리합니다. 컴포넌트용 별도 웹 서버나 외부 엔드포인트를 직접 운영하는 부담을 줄이는 구조입니다.

| 검토 항목 | 외부 호스팅 MCP App | Copilot UX components |
|---|---|---|
| UI 호스팅·운영 | 웹 앱과 엔드포인트의 배포·확장·운영을 직접 담당 | Microsoft 365 테넌트에서 컴포넌트 호스팅 |
| 라우팅 | 엔드포인트 공개·보안·유지 관리 필요 | 플랫폼이 컴포넌트 등록과 라우팅 처리 |
| 사용자 인증 | 인증 체계 구현·유지 관리 필요 | 로그인한 사용자 권한을 사용하는 기본 SSO |
| 승인·거버넌스 | 외부 앱·서비스 검토 및 동의 필요 | SPFx 배포 모델 활용, 연결 API는 별도 권한·동의가 필요할 수 있음 |
| 데이터 연결 | 직접 운영하는 서비스를 거치는 구조 | UI 자산은 Microsoft 365에 호스팅되며 데이터 연결은 솔루션 설계에 따름 |

따라서 “테넌트에서 호스팅하므로 모든 데이터가 자동으로 테넌트 안에만 머문다”거나 “추가 API 권한 검토가 없다”고 해석하면 안 됩니다. **연결하는 업무 API의 권한·동의와 데이터 흐름은 여전히 설계·검토 대상**입니다.

![Microsoft 365가 컴포넌트 호스팅과 라우팅을 처리하는 구조](/mwkorea/assets/images/2026-10-28-CopilotUXComponentsGA/image5.webp)

## 같은 패키지를 여러 테넌트와 Microsoft 365 화면에 활용

개발·테스트·운영 테넌트로 같은 SPFx 패키지를 옮길 수 있고, 파트너나 ISV는 여러 고객에게 패키지 형태로 솔루션을 배포할 수 있습니다. 고객별 배포는 각 고객 테넌트의 거버넌스를 따릅니다. GA에서는 SharePoint Store를 통해 제공되는 SPFx 솔루션의 Copilot UX components도 지원합니다.

![여러 고객 테넌트에 같은 솔루션 패키지를 배포하는 모델](/mwkorea/assets/images/2026-10-28-CopilotUXComponentsGA/image6.webp)

웹 코드의 활용 범위도 Copilot에만 한정되지 않습니다. 업무 흐름에 맞춰 SharePoint 웹 파트, Teams 탭, Outlook 왼쪽 탐색에서 여는 전체 페이지 앱으로 재사용할 수 있다고 원문은 설명합니다. 각 화면에 맞는 구성은 필요하므로, 패키지 하나가 아무 설정 없이 모든 화면에 자동으로 나타난다는 의미는 아닙니다.

![Copilot, SharePoint, Teams, Outlook에서 웹 경험을 재사용하는 구상](/mwkorea/assets/images/2026-10-28-CopilotUXComponentsGA/image7.webp)

## GA 조건: 라이선스와 지원 클라이언트부터 확인하세요

다음은 **2026년 10월 28일 발표 기준**입니다. 정식 출시된 기능과 후속 계획을 구분해야 합니다.

| 항목 | GA에서 확인할 조건 |
|---|---|
| 제공 범위 | SPFx 1.24와 함께 전 세계 정식 출시 |
| 사용자 라이선스 | 원문 표현상 Microsoft Copilot 추가 기능(add-on) 라이선스 필요. 미보유 사용자는 컴포넌트 대신 라이선스 안내 메시지를 보게 됨 |
| 과금 | UX components 사용 자체에는 소비량 기반 요금이 없지만, Work IQ 같은 소비량 기반 API 호출에는 해당 API 요금이 발생할 수 있음 |
| 지원 클라이언트 | 브라우저·데스크톱의 Microsoft Copilot, 브라우저·데스크톱 Teams를 통한 Copilot |
| 패키징 | 선언형 에이전트와 UX components를 하나의 SPFx 솔루션에 함께 포함 |
| 스토어 | SharePoint Store에서 제공되는 SPFx 솔루션도 지원 |

**Android·iOS 모바일 지원, 새 Copilot plug-in 모델을 통한 패키징, Cowork 및 추가 Copilot 화면 지원은 후속 계획**입니다. 특히 특정 에이전트로 전환하지 않고 일반 Copilot 채팅에서 컴포넌트를 사용하는 경험은 새 플러그인 모델과 조직 설정에 관련된 계획이지, 이번 GA 전체에 이미 제공된다고 볼 수 없습니다.

원문은 SPFx 1.25를 2026년 12월 또는 2027년 1월로 계획하고 있다고 덧붙였습니다. 이는 발표 당시의 계획이며, 후속 기능 전체의 확정 출시일을 의미하지 않습니다.

## 개발팀이 알아둘 SPFx 1.24 변경점

SPFx 1.24는 UX components의 정식 지원 외에도 개발 환경과 빌드 동작을 바꿨습니다.

- 새 SPFx 솔루션은 **React 18.x**를 기본으로 사용합니다.
- SPFx 개발에 **Node.js 24와 Node.js 26**을 지원합니다.
- Copilot 캔버스의 기본 표시 모드 동작을 정비하고, Teams 매니페스트 버전을 자동 갱신해 컴포넌트 업데이트 시 버전 충돌을 줄입니다.
- 빌드 시 선언형 에이전트 매니페스트를 검증하며, 새 컴포넌트는 선언형 에이전트 매니페스트 **v1.8**로 생성합니다.
- 프리뷰 피드백 기반 수정과 npm audit 지적 사항에 대응한 업데이트를 포함합니다.

1.24 프리뷰로 만든 솔루션은 GA 버전으로 업데이트해야 합니다. 기존 솔루션을 React 18로 옮긴다면 서드파티 라이브러리 호환성과 동작을 함께 점검하세요. 구체적인 전환 경로는 [React 18 업그레이드 안내](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/react-18-upgrade)와 [SPFx 1.24 릴리스 노트](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/release-1.24.0)를 참조하면 됩니다.

## 시작하기: 샘플을 배포한 뒤 한 가지 업무로 좁혀 보기

원문은 먼저 테넌트에 배포 가능한 샘플을 체험하는 방법을 권합니다. [샘플 갤러리](https://aka.ms/SPFx/Copilot/Samples)에는 솔루션 패키지, 데모 데이터, 설정 단계가 포함돼 있습니다.

직접 개발할 때의 기본 흐름은 다음과 같습니다.

1. SPFx 1.24 개발 환경을 준비합니다. 원문이 제시한 생성기 설치 명령은 아래와 같습니다. `@latest`는 실행 시점에 따라 달라지므로 실제 설치 버전을 확인하세요.
2. 새 Copilot UX component를 생성하고 Minimal, No framework, React 중 템플릿을 선택합니다.
3. **Copilot Workbench**에서 로컬 실행·디버깅을 진행합니다. 인라인·전체 화면, 밝은·어두운 테마, 입력 속성별 동작을 확인합니다.
4. 솔루션 패키지를 테넌트에 배포하고 Copilot에서 사용하도록 구성합니다.

```shell
npm install @microsoft/generator-sharepoint@latest --global
```

코딩 에이전트로 프로젝트 생성이나 리팩터링을 도울 수 있지만, 업무 동작과 사용자 확인 절차의 책임은 개발팀에 남습니다. 파일럿 단계에서는 사용자 라이선스, 업무 API 권한·동의, 변경 전 확인 화면, 지원 클라이언트에서의 동작을 함께 점검하는 것이 좋습니다. 이는 원문의 조건을 바탕으로 정리한 도입 체크포인트입니다.

원문 영상: 샘플 갤러리 소개

{% include video id="nuXGCUpGscU" provider="youtube" %}

원문 영상: 첫 Copilot UX component 만들기

{% include video id="1TaK6osdvc0" provider="youtube" %}

개발 자료는 [시작 페이지](https://aka.ms/SPFx/Copilot), [공식 문서](https://aka.ms/SPFx/Copilot/docs), [첫 컴포넌트 만들기 튜토리얼](https://learn.microsoft.com/en-us/sharepoint/dev/spfx/copilot/get-started/build-your-first-copilot-app), [영상 모음](https://aka.ms/SPFx/Copilot/Videos)에서 확인할 수 있습니다. 이전 자료에서는 SharePoint Copilot Apps 또는 Copilot Components라는 이름이 쓰이기도 했지만, 이번 발표의 명칭은 Copilot UX components입니다.

## 마무리

이번 GA는 Copilot에 화면을 하나 더 붙이는 소식이라기보다, 사용자가 답을 받은 뒤 다른 포털에서 마무리하던 업무를 대화 안으로 가져올 수 있게 됐다는 점에서 의미가 있습니다. 기존 웹 개발 역량과 SPFx 배포 체계를 활용할 수 있어 이미 사내 포털을 운영하는 팀이라면 검토할 만합니다.

첫 과제는 작게 잡아도 됩니다. 자주 묻지만 결국 별도 사이트에서 끝내야 했던 업무 하나를 고르고, 조회부터 검토·확인까지 연결해 보세요. 호스팅 부담이 줄어든 만큼, 실제 업무에 맞는 화면과 안전한 실행 절차에 개발 시간을 쓸 수 있습니다.

---

> **출처**: Microsoft 365 Developer Blog, [Copilot UX components are generally available: bring interactive experiences into Copilot](https://devblogs.microsoft.com/microsoft365dev/copilot-ux-components-are-generally-available-bring-interactive-experiences-into-copilot/) — 2026년 10월 28일. 이 글은 원문 발표 시점의 기능·조건을 정리했습니다. 자세한 내용은 원문 참조.
