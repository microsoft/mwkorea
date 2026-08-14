---
title: "Excel =COPILOT 함수, 정식 출시 계획이 취소됐습니다"
date: 2026-08-14T00:00:00 KST
categories:
  - Copilot
tags:
  - Excel
  - M365Copilot
  - CopilotFunction
  - Formula
  - Roadmap
excerpt: "Excel 수식 안에서 텍스트와 데이터를 생성·분류·요약하도록 계획됐던 =COPILOT 함수의 정식 출시가 취소됐습니다. Microsoft는 동일 기능에 대한 세 개의 로드맵 항목에서 더 이상 진행하지 않기로 했다고 밝혔습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Excel =COPILOT 함수, 정식 출시 계획이 취소됐습니다

Excel 셀에 `=COPILOT()`을 입력해 텍스트와 데이터를 생성하고, 분류하고, 요약하는 기능이 정식 출시될 예정이었습니다. 자연어 AI를 일반 함수처럼 수식에 넣는 방식이라 관심이 큰 기능이었습니다.

그러나 Microsoft가 이 기능을 **더 이상 진행하지 않기로 결정**했습니다.

같은 제목과 설명을 가진 Microsoft 365 Roadmap 항목 세 개(RM499658, RM499659, RM499660)가 동시에 업데이트됐으며, 모두 동일하게 기능 취소를 알리고 있습니다.

---

## 어떤 기능이었나요

예정됐던 `=COPILOT` 함수는 Excel 수식 안에서 직접 Copilot을 호출해 다음 작업을 수행하는 기능이었습니다.

- 텍스트 및 데이터 **생성**
- 항목 **분류**
- 긴 텍스트나 데이터 **요약**

기존 Excel 함수가 정해진 계산 규칙을 수행했다면, `=COPILOT`은 자연어 지시와 생성형 AI를 셀 계산 흐름에 넣는 접근이었습니다.

예를 들어 고객 피드백을 주제별로 분류하거나, 여러 행의 설명을 짧게 요약하거나, 입력값을 바탕으로 문구를 생성하는 시나리오를 수식 형태로 구성할 수 있다는 기대가 있었습니다.

## 취소 공지

세 로드맵 항목에 표시된 문구는 같습니다.

> **이 기능을 더 이상 진행하지 않기로 결정했습니다. 불편을 드려 죄송합니다.**
>
> *We have decided not to move forward with this feature. We apologize for the inconvenience.*

취소 사유나 대체 기능, 재추진 일정은 명시되지 않았습니다. 확인되지 않은 배경을 추측하기보다 **현재 계획상 정식 출시되지 않는다**고 이해하는 것이 정확합니다.

각 항목에는 원래 정식 출시 시점이 **2027년 1월(CY2027 January)**로 표시되어 있었습니다.

---

## 왜 로드맵 항목이 세 개인가

Microsoft 365 Roadmap은 동일 기능을 플랫폼이나 배포 범위에 따라 여러 항목으로 나누는 경우가 있습니다. 이번에는 다음 세 ID가 동일한 제목·설명·예정 시점을 담고 있습니다.

| Roadmap ID | 제목 | 기존 GA 예정 |
|---|---|---|
| **RM499658** | Excel: =COPILOT Function | 2027년 1월 |
| **RM499659** | Excel: =COPILOT Function | 2027년 1월 |
| **RM499660** | Excel: =COPILOT Function | 2027년 1월 |

세 항목 모두 취소 문구가 같으므로 중복 글을 만들지 않고 하나로 정리했습니다.

---

## Excel의 Copilot 자체가 사라지는 것은 아닙니다

이번 공지는 **`=COPILOT` 함수라는 특정 제공 방식**에 관한 것입니다. Excel의 다른 Copilot 기능 전체가 중단된다는 뜻은 아닙니다.

Excel에는 여전히 자연어로 데이터 분석을 요청하고, 수식을 만들고, 차트나 인사이트를 생성하는 Copilot 경험이 있습니다. 따라서 조직의 Excel Copilot 도입 계획을 전부 중단할 필요는 없습니다.

