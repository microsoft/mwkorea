---
title: "Cowork·Code·Autopilot이 보여도 자동 과금은 아닙니다: Copilot UBB 새 접근 정책"
date: 2026-11-10T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Cowork
  - Autopilot
  - UsageBasedBilling
  - CopilotCredits
  - Governance
excerpt: "Cowork·Code·Autopilot 같은 사용량 기반 기능의 기본 노출 일정이 2027년 1월 말로 조정됐습니다. 새 접근 요청 설정과 사내 안내 URL을 준비할 수 있으며, 메뉴가 보이더라도 지출 정책과 Copilot Credits 없이는 실제 사용이나 과금이 시작되지 않습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Cowork·Code·Autopilot이 보여도 자동 과금은 아닙니다: Copilot UBB 새 접근 정책

사용자가 Copilot 앱에서 Cowork나 Code 메뉴를 발견하면 “우리 회사도 사용할 수 있는 건가요?”라는 질문이 뒤따르기 쉽습니다. 앞으로는 **기능이 보이는 것, 사용 권한이 있는 것, 비용이 발생하는 것**을 나눠 설명해야 합니다.

Microsoft는 MC1546354에서 사용량 기반 과금(Usage-Based Billing, UBB) 경험의 노출 정책과 관리자 제어를 업데이트했습니다. 이전 MC1479277에 이어 고객 피드백을 반영해 일정을 연장하고, 사용자를 사내 안내로 연결할 수 있는 옵션을 추가한 내용입니다.

---

## 무엇이 기본으로 보이게 되나요?

**Microsoft 365 Copilot 라이선스가 있는 사용자**에게 Cowork, Code, Autopilot 등의 진입점이 기본 표시됩니다. 조직이 아직 해당 기능의 사용을 허용하지 않았더라도 메뉴 자체는 발견할 수 있게 되는 방향입니다.

해당 기능을 허용하는 지출 정책이 없는 사용자는 바로 기능을 실행하는 대신 조직 설정에 따라 **Request access** 또는 **Learn more** 안내를 보게 됩니다.

원문은 이 변경이 **기능을 자동으로 활성화하거나 과금을 시작하지 않는다**고 명확히 설명합니다. 실제 사용에는 적용 가능한 **spending policy와 사용 가능한 Copilot Credits가 모두 필요**합니다.

## 변경된 일정: 설정은 먼저, 사용자 노출은 나중에

| 예정 시점 | 변경 내용 |
|---|---|
| 2026년 11월 중순 | **Access requests to usage-based billing experiences** 관리자 설정 제공 |
| 2026년 12월 중순 | 사내 안내용 custom URL 옵션 추가 |
| 2027년 1월 말 | 새 기본 노출 동작과 관리자 설정 적용, 기존 설정 폐지 |
| 2027년 2월 말 | deferred release 고객에게 적용 |

기존 **Allow users to discover and use AI experiences enabled by usage-based billing** 설정은 2027년 1월 말 폐지 전까지 계속 적용됩니다. 기존 설정과 새 설정을 같은 시점부터 동작하는 것으로 오해하지 않는 것이 중요합니다.

## 접근 요청과 사내 안내 URL을 제어합니다

새 설정에서는 **누가 사용 권한을 요청할 수 있는지**를 정하고, 접근 요청을 막는 선택도 할 수 있습니다.

12월 중순 추가 예정인 custom URL 옵션은 **Specific users 또는 No users**를 선택한 경우 사용할 수 있습니다. 이때 **접근 요청을 할 수 없는 사용자만** Learn more 안내 안의 **Your organization’s guidance** 링크를 보게 됩니다.

즉 사내 안내 링크는 모든 사용자에게 일괄 표시되는 공통 배너가 아닙니다. 요청 자격이 없는 사용자에게 조직의 방침과 대체 절차를 설명하는 용도입니다.

![Cowork의 사내 안내 링크를 보여 주는 원문 UI 예시](/mwkorea/assets/images/2026-11-10-CopilotUsageBasedBillingDiscovery/image1.png)

![Code의 사내 안내 링크를 보여 주는 원문 UI 예시](/mwkorea/assets/images/2026-11-10-CopilotUsageBasedBillingDiscovery/image2.jpg)

위 이미지는 원문에 포함된 예시이며, 실제 UI는 변경될 수 있습니다.

## 관리자 준비 순서

1. 11월 중순 이후 **Microsoft 365 admin center > Copilot > Settings > Access requests to usage-based billing experiences**를 확인합니다.
2. 접근 요청을 허용할 사용자 범위를 결정합니다.
3. 요청할 수 없는 사용자에게 제공할 사내 정책·지원 안내를 준비합니다.
4. 12월 중순 custom URL 옵션이 제공되면 안내 페이지를 연결합니다.
5. 실제 사용 범위가 조직의 의도와 일치하도록 지출 정책을 점검합니다.

사용자 안내에는 “메뉴가 보여도 사용 승인이나 예산 배정이 끝난 것은 아니다”라는 설명을 넣는 편이 좋습니다. 사내 안내 페이지에는 허용 대상, 문의 창구, 조직에서 정한 절차를 명시할 수 있습니다. 이러한 안내 내용은 조직이 설계할 사항이지 Microsoft가 이번 공지로 정한 공통 승인 절차는 아닙니다.

## 문서의 업데이트 시점도 확인하세요

원문이 연결한 [Access requests to usage-based billing experiences](https://learn.microsoft.com/copilot/implement/request-access-usage-based-billing-experiences) 문서는 custom URL 사용 지침을 반영하도록 **12월 중순 업데이트 예정**이라고 설명되어 있습니다. 공지 시점의 예정 기능과 실제 문서·관리 화면에 반영된 기능을 구분해서 확인해야 합니다.

## 마무리

이번 변화의 중심은 자동 과금이 아니라 **유료 경험의 발견 가능성과 접근 요청 관리**입니다. 2027년 1월 말 적용 전에 요청 대상과 사내 안내를 정리하고, 실제 사용 통제는 지출 정책과 크레딧 조건으로 별도 관리하세요.

> 출처: [MC1546354 — Discover usage-based billing (UBB) experiences like Cowork, Code, and Autopilot](https://mc.merill.net/message/MC1546354)
>
> 참고: [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap). 이 공개 공지에는 개별 Roadmap ID가 제시되어 있지 않습니다.
>
> 일정과 기능은 원문 공지 시점 기준이며, 실제 출시 일정·기능은 변경될 수 있습니다.
