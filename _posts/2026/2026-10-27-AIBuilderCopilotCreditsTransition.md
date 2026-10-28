---
title: "AI Builder 크레딧 종료, 11월 1일에 모두 멈추는 건 아닙니다: Copilot Credits 전환 가이드"
date: 2026-10-27T00:00:00 KST
categories:
  - Copilot
tags:
  - AIBuilder
  - CopilotCredits
  - CopilotStudio
  - PowerAutomate
  - PowerApps
  - Licensing
excerpt: "AI Builder는 유지되지만 사용량 과금은 Copilot Credits 중심으로 전환됩니다. 2026년 11월 1일의 의미와 계약별 기존 크레딧 유효기간, 업무 중단을 막기 위한 관리자 확인 절차를 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# AI Builder 크레딧 종료, 11월 1일에 모두 멈추는 건 아닙니다: Copilot Credits 전환 가이드

Power Apps와 Power Automate에서 AI Builder를 사용하고 있다면 기능보다 먼저 확인할 것이 있습니다. 바로 **어떤 크레딧으로 업무가 실행되고 있으며, 그 권리가 언제 만료되는가**입니다.

Message Center **MC1526652**는 AI Builder credits를 종료하고 Copilot Credits로 전환하는 정책을 설명합니다. **AI Builder 기능 자체가 종료되는 것은 아닙니다.** AI Builder와 Copilot Studio가 공통 크레딧 기반의 라이선스 체계로 모이는 변화입니다.

특히 원문은 **2026년 11월 1일이 기존 크레딧의 일괄 소멸일은 아니다**라고 명시합니다. 전환 기한은 해당 계약의 만료일과 크레딧 소진 시점에 따라 달라집니다.

---

## 날짜별로 무엇이 달라지나요?

| 날짜 | 변경 사항 |
|---|---|
| 2025년 11월 1일 | 신규 고객 대상 AI Builder 용량 추가 기능 판매 종료 |
| 2026년 11월 1일 | AI Builder 용량 추가 기능의 수명 종료. 유효한 추가 기능 계약의 크레딧은 해당 계약 만료까지 사용 가능 |
| 2026년 11월 1일 | 이후 신규 구매·갱신되는 적격 Power Platform 및 Dynamics 365 라이선스에 기본 포함 AI Builder 크레딧을 더 이상 제공하지 않음 |
| 기존 계약 기간 종료 | 기준일 전에 구매·갱신한 적격 라이선스의 기본 포함 크레딧은 해당 계약 기간 종료까지 유지 |

원문은 Worldwide 및 GCC의 GA 배포 기간을 **2026년 11월 초**로 안내합니다. 이는 정책 적용 안내이며, 모든 조직의 남은 크레딧이 같은 날 사라진다는 뜻은 아닙니다.

## 크레딧이 부족하면 실제 업무는 어떻게 되나요?

Power Apps와 Power Automate의 AI Builder 기능은 사용 가능한 **AI Builder credits를 먼저 소비**합니다. 해당 크레딧이 없거나 소진되면 사용 가능한 **Copilot Credits로 자동 전환**됩니다.

두 종류 모두 사용할 수 없으면 영향을 받는 AI Builder 실행이 차단됩니다. 문서 처리 등 AI 단계에 의존하는 앱·흐름·업무 프로세스가 중단될 수 있다는 뜻입니다.

반드시 구분해야 할 사항도 있습니다.

- AI Builder credits가 Copilot Credits로 **자동 환산되지는 않습니다**.
- 기능별 소비율이 달라 **단일 환산 비율이 없습니다**.
- Copilot Studio 안의 AI Builder 기능은 이미 Copilot Credits를 소비합니다.
- 이번 변경의 초점은 기능 제거가 아니라 **라이선스와 용량 확보**입니다.

따라서 기존 AI Builder 크레딧 사용량과 같은 숫자의 Copilot Credits를 구매하면 충분하다고 가정해서는 안 됩니다.

## 관리자 실행 순서

### 1. 계약과 자동 갱신을 확인합니다

