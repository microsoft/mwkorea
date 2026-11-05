---
title: "유료 Copilot 사용자만 작업 표시줄에 고정하기: 관리자 센터 옵션이 바뀝니다"
date: 2026-10-30T00:00:00 KST
categories:
  - Copilot
tags:
  - Administration
  - Windows
  - EntraID
  - Intune
excerpt: "Microsoft 365 관리자 센터에서 유료 Copilot 라이선스 사용자만 앱 고정을 대상으로 지정할 수 있게 됩니다. 12월 배포 예정이며 Entra 그룹 생성 권한과 기존 Do not pin 설정의 표시 변경을 확인해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 유료 Copilot 사용자만 작업 표시줄에 고정하기: 관리자 센터 옵션이 바뀝니다

Copilot 앱을 모든 직원에게 똑같이 고정하는 대신 실제 유료 라이선스 사용자에게 집중해 배포하고 싶은 조직이 있습니다. Microsoft 365 관리자 센터에 이를 위한 새 대상 옵션이 추가됩니다.

동시에 미설정 상태에서 **Do not pin**이 기본 선택돼 보이던 표시 방식도 바뀝니다. 화면의 기본 표시와 기기에 적용되는 정책을 구분해서 이해해야 합니다.

---

## 라이선스 기반 고정 옵션

관리자 센터의 **Copilot > Settings > Pin Microsoft Copilot app to the Windows taskbar**에서 유료 Microsoft 365 Copilot 라이선스 사용자 대상 옵션을 선택할 수 있습니다.

저장하면 관리자 센터가 Microsoft Entra에 라이선스 기반 그룹을 만들고 기존 Intune 정책 흐름을 통해 대상에 적용합니다. 따라서 **설정하는 관리자에게 Entra 보안 그룹 생성 권한이 필요**하며, 권한이 없으면 필요한 그룹을 만들 수 없어 변경이 저장되지 않습니다.

![유료 라이선스 사용자 대상 Copilot 앱 고정 옵션](/mwkorea/assets/images/2026-10-30-CopilotPaidLicensePinning/image1.png)

## 기존 설정은 어떻게 보이나요?

| 기존 상태 | 변경 후 |
|---|---|
| 미설정 | 어떤 옵션도 기본 선택되지 않음. 기기 고정 동작은 바뀌지 않음 |
| Do not pin 저장 | 새 고정은 추가되지 않지만 화면에서는 미선택으로 보임. 명시적으로 표시하려면 다시 선택·저장 |
| 전체 또는 선택 그룹 고정 | 기존 선택과 동작 유지 |

**Do not pin은 새 고정 추가를 막는 설정이지 이미 있는 고정을 제거하는 설정이 아닙니다.** 혼합 대상이 필요하면 기존 선택 그룹 옵션도 사용할 수 있습니다.

## 일정과 준비

전 세계 GA 배포는 **2026년 12월 초 시작, 중순 완료 예정**입니다. 기존 설정과 Entra 그룹 생성 권한을 확인하고, 실제 변경 시에는 조직의 정책 승인 절차를 따르세요. 이 글은 설정 변경을 수행한 것이 아니라 공지 내용을 설명합니다.

> **출처**: MC1530612 — [Microsoft 365 admin center: Pin Microsoft Copilot app setting for users with a paid Microsoft 365 Copilot license](https://mc.merill.net/message/MC1530612). [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap). 원문에 개별 Roadmap ID는 표시되어 있지 않습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
