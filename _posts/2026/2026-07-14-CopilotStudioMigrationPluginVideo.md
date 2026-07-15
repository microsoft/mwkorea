---
title: "클래식 Copilot Studio 에이전트를 모던 오케스트레이션으로: 마이그레이션 플러그인 실전 영상"
date: 2026-07-14T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - ModernOrchestration
  - Migration
  - GitHubCopilotCLI
  - AICodingAgents
  - Skills
excerpt: "Microsoft Copilot Studio CAT가 클래식 에이전트를 모던 오케스트레이션으로 마이그레이션하는 전체 과정을 영상으로 공개했습니다. GitHub Copilot CLI와 실험적 Copilot Studio 플러그인을 사용해 기존 기능을 분석하고, 현대적인 구성 요소로 재설계한 결과를 검토합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 클래식 Copilot Studio 에이전트를 모던 오케스트레이션으로: 마이그레이션 플러그인 실전 영상

클래식 에이전트를 새로운 형식으로 그대로 복사하는 것은 제대로 된 마이그레이션이 아닙니다. 모던 오케스트레이션은 구성 요소 모델 자체가 다르기 때문에, 기존 기능과 업무 결과를 유지하면서도 각각을 가장 적합한 현대적 구조에 배치해야 합니다.

Microsoft Copilot Studio Customer Advisory Team(CAT)은 앞서 소개한 Copilot Studio 플러그인의 마이그레이션 기능을 **GitHub Copilot CLI에서 처음부터 끝까지 실행하는 영상**을 공개했습니다.

![Copilot Studio 마이그레이션 플러그인 영상](/mwkorea/assets/images/2026-07-14-CopilotStudioMigrationPluginVideo/image1.png)

---

## 영상에서 다루는 내용

약 10~20분 분량의 영상은 가상의 여행사 에이전트를 예제로 사용합니다.

1. **클래식 에이전트 확인**  
   이탈리아 도시와 여행지를 안내하는 child agent, 피자 주문, 잘못되거나 누락된 주문에 대한 환불 요청 기능을 살펴봅니다.
2. **전체 마이그레이션 실행**  
   플러그인이 클래식 에이전트를 가져오고, 기능을 분석하고, 모던 설계를 제안하고, 마이그레이션된 에이전트를 생성하는 전 과정을 설명합니다.
3. **생성 결과 검토**  
   모던 에이전트를 열어 기존 기능이 어떤 Skill과 Tool로 옮겨졌는지 확인합니다.

## 마이그레이션 영상

<video controls style="width: 100%;">
  <source src="https://github.com/GiorgioUghini/WebVideos/releases/download/video-6-1.0.0/Video.Project.23.mp4" type="video/mp4">
</video>

영상은 플러그인이 이미 설치된 상태에서 시작합니다. 아래 준비 절차를 먼저 완료해야 같은 흐름을 따라갈 수 있습니다.

## 가장 중요한 아키텍처 선택

예제에서는 여행 안내를 담당하던 클래식 child agent가 모던 에이전트의 **Skill**로 바뀝니다. 하지만 이것이 모든 child agent를 Skill로 바꾸라는 일반 규칙은 아닙니다.

플러그인은 구성 요소를 일대일로 변환하는 대신, **기능과 업무 결과가 무엇인지 분석해 현대적 모델에서 책임이 들어갈 위치를 제안**합니다. 다른 시나리오의 child agent라면 connected agent나 다른 구조가 더 적합할 수 있습니다.

문자 그대로 변환하면 과거 구조만 보존하고 새 오케스트레이션 모델의 이점을 놓칠 수 있습니다. 기능 중심 마이그레이션은 설계를 단순화하고, 각 책임을 더 적합한 구성 요소에 배치할 기회를 만듭니다.

## 직접 실행하기

### 전제조건

- Power Platform CLI 2.9.3보다 최신 버전
- GitHub Copilot CLI 등 플러그인을 지원하는 AI 코딩 에이전트
- 충분한 성능의 AI 모델
- 대상 환경 ID, 에이전트 ID, 테넌트 ID

### 플러그인 설치

```text
/plugin marketplace add microsoft/copilot-studio-plugin
/plugin install mcs-assistant@copilot-studio-plugin
```

### 마이그레이션 실행

```text
/mcs-assistant:migrate Migrate this agent to modern orchestration:
https://copilotstudio.microsoft.com/environments/<ENV_ID>/bots/<BOT_ID>
from tenant <TENANT_ID>
```

최신 명령과 전제조건은 항상 [플러그인 README](https://github.com/microsoft/copilot-studio-plugin#readme)를 기준으로 확인해야 합니다.

## 반드시 점검해야 할 제한사항

> 이 플러그인은 실험적 연구 프로젝트이며 공식 지원되는 Microsoft 제품이 아닙니다.

영상에서는 수동 수정 없이 마이그레이션이 완료됐지만 같은 결과가 항상 보장되지는 않습니다. 출력은 완성본이 아니라 **강력한 첫 번째 초안**으로 취급해야 합니다.

- 클래식과 모던 에이전트의 행동을 비교합니다.
- 생성된 모든 Skill과 Tool을 검토합니다.
- 정상 입력뿐 아니라 예상하지 못한 입력도 테스트합니다.
- 실제 작업에 필요한 승인과 안전장치가 유지됐는지 확인합니다.
- 핵심 사용자 여정에 대한 평가를 다시 실행합니다.

## 왜 중요한가

마이그레이션에서 가장 어려운 부분은 파일 변환이 아니라 **모던 에이전트가 어떤 구조가 되어야 하는지 결정하는 일**입니다. 플러그인은 반복적인 분석·생성 작업을 줄이고 일관된 출발 아키텍처를 제안합니다. 덕분에 메이커는 기능을 하나씩 다시 만드는 대신 행동·품질·검증에 더 많은 시간을 쓸 수 있습니다.

## 마무리

Copilot Studio 플러그인은 클래식 에이전트의 기능을 현대적인 구성 요소로 다시 생각할 수 있는 빠른 출발점을 제공합니다. 다만 제안된 구조를 그대로 신뢰하지 말고, 사람이 설계를 검토하고 기존 평가와 비교해야 안전한 마이그레이션이 완성됩니다.

---

> **원문**: [Video Demo: Migrating a Classic Agent to Modern Orchestration (The Custom Engine, Microsoft Copilot Studio CAT, 2026-07-14)](https://microsoft.github.io/mcscatblog/posts/migration-plugin-video-demo/)
>
> 자세한 내용은 원문을 참조하세요.
