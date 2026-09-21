---
title: "Edge for Business에서 선택한 문장을 바로 다듬는 Copilot Chat Rewrite"
date: 2026-09-10T00:00:00 KST
categories:
  - Copilot
tags:
  - EdgeForBusiness
  - Microsoft365CopilotChat
  - Rewrite
  - DataLossPrevention
  - BrowserPolicy
excerpt: "Edge for Business 사용자는 편집 가능한 글을 선택한 뒤 오른쪽 클릭 메뉴에서 Copilot Chat 기반 Rewrite를 실행할 수 있습니다. 기능은 기본으로 켜지지만 DLP 정책을 따르며 관리자는 InlineComposeEnabled 정책으로 사용 가능 여부를 제어할 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Edge for Business에서 선택한 문장을 바로 다듬는 Copilot Chat Rewrite

웹 양식이나 브라우저 기반 업무 앱에서 문장을 작성하다가 표현을 다듬기 위해 다른 도구로 옮길 필요가 줄어듭니다. Edge for Business의 **Rewrite**는 편집 가능한 텍스트를 선택하고 오른쪽 클릭해 초안을 만들거나 문장을 다시 쓸 수 있는 기능입니다.

이 기능은 Microsoft 365 Copilot Chat을 기반으로 하며 Edge 안에서 직접 실행됩니다. 기본으로 제공되지만 조직의 데이터 손실 방지 정책과 브라우저 관리 정책을 그대로 따르도록 설계됐습니다.

---

## 선택하고 오른쪽 클릭하는 작성 흐름

사용자는 입력할 수 있는 영역의 텍스트를 강조 표시한 뒤 오른쪽 클릭 메뉴에서 Rewrite를 선택합니다. 별도 페이지로 이동하지 않고 현재 작성 맥락에서 문장을 새로 쓰거나 표현을 바꿀 수 있습니다.

![Edge for Business의 Rewrite 대화 상자](/mwkorea/assets/images/2026-09-10-EdgeForBusinessCopilotRewrite/image1.png)

이 기능은 사용자가 메뉴를 직접 호출할 때 작동합니다. 공지에는 문서를 자동으로 바꾸거나 사용자의 확인 없이 텍스트를 전송한다는 내용이 없습니다.

## 기본 제공과 관리자 정책

Rewrite는 Edge for Business 사용자에게 기본으로 켜집니다. 관리자는 Edge 정책인 **InlineComposeEnabled**를 사용해 기능의 제공 여부를 관리할 수 있습니다.

공지의 규정 준수 설명은 이 관리자 제어가 Microsoft Entra ID 그룹 멤버십을 통해 적용될 수 있다고 밝힙니다. 조직은 브라우저 정책 배포 구조에 맞춰 허용 대상을 나누고, 내부 작성 도구나 민감 업무 화면에서 기대하는 동작을 사전에 확인할 수 있습니다.

## DLP가 차단한 페이지에서는 작동하지 않습니다

Microsoft 365 Copilot이 데이터 손실 방지, DLP 정책 때문에 페이지 콘텐츠에 접근할 수 없다면 Rewrite도 해당 콘텐츠에서 작동하지 않습니다. 새 기능이 기존 보호 정책을 우회하는 것이 아니라 접근 가능 범위 안에서만 생성형 AI를 사용하는 구조입니다.

배포 전에는 대표적인 사내 웹 앱과 DLP 적용 페이지를 골라 메뉴 노출과 실제 동작을 확인하는 것이 좋습니다. 사용자에게는 Rewrite가 보이더라도 보호된 콘텐츠에서는 실행되지 않을 수 있다는 점을 함께 안내해야 지원 문의를 줄일 수 있습니다.

## 생성형 AI와 사용자 선택

Microsoft는 이번 변경이 고객 데이터와 상호작용하는 새로운 생성형 AI 기능이며, 사용자가 Edge의 오른쪽 클릭 메뉴로 AI 지원 작성과 바꿔쓰기를 이용하는 새 방법을 제공한다고 설명합니다. 사용자는 필요할 때만 Rewrite를 직접 호출할 수 있습니다.

따라서 내부 가이드에는 중요한 사실, 수치와 규정 문구를 사용자가 원자료와 대조해야 한다는 검토 원칙을 넣는 편이 좋습니다. 기능이 문장 품질을 돕더라도 결과의 정확성과 조직 표준 준수는 별도 확인이 필요합니다.

## 수정된 배포 일정

| 구분 | 일정 |
|---|---|
| 일반 공급, 전 세계 | 2026년 9월 말 시작, 10월 말 완료 예정 |
| 이전 안내 | 2026년 8월 말 시작 |

2026년 9월 9일에 일정이 갱신됐습니다. 필수 사전 작업은 없지만 DLP 구성, InlineComposeEnabled 정책, 사용자 교육과 내부 문서를 점검하는 것이 권장됩니다.

---

> **출처**
>
> - 원문 ID: **MC1146821** — *Rewrite with Microsoft 365 Copilot Chat coming soon to Edge for Business users*
> - 원문: [https://mc.merill.net/message/MC1146821](https://mc.merill.net/message/MC1146821)
> - Microsoft 365 Roadmap: [420335](https://www.microsoft.com/microsoft-365/roadmap?filters=&searchterms=420335)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
