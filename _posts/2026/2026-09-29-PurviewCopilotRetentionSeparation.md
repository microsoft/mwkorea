---
title: "Teams 보존 정책만 믿고 있다면? Copilot 데이터 보존 설정을 따로 확인하세요"
date: 2026-09-29T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - MicrosoftPurview
  - Teams
  - DataRetention
  - Compliance
excerpt: "기존 Teams 보존 정책이 Copilot 상호작용까지 관리하던 방식이 변경됩니다. 2026년 10월 말부터 예정된 적용에 앞서, Copilot 워크로드의 보존·삭제 정책을 명시적으로 구성해야 하는 조직과 준비 사항을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Teams 보존 정책만 믿고 있다면? Copilot 데이터 보존 설정을 따로 확인하세요

Copilot 도입에서는 데이터 접근 권한만큼 **대화 기록을 얼마나 보관하고 언제 삭제할지**도 중요합니다. 특히 과거에 설정한 Teams 보존 정책이 Copilot 상호작용까지 포함한다고 생각해 온 조직이라면, 이번 Microsoft Purview 공지를 확인해야 합니다.

Message Center **MC1481313**에 따르면, 일부 기존 Teams 보존 정책이 Copilot에도 암묵적으로 적용되던 동작이 종료됩니다. 변경 후 해당 정책은 Teams 전용으로 취급되며, Copilot 데이터에는 별도의 명시적 보존 설정이 필요합니다.

---

## 무엇이 달라지나요?

| 구분 | 변경 내용 |
|---|---|
| 기존 Teams 정책의 적용 범위 | Teams와 Copilot에 함께 영향을 주던 레거시 정책을 Teams 전용으로 취급 |
| Copilot 상호작용 | 해당 Teams 정책을 통한 보존·삭제가 더 이상 적용되지 않음 |
| Teams 콘텐츠 | 기존 보존 동작 유지 |
| 조직이 해야 할 일 | Copilot 보존이 필요하다면 해당 워크로드를 대상으로 정책 구성 |

핵심은 **Teams 정책 자체가 사라지는 것이 아니라, Copilot에 대한 암묵적 적용이 사라진다**는 점입니다. 이 공지를 모든 Copilot 기록이 즉시 삭제된다는 뜻으로 해석해서는 안 됩니다. 확인해야 할 것은 우리 조직이 의도한 보존·삭제 통제가 변경 후에도 실제로 적용되는지입니다.

## 어떤 조직이 영향을 받나요?

과거 Teams용으로 만든 Microsoft Purview 보존 정책에 의존해 Microsoft 365 Copilot 상호작용을 보관하거나 삭제하는 조직이 대상입니다. 컴플라이언스 관리자와 기록 관리 담당자는 정책 이름만 볼 것이 아니라 실제 적용 위치와 범위를 점검해야 합니다.

이미 Copilot 워크로드를 명시적으로 대상으로 관리하고 있는 경우에도, 기존 Teams 정책에 대한 의존성이 남아 있는지 함께 확인하는 편이 좋습니다. 이는 도입 점검 권고이며, 원문이 모든 조직에 새 정책 생성을 일괄 요구하는 것은 아닙니다.

## 적용 일정과 관리자 준비 사항

원문에 제시된 **Worldwide 적용 일정은 2026년 10월 말 시작, 11월 중순 완료 예상**입니다. 2026년 9월 29일 확인한 공지 기준 계획이므로, 실제 테넌트 적용 시점은 관리 센터에서 다시 확인해야 합니다.

1. 기존 Purview 보존 정책 가운데 Teams와 Copilot을 함께 관리해 온 정책을 찾습니다.
2. Copilot 상호작용에 필요한 보존 기간과 삭제 요구사항을 확인합니다.
3. Copilot 워크로드를 명시적으로 대상으로 하는 보존 정책을 구성합니다.
4. 내부 컴플라이언스 문서와 관리자 안내를 수정하고 기록 관리 담당자에게 변경을 공유합니다.

한국 기업에서는 보안팀의 정책 변경만으로 끝내기보다, 법무·기록 관리 부서가 정한 보존 요구와 실제 설정이 일치하는지 함께 검토하는 것이 중요합니다. 법적 보존 기간이나 구체적인 의무는 조직별로 다르므로 이번 제품 공지만으로 판단하지 않아야 합니다.

## 마무리

이번 변화는 Copilot 데이터 수명주기를 Teams 정책의 부수 효과에 맡기지 말고 **Copilot 자체의 관리 대상으로 명확히 설정하라**는 신호입니다. 해당 방식에 의존해 왔다면 적용 시작 전에 정책 범위를 확인하고 필요한 보존·삭제 통제를 준비하세요.

> **출처**: MC1481313 — [Microsoft Purview | DLM: Legacy Teams retention policies that cover Copilot will be treated as Teams-only](https://mc.merill.net/message/MC1481313)  
> **Microsoft 365 Roadmap**: [로드맵 확인](https://www.microsoft.com/en-us/microsoft-365/roadmap) — 이 공지 본문에는 개별 Roadmap ID가 명시되어 있지 않습니다.  
> 실제 출시 일정·기능은 변경될 수 있습니다.
