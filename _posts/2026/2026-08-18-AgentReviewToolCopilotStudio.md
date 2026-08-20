---
title: "\"Preview에서 잘 되는데요?\"로는 부족합니다: Agent Review Tool로 배포 전 에이전트 점검하기"
date: 2026-08-18T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Agent
  - AgentReviewTool
  - CopilotAgentKit
  - GitHubCopilotHarness
  - Skills
  - Governance
excerpt: "Copilot Studio 에이전트가 Preview 탭에서 잘 동작한다고 배포 준비가 끝난 것은 아닙니다. Agent Review Tool은 저장된 구성 자체를 점검해 스킬 중복, 존재하지 않는 기능 참조, 평가 커버리지 공백 같은 위험을 근거와 함께 찾아냅니다. MCSCAT 팀이 가상의 ZAVA 에이전트로 보여 준 배포 전 점검 워크플로를 따라가 봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# "Preview에서 잘 되는데요?"로는 부족합니다: Agent Review Tool로 배포 전 에이전트 점검하기

Copilot Studio에서 에이전트를 만들고 **Preview** 탭에서 몇 가지 질문을 던져 봅니다. 답변도 괜찮고, 도구도 제대로 호출됩니다. 다음 환경으로 넘길 준비가 된 것 같습니다.

그런데 배포하기 전에 이런 질문에 답할 수 있으신가요? **지시문(instructions), 스킬(skills), 도구(tools), 지식 소스(knowledge sources), 평가 커버리지, 연결된 에이전트 구조를 체계적으로 검토했는가?**

지시문 하나에 스킬 하나뿐인 에이전트라면 전부 눈으로 확인할 수 있습니다. 하지만 에이전트는 그렇게 작게 머물러 주지 않습니다. 규모가 커지면 구성이 여러 화면에 흩어지고, 스킬 하나하나는 멀쩡한데 서로 역할이 겹치거나, 도구는 제대로 설정됐는데 참조가 모호하거나, 지식 소스는 있는데 스킬이 그것을 쓸 방향을 주지 않는 상황이 생깁니다. Preview는 **특정 입력 조합이 나타나기 전까지 이런 문제를 드러내지 않습니다.**

Microsoft Copilot Studio Customer Advisory Team(MCSCAT)이 2026년 8월 18일 공개한 글은 이 문제를 다룹니다. Copilot Agent Kit에 포함된 **[Agent Review Tool](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/kit-overview)** 로 배포 전 점검을 반복 가능한 절차로 만드는 방법입니다.

![Agent Review Tool for Copilot Studio Agents](/mwkorea/assets/images/2026-08-18-AgentReviewToolCopilotStudio/image1.png)

> 원문 기준(2026년 8월 18일) Agent Review Tool은 **미리 보기(preview) 경험**으로 제공되며, 평가기와 화면 구성은 변경될 수 있습니다.

---

## Preview 탭만으로는 왜 부족한가

대화를 테스트하는 것은 필수입니다. 다만 대화 하나는 **그 입력에 대해 선택된 경로만** 실행합니다. 다음과 같은 것들은 자동으로 알려 주지 않습니다.

- 두 스킬의 책임 범위가 겹치는가
- 스킬 설명이 "언제 이 스킬을 써야 하는지" 판단에 도움이 되는가
- 지시문이 경계와 에스컬레이션 동작을 정의하고 있는가
- 구성된 기능들에 대표성 있는 평가 커버리지가 있는가
- 스킬이 도구나 지식 소스를 유지보수 가능한 수준으로 명확히 참조하는가
- 구조적 관계가 실제 구성된 것인지, 작성된 텍스트에서 유추된 것인지, 런타임에서 관찰된 것인지

Agent Review Tool은 런타임 테스트를 **대체하지 않고 보완합니다.** 저장된 구성을 점검해 메이커가 조사할 수 있는 발견 사항(findings)을 만들어 냅니다.

| 검토 방법 | 답할 수 있는 질문 |
|---|---|
| Preview 및 평가(evaluations) | 이 대화들에서 에이전트가 기대대로 동작했는가? |
| Agent Review | 저장된 구성에 품질·명확성·커버리지·유지보수성 위험이 있는가? |

