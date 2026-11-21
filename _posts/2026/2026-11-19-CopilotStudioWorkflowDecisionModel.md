---
title: "Copilot Studio 대량 분류를 위한 새 선택지: Classify 노드의 Decision 모델"
date: 2026-11-19T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Workflows
  - DecisionModel
  - Classification
  - Automation
excerpt: "Copilot Studio 워크플로의 Classify 노드에서 Decision 모델을 선택할 수 있게 됩니다. 기존 범주 기반 분기와 출력은 유지되며, 기존 노드는 자동 변경되지 않는다는 점과 전환 전 검토사항을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio 대량 분류를 위한 새 선택지: Classify 노드의 Decision 모델

문의나 요청을 유형별로 분류한 뒤 담당 흐름으로 보내는 작업은 자동화의 기본입니다. 처리량이 많아질수록 분류에 사용하는 모델을 업무 성격에 맞게 선택하는 것도 중요해집니다.

Message Center 공지 MC1560402는 **Copilot Studio 워크플로의 Classify 노드에서 Decision 모델을 선택할 수 있는 기능**을 안내합니다. 공지에 명시된 GA 날짜는 **2026년 11월 19일**입니다.

---

## 무엇이 달라지나요?

메이커는 Classify 노드에서 Decision 모델을 선택해 보다 효율적인 대량 분류에 활용할 수 있습니다. 원문은 더 높은 처리량의 분류를 위한 선택지라고 설명하지만, 구체적인 처리 속도·정확도·비용 개선 수치는 제시하지 않습니다.

분류 모델을 바꾸더라도 기존 작업 방식의 다음 요소는 유지됩니다.

- **범주와 설명 정의:** 지금처럼 분류할 범주와 설명을 작성합니다.
- **범주 기반 분기:** 분류 결과에 따라 후속 흐름을 나눕니다.
- **출력:** Classify 노드의 출력이 계속 동작합니다.
- **자동 Other 범주:** 기존의 자동 Other 범주도 계속 동작합니다.

따라서 이번 변화는 새로운 분류 체계를 강제로 적용하는 것이 아니라, **현재의 범주 기반 워크플로 안에서 모델 선택지를 추가하는 것**으로 이해하면 됩니다.

## 기존 워크플로는 자동 변경되지 않습니다

원문이 분명하게 밝히는 부분은 **기존 Classify 노드의 현재 모델과 동작이 유지된다**는 점입니다. Decision 모델을 쓰려면 메이커가 해당 노드를 업데이트해야 합니다.

공지 자체로 필수 관리자 조치는 없습니다. 기존 노드가 자동으로 Decision 모델로 전환된다고 전제하거나, 모든 운영 흐름을 즉시 변경할 필요는 없습니다.

## 어떤 업무에 검토할 수 있을까요?

예를 들어 접수 문의를 제품·계정·결제 관련 요청으로 나누거나, 문서의 유형에 따라 후속 처리 경로를 정하는 흐름에서 적용을 검토할 수 있습니다. 이는 기능을 이해하기 위한 활용 예시이며, 원문에 제시된 성능 검증 사례는 아닙니다.

도입 전에는 실제 데이터에 가까운 입력으로 다음을 확인하는 것이 좋습니다.

1. 대표 입력이 의도한 범주로 분류되는지 확인합니다.
2. 여러 범주에 걸친 모호한 입력과 기존 Other 처리 사례를 확인합니다.
3. 분류 출력과 후속 분기가 기존 업무 흐름과 맞게 연결되는지 확인합니다.
4. 변경 전후 품질과 처리 특성을 비교한 뒤 운영 반영 범위를 결정합니다.

위 항목은 전환을 위한 권고입니다. 공지에는 모델 선택 UI의 상세 경로나 전용 설정 명령어가 없으므로 실제 제공 화면과 제품 문서를 확인해야 합니다.

## 마무리

이번 업데이트의 핵심은 **기존 흐름을 유지하면서 대량 분류에 맞는 모델을 선택할 수 있다는 것**입니다. 모든 노드를 한 번에 바꾸기보다, 분류량이 많고 결과를 비교하기 쉬운 흐름부터 평가하는 접근이 적절합니다.

> **출처:** Message Center **MC1560402**, [Copilot Studio – Use the Decision model in the Classify node in Workflows](https://mc.merill.net/message/MC1560402). [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap)에서 관련 업데이트를 확인할 수 있습니다. 이 공지에는 개별 Roadmap ID가 명시되어 있지 않습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
