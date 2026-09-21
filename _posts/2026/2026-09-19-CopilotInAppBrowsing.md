---
title: "Copilot 대화 옆에서 웹페이지 열기: Windows·Mac 앱 내 브라우징"
date: 2026-09-19T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftCopilot
  - Windows
  - Mac
  - InAppBrowsing
  - DeviceManagement
excerpt: "Microsoft Copilot 데스크톱 앱에서 링크를 대화 옆의 브라우저 패널로 여는 기능을 선택한 장치에서 먼저 시험할 수 있습니다. 기본 활성화는 아니며, 관리자 옵트인과 로컬 브라우징 데이터 관리가 필요합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 대화 옆에서 웹페이지 열기: Windows·Mac 앱 내 브라우징

Copilot이 알려 준 링크를 확인할 때 대화와 브라우저를 계속 오가게 됩니다. 웹페이지를 바로 옆에서 열 수 있다면 답변과 참고 자료를 함께 보기 편리합니다.

메시지 센터 **MC1474455**는 Windows와 Mac의 Microsoft Copilot 앱에 **앱 내 브라우징**을 소개합니다. 지금은 관리자가 선택한 장치에 옵트인해 시험할 수 있으며, 기본 활성화된 기능은 아닙니다.

---

## 대화 오른쪽에 웹페이지 표시

앱에서 링크를 클릭하면 Copilot 대화 오른쪽의 측면 패널에 웹사이트가 열립니다. 여러 링크는 별도 탭으로 열리고, 필요에 따라 탭을 전환하거나 패널을 닫을 수 있습니다.

![Copilot 대화 옆의 측면 패널에서 웹페이지를 여는 원문 화면](/mwkorea/assets/images/2026-09-19-CopilotInAppBrowsing/image1.png)

패널 크기를 조절할 수 있으며, 패널 헤더의 버튼으로 전체 화면 모드를 켜거나 끌 수도 있습니다.

![앱 내 브라우저 패널의 크기와 화면 표시를 조절하는 예시](/mwkorea/assets/images/2026-09-19-CopilotInAppBrowsing/image2.png)

## 외부 브라우저도 계속 사용

| 방법 | 원문 안내 |
|---|---|
| 채팅 링크의 점 세 개 메뉴 | External browser 선택 |
| 주소 복사 | Copy the URL 후 외부 브라우저에 붙여넣기 |
| 측면 패널 탭 우클릭 | External browser 선택, 원문은 9월 21일 제공 예정으로 표기 |

마지막 항목은 9월 19일 기준 예정 기능이므로 현재 모든 장치에서 사용할 수 있다고 안내하지 마세요.

## 관리자가 시험 장치를 선택

현재 조기 접근은 옵트인 방식입니다. 원문은 장치 관리 시스템에서 **BrowsingEnabled** 정책을 켜는 방법을 안내하며, 배포와 관련 정책은 [Microsoft Edge 정책 문서](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies) 및 [Windows 정책 구성 안내](https://learn.microsoft.com/en-us/deployedge/configure-microsoft-edge)를 연결합니다.

| 구분 | 일정·상태 |
|---|---|
| 옵트인 조기 접근 | 현재 사용 가능, 기본 활성화 아님 |
| 더 넓은 배포 | 2026년 11월 하순 시작 |
| 대상 앱 | Windows·Mac용 Copilot 데스크톱 앱 |

원문에 없는 Mac 관리 경로나 정책 명령을 Windows 안내에서 추측해 적용하지 않는 것이 좋습니다. 선택한 관리 장치에서 배포와 브라우징 동작을 살펴보고, 사용자와 지원팀의 안내를 준비하세요.

## 로컬에 저장되는 데이터 확인

원문은 **검색·방문 이력, 쿠키, 자동 완성 정보**가 로컬 장치에 저장된다고 설명합니다. Edge와 같은 저장 메커니즘을 사용하며 제시된 사용자 데이터 경로는 다음과 같습니다.

```text
%localappdata%\Microsoft\Copilot\User Data
```

이 경로는 Windows 형식입니다. Mac에서도 같은 경로를 사용한다고 해석해서는 안 됩니다. 장치 관리 담당자는 조직의 브라우징 데이터 관리와 관련 정책을 검토할 필요가 있습니다.

이 기능은 웹사이트나 다른 Copilot 기능으로 생성된 HTML을 **보는 방식**을 바꿉니다. 원문은 생성형 AI를 새롭게 생성하거나 조종하는 기능을 추가한 것은 아니라고 명시합니다. 웹페이지를 열었다는 이유만으로 자동 요약이나 페이지 작업 수행까지 이번 기능에 포함됐다고 안내하지 마세요.

---

> **출처**
>
> - 원문 ID: **MC1474455** — *In-app browsing in Copilot app*
> - 원문: [MC1474455](https://mc.merill.net/message/MC1474455)
> - [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
