---
title: "Copilot Studio 에이전트의 자기 학습: 실행 기록에서 개선안을 찾는다"
date: 2026-10-01T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - SelfLearning
  - AgentOptimization
  - Workflow
  - Governance
excerpt: "Copilot Studio가 완료된 실행에서 반복 도구 순서를 찾아 워크플로 전환과 지침 개선을 추천합니다. 메이커가 근거와 예상 효과를 검토한 뒤 복사본을 구성·테스트·게시하는 통제형 개선 과정입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio 에이전트의 자기 학습: 실행 기록에서 개선안을 찾는다

Microsoft Copilot Studio에 완료된 실행 기록을 바탕으로 에이전트 개선안을 제시하는 **self-learning** 기능이 추가될 예정입니다. 이름만 보면 에이전트가 스스로 코드를 바꾸는 것처럼 들리지만, 실제 흐름은 메이커의 검토와 테스트를 거치는 통제형 최적화입니다.

기능은 반복되는 도구 호출 순서를 찾아 결정론적 workflow로 옮길 수 있는 부분을 제안합니다. 모델 판단이 필요한 일은 남겨 두고, 표준화할 수 있는 단계는 워크플로로 전환해 오류와 비용을 줄이는 접근입니다.

---

## 추천이 만들어지는 방식

Copilot Studio는 완료된 run에서 반복 패턴을 분석해 다음 정보를 메이커에게 제공합니다.

- 반복 도구 시퀀스와 이를 workflow로 처리할 수 있다는 추천
- 추천을 뒷받침하는 실행 근거
- 예상되는 품질·비용 영향
- 관련 instruction과 tool 변경 내용

메이커는 추천을 그대로 자동 적용하는 대신 수락 여부를 결정합니다. 수락하면 개선된 에이전트의 복사본을 구성하고 테스트한 뒤 게시합니다.

## 왜 workflow 전환이 중요한가

매 실행마다 모델이 동일한 도구 순서를 다시 판단하면 결과 편차와 토큰·도구 호출 비용이 커질 수 있습니다. 반복 단계만 workflow로 고정하면 다음 효과를 기대할 수 있습니다.

- 에이전트 동작 표준화
- 반복 단계의 오류 감소
- 불필요한 모델 판단과 비용 절감
- 판단이 필요한 부분에 모델 역량 집중

## 거버넌스와 테스트

self-learning은 운영 기록을 개선 근거로 사용하므로 대표 데이터와 예외 사례가 충분히 쌓여야 합니다. 추천을 적용하기 전에는 성공률뿐 아니라 실패 유형, 권한 변경, 비용 변화, 예외 처리까지 비교해야 합니다.

또한 개선본을 별도 복사본으로 테스트하고 게시하는 구조를 활용해 기존 운영 버전과의 회귀 테스트를 수행하는 것이 좋습니다. 추천이 있다는 이유만으로 모든 반복 단계를 workflow로 고정하면 유연성이 필요한 예외까지 막을 수 있습니다.

## 일정

Preview는 **2026년 9월**, GA는 **2026년 10월**로 안내되었습니다. 테넌트에서 기능이 보이면 소규모 에이전트부터 추천 근거와 예상 효과의 정확성을 검증해 보는 것이 안전합니다.

> **출처**: 원문 ID **RM570432** · [mc.merill.net 원문](https://mc.merill.net/message/RM570432) · [Microsoft 365 Roadmap 570432](https://www.microsoft.com/en-us/microsoft-365/roadmap?featureid=570432)  
> 실제 출시 일정·기능은 변경될 수 있습니다.
