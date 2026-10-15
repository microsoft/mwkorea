---
title: "Copilot Studio 훅(Hooks) 활용법: 지침만으로는 부족한 에이전트 제어를 이벤트 기반으로"
date: 2026-10-12T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Hooks
  - Agent
  - GitHubCopilotHarness
  - Governance
  - PII
excerpt: "GitHub Copilot 하니스 기반 Copilot Studio 에이전트에서 세션 시작, 프롬프트 제출, 도구 호출 전 같은 시점에 워크플로를 실행하는 훅(Hooks)이 퍼블릭 프리뷰로 제공됩니다. 컨텍스트 주입, PII 마스킹, 예산 검증 예제와 fail-open 동작에 대한 주의점을 정리했습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio 훅(Hooks) 활용법: 지침만으로는 부족한 에이전트 제어를 이벤트 기반으로

GitHub Copilot 하니스(harness)로 동작하는 에이전트는 작업 접근 방식과 호출할 도구를 모델이 스스로 추론합니다. 지침(instructions)이 이 판단을 안내하지만, 어떤 이벤트가 발생할 때마다 **반드시** 실행되어야 하는 단계도 있습니다. 훅(Hooks)은 모델의 선택과 무관하게 런타임이 여러분의 로직을 호출하는 예측 가능한 체크포인트입니다.

예를 들어 HR 에이전트는 대화 시작 시 직원의 국가와 선호 언어를 이미 알고 있을 수 있고, 개인정보는 에이전트가 처리하기 전에 마스킹할 수 있으며, 항공권 예약은 예약 도구가 실행되기 전에 예산을 점검할 수 있습니다. 이 글은 Copilot Studio Customer Advisory Team(MCSCAT) 블로그의 내용을 바탕으로 세 가지 예제의 워크플로, 입출력 매핑, 실행 트레이스, 그리고 훅이 실패했을 때의 동작을 정리합니다.

훅은 현재 **GitHub Copilot 하니스 기반 에이전트에서 퍼블릭 프리뷰**입니다. 지금 사용하려면 copilotstudio.preview.microsoft.com에 접속해 환경에서 사용 가능한지 확인하세요.

---

## 토픽 트리거에서 훅으로

Standard 하니스 에이전트에서는 "메시지를 받았을 때", "AI 생성 응답이 전송되기 직전" 같은 토픽 트리거로 대화 중 정해진 시점에 대응했습니다. GitHub Copilot 하니스 기반 에이전트는 세션 시작, 도구 호출 전 등 실행 중 정해진 순간에 **훅**을 확장 지점으로 사용합니다. 모델이 선택하지 않아도 이벤트가 발생하면 설정한 로직이 호출됩니다.

이 라이프사이클 훅 패턴은 GitHub Copilot SDK에서도 `onSessionStart`, `onPreToolUse` 같은 코드 핸들러로 제공됩니다. Copilot Studio에서는 현재 훅의 핸들러를 **워크플로**로 구현합니다. 워크플로는 이벤트 입력을 받아 컨텍스트 추가, 값 교체, 도구 호출 거부(deny) 같은 출력을 반환합니다. 훅은 *언제* 워크플로가 실행될지를 정하고, 에이전트는 그 결과를 바탕으로 *어떻게* 작업할지를 여전히 스스로 결정합니다. 에이전트 스킬이 작업 지침을 제공한다면, 훅은 이벤트 기반 실행을 제공합니다.

훅을 구성하려면 이벤트를 선택하고, 호환되는 워크플로를 만들거나 선택해 에이전트에 연결합니다. 같은 워크플로를 여러 에이전트에서 재사용할 수 있으며, 에이전트·사용자·채널 메타데이터로 적용할 규칙을 구분할 수 있습니다.

---

## 예제 1: 세션 시작 시 직원 컨텍스트 로드

HR Buddy 에이전트는 복리후생과 온보딩 질문에 답합니다. 국가는 적용 가이드를, 고용 구분은 관련 정책을, 선호 언어는 응답 언어를 좌우하므로 세션 시작 시점에 이 정보를 제공하는 것이 목표입니다.