**어느 쪽도 단독으로 "프로덕션 준비 완료"를 보증하지 않습니다.** 둘을 함께 써야 더 유용한 그림이 나옵니다.

---

## 워크스페이스 구성

원문은 GitHub Copilot harness 기반의 가상 소매 비주얼 머천다이징 에이전트 **ZAVA Visual Merchandiser** 를 예시로 사용합니다. (다운로드 가능한 샘플이 아니라 설명용 가상 에이전트입니다.)

리뷰를 완료하면 워크스페이스가 세 개 섹션으로 열립니다.

- **Review** — 발견 사항, Skill evaluator, 평가 커버리지, 전체 체크 목록
- **Agent map** — 검토된 아키텍처의 그래프·목록 뷰
- **Cost & efficiency** — 관찰된 활동 신호, 개선·검증 가이드, 계획 범위

원문은 앞의 두 섹션에 집중합니다. 비용·효율 영역은 계획 범위와 관찰 활동의 **근거 경계가 구성 검토와 다르기 때문에** 별도 논의가 필요하다고 밝히고 있습니다.

리뷰는 **결정론적(deterministic) 체크와 AI 지원 분석을 결합**해 수행되며, 발견 사항은 해당 리뷰에서 수집된 근거에 기반합니다.

![리뷰 요약 화면](/mwkorea/assets/images/2026-08-18-AgentReviewToolCopilotStudio/image2.png)

이 워크스루의 **기준선(baseline) 리뷰 점수는 63%, 54개 체크 중 39개 통과**였습니다.

---

## 1단계: 점수가 아니라 발견 사항에서 시작하기

리뷰 요약은 점수와 함께 오류(error)·경고(warning)·정보(informational) 항목의 분포를 보여 줍니다. 점수는 요약으로 유용하지만, **무엇을 조사하고 개선할지 알려 주는 것은 개별 발견 사항과 그 근거**입니다.

GitHub Copilot harness 기반 에이전트의 경우 **grounded score**는 평가 준비도와 지시문에 대해 결정론적·규칙 기반 pillar를 사용하고, 에이전트에 스킬·도구·지식 소스·연결된 에이전트가 있으면 pillar가 추가됩니다. **AI 지원 발견 사항은 보조 근거로 표시될 뿐 결정론적 pillar 점수를 바꾸지 않습니다.**

> 높은 점수가 런타임 품질을 증명하지 않고, 낮은 점수가 실패를 증명하지도 않습니다. 발견 사항을 보고 **무엇을 조사할지, 다음에 어떤 평가를 돌릴지** 결정하는 데 쓰세요.

### 기준선을 먼저 기록하세요

무언가를 바꾸기 전에 다음을 적어 둡니다.

- 전체 점수
- 오류·경고 개수
- 평가된 스킬 수
- 가장 약한 스킬 차원(dimension)
- 교차 스킬 오케스트레이션 발견 사항
- 구성된 기능에 대한 평가 커버리지

이렇게 해 두면 두 번째 리뷰에서 "좀 나아진 것 같다"보다 훨씬 쓸모 있는 비교가 가능합니다.

### Review findings로 분류하기

**Review findings**를 먼저 엽니다. 기능 인벤토리가 수집된 내용을 요약하고, 심각도 필터로 결과를 좁힐 수 있습니다. 발견 사항은 규칙 계열(rule family)별로 묶이며, 하나를 선택하면 **근거·근거 설명·권고·수정 절차·참고 자료**가 함께 열립니다.

여기서 가장 빠르게 답할 수 있는 세 가지 질문입니다.

1. 이번 릴리스 전에 반드시 처리해야 할 발견 사항은 무엇인가?
2. 어떤 기능이나 구성 영역에서 발생했는가?
3. 근거가 에이전트에서 직접 확인할 수 있을 만큼 구체적인가?

![Review findings 화면](/mwkorea/assets/images/2026-08-18-AgentReviewToolCopilotStudio/image3.png)

Review findings는 **무엇을 조사할지**를 알려 줍니다. 그 문제가 하나뿐인지 스킬 전반에 반복되는지는 Skill evaluator가, 주변 구성 맥락은 Agent map이 채워 줍니다.

---

## 2단계: 패턴으로 스킬 품질 점검하기

