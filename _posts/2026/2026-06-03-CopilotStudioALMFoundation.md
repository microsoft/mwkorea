---
title: "Copilot Studio 에이전트 ALM의 기초: Dev·Test·Prod부터 파이프라인까지"
date: 2026-06-03T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - ALM
  - PowerPlatform
  - Solutions
  - Pipelines
  - EnvironmentVariables
  - Evaluations
excerpt: "Copilot Studio 에이전트를 안전하게 변경·배포하기 위한 ALM 기본선을 정리합니다. Dev·Test·Production 환경 분리, Solution과 Publisher, Managed 배포, Power Platform Pipelines, 환경 변수와 Key Vault, 평가 기반 품질 게이트가 핵심입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio 에이전트 ALM의 기초: Dev·Test·Prod부터 파이프라인까지

Copilot Studio는 아이디어를 실제 에이전트로 빠르게 바꿀 수 있습니다. 하지만 버전 1을 사용자가 쓰는 동안 버전 2를 안전하게 개발하려는 순간부터는 개발 위치, 변경 이동 방식, 환경별 설정, 품질 검증을 체계적으로 관리해야 합니다.

Application Lifecycle Management(ALM)는 에이전트를 안전하게 변경하고 배포하기 위한 기본 구조를 제공합니다. 이 글은 고급 CI/CD보다 먼저 마련해야 할 **안전한 최소 기준**을 정리합니다.

![Copilot Studio 에이전트 ALM 기초](/mwkorea/assets/images/2026-06-03-CopilotStudioALMFoundation/image1.png)

---

## 1. 환경 분리부터 시작하기

가장 검증된 기본 패턴은 세 환경입니다.

| 환경 | 구성 | 목적 |
|---|---|---|
| Development | Unmanaged solution | 일상적인 제작과 변경 |
| Test | Managed solution | 검증과 UAT |
| Production | Managed solution | 실제 사용자 서비스 |

변경은 **Dev → Test → Production** 한 방향으로 이동합니다. 일회성 PoC에는 단일 환경도 가능하지만, 운영 중인 버전을 유지하면서 다음 버전을 개발하려면 환경 분리가 필요합니다.

성숙한 운영에서는 조기 릴리스 플랫폼 변경을 확인하는 Preview 환경이나 긴급 수정용 Production-aligned 환경을 추가할 수 있지만, 실제 필요가 생기기 전까지는 세 환경으로 시작하는 편이 낫습니다.

## 2. Solution을 배포 단위로 사용하기

환경이 에이전트가 사는 장소라면 **Solution은 환경 사이를 이동하는 패키지**입니다. 에이전트가 의존하는 모든 구성 요소를 하나의 Solution에 넣어야 합니다.

### 먼저 Custom Publisher 만들기

Solution을 만들기 전에 custom publisher와 고유 prefix를 정의합니다. `contoso_` 같은 prefix는 생성되는 구성 요소의 schema name에 계속 사용되므로 처음부터 신중하게 결정해야 합니다.

### Solution에 포함할 항목

- Agent와 Topics
- Tools와 Knowledge sources
- Custom connectors
- Connection references
- Environment variables
- Power Automate workflows

Solution 밖에서 만든 구성 요소는 배포 파이프라인이 인식하지 못해 환경 사이를 안정적으로 이동하기 어렵습니다. 따라서 Solution을 먼저 만들고 **Preferred Solution**으로 지정한 뒤 제작을 시작합니다.

## 3. Managed와 Unmanaged 구분하기

- **Unmanaged Solution**: Development에서 자유롭게 추가·편집·삭제합니다.
- **Managed Solution**: Test와 Production에 가져오는 배포 아티팩트입니다.

변경이 필요하면 Dev에서 수정한 뒤 새 버전의 Managed Solution을 다시 배포합니다. Test나 Production에서 직접 수정하면 unmanaged layer가 생겨 다음 배포에서 덮어써지거나 예측하기 어려운 충돌이 발생할 수 있습니다.

### 운영 환경 보호

- Test와 Production에서 **Block unmanaged customizations**를 활성화합니다.
- 메이커와 불필요한 관리자 권한을 제거합니다.
- Flow 활성화 같은 예외 작업도 있으므로 설정뿐 아니라 접근 권한도 함께 관리합니다.

