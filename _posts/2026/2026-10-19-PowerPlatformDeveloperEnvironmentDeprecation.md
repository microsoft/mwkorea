---
title: "[긴급 공지] 12월 15일부터 관리되지 않는 개발자 환경이 중지됩니다"
date: 2026-10-19T00:00:00 KST
categories:
  - PowerPlatform
tags:
  - PowerPlatform
  - PowerApps
  - DeveloperPlan
  - ManagedEnvironments
  - Dataverse
  - Deprecation
excerpt: "관리되지 않는 개발자 환경은 11월 15일부터 새로 만들 수 없고, 12월 15일에 중지, 2027년 1월 15일부터 삭제됩니다. 지금 내 개발자 환경이 관리형인지 확인하세요."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# [긴급 공지] 12월 15일부터 관리되지 않는 개발자 환경이 중지됩니다

Power Apps Developer Plan으로 만든 **관리되지 않는(unmanaged) 개발자 환경**이 단계적으로 종료됩니다. 약 8주 안에 확인하고 조치해야 합니다.

**영상으로 먼저 보기:** 매일매일코파일럿 채널의 「[긴급 공지] Power Platform 중요 변경 예고 | Teams용 Dataverse · 관리되지 않는 개발자 환경 사용 중단」

{% include video id="XfWXN1NCAfQ" provider="youtube" %}

