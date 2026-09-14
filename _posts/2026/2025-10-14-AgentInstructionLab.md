---
title: "한 줄 지침에서 일관된 에이전트로: ShowExpert로 배우는 지침 개선 실습"
date: 2025-10-14T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotCamp
  - DeclarativeAgents
  - AgentInstructions
  - Microsoft365AgentsToolkit
  - AgentBuilder
  - Evaluation
excerpt: "영상 추천 에이전트 ShowExpert를 만들며 역할, 실행 순서, 응답 원칙과 대화 예시를 단계적으로 보강하는 실습입니다. 지침을 바꿀 때마다 같은 질문으로 다시 평가하고, 개인정보와 불확실성 처리도 함께 설계하는 방법을 소개합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 한 줄 지침에서 일관된 에이전트로: ShowExpert로 배우는 지침 개선 실습

“볼 만한 프로그램을 추천해 줘”라는 역할만 부여해도 에이전트는 답을 만들 수 있습니다. 하지만 사용자의 취향을 먼저 묻는지, 추천 이유를 설명하는지, 모르는 정보를 솔직히 말하는지까지 일관되게 기대하기는 어렵습니다.

Copilot Camp의 **Agent Instruction Lab**은 스트리밍 프로그램 추천 에이전트 **ShowExpert**를 통해 지침을 조금씩 바꾸고 결과를 비교하는 실습입니다. 최종 프롬프트를 한 번에 붙여 넣기보다, 어떤 변경이 어떤 응답 차이를 만드는지 관찰하는 데 초점을 맞춥니다.

원문 발행일은 **2025년 10월 14일**입니다. 이 글은 기존 실습을 2026년 9월 13일 소개하면서 현재 Microsoft Learn의 지침 작성 안내를 함께 참고했습니다. 원문의 도구 화면과 현재 메뉴는 다를 수 있습니다.

---

## 목표를 먼저 정하고 반복해서 평가

ShowExpert의 목표는 사용자가 무엇을 볼지 결정하도록 돕는 것입니다. 친근하게 대화하고, 취향을 확인하며, 추천한 프로그램의 정보와 추천 이유를 제공하도록 설계합니다.

![목표 대비 응답을 평가하고 지침을 수정하는 반복 개선 흐름](/mwkorea/assets/images/2025-10-14-AgentInstructionLab/image1.png)

원문은 콘텐츠를 찾는 데 연간 약 **110시간**을 쓴다는 수치를 동기로 제시하지만, 본문에서 조사 출처를 확인할 수 없습니다. 따라서 이 수치를 검증된 도입 성과나 절감 시간으로 사용하지 않고, 프로그램 선택이라는 반복 문제 자체에 집중하는 것이 좋습니다. 원문의 “일주일” 비유도 110시간의 정확한 근무 시간 환산으로 받아들이면 안 됩니다.

![취향 파악, 웹 자료 분석, 추천, 선택을 잇는 의사결정 흐름](/mwkorea/assets/images/2025-10-14-AgentInstructionLab/image2.png)

## 시작에 필요한 것

Copilot 접근과 지침을 수정·시험할 도구가 필요합니다. 원문은 Microsoft 365 Agents Toolkit을 사용하지만, 지침을 단계적으로 개선하는 방법은 Agent Builder나 Copilot Studio에서도 시험할 수 있다고 설명합니다. 다만 도구 간 배포 방식과 기능까지 같다는 뜻은 아닙니다.

