---
title: "Copilot 모델 선택이 어렵다면: Auto부터 Cowork 추론 강도까지"
date: 2026-11-20T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotCowork
  - Researcher
  - ModelCouncil
  - Frontier
excerpt: "Copilot은 가장 큰 모델을 고르는 것보다 목표에 맞는 모드와 추론 강도를 선택하는 것이 중요합니다. Auto, Cowork의 5단계 effort, Researcher의 Model Council·Critique와 이용 조건을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 모델 선택이 어렵다면: Auto부터 Cowork 추론 강도까지

Copilot의 모델과 모드가 다양해질수록 무엇을 골라야 할지 고민하기 쉽습니다. 하지만 모든 모델의 순위를 외우기보다, 필요한 산출물을 먼저 정하는 편이 업무에는 더 유용합니다.

Microsoft Inside Track은 **일상 업무는 Auto로 시작하고, 필요할 때 모델·모드·추론 강도를 조절하는 방법**을 소개했습니다. 이 글은 2026년 11월 19일 UTC, 한국 시간 11월 20일에 발행된 원문 기준이며 실제 메뉴는 라이선스, 조직 설정, 지역과 경험별로 다를 수 있습니다.

![업무 목표에 맞는 Copilot 도구 선택을 소개하는 원문 안내 그림](/mwkorea/assets/images/2026-11-20-CopilotModelModeEffortGuide/image1.png)

---

## 모델보다 먼저 결과를 정의하세요

회의 전에 짧은 답이 필요한지, 여러 자료를 종합한 조사가 필요한지, 반복 업무를 자동화할 것인지부터 구분합니다. 그다음 **목표, 독자, 형식, 어조, 참고 자료**를 프롬프트에 명시합니다.

짧은 요약에 항상 최대 추론 강도가 필요한 것은 아닙니다. 반대로 조건이 많고 검토가 중요한 작업은 더 깊은 추론이나 여러 모델의 비교가 도움이 될 수 있습니다.

## 기본 출발점은 Auto입니다

Auto는 사용 중인 Copilot 경험에서 이용 가능한 모델과 모드 가운데 선택합니다. 모든 Copilot 화면에서 같은 모델이 제공되는 것은 아니며 라이선스, 조직 설정, 지역에 따라 표시되는 옵션이 달라집니다.

우선 Auto 결과가 목적을 충족하는지 확인하고, 부족할 때 드롭다운에서 다른 모델이나 모드를 선택합니다. 원문은 **대화 중 모델을 바꿔도 처음부터 대화를 다시 시작할 필요는 없다**고 안내합니다.

![Copilot의 기본 선택인 Auto 화면](/mwkorea/assets/images/2026-11-20-CopilotModelModeEffortGuide/image2.png)

## Cowork의 effort는 5단계입니다

Cowork에서는 프롬프트 실행 전에 effort 드롭다운과 슬라이더로 작업에 들일 추론 강도를 고릅니다.

| 단계 | 원문 기준 안내 |
|---|---|
| Light | 제공되는 추론 강도 선택지 |
| Medium | 기본값이며 대부분의 작업에서 출발점으로 권장 |
| High | 더 높은 추론 강도 선택지 |
| Extra High | 더 높은 추론 강도 선택지 |
| Max | 가장 높은 추론 강도 선택지 |

강도를 올리면 더 충실한 결과를 얻을 수 있지만 **시간이 더 걸리고 크레딧도 더 사용**합니다. 각 단계별 정확한 비용이나 품질 상승률은 원문에서 제시하지 않습니다.

![업무 난이도에 맞춘 설정 조정을 설명하는 원문 그림](/mwkorea/assets/images/2026-11-20-CopilotModelModeEffortGuide/image3.png)

![Cowork에서 effort를 조정하는 슬라이더 화면](/mwkorea/assets/images/2026-11-20-CopilotModelModeEffortGuide/image4.png)

실무에서는 Medium으로 시작한 뒤 결과의 누락이나 논리적 한계를 확인하고 높이는 방식이 합리적입니다. 이는 적용을 위한 제안이며, 높은 설정이 사실 정확성을 보장하는 것은 아닙니다.

## 모델 비교가 필요할 때는 Model Council

Researcher에서 Model Council을 선택하면 GPT와 Claude가 같은 요청을 각각 처리합니다. 결과를 나란히 비교하면서 동의하는 부분과 다른 결론을 내린 부분을 확인할 수 있습니다.

사용 절차는 **Copilot Chat에서 Researcher 열기 → 왼쪽 위 드롭다운에서 Model Council 선택 → 질문 입력 → 두 결과 비교**입니다.

하나의 보고서를 원한다면 Critique라는 별도 옵션이 있습니다. 원문 설명에서는 GPT가 보고서를 작성하고 Claude가 검토합니다. 여러 모델을 이용한다고 모든 오류가 제거되는 것은 아니므로 출처와 결론의 근거는 사용자가 확인해야 합니다.

![Researcher에서 Model Council을 선택하는 화면](/mwkorea/assets/images/2026-11-20-CopilotModelModeEffortGuide/image6.png)

## Frontier와 관리자 허용 조건을 확인하세요

**Model Council과 Critique는 원문 시점 Frontier 프로그램 제공 기능**입니다. 또한 관리자가 Anthropic 모델 사용을 허용해야 사용할 수 있습니다.

두 조건을 충족하지 않은 상태에서 메뉴가 보이지 않는다고 곧바로 오류로 판단해서는 안 됩니다. 사내 가이드에도 GA 기능처럼 일괄 안내하지 않고, 대상 사용자와 정책 조건을 함께 표기하는 것이 좋습니다.

![원문의 추가 학습 안내 아이콘](/mwkorea/assets/images/2026-11-20-CopilotModelModeEffortGuide/image5.png)

## 교육에서는 한 가지 흐름으로 정리하면 됩니다

먼저 산출물과 자료 범위를 정하고 Auto로 실행합니다. 부족한 점이 구체적이면 모델이나 모드를 바꾸고, Cowork의 깊이 있는 수행이 필요하면 effort를 조절합니다. 서로 다른 관점의 조사가 중요한 경우에만 Model Council이나 Critique를 검토합니다.

새 모델이 나오면 익숙한 업무 프롬프트로 시험하되, 한 번의 인상으로 영구적인 우열을 정하지 않는 것이 좋습니다. **응답 속도, 스타일, 충실도와 비용을 실제 업무 기준으로 함께 판단**해야 합니다.

![상황에 맞는 모델과 설정 선택을 마무리하는 원문 그림](/mwkorea/assets/images/2026-11-20-CopilotModelModeEffortGuide/image7.png)

## 마무리

좋은 Copilot 활용은 가장 강력한 설정을 고정하는 일이 아닙니다. 기본값으로 충분한 일과 추가 추론·비교가 필요한 일을 구분하면 결과 품질과 시간, 크레딧을 함께 관리할 수 있습니다.

> 출처: [Charting your course in Copilot: Picking the right model, mode, and effort](https://www.microsoft.com/insidetrack/blog/charting-your-course-in-copilot-picking-the-right-model-mode-and-effort/) — Microsoft Inside Track Blog
>
> 자세한 내용은 원문 참조.
