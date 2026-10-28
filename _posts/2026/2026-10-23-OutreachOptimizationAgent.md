---
title: "언제, 얼마나 자주 연락할까: Outreach Optimization Agent의 메시지 조율"
date: 2026-10-23T00:00:00 KST
categories:
  - Copilot
tags:
  - CustomerInsights
  - OutreachOptimizationAgent
  - Marketing
  - Agent
excerpt: "Outreach Optimization Agent는 고객 참여 신호에 따라 이메일 시점과 빈도를 조정합니다. 초기 기준 계획과 실시간 적응, 반드시 지키는 quiet time 제약을 중심으로 기능을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 언제, 얼마나 자주 연락할까: Outreach Optimization Agent의 메시지 조율

고객 여정을 잘 만들었어도 모두에게 같은 간격으로 리마인더를 보내면 메시지 피로가 커질 수 있습니다. 이미 관심을 보인 고객과 반응이 없는 고객에게 같은 후속 연락이 적절하지 않을 수 있기 때문입니다.

Roadmap RM577417의 **Outreach Optimization Agent**는 Customer Insights - Journeys에서 이메일 전달 시점과 빈도를 조율합니다. 여정에 에이전트를 추가하고 보낼 이메일을 선택하는 방식입니다.

---

## 처음에는 공통 기준 계획으로 시작

에이전트는 전체의 과거 참여 패턴을 분석해 대상 고객군을 위한 초기 메시지 계획을 만듭니다. 개인별 최적화 신호가 충분하지 않은 시작 단계에도 활용할 수 있는 기준선입니다.

원문이 설명하는 것은 모두에게 처음부터 완벽히 개인화된 발송을 보장하는 기능이 아니라, 기준 계획에서 시작해 신호에 따라 적응하는 구조입니다.

## 참여와 무응답에 따라 후속 흐름 조정

들어오는 참여 신호와 무응답을 지속적으로 관찰하며 후속 연락 시점과 간격을 조절합니다. 목표의 진행 상태나 달성 여부에 따라 계획에서 빠져나오도록 조정할 수도 있습니다.

원문의 소매 캠페인 사례는 관심을 보인 고객의 후속 연락을 늦추거나 멈추고, 무응답 고객의 리마인더 간격을 조율하는 모습을 제시합니다. 정량적인 참여율 개선 수치는 제공하지 않습니다.

## quiet time은 최적화보다 우선합니다

**quiet time 설정은 엄격한 제약**입니다. 참여 데이터상 더 좋은 시각으로 보이더라도 승인된 소통 시간 밖에는 메시지를 보내지 않는다고 설명합니다.

한국 조직은 이를 국내 마케팅 수신 동의·시간 정책 검토와 함께 살펴야 합니다. 기능이 국내 규정의 모든 요건을 자동 충족한다고 단정하지 말고, 동의 관리와 시간대 설정을 검증하는 것이 좋습니다.

## 시작하기와 일정

[Outreach Optimization Agent 문서](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/outreach-optimization-agent)에서 제공 조건을 확인하세요. 목표 달성 정의, 선택할 이메일, quiet time과 참여 데이터 품질을 먼저 정리하면 검증 기준이 명확해집니다.

수집 시점 상태는 **In development**, 프리뷰 **2026년 7월**, GA 목표 **2027년 4월**입니다.

> **출처**: [RM577417 — Outreach Optimization Agent](https://mc.merill.net/message/RM577417) · [Microsoft 365 Roadmap 577417](https://www.microsoft.com/microsoft-365/roadmap?id=577417). 실제 출시 일정·기능은 변경될 수 있습니다.
