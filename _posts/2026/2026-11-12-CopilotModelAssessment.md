---
title: "에이전트 모델을 바꾸기 전에: Model Assessment로 품질·회귀·크레딧 함께 평가하기"
date: 2026-11-12T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - CopilotAgentKit
  - ModelAssessment
  - Evaluation
  - Governance
excerpt: "Copilot Agent Kit의 Model Assessment는 모델 변경 전후의 테스트 결과와 크레딧을 비교합니다. 두 평가 경로의 조건, 실제 모델 변경의 영향, 불완전한 비용 수치를 해석하는 주의사항을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트 모델을 바꾸기 전에: Model Assessment로 품질·회귀·크레딧 함께 평가하기

새 모델이 등장하면 에이전트의 모델 선택을 바꾸기는 쉽습니다. 그러나 설명이 더 자연스러워졌다고 도구 사용, 필수 정보 제공, 비용까지 모두 좋아졌다고 판단할 수는 없습니다.

Microsoft Copilot Studio Customer Advisory Team의 기술 블로그는 **Copilot Agent Kit의 Model Assessment**를 통해 이 결정을 검증하는 방법을 소개합니다. 핵심 질문은 “어떤 모델이 가장 좋은가”가 아니라 “우리 에이전트가 맡은 실제 업무에서 어떤 모델이 더 적합한가”입니다.

원문 발행 메타데이터는 KST 11월 12일에 해당하지만, 수집 시점 본문의 예시는 **2026년 11월 16일 평가 실행**을 다룹니다. 아래 수치는 그 본문 예시 기준이며, 연결된 고정 리비전 설정 문서는 Model Assessment를 **Preview**로 표시합니다.

![Model Assessment 소개](/mwkorea/assets/images/2026-11-12-CopilotModelAssessment/image1.png)

---

## 두 가지 테스트 경로부터 구분하세요

| 구분 | Copilot Studio evaluations | Copilot Agent Kit 테스트 자동화 |
|---|---|---|
| 대상 | Microsoft Copilot harness 및 Standard harness | 현재 Standard harness만 지원 |
| 준비 | 이름에 `MODELCHECK`가 포함된 활성 평가 테스트 세트 | Pipeline Enabled를 켠 Agent Configuration과 Kit 테스트 세트 |
| 평가 대상 버전 | 저장된 초안 | 게시된 에이전트 |
| 크레딧 보고 | Microsoft Copilot harness 평가에서 반환한 소비량을 활용 | Copilot Credits를 보고하지 않음 |

서로 다른 엔진의 결과를 같은 척도로 직접 비교하지 않습니다. 비교 화면에서 모델 추천을 받으려면 **같은 테스트 엔진으로 완료된 실행 두 개**가 필요합니다.

## 설치·권한과 연결 준비

