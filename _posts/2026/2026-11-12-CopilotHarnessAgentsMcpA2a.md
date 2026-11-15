---
title: "기존 Copilot Studio 에이전트, 다시 만들지 말고 MCP·A2A로 연결하세요"
date: 2026-11-12T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - MicrosoftCopilot
  - MCP
  - A2A
  - MultiAgent
  - OAuth
  - MicrosoftEntraID
  - OBO
excerpt: "기존 Copilot Studio 에이전트에 Microsoft Copilot harness 에이전트를 연결하는 MCP·A2A 구성 방법을 정리합니다. 프리뷰 전제조건부터 OAuth, OBO 인증, 사용자 공유 권한과 후속 대화 오류까지 실무에서 확인할 사항을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 기존 Copilot Studio 에이전트, 다시 만들지 말고 MCP·A2A로 연결하세요

이미 운영 중인 Copilot Studio 에이전트를 새 기술이 나올 때마다 다시 만들기는 어렵습니다. 다른 팀이 만든 전문 에이전트를 활용하려고 그 에이전트의 구성과 데이터를 우리 환경에 복사하는 것도 유지보수 부담이 큽니다.

Microsoft Copilot Studio Customer Advisory Team의 기술 블로그 **The Custom Engine**은 2026년 11월 12일, 기존 Standard 에이전트가 **Microsoft Copilot harness** 에이전트를 MCP 도구로 호출하고, harness 에이전트끼리는 다른 환경에 있는 에이전트를 A2A로 연결하는 사례를 공개했습니다. Microsoft Copilot harness는 원문에서 이전 명칭인 GitHub Copilot harness와 함께 설명됩니다.

이번 글의 범위는 **호출자와 호출 대상이 모두 Copilot Studio 에이전트인 구성**입니다. MCP·A2A 채널은 아직 **프리뷰**이며, 원문 저자가 3개 테넌트에서 확인한 결과를 일반 공급의 보장 사항과 구분해야 합니다.

![MCP·A2A와 Microsoft Entra ID를 통해 전문 에이전트를 연결하는 구성](/mwkorea/assets/images/2026-11-12-CopilotHarnessAgentsMcpA2a/image1.png)

---

## 먼저 정할 것: MCP인가, A2A인가?

두 채널은 같은 게시된 에이전트를 호출합니다. 차이는 에이전트의 업무 역량보다 **호출자의 호환성, 발견 방법, 응답 형태**에 있습니다.

| 구분 | MCP | A2A |
|---|---|---|
| 원문 구성의 호출자 | Standard 및 Microsoft Copilot harness 에이전트 | Microsoft Copilot harness 에이전트 |
| 프로토콜 | MCP `2025-06-18` | A2A 1.0만 지원 |
| 호출·응답 | `send-message`로 완료 응답 수신 | 채널에서 스트리밍 지원 |
| 발견 정보 | 에이전트 이름 기반 설명을 가진 도구 1개 | agent card와 skills 메타데이터 |
| 후속 대화 식별자 | `conversationId` | `context_id` |

**기존 Standard 에이전트에서 출발한다면 원문 시점에는 MCP가 연결 경로입니다.** 저자의 테스트에서 Standard harness의 A2A 입력 화면은 0.x 형식을 기대했지만, 대상은 1.0 card를 제공해 커넥터 생성까지 진행되지 않았습니다.

반대로 Microsoft Copilot harness 에이전트끼리 **같은 환경**에 있다면, Connected agents 목록에서 직접 연결할 수 있습니다. 이 경우 MCP·A2A URL, 앱 등록, OAuth를 추가로 구성할 필요가 없다는 점도 먼저 확인하세요.

## 전제조건과 담당자

| 구성 요소 | 필요한 상태 | 주요 담당자 |
|---|---|---|
| 호출 대상 | Microsoft Copilot harness 에이전트, 한 번 이상 게시, Early 환경, 사용 가능한 크레딧 | 메이커·Power Platform 관리자 |
| 호출용 앱 | 대상 에이전트가 속한 Entra 테넌트의 앱 등록 | ID 관리자 |
| 호출자 | 커넥터와 연결 구성 | 호출 에이전트 메이커 |

