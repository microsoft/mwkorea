---
title: "Teams 어디서나 나란히 쓰는 Copilot Chat, 회의 음성 중지 제어까지"
date: 2026-09-12T00:00:00 KST
categories:
  - Copilot
tags:
  - Teams
  - Microsoft365Copilot
  - Meetings
  - Governance
excerpt: "Teams 채팅·채널·통화·회의에서 Copilot Chat을 나란히 사용할 수 있습니다. 회의 음성 처리를 중지하는 제어와 기존 Copilot 기록 접근 방식, 라이선스 외에 필요한 앱 허용 설정을 함께 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Teams 어디서나 나란히 쓰는 Copilot Chat, 회의 음성 중지 제어까지

Teams에서 대화를 보다가 Copilot을 쓰기 위해 맥락을 옮길 필요가 줄어듭니다. Microsoft는 채팅, 채널, 통화, 회의에 **나란히 열리는 Copilot Chat**을 제공해 기존 Copilot 기능에 Microsoft 365 및 웹 데이터 활용을 더합니다.

2026년 9월 11일 업데이트된 MC1156360에는 회의 중 음성 처리를 중지하는 제어와 관리자 준비 사항도 포함되어 있습니다. 단순한 버튼 위치 변경이 아니라 회의 운영 정책과 기존 기록 안내를 함께 점검할 업데이트입니다.

---

## 지원 환경과 대화 세션

대상은 **Microsoft 365 Copilot 라이선스 사용자**입니다. Teams Windows·Mac 데스크톱 및 웹에서 각 화면 오른쪽 위 Copilot 아이콘으로 접근합니다. 웹 지원 브라우저는 Chrome, Edge, Firefox, Safari입니다.

![Teams 대화 옆에서 열리는 Copilot Chat 예시](/mwkorea/assets/images/2026-09-12-TeamsCopilotChatAcrossConversations/image1.png)

대화 창에서 새 Copilot Chat 세션을 만들거나 다른 세션에 접근할 수 있습니다. 다시 열면 해당 대화 창 안에서 마지막으로 사용한 세션으로 돌아갑니다.

## 기존 기록은 자동 이전되지 않습니다

마이그레이션 완료 후 이전 Copilot 기록이 새로운 Copilot Chat 경험으로 옮겨지는 것은 아닙니다. 대신 대화 창 오른쪽 위 **더 보기(…) → View Copilot history**에서 기존 기록에 접근할 수 있습니다. 채널 스레드 요약의 더 보기 메뉴에도 기록 접근 경로가 제공됩니다.

따라서 새 화면에 이전 기록이 보이지 않는다고 바로 삭제되었다고 판단하지 말고, 지원팀이 기존 기록 경로를 안내할 수 있도록 준비해야 합니다.

## 회의 음성 처리 중지의 의미

새 회의 중 제어가 활성화되면 Teams는 음성 처리를 중지합니다. 여기에는 전사와 녹화가 포함되며, Copilot은 그 시간 동안 발언된 내용을 사용하거나 참조하지 않습니다.

Facilitator가 실행 중이면 함께 꺼집니다. 제어가 유지되는 동안 사용자는 녹화, 전사, Facilitator를 다시 시작할 수 없습니다. 관련 공지인 [MC1319216](https://mc.merill.net/message/MC1319216)도 확인할 필요가 있습니다.

## 단계별 일정 구분

| 범위 | 원문에 제시된 배포 계획 |
|---|---|
| 채팅·채널·회의 후 및 통화 요약 | 2025년 10월 초 Public Preview 시작, 11월 중순 GA 시작 |
| 회의 중·통화 중 | 2025년 12월 초 Public Preview 시작, 2026년 1월 중순 GA 시작 및 3월 초 완료 |
| 회의 중 음성 제어 | 2026년 9월 시작 및 같은 달 완료 예상 |

이는 9월 업데이트 공지의 일정 설명이며, 현재 모든 테넌트의 배포 완료를 별도로 확인한 것은 아닙니다.

## 관리자는 라이선스와 앱 허용을 함께 확인하세요

라이선스만 할당해도 항상 진입점이 나타나는 것은 아닙니다. 관리자는 **Microsoft 365 Copilot 앱을 테넌트에서 허용**하고 Teams 앱 권한·앱 설정 정책이 대상 사용자에게 적절한지 확인해야 합니다.

회의에서 Copilot이 보이지 않는 문제를 조사할 때는 라이선스와 앱 활성화를 함께 점검하세요. 한국 조직의 교육에서는 새 진입점, 기존 기록 경로, 음성 처리 중지의 영향을 묶어서 설명하는 것이 효과적입니다.

> **출처**: [MC1156360 — Microsoft 365 Copilot: Copilot Chat for Teams Chats, Channels, Calling, and Meetings](https://mc.merill.net/message/MC1156360). [Microsoft 365 Roadmap 501107](https://www.microsoft.com/microsoft-365/roadmap?searchterms=501107). **실제 출시 일정·기능은 변경될 수 있습니다**.