Copilot Agent Kit의 **Advanced Testing > Model assessment**에서 기능을 엽니다. 원문이 연결한 [설정 문서의 고정 리비전](https://github.com/microsoft/Power-CAT-Copilot-Studio-Kit/blob/db22736e71bf6acb813e2e9dd2491e489a8c0f92/MODEL_ASSESSMENT.md#2-prerequisites)은 다음을 요구합니다.

1. 사용자에게 **CSK - Maker 또는 CSK - Administrator** 역할을 부여하고 Kit 코드 앱을 공유합니다.
2. **Model Assessment | Run Copilot Studio Evaluations**, **Model Assessment | Run Copilot Agent Kit Tests** 플로를 모두 켭니다.
3. Dataverse 연결 참조 `cat_CopilotStudioAcceleratorDataverse`와 Copilot Studio 연결 참조 `cat_CopilotStudioKitAutomatedTests`를 설정합니다. Copilot Studio 연결 계정은 평가할 에이전트에 접근할 수 있어야 합니다.
4. 위 표의 조건에 맞는 테스트를 준비하고, 평가 및 AI 프롬프트에 필요한 Copilot Credits 용량을 확보합니다.

설정 문서에는 일부 과거 명칭이 남아 있을 수 있으므로 harness 지원 범위는 원문 본문의 구분과 실제 설치 버전을 함께 확인해야 합니다.

![에이전트별 이전·현재 모델과 평가 상태](/mwkorea/assets/images/2026-11-12-CopilotModelAssessment/image2.png)

## 기준선을 만든 뒤 모델을 바꿉니다

먼저 현재 모델로 **baseline 평가**를 실행합니다. 이후 지침, 지식, 도구, 테스트 케이스, 채점 기준을 유지한 채 후보 모델을 평가해야 모델 변화의 영향을 분리할 수 있습니다. 다른 설정도 바꿨다면 결과와 함께 기록합니다.

특히 **Model Assessment에서 모델을 선택하면 원본 에이전트에 실제 저장됩니다. Kit 테스트 경로에서는 게시까지 수행합니다.** 단순한 가상 비교 화면이 아니므로 개발·테스트 환경의 에이전트에서 진행하는 것이 중요합니다.

![실행 이력을 보존하는 Model history](/mwkorea/assets/images/2026-11-12-CopilotModelAssessment/image3.png)

진행 상태는 Initializing, Running evaluations 또는 Running Kit tests, Scoring results, Generating AI analysis 순으로 표시됩니다. 패널을 닫아도 실행은 계속됩니다. 설정 문서상 에이전트당 동시 평가는 하나만 실행할 수 있습니다.

![평가 실행과 AI 분석 진행 단계](/mwkorea/assets/images/2026-11-12-CopilotModelAssessment/image4.png)

## 예시 비교: 통과율만으로 끝내지 않기

원문은 데모 에이전트 Zava Kit Test Automation의 두 실행을 비교합니다. GPT-6 Luna와 GPT-6.1 Sol은 원문이 참조한 Microsoft Copilot harness 모델 안내에서 GA 모델로 소개되지만, 이 예시는 **특정 에이전트의 평가이지 범용 벤치마크가 아닙니다.**

| 관측값 | GPT-6 Luna | GPT-6.1 Sol |
|---|---:|---:|
| 실행일 | 2026-11-16 | 2026-11-16 |
| 통과 / 실패 검사 | 14 / 4 | 12 / 6 |
| 오류 / 제외 | 0 / 0 | 0 / 0 |
| 공통 검사 통과율 | 77.8% | 66.7% |
| 실행 상태 | Critical | Critical |
| 보고된 평가 크레딧 추정치 | 77.68 | 71.13, **일부만 보고됨** |
| 응답 / 채점 크레딧 | 64.87 / 12.81 | 58.29 / 12.84 |

비교 대상은 **18개의 공통 검사**이며 18개의 별도 대화가 아닙니다. 하나의 테스트에 여러 평가 지표가 있을 수 있습니다. 양쪽 모두 Pass 또는 Fail이 있는 검사만 공통 검사로 보며, 누락·오류·제외를 통과로 취급하지 않습니다.

Luna는 두 검사를 더 통과했고, 반대로 Sol만 통과한 검사는 없었습니다. 앱은 Luna를 **Medium confidence**로 추천합니다. 추천과 신뢰도는 코드로 계산하고, AI 프롬프트는 이유와 절충점을 설명합니다. AI의 인상만으로 결정하는 구조가 아닙니다.

![같은 엔진으로 실행한 두 모델의 결과 비교](/mwkorea/assets/images/2026-11-12-CopilotModelAssessment/image5.png)

## 크레딧 숫자는 어디까지 포함하나요?

Sol의 71.13은 **partial** 표시가 있으므로 더 저렴하다는 근거가 될 수 없습니다. 표는 평가 질문에 답하는 소비량과 답을 채점하는 소비량을 합친 보고치이며, 전체 평가 워크플로의 총비용도 아닙니다.

결과 분석용 AI 프롬프트는 별도로 크레딧을 사용합니다. 저자가 관측한 AI 분석 소비량은 **평가당 약 120~150 Copilot Credits**이며, 테스트 케이스를 실행하는 에이전트 소비량은 제외한 값입니다. 이는 운영 계획을 위한 관측 추정치이지 고정 요금이나 절감 보장이 아닙니다.

Kit 테스트에는 크레딧이 보고되지 않고 불완전한 소비량도 있을 수 있습니다. 운영 비용 절감 주장은 완전한 측정 데이터를 확보한 뒤에 해야 합니다.

## AI 요약은 탐색 도구이지 판정 원본이 아닙니다

AI summary는 Works well, Needs attention, What changed 등으로 강점과 문제를 설명합니다. 하지만 원문 예시에서 Luna의 생성 요약은 Warning이라고 쓰는 반면 실제 실행 카드는 **Critical**입니다. 생성 문장이 저장된 상태를 덮어쓰지는 않습니다.

또한 모델 추천은 선택한 두 실행의 비교이고, 각 실행의 What changed는 그 실행에 기록된 baseline 비교입니다. 비교할 실행을 바꾼다고 모든 요약이 새 쌍을 기준으로 재해석되는 것은 아닙니다.

![강점·문제점·변화를 정리하는 AI summary](/mwkorea/assets/images/2026-11-12-CopilotModelAssessment/image6.png)

## 실패한 검사를 재현해 원인을 좁히기

Regressed 화면에는 두 가지 변화가 나타납니다.

**Customer Support Case Agent 테스트 세트의 테스트 목록 요청**은 Luna에서 Response Quality가 통과하고 Sol에서 실패했습니다. 반면 Tool and Capability Use는 양쪽 모두 통과했습니다. 따라서 이 결과만으로 도구 호출 실패라고 진단해서는 안 됩니다.

또 다른 차이는 **Start a test run**의 Required Information Coverage 검사입니다. 키워드 검사가 실패했다고 테스트 실행 자체가 실패했다고 단정할 수는 없습니다. 예상 문구와 실제 응답을 먼저 대조해야 합니다.

![퇴행한 검사와 평가 지표 확인](/mwkorea/assets/images/2026-11-12-CopilotModelAssessment/image7.png)

테스트 목록 요청의 보고 소비량은 Luna **10.85**, Sol **13.46 크레딧**입니다. 이는 테스트 케이스 단위의 소비량이며 각 지표 행마다 별도로 과금된 값이 아닙니다. Sol의 실행 전체 보고가 불완전하다는 한계도 유지됩니다.

![테스트별 평가 결과와 소비 크레딧](/mwkorea/assets/images/2026-11-12-CopilotModelAssessment/image8.png)

## 추천 모델이어도 운영 승인은 별개입니다

양쪽 실행에는 동일하게 실패한 **Business Classification 검사 네 개**가 남습니다. 테스트 결과 해석, 테스트 세트 실행, 에이전트 기능 설명, 테스트 유형 설명과 관련된 검사입니다.

추천은 두 후보 중 상대적으로 어느 쪽이 나은지를 답합니다. **Critical은 해결되지 않은 실패가 있다는 별개의 상태**입니다. 연결된 설정 문서는 실패율이 20%를 초과하면 Critical로 분류하는 절대 기준과 baseline 대비 회귀 기준 중 더 나쁜 상태를 적용한다고 설명합니다.

![모델 변경과 무관하게 남는 공통 실패](/mwkorea/assets/images/2026-11-12-CopilotModelAssessment/image9.png)

따라서 두 회귀 검사를 재현하고, 공통 실패의 분류 기준과 정답 라벨도 검토해야 합니다. 에이전트가 잘못됐을 수도 있지만 평가 기준을 수정해야 할 수도 있습니다. 설정상의 위험을 살피는 Agent Review Tool을 보완적으로 활용할 수 있습니다.

## 시작하기와 마무리

Copilot Agent Kit는 [Microsoft Marketplace](https://marketplace.microsoft.com/en-us/product/dynamics-365/microsoftpowercatarch.copilotstudiokit2)에서 확인할 수 있습니다. 비교 결과는 PDF로 내보내 검토 담당자와 공유할 수 있습니다.

모델 교체 전에는 개선할 업무와 깨뜨려서는 안 되는 업무를 먼저 정하고, 같은 조건에서 기준선과 후보를 평가하세요. 더 높은 통과율, 더 낮아 보이는 비용, 추천 배지 중 어느 하나도 단독으로 운영 전환의 근거가 되어서는 안 됩니다.

> **출처**: [Before you switch models: Assess your Copilot Studio agent with Model Assessment](https://microsoft.github.io/mcscatblog/posts/model-assessment/) — MCSCAT Blog, The Custom Engine. 자세한 내용은 원문 참조.