원문은 **호출 대상만 Early release 환경이 필요**하며, 호출자는 기본 환경 같은 Standard release 환경에서도 연결한 사례를 설명합니다. 같은 테넌트의 여러 클라이언트·에이전트와 MCP·A2A에 하나의 앱 등록을 사용할 수 있지만, 프로토콜별 권한과 동의는 별개입니다.

앱 등록은 호출자를 식별하기 위한 것입니다. 대상 채널 API는 Microsoft가 제공하므로, 이 사례에서 대상 에이전트용 서비스 앱을 새로 만드는 절차는 필요하지 않습니다. API가 검색되지 않으면 대상 에이전트의 MCP 또는 A2A 채널 화면을 한 번 열어 enterprise application이 프로비저닝되도록 한 뒤 다시 확인합니다.

API 표시 이름이 달라도 다음 공개 application ID로 검색할 수 있습니다.

```text
6f46e6ed-07bf-4616-80f0-47546850f654
```

연결은 **로그인한 사용자에게 위임된 권한**으로 동작하며, 대상 에이전트 접근 권한도 확인합니다. client secret은 커넥터가 토큰을 교환할 수 있는 호출자임을 증명하는 값이지, 사용자 권한을 우회하는 수단이 아닙니다. 실제 secret은 게시 글이나 저장소에 넣지 마세요.

## 대상 에이전트의 URL 확인

원문 테스트 화면에서는 Early 환경의 게시된 에이전트에서 **Triggers 옆 + → MCP protocol / A2A protocol**로 URL을 확인했습니다.

![Early 환경에서 표시되는 MCP·A2A 프리뷰 항목](/mwkorea/assets/images/2026-11-12-CopilotHarnessAgentsMcpA2a/image2.png)

URL 구조는 다음과 같지만, 직접 조합하기보다 **실제 화면에 표시된 값을 복사**하세요.

```text
MCP: https://api.powerplatform.com/copilotstudio-mcp/tenants/{tenantId}/environments/{environmentId}/agents/{agentSchemaName}
A2A: https://api.powerplatform.com/copilotstudio-a2a/tenants/{tenantId}/environments/{environmentId}/agents/{agentSchemaName}
Card: {A2A URL}/.well-known/agent-card.json
```

![A2A endpoint, agent card URL, skills를 확인하는 화면](/mwkorea/assets/images/2026-11-12-CopilotHarnessAgentsMcpA2a/image3.png)

**2026년 11월 13일 확인한 Microsoft Learn 문서**는 **Channels → Add a channel → MCP client / A2A client** 경로를 안내합니다. 원문과 공식 문서의 UI 경로가 다를 수 있으므로 자신의 환경에서 확인해야 합니다. 문서에서도 Early 환경 조건과 프리뷰 상태는 유지됩니다.

저자는 채널 대화상자를 여는 것 자체는 URL 확인이며, A2A skills는 저장되는 구성이라고 설명합니다. 테스트에서는 skills가 인증된 클라이언트가 읽는 전체 세부정보에 나타났지만 **공개 agent card에는 나타나지 않았습니다**. 게시 화면의 트리거 추가 경고가 있어도 MCP·A2A 호출이 성공한 관찰 역시 모든 환경의 보장 사항은 아닙니다.

## 시나리오 1: 기존 Standard 에이전트에 MCP 도구 추가

기존 에이전트를 다시 만드는 대신 전문 에이전트를 하나의 도구로 연결합니다.

### 앱 권한과 Manual OAuth

호출용 앱 등록에 채널 API의 delegated permission **`MCS.InvokeAsMCP`**를 추가하고 client secret을 준비합니다. Standard 에이전트에서 **Tools → Add a tool → Create new → Model Context Protocol**로 이동해 이름, 업무 범위를 설명하는 description, 대상 MCP URL을 입력합니다.