**Start (pre-loop)** 이벤트는 새 대화가 시작될 때 실행됩니다. 배포된 워크플로가 로그인한 직원의 프로필을 조회해 `additionalContext`를 반환하면, 이 텍스트가 세션 첫 사용자 메시지에 추가 컨텍스트 블록으로 붙습니다. 사용자가 직접 입력하지 않아도 "Country: Greece", "Preferred language: Greek"가 모델에 전달되어 그리스어로 응답할 수 있습니다. 데이터 권한과 복리후생 자격 판단은 여전히 HR 시스템이 담당합니다.

![훅 생성 폼이 세션 시작 이벤트를 직원 컨텍스트 워크플로에 연결한 화면](/mwkorea/assets/images/2026-10-12-CopilotStudioHooks/image2.png)

샘플 워크플로의 흐름은 다음과 같습니다.

| 단계 | 입력 및 출력 |
|---|---|
| 직원 식별 | 훅 입력의 `metadata.userAadObjectId` 읽기 |
| 프로필 조회 | ID를 샘플 직원 레코드와 매칭, 불일치 시 사유 기록 |
| 필드 선택 | `country`, `employmentCategory`, `preferredLanguage`, `onboardingStage` |
| 컨텍스트 반환 | 값을 `additionalContext`로 포맷, 미일치 시 빈 컨텍스트 반환 |

![직원 컨텍스트 워크플로 화면](/mwkorea/assets/images/2026-10-12-CopilotStudioHooks/image3.png)

프로덕션에서는 샘플 프로필 단계를 인증·권한이 적용된 HR 조회로 교체해야 합니다.

![HR Buddy 실행 트레이스: 훅이 additionalContext를 반환하고 도구 호출 후 그리스어로 응답](/mwkorea/assets/images/2026-10-12-CopilotStudioHooks/image4.png)

---

## 예제 2: Azure Language로 프롬프트 PII 마스킹

**User prompt submitted** 이벤트에서 프롬프트를 Azure Language의 PII 탐지로 보내고, 서비스가 돌려준 마스킹 텍스트를 `modifiedPrompt`로 반환합니다. 프리뷰 테스트에서는 Microsoft 문서의 샘플 주민번호(SSN)가 포함된 육아휴직 질문을 사용했습니다.

Azure Cognitive Service for Language 커넥터의 **Detect Personal Information (V3.1)** 을 사용하며 단계 이름은 `Analyze prompt PII`입니다.

| 설정 | 값 |
|---|---|
| Endpoint | 승인된 Azure Language 리소스의 HTTPS 엔드포인트 |
| 인증 | 보안 커넥터 연결에 저장된 계정 키 |
| Operation | `EntitiesRecognitionPIIV3_1` (Text Analytics v3.1) |
| PII 카테고리 | 이 예제에서는 `USSocialSecurityNumber` |
| 로깅 옵트아웃 | `true` |

자격 증명은 보안 연결에 보관하고 승인된 호출자만 접근하도록 제한하세요. 이어서 `Redact prompt PII` 단계에서 `prompt`를 문서의 `text`에 매핑하고 ID는 `prompt-1`, 언어는 `en`으로 지정합니다. 커넥터가 따옴표와 줄바꿈을 올바르게 직렬화하도록 문서 객체를 전달합니다. 기본 마스킹은 별표(`*`)입니다.

![프롬프트를 Azure Language로 보내 검증 후 마스킹 텍스트를 반환하는 워크플로](/mwkorea/assets/images/2026-10-12-CopilotStudioHooks/image5.png)

결과는 검증한 뒤 훅 출력에 매핑합니다. `errors` 배열이 비어 있고, 일치하는 문서 ID가 정확히 하나이며, `redactedText`가 채워져 있고, 경고가 처리되었는지 확인합니다. 저장된 Parse JSON 스키마는 예상 밖 문서, 빈 마스킹 텍스트, 비어 있지 않은 errors/warnings를 거부합니다. 일치하는 문서의 `redactedText`를 `Respond to the agent`의 `modifiedPrompt`로 매핑하고 워크플로를 User prompt submitted 훅에 연결합니다.

![실제 프리뷰 실행: SSN은 별표로 바뀌고 육아휴직 질문과 응답 언어 요청은 유지됨](/mwkorea/assets/images/2026-10-12-CopilotStudioHooks/image6.png)