> **🔴 지금 당장 할 일 — 딱 하나**
> **현재 존재하는 내 개발자 환경이 관리형(managed)인지 확인하세요.**
> [Power Platform 관리 센터](https://admin.powerplatform.microsoft.com) **관리 > 환경**에서 **유형 = 개발자**, **관리형 = 아니요**로 필터링하면 대상이 나옵니다.
>
> - **관리형이면** 영향이 없습니다.
> - **관리형이 아니면 12월 15일 전에** 관리형으로 전환하거나 솔루션을 옮기세요.

![관리되지 않는 개발자 환경 변경 일정 인포그래픽: 2026.11.15 신규 생성 종료, 12.15 환경 중지, 2027.01.15 삭제 시작. 환경 라우팅으로 만든 관리형 개발자 환경은 예외이며, 관리형 전환 또는 솔루션 이동으로 대응](/mwkorea/assets/images/2026-10-19-PowerPlatformDeprecation/infographic-dev.png)

---

## 일정

| 날짜 | 무슨 일이 생기나요? |
|---|---|
| **2026년 11월 15일** | 관리되지 않는 개발자 환경을 새로 만들 수 없습니다. Developer Plan에 가입해도 환경이 만들어지지 않습니다. |
| **2026년 12월 15일** | 기존 환경이 **중지**됩니다. 앱, 플로우, 에이전트, Power Pages 개발 사이트, 데이터를 쓸 수 없습니다. |
| **2027년 1월 15일** | 중지된 환경이 **삭제**되기 시작합니다. |

## 내 환경은 해당되나요?

| 환경 | 영향 |
|---|---|
| 관리되지 않는 개발자 환경 (Developer Plan 포함) | **해당** |
| **관리형 개발자 환경** | 해당 없음 |
| **환경 라우팅으로 만들어진 개발자 환경** | 해당 없음 (기본적으로 관리형) |
| 프로덕션, 샌드박스, 체험판, 기본 환경 | 해당 없음 |

개발자 환경 유형은 사라지지 않지만 앞으로는 **관리형만**, 새로 만들 때 **사용자당 1개**만 만들 수 있습니다. **이미 관리형 개발자 환경을 여러 개 가지고 있어도** 기존 환경은 그대로 유지됩니다.

## 해야 할 일

**관리자**

1. 위의 필터로 대상 환경을 찾고, **마지막 활동**으로 아직 쓰는 환경을 가립니다.
2. 필요한 환경은 12월 15일 전에 둘 중 하나를 선택합니다.
   - **관리형으로 전환:** 관리 센터에서 **Enable Managed Environments**를 선택합니다. 앱·플로우·데이터는 그대로 유지됩니다.
   - **솔루션 이동:** 솔루션을 내보내 샌드박스 같은 다른 환경으로 가져옵니다.
3. 메이커에게 개인 작업 공간을 주려면 **환경 라우팅**을 켭니다. 관리형 개발자 환경이 자동으로 만들어집니다.

**메이커**

- **지금 솔루션을 내보내** 사본을 확보하세요.
- 관리자에게 관리형 전환을 요청하세요.

## 헷갈리기 쉬운 점

**관리형으로 전환하면 환경이 바뀌나요?**
같은 환경에 관리형 속성만 켜는 것입니다. 환경 유형은 개발자 환경으로 남고 앱·데이터도 유지됩니다.

**Dataverse 용량을 쓰나요?**
공식 문서상 개발자 환경의 용량은 테넌트 쿼터에 포함되지 않아, 전환해도 소비하지 않는 것으로 보입니다. 전환 시점의 계산을 직접 설명한 문구는 없으므로 전환 전에 관리 센터에서 확인하세요. 반대로 솔루션을 샌드박스로 옮기면 일반적으로 용량을 사용합니다.

**라이선스가 필요한가요?**
**전환하면 그 환경에서 앱·플로우를 실행하는 사용자에게 프리미엄 라이선스가 필요합니다.** Developer Plan에는 Managed Environments 권한이 없습니다. 만들고 미리 보는 데는 프리미엄 라이선스가 필요 없습니다.

**전환하면 또 바뀌는 것은?**
공유 제한 같은 관리자 정책이 적용되어 메이커의 사용 방식이 달라질 수 있습니다. 전환은 Power Platform 관리자 또는 Dynamics 365 관리자만 할 수 있습니다.

## 왜 바뀌나요? 매니지드 앱과의 연결

팀 내에서는 이번 변경이 이번에 미리 보기가 시작된 **매니지드 앱(Copilot Managed Runtime)** 과 같은 방향이라고 봅니다. 매니지드 앱은 각 사용자의 **환경 라우팅 개인 관리형 개발자 환경**을 기반으로 만들어지기 때문입니다. 공식 문서에서 확인된 내용은 다음과 같습니다.

- 매니지드 앱용 환경 라우팅은 **모든 테넌트에서 자동으로 켜져 있고 끌 수 없습니다.**
- 라우팅 규칙이 없으면 **"모든 사용자를 각자의 개인 개발자 환경으로" 보내는 규칙이 자동 생성**됩니다. 기존 규칙에 보안 그룹만 있으면 그 밖의 메이커는 매니지드 앱을 만들 수 없으니, **Everyone 규칙**이 있는지 확인하세요.
- 이렇게 만들어진 환경은 **기본적으로 관리형**입니다. 관리자가 만든 적 없는 개발자 환경이 보여도 **삭제 전에 소유자와 앱을 먼저 확인**하세요.
- 환경 라우팅으로 환경을 받는 데에는 **라이선스 조건이 문서에 없고**, 라이선스는 환경에서 **앱을 실행할 때** 필요합니다. Copilot 라이선스에 포함된 Managed Environments 권한은 **Copilot Studio 범위**로 한정됩니다.

## 참고: Dataverse for Teams 환경도 종료됩니다

일정은 더 여유롭습니다.

| 날짜 | 일어나는 일 |
|---|---|
| **2026년 11월 15일** | 새 Dataverse for Teams 환경 생성 종료 |
| **2027년 9월 15일** | 업그레이드하지 않은 환경 중지 |
| **2027년 10월 30일** | 업그레이드하지 않은 환경 폐기 |

관리 센터에서 **유형 = Microsoft Teams** 환경을 확인하고, 필요한 환경은 **2027년 10월 30일 전에** [Dataverse로 업그레이드](https://learn.microsoft.com/en-us/power-platform/admin/about-teams-environment#upgrade-process)하세요. 업그레이드하려면 **Dataverse 용량**과 **Power Apps·Power Automate·Copilot Studio 라이선스**가 필요합니다. Teams 채널·채팅·파일은 영향이 없습니다.

---

> 출처: [Important changes (deprecations) coming in Power Platform](https://learn.microsoft.com/en-us/power-platform/important-changes-coming) (2026년 10월 16일 업데이트), [Environment routing](https://learn.microsoft.com/en-us/power-platform/admin/default-environment-routing), [Environment routing for Microsoft Copilot Managed Runtime](https://learn.microsoft.com/en-us/power-platform/admin/default-environment-routing-copilot-managed-runtime), [Enable managed environments](https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-enable), [Managed Environments 라이선스](https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-licensing). 매니지드 앱은 미리 보기 기능입니다. 일정과 세부 절차는 변경될 수 있으니 실행 전 원문과 관리 센터 안내를 다시 확인하세요.