인증은 **OAuth 2.0 → Manual**로 선택합니다. Entra는 dynamic client registration을 지원하지 않아, 원문에서는 기본 Dynamic discovery로 구성했을 때 404가 발생했습니다.

| OAuth 항목 | 값 |
|---|---|
| Client ID | 호출용 앱의 Application (client) ID |
| Client secret | 생성한 secret의 Value |
| Authorization URL | `https://login.microsoftonline.com/{tenantId}/oauth2/v2.0/authorize` |
| Token URL template | `https://login.microsoftonline.com/{tenantId}/oauth2/v2.0/token` |
| Refresh URL | `https://login.microsoftonline.com/{tenantId}/oauth2/v2.0/token` |
| Scopes | `https://api.powerplatform.com/copilotstudio-mcp/MCS.InvokeAsMCP offline_access` |

`{tenantId}`는 Directory (tenant) ID로 바꿉니다. **`offline_access`는 토큰 갱신을 위해 포함**하며, 원문에서는 PKCE가 로그인 요청에 자동 포함되어 별도 설정이 필요하지 않았습니다. 위 host는 프로덕션 기준이며, 공식 문서는 비프로덕션 환경의 경우 복사한 endpoint의 host와 맞추라고 안내합니다.

![Manual OAuth와 MCP scope 설정 화면](/mwkorea/assets/images/2026-11-12-CopilotHarnessAgentsMcpA2a/image4.png)

### 커넥터별 Web redirect URI와 연결

도구 생성 과정에서 제시되는 `https://global.consent.azure-apim.net/redirect/`로 시작하는 **커넥터별 redirect URL**을 앱 등록의 Authentication에 **Web** 플랫폼으로 정확하게 추가합니다. 이후 Copilot Studio에서 연결을 만들고 로그인합니다.

![앱 등록에 커넥터의 Web redirect URI를 추가하는 화면](/mwkorea/assets/images/2026-11-12-CopilotHarnessAgentsMcpA2a/image5.png)

일반 로그인 구성에서는 필요한 권한에 대한 사용자 동의가 발생할 수 있으며, 테넌트 정책에 따라 관리자 동의가 필요할 수 있습니다. MCP에 동의했다고 A2A 권한까지 동의된 것은 아닙니다.

연결 후 노출되는 도구는 **`send-message` 하나**입니다. 원문에서는 같은 환경의 여러 에이전트에 기존 커넥터와 연결을 재사용했습니다.

![전문 에이전트를 send-message 도구로 연결한 Standard 에이전트](/mwkorea/assets/images/2026-11-12-CopilotHarnessAgentsMcpA2a/image6.png)

### 라우팅은 실제 질문으로 검증

Server description을 상세히 작성하는 것은 좋지만, 그것만으로 올바른 도구 호출이 보장되지는 않습니다. 원문에서는 구체적인 설명과 일반적인 설명 모두 휴가 질문을 도구로 보냈으나, **7시간 비행의 좌석 등급 질문은 웹 검색으로 빠진 실행**이 있었습니다.

따라서 사내 정책 에이전트를 연결한다면 호출자의 instructions에 “휴가·출장·경비 등 사내 정책은 해당 전문 도구를 사용하고 일반 지식이나 웹 검색으로 답하지 않는다”처럼 경계를 명확히 정하세요. 이는 원문 사례를 한국어로 풀어 쓴 지시 예시입니다.

도구를 추가할 때 설명이 에이전트에 복사되므로, **커넥터 설명을 나중에 수정해도 기존 도구에 자동 반영되지 않았습니다**. 원문에서는 도구를 제거한 뒤 다시 추가해야 했습니다.

대상만 아는 질문으로 테스트하고 activity trace의 **Used tool: send-message**를 확인합니다. 저자가 측정한 응답은 **약 9~17초**로, 제품 SLA가 아닙니다. 후속 질문의 맥락은 Copilot Studio가 반환된 `conversationId`를 전달하면서 유지했습니다.

