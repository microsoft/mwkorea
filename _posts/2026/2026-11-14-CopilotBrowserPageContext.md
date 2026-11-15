---
title: "열어 둔 여러 탭을 한 대화에서: Copilot 데스크톱 브라우저의 페이지 컨텍스트"
date: 2026-11-14T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotDesktop
  - Browser
  - PageContext
  - Governance
excerpt: "Copilot 데스크톱 앱의 내장 브라우저에서 열린 탭 내용을 질문과 요약의 맥락으로 활용할 수 있게 됩니다. 현재 대화로 제한되는 범위와 내장 브라우저 활성화 조건을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 열어 둔 여러 탭을 한 대화에서: Copilot 데스크톱 브라우저의 페이지 컨텍스트

자료를 비교할 때는 여러 웹페이지를 오가며 필요한 내용을 복사하는 일이 많습니다. Copilot이 지금 열어 둔 페이지를 맥락으로 사용할 수 있다면 질문과 자료 확인을 한 흐름으로 이어갈 수 있습니다.

MC1552386은 **Copilot 데스크톱 앱의 내장 브라우저**에서 열린 웹페이지 탭 내용을 답변과 요약의 컨텍스트로 활용하는 기능을 안내합니다. 모든 브라우저나 모든 Copilot 환경에 적용되는 기능으로 발표된 것은 아닙니다.

---

## 한 탭뿐 아니라 여러 탭에 질문하기

내장 브라우저가 활성화되어 있으면 사용자는 단일 탭 또는 여러 탭의 내용에 관해 질문하거나 요약을 요청할 수 있습니다.

![Copilot 데스크톱 앱 내장 브라우저의 열린 탭과 페이지 컨텍스트 안내](/mwkorea/assets/images/2026-11-14-CopilotBrowserPageContext/image1.png)

실무에서는 여러 참고 자료의 공통점과 차이를 묻는 흐름을 생각해 볼 수 있습니다. 다만 원문은 특정 사이트의 호환성이나 모든 페이지에 대한 완전한 이해를 보장하지 않습니다.

![열린 웹페이지 내용을 바탕으로 질문하는 Copilot 사용 예시](/mwkorea/assets/images/2026-11-14-CopilotBrowserPageContext/image2.png)

## 컨텍스트의 범위는 현재 대화

**페이지 컨텍스트는 현재 대화로 제한**됩니다. 이를 다른 대화에서도 자동으로 유지되는 장기 기억이나 다른 브라우저의 탭까지 읽는 기능으로 이해하면 안 됩니다.

원문이 설명하는 적용 조건은 다음과 같습니다.

| 항목 | 범위 |
|---|---|
| 앱 | Microsoft Copilot 데스크톱 앱 |
| 페이지 | 앱 내장 브라우저에서 열린 웹페이지 탭 |
| 활용 | 한 탭 또는 여러 탭에 대한 질문과 요약 |
| 대화 범위 | 현재 대화 |
| 내장 브라우저 비활성화 | 기능이 동작하지 않으며 영향 없음 |

현재 대화로 범위가 제한된다는 설명만으로 데이터 보존 기간이나 모든 규정 준수 조건을 단정할 수는 없습니다.

## 제공 일정과 관리자 준비

전 세계 일반 공급 배포는 **2026년 11월 중순 시작, 11월 말 완료 예상**입니다. 공지 시점에는 순차 배포 일정이므로 사용자별 사용 가능 여부가 다를 수 있습니다.

필수 조치는 없지만 관리자는 내장 브라우저가 조직에 활성화되어 있는지, 앱 내 브라우징과 페이지 컨텍스트 관련 거버넌스 설정이 적절한지 확인하는 것이 권장됩니다. 파일럿 사용자로 예상 동작을 점검하고 지원 부서에 대화 범위를 안내하는 준비도 도움이 됩니다.

## 마무리

이번 기능은 열린 웹 자료를 Copilot 대화에 연결하는 변화입니다. 도입 시에는 편의성만큼 **어떤 앱의 어떤 탭이 현재 대화에 사용되는지**를 사용자에게 명확하게 알려 주는 것이 중요합니다.

> **출처**: MC1552386, [Microsoft 365 Copilot: Page context for open tabs in the Copilot desktop app built-in browser](https://mc.merill.net/message/MC1552386).
> **Microsoft 365 Roadmap**: [공식 로드맵](https://www.microsoft.com/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 제시되지 않았습니다.
> 실제 출시 일정·기능은 변경될 수 있습니다.
