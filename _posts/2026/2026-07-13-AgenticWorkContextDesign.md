---
title: "좋은 모델만으로는 부족하다: Work IQ 사례로 보는 에이전트의 맥락 설계"
date: 2026-07-13T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotCamp
  - WorkIQ
  - ContextEngineering
  - Grounding
  - AIAgents
  - Privacy
excerpt: "Copilot Camp는 Work IQ 페르소나 스케치의 확산을 통해 모델 성능만큼 중요한 업무 맥락의 품질을 설명합니다. 신뢰할 출처와 권한 경계를 먼저 정하는 방법, LinkedIn 내보내기 자료로 맥락을 구성할 때의 주의사항을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 좋은 모델만으로는 부족하다: Work IQ 사례로 보는 에이전트의 맥락 설계

에이전트가 그럴듯한 답을 내놓아도 어떤 자료를 근거로 했는지 알 수 없다면 다시 확인해야 합니다. 이 과정이 반복되면 모델이 답변을 빨리 만들었다는 장점도 줄어듭니다.

Copilot Camp의 Rabia Williams는 **Why Context Became the Real Differentiator in Agentic Work**에서 관심의 초점을 “어느 모델이 가장 좋은가”에서 “어떤 맥락을 신뢰할 수 있는가”로 옮겨 보자고 제안합니다. Work IQ를 활용한 페르소나 스케치와 LinkedIn 데이터 실습이 그 예입니다.

이 글은 원문에 표시된 2026년 7월 13일 발행일을 유지해 소개하는 기존 글입니다. 새로운 제품 출시 공지가 아니라, Copilot과 에이전트를 업무에 연결할 때의 설계 관점에 관한 내용입니다.

---

## 맥락을 먼저 설계해야 하는 이유

원문은 고객 워크숍에서 반복되는 고민을 비용, 신뢰, 통합으로 묶습니다.

| 관점 | 맥락 설계에서 살펴볼 점 |
|---|---|
| 비용 | 요청마다 같은 배경을 다시 구성하는 일을 줄이고, 활용할 맥락을 재사용할 수 있는가 |
| 신뢰 | 사용자가 답변의 출처를 따라가 확인할 수 있는가 |
| 통합 | 한 도구에 머무르지 않고 메일·문서·회의를 잇는 업무 흐름에서 맥락을 활용하는가 |

이는 맥락을 재사용하면 언제나 특정 비율로 비용이 절감된다는 보장은 아닙니다. 원문의 요지는 더 큰 모델을 고르기 전에 **경계 설정, 검증 가능한 근거, 사람의 책임, 업무 시스템 간 연결**을 설계하자는 것입니다.

## Work IQ 페르소나 스케치가 보여 준 것

Anthony Shaw가 작성한 Work IQ 페르소나 스케치 프롬프트는 개인의 업무 역할과 관계를 시각 자료로 표현하는 사례입니다. 원문은 해당 샘플이 `pnp/copilot-prompts` 저장소에서 **72,000회 이상 조회**됐다고 소개합니다.

![커뮤니티에서 공유된 Work IQ 페르소나 스케치 모음](/mwkorea/assets/images/2026-07-13-AgenticWorkContextDesign/image1.png)

이 숫자는 원문이 제시한 확산 지표이지 업무 성과나 도입률이 아닙니다. 저자도 조회수와 실제 업무 개선을 구분해야 한다고 강조합니다.

![원문이 소개한 Anthony Shaw의 업무 맥락 스케치 예시](/mwkorea/assets/images/2026-07-13-AgenticWorkContextDesign/image2.jpg)

주목할 부분은 그림 자체보다 역할에 맞춘 결과를 만드는 틀입니다. 재사용할 수 있는 프롬프트 구조에 실제 업무 맥락을 넣고, 그 결과를 보며 출처와 거버넌스, 재사용 방법을 논의할 수 있게 됐다는 설명입니다. 이미지 안의 표현이나 수치는 공개된 데모의 내용이며 별도의 제품 사양을 보증하지 않습니다.

## 팀에서는 무엇부터 정할까요

1. 에이전트가 도울 업무와 다뤄서는 안 되는 범위를 정합니다.
2. 답변에서 우선할 공식 자료와 권위 있는 출처를 정합니다.
3. 중요한 결과에는 인용을 요구하고, 민감하거나 규제와 관련된 작업에는 검토 단계를 둡니다.
4. 토큰 사용량뿐 아니라 재작업 감소, 의사결정 지원 등 실제 업무 변화로 평가합니다.

맥락은 개발 중 뒤늦게 붙이는 자료 목록이 아니라 제품을 설계할 때 결정할 항목입니다. 어떤 자료가 최신인지, 누가 볼 수 있는지, 자료가 부족할 때 어떻게 답할지도 함께 정해 두는 것이 좋습니다.

## Work IQ 없이 시작하는 LinkedIn 데이터 실습