## OBO 인증: 재로그인을 줄여도 동의와 권한은 필요합니다

Manual OAuth로 생성된 일반 OAuth 2 커넥터는 기본적으로 **End user credentials**를 사용합니다. 이 구성은 동작하지만, 사용자마다 별도의 connection manager 페이지에서 다시 로그인해야 할 수 있습니다.

원문의 MCP 사례에서는 **On-Behalf-Of(OBO)**로 바꾸어 기존 로그인을 활용하고, 대화 안에서 사용자가 최초 **Allow**를 선택하도록 구성했습니다. **OBO는 무승인 자동 연결을 뜻하지 않습니다.**

![로그인한 사용자 신원을 유지하며 토큰을 교환하는 OBO 흐름](/mwkorea/assets/images/2026-11-12-CopilotHarnessAgentsMcpA2a/image7.png)

### 앱 등록의 OBO 구성

1. **Expose an API → Add a scope**에서 기본 `api://{client-id}` URI를 사용하고, `access_as_user` scope를 만듭니다. 동의 가능 주체는 **Admins and users**, 상태는 **Enabled**로 구성합니다.
2. **Authorized client applications**에 Azure API Connections의 공개 client ID `fe053c5f-3692-4f14-aef2-ee34fc081cae`를 추가하고 `access_as_user`를 선택합니다.
3. **`MCS.InvokeAsMCP`에 관리자 동의**를 부여합니다. OBO의 백그라운드 토큰 교환 단계에서는 사용자에게 이 API 권한 동의를 새로 받을 수 없기 때문입니다.

![access_as_user scope와 Azure API Connections 사전 권한 구성](/mwkorea/assets/images/2026-11-12-CopilotHarnessAgentsMcpA2a/image8.png)

현재 공식 OBO 문서는 Azure API Connections service principal이 테넌트에 없다면 관리자가 먼저 프로비저닝해야 한다는 점도 안내합니다.

### Power Apps 커넥터의 Security 설정

MCP 마법사가 만든 커넥터를 **Power Apps → Custom connectors → 편집 → Security**에서 수정합니다.

| 항목 | MCP 사례의 설정 |
|---|---|
| Identity Provider | Azure Active Directory / Microsoft Entra ID |
| Enable Service Principal support | Off |
| Client ID·Tenant ID | 호출용 앱과 해당 테넌트의 값 |
| Client secret | 실제 Value 재입력. ID provider 변경 시 지워질 수 있음 |
| Authorization URL | 기본 `https://login.microsoftonline.com` |
| Resource URL | `https://api.powerplatform.com/copilotstudio-mcp` |
| Enable on-behalf-of login | `true` |
| Scope | 앞에서 사용한 `MCS.InvokeAsMCP` 전체 URI와 `offline_access` 유지 |

**Resource URL을 단순히 `https://api.powerplatform.com`으로 넣으면 안 됩니다.** 그것은 다른 API의 audience이므로 MCP endpoint에 유효한 토큰이 아닙니다.

![MCP 채널 Resource URL과 OBO 설정](/mwkorea/assets/images/2026-11-12-CopilotHarnessAgentsMcpA2a/image9.png)

Update connector 이후 redirect URI를 다시 확인합니다. 원문 테스트에서는 값이 유지됐지만, 현재 공식 문서는 표시된 redirect URL을 앱 등록에 등록하도록 안내하므로 변경이 없다고 가정하지 마세요. Standard 에이전트 도구에서 **새 연결을 생성해 선택**하고, 같은 커넥터를 사용하는 다른 에이전트에도 적용합니다.

## 메이커 계정으로 성공했다고 배포가 끝난 것은 아닙니다

원문은 다른 일반 사용자로 검증하면서 다음 네 가지를 확인했습니다.

