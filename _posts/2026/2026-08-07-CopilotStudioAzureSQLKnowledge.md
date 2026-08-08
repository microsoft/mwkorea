---
title: "사내 DB의 데이터를 에이전트로 — Copilot Studio에 Azure SQL 지식 소스 추가"
date: 2026-08-07T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - AzureSQL
  - KnowledgeSource
  - Grounding
  - EnterpriseData
  - Roadmap
excerpt: "Copilot Studio에서 Azure SQL을 지식 소스(Knowledge Source)로 연결할 수 있게 됩니다. 기존 지식 소스와 동일한 방식으로 업무 핵심 데이터를 에이전트에 그라운딩할 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 사내 DB의 데이터를 에이전트로 — Copilot Studio에 Azure SQL 지식 소스 추가

Copilot Studio로 에이전트를 만들 때 가장 자주 부딪히는 벽은 **"우리 데이터를 어떻게 붙이느냐"**입니다. SharePoint 문서나 웹사이트 같은 비정형 콘텐츠는 비교적 쉽게 연결할 수 있었지만, 정작 업무의 핵심인 **관계형 데이터베이스의 정형 데이터**는 별도의 커넥터나 커스텀 개발을 거쳐야 했습니다.

주문 이력, 재고, 고객 마스터, 계약 정보 — 조직에서 가장 중요한 데이터는 대개 데이터베이스 안에 있습니다.

Microsoft Copilot Studio에 **Azure SQL Knowledge Source** 기능이 로드맵에 올랐습니다. 메이커가 에이전트를 만들 때 활용할 수 있는 엔터프라이즈 데이터 소스의 범위를 넓히는 업데이트입니다.

---

## 무엇이 새로워지나요

Microsoft가 밝힌 내용을 정리하면 다음과 같습니다.

- **Azure SQL Knowledge Source** 기능이 Copilot Studio에서 메이커가 활용할 수 있는 **엔터프라이즈 데이터 소스의 범위를 확장**합니다.
- 조직은 **Azure SQL에 저장된 비즈니스 핵심 정보(business-critical information)**를 에이전트 경험에 가져올 수 있습니다.
- 방식은 **다른 지원 지식 소스에서 이미 사용하던 것과 동일한 지식 중심 접근(knowledge-centric approach)**입니다.

마지막 항목이 실무적으로 중요합니다. 완전히 새로운 개발 방식을 배워야 하는 것이 아니라, **기존에 SharePoint나 파일을 지식 소스로 붙이던 것과 같은 흐름**으로 Azure SQL을 연결할 수 있다는 의미이기 때문입니다.

---

## 통합 지식 플랫폼 전략의 일부

Microsoft는 이번 기능을 **"통합 지식 플랫폼 전략(unified knowledge platform strategy)을 향한 또 하나의 단계"**로 설명합니다.

그 전략의 지향점은 이렇습니다.

> 고객이 **공통 지식 프레임워크(common knowledge framework)**를 통해 엔터프라이즈 데이터 소스를 연결하고, 그 소스들을 **여러 에이전트 경험 전반에서 일관되게 활용**할 수 있게 하는 것.

즉 데이터 소스마다 다른 방식으로 붙이고 각 에이전트마다 다시 설정하는 구조가 아니라, **한 번 연결한 지식을 여러 에이전트가 공통으로 쓰는 구조**를 지향합니다.

그리고 Microsoft는 이 기능이 **기존 Microsoft 데이터 자산을 활용해 근거 있고(grounded) 엔터프라이즈에 적합한 AI 솔루션을 구축하려는 조직에게 설득력을 강화한다**고 덧붙입니다.

---

## 활용 시나리오

Azure SQL에 데이터가 있는 조직이라면 다음과 같은 에이전트를 떠올려 볼 수 있습니다.

### 1. 사내 조회 에이전트

"○○ 고객사의 최근 계약 만료일이 언제야?", "이 제품 현재 재고가 얼마나 돼?" 같은 질문에 답하는 에이전트. 지금까지는 담당자에게 묻거나 시스템에 직접 접속해야 했던 조회입니다.

