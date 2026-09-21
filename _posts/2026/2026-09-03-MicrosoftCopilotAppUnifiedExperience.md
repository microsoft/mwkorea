---
title: "Microsoft 365 Copilot 앱, 개인·업무 계정을 아우르는 Microsoft Copilot 앱으로 개편"
date: 2026-09-03T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft Copilot
  - Microsoft 365
  - Entra ID
  - Desktop
  - Mobile
  - Web
excerpt: >-
  Microsoft 365 Copilot 앱이 개인용 Microsoft 계정과 업무·학교용 Microsoft Entra ID 계정을 한 앱에서 더 명확히 구분하는 Microsoft Copilot 앱으로 바뀝니다.
  이름과 아이콘, 웹 주소, 데스크톱 아키텍처가 순차적으로 변경되지만 애플리케이션 ID와 기존 보안·규정 준수·엔터프라이즈 제어는 유지됩니다.
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Microsoft 365 Copilot 앱, 개인·업무 계정을 아우르는 Microsoft Copilot 앱으로 개편

Microsoft는 다른 Microsoft 365 앱과 마찬가지로 Copilot도 개인 계정과 업무 계정을 함께 다루는 단일 앱 경험으로 정리합니다. 사용자는 같은 앱 안에서 계정을 전환하되, 현재 개인용 Microsoft 계정인지 업무·학교용 Microsoft Entra ID 계정인지 더 분명하게 확인할 수 있게 됩니다.

이번 변화에는 앱 이름과 아이콘, 웹 주소, Windows·Mac 앱 아키텍처가 포함됩니다. 그러나 보안, 개인 정보 보호, 규정 준수와 엔터프라이즈 제어의 경계는 바뀌지 않으며, 업무 계정과 개인 계정의 데이터가 서로 흘러가는 변경도 아닙니다.

---

## 이름과 계정 표시가 달라집니다

‘Microsoft 365 Copilot 앱’은 더 단순한 **‘Microsoft Copilot 앱’** 이름과 새 아이콘을 사용합니다. 웹과 데스크톱 앱에서는 계정 종류에 따라 배경색을 다르게 표시하고, 업무·학교 계정에는 탐색 창 프로필 아래 **Work** 레이블을 보여 줍니다. 기존 Microsoft Entra ID 경험의 녹색 데이터 보호 방패도 계속 유지됩니다.

![새 Microsoft Copilot 앱 이름과 아이콘](/mwkorea/assets/images/2026-09-03-MicrosoftCopilotAppUnifiedExperience/image1.png)

조직이 개인용 Microsoft 계정 로그인을 허용하는 경우에는 Apple 또는 Google 자격 증명으로 개인 Microsoft 계정에 접근하는 로그인 방식도 관련됩니다. 사용자는 기존처럼 탐색 창의 계정 전환기를 이용해 개인 계정과 업무·학교 계정을 오갑니다.

## 웹 URL과 데스크톱 앱 변경

웹 앱 주소는 `m365.cloud.microsoft`에서 **`copilot.cloud.microsoft`**로 전환되며 기존 주소 사용자는 자동으로 리디렉션됩니다. 두 주소 모두 `*.cloud.microsoft` 도메인 안에 있으므로, Microsoft 365 Copilot의 권장 네트워크 구성을 이미 적용한 조직은 이 변경 때문에 별도의 네트워크 허용 목록을 수정할 필요가 없습니다.

![웹과 데스크톱에서 구분되는 업무 계정 경험](/mwkorea/assets/images/2026-09-03-MicrosoftCopilotAppUnifiedExperience/image2.png)

Windows와 Mac 앱에는 앞으로의 개선을 지원하는 새 아키텍처가 적용됩니다. Microsoft는 기능 세부 사항보다 기반 변경으로 설명하고 있으므로, 현재 공지되지 않은 기능을 미리 전제해서는 안 됩니다.

![개인 계정과 업무 계정의 시각적 구분](/mwkorea/assets/images/2026-09-03-MicrosoftCopilotAppUnifiedExperience/image3.png)

## 업데이트된 배포 일정

2026년 8월 21일 업데이트에서 URL 리디렉션 일정이 조정됐습니다.

- **2026년 8월 중순:** 모바일·웹 앱 전 세계 배포 시작, Windows·Mac 조기 액세스 옵트인 시작
- **2026년 8월 중순:** `copilot.cloud.microsoft`를 Frontier에서 테스트 가능
- **2026년 9월 초:** 웹 URL 리디렉션 표준 배포 시작
- **2026년 9월 중순:** Windows·Mac 앱 전 세계 배포 시작
- **2026년 9월 말:** 웹 URL 리디렉션 지연 배포 시작

Windows·Mac 조기 액세스는 시험 장치 그룹에 배포하는 방식이며, 특별 클라우드 환경에는 당시 옵트인이 제공되지 않습니다. 해당 환경의 조기 액세스 일정은 추후 별도로 안내될 예정입니다.

## 영향받는 사용자와 유지되는 제어

웹, Windows, Mac, 모바일에서 Microsoft 365 Copilot 앱을 쓰는 모든 사용자가 대상이며, **Microsoft 365 Copilot 및 Copilot Chat 사용자 모두**에게 적용됩니다. 별도의 새 라이선스 요구 사항은 공지되지 않았습니다.

애플리케이션 ID는 바뀌지 않아 기존 정책이 계속 작동합니다. 관리자는 Tenant Restrictions를 사용해 Copilot 앱의 개인 Microsoft 계정 접근을 계속 제한할 수 있습니다. 업무·학교 환경과 개인 환경의 입력 데이터도 서로 이동하지 않으며, 정부 클라우드를 포함한 기존 보안·규정 준수 제어는 유지됩니다.

다만 Windows Recall에서 이전 Microsoft Copilot 앱을 스냅샷 저장 대상에서 제외하도록 그룹 정책을 적용했다면 주의해야 합니다. 해당 필터는 새 앱에 자동 승계되지 않으므로 [새 Microsoft Copilot 앱을 대상으로 Recall 필터를 다시 구성](https://learn.microsoft.com/en-us/windows/client-management/manage-recall#app-and-website-filtering-policies)해야 합니다.

## 관리자가 준비할 일

관리자는 앱 이름, 아이콘, URL을 참조하는 사용자 안내와 교육, 헬프 데스크 문서를 업데이트해야 합니다. 업무 계정을 쉽게 알아볼 수 있도록 Microsoft Copilot 앱에 브랜드 바닥글을 추가하는 기능도 별도 공지 MC1238432의 일정과 설정 안내에 따라 검토할 수 있습니다.

또한 시험 그룹에서 새 Windows·Mac 앱을 검증하고, 개인 계정 허용 정책과 Recall 필터를 확인해야 합니다. URL은 같은 `*.cloud.microsoft` 경계에 남고 애플리케이션 ID도 유지되므로, 기존 정책을 무조건 새로 만드는 대신 실제 예외 항목만 점검하는 것이 핵심입니다.

---

> **출처**
> - Message Center ID: **MC1454108**
> - 원문 제목: **Microsoft 365 Copilot app update: Simpler Copilot access**
> - 원문: <https://mc.merill.net/message/MC1454108>
> - Microsoft 365 Roadmap: <https://www.microsoft.com/microsoft-365/roadmap>
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
