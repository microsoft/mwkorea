---
title: "Copilot Studio 새 오케스트레이터, 어디서부터 배울까? CAT가 공개한 3가지 실전 자료"
date: 2026-07-07T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Orchestration
  - ModernAgents
  - Skills
  - ConnectedAgents
  - Migration
  - AICodingAgents
excerpt: "Copilot Studio의 새로운 에이전트·워크플로 경험은 단순한 UI 변경이 아니라 설계 방식의 전환입니다. Microsoft Copilot Studio CAT가 이를 이해하고, 실행해 보고, 클래식 에이전트를 마이그레이션하는 데 사용할 수 있는 Deep Dive 덱·기술 가이드·AI 코딩 에이전트 플러그인을 공개했습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio 새 오케스트레이터, 어디서부터 배울까? CAT가 공개한 3가지 실전 자료

Copilot Studio의 새로운 경험과 그 아래에서 동작하는 오케스트레이션 스택은 큰 변화입니다. 에이전트는 더 유연하고 정교해졌고, 워크플로는 시각적 캔버스에서 자동화 프로세스를 구성하면서 어떤 단계를 AI가 처리할지 더 세밀하게 제어할 수 있게 됐습니다.

새로운 설계 공간과 새로운 스택은 자연스럽게 여러 질문을 만듭니다. 기존과 무엇이 달라졌는지, 에이전트와 워크플로 중 무엇을 만들어야 하는지, 기존 클래식 에이전트는 어떻게 옮겨야 하는지 말입니다.

Microsoft Copilot Studio Customer Advisory Team(CAT)은 이 질문에 답하기 위해 **이해하기, 실행해 보기, 마이그레이션하기**의 세 단계로 구성된 자료를 공개했습니다.

![Copilot Studio 새 오케스트레이터 자료 소개](/mwkorea/assets/images/2026-07-07-CopilotStudioNewOrchestratorResources/image1.png)

---

## 한눈에 보는 3가지 자료