**Skill evaluator**를 엽니다. 기본값인 **Group by pattern** 뷰는 평가된 모든 스킬의 결과를 묶어 평균 품질, 안전 플래그, 가장 약한 루브릭 차원, 교차 스킬 오케스트레이션 발견 사항을 요약합니다.

지시문 품질은 네 가지 루브릭 차원으로 평가됩니다.

| 차원 | 확인할 내용 |
|---|---|
| **Clarity**(명확성) | 스킬을 언제 선택해야 하는지를 구체적이고 모호하지 않은 표현으로 서술하는가? |
| **Actionability**(실행 가능성) | 단계가 실행 가능하고 순서가 있으며, 필요한 입력·출력·예외 상황·검증이 분명한가? |
| **Scope discipline**(범위 규율) | 하나의 일관된 작업만 수행하며, 경계가 명확하고 무관한 책임이 섞이지 않았는가? |
| **Composability**(조합 가능성) | 상위 지시문 및 형제 스킬과 겹침·모순·숨은 의존성 없이 함께 동작할 수 있는가? |

같은 화면에서 **Bundle integrity, Resource safety, Operational readiness** 도 함께 보고됩니다. 이 결과들은 위 네 가지 지시문 품질 차원과는 **별개** 항목입니다.

이 차원들이 GitHub Copilot harness 기반 에이전트에서 특히 중요한 이유는, 스킬 품질이 `SKILL.md` 하나의 내용만으로 결정되지 않기 때문입니다. 에이전트는 **가용한 모든 대안과 그 스킬을 구별할 수 있어야** 합니다.

![Skill evaluator - 패턴별 그룹 뷰](/mwkorea/assets/images/2026-08-18-AgentReviewToolCopilotStudio/image4.png)

### "By skill"로 실제 수정 지점 찾기

그룹 뷰가 "약점이 반복되는가"를 알려 준다면, **By skill** 뷰는 "어디를 고쳐야 하는가"를 알려 줍니다.

ZAVA의 경우 `display-audit` 스킬이 지목됐습니다. 다섯 단계 중 두 단계가 **Merchandising Scorecard** 와 **Regional Escalation Agent** 를 언급했는데, **두 기능 모두 에이전트에 구성되어 있지 않았습니다.** Agent Review는 이를 **Skill References a Capability the Agent Does Not Have** 규칙의 오류로 표시했습니다.

해당 스킬의 점수는 **Actionability 4/10, 지시문 품질 61%** 였습니다. 즉 에이전트는 작성된 대로는 컴플라이언스 스코어링이나 에스컬레이션 단계를 완료할 수 없는 상태였습니다.

![스킬 발견 사항 - 수정 전](/mwkorea/assets/images/2026-08-18-AgentReviewToolCopilotStudio/image5.png)

좋은 발견 사항은 문제를 일으킨 **지시문이나 스킬 텍스트를 직접 가리켜** 메이커가 확인하고 고치기 쉽게 만듭니다. AI 지원 평가를 사용할 수 없는 경우, Agent Review는 **해당 체크를 통과로 처리하지 않고 사용 불가 상태로 표시**합니다.

---

## 3단계: Agent map으로 주변 아키텍처 확인하기

스킬 발견 사항은 구조적 맥락 안에서 볼 때 이해가 더 잘 됩니다. **Agent map**을 열어 저장된 리뷰에 포착된 구성 요소를 확인합니다.

맵에는 리뷰에서 수집된 지원 구성 요소가 포함되며, 검색·필터로 그래프를 좁힐 수 있습니다. **Map**과 **List**는 같은 필터 결과를 시각적·의미적으로 각각 보여 줍니다.

ZAVA 사례에서는 문제가 된 스킬과 관련 도구·지식 소스로 맵을 필터링한 뒤 이렇게 물었습니다.

1. 참조된 기능이 실제로 에이전트에 구성되어 있는가?
2. 스킬이 그 기능의 구성된 이름을 명확하고 일관되게 사용하는가?
3. 다른 메이커가 이 스킬이 언제·왜 그 기능을 쓰는지 이해할 수 있는가?

![Agent map 화면](/mwkorea/assets/images/2026-08-18-AgentReviewToolCopilotStudio/image6.png)