| 사용자에게 필요한 것 | 누락 시 원문에서 관찰한 결과 |
|---|---|
| 게시된 호출 Standard 에이전트 공유 | 일반적인 에이전트 접근 요건 |
| Custom connector의 **Can view** 공유 | connector ReadAccess 오류 |
| 호출 대상 harness 에이전트 공유 | 전문 에이전트 답변 대신 일반 응답 |
| 기본 환경이 아닌 호출자 환경의 보안 역할 | Allow 뒤 연결 실패, 연결 생성 안 됨 |

보안 역할은 원문 테스트에서 **Basic User**로 충분했습니다. 이는 해당 테스트 구성의 관찰이며, 조직의 역할 설계를 무조건 바꾸라는 뜻은 아닙니다. 첫 세 공유 항목은 사용자별 수작업보다 보안 그룹으로 관리하는 것이 원문의 권장 방식입니다.

다른 환경의 대상을 호출하고 호출자가 기본 환경에 있던 구성에서는 대상 에이전트 공유만으로 대상 Early 환경 측 접근이 가능했다고 설명합니다. 자신의 테넌트에서도 실제 사용자로 검증하세요.

![OBO 구성에서 최초 연결 시 표시되는 대화 내 동의 카드](/mwkorea/assets/images/2026-11-12-CopilotHarnessAgentsMcpA2a/image10.png)

![사용자가 동의한 뒤 전문 에이전트의 답변을 받는 예시](/mwkorea/assets/images/2026-11-12-CopilotHarnessAgentsMcpA2a/image11.png)

![기존 연결을 이용해 추가 동의 카드 없이 후속 질문에 답하는 예시](/mwkorea/assets/images/2026-11-12-CopilotHarnessAgentsMcpA2a/image12.png)

화면에 보이는 육아휴직 기간과 연차 이월 일수는 **원문 테스트용 HR handbook의 답변**입니다. 한국 법령이나 Microsoft의 실제 인사 정책으로 적용하면 안 됩니다. 일반 OAuth 설정을 유지한 사용자는 connection manager에서 연결한 뒤 대화로 돌아와 Retry를 선택하는 흐름을 거칠 수 있습니다.

## 시나리오 2: 다른 환경의 harness 에이전트를 A2A로 연결

다른 팀이 관리하는 게시된 전문 에이전트를 복사하지 않고 **Connected agent**로 연결하는 구성입니다. 원문에서는 호출자가 기본 환경, 대상이 Early 환경이었습니다. MCP도 환경 간 호출이 가능하며, A2A만의 독점 기능은 아닙니다.

1. 호출용 앱에 delegated permission **`MCS.InvokeAsA2A`**를 추가합니다. MCP와 앱·secret을 재사용할 수 있지만 A2A 동의는 별도입니다.
2. 호출자에서 **Connected agents → + Add → Add A2A agent**로 이동해 대상의 **agent card URL**을 입력합니다.
3. 세부정보 출처는 **The agent's full details (Recommended)**를 선택합니다. OAuth 2.0을 지정하고 client ID·secret을 입력합니다.
4. card에서 채워진 Authorization·Token·Refresh URL을 확인합니다. 비어 있다면 MCP 표의 Entra URL을 사용하고, scope에는 아래처럼 **`offline_access`를 추가**합니다.

```text
https://api.powerplatform.com/copilotstudio-a2a/MCS.InvokeAsA2A offline_access
```

![A2A 연결 폼에서 OAuth와 offline_access를 설정한 예시](/mwkorea/assets/images/2026-11-12-CopilotHarnessAgentsMcpA2a/image13.png)

Next 이후 생성된 커넥터의 redirect URL도 호출용 앱의 **Web redirect URI**로 등록합니다. 이어서 Create new connection으로 연결하고 로그인합니다.

### 자동으로 가져온 description도 검토하세요

Review and add에서 가져온 이름·설명을 읽어야 합니다. 원문에서는 full details를 선택해도 “HR Policy라는 Copilot Studio 에이전트” 정도의 일반적인 설명만 들어왔습니다.