Toolkit 경로를 이용한다면 [Lab E1B](https://microsoft.github.io/copilot-camp/pages/extend-m365-copilot/01-first-agent-toolkit/)의 개발 환경 준비를 먼저 진행합니다. 원문의 프로젝트 생성 순서는 **Create a New App > Declarative Agent > No Action**, 프로젝트 위치와 이름 지정입니다.

프로젝트의 `appPackage` 아래에서 `declarativeAgent.json`과 연결된 지침 파일을 수정합니다. 원문은 `instruction.txt`를 사용하며, 선택 사항으로 **192×192** 아이콘 교체도 소개합니다. 지침 파일의 실제 이름과 참조는 생성된 프로젝트에 맞춰야 합니다.

원문은 웹 검색을 사용하도록 `declarativeAgent.json`에 다음 속성을 추가합니다. 아래는 전체 manifest가 아니라 기존 JSON에 병합할 일부입니다.

```json
{
  "capabilities": [
    {
      "name": "WebSearch"
    }
  ]
}
```

이 선언만으로 모든 환경에서 웹 검색이 허용된다고 가정해서는 안 됩니다. 지원 여부와 조직 설정을 확인하고, 원문처럼 **Provision** 후 Copilot에서 에이전트를 열어 시험합니다. 다른 제작 도구에서는 해당 도구의 저장·배포 절차를 따릅니다.

## 1. 한 줄 지침으로 기준 응답 만들기

처음에는 “온라인 스트리밍 프로그램을 추천하는 에이전트”라는 최소한의 지침으로 시작합니다. “오늘 볼 프로그램을 추천해 줘”처럼 이후에도 반복할 질문을 정하고 응답을 남겨 둡니다.

![기본 지침만 적용한 ShowExpert의 응답 예시](/mwkorea/assets/images/2025-10-14-AgentInstructionLab/image3.png)

기준 응답이 있어야 다음 변경의 효과를 비교할 수 있습니다. 처음부터 모든 조건을 넣기보다 사용자의 취향 확인이나 추천 이유처럼 아직 부족한 행동을 구체적으로 기록하세요.

## 2. 역할과 목적을 분명하게

원문은 스트리밍 프로그램의 리뷰와 추천을 전문으로 하고, 사용자가 즐길 만한 콘텐츠를 발견하도록 돕는 역할을 부여합니다. 장단점을 편향되지 않게 설명하는 방향도 함께 제시합니다.

![역할과 목적을 보강한 뒤의 응답 예시](/mwkorea/assets/images/2025-10-14-AgentInstructionLab/image4.png)

`description`에는 에이전트를 알아볼 수 있는 설명을 쓰고, 실제 행동 지시는 지침에 담는 편이 명확합니다. 원문의 개인 인사 예시를 적용할 때도 사용자 이름을 임의로 추정하지 말고 자발적으로 제공한 정보만 사용하도록 해야 합니다.

## 3. 실행 순서와 전환 조건 넣기

추천 업무라면 요청을 리뷰·추천·질문으로 구분하고, 선호가 부족할 때 먼저 질문한 뒤 후보를 좁히는 순서가 필요합니다. “취향을 고려해”라는 표현보다 **언제 확인 질문을 하고 언제 추천할지**를 적는 것이 실무적으로 유용합니다.

![실행 단계를 추가한 ShowExpert의 대화 예시](/mwkorea/assets/images/2025-10-14-AgentInstructionLab/image5.png)

아래는 원문과 공식 지침 작성 원칙을 바탕으로 간추린 한국어 예시입니다.

```text
역할: 사용자의 선호에 맞는 스트리밍 프로그램 선택을 돕는다.

1. 요청이 추천, 리뷰, 사실 질문 중 무엇인지 구분한다.
2. 사용자가 직접 알려 준 장르와 좋아한 작품을 확인한다.
3. 추천에 필요한 선호가 부족하면 확인 질문을 하고 답을 기다린다.
4. 선호가 확인되면 적합한 후보 2~3개와 간단한 추천 이유를 제시한다.
5. 확인하지 못한 평점이나 제공 여부는 추측하지 않고 한계를 설명한다.
```

결과에는 사용자가 이해할 수 있는 짧은 추천 근거면 충분합니다. 내부 추론 과정을 길게 노출하는 것을 실습의 목표로 삼을 필요는 없습니다.

## 4. 응답 형식과 개인정보 원칙 정하기

원문은 요청 종류에 따라 출력 내용을 구분합니다.

| 요청 | 응답에 담을 내용 |
|---|---|
| 리뷰 | 기본 정보, 평점, 비평·시청자 반응, 필요 시 시청 주의사항과 적합성 |
| 추천 | 선호에 맞는 2~3개 후보, 기본 정보, 추천 이유 |
| 사실 질문 | 간결한 답변, 모호하면 확인 질문, 자료가 없으면 한계 설명 |

원문은 리뷰에 대표 인용 **2~3개**도 제안하지만, 실제 출처가 확인된 경우에만 사용할 수 있습니다. 예시 속 평점과 인용을 최신 사실로 복사하거나 응답 형식을 채우기 위해 없는 평가를 만들어서는 안 됩니다.

![응답 형식과 운영 원칙을 보강한 결과](/mwkorea/assets/images/2025-10-14-AgentInstructionLab/image6.png)

개인정보와 한계도 지침의 일부입니다. 사용자가 제공한 정보만 이용하고, 최근 작품 정보가 제한적일 수 있음을 알리며, Netflix 계정이나 시청 이력에 직접 접근한다고 주장하지 않도록 합니다. 친근한 말투보다 이런 경계가 먼저 명확해야 합니다.

## 5. 대화 예시로 원하는 행동 보여 주기

원문은 최소 **두 개의 예시**를 권하고, 여러 턴이 이어지는 업무라면 후속 질문도 포함하도록 제안합니다. 중요한 것은 예시의 길이보다 지침만으로 모호했던 행동을 보여 주는 것입니다.

```text
사용자: SF 프로그램을 추천해 줘.
에이전트: 좋아했던 SF 작품이나 피하고 싶은 분위기가 있나요?

사용자: 이 작품의 현재 평점은 몇 점이야?
에이전트: 현재 평점을 확인할 수 있는 자료가 없습니다.
          확인되지 않은 숫자 대신, 제공해 주신 정보로 특징을 설명할 수 있습니다.
```

첫 예시는 정보가 부족할 때 질문하는 행동, 두 번째는 확인하지 못한 사실을 꾸미지 않는 행동을 보여 줍니다. 이런 예시는 일반적인 요청과 실패하기 쉬운 요청을 함께 시험하는 데 도움이 됩니다.

![대화 예시까지 반영한 ShowExpert의 응답 흐름](/mwkorea/assets/images/2025-10-14-AgentInstructionLab/image7.gif)

## 지침을 바꾼 뒤에는 새 대화에서 다시 시험

원문은 변경할 때마다 Provision으로 반영하고 새 대화에서 같은 방식으로 시험합니다. 앞선 대화 맥락의 영향을 줄이면서 역할, 단계, 응답 형식, 예시가 기대한 행동으로 이어지는지 확인하는 방식입니다.

여기서 “fine tune”은 지침을 반복해서 다듬는다는 의미로 읽어야 합니다. 모델 가중치를 재학습하는 파인튜닝 절차를 수행하는 실습은 아닙니다.

원문은 지침 전체를 **8,000자 이내**로 유지하도록 안내합니다. 최신 Microsoft Learn도 이 제한을 우회하려고 SharePoint 같은 지식 원본에 지침을 옮기는 방법을 권하지 않습니다. 지식 자료는 응답의 근거이지 제작자가 작성한 지침을 대신하는 저장소가 아니기 때문입니다.

또한 모델이 업데이트되면 행동이 달라질 수 있습니다. 실습을 한 번 마친 뒤 끝내지 말고 기준 질문을 남겨 두고 다시 평가하세요. 커스텀 스킬은 현재 별도 패키지 구성 요소로 설명되므로, 오래된 글의 “skills” 표현을 모두 현재의 `SKILL.md` 업로드 기능으로 해석하지 않는 것도 중요합니다.

## 원문에 포함된 참고 영상

{% include video id="hzNhQGYDz4w" provider="youtube" %}

이 실습의 목표는 프롬프트를 길게 만드는 것이 아닙니다. 역할과 범위를 정하고, 필요한 순서와 예외를 명확히 하며, 실제 대화로 일관성을 확인하는 습관을 만드는 것입니다. 콘텐츠 추천 대신 사내 문서 안내나 제품 비교를 맡기는 에이전트에도 같은 개선 방식을 적용해 볼 수 있습니다.

---

> **출처**
>
> - Copilot Camp: [Agent Instruction Lab - Improve your agent instructions (Beginner friendly)](https://microsoft.github.io/copilot-camp/pages/beyond-labs/blogs/beginner-agent/)
> - Microsoft Learn: [Write effective instructions for declarative agents](https://learn.microsoft.com/microsoft-365/copilot/extensibility/declarative-agent-instructions)
>
> 자세한 내용은 원문 참조. 원문 작성자: Rabia Williams. 발행일은 원문에 표시된 2025년 10월 14일을 유지했습니다. 이번 글 작성 및 관련 문서 확인일은 2026년 9월 13일입니다.
>
> 원문의 이미지 상대 경로가 404를 반환하여 [공개 저장소의 동일 자료](https://github.com/microsoft/copilot-camp/tree/30c48b468d51661c7de2ad93ac2fbcf9a8fbc9ea/docs/assets/images/copilot-instructions)에서 복구했습니다. Copyright (c) Microsoft Corporation, [MIT License](/mwkorea/assets/images/2025-10-14-AgentInstructionLab/LICENSE.txt).