| 원하는 것 | 사용할 자료 |
|---|---|
| 무엇이 왜 바뀌었는지 이해하고 설명하기 | [Technical Deep Dive 덱](https://aka.ms/CopilotStudioDeepDiveDeck) |
| 실제로 동작하는 전체 시나리오 보기 | [기술 가이드 미니사이트](https://aka.ms/MCSTechGuide) |
| 클래식 에이전트 마이그레이션 시작하기 | [Copilot Studio AI 코딩 에이전트 플러그인](https://github.com/microsoft/copilot-studio-plugin) |

## 1. 이해하기: Technical Deep Dive 덱

새 경험에서 **무엇이 바뀌었고 왜 바뀌었는지** 배우거나 설명해야 할 때 사용하는 자료입니다. 기능 목록을 나열하는 소개 자료보다는 에이전트·워크플로 빌더와 아키텍트를 위한 의사결정 프레임워크에 가깝습니다.

덱은 다음 질문을 다룹니다.

- 에이전트와 워크플로 중 어디에 무엇을 구현해야 하는가
- 현대적인 에이전트와 워크플로는 어떻게 설계하는가
- 기존 설계를 그대로 복제하지 않고 클래식에서 모던으로 어떻게 옮기는가
- 새 경험에서 개선된 부분과 아직 지원되지 않는 부분은 무엇인가

![새 컴포넌트 모델을 설명하는 Deep Dive 슬라이드](/mwkorea/assets/images/2026-07-07-CopilotStudioNewOrchestratorResources/image2.png)

### 핵심 설계 원칙

CAT가 강조한 핵심은 **각 동작을 신뢰할 수 있고 점검 가능한 가장 작은 컴포넌트에 배치하는 것**입니다.

| 컴포넌트 | 담당 역할 |
|---|---|
| Instructions | 항상 참이어야 하는 행동 원칙 |
| Knowledge | 검색 가능한 사실과 정보 |
| Tools | 시스템에서 실행하는 실제 작업 |
| Memory | 세션을 넘어 유지할 맥락 |
| Skills | 특정 상황에서 필요할 때 불러오는 절차 |
| Connected agents | 명확한 전문 영역을 담당하는 에이전트 |

모든 로직을 거대한 지침 하나에 넣거나, 수십 개 도구를 하나의 에이전트에 무작정 연결하는 대신 책임을 분리해야 한다는 의미입니다.

## 2. 실행해 보기: 기술 가이드 미니사이트와 샘플

슬라이드의 개념을 이해한 다음 실제 동작을 보고 싶다면 기술 가이드 미니사이트를 사용합니다. 빌딩 블록을 읽고, 시나리오 대화를 실행한 뒤, 솔루션을 내려받아 자신의 Power Platform 환경에 배포할 수 있습니다.

![Copilot Studio 기술 가이드 미니사이트](/mwkorea/assets/images/2026-07-07-CopilotStudioNewOrchestratorResources/image3.png)

이 자료는 화면 캡처만 모아 놓은 데모가 아니라 실제로 배포할 수 있는 샘플입니다. **BlastBox Omega**라는 레트로 미래형 게임 스토어 시나리오를 통해 다음 기능을 보여 줍니다.

- 여러 대화 턴에 걸친 추론
- 전문 에이전트로의 위임
- 실제 시스템 작업 실행
- 다운로드 가능한 결과물 생성

### 제공되는 시나리오

- **Self-Serve Card Reissue**: 사용자의 카드 재발급 요청을 처음부터 끝까지 처리하며, 실제 쓰기 작업 전에 신원 확인을 거치고 생성된 파일을 제공합니다.
- **Block Party Trade-Up**: 상위 에이전트가 전문 에이전트들을 조율해 복합적인 요청을 해결하고 다운로드 가능한 문서로 마무리합니다.

샘플의 진짜 가치는 각 책임이 어디에 놓였는지 확인하는 데 있습니다. 전문 추론은 connected agent, 실제 작업은 tool, 반복 가능한 절차는 Skill, 정확한 계산은 코드가 담당합니다.

## 3. 마이그레이션하기: Copilot Studio 플러그인

기존 클래식 에이전트를 현대적인 구조로 옮길 출발점이 필요할 때 사용하는 도구입니다. AI 코딩 에이전트용 [Copilot Studio 플러그인](https://github.com/microsoft/copilot-studio-plugin)을 설치하고 `/migrate` 명령에 환경·테넌트·Copilot Studio URL과 제약 조건을 전달합니다.

플러그인은 다음 과정을 수행합니다.

1. 클래식 에이전트를 가져옵니다.
2. 기존 구조와 동작을 분석합니다.
3. 현대적인 아키텍처를 제안합니다.
4. 테스트 가능한 마이그레이션 에이전트를 생성합니다.

![Copilot Studio 플러그인의 마이그레이션 흐름](/mwkorea/assets/images/2026-07-07-CopilotStudioNewOrchestratorResources/image4.png)

### 시작 프롬프트 예시

```text
/mcs-assistant:migrate Migrate this agent to modern orchestration:
https://copilotstudio.microsoft.com/environments/<ENV_ID>/bots/<BOT_ID>
from tenant <TENANT_ID>
```

### 결과는 초안으로 취급해야 합니다

중요한 단어는 **제안(propose)**입니다. 플러그인은 빠른 출발점을 제공하지만 아키텍처의 정확성을 자동으로 보장하는 버튼은 아닙니다.

- 기존 토픽이라고 해서 모두 Skill로 바꾸지 않습니다.
- 기존 변수라고 해서 모두 Memory로 옮기지 않습니다.
- 유지해야 할 업무 결과와 핵심 사용자 여정을 먼저 정의합니다.
- 각 책임을 적합한 현대적 컴포넌트에 배치합니다.
- 기존 평가 시나리오와 비교해 품질을 검증합니다.

> 생성 결과를 실행하고, 구조를 점검하고, 기존 평가와 비교한 뒤 실제 사용에 충분한지 판단해야 합니다.

## 어떤 순서로 시작할까

1. **덱**으로 개념과 설계 원칙을 이해합니다.
2. **미니사이트와 샘플**로 실제 동작과 책임 분리를 확인합니다.
3. **플러그인**으로 기존 에이전트 하나를 마이그레이션해 봅니다.
4. 핵심 사용자 여정에 대한 평가를 실행하고 사람이 아키텍처를 검토합니다.

## 도입 관점 체크포인트

- 기존 클래식 에이전트를 그대로 복제하기보다 업무 결과를 기준으로 재설계합니다.
- Instructions, Knowledge, Tools, Memory, Skills, connected agents의 책임 경계를 문서화합니다.
- 쓰기 작업이나 민감한 동작에는 신원 확인·승인 같은 명시적 제어를 둡니다.
- 마이그레이션 전후의 핵심 여정을 동일한 평가 세트로 비교합니다.
- 플러그인에 전달하는 테넌트·환경 정보와 로컬 개발 환경의 보안 정책을 점검합니다.

## 마무리

새 Copilot Studio 경험은 UI만 바뀐 것이 아니라 에이전트를 설계하는 사고방식 자체가 달라진 것입니다. CAT가 공개한 세 자료는 그 변화를 **이해하고, 눈으로 확인하고, 실제 기존 에이전트에 적용하는** 순서로 접근할 수 있게 해 줍니다. 처음부터 모든 것을 바꾸기보다, 대표적인 클래식 에이전트 하나를 골라 이 세 단계를 따라가 보는 것이 좋은 출발점입니다.

---

> **원문**: [New Orchestrator, New Rules? CAT's Got You (The Custom Engine, Microsoft Copilot Studio CAT, 2026-07-07)](https://microsoft.github.io/mcscatblog/posts/new-orchestrator-resources/)
>
> 자세한 내용은 원문을 참조하세요.