![업무 범위를 설명하지 못하는 A2A 기본 description 예시](/mwkorea/assets/images/2026-11-12-CopilotHarnessAgentsMcpA2a/image14.png)

A2A 라우팅은 **연결된 에이전트 이름·설명, 사용자 메시지와 대화 맥락, 호출자 instructions**를 함께 사용합니다. “HR 정책 질문에 사용하며 휴가·출장·경비를 다룬다”처럼 실제 범위를 적고, 겹치는 도구가 있으면 호출자 지시도 보완합니다. skills를 잘 적었다고 라우팅까지 자동 해결되는 것은 아닙니다.

Add to agent 후 저장하고 Preview에서 테스트할 수 있습니다. **호출자는 아직 게시하지 않아도 Preview 테스트가 가능하지만 대상은 이미 게시되어 있어야 합니다.**

![A2A 호출 결과와 context ID를 확인하는 activity trace](/mwkorea/assets/images/2026-11-12-CopilotHarnessAgentsMcpA2a/image15.png)

원문의 첫 응답은 약 17초였으며, 캡처에는 17.5초가 표시됩니다. 이 역시 환경별 성능을 보장하는 값이 아닙니다.

### 후속 대화의 -32004 오류

원문 테스트에서 도구의 기본 안내대로 `context_id`와 `task_id`를 모두 재전달하면, 완료된 task에 대해 **`-32004` / Task is in a terminal state** 오류가 발생했습니다. **`context_id`만 전달하면 맥락이 유지**됐습니다.

두 테스트에서는 호출 모델이 `task_id` 없이 자동 재시도했지만, 이를 항상 복구된다는 보장으로 삼지 마세요. 추적에서 오류가 보이면 후속 호출의 식별자와 완료 상태를 확인해야 합니다.

## 운영·거버넌스 체크포인트

두 채널 모두 게시된 버전을 호출하므로 **저장만 한 변경은 제공되지 않습니다**. 크레딧은 **호출 대상 에이전트의 환경에서 소비**되므로, 전문 에이전트 운영 팀과 비용·사용량 책임을 정하는 것이 좋습니다.

대상 에이전트의 hooks도 두 채널에서 동작합니다. 원문은 `metadata.channel`이 각각 `mcs-agent-as-mcp`, `mcs-agent-as-a2a`이며 `userAadObjectId`가 로그인한 호출 사용자라고 설명합니다. 이 정보를 활용한 정책은 사용자 위임 호출과 직접 대화를 구분하는 데 도움이 됩니다.

도입 검증에는 프로토콜 호환성, delegated permissions와 동의, secret 수명 관리, 커넥터별 redirect URI, 실제 사용자 공유, 도구 라우팅, 후속 대화와 대상 환경 크레딧을 함께 포함하세요. **현재 문서의 프리뷰 조건과 실제 환경 UI를 확인한 뒤 적용**하는 것이 중요합니다.

## 마무리

기존 에이전트를 버리고 새로 만드는 대신, 전문 에이전트를 연결해 점진적으로 확장할 수 있다는 점이 이번 사례의 가치입니다. 연결 URL보다 중요한 것은 **누구의 신원으로 호출하는지, 어떤 질문을 위임하는지, 일반 사용자에게도 제대로 작동하는지**입니다.

> **출처**: [Call Microsoft Copilot Harness Agents from Other Copilot Studio Agents with MCP and A2A — Shaji Sivaraman, The Custom Engine](https://microsoft.github.io/mcscatblog/posts/call-ghcp-harness-agents-mcp-a2a/)  
> 자세한 내용은 원문 참조. 원문과 이미지는 저자의 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 표기에 따라 출처를 밝히며, 본문은 한국어로 재구성한 해설입니다.  
> **공식 문서 보완 확인(2026-11-13)**: [MCP·A2A 채널 프리뷰](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/publication-channels-mcp-agent-to-agent), [Custom connector OBO 인증](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-custom-connector-on-behalf-of)
