---
title: "인사말 전에 문을 닫는다: Copilot Studio 에이전트의 Microsoft 인증 강제"
date: 2026-06-14T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Authentication
  - MicrosoftEntra
  - DirectLine
  - M365AgentsSDK
  - Governance
excerpt: "Power Platform admin center의 Authentication for agents 정책에 Require Microsoft authentication 옵션이 추가됐습니다. 직원용 에이전트에서 인증 전 인사말조차 노출하지 않고, M365 Agents SDK 통합은 유지하면서 raw Direct Line 접근을 차단할 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 인사말 전에 문을 닫는다: Copilot Studio 에이전트의 Microsoft 인증 강제

Copilot Studio 에이전트에서 인증을 요구하는 것과 **인증 전에는 아무 콘텐츠도 노출하지 않는 것**은 다릅니다. Manual authentication with Entra ID를 사용해도 사용자가 채팅을 열면 Direct Line 대화가 먼저 만들어지고, 메이커가 편집한 로그인 안내 메시지가 인증 전에 표시될 수 있습니다.

직원용 내부 에이전트라면 인사말조차 신원 경계 밖에 노출하지 않는 것이 바람직합니다. Power Platform admin center의 **Authentication for agents** 정책에 추가된 **Require Microsoft authentication** 옵션이 이 요구를 해결합니다.

![Copilot Studio 에이전트 인증 제어](/mwkorea/assets/images/2026-06-14-CopilotStudioAuthenticationControls/image1.png)

---

## 기존 DLP 제어의 한계

DLP에서 익명 에이전트를 막기 위해 **Chat without Microsoft Entra ID authentication** 채널을 차단할 수 있습니다. 하지만 직원용 사용자 지정 UI에 권장되는 M365 Agents SDK Copilot Studio client와 raw Direct Line은 같은 **Direct Line channels** 제어를 공유합니다.

Direct Line 채널 자체를 끄면 인증 전 콘텐츠 표면은 닫히지만, SDK client의 위임 인증 경로도 함께 중단됩니다.

### 두 연결 방식의 차이

- **Raw Direct Line / WebChat**: 연결 직후 인증 전에 대화가 생성되고 메이커가 작성한 로그인 메시지가 표시될 수 있습니다.
- **M365 Agents SDK client**: Microsoft 인증이 완료되기 전에는 Copilot Studio 응답을 받을 수 없어 인증 전 대화·콘텐츠 표면이 없습니다.

따라서 관리자가 원하는 것은 채널 전체를 끄는 것이 아니라, SDK client는 유지하면서 raw Direct Line의 인증 전 표면만 닫는 것입니다.

## 새로운 Require Microsoft authentication

Power Platform admin center의 **Security > Identity and access > Authentication for agents**에서 환경 단위 정책을 설정합니다.

![Authentication for agents 정책 옵션](/mwkorea/assets/images/2026-06-14-CopilotStudioAuthenticationControls/image2.png)

| 관리자 정책 | 메이커가 선택할 수 있는 방식 | 차단되는 방식 |
|---|---|---|
| No authentication | 익명 포함 모든 방식 | 없음 |
| Require Microsoft authentication | Authenticate with Microsoft만 | Manual auth, 익명 |
| Require Entra authentication | Microsoft 또는 Manual Entra ID | 익명, Generic OAuth 2 |
| Allow all supported methods | Microsoft, Manual Entra ID, Generic OAuth 2 | 익명 |

기존 **Require Entra authentication**은 Manual auth with Entra ID를 허용하기 때문에 인증 전 로그인 메시지 표면이 남습니다. 새 **Require Microsoft authentication**은 통합된 `Authenticate with Microsoft`만 허용합니다.

## Direct Line 문제를 해결하는 방식

Raw Direct Line은 `Authenticate with Microsoft`를 지원하지 않습니다. 이 정책을 강제하면 다음 결과가 나타납니다.

- Direct Line endpoint 자체는 유지됩니다.
- Raw Direct Line client는 콘텐츠를 받기 전에 오류가 발생합니다.
- 메이커가 작성한 로그인 메시지도 공유되지 않습니다.
- M365 Agents SDK client는 같은 채널을 통해 계속 동작합니다.

즉, Direct Line channels를 끄지 않고도 직원용 앱에 필요한 SDK 연결은 유지하면서 인증 전 노출을 차단합니다.

## 기존 에이전트에 대한 영향

정책은 소급 적용됩니다. 이미 게시된 에이전트가 `Authenticate with Microsoft`를 사용하지 않는다면 정책 적용 즉시 다음 영향을 받습니다.

- 게시가 차단됩니다.
- 메이커가 인증 방식을 수정할 때까지 응답을 중단합니다.

따라서 기존 환경에 적용하기 전 영향 범위를 파악해야 합니다.

## Copilot Studio Kit로 영향 범위 확인

[Copilot Studio Kit](https://marketplace.microsoft.com/en-us/product/dynamics-365/microsoftpowercatarch.copilotstudiokit2?tab=overview)의 인벤토리 모듈은 환경을 스캔해 에이전트 인증 구성을 Dataverse에 저장합니다.

![Copilot Studio Kit 인증 인벤토리](/mwkorea/assets/images/2026-06-14-CopilotStudioAuthenticationControls/image3.png)

Agent Details 테이블의 **End User Authentication Type** 열을 확인합니다.

- `Integrated`: Authenticate with Microsoft
- `Custom Entra ID`: 새 정책 적용 시 차단 대상
- `Generic OAuth 2`: 차단 대상
- 빈 값: 인증 없음으로 차단 대상

`Integrated`가 아닌 행을 필터링하면 정책 적용 시 영향을 받을 에이전트 목록을 만들 수 있습니다.

![인증 정책 적용 전 점검 화면](/mwkorea/assets/images/2026-06-14-CopilotStudioAuthenticationControls/image4.png)

## 권장 적용 방식

- 직원용 신규 환경은 처음부터 **Require Microsoft authentication**을 기본값으로 설정합니다.
- 직원용과 고객용 에이전트를 같은 환경에 섞지 않습니다.
- 기존 환경은 Copilot Studio Kit로 영향 범위를 확인한 뒤 메이커에게 변경 일정을 안내합니다.
- M365 Agents SDK client를 사용하는 앱의 인증 흐름을 정책 적용 전후로 테스트합니다.
- 정책을 적용한 뒤 raw Direct Line에서 콘텐츠가 노출되지 않는지 확인합니다.

## 마무리

에이전트 인증 거버넌스의 핵심은 채널 이름이 아니라 **어떤 신원 상태에서 콘텐츠를 볼 수 있는가**입니다. Require Microsoft authentication은 직원용 에이전트에서 Microsoft 로그인을 처음부터 강제하고, SDK 기반 사용자 지정 UI는 유지하면서 Direct Line의 인증 전 콘텐츠 표면을 닫는 더 명확한 통제 수단입니다.

---

> **원문**: [The Admin Control That Closes the Door Before "Hello" (The Custom Engine, Microsoft Copilot Studio CAT, 2026-06-14)](https://microsoft.github.io/mcscatblog/posts/agent-authentication-controls/)
>
> 자세한 내용은 원문을 참조하세요.
