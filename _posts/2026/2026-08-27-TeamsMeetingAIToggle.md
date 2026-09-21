---
title: "Teams 회의 중 Meeting AI를 켜고 끄는 토글이 추가됩니다"
date: 2026-08-27T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftTeams
  - MeetingAI
  - Copilot
  - Facilitator
  - Transcription
  - Compliance
excerpt: "라이선스를 갖춘 Teams 회의 주최자와 발표자가 회의 도중 Copilot과 Facilitator를 포함한 Meeting AI를 켜거나 끌 수 있게 됩니다. 다만 전사가 함께 사용되면 Meeting AI와 전사가 서로 연동되므로, AI를 쓰지 않아야 하는 회의에서는 둘 다 꺼진 상태를 유지해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Teams 회의 중 Meeting AI를 켜고 끄는 토글이 추가됩니다

회의를 시작하기 전에 정한 AI 사용 여부를 회의가 끝날 때까지 그대로 유지할 필요가 없어집니다. 라이선스를 갖춘 주최자와 발표자는 대화의 성격에 맞춰 회의 도중 Meeting AI를 켜거나 끌 수 있습니다.

하지만 이 토글을 단순한 Copilot 스위치로 이해하면 안 됩니다. Meeting AI와 전사(transcription), 녹화·요약 산출물의 관계가 함께 움직이므로, 민감한 회의에서 AI 접근을 막으려면 전사 동작까지 정확히 알아야 합니다.

---

## 회의 도구 모음에 새 제어가 나타납니다

예약된 Teams 회의의 도구 모음에 Meeting AI 제어가 표시됩니다. 대상은 정책과 회의 옵션에서 Meeting AI(Copilot 또는 Facilitator)가 허용된 Microsoft 365 테넌트이며, 실제로 토글을 조작할 수 있는 사람은 **라이선스를 갖춘 회의 주최자와 발표자**입니다.

![Copilot과 Facilitator가 꺼진 Meeting AI 토글](/mwkorea/assets/images/2026-08-27-TeamsMeetingAIToggle/image1.png)

![Copilot과 Facilitator가 켜진 Meeting AI 토글](/mwkorea/assets/images/2026-08-27-TeamsMeetingAIToggle/image2.png)

정책에서 Meeting AI를 허용하지 않았다면 토글 자체가 나타나지 않습니다. 참가자에게는 AI가 현재 활성 상태인지 보여 주는 상태 표시가 제공됩니다. 지원 플랫폼은 Teams 데스크톱, 웹, 모바일입니다.

## 껐을 때와 켰을 때 달라지는 것

Meeting AI를 끄면 Copilot과 Facilitator의 응답, Notes가 더 이상 새로 생성되지 않습니다. 끄기 전에 만들어진 산출물은 삭제되지 않고 계속 사용할 수 있으며 기존 보존 정책의 적용을 받습니다.

AI를 전사 없이 사용하던 경우에는 끄는 시점부터 음성-텍스트 데이터 처리가 중단되고 Recap이 생성되지 않습니다. 반면 **전사와 함께 사용하는 Meeting AI는 서로 연동**됩니다.

- Meeting AI를 켜면 전사가 자동으로 켜지고 Recap이 생성됩니다.
- 전사를 시작하면 Meeting AI와 Recap도 자동으로 활성화됩니다.
- Meeting AI 사용을 확실히 막아야 한다면 전사와 Meeting AI가 모두 꺼져 있어야 합니다.

즉, 민감한 구간에서 AI 토글만 끈 뒤 누군가 전사를 다시 시작하면 Meeting AI와 Recap도 다시 활성화될 수 있습니다. 이 동작은 사용자 교육에서 가장 먼저 강조할 내용입니다.

## 기존 정책과 회의 옵션은 유지됩니다

이번 업데이트는 회의 중 실시간 제어를 추가하지만 다음 체계를 바꾸지는 않습니다.

- 회의 전에 구성한 Meeting options
- 녹화, 전사, 민감도 레이블 동작
- 보존 및 규정 준수 정책
- Copilot과 Meeting AI의 라이선스 요구 사항

새 토글은 기존 정책을 우회하지 않습니다. 테넌트 정책이 Meeting AI를 차단하면 토글이 나타나지 않으며, 허용된 환경 안에서 라이선스가 있는 역할만 회의 중 상태를 바꿀 수 있습니다.

## 출시 일정

| 채널 | 시작 | 완료 예상 |
|---|---|---|
| Targeted Release | 2026년 9월 중순 | 2026년 9월 말 |
| General Availability, Worldwide | 2026년 9월 중순 | 2026년 9월 말 |

8월 26일 갱신에서 기존 8월 계획이 9월로 변경됐습니다. 배포 전 별도 관리자 작업은 요구되지 않습니다.

## 관리자와 회의 운영자를 위한 체크리스트

1. **누가 토글을 조작하는지 안내합니다.** 라이선스를 갖춘 주최자와 발표자가 대상입니다.
2. **전사 의존성을 교육합니다.** 전사를 시작하면 Meeting AI와 Recap도 활성화된다는 문구를 교육 자료에 그대로 반영합니다.
3. **민감 회의 절차를 수정합니다.** AI 금지가 필요한 회의는 전사와 Meeting AI를 모두 끈 상태로 유지하도록 체크리스트를 만듭니다.
4. **기존 산출물의 보존을 설명합니다.** AI를 끄더라도 이미 생성된 내용은 남고 보존 정책을 따릅니다.
5. **헬프데스크 시나리오를 준비합니다.** 토글이 보이지 않는 경우 정책, 회의 옵션, 역할, 라이선스를 순서대로 확인합니다.
6. **상태 표시를 확인하게 합니다.** 참가자는 AI 상태 표시로 현재 활성 여부를 확인해야 합니다.

## 정리

회의 중 AI를 유연하게 제어할 수 있다는 점은 실무에 유용합니다. 일반 논의에서는 요약과 메모를 활용하다가 민감한 안건으로 넘어갈 때 AI를 중단하는 운영이 가능해집니다.

다만 제어의 실효성은 전사와의 결합 관계를 이해할 때 확보됩니다. “AI를 껐다”가 아니라 **Meeting AI와 전사가 모두 꺼져 있는지**를 확인하는 습관이 필요합니다.

---

> **출처**
>
> - 원문 ID: **MC1319216** — *Microsoft Teams: In‑meeting toggle to turn Meeting AI on or off*
> - 메시지 센터: [https://mc.merill.net/message/MC1319216](https://mc.merill.net/message/MC1319216)
> - Microsoft 365 로드맵: [https://www.microsoft.com/microsoft-365/roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