> Agent map은 **검토된 구성과 작성된 참조**를 설명합니다. 에이전트의 런타임 계획을 재구성하거나, 도구·지식 소스·스킬·연결된 에이전트가 실제로 호출되었음을 증명하지는 않습니다.

---

## 4단계: 하나만 집중해서 고치기

근거가 지목한 지시문이나 구성만 바꿉니다. ZAVA를 수정하기 전에 의도한 수정 내용을 문서화하고, 무관한 동작에 영향을 주지 않는지 확인했습니다.

`display-audit`에 대해서는 **새 기능을 추가하는 대신 스킬을 다시 작성하는 쪽**을 택했습니다.

| 기준선 문제 | 적용한 수정 |
|---|---|
| 스킬이 **Merchandising Scorecard** 와 **Regional Escalation Agent** 를 참조했으나 두 기능 모두 ZAVA에 구성되어 있지 않음 | 해당 단계들이 실제 구성된 기능을 사용하도록 변경: **Planogram Archive**, **Display Photo Library**, **ZAVA 비주얼 머천다이징 표준** 지식 소스, **ZAVA Store Ops Assistant** |

이 수정은 참조된 모든 기능이 실제로 에이전트에 존재하게 만들어 근거를 직접 해소합니다. 동시에 스킬의 원래 목적 — 진열을 점검하고, 가용한 머천다이징 표준에 비추어 평가하고, 후속 조치를 구성된 어시스턴트로 라우팅 — 도 유지합니다.

> 원문은 정확한 단계 텍스트가 보존되지 않아 위 표가 **개념적 요약**이며 그대로 복사해 쓸 수 있는 스킬 가이드가 아니라고 명시합니다.

### 수정 후 절차

1. 변경된 스킬을 가장 많이 사용할 대화와 평가를 실행합니다.
2. 라우팅과 출력이 여전히 의도대로 동작하는지 확인한 뒤 Agent Review를 다시 실행합니다.
3. 스킬 차원, 오케스트레이션 발견 사항, 근거를 기준선과 비교합니다.
4. Agent map을 다시 열어 구성 뷰가 의도한 아키텍처를 반영하는지 확인합니다.

---

## 결과 비교

| 지표 | 기준선 리뷰 | 두 번째 리뷰 |
|---|---|---|
| Grounded configuration score | 63% | **67%** |
| 통과한 체크 | 39 / 54 | **51 / 54** |
| 오류(Errors) | 8 | **0** |
| 경고(Warnings) | 7 | **2** |
| 평균 스킬 품질 | 64% | **90%** |
| 평가 커버리지 | 0 / 7 | 0 / 7 |

![두 번째 리뷰 요약](/mwkorea/assets/images/2026-08-18-AgentReviewToolCopilotStudio/image7.png)

여기서 눈여겨볼 지점이 있습니다. **체크는 54개 중 51개가 통과했는데 점수는 67%에 그쳤습니다.** 이유는 **Evaluation이 pillar 가중 grounded score에서 고정적으로 30% 비중을 차지**하기 때문입니다. 테스트 커버리지가 0/7로 남아 있는 한 점수 상승에 한계가 있습니다.

![두 번째 Skill evaluator 결과](/mwkorea/assets/images/2026-08-18-AgentReviewToolCopilotStudio/image8.png)

Skill evaluator는 **평균 품질 90%, 안전 플래그 없음, 교차 스킬 오케스트레이션 발견 사항 1건**을 보고했습니다.

원문은 정직하게 한계도 밝힙니다. `display-audit`의 최종 지시문 품질 수치는 보존된 근거에 없어 스킬별 변화량을 정확히 주장하지 않으며, 런타임 평가 결과도 별도로 보존되지 않았습니다. 즉 이 워크스루가 증명한 것은 **구성 관련 발견 사항이 해소되었다는 것이지, 런타임 동작이 개선되었다는 것은 아닙니다.**

오류 하나를 해결하자 발견 사항 목록이 비는 대신 **다음 우선순위가 드러났습니다.** 남은 경고 2건은 누락된 평가 테스트 세트와 지시문 문자 위생(instruction-character hygiene)에 관한 것이었고, Skill evaluator는 네 스킬에 걸친 **Capability Coverage Gap** 1건을 추가로 표시했습니다.

