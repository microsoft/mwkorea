---
title: "에이전트와 Cowork는 어디에 쓰일까? Copilot 사용 사례 분류 프리뷰"
date: 2026-11-18T00:00:00 KST
categories:
  - Copilot
tags:
  - Agent365
  - CopilotCowork
  - Analytics
  - Frontier
excerpt: "Microsoft가 에이전트 세션과 Copilot Cowork 활동의 사용 사례 분류를 Frontier 공개 프리뷰로 제공합니다. 기본 활성화 범위와 관리자 제어, 사용자 옵트아웃 및 개인정보 보호 조건을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트와 Cowork는 어디에 쓰일까? Copilot 사용 사례 분류 프리뷰

AI 비용을 관리하려면 사용량뿐 아니라 **어떤 업무에 사용했는지**도 알아야 합니다. Microsoft는 MC1557759에서 에이전트 세션과 Copilot Cowork 활동을 미리 정의된 업무 분류에 연결하는 기능을 발표했습니다.

이 기능은 개별 직원을 평가하거나 대화 내용을 감사하기 위한 도구가 아니라 조직의 사용 경향과 투자 방향을 살펴보기 위한 분석 기능입니다. 특히 기본 활성화 방식이므로 도입 담당자는 보고서뿐 아니라 개인정보 관련 제어도 함께 확인해야 합니다.

---

## 무엇을 분류하나요?

Copilot Studio 및 Azure AI Foundry로 만든 에이전트, 선언형 에이전트, Agent 365 Connected platforms에 등록된 타사 에이전트의 세션을 수행 업무에 따라 분류합니다. 관리자는 Microsoft 365 관리 센터의 에이전트 **Activity** 탭과 **Agent Map**에서 사용 사례와 세션 수를 확인할 수 있습니다. 이 분류는 최종 사용자나 에이전트 제작자에게 공유되지 않습니다.

Cowork 활동은 가장 가까운 사전 정의 사용 사례에 연결됩니다. 관리자는 **Cost Management > Consumption > Use cases**에서 집계된 사용 사례, 비용, 추정 가치를 확인할 수 있습니다. 공지 시점에 분류 기반 AI 가치 계산은 Cowork 사용자 활동에 한정됩니다.

## 일정과 기본 설정

Frontier 공개 테넌트에 2026년 11월 중순부터 말까지 순차 제공할 예정입니다. 대상 테넌트와 사용자에게 사용 사례 분류 및 AI 가치 계산이 기본 활성화되며, 이는 일반 공급 전체에 대한 발표가 아닙니다.

Global Administrator와 AI Administrator는 서로 독립된 세 가지 제어를 관리할 수 있습니다.

| 제어 | 관리 위치와 범위 |
|---|---|
| 에이전트 세션 분류 | Agents > Settings > Activity classification에서 테넌트 전체 비활성화 |
| Cowork 업무 활동 분류 | Feature access management 정책으로 조직·그룹·개인별 비활성화 |
| AI 가치 계산 | Agents > Settings > AI value에서 활성화 및 계산 입력값 조정 |

대상 사용자는 Microsoft 프로필 편집기의 **Data and privacy**에서도 Cowork 분류를 옵트아웃할 수 있습니다.

## 개인정보 보호에서 놓치지 말아야 할 점

분류를 끄면 하루 이내 중단됩니다. 기존 결과는 **삭제가 아니라 숨김 처리**되며, 다시 켜도 비활성화 기간의 활동을 소급 분류하지 않습니다.

분류 체계는 테넌트별 프로젝트명이 아닌 사전 정의 항목을 사용합니다. 다른 사람에게 개인별 분류가 노출되지 않고, 조직 리더에게는 집계된 업무 활동 정보가 제공됩니다. 결과는 방향성을 파악하는 수준의 정확도를 전제로 하므로 개별 상호작용 감사 자료로 해석하면 안 됩니다.

## 도입 체크포인트

한국 조직에서는 개인정보 담당자와 함께 기본 활성화 여부, 옵트아웃 안내, 기존 결과 보존 특성을 검토하는 것이 좋습니다. 추정 가치의 입력값도 실제 조직의 시간·인건비 가정에 맞춰야 하며, 이를 확정된 재무 성과와 동일시하지 않는 것이 중요합니다.

기능의 목적과 관리 절차는 [Microsoft Learn의 에이전트 업무 사용 사례 안내](https://learn.microsoft.com//microsoft-agent-365/admin/business-use-case-for-agents)에서 추가 확인할 수 있습니다.

> **출처**: [MC1557759](https://mc.merill.net/message/MC1557759), Microsoft 365 Message Center Archive. [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 제시되지 않았습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