주의할 점은 다음과 같습니다.

- 에이전트에는 마스킹된 텍스트만 전달하고, 원본 값을 포함한 엔터티 세부 정보는 승인된 처리 경로 안에 두세요.
- 탐지가 0건이면 원문이 그대로 전달됩니다. 탐지 범위는 서비스에 따라 다르며 민감 값이 남을 수 있습니다.
- **실패 경로**: 훅이 오류가 나거나 시간 초과되면 원래 프롬프트가 에이전트 처리로 계속될 수 있습니다. 정제된 진단 정보를 남기고 아래의 접근·보존 제어를 구성하세요.

---

## 예제 3: 도구 실행 전 예약 금액 vs. 예산 점검

여행 에이전트가 650달러 항공권을 제안했는데 직원 예산은 500달러입니다. 실행 전에 실제 제안된 예약을 점검하고, 예산 내 항공편을 고르도록 에이전트에 명확한 사유를 주는 것이 목표입니다.

**Pre tool use** 이벤트는 도구 호출 직전에 실행되며 `toolName`과 `parameters`를 제공합니다. 워크플로가 제안 요금·통화를 독립적으로 조회한 정책과 비교해 결정을 반환합니다. `deny`를 반환하면 해당 호출이 차단되고, 모델은 이 사유로 한도를 설명하거나 다른 옵션을 고릅니다.

샘플 Travel Buddy 에이전트는 비트랜잭션 `BookFlight` 워크플로 도구와, Tools 필드로 범위를 한정한 `Check booking policy` pre-tool 훅을 가집니다. 도구는 `quoteId`, `totalMinorUnits`, `currency`를 받고, USD는 정수 센트(65000 = $650)를 사용합니다. 프리뷰 채팅에서 도구가 이 값을 텍스트로 직렬화했기 때문에 워크플로는 비교 전에 `int()`로 변환합니다.

![요금을 정규화해 한도와 비교하는 샘플 정책 워크플로](/mwkorea/assets/images/2026-10-12-CopilotStudioHooks/image7.png)

| 단계 | 입력과 결정 |
|---|---|
| 제안 검증 | 설정된 도구 이름, 로그인 ID, 견적 ID, 양의 정수 요금, USD 통화 필요 |
| 정책 조회 | `metadata.userAadObjectId`로 권한 있는 정책 조회 (샘플 한도 50000 USD 센트) |
| 정책 검증 | 적용 정책 1건, 음수 아닌 정수 한도, 통화 일치 |
| 금액 비교 | 한도 초과 요금은 deny, 한도 이내는 허용 |
| 결정 반환 | `permissionDecision`, `permissionDecisionReason` 설정, `modifiedParameters`는 비워 원래 인수 유지 |

![실제 프리뷰 실행: 650달러 제안이 사유와 함께 거부되고 에이전트가 더 저렴한 견적을 요청](/mwkorea/assets/images/2026-10-12-CopilotStudioHooks/image8.png)

허용하려면 두 permission 출력을 모두 비워 둡니다. 처리된 검증·정책 조회 오류에는 "정책 확인이 필요합니다. 정책 확인에 성공한 뒤 다시 시도하세요."와 같은 사유로 `deny`를 반환하고, `additionalContext`는 비우고 `suppressOutput`은 false로 둡니다.

**실패 경로**: pre-tool 훅이 실패하거나 시간 초과되어도 예약 도구는 실행될 수 있습니다. 프로덕션에서는 예약 서비스가 호출자, 견적 가격, 예산을 독립적으로 검증해야 합니다.

---

## 그 밖의 훅 이벤트

| 이벤트 | 입력 | 용도 |
|---|---|---|
| Post tool use | `toolName`, `parameters`, `result` | `modifiedResult`를 반환해 모델 처리 전에 성공한 도구 결과에서 승인된 필드만 선택 |
| After tool failure | `toolName`, `parameters`, `error` | 도구와 오류를 매칭해 `additionalContext`로 안내(예: 일시적 조회 오류의 제한적 재시도 정책) 제공 |
| Error | `error`, `errorContext`, `recoverable` | 도구 호출 외 오류를 `errorHandling`(`retry`, `skip`, `abort`)으로 처리. 제한된 `retryCount`와 안전한 `userNotification` 사용 |

