---
title: "에이전트 평가자도 비교해야 합니다: Power Platform의 Multi-grader comparison"
date: 2026-10-21T00:00:00 KST
categories:
  - Copilot
tags:
  - PowerPlatform
  - AgentEvaluation
  - Graders
  - Quality
excerpt: "Multi-grader comparison은 같은 평가에 적용된 여러 채점자의 점수와 설명, 합격·불합격을 나란히 비교하는 기능입니다. 로드맵은 2026년 10월 GA 목표를 표시하지만 수집 시점의 상태는 In development이므로 실제 제공 여부를 구분해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트 평가자도 비교해야 합니다: Power Platform의 Multi-grader comparison

에이전트 답변을 평가할 때 채점 기준이 달라지면 결과도 달라질 수 있습니다. 한 평가자에게는 합격인 답변이 다른 평가자에게는 불합격이라면, 점수뿐 아니라 그 이유를 함께 살펴봐야 합니다.

Microsoft 365 Roadmap 577183은 Power Platform 거버넌스·관리 영역의 **Multi-grader comparison**을 소개합니다. 같은 평가에 적용한 여러 grader의 결과를 비교해 일치점과 차이, 전반적인 채점 동작을 파악하는 기능입니다.

---

## 점수·판정·설명·근거를 나란히 봅니다

원문은 grader 병렬 비교, 점수 비교, 각 grader의 설명 검토, 채점 일관성 분석을 핵심 기능으로 제시합니다.

결과 화면에는 **비교 점수 보기, pass/fail 비교, grader별 설명, 평가를 뒷받침하는 근거**가 포함된다고 안내합니다. 단순히 평균 점수 하나를 구하는 것보다 평가 기준의 불일치를 찾아내는 데 초점이 있습니다.

## 이런 방식으로 활용할 수 있습니다

예를 들어 사내 지식 에이전트에서 답변 정확성과 정책 준수를 서로 다른 기준으로 평가한 뒤, 같은 응답에서 판정이 갈리는 이유를 검토할 수 있습니다. 이는 기능을 이해하기 위한 활용 예시이며, 원문이 특정 기본 grader 구성을 제공한다고 명시한 것은 아닙니다.

메이커는 비교 결과를 통해 에이전트 지침을 바꿔야 하는지, 평가 기준 자체를 다듬어야 하는지 판단할 수 있습니다. **여러 grader가 동의한다고 실제 업무 정답이 자동 보장되는 것은 아니므로**, 중요한 사례는 사람이 근거까지 검토해야 합니다.

## 일정은 목표와 상태를 함께 보세요

수집한 로드맵은 프리뷰 **2026년 9월**, GA **2026년 10월**을 표시합니다. 그러나 현재 상태는 **In development**입니다. 따라서 이 글은 “이미 GA가 완료됐다”는 안내가 아닙니다.

대상은 Web, Worldwide Standard Multi-Tenant로 표시되어 있습니다. 구체적인 사용 경로, 라이선스와 비용은 이 로드맵만으로 확인되지 않습니다.

## 마무리

에이전트 품질 관리에서는 답변뿐 아니라 **답변을 판정하는 체계의 일관성**도 점검해야 합니다. Multi-grader comparison은 이 검토를 더 명시적으로 수행하도록 돕는 기능으로 이해하면 좋습니다.

> **출처**: [RM577183 — Microsoft Power Platform governance and administration: Multi-grader comparison](https://mc.merill.net/message/RM577183) · [Microsoft 365 Roadmap 577183](https://www.microsoft.com/microsoft-365/roadmap?id=577183). 실제 출시 일정·기능은 변경될 수 있습니다.
