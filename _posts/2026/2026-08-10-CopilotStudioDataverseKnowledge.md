---
title: "Dataverse가 Copilot Studio의 네이티브 지식 소스가 됩니다"
date: 2026-08-10T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Dataverse
  - KnowledgeSource
  - Grounding
  - PowerPlatform
  - Roadmap
excerpt: "Microsoft Dataverse가 Copilot Studio의 네이티브 지식 소스로 추가됩니다. 레코드, 고객 데이터, 운영 데이터, 비즈니스 애플리케이션 콘텐츠를 에이전트의 신뢰할 수 있는 근거로 활용할 수 있게 됩니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Dataverse가 Copilot Studio의 네이티브 지식 소스가 됩니다

Power Platform을 쓰는 조직에게 **Dataverse**는 사실상 업무 데이터의 중심입니다. Power Apps로 만든 업무 앱, Dynamics 365의 고객 정보, 각종 업무 프로세스 데이터가 그곳에 모입니다.

그런데 Copilot Studio로 에이전트를 만들 때는 그 데이터를 활용하기가 생각만큼 매끄럽지 않았습니다. 커넥터를 붙이고 액션을 정의하는 방식은 가능했지만, **지식 소스(Knowledge Source)로서 자연스럽게 그라운딩**하는 경로는 별개의 문제였습니다.

Microsoft가 이 간극을 메웁니다. **Microsoft Dataverse를 Copilot Studio의 네이티브 지식 소스로** 제공하는 기능이 로드맵에 올랐습니다.

---

## 무엇이 새로워지나요

Microsoft가 밝힌 내용을 정리하면 다음과 같습니다.

> Microsoft Dataverse를 Copilot Studio의 **네이티브 지식 소스(native knowledge source)**로 활성화하여, **구조화된 엔터프라이즈 데이터에 AI 에이전트를 그라운딩**하는 플랫폼의 역량을 확장합니다.

활용할 수 있는 데이터 유형으로 다음이 명시되어 있습니다.

- **레코드(records)**
- **고객 데이터(customer data)**
- **운영 데이터(operational data)**
- **비즈니스 애플리케이션 콘텐츠(business application content)**

이 정보들을 에이전트 경험을 위한 **신뢰할 수 있는 지식 소스(trusted knowledge source)**로 삼을 수 있게 됩니다.

---

## Azure SQL 지원과 함께 보면

며칠 전 Copilot Studio에 **Azure SQL Knowledge Source**가 로드맵에 오른 바 있습니다(RM568930). 그리고 이번에는 Dataverse입니다. 두 건을 나란히 놓으면 방향이 분명해집니다.

| 지식 소스 | Preview | GA |
|---|---|---|
| **Azure SQL** (RM568930) | 2026년 8월 | 2026년 9월 |
| **Dataverse** (RM568929) | 2026년 8월 | 2026년 9월 |

Microsoft가 Azure SQL 발표에서 언급했던 **"통합 지식 플랫폼 전략(unified knowledge platform strategy)"**이 실제로 진행되고 있음을 보여 줍니다. 문서 같은 비정형 데이터뿐 아니라 **정형 엔터프라이즈 데이터를 공통 지식 프레임워크로 끌어들이는** 흐름입니다.

특히 국내에서 Power Platform 도입이 활발한 조직이라면, **이미 Dataverse에 쌓아 둔 데이터를 별도 개발 없이 에이전트에 연결**할 수 있다는 점이 실질적인 이점입니다.

---

## 활용 시나리오

### 1. 사내 업무 앱 데이터 조회 에이전트

Power Apps로 만든 업무 앱의 데이터를 자연어로 조회합니다. "지난달 접수된 시설 수리 요청 중 미처리 건이 몇 건이야?" 같은 질문에 답하는 에이전트를 만들 수 있습니다.

### 2. 고객 정보 기반 응대 지원

Dynamics 365의 고객 레코드를 지식 소스로 삼아, 상담원이 고객 이력과 계약 상태를 자연어로 확인합니다.

### 3. 운영 현황 브리핑

운영 데이터를 근거로 정기 현황을 요약해 주는 에이전트를 구성합니다.

### 4. 정책 문서 + 실데이터 결합