> 발견 사항은 사라졌는데 런타임 평가가 나빠졌다면, 개선된 것은 에이전트가 아니라 리뷰 결과입니다. 목표는 점수를 따는 것이 아니라 **에이전트를 더 명확하고 신뢰할 수 있으며, 다음 메이커가 이해하기 쉽게 남기는 것**입니다.

---

## Agent Review Tool이 주장하지 않는 것

원문은 도구의 경계를 명확히 선을 긋습니다. Agent Review Tool은 조사를 **안내**할 뿐, 다음을 하지 않습니다.

- 에이전트를 프로덕션 준비 완료로 **인증하지 않습니다**
- 원본 에이전트를 **수정하지 않습니다**
- 대표성 있는 테스트 케이스나 사람의 검토를 **대체하지 않습니다**
- 구성된 기능이 실제로 실행되었음을 **증명하지 않습니다**
- 비용 계획·관찰 활동 뷰는 실제 청구 금액을 보고하거나 절감을 보장하지 **않습니다**

---

## 한국 메이커·도입 담당자를 위한 체크포인트

- **설치 경로**: Agent Review Tool은 [Microsoft Marketplace](https://marketplace.microsoft.com/en-us/product/dynamics-365/microsoftpowercatarch.copilotstudiokit2)의 **Copilot Agent Kit**을 통해 제공됩니다. 설치·접근 요구 사항은 [Agent Review Tool 참조 가이드](https://github.com/microsoft/Power-CAT-Copilot-Studio-Kit/blob/2e1a9883f73669d410d33c38a3a4527744df90a4/AGENTREVIEWTOOL_REFERENCE_GUIDE.md)에 정리되어 있습니다.
- **평가 커버리지를 먼저 확보하세요**: Evaluation이 grounded score에서 **고정 30%** 를 차지합니다. 체크를 아무리 통과해도 테스트 세트가 없으면 점수 상한이 생깁니다. 스킬 지시문을 다듬는 것과 별개로 **대표 평가 케이스 확보**를 병행해야 합니다.
- **"존재하지 않는 기능 참조"를 우선 점검하세요**: 이번 사례의 핵심 오류가 이것이었습니다. 스킬 문서를 작성하다 보면 "있으면 좋을 것 같은" 도구·에이전트 이름을 쓰게 되는데, 실제로 구성되지 않았다면 그 단계는 실행될 수 없습니다.
- **한 번에 하나만 고치세요**: 여러 곳을 동시에 바꾸면 개선의 원인을 특정할 수 없습니다. 기준선 기록 → 근거 확인 → 한 가지 수정 → 재리뷰 순서를 지키세요.
- **런타임 검증은 별도로**: 구성 리뷰 통과와 실제 동작 개선은 다른 문제입니다. 수정 후에는 반드시 해당 스킬을 사용하는 대화·평가를 다시 실행해 확인하세요.
- **미리 보기 상태 감안**: 2026년 8월 18일 기준 미리 보기 경험이며, 평가기와 화면 구성이 변경될 수 있습니다.

---

## 마무리

Preview 탭에서 기대대로 동작하는 에이전트는 **더 깊은 검토를 받을 준비가 된 것**이지, 반드시 릴리스할 준비가 된 것은 아닙니다.

Agent Review Tool은 발견 사항, 뒷받침 근거, 스킬 품질, 평가 공백, 구성 관계를 하나의 워크플로에 모아 줍니다. 덕분에 메이커는 "괜찮아 보이는데요"에서 **근거를 따라갈 수 있는 구체적 개선**으로 넘어갈 수 있습니다.

원문은 마지막에 이런 질문을 던집니다. **여러분의 에이전트에서 배포 전 검토가 가장 어려운 부분은 무엇인가요 — 스킬 경계, 평가 커버리지, 아니면 구성된 아키텍처를 이해하는 일인가요?**

---

> **출처**
>
> - 원문 제목: *Review Before Release: Using Agent Review Tool for Copilot Studio Agents*
> - 링크: [https://microsoft.github.io/mcscatblog/posts/agent-review-tool/](https://microsoft.github.io/mcscatblog/posts/agent-review-tool/)
>
> 자세한 내용은 원문을 참조하세요.
