---
title: "모델을 바꿨다면 다시 평가하세요: Copilot Studio가 평가 누락을 알려줍니다"
date: 2026-10-31T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Evaluation
  - Agent
excerpt: "Copilot Studio가 한 번도 평가하지 않은 에이전트나 마지막 평가 이후 모델이 바뀐 에이전트에 경고를 표시합니다. 경고는 게시를 차단하지 않으며 Evaluate agent에서 현재 모델로 평가를 실행할 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 모델을 바꿨다면 다시 평가하세요: Copilot Studio가 평가 누락을 알려줍니다

지난번 평가 결과가 좋았더라도 모델이 바뀌면 같은 결과를 보장할 수 없습니다. 평가 자체를 한 번도 하지 않은 에이전트라면 더 큰 공백이 남습니다.

Copilot Studio는 이런 상황을 메이커가 놓치지 않도록 **Review 패널의 에이전트 평가 상태 경고**를 제공합니다.

---

## 경고가 나타나는 두 가지 경우

에이전트를 한 번도 평가하지 않았거나, 가장 최근 평가 이후 모델이 바뀌었을 때 경고가 자동으로 표시됩니다. 메이커가 개발이나 배포를 계속하기 전에 재평가 필요성을 판단하도록 돕는 장치입니다.

중요한 점은 **경고가 게시를 차단하지 않는다는 것**입니다. 조직이 배포 전 평가를 의무화하려면 별도 운영 절차로 적용해야 하며, 이 알림 자체를 강제 품질 게이트로 보면 안 됩니다.

## 사용 방법과 일정

기능은 **2026년 10월 15일 GA**로 제공됐습니다. 별도 관리자 조치나 추가 설정은 필요하지 않습니다.

경고가 보이면 **Evaluate agent**를 선택해 Evaluation 페이지를 열고 현재 모델로 평가를 실행합니다. 국내 운영팀에서는 모델 변경 승인 절차에 재평가와 결과 확인 단계를 함께 넣는 방식을 고려할 수 있습니다.

## 마무리

알림의 가치는 평가를 대신하는 데 있지 않고, 오래된 평가 결과에 의존하는 실수를 줄이는 데 있습니다. 경고를 확인한 뒤 실제 평가를 실행하고 결과를 검토하는 책임은 여전히 팀에 있습니다.

> **출처**: MC1532071 — [Copilot Studio - Agent status evaluation warnings announcement](https://mc.merill.net/message/MC1532071). [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap). 원문에 개별 Roadmap ID는 표시되어 있지 않습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
