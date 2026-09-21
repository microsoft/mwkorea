---
title: "Copilot 웹 앱 URL 전환 전 copilot.cloud.microsoft 연결을 허용하세요"
date: 2026-09-09T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftCopilot
  - NetworkSecurity
  - CloudMicrosoft
  - Firewall
  - TenantRestrictions
excerpt: "Copilot 웹 앱 사용자는 m365.cloud.microsoft에서 copilot.cloud.microsoft로 자동 이동하게 됩니다. 2026년 10월 남은 조직까지 리디렉션되기 전에 프록시, 방화벽과 보안 게이트웨이가 전체 *.cloud.microsoft 도메인을 허용하는지 확인해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 웹 앱 URL 전환 전 copilot.cloud.microsoft 연결을 허용하세요

Microsoft Copilot 웹 앱의 주소가 `m365.cloud.microsoft`에서 `copilot.cloud.microsoft`로 전환됩니다. 사용자는 자동으로 새 주소로 이동하지만 네트워크나 보안 제품이 이를 막으면 웹 앱 자체에 접근하지 못할 수 있습니다.

새 주소도 `*.cloud.microsoft` 범위 안에 있으며 Microsoft가 안내한 보안, 규정 준수와 엔터프라이즈 허용 목록 속성을 유지합니다. 이미 Microsoft 365 Copilot 권장 네트워크 구성을 따르는 조직은 추가 변경이 필요하지 않지만, 개별 URL만 허용한 환경은 점검이 필요합니다.

---

## 두 단계로 진행되는 리디렉션

2026년 9월 초에는 `copilot.cloud.microsoft` 연결이 이미 가능한 조직의 사용자가 먼저 리디렉션됩니다. 10월 초에는 9월에 전환되지 않은 나머지 사용자도 새 주소로 이동합니다.

이 변경은 사용자에게 새 URL을 직접 입력하도록 요구하는 방식이 아닙니다. 기존 주소에서 자동 이동하므로, 실제 위험은 이동 대상 주소가 프록시나 방화벽에서 차단되는 경우입니다.

## 확인해야 할 보안 제어

다음과 같은 제어가 `copilot.cloud.microsoft` 또는 상위 도메인의 연결을 방해하지 않는지 확인해야 합니다.

- 레거시 URL 필터와 URL 범주 제한
- 프록시와 방화벽 규칙
- 보안 웹 게이트웨이 및 SSE/SASE 플랫폼
- 테넌트 제한과 조건부 액세스 정책
- 앱 제어 정책
- 관리형 장치의 네트워크 설정

네트워크, 엔드포인트, 보안 운영팀이 각각 다른 제어 지점을 관리한다면 함께 검증하는 것이 좋습니다. 한 구간에서만 허용해도 다른 보안 계층이 새 주소를 차단할 수 있기 때문입니다.

## 일부 주소만 고르는 허용 방식은 지원되지 않습니다

Microsoft는 `*.cloud.microsoft` 전체를 조직의 허용 목록에 추가하라고 권고합니다. 이 와일드카드 도메인 안에서 Microsoft 365 애플리케이션 URL 일부만 선택해 허용하는 구성은 지원하지 않는다고 명시했습니다.

[Microsoft 365 연결 테스트](https://connectivity.m365.cloud.microsoft/copilot)를 사용하면 새 주소와 `*.cloud.microsoft` 연결을 확인할 수 있습니다. 공지 시점의 권고는 차단을 발견한 조직이 **2026년 9월 10일 전** Microsoft 계정 담당자와 가능한 선택지를 논의하는 것이었습니다. 현재 적용 상태는 관리 센터와 실제 연결 테스트로 다시 확인해야 합니다.

## 개인 Microsoft 계정 차단이 목적이라면

조직이 개인 Microsoft 계정 로그인을 막기 위해 `copilot.cloud.microsoft` 자체를 차단했다면 서비스 URL 차단 대신 Microsoft Entra의 **Tenant Restrictions**를 고려할 수 있습니다. 이 방식은 관리형 네트워크나 장치에서 소비자 계정 인증을 제한하면서 Copilot 서비스 주소 연결은 허용하도록 목표를 좁힙니다.

정책 전환은 조직의 인증 및 보안 요구 사항에 맞춰 검증해야 합니다. 공지는 특정 조직에 대한 구성값을 제시하지 않으므로 최신 Microsoft Entra 지침을 기준으로 적용해야 합니다.

## 일정과 운영 권고

| 단계 | 일정 |
|---|---|
| 연결 가능한 조직 우선 리디렉션 | 2026년 9월 초 |
| 남은 사용자 리디렉션 | 2026년 10월 초 |

전환 전에 권장 Copilot 네트워크 요구 사항과 전체 `*.cloud.microsoft` 허용 여부를 확인하고, 실제 사용자 경로에서 연결 테스트를 실행해야 합니다. 새 주소를 막은 채 리디렉션을 맞으면 Copilot 웹 앱을 사용할 수 없는 서비스 중단으로 이어질 수 있습니다.

---

> **출처**
>
> - 원문 ID: **MC1462915** — *Allow connections to copilot.cloud.microsoft before the Copilot URL redirect*
> - 원문: [https://mc.merill.net/message/MC1462915](https://mc.merill.net/message/MC1462915)
> - [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