AI Builder 용량 추가 기능과 기본 포함 크레딧을 제공하는 라이선스의 만료일을 확인합니다. 원문은 용량 추가 기능을 사용하는 조직에 **2026년 11월 1일 전 관리자 조치**를 요구하며, 기존 사용 권리가 만료되기 전에 대체 용량을 준비하도록 안내합니다.

추가 기능의 자동 갱신은 Microsoft 365 관리 센터에서 끄거나, 파트너에게 Partner Center에서 처리하도록 요청하는 절차가 제시되어 있습니다. 실제 변경 전에는 구매 담당자·파트너와 계약 조건을 확인하세요.

### 2. 환경별 소비 보고서를 내려받습니다

[Power Platform 관리 센터](https://admin.powerplatform.microsoft.com/)에서 다음 경로를 사용합니다.

**Licensing → Capacity add-ons → Download reports → + New → AI Builder**

보고서는 선택한 기준일 이전 **30일간**의 크레딧 소비를 날짜·사용자·환경별로 확인하는 데 활용합니다. 단순 잔액뿐 아니라 어느 환경의 업무가 용량을 소비하는지 파악하는 단계입니다.

### 3. 영향을 받는 앱과 흐름을 찾습니다

[Power Automate 포털](https://make.powerautomate.com/)에서 환경을 선택한 후 **Automation Center → Monitor → AI Builder activity**로 이동합니다.

메이커는 자신이 접근할 수 있는 모델에 대한 본인 활동을 확인할 수 있습니다. **System Administrator 또는 System Customizer** 역할 사용자는 환경 전체 활동을 확인할 수 있으며, Dataverse의 **AI Event 테이블**에서도 활동 데이터를 확인할 수 있습니다.

### 4. 기능별 소비율로 대체 용량을 산정합니다

[AI Builder capability rate table](https://learn.microsoft.com/en-us/ai-builder/administer-licensing#aibuildercapabilityrate-table)을 기준으로 Copilot Credits 필요량을 추정합니다. 기존 권리가 만료되기 전에 구매하고, 영향을 받는 환경에서 충분한 용량을 사용할 수 있도록 준비해야 합니다.

### 5. 메이커와 지원팀에 안내합니다

크레딧 부족으로 중단되면 영향이 큰 앱과 흐름을 우선 식별합니다. 사내 가이드의 크레딧 종류·소비율·용량 확인 절차를 갱신하고, 지원팀이 라이선스 부족과 모델 오류를 구분할 수 있도록 준비하세요.

## 한국 조직에서 특히 주의할 점

여러 부서가 별도 환경과 계약으로 Power Platform을 운영한다면 전환 기한도 하나가 아닐 수 있습니다. 계약 만료일, 환경별 사용량, 중요 업무, 대체 용량 확보 여부를 한 표로 관리하는 것이 좋습니다. 이는 원문 절차를 실제 운영에 적용하기 위한 제안입니다.

이번 글은 공지에 기재된 정책을 정리한 것입니다. 실제 구매 조건과 최신 소비율은 계약 담당자 및 공식 문서에서 확인해야 하며, 원문 시점의 설명을 이후의 최신 계약 조건으로 단정해서는 안 됩니다.

## 참고 문서와 마무리

- [End of AI Builder credits](https://learn.microsoft.com/en-us/ai-builder/endofaibcredits)
- [AI Builder licensing overview](https://learn.microsoft.com/en-us/ai-builder/administer-licensing)
- [AI Builder consumption report](https://learn.microsoft.com/en-us/ai-builder/administer-consumption-report)
- [Monitor AI Builder activity](https://learn.microsoft.com/en-us/ai-builder/activity-monitoring)

이번 전환의 핵심은 “11월 1일에 모두 중단된다”가 아니라 **계약 종료 또는 소진 전에 충분한 Copilot Credits를 준비한다**는 것입니다. 기능은 유지되지만, 용량 준비는 관리자의 별도 조치가 필요합니다.

> **출처**: [MC1526652 — AI Builder credits retirement: Prepare to use Copilot Credits](https://mc.merill.net/message/MC1526652)  
> **Microsoft 365 Roadmap**: [공식 로드맵](https://www.microsoft.com/en-us/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 제공되지 않았습니다.  
> 실제 출시 일정·기능은 변경될 수 있습니다.