원문은 Work IQ가 활성화되지 않은 환경에서도 맥락 기반 결과물을 경험할 수 있도록, 약 **15분짜리 실습**으로 LinkedIn 내보내기 자료를 활용하는 방법을 제안합니다. 여기서 LinkedIn 자료는 Work IQ와 같은 서비스가 아니라 별도로 준비하는 입력 데이터입니다.

| 필요한 정보 | 준비할 데이터 |
|---|---|
| 게시물 성과와 콘텐츠 추세 | Creator Analytics의 콘텐츠 데이터 내보내기 |
| 경력·스킬·연결 관계 등 프로필 맥락 | LinkedIn 전체 데이터 내보내기 |

Creator Analytics에서는 [Content 분석 페이지](https://www.linkedin.com/analytics/creator/content/)를 열어 분석 기간을 정하고 **Export**로 파일을 내려받습니다. 형식을 선택하는 화면이 있다면 제공되는 형식 중 하나를 선택합니다.

경력, 스킬, 연결 관계, 추천 정보까지 필요하다면 **Settings & Privacy > Data privacy > Get a copy of your data**에서 전체 데이터 사본을 요청하는 방법도 소개합니다. 두 내보내기의 포함 정보는 다르므로, 게시물 통계 파일 하나에 프로필과 연결 정보가 모두 들어 있다고 가정하지 마세요.

## 개인 이름 대신 집계된 관계로 표현하기

원문의 이미지 프롬프트는 얼굴 사진과 내보내기 파일을 참고해 역할, 가치관, 하는 일, 관계망을 그리도록 구성됩니다. 특히 연결 관계는 개인 이름이나 실제 인물 사진 대신 **산업·직무별 집계와 일반적인 실루엣**으로 표현하도록 합니다.

아래는 그 취지를 간추린 한국어 예시입니다. 실제 자료를 사용할 때는 먼저 업로드할 도구가 조직 정책상 허용되는지 확인하고 불필요한 개인정보를 제거하세요.

```text
첨부한 자료에 있는 정보만 바탕으로 내 업무 맥락을 시각적으로 정리해 줘.
현재 역할과 스킬, 반복되는 게시물 주제를 구분해 표현해 줘.
연결 관계는 산업과 직무별로 집계하고 개인 이름·사진은 표시하지 마.
자료에 없는 항목은 추측하지 말고, 확인할 수 없다고 표시해 줘.
이미지에 들어가는 수치와 문구가 원자료와 맞는지 검토해 줘.
```

![Rabia Williams가 LinkedIn 데이터로 만든 역할·관심사·관계망 시각화 예시](/mwkorea/assets/images/2026-07-13-AgenticWorkContextDesign/image3.png)

저자는 자신의 내보내기 자료를 사용했을 때 예상한 직무 요약을 넘어, 그동안 의식하지 못했던 산업별 관계망을 발견했다고 설명합니다. 개인적 경험을 소개한 것이므로 다른 데이터에서도 같은 발견이 보장되는 것은 아닙니다.

## 공개 가능한 결과인지 마지막으로 확인

Work IQ나 내보내기 자료를 이용한 결과에는 함께 일하는 사람, 고객, 프로젝트, 조직 정보가 드러날 수 있습니다. 원문도 공개 게시 전에 이런 내용을 검토하고 조직의 개인정보·정보보호 지침을 따르라고 안내합니다.

본인의 데이터 사본에도 다른 사람의 정보가 들어 있을 수 있습니다. 파일을 확보했다는 사실만으로 모든 외부 도구에 업로드하거나 결과를 공개할 권한이 생기는 것은 아닙니다. 집계 결과도 너무 작은 그룹이나 구체적인 설명으로 개인이 드러나지 않는지 살펴봐야 합니다.

좋은 맥락은 답변을 더 개인화하는 데서 끝나지 않습니다. **무엇을 근거로 했고, 어디까지 사용할 수 있으며, 누가 결과에 책임지는지**를 설명할 수 있어야 팀에서 다시 쓰는 업무 방식이 됩니다.

---

> **출처**
>
> - Copilot Camp: [Why Context Became the Real Differentiator in Agentic Work](https://microsoft.github.io/copilot-camp/pages/beyond-labs/blogs/context-and-viral-prompt-impact/)
> - 참고 프롬프트: [M365 WorkIQ Persona Sketch](https://github.com/pnp/copilot-prompts/tree/main/samples/prompts/m365-workiq-persona-sketch)
>
> 자세한 내용은 원문 참조. 원문 작성자: Rabia Williams. 파일 날짜는 원문의 발행일 2026년 7월 13일을 따르며, 이번 소개 작성일은 2026년 9월 13일입니다.
>
> 이미지 출처: Microsoft Copilot Camp 공개 저장소. Copyright (c) Microsoft Corporation, [MIT License](/mwkorea/assets/images/2026-07-13-AgenticWorkContextDesign/LICENSE.txt). 첫 번째 이미지는 웹 표시용으로 비율을 유지해 축소했습니다.