전체 필드는 이벤트 레퍼런스를 참고하세요.

---

## 현재 동작과 구현 시 필수 사항

### 훅 실패와 필수 점검

- 현재 런타임은 **fail-open**입니다. 훅이 오류, 시간 초과, 읽을 수 없는 응답을 내면 기본 동작으로 실행이 계속됩니다.
- 훅 워크플로는 워크플로 응답 데드라인을 따르며, 시간 초과 시 프리뷰 채팅에 훅이 실패했다는 안내가 표시됩니다.

| 예제 | 훅 실패 시 결과 |
|---|---|
| 직원 컨텍스트 | 에이전트가 기존 컨텍스트로 계속 진행 |
| 프롬프트 마스킹 | 원본 프롬프트가 에이전트 처리로 계속될 수 있음 |
| 예약 점검 | 도구 실행이 계속됨 (백엔드의 독립 검증 필요) |

PII 탐지, 개인정보 보호, 정책 검증, 권한 부여, DLP 등 컴플라이언스 점검이 실패하면 민감 데이터가 노출되거나 정책이 막았을 작업이 허용될 수 있습니다. 필수 점검은 검증 실패 시 보호 대상 작업을 막는 **fail-closed**여야 합니다. 현재 Copilot Studio 훅은 fail-open이므로 핵심 규칙은 도구나 하위 서비스에서 독립적으로 강제하세요. 워크플로가 서비스 오류를 잡아 `deny`를 반환하면 도구 호출을 막을 수 있지만, 워크플로 자체가 실패하거나 시간 초과되면 도구가 실행될 수 있습니다. 두 상황을 따로 테스트하고, 민감 데이터를 전송하는 도구는 데이터가 시스템을 떠나기 전에 점검이 성공해야 합니다. 로그와 알림은 실패를 식별하게 해줄 뿐 작업을 막지는 못합니다.

### 마스킹과 데이터 보존

훅은 세 지점에서 데이터를 변환할 수 있습니다. User prompt submitted는 `modifiedPrompt`로 에이전트에 전달되는 메시지를, Pre tool use는 `modifiedParameters`로 도구 인수를, Post tool use는 `modifiedResult`로 모델이 받는 도구 결과를 교체합니다. 단, 이 변환은 **이미 수신·저장된 데이터를 지우지 않습니다.** PII 예제에서도 Copilot Studio와 Azure Language는 원본 프롬프트를 받으므로 트랜스크립트와 로그의 접근·보존 정책을 별도로 구성해야 합니다. `suppressOutput`은 사용자에게 보이는 출력만 제어하며 데이터 저장과는 무관합니다.

### 기본 제공 도구에 훅 적용

훅은 `web_search` 같은 기본 제공 지식 도구와 bash 명령 같은 CLI 도구도 지원합니다. 먼저 에이전트에 도구를 하나 이상 추가해야 훅 구성에 Tools 필터가 나타납니다. 기본 제공 도구에 적용하려면 Tools 필드를 비워 **All tools**를 사용하세요. 기본 제공 도구는 개별 선택지로 나오지 않습니다. 훅 입력의 `toolName`으로 호출된 도구를 구분할 수 있지만, All tools는 다른 도구 호출도 포함하므로 분기 전에 프리뷰에서 실제 이름을 확인하세요.

---

## 도입 체크포인트

- 개인화, 프라이버시, 도구 사용 결정 중 효과가 큰 사용 사례 하나로 시작하세요.
- 프리뷰에서 결과를 검증하고, 워크플로가 실패했을 때의 동작을 계획하세요.
- 필수 규칙은 훅에만 의존하지 말고 백엔드·도구 수준에서도 강제하세요.
- 프리뷰 기능이므로 환경별 제공 여부와 동작은 변경될 수 있습니다.

---

> **출처**: Hooks in Copilot Studio: Give Your Agent More Than Instructions — <https://microsoft.github.io/mcscatblog/posts/hooks-in-copilot-studio/> (MCSCAT Blog, The Custom Engine). 자세한 내용은 원문 참조.
