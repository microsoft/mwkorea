---
title: "도구를 제대로 골랐는지까지 평가합니다: Copilot Studio Tool accuracy grader"
date: 2026-10-30T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Evaluation
  - Tools
excerpt: "Copilot Studio의 Tool accuracy grader는 에이전트가 올바른 도구·액션을 선택하고 기대한 입력을 사용했는지 평가합니다. 2026년 10월 15일 GA 기능으로 답변만으로 드러나지 않는 실행 오류를 찾는 데 도움을 줍니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 도구를 제대로 골랐는지까지 평가합니다: Copilot Studio Tool accuracy grader

에이전트가 맞는 말을 했더라도 잘못된 액션을 호출했다면 업무 결과는 틀릴 수 있습니다. 실행형 에이전트에서는 도구 선택과 입력값 자체를 평가해야 합니다.

Copilot Studio의 **Tool accuracy grader**는 사용자 요청에 맞는 도구 또는 액션을 선택하고 기대한 입력을 사용했는지 확인하도록 돕습니다.

---

## 답변 품질과 도구 정확도는 다릅니다

이 평가기는 실행 문제를 일찍 발견하고 trace를 수동 검사하는 부담을 줄이는 데 초점을 맞춥니다. 문장 표현이 자연스러운지와 별개로 어떤 기능을 어떤 값으로 실행했는지를 살펴봅니다.

예를 들어 조회 요청에 수정 도구를 선택하지 않는지, 대상 식별자를 올바르게 전달하는지 등을 조직의 테스트 시나리오로 삼을 수 있습니다. 이는 적용 예시이며, 원문이 특정 커넥터나 도구를 나열한 것은 아닙니다.

## 일정과 도입 체크포인트

기능은 **2026년 10월 15일 GA**에 도달했습니다. 공지에는 별도 필수 조치가 없다고 안내돼 있습니다.

국내 메이커는 중요한 액션부터 기대 도구와 기대 입력을 명확히 정의하는 것이 좋습니다. 평가는 권한 통제나 실행 승인 절차를 대신하지 않으므로, 쓰기 작업과 고위험 액션의 보호 장치는 별도로 유지해야 합니다.

## 마무리

좋은 실행형 에이전트의 기준은 답변뿐 아니라 도구 사용에도 있습니다. Tool accuracy grader는 그 두 번째 축을 구조적으로 확인하도록 돕습니다.

> **출처**: MC1530748 — [Copilot Studio - Tool accuracy grader](https://mc.merill.net/message/MC1530748). [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap). 원문에 개별 Roadmap ID는 표시되어 있지 않습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
