---
title: "Copilot Studio × M365 Copilot, 이제 에이전트 자동화가 무료라고요?"
date: 2026-04-21T00:00:00 KST
categories:
  - CopilotStudio
tags:
  - CopilotStudio
  - M365Copilot
  - Agent
  - Automation
  - Trigger
  - 과금정책
excerpt: "M365 Copilot 라이선스가 있으면 트리거 기반 자동화 에이전트도 추가 과금 없이 이용할 수 있습니다. 무료 조건과 주의사항을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio × M365 Copilot, 이제 에이전트 자동화가 무료라고요?

## 들어가며

Copilot Studio로 업무 자동화 에이전트를 만들고 싶었지만, "크레딧 과금이 부담돼서" 망설이셨던 분들께 반가운 소식입니다.

2025년 12월, Microsoft는 Copilot Studio의 과금 정책을 조용히 변경했습니다. 핵심은 단 한 줄입니다.

> **Microsoft 365 Copilot 라이선스가 있으면, 개인 업무 자동화 에이전트는 추가 과금 없이 이용할 수 있습니다.**

이번 포스팅에서는 무엇이 바뀌었고, 어떤 조건에서 무료이며, 주의할 점은 무엇인지 정리해 드립니다.

---

## 뭐가 바뀌었나요?

### 기존 정책

Copilot Studio 에이전트는 크게 세 가지로 분류되었습니다.

| 구분 | 과금 여부 |
|------|-----------|
| Non-M365 Copilot 사용자 | 과금 |
| M365 Copilot 사용자 (대화형) | 무료 |
| 트리거 기반 자동화 에이전트 | 과금 |

즉, 메일 수신 → 자동 요약처럼 자동으로 돌아가는 에이전트는 **무조건 크레딧이 소모**되었습니다.

### 변경된 정책

이제는 **트리거 기반 자동화 에이전트도 조건을 충족하면 무료**입니다.

Microsoft 공식 문서의 표현을 빌리면:

> *"Employee-facing usage scenarios (B2E) of Copilot Studio agents are included in the Microsoft 365 Copilot USL when the user is licensed with Microsoft 365 Copilot, and the agent operates using the authenticated user's identity."*
>
> — [Microsoft Learn: Requirements Messages Management](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management)

---

## 무료의 조건, 두 가지만 기억하세요

### ✅ 조건 1: 라이선스 사용자 본인의 인증으로 실행될 것

에이전트의 트리거와 액션이 M365 Copilot 라이선스가 할당된 사용자 계정의 인증으로 호출되어야 합니다.

**무료 예시:**
- 내 Outlook 메일함에 새 메일이 도착하면 → 자동 요약 에이전트 실행
- 내 계정으로 로그인한 상태에서 에이전트에게 질문

**과금 예시:**
- 서비스 계정이나 시스템 연결 기반으로 실행되는 트리거
- 사용자 인증 없이 자동 실행되는 에이전트

💡 쉽게 말하면: **"내가 로그인해서 쓰면 무료, 시스템이 알아서 돌리면 과금"**

### ✅ 조건 2: Fair Usage (공정 사용) 범위 내일 것

무료이긴 하지만 무제한은 아닙니다. Microsoft는 **"Fair Usage Limit"**이라는 개념을 적용합니다.

**Fair Usage에 해당하는 경우:**
- 🏢 B2E (Business to Employee): 사내 직원 대상 서비스
- 👤 개인 업무 자동화: 내 메일 요약, 내 데이터 처리, 내 일정 관리 등

**Fair Usage를 벗어날 수 있는 경우:**
- 라이선스 1개로 조직 전체가 AI를 이용하도록 설계
- 예: A씨의 메일함을 공용 창구로 만들어 라이선스 없는 직원들이 메일로 질문 → AI 답변 수신

이런 경우 Microsoft가 어뷰징으로 판단하여 **과금 또는 사용 제한**을 적용할 수 있습니다.

---

## 채널은 상관없나요?

네, Copilot Studio에서 제공하는 **모든 채널에서 무료 적용이 가능**합니다.

단, 한 가지 전제가 있습니다: 에이전트 인증 설정을 수동(Manual)으로 구성하여, 사용자가 **Entra ID(구 Azure AD)로 인증**을 받아야 합니다.

웹사이트에 에이전트를 붙여도, Teams에서 사용해도, **로그인만 하면 무료**입니다.

### ⚠️ SSO 지원 채널은 제한적

모든 채널에서 SSO(Single Sign-On)가 되는 것은 아닙니다.

| 채널 | SSO 지원 |
|------|----------|
| Microsoft Teams | ✅ 지원 |
| Custom Website | ✅ 지원 |
| SharePoint | ✅ 지원 |
| Demo Website | ❌ 미지원 |
| Facebook | ❌ 미지원 |
| Azure Bot Service 채널 | ❌ 미지원 |

> 참고: [Microsoft Learn: Configure SSO](https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-sso?tabs=webApp)

SSO가 안 되는 채널에서는 사용자가 액세스 토큰을 직접 입력해야 하므로, 실무적으로는 **Teams 또는 웹사이트 중심으로 활용**하시는 것이 현실적입니다.

---

## 전사 포털에 붙이려면? 쓰로틀링을 꼭 확인하세요

"그럼 사내 포털 메인에 에이전트를 붙이면 되겠네!" 라고 생각하실 수 있지만, **쓰로틀링 제한**을 반드시 고려해야 합니다.

| 제한 항목 | 한도 |
|-----------|------|
| 분당 요청 수 | 100회 |
| 시간당 요청 수 | 2,000회 |

이 제한은 **환경(Environment) 단위**로 적용되기 때문에, 중견 이상 기업에서 수백~수천 명이 동시에 접속하는 전사 포털에는 병목이 발생할 수 있습니다.

> 참고: [Microsoft Learn: Requirements Quotas](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-quotas)

---

## 한눈에 정리

| 시나리오 | 과금 여부 |
|----------|-----------|
| 개인 업무 자동화 (메일 요약, 데이터 처리 등) | ✅ 무료 |
| 라이선스 사용자가 로그인하여 에이전트 사용 | ✅ 무료 |
| 트리거 기반이지만 본인 계정 인증 | ✅ 무료 |
| 시스템/서비스 계정 기반 자동 실행 | ❌ 과금 |
| 라이선스 우회 목적의 전사 서비스 | ❌ 과금 가능 |

---

## 마무리

이번 정책 변경의 의미는 명확합니다.

> **"M365 Copilot 라이선스만 있으면, 나만의 업무 자동화 에이전트를 부담 없이 만들고 쓸 수 있다."**

그동안 크레딧 걱정에 Copilot Studio를 망설이셨다면, 지금이 시작할 타이밍입니다. 내 메일을 자동으로 정리하고, 반복 업무를 에이전트에게 맡기고, 더 중요한 일에 집중하세요.

궁금한 점이 있으시면 언제든 문의해 주세요! 🚀