다만 다음과 같은 설계를 `=COPILOT` 함수에 의존했다면 수정이 필요합니다.

- 셀마다 생성형 AI 결과를 계산하는 템플릿
- 수식을 복사해 여러 행을 일괄 분류하는 워크플로
- `=COPILOT` 결과를 다른 함수가 다시 참조하는 계산 구조
- 해당 함수를 전제로 한 교육 자료나 데모

## 가능한 대안

Microsoft가 공식 대체 기능을 지정하지는 않았습니다. 현재 제공되는 기능 범위 안에서는 다음 접근을 검토할 수 있습니다.

### Excel Copilot의 대화형 분석

분류·요약·수식 생성이 목적이라면 Excel의 Copilot 창에서 자연어로 요청하고 결과를 검토하는 방식이 가장 가까운 대안입니다.

### Power Query

반복 가능하고 결정적인 데이터 정리·변환은 생성형 AI 함수보다 Power Query가 더 안정적일 수 있습니다.

### Power Automate 또는 에이전트

대량 텍스트 분류·요약이 필요한 업무라면 Power Automate나 Copilot Studio 에이전트로 처리 흐름을 분리하고, 검토된 결과를 Excel에 기록하는 구조를 고려할 수 있습니다.

### 사용자 지정 Office Scripts·API

개발 역량이 있는 조직은 Office Scripts나 승인된 AI API를 조합할 수 있습니다. 이 경우 비용, 보안, 오류 처리, 재현성을 별도로 설계해야 합니다.

---

## 도입 담당자를 위한 체크포인트

- **로드맵 의존 계획을 수정하세요.** 2027년 1월 출시를 전제로 만든 프로젝트 일정과 PoC 범위에서 `=COPILOT`을 제거해야 합니다.
- **중복 Roadmap ID를 하나의 변경 사항으로 관리하세요.** 세 ID가 있지만 사실상 동일 기능 취소입니다. 변경 관리 시스템에 세 건의 별도 기능으로 등록하지 않도록 주의하세요.
- **교육 자료를 점검하세요.** 미리 보기나 행사 데모를 바탕으로 `=COPILOT` 사용법을 사내 교육에 넣었다면 삭제하거나 취소 상태를 명시해야 합니다.
- **비결정적 결과를 셀 계산에 넣는 위험도 다시 검토하세요.** 생성형 결과를 수식처럼 대량 복제하는 구조는 비용과 결과 재현성, 검토 책임 측면에서도 별도 통제가 필요합니다.
- **공식 대체 발표를 기다리세요.** 현재 공지에는 취소 사유나 후속 기능이 없습니다. 유사 기능이 다른 형태로 제공될지는 별도 발표를 확인해야 합니다.

## 마무리

`=COPILOT` 함수는 생성형 AI를 Excel의 가장 기본적인 상호작용 단위인 **셀과 수식** 안으로 가져오려는 흥미로운 접근이었습니다. 그만큼 취소 소식의 영향도 작지 않습니다.

이번 사례는 로드맵 항목이 확정된 제품 약속이 아니라 변경 가능한 계획이라는 점을 다시 보여 줍니다. 아직 출시되지 않은 기능은 도입 일정의 필수 전제로 삼기보다, 실제 GA가 확인될 때까지 선택 사항으로 관리하는 편이 안전합니다.

---

> **출처**: Microsoft 365 Roadmap — *Excel: =COPILOT Function*
> - **RM499658**: [https://mc.merill.net/message/RM499658](https://mc.merill.net/message/RM499658) / [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap?searchterms=499658)
> - **RM499659**: [https://mc.merill.net/message/RM499659](https://mc.merill.net/message/RM499659) / [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap?searchterms=499659)
> - **RM499660**: [https://mc.merill.net/message/RM499660](https://mc.merill.net/message/RM499660) / [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap?searchterms=499660)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
