---
title: "Outlook의 Copilot, 에이전트로 진화하다: 받은편지함과 캘린더를 알아서 챙겨주는 새로운 경험"
date: 2026-04-30T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Outlook
  - Copilot
  - Agent
  - Frontier
  - Email
  - Calendar
excerpt: "Outlook의 Copilot이 단순한 작성 도우미를 넘어, 받은편지함을 분류·후속 처리하고 캘린더 충돌까지 알아서 해결하는 에이전트 경험으로 진화했습니다. 2026년 4월 27일부터 Frontier 프로그램을 통해 순차 제공됩니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 김유연
---

# Outlook의 Copilot, 에이전트로 진화하다: 받은편지함과 캘린더를 알아서 챙겨주는 새로운 경험

Microsoft는 2026년 4월 27일, Outlook 블로그를 통해 [Copilot in Outlook: New agentic experiences for email and calendar](https://techcommunity.microsoft.com/blog/outlook/copilot-in-outlook-new-agentic-experiences-for-email-and-calendar/4514601)를 공개했습니다.

지금까지 Outlook의 Copilot은 "지금 눈앞에 있는 일"을 도와주는 도구였습니다. 메일 한 통을 작성하고, 긴 스레드를 요약하고, 회의 시간을 잡아주는 식이었죠. 유용했지만, 사실 업무에서 가장 어려운 부분은 그 다음입니다. **놓친 후속 답장, 응답이 필요한 메일, 하루가 시작되기도 전에 쌓이는 일정 변경** — 이런 "주변 업무"가 진짜 시간을 잡아먹습니다.

이번 업데이트로 Outlook의 Copilot은 **에이전트(agentic)** 로 동작합니다. 메일을 분류하고, 일정 충돌을 재조정하고, 묻기 전에 중요한 일을 먼저 꺼내 줍니다. 사용자는 모든 작업을 직접 하지 않고, Copilot이 해 둔 일을 검토하고 필요할 때만 개입하면 됩니다.

![Outlook Copilot agentic experiences](/mwkorea/assets/images/2026-04-30-CopilotOutlookAgentic/image1.png)

---

## 한눈에 보는 핵심 변화

- **받은편지함 자동 운영**: 우선순위 분류, 후속 답장 초안, 인박스 규칙 생성까지 Copilot이 단계별로 처리
- **캘린더 위임 관리**: 1:1 충돌 자동 재조정, 회의실 재예약, 집중 시간 보호를 Copilot이 지속적으로 수행
- **시간의 우선순위 정렬**: 다음 주 일정을 검토해 거절·위임·비동기 전환을 추천, 중요 회의 사전 준비까지 지원
- **제공 방식**: 2026년 4월 27일부터 [Microsoft 365 Copilot Frontier 프로그램](https://www.microsoft.com/en-us/microsoft-365-copilot/frontier-program)을 통해 순차 제공 (캘린더 기능은 Outlook for Windows / Web 우선)

---

## 1. 받은편지함을 Copilot에게 맡기기 (Manage your inbox with Copilot)

받은편지함을 운영한다는 건 단순히 읽고 답장하는 일이 아닙니다. **계속 흐름을 유지하는 작업**이죠. 이번 업데이트로 Copilot in Outlook이 그 흐름 자체를 가져갑니다.

- 메일의 **우선순위를 분류**하고
- **응답이 필요한 메일**을 꺼내 보여주고
- **후속 답장 초안**을 자동으로 작성하고
- 받은편지함을 깔끔하게 유지할 **규칙(rule)** 까지 만들어 줍니다.

사용자는 원하는 것을 말로 지시하면 되고, Copilot은 단계별로 무엇을 하고 있는지 보여 주기 때문에 언제든 검토하거나 수정하거나 직접 개입할 수 있습니다.

<figure>
  <div style="position: relative; width: 100%; height: 0; padding-bottom: 56.34%; overflow: hidden;">
    <iframe src="https://medius.microsoft.com/Embed/video-nc/943a12a7-fa20-43f8-951d-eabce33531e5" title="Scenario 1 - Email" allowfullscreen="allowfullscreen" allow="fullscreen; picture-in-picture" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" sandbox="allow-scripts allow-same-origin allow-forms"></iframe>
  </div>
  <figcaption><em>데모 영상: Copilot이 받은편지함을 분류하고 후속 답장을 작성하는 흐름 (출처: Microsoft Outlook Blog)</em></figcaption>
</figure>

### 바로 써볼 수 있는 프롬프트

- **후속 답장 챙기기**
  > 24시간 동안 답장이 없는 사람들을 찾아서, 가장 중요한 건부터 우선순위를 정한 뒤 정중한 후속 메일 초안을 작성해 줘.
- **복잡한 메일 작성**
  > 지난 한 주간 [프로젝트명] 관련 최신 업데이트를 모아서, 기밀 / 높은 중요도로 매니저에게 보낼 업데이트 메일 초안을 작성해 줘.
- **중요한 메일 놓치지 않기**
  > 매니저로부터 새로 도착하는 메일 중 내가 To: 라인에 있는 것에는 자동으로 "High Priority" 카테고리를 부여하는 인박스 규칙을 만들어 줘.
- **휴가 복귀 후 빠르게 따라잡기**
  > 휴가에서 막 복귀했어. 그동안 놓친 메일을 요약하고, 가장 시급한 것을 강조하고, 짧은 브리핑 메일 초안을 작성해 줘. 그리고 안전하게 보관 처리할 수 있는 메일과 오늘 가장 먼저 집중해야 할 1~2가지 작업도 제안해 줘.

> **제공 시점**: 2026년 4월 27일부터 모든 Outlook 엔드포인트(Windows / Mac / Web / Mobile)에서 Frontier 프로그램을 통해 순차 제공.

---

## 2. 캘린더 관리를 Copilot에게 위임하기 (Delegate calendar management to Copilot)

회의를 잡는 일 자체는 사실 쉬운 부분입니다. **그 뒤에 따라오는 우선순위 재조정, 충돌 해결, 사전 준비 시간 확보** 가 진짜 어려운 일이죠.

이제 Copilot in Outlook은 캘린더에서 **지속적으로 일하는** 도우미가 됩니다. 일정의 흐름을 유지하고, 자잘한 변경을 처리하며, 시간을 가장 중요한 일에 맞추도록 도와줍니다.

### 2-1. 일정을 능동적으로 모니터링하고 관리

선호 설정을 기반으로 Copilot이 캘린더를 **선제적으로 관리**합니다.

- 회의 초대에 응답
- 1:1 미팅 충돌을 자동 재조정
- 회의실 재예약
- 필요한 때 집중 시간(focus time) 자동 차단

직접 변경이 필요할 때는 채팅이나 회의 폼에서 일정을 옮기거나 취소하고, 세부 정보를 갱신하거나, 목적·청중·톤에 맞춘 **회의 안건(agenda) 초안**까지 작성해 줍니다.

<figure>
  <div style="position: relative; width: 100%; height: 0; padding-bottom: 56.34%; overflow: hidden;">
    <iframe src="https://medius.microsoft.com/Embed/video-nc/8ef5c0c8-6f42-45e0-8186-bbd59facfd75" title="Scenario 2 - Calendar Managed Events" allowfullscreen="allowfullscreen" allow="fullscreen; picture-in-picture" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" sandbox="allow-scripts allow-same-origin allow-forms"></iframe>
  </div>
  <figcaption><em>데모 영상: Copilot이 1:1 충돌을 자동 재조정하고 회의를 관리하는 흐름 (출처: Microsoft Outlook Blog)</em></figcaption>
</figure>

**프롬프트 예시**

- *Copilot이 관리하는 1:1 일정 만들기*
  > 매주 월요일 오후에 매니저와 1:1 미팅을 잡아 줘. 충돌이 생기면 자동으로 재조정해 줘.
- *내 시간 보호하기*
  > 근무 시간 외에 잡힌 대규모 회의는, 리더십 팀이 보낸 것이 아니라면 자동으로 모두 팔로우만 하도록 설정해 줘.
- *일정 조정*
  > 다음 주에 잡힌 직속 부하들과의 모든 1:1을 그 주 금요일 오후로 모두 옮겨 줘.
- *안건 초안 작성*
  > 내일 있을 제품 출시 스탠드업 회의 안건을 작성해 줘. 미해결 블로커, 담당자 배정, go/no-go 결정 위주로.

> **제공 시점**: 2026년 4월 27일부터 Outlook for Windows / Web에서 Frontier 프로그램을 통해 순차 제공.

### 2-2. 시간의 우선순위 맞추기

회사에서 내 시간이 어디로 흘러가는지 한눈에 보이지 않을 때가 많습니다. Copilot은 한 발짝 물러서서 **가장 중요한 일에 시간을 맞추도록** 도와줍니다.

- 우선순위와 과부하 구간을 시각적으로 보여주고
- 컨텍스트 스위칭이 잦은 구간을 짚어 주고
- 중요 회의 전 준비 자료를 모아 주며
- 집중 시간을 미리 보호합니다.

<figure>
  <div style="position: relative; width: 100%; height: 0; padding-bottom: 56.34%; overflow: hidden;">
    <iframe src="https://medius.microsoft.com/Embed/video-nc/cb4a1d60-d0fb-4863-be65-27c3d90da487" title="Scenario 3 - Calendar Layers" allowfullscreen="allowfullscreen" allow="fullscreen; picture-in-picture" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" sandbox="allow-scripts allow-same-origin allow-forms"></iframe>
  </div>
  <figcaption><em>데모 영상: 다음 주 일정을 검토해 우선순위에 맞게 시간을 재배치하는 흐름 (출처: Microsoft Outlook Blog)</em></figcaption>
</figure>

**프롬프트 예시**

- *내 시간 우선순위 정하기*
  > 다음 주 캘린더를 검토해서, 회의 부담은 줄이되 산출물 품질은 유지할 수 있도록 거절 / 팔로우 / 위임 / 비동기 전환할 회의를 추천해 줘.
- *회의 사전 준비*
  > 내일 [고객사명]과의 미팅을 준비해 줘. 무엇을 알아야 하고, 무엇을 물어야 하며, 어떤 리스크를 살펴야 할지 알려 줘.

> **제공 시점**: 2026년 4월 27일부터 Outlook for Windows / Web에서 Frontier 프로그램을 통해 순차 제공.

---

## 한국 고객을 위한 시사점

- **"작성 도우미"에서 "운영 에이전트"로**: 메일·일정 한 건씩 도와주던 Copilot이, 받은편지함과 캘린더라는 **업무 흐름 자체를 운영**하는 단계로 진화했습니다. 임원·관리자·영업처럼 메일과 회의가 폭주하는 직무에서 체감 효과가 가장 큽니다.
- **"검토 가능한 자동화"**: 에이전트는 무엇을 했는지 단계별로 보여 주므로, 한국 기업이 흔히 우려하는 "AI가 멋대로 보내거나 옮기는" 리스크를 낮춥니다. 사용자가 언제든 개입·수정할 수 있는 구조입니다.
- **Frontier 프로그램으로 먼저 검증**: 정식 GA 전에 [Microsoft 365 Copilot Frontier 프로그램](https://www.microsoft.com/en-us/microsoft-365-copilot/frontier-program)을 통해 선행 체험·내부 검증이 가능합니다. PoC와 사내 가이드라인(예: 자동 응답 범위, 외부 메일 처리 정책)을 미리 정비하기에 좋은 시점입니다.
- **운영 정책 정비 포인트**
  - "Copilot이 자동으로 보낼 수 있는 메일"의 범위와 승인 절차
  - 자동 인박스 규칙 / 카테고리 표준화
  - 임원 캘린더의 자동 재조정 권한 정책
  - 외부 회의/고객 회의에 대한 안건 자동 생성 가이드

---

## 시작하기 (Get started)

Outlook의 Copilot은 이제 받은편지함과 캘린더 전반의 일을 처리합니다. [Microsoft 365 Copilot Frontier 프로그램](https://www.microsoft.com/en-us/microsoft-365-copilot/frontier-program)에 참여해 새로운 에이전트 경험을 가장 먼저 사용해 보고, 함께 발전시켜 가시기 바랍니다.

> **원문**: [Copilot in Outlook: New agentic experiences for email and calendar (Microsoft Tech Community, Outlook Blog, 2026-04-27)](https://techcommunity.microsoft.com/blog/outlook/copilot-in-outlook-new-agentic-experiences-for-email-and-calendar/4514601)
