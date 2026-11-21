---
title: "우리 회사의 판단 기준으로 에이전트를 개선한다: Frontier Tuning 비공개 프리뷰 확대"
date: 2026-11-19T00:00:00 KST
categories:
  - Copilot
tags:
  - FrontierTuning
  - GitHubCopilot
  - CopilotCowork
  - WorkIQ
  - Evaluation
excerpt: "Frontier Tuning이 비공개 프리뷰 참여 범위와 제작 도구를 확대합니다. 업무 전문가의 평가 기준, 분리된 학습·평가 샘플, 반복 튜닝과 게시 승인을 연결하는 구조를 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 우리 회사의 판단 기준으로 에이전트를 개선한다: Frontier Tuning 비공개 프리뷰 확대

전문 업무에서 좋은 AI 답변은 단순히 자연스러운 문장만으로 결정되지 않습니다. 어떤 근거를 인용하고, 어디까지 확신하며, 어떤 검토 기준을 지켜야 하는지가 조직마다 다릅니다.

Microsoft는 Ignite에서 Frontier Tuning의 **확대된 비공개 프리뷰**를 발표했습니다. 2026년 6월 Build에서 시작한 프로그램을 확장해, 메이커와 업무 전문가가 직접 튜닝에 참여할 수 있는 도구를 제공합니다. 원문 발행은 11월 18일 UTC이며 이 글의 날짜는 KST 환산 기준입니다.

---

## 제작자와 전문가가 함께 쓰는 도구

GitHub Copilot용 Frontier Tuning 플러그인은 메이커와 업무 전문가가 **Tuning Environment**를 함께 구성하도록 돕습니다. 이 과정에서 Work IQ를 활용해 업무 맥락을 반영합니다.

개발자는 **CLI와 API**를 통해 기존 도구에서 튜닝을 실행하고 튜닝된 스킬을 자체 에이전트에 넣을 수 있습니다. 메이커의 검토를 거친 결과는 Cowork 플러그인으로 게시할 수 있으며, 사용자는 학습 가치가 있는 사례를 환경으로 다시 공유할 수 있습니다.

비공개 프리뷰에서 튜닝 가능한 모델로 원문은 **GPT 6 Luna와 MAI Code 2 Flash**를 명시합니다. Copilot Studio 지원은 가까운 미래의 계획으로 소개됐으며, 이번 발표 시점에 이미 제공되는 기능과 구분해야 합니다.

![Frontier Tuning의 구성과 개선 흐름](/mwkorea/assets/images/2026-11-19-FrontierTuningPrivatePreview/image1.webp)

## Tuning Environment의 네 가지 구성요소

| 구성요소 | 역할 |
|---|---|
| 과제 | 에이전트가 수행할 업무 정의 |
| 루브릭 | 업무 전문가가 정의한 좋은 결과의 평가 기준 |
| 샘플 | 학습용 사례와 별도의 평가용 사례 |
| 도구 | 실제 운영에서 스킬이 사용할 도구 |

학습용과 평가용 샘플을 나누는 이유는 **학습하지 않은 사례에서도 개선되는지 확인하기 위해서**입니다. 운영과 다른 도구나 지식으로만 평가하면 실제 업무 품질을 판단하기 어려워집니다.

튜닝은 hill climbing이라는 반복 과정으로 진행됩니다. 새 버전을 만들고, 평가 샘플에 대해 루브릭으로 채점한 뒤, 개선된 방향을 다음 회차에 반영합니다. 어떤 버전을 사용자에게 제공할지는 메이커가 결정하며, 게시하지 않는 선택도 가능합니다.

서비스는 샘플·도구·루브릭·튜닝된 모델을 저장하고 접근 통제를 제공합니다. 다만 “보안 기능이 있다”는 설명을 조직별 모든 규정 준수 요구가 자동 충족된다는 의미로 확대해서는 안 됩니다.

## 스킬 튜닝과 모델 튜닝의 차이

원문은 많은 팀이 먼저 **스킬 자체를 개선**한다고 설명합니다. 지원 모델을 바꾸며 작업할 유연성을 유지할 수 있기 때문입니다. 더 필요한 경우에는 조직이 관리하는 모델에 전문성을 반영하는 모델 튜닝을 선택합니다.

따라서 도입 초기부터 모델 튜닝만을 전제로 하기보다, 명확한 과제와 루브릭을 먼저 만들고 스킬 개선으로 해결되는 범위를 확인하는 접근이 적절합니다.

## EY 사례에서 읽을 점

EY는 세무 전문가의 조사 업무를 지원하는 Tax Advisor 에이전트에 이 방식을 적용합니다. 세무 방법론, 표현 방식, 검토 기준을 루브릭으로 만들고, 운영 에이전트와 동일한 선례 검색 도구를 연결했습니다.

EY는 자체 품질 기준에서 작은 모델이 프런티어 모델을 앞섰다고 설명하지만, 이는 **해당 조직의 평가 기준에 대한 사례**입니다. 모든 세무 업무나 일반 모델 성능의 우열을 입증한 수치로 해석할 수는 없습니다. 고객에게 제공하는 자문에 대한 책임도 EY 전문가에게 남습니다.

## 시작 조건과 운영상의 체크포인트

확대 대상은 Frontier 프로그램의 더 많은 고객이며, 신청은 [Frontier Tuning 프리뷰 등록](https://aka.ms/FrontierTuning)에서 할 수 있습니다. **비공개 프리뷰 동안에는 Frontier Tuning 요금이 없고**, 확대 제공 전 가격을 안내할 예정입니다. 영구 무료나 GA 발표는 아닙니다.

국내 조직은 실제 업무 사례를 반영한 샘플, 전문가가 합의한 루브릭, 운영 도구 접근 범위, 게시 승인 담당자를 먼저 준비하는 것이 좋습니다. 운영 이후에도 사용자가 공유를 선택한 사례를 반영하고, 요구사항이나 모델이 바뀌면 같은 평가 기준으로 기존 버전과 비교할 수 있습니다.

## 원문 데모와 마무리

{% include video id="jZZaXtzH4yQ" provider="youtube" %}

Frontier Tuning의 중심에는 “더 큰 모델”보다 **조직의 품질 기준을 명시하고 반복 검증하는 과정**이 있습니다. 전문성을 가진 현업과 구현을 맡는 메이커가 함께 평가 체계를 만드는 것이 출발점입니다.

> **출처**: [Frontier Tuning opens to more customers, with new tools for your teams](https://devblogs.microsoft.com/microsoft365dev/frontier-tuning-opens-to-more-customers-with-new-tools-for-your-teams/) — Microsoft 365 Developer Blog. 자세한 내용은 원문 참조.