## 4. Power Platform Pipelines로 안전하게 이동하기

수동으로 ZIP을 내보내고 가져올 수도 있지만 오류가 발생하기 쉽고 누가 언제 무엇을 배포했는지 기록하기 어렵습니다.

Power Platform Pipelines는 환경을 순서대로 연결한 승격 경로를 제공합니다. Test에 배포해 검증한 **동일한 Solution 버전**을 Production으로 승격하므로 Dev에서 다시 내보내 생기는 차이를 막습니다.

### 파이프라인의 이점

- 반복 가능한 동일한 배포 절차
- 배포자·시간·대상 환경 감사 기록
- 환경별 실행 버전 가시성
- 다음 단계 전 승인 요구
- 환경별 Connection과 Variable 매핑

배포 이력은 버전을 보여 주지만 자동 롤백 버튼은 아닙니다. 이전 Managed 버전을 다시 배포하거나 환경 백업을 복원해야 할 수 있으므로 롤백 절차를 별도로 준비합니다.

## 5. 환경별 설정은 Environment Variables로

API endpoint, SharePoint URL, 임계값, feature flag처럼 환경마다 달라지는 값을 하드코딩하지 않습니다.

Environment Variable은 다음으로 구성됩니다.

- **Definition**: 이름·유형·설명 등 schema로 Solution과 함께 이동
- **Value**: 환경별 실제 값

대부분의 환경별 값은 Solution에서 제외하고 배포 시 대상 환경에 입력합니다. 모든 환경에서 같은 기본값이라면 Solution에 포함할 수도 있습니다.

### Secret 관리

API key, token, credential은 일반 변수에 저장하지 않습니다. Azure Key Vault를 참조하는 secret environment variable을 사용합니다. 에이전트는 Secret 이름을 참조하고 플랫폼이 실행 시 값을 가져오므로 Key Vault에서 값을 교체해도 에이전트를 다시 배포할 필요가 없습니다.

## 6. 배포 후 행동을 Evaluation으로 검증하기

배포 성공은 에이전트가 올바르게 동작한다는 뜻이 아닙니다. Evaluation은 입력과 기대 결과를 정의해 올바른 Tool을 선택하고 허용 가능한 응답을 생성하는지 측정합니다.

- Dev에서 내보내기 전에 실행합니다.
- Test와 Production 대상 환경에 가져온 후 다시 실행합니다.
- 자동화 파이프라인에서는 품질이 기준 아래로 떨어질 때 배포를 차단하는 Gate로 사용합니다.

## 배포 전 체크리스트

- Custom Publisher와 Prefix를 만들었습니다.
- 모든 에이전트 자산이 하나의 Solution에 있습니다.
- Dev의 Preferred Solution으로 설정했습니다.
- 환경별 값은 Environment Variables에 있습니다.
- Secret은 Key Vault와 Secret Environment Variable을 사용합니다.
- Test와 Production에서 unmanaged customization을 차단했습니다.
- 메이커·관리자의 운영 환경 직접 편집 권한을 제거했습니다.
- Pipeline 단계 순서가 올바릅니다.
- Test와 Production에는 Managed Solution을 배포합니다.
- 내보내기 전과 가져오기 후 Evaluation이 통과합니다.

## 마무리

ALM의 기본이 갖춰지면 에이전트 변경은 Dev에서 시작해 동일한 Managed 아티팩트로 Test와 Production까지 이동합니다. 운영 환경은 직접 편집되지 않고, 설정은 환경별로 바인딩되며, Secret은 재배포 없이 교체할 수 있고, 각 환경의 실행 버전과 품질을 확인할 수 있습니다.

고급 자동화·소스 관리·Hotfix 전략보다 먼저 이 기본선을 단단하게 만드는 것이 안전한 Copilot Studio 운영의 출발점입니다.

---

> **원문**: [ALM for Copilot Studio Agents: The Foundation (The Custom Engine, Microsoft Copilot Studio CAT, 2026-06-03)](https://microsoft.github.io/mcscatblog/posts/alm-copilot-studio-agents-foundation/)
>
> 자세한 내용은 원문을 참조하세요.
