---
title: "작업 표시줄에 나타난 Copilot, 이제 조직의 안내 알림도 함께 보냅니다"
date: 2026-11-25T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Windows11
  - Intune
  - OrganizationalMessages
  - Adoption
excerpt: "Microsoft 365 관리 센터에서 선택한 그룹에 Microsoft Copilot을 작업 표시줄로 고정할 때 일회성 안내 알림을 예약할 수 있게 됩니다. 앱 설치와 Intune 등 적용 조건, 2026년 11~12월 예정된 배포 일정을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 작업 표시줄에 나타난 Copilot, 이제 조직의 안내 알림도 함께 보냅니다

회사에서 Copilot 앱을 배포하더라도 직원이 작업 표시줄의 새 아이콘을 알아차리지 못하거나, 왜 생겼는지 몰라 사용하지 않는 경우가 있습니다. 배포 정책과 사용자 안내가 따로 움직이기 때문입니다.

Microsoft는 Message Center 공지 **MC1567263**에서 작업 표시줄 고정과 사용자 안내를 연결하는 선택적 알림 기능을 소개했습니다. 관리자가 특정 그룹에 Microsoft Copilot을 고정하면서 일회성 알림을 예약하면, 해당 사용자는 조직의 안내와 함께 **Open Copilot** 동작으로 데스크톱 앱을 열 수 있습니다.

이 글은 한국 시간 2026년 11월 25일에 해당하는 공지 발행 시점의 내용을 정리한 것입니다. 새로운 모델이나 에이전트 실행 기능이 아니라, **Copilot 접근성과 도입 커뮤니케이션을 개선하는 관리 기능**입니다.

---

## 무엇이 달라지나요?

Microsoft 365 관리 센터의 **Pin Microsoft Copilot to the Windows taskbar** 설정에서 **Pin for selected groups**를 선택한 뒤, 고정 대상 사용자에게 안내 알림을 보내도록 설정할 수 있습니다.

알림은 기본으로 켜지지 않습니다. 관리자가 명시적으로 선택하고 발송 일정을 정해야 하며, 예약 후에는 **Organizational Messages**에서 관리합니다. 사용자에게는 조직이 작업 표시줄에서 Copilot을 쉽게 열 수 있도록 했다는 사실과 앱 실행 동작이 제공됩니다.

![Organizational Messages에서 Copilot 작업 표시줄 안내 알림의 세부 정보를 확인하는 화면](/mwkorea/assets/images/2026-11-25-CopilotTaskbarPinNotification/image1.png)

원문은 첫 번째와 두 번째 관리 화면에 같은 이미지 URL을 사용하므로, 이 글에는 중복 이미지를 한 번만 실었습니다.

## 적용 대상과 사전 조건

| 구분 | 공지에서 명시한 조건 |
|---|---|
| 관리자 | Intune Administrator 또는 Global Administrator 역할 |
| 테넌트 | 활성 Microsoft Intune 라이선스가 최소 1개 있어야 함 |
| 사용자 및 디바이스 | 관리자가 선택한 그룹에 포함된 Intune 관리 Windows 11 사용자 |
| 앱 | 대상 사용자에게 Microsoft Copilot 앱이 설치되어 있어야 함 |
| 지원 설정 | 출시 시점에는 **Pin for selected groups**에서만 알림 예약 지원 |

특히 **앱이 설치되지 않았다면 작업 표시줄 고정과 알림 모두 표시되지 않습니다.** 그룹을 지정했다는 사실만으로 모든 대상자에게 전달된다고 판단하면 안 됩니다.

Intune 라이선스가 없는 테넌트는 XML 구성 파일로 앱을 고정하는 방법을 사용할 수 있지만, 이번 공지의 알림 기능까지 제공되는 것은 아닙니다. 알림은 Microsoft 365 관리 센터의 지원되는 설정 흐름을 요구합니다. 다른 고정 옵션에 대한 지원은 향후 계획이며, 확정된 제공 기능으로 보아서는 안 됩니다.

## 설정은 이렇게 진행합니다

1. 테넌트의 활성 Intune 라이선스와 대상 사용자의 Copilot 앱 설치 여부를 확인합니다.
2. [Microsoft 365 관리 센터의 작업 표시줄 고정 설정](https://admin.cloud.microsoft/?#/copilot/settings/ViewAll/:/CopilotSettings/PinCopilotAppInTaskbar)을 엽니다.
3. **Pin for selected groups**를 선택하고 적용할 그룹을 지정합니다.
4. Copilot을 고정한 뒤 사용자에게 알리도록 하는 옵션을 선택합니다.
5. 일회성 알림의 일정을 예약합니다.
6. 예약한 메시지는 Organizational Messages에서 확인하고 관리합니다.

![조직이 Copilot을 작업 표시줄에 추가했다는 안내와 앱 열기 동작을 보여주는 사용자 알림](/mwkorea/assets/images/2026-11-25-CopilotTaskbarPinNotification/image3.png)

이 기능을 사용하지 않을 조직은 별도로 조치할 필요가 없습니다.

## 배포 일정과 확인할 범위

공지의 **Worldwide 일반 공급(GA) 배포 예정**은 다음과 같습니다.

| 단계 | 공지 기준 일정 |
|---|---|
| 배포 시작 | 2026년 11월 말 |
| 배포 완료 예상 | 2026년 12월 말 |

이는 순차 배포 계획이지 모든 테넌트에서 같은 날 사용할 수 있다는 뜻은 아닙니다. 원문은 기능 출시 시점에 추가 Microsoft Learn 문서가 제공될 예정이라고 설명하므로, 이 글에서는 아직 제시되지 않은 문서나 설정 항목을 가정하지 않았습니다.

## 한국 조직의 도입 체크포인트

파일럿 그룹에 먼저 적용해 앱 설치, 실제 작업 표시줄 고정, 알림 표시를 각각 확인하는 방식이 적절합니다. 세 가지를 분리해서 보면 미설치 문제와 메시지 전달 문제를 혼동하지 않을 수 있습니다.

사내 안내에서는 앱을 여는 방법뿐 아니라 조직에서 허용하는 활용 범위와 지원 창구를 함께 설명하는 것이 좋습니다. 다만 이번 공지는 **별도의 Copilot 유료 라이선스 부여나 모든 AI 기능의 사용 권한 확대를 발표한 것이 아닙니다.** 앱 접근 경로와 서비스 이용 권한은 구분해 안내해야 합니다.

## 마무리

이번 변화는 Copilot을 직원의 화면에 배치하는 데서 끝내지 않고, 왜 배치했으며 어떻게 시작하는지까지 연결합니다. 관리자는 선택적 일회성 알림을 기존 도입 교육과 맞춰 예약하고, 대상 그룹의 앱 설치 상태를 먼저 확인하는 것이 핵심입니다.

> **출처**: 원문 ID **MC1567263**, [Microsoft 365 Copilot: New notification option when pinning Copilot to the Windows taskbar](https://mc.merill.net/message/MC1567263)  
> **Microsoft 365 Roadmap**: [공식 Roadmap 확인](https://www.microsoft.com/en-us/microsoft-365/roadmap) — 해당 공지에는 개별 Roadmap ID가 명시되어 있지 않습니다.  
> **실제 출시 일정·기능은 변경될 수 있습니다**
