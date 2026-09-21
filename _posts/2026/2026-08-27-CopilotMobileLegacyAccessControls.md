---
title: "모바일 Copilot Chat 접근 단순화: 두 레거시 제어가 더 이상 차단하지 않습니다"
date: 2026-08-27T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotChat
  - Mobile
  - Intune
  - Privacy
  - Governance
excerpt: "Microsoft 365 Copilot 모바일 앱에서 두 가지 레거시 모바일 전용 설정이 Copilot Chat 접근을 더 이상 제한하지 않게 됩니다. 관리자는 실제 접근을 결정하는 현재의 Copilot Chat 정책과 라이선스 배정을 다시 확인해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 모바일 Copilot Chat 접근 단순화: 두 레거시 제어가 더 이상 차단하지 않습니다

Microsoft 365 Copilot 모바일 앱의 Copilot Chat 접근 방식이 웹과 데스크톱에 더 가까워집니다. 과거 모바일에서만 별도로 접근을 막던 두 설정이 더 이상 차단 수단으로 작동하지 않기 때문입니다.

이번 변경은 Copilot Chat 자체를 모든 사용자에게 새로 허용한다는 뜻은 아닙니다. 이미 Copilot Chat을 사용할 수 있는 사용자에게 모바일 앱에서도 일관된 접근 경험을 제공하는 변화이므로, 관리자는 기존 정책을 어떤 목적으로 사용했는지부터 점검해야 합니다.

---

## 더 이상 모바일 접근을 제한하지 않는 두 설정

정식 출시 후 다음 두 제어는 iOS와 Android의 **Microsoft 365 Copilot 모바일 앱**에서 Copilot Chat 접근을 제한하지 않습니다.

- Intune 정책 `com.microsoft.office.officemobile.BingChatEnterprise.IsAllowed`
- 개인정보 제어 **Analyze content**

조직이 이 설정 가운데 하나를 모바일 Copilot Chat 차단 장치로 사용했다면, 영향을 받던 사용자는 웹·데스크톱에서 허용된 것과 동일하게 모바일에서도 다시 접근할 수 있습니다. 변경은 기본으로 적용되며 사용자 조치는 필요하지 않습니다.

중요한 범위도 분명합니다. 공지는 두 **레거시 모바일 전용 제어의 제한 효과**가 사라진다고 설명할 뿐, Copilot Chat의 현재 관리 정책이나 사용자 자격을 없앤다고 안내하지 않습니다. 따라서 “이 두 설정을 꺼 두었으니 모바일은 계속 차단된다”는 운영 가정만 수정해야 합니다.

## 일정과 대상 환경

| 항목 | 일정 |
|---|---|
| 정식 출시(GA) | 2026년 8월 중순 시작 |
| 완료 예상 | 2026년 9월 말 |
| 대상 클라우드 | Worldwide, GCC, GCC High, DoD |
| 대상 앱 | Microsoft 365 Copilot 모바일 앱(iOS, Android) |

롤아웃은 테넌트마다 순차 적용될 수 있습니다. 같은 조직에서도 앱 버전이나 배포 시점에 따라 사용자가 변화를 확인하는 시점이 다를 수 있으므로, 안내 문서에는 완료 예정 시점까지 함께 적는 편이 좋습니다.

## 관리자가 확인할 사항

별도의 사전 설정은 요구되지 않지만, 아무것도 살펴볼 필요가 없다는 뜻은 아닙니다.

1. **두 설정의 사용 목적을 조사합니다.** 모바일 Copilot Chat 차단을 위해 배포한 Intune 구성 프로필이나 개인정보 기준선이 있는지 확인합니다.
2. **현재 Copilot Chat 접근 정책을 검토합니다.** 실제 허용·차단 의도와 사용자 범위가 최신 관리 방식에 반영되어 있는지 [Copilot Chat 관리 문서](https://learn.microsoft.com/en-us/copilot/manage)를 기준으로 확인합니다.
3. **지원 문서를 고칩니다.** `BingChatEnterprise.IsAllowed` 또는 Analyze content가 모바일 Chat을 막는다고 적은 도움말, 운영 절차, 헬프데스크 응답문을 갱신합니다.
4. **대상 사용자에게 알립니다.** 이전에 모바일에서만 접근하지 못했던 사용자는 변경을 보안 우회나 오류로 오해할 수 있습니다.
5. **실제 적용을 검증합니다.** 대표 iOS·Android 관리 기기에서 정책 적용 상태와 Copilot Chat 접근 결과를 함께 시험합니다.

## 개인정보 제어의 의미를 과도하게 확대하지 마세요

Analyze content가 모바일 Copilot Chat의 접근 차단 수단에서 제외된다고 해서 모든 개인정보 설정이 무효가 되는 것은 아닙니다. 이번 공지에서 확인되는 변화는 **해당 제어가 모바일 앱의 Copilot Chat 진입을 제한하지 않게 되는 것**입니다.

따라서 다른 연결 환경, 데이터 처리 동작, 규정 준수 설정까지 바뀐다고 추정해서는 안 됩니다. 보안 검토에서는 제거되는 제한 효과와 여전히 적용되는 조직의 Copilot 관리 체계를 구분해야 합니다.

## 정리

이번 업데이트의 핵심은 기능 추가보다 **접근 제어 경로의 정리**입니다. 모바일에만 남아 있던 두 레거시 설정을 기준으로 운영하던 조직은 의도와 실제 동작이 어긋날 수 있습니다.

관리자는 새 구성을 배포하기 전에 기존 프로필과 문서를 찾아내고, 현재 Copilot Chat 관리 정책이 모바일까지 원하는 범위를 정확히 표현하는지 확인해야 합니다. 사용자는 별도 조치 없이 변경을 받습니다.

---

> **출처**
>
> - 원문 ID: **MC1454386** — *Simplified access to Copilot Chat on the Microsoft 365 Copilot mobile app*
> - 메시지 센터: [https://mc.merill.net/message/MC1454386](https://mc.merill.net/message/MC1454386)
> - Microsoft 365 로드맵: [https://www.microsoft.com/microsoft-365/roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