### 2. 고객 응대 지원

상담원이 고객과 통화하면서 주문 상태나 이력을 자연어로 조회합니다.

### 3. 영업 지원 에이전트

파이프라인, 지난 거래 내역, 담당자 정보를 결합해 미팅 준비를 돕습니다.

### 4. 운영 현황 브리핑

정기적으로 운영 데이터를 요약해 전달하는 에이전트를 구성합니다.

### 5. 문서 + DB 결합 답변

사내 정책 문서(SharePoint)와 실제 데이터(Azure SQL)를 함께 지식 소스로 두면, **"규정상 이렇게 하게 되어 있고, 현재 데이터는 이렇습니다"** 형태의 답변이 가능해집니다. 이 조합이 이번 업데이트의 진짜 가치일 수 있습니다.

---

## 일정

| 항목 | 내용 |
|---|---|
| 대상 제품 | Microsoft Copilot Studio |
| 미리 보기(Preview) | **2026년 8월(CY2026 August)** |
| 정식 출시(GA) | **2026년 9월(CY2026 September)** 예정 |

미리 보기가 이번 달이고 GA까지의 간격이 짧은 편입니다. 검증을 서두르실 만한 일정입니다.

실제 출시 일정·기능은 변경될 수 있습니다.

---

## 도입 체크포인트

- **대상은 Azure SQL입니다.** 로드맵 설명은 **Azure SQL**을 명시합니다. 온프레미스 SQL Server를 포함한 구체적 지원 범위는 미리 보기·GA 시점 문서에서 확인하셔야 합니다. 국내에는 온프레미스 DB를 운영 중인 조직이 많으므로 이 부분 확인이 특히 중요합니다.
- **데이터 접근 권한 설계가 핵심입니다.** 지식 소스로 연결하는 순간 "누가 어떤 행(row)까지 볼 수 있는가"가 문제가 됩니다. 에이전트 사용자의 권한과 DB 권한이 어떻게 매핑되는지 반드시 검증하시기 바랍니다. 특히 개인정보나 인사·급여 데이터가 있는 DB는 신중해야 합니다.
- **어떤 테이블을 노출할지 좁게 시작하세요.** 전체 DB를 연결하기보다, 조회 전용 뷰(view)를 만들어 필요한 컬럼만 노출하는 방식이 안전합니다.
- **데이터 품질이 답변 품질입니다.** 정형 데이터는 문서와 달리 오류가 그대로 사실처럼 전달됩니다. 지식 소스로 삼기 전에 데이터 정합성을 점검해 두시기 바랍니다.
- **평가(evaluation)를 함께 준비하세요.** 최근 Copilot Studio는 게시 전 평가 누락을 위험 요소로 표시하는 방향으로 가고 있습니다. DB 그라운딩 에이전트는 특히 정확도 검증이 중요하므로, 대표 질문 세트를 미리 만들어 두시면 좋습니다.

---

## 마무리

에이전트가 실무에서 쓸모 있으려면 결국 **조직의 진짜 데이터**에 닿아야 합니다. 문서 요약만 하는 에이전트와, 실제 재고와 계약 상태를 아는 에이전트는 체감 가치가 다릅니다.

Azure SQL 지식 소스 지원은 그 간극을 좁히는 업데이트입니다. 2026년 8월 미리 보기, 9월 GA로 일정이 촘촘하니, Azure SQL을 운영 중인 조직이라면 **연결 대상 데이터 범위와 권한 설계**를 지금부터 정리해 두시길 권합니다.

---

> **출처**: Microsoft 365 Roadmap 메시지 **RM568930** — *Microsoft Copilot Studio: SQL server Support in Microsoft Copilot Studio*
> - 메시지 원문: [https://mc.merill.net/message/RM568930](https://mc.merill.net/message/RM568930)
> - Microsoft 365 Roadmap: [https://www.microsoft.com/en-us/microsoft-365/roadmap?searchterms=568930](https://www.microsoft.com/en-us/microsoft-365/roadmap?searchterms=568930)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
