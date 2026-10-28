---
title: "에이전트가 고객을 더 잘 이해하려면: Customer Insights를 MCP로 연결하기"
date: 2026-10-23T00:00:00 KST
categories:
  - Copilot
tags:
  - CustomerInsights
  - MCP
  - CopilotStudio
  - Grounding
excerpt: "Customer Insights MCP server는 통합 고객 프로필과 구매·세그먼트·예측 인사이트를 에이전트에 제공합니다. CRM 연락처를 실제 고객 맥락으로 연결하는 기능과 도입 시 확인할 조건을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트가 고객을 더 잘 이해하려면: Customer Insights를 MCP로 연결하기

영업 에이전트가 잠재고객의 이름만 안다면 답변의 깊이에는 한계가 있습니다. 기존 VIP 고객인지, 최근 구매가 있었는지, 이탈 위험은 어떤지 알아야 실제로 도움이 되는 제안을 할 수 있습니다.

Roadmap RM577814는 **Customer Insights - Data의 통합 프로필과 인사이트를 MCP로 에이전트에 제공**하는 기능을 설명합니다. 모델 자체를 바꾸기보다 답변의 근거가 되는 고객 맥락을 보강하는 접근입니다.

---

## 어떤 정보를 에이전트에 제공하나요?

Customer Insights MCP server는 표준 MCP 아키텍처로 AI 에이전트와 채팅 경험에 데이터를 전달합니다. 원문에서 제시한 주요 도구 활용은 다음과 같습니다.

- Dataverse의 연락처·리드를 통합 고객 프로필에 연결
- Dataverse에 없던 외부 소스의 고객 정보 조회
- 최근 **4개월 구매 합계**나 가장 최근 참여일 등 계산된 측정값 이해
- 고객이 속한 세그먼트와 중복 연락처, 대표 레코드 파악
- Customer Lifetime Value와 이탈 위험 같은 예측 인사이트 조회

이는 단순한 CRM 레코드 검색보다 넓은 범위입니다. Copilot Studio로 만든 사용자 지정 에이전트도 통합된 고객 인사이트를 활용하는 방향을 제시합니다.

## 같은 고객을 다른 이름으로 만났을 때

원문 사례에서는 웨비나 참석 리드인 Joe가 기존 VIP 고객 Joseph과 연결됩니다. 외부 구매·리워드 데이터와 Dataverse 정보가 통합되어 있기 때문에, 영업 담당자는 신규 리드로만 접근하지 않고 기존 관계와 보유 제품을 고려할 수 있습니다.

한국 기업에서도 온라인 이벤트, 멤버십, 구매 시스템의 고객 정보가 분산되어 있다면 비슷한 가치를 기대할 수 있습니다. 다만 이러한 효과는 **고객 식별과 데이터 통합이 제대로 되어 있다는 전제**에 달려 있습니다.

## 도입 전에 확인할 것

먼저 [MCP server 도구 문서](https://learn.microsoft.com/en-us/dynamics365/customer-insights/data/mcp-server-tools)에서 사용 가능한 도구와 접근 조건을 확인해야 합니다. 프로필 매칭 품질, 측정값 갱신 주기, 개인정보 접근 범위는 조직이 별도로 검증할 항목입니다.

예측값을 확정 사실처럼 표현하지 않도록 에이전트 안내도 마련하는 것이 좋습니다. 예를 들어 이탈 위험은 의사결정의 참고 신호이지, 고객 의사를 직접 확인한 결과가 아닙니다.

## 제공 일정

수집 시점 상태는 **In development**이며, 프리뷰는 **2026년 6월**, GA는 **2026년 11월**로 표기되어 있습니다. 이 일정만으로 한국의 모든 환경에서 즉시 사용할 수 있다고 단정할 수는 없습니다.

> **출처**: [RM577814 — 고객 인사이트로 에이전트 그라운딩 강화](https://mc.merill.net/message/RM577814) · [Microsoft 365 Roadmap 577814](https://www.microsoft.com/microsoft-365/roadmap?id=577814). 실제 출시 일정·기능은 변경될 수 있습니다.
