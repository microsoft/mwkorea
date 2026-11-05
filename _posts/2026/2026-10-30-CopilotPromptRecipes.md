---
title: "좋은 프롬프트를 반복 가능한 업무 레시피로: Copilot 공유·모델·Skills 활용법"
date: 2026-10-30T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotChat
  - Cowork
  - Prompting
  - Skills
excerpt: "Microsoft Inside Track이 목적·대상·톤·출처·형식으로 프롬프트를 구성하는 방법과 대화 공유, 모델 선택, Skills 재사용을 소개했습니다. Cowork Effort의 다섯 단계와 비용·시간의 관계도 함께 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 좋은 프롬프트를 반복 가능한 업무 레시피로: Copilot 공유·모델·Skills 활용법

“이거 요약해 줘”라고 시작한 뒤 대상과 형식을 여러 번 덧붙이는 경험이 있습니다. 처음 요청에 필요한 재료가 빠져 있으면 왕복 작업도 늘어납니다.

Microsoft Inside Track은 이를 요리에 빗대어 프롬프트 작성과 공유·재사용 방법을 소개합니다. 핵심은 멋진 표현보다 **목표와 완료 형태를 처음부터 분명히 하는 것**입니다.

원문은 기능 제공이 테넌트와 라이선스에 따라 다를 수 있다고 명시합니다. 아래 화면이나 메뉴가 보이지 않는다고 바로 장애로 판단하지 말고 적용 상태를 확인해야 합니다.

---

## 다섯 가지 재료를 먼저 넣기

| 재료 | 적어둘 내용 |
|---|---|
| 목표 | 무엇을 만들거나 해결할지 |
| 대상 | 누가 읽고 어떤 배경지식이 있는지 |
| 톤 | 격식, 간결함, 쉬운 표현 등 |
| 참고 출처 | 사용할 파일·메모·자료 |
| 출력 형식 | 항목 수, 표, 분량 등 완료 형태 |

다음은 이 원칙을 한국 업무에 맞춰 구성한 예시입니다.

> 첨부한 회의 메모와 이번 주 진행 현황을 참고해, 내용을 아직 읽지 않은 팀장들이 5분 안에 검토할 요약을 작성해 줘. 쉬운 표현을 쓰고 핵심 5개와 권장 후속 행동 1개로 정리해 줘.

![Copilot 활용 팁 안내 아이콘](/mwkorea/assets/images/2026-10-30-CopilotPromptRecipes/image1.png)

## 1. 대화 전체와 개별 답변을 공유

원문은 Copilot에서 전체 채팅 또는 개별 응답을 공유하고 수신자가 자신의 대화처럼 이어갈 수 있는 경험을 소개합니다.

전체 대화는 채팅 오른쪽 위 **Share > Share chat**, 개별 응답은 아래쪽 더보기에서 **Share response**를 선택합니다. 공유할 내용의 미리보기를 확인한 뒤 **Copy link**를 누르는 흐름입니다.

![공유 내용 미리보기와 링크 복사 화면](/mwkorea/assets/images/2026-10-30-CopilotPromptRecipes/image2.png)

국내 조직에서는 링크를 보내기 전에 기밀·개인정보와 첨부 내용의 범위를 확인하는 것이 좋습니다. 대화 공유를 원본 파일 권한의 무조건적 부여와 동일하게 해석해서는 안 됩니다.

## 2. 모델과 Effort를 업무에 맞추기

Chat의 모델 선택을 **Auto**로 두면 Copilot이 작업에 맞는 모델을 선택합니다. 원문은 속도와 토큰 사용 측면의 이점을 설명하지만, 고정된 절감률을 제시하지는 않습니다. 결과가 만족스럽지 않으면 모델 선택 드롭다운에서 다른 모델을 시도할 수 있습니다.

![Copilot Chat 모델 선택 메뉴](/mwkorea/assets/images/2026-10-30-CopilotPromptRecipes/image3.png)

Cowork에는 실행 전에 고르는 **Effort**가 소개됩니다.

| 단계 | 원문 안내 |
|---|---|
| Light | 낮은 노력 단계 |
| Medium | 기본값이며 대부분의 작업에 권장 |
| High | 더 높은 노력 단계 |
| Extra High | 높은 노력 단계 |
| Max | 가장 높은 노력 단계 |

**높은 설정일수록 더 오래 걸리고 더 많은 Credits를 사용합니다.** 단순한 작업에 항상 Max를 고르는 것이 효율적인 사용법은 아닙니다. 원문은 요리의 온도에 비유하지만 이를 모델 API의 `temperature` 설정과 같은 개념으로 읽으면 안 됩니다.

![Cowork의 Effort 조정 화면](/mwkorea/assets/images/2026-10-30-CopilotPromptRecipes/image4.png)

## 3. 잘 만든 요청을 Skill로 저장하고 나누기

반복되는 업무에는 목적·자료·절차·세부 기준을 묶은 Skill이 유용합니다. 원문이 설명한 흐름은 다음과 같습니다.

1. Copilot Chat에 Skill이 할 일을 설명하고 ZIP 파일로 패키징해 달라고 요청합니다.
2. Markdown `.md` 파일을 포함한 결과를 받고 **Save skill**로 저장합니다.
3. 응답의 더보기에서 **Share response**로 공유하면 수신자가 Skill ZIP을 받아 활용할 수 있습니다.
4. 추가·게시된 Skill은 왼쪽 **Agents and Skills**에서 찾습니다. 일부만 보이면 **More**를 확인합니다.
5. 목록에서 선택하거나 Copilot·Cowork의 입력란에서 `/`를 입력해 실행할 Skill을 고릅니다.

![Copilot의 Save skill 화면](/mwkorea/assets/images/2026-10-30-CopilotPromptRecipes/image5.png)

Skill은 재사용 가능한 지침이지 결과의 정확성을 보증하는 장치는 아닙니다. 공유받은 Skill도 지침과 참고 자료를 검토하고 조직 정책에 맞는지 확인해야 합니다.

## 작업에 맞는 Copilot 경험 고르기

간단한 생성·브레인스토밍은 Chat, 스프레드시트처럼 특정 앱에 붙은 업무는 해당 Microsoft 365 앱의 Copilot, 여러 출처를 사용하는 긴 다단계 작업은 Cowork라는 구분이 소개됩니다. 이동 중 빠른 작업에는 모바일 경험이 적합할 수 있습니다.

가장 중요한 것은 모든 작업을 가장 무거운 모드로 처리하는 것이 아닙니다. 좋은 입력, 적절한 실행 환경, 재사용 가능한 절차를 함께 정리하면 왕복 작업을 줄이는 데 도움이 됩니다.

> **출처**: [Our best recipes for cooking up better Copilot prompts — Microsoft Inside Track](https://www.microsoft.com/insidetrack/blog/our-best-recipes-for-cooking-up-better-copilot-prompts/). 자세한 내용은 원문 참조.