SharePoint의 사내 규정 문서와 Dataverse의 실제 레코드를 함께 지식 소스로 두면, **"규정은 이렇고, 현재 이 건의 상태는 이렇습니다"** 형태의 답변이 가능해집니다. 여러 지식 소스를 조합할 수 있다는 점이 통합 지식 플랫폼 전략의 핵심 가치입니다.

### 5. 신규 직원 온보딩 지원

업무 프로세스 데이터와 문서를 함께 참조해 "이런 경우엔 어떻게 처리하나요?"에 답하는 에이전트를 만듭니다.

---

## 일정

| 항목 | 내용 |
|---|---|
| 대상 제품 | Microsoft Copilot Studio |
| 미리 보기(Preview) | **2026년 8월(CY2026 August)** |
| 정식 출시(GA) | **2026년 9월(CY2026 September)** 예정 |

미리 보기가 이번 달이고 GA까지 간격이 짧습니다. 검증을 서두르실 만합니다.

실제 출시 일정·기능은 변경될 수 있습니다.

---

## 도입 체크포인트

Dataverse는 특히 **권한 모델이 정교한** 데이터 저장소이므로, 다음 항목을 반드시 확인하셔야 합니다.

- **보안 역할·행 수준 보안 매핑 검증.** Dataverse는 보안 역할(security role), 비즈니스 유닛, 행 수준 소유권으로 접근을 통제합니다. 에이전트를 통한 조회에서 이 권한 체계가 어떻게 적용되는지 **반드시 실제 계정으로 테스트**하시기 바랍니다. "에이전트에게 물으니 원래 못 보던 데이터가 나오더라"는 상황은 절대 발생해서는 안 됩니다.
- **개인정보 포함 테이블 주의.** 고객 데이터가 명시적으로 포함되므로, 개인정보가 담긴 테이블을 지식 소스로 지정할 때는 내부 개인정보 처리 방침과 대조해 검토하셔야 합니다.
- **좁게 시작하세요.** 전체 환경을 연결하기보다, 필요한 테이블과 컬럼만 선별해 시작하는 편이 안전하고 답변 품질도 좋습니다.
- **데이터 품질 점검.** 정형 데이터는 오류가 그대로 사실처럼 전달됩니다. 지식 소스로 삼기 전에 정합성을 확인해 두시기 바랍니다.
- **평가(evaluation) 준비.** Copilot Studio는 게시 전 평가 누락을 위험 요소로 표시하는 방향(Agent Readiness, RM568762)으로 가고 있습니다. 데이터 그라운딩 에이전트는 정확도 검증이 특히 중요하므로 대표 질문 세트를 미리 준비하시면 좋습니다.
- **환경(Environment) 전략 확인.** Dataverse는 환경 단위로 분리되어 있습니다. 개발·테스트·운영 환경 중 어디를 연결할지, ALM 관점에서 어떻게 승격할지 미리 정해 두시기 바랍니다.

---

## 마무리

에이전트의 유용성은 결국 **어떤 데이터에 닿을 수 있느냐**로 결정됩니다. 문서만 아는 에이전트와, 실제 고객 레코드와 운영 현황을 아는 에이전트는 업무에서의 가치가 다릅니다.

Azure SQL에 이어 Dataverse까지 네이티브 지식 소스로 편입되면서, Copilot Studio는 **조직의 정형 데이터를 다루는 플랫폼**으로 한 걸음 더 나아갑니다. Power Platform을 이미 운영 중인 조직이라면 가장 빠르게 효과를 볼 수 있는 경로이기도 합니다.

2026년 8월 미리 보기, 9월 GA 일정이니 **연결 대상 테이블 선정과 권한 검증 계획**을 지금부터 준비하시길 권합니다.

---

> **출처**: Microsoft 365 Roadmap 메시지 **RM568929** — *Microsoft Copilot Studio: Dataverse integration on Copilot Studio*
> - 메시지 원문: [https://mc.merill.net/message/RM568929](https://mc.merill.net/message/RM568929)
> - Microsoft 365 Roadmap: [https://www.microsoft.com/en-us/microsoft-365/roadmap?searchterms=568929](https://www.microsoft.com/en-us/microsoft-365/roadmap?searchterms=568929)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
