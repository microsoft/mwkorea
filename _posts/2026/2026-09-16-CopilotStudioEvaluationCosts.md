---
title: "에이전트 평가에도 비용이 보인다: Copilot Studio Agent Evaluations 개선"
date: 2026-09-16T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - AgentEvaluations
  - CostManagement
  - Roadmap
excerpt: "Copilot Studio의 Agent Evaluations에서 평가와 직접 연결된 소비 비용을 확인하는 기능이 예고됐습니다. 평가 생성, 테스트 실행, 모델 채점·판정의 사용량을 구분해 평가를 반복할 때 비용을 함께 살펴볼 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트 평가에도 비용이 보인다: Copilot Studio Agent Evaluations 개선

에이전트의 답변 품질을 높이려면 테스트와 평가를 반복해야 합니다. 평가 결과뿐 아니라 어느 단계에서 사용량이 발생하는지도 알 수 있어야 운영 비용을 계획하기 쉽습니다.

로드맵 **571195**, 수집 ID **RM571195**는 제작자가 **Agent Evaluations에 직접 연결된 소비 비용**을 볼 수 있도록 개선한다고 안내합니다. 원문은 개발 과정에서 테스트하고 수정하며 대화를 검토할 때 비용을 더 투명하게 확인하는 기능으로 설명합니다.

---

## 어떤 평가 비용을 구분하나요

| 단계 | 원문이 명시한 범위 |
|---|---|
| 평가 생성 | 평가를 만드는 과정의 사용량 |
| 테스트 실행 | 테스트를 수행한 사용량 |
| 모델 채점·판정 | 평가 결과를 모델이 채점하거나 판단하는 과정의 사용량 |

이 구분은 평가를 한 번 실행했을 때 총량만 보는 대신 어느 활동에서 소비가 발생했는지 파악하는 데 도움이 됩니다. 다만 구체적인 단가나 계산 방식은 이번 설명에 없습니다.

## 품질과 소비량을 함께 기록

실무에서는 같은 테스트 세트로 에이전트 지침이나 모델 구성을 바꿔 보고, 품질 변화와 평가 소비량을 함께 기록하는 방법을 생각할 수 있습니다. 이는 활용 예시이지 자동 최적화 기능의 발표는 아닙니다.

평가 비용이 낮다고 품질이 좋다는 뜻은 아니며, 비용 증가가 항상 개선을 의미하지도 않습니다. 어떤 오류를 찾으려는 평가인지 먼저 정한 뒤 결과를 해석하는 것이 좋습니다.

## 일정과 주의사항

로드맵의 **GA 표기는 2026년 9월**입니다. 실제 환경의 제공 상태와 표시 단위는 제품에서 확인해야 합니다.

이 항목은 비용의 **가시성**에 관한 안내입니다. 비용을 표시하는 기능을 자동 지출 한도나 소비 중단 기능으로 받아들이면 안 됩니다. 별도의 과금 정책 변경, 예산 자동 설정, 무료 평가 제공은 이 원문에 명시되지 않았습니다.

---

> **출처**
>
> - 원문 ID: **RM571195** — *Microsoft Copilot Studio: Cost visibility in Agent Evaluations*
> - 원문: [RM571195](https://mc.merill.net/message/RM571195)
> - [Microsoft 365 Roadmap 571195](https://www.microsoft.com/microsoft-365/roadmap?id=571195)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
