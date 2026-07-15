---
title: "Copilot Studio 모던 에이전트의 Skills: 필요한 순간에만 불러오는 업무 절차"
date: 2026-06-15T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - AgentSkills
  - ModernAgents
  - Orchestration
  - SKILLmd
  - ALM
excerpt: "Copilot Studio 모던 에이전트에 Agent Skills 개방형 형식을 따르는 Skills가 추가됐습니다. 항상 필요한 지침은 Instructions에 두고, 특정 상황에서만 필요한 절차·예제·스크립트는 Skill로 분리해 컨텍스트와 유지관리 부담을 줄일 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio 모던 에이전트의 Skills: 필요한 순간에만 불러오는 업무 절차

LLM은 일반적인 문제에는 강하지만 조직 고유의 맥락·규칙·데이터·업무 노하우를 스스로 알아낼 수는 없습니다. 특히 특정 업무를 처리하는 단계별 절차를 가르치려다 보면 에이전트 지침이 계속 길어지고, 모든 대화에 불필요한 정보까지 들어가면서 동작이 불안정해질 수 있습니다.

Copilot Studio 모던 에이전트는 이런 **상황별 지침을 Skills로 분리**합니다. Skill은 특정 작업이 나타났을 때만 불러오는 지침과 선택적 리소스 묶음입니다.

![Copilot Studio Skills 개념](/mwkorea/assets/images/2026-06-15-CopilotStudioModernAgentSkills/image1.png)

---

## Skill이란

Skill의 기본은 `SKILL.md` 파일입니다.

- 이름
- 설명
- 실제 지침
- 선택적 예제·템플릿·참조 자료·스크립트

에이전트는 기본적으로 Skill의 이름과 설명만 확인합니다. 사용자의 요청과 관련 있다고 판단할 때만 전체 지침과 리소스를 컨텍스트에 불러옵니다.

## 왜 Skill로 분리하나

### 관리 용이성

하나의 거대한 지침 대신 업무별 Skill을 독립적으로 검토하고 버전 관리할 수 있습니다.

### 컨텍스트 관리

Skills는 필요할 때만 전체 내용을 로드합니다. Skill 10개의 긴 지침을 매 대화에 넣는 대신 짧은 설명 10개만 기본 컨텍스트에 유지합니다.

### 정확성

특정 상황에 필요한 Tool, 중요 매개변수, 쿼리 작성법, 호출 전 검증, 빈 결과 처리법을 Skill에 담을 수 있습니다. 도구가 많거나 서로 겹칠 때 올바른 Tool 사용을 도울 수 있지만, 효과는 평가로 확인해야 합니다.

### 속도와 비용

에이전트가 접근 방법을 처음부터 추론하는 대신 관련 절차를 바로 사용할 수 있습니다. 불필요한 검색·Tool 호출·추론 반복이 줄면 지연 시간과 크레딧 사용량도 줄어들 수 있습니다.

## Copilot Studio에서의 동작

모던 오케스트레이터는 사용 가능한 Skills의 메타데이터를 보고 관련 Skill을 선택합니다. 선택된 Skill의 전체 지침과 리소스가 컨텍스트에 로드되고, 에이전트는 기본 Instructions·Knowledge·Tools와 함께 이를 사용합니다.

![Skill이 필요한 순간에 로드되는 흐름](/mwkorea/assets/images/2026-06-15-CopilotStudioModernAgentSkills/image2.png)

Knowledge, Tools, Skills는 기본 컨텍스트에 메타데이터만 들어가고 필요할 때 상세 내용이 로드됩니다. 에이전트의 Instructions만 항상 전체가 로드됩니다.

## Skill 추가와 호출

Skills 탭에서 빈 Skill을 만들거나 기존 Skill을 업로드할 수 있습니다.

- 단일 `SKILL.md`
- `SKILL.md`와 스크립트·참조·템플릿을 포함한 `.zip`

추가된 Skill은 해당 에이전트에 포함되며, 에이전트를 Power Platform Solution에 넣으면 ALM 수명주기와 함께 이동합니다.

Skill을 직접 호출하는 명령은 없습니다. 오케스트레이터가 이름과 설명을 바탕으로 선택하며, reasoning view에서 그 과정을 확인할 수 있습니다.

- 너무 자주 실행되면 설명이 지나치게 넓을 수 있습니다.
- 전혀 실행되지 않으면 설명이 너무 좁거나 실제 사용자 표현과 다를 수 있습니다.

## 설명은 문서가 아니라 라우팅 메타데이터

Skill의 이름과 설명은 사람이 읽는 소개문보다 **오케스트레이터가 사용 시점을 결정하는 신호**에 가깝습니다.

- `HR Help`보다 `HR Leave Eligibility Triage`처럼 구체적으로 이름을 정합니다.
- 사용할 상황과 사용하지 않을 상황을 모두 적습니다.
- 두 메이커가 적용 시점을 다르게 판단한다면 설명을 더 명확히 합니다.

## 개방형 Agent Skills 형식

Copilot Studio Skills는 [Agent Skills 개방형 형식](https://agentskills.io/)을 따릅니다.

```text
my-skill/
├── SKILL.md
├── scripts/
├── references/
└── assets/
```

현재 Copilot Studio는 지침과 함께 참조 파일·예제·템플릿·실행 스크립트를 묶는 구조를 지원합니다.

### 현재 제약

- Skill은 현재 에이전트 단위로 배포됩니다. 공유 카탈로그를 통한 교차 에이전트 배포는 아직 제공되지 않습니다.
- Skill은 에이전트의 Actions, Flows, Connectors, MCP Servers를 지침으로 참조할 수 있지만 권한을 부여하거나 강제로 바인딩하지는 않습니다.
- 참조한 Tool이 에이전트에 없거나 오케스트레이터가 지침을 따르지 않으면 실행이 보장되지 않습니다.

## Instructions와 Skill 중 무엇을 선택할까

1. Tool·Knowledge 설명만으로 에이전트가 알아낼 수 있습니까? 그렇다면 별도 지침이 필요하지 않을 수 있습니다.
2. 모든 대화와 시나리오에서 항상 참입니까? **Instructions**에 둡니다.
3. 특정 상황에만 적용됩니까? **Skill**로 만듭니다.

![Instructions와 Skill 선택 기준](/mwkorea/assets/images/2026-06-15-CopilotStudioModernAgentSkills/image3.png)

톤, 역할, 상시 Guardrail은 Instructions에 적합합니다. 환불 처리 절차, 보안 사고 대응, 특정 지역 세금 규칙, 제출 전 검증 체크리스트처럼 상황별 노하우는 Skill에 적합합니다.

## Skill과 별도 에이전트 중 무엇을 선택할까

같은 사용자, 같은 Knowledge 경계, 같은 목적을 공유한다면 여러 작업을 하나의 에이전트 안의 Skills로 구성하는 편이 낫습니다.

별도 에이전트가 적합한 경우는 다음과 같습니다.

- 독립적으로 사용할 수 있는 전문 영역입니다.
- 대상 사용자나 보안 경계가 다릅니다.
- 한 에이전트의 Tool이 지나치게 많아 정확도가 저하됩니다.

## 신뢰와 보안

Skill은 에이전트 행동을 바꾸고 스크립트도 포함할 수 있으므로 신뢰 경계로 취급해야 합니다. 커뮤니티·AI 생성·다른 환경에서 가져온 Skill은 코드처럼 검토합니다.

- 프롬프트 인젝션
- Tool 오용 지침
- 설명과 다른 숨겨진 동작
- 불필요한 데이터 접근

## 마무리

Skills의 핵심은 간단합니다. **항상 참인 것은 Instructions에, 상황별 절차는 필요할 때 불러오는 Skill에 둡니다.** 이 구분만 잘해도 에이전트의 컨텍스트를 가볍게 유지하고, 업무 절차를 독립적으로 관리하며, 더 예측 가능한 Tool 사용을 설계할 수 있습니다.

---

> **원문**: [Modern Agents Have Skills Now — Here's How They Work in Copilot Studio (The Custom Engine, Microsoft Copilot Studio CAT, 2026-06-15)](https://microsoft.github.io/mcscatblog/posts/modern-mcs-agent-skills/)
>
> 자세한 내용은 원문을 참조하세요.
