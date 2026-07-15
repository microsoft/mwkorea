---
title: "E3 사용자도 Copilot Studio에서 에이전트를 만든다고요? 원인과 차단 방법"
date: 2026-07-09T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Microsoft365E3
  - Microsoft365E5
  - ClassicAgents
  - Governance
  - DataverseForTeams
excerpt: "E3·E5 사용자가 Copilot Studio 웹 앱에서 클래식 에이전트를 만들 수 있는 이유는 라이선스에 포함된 Copilot Studio for Microsoft Teams 권한 때문입니다. 조직에서 이를 허용하지 않으려면 Power Virtual Agents for Office 365 서비스 플랜을 비활성화해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# E3 사용자도 Copilot Studio에서 에이전트를 만든다고요? 원인과 차단 방법

최근 E3 같은 기본 Microsoft 365 라이선스만 가진 사용자가 **Copilot Studio 웹 앱에서 Teams용 에이전트를 만드는 화면**을 보게 됐다는 문의가 늘고 있습니다. 별도의 Copilot Studio 라이선스를 구매한 적이 없는데도 이런 화면이 나타나니, 관리자 입장에서는 라이선스나 과금 설정이 잘못된 것은 아닌지 걱정할 수 있습니다.

결론부터 말하면 새로 구매된 기능이 아닙니다. E3·E5 등 일부 Microsoft 365 구독에 이미 포함된 **Copilot Studio for Microsoft Teams 플랜**이 더 눈에 잘 띄는 경로로 노출된 것입니다.

![Copilot Studio 클래식 에이전트 거버넌스](/mwkorea/assets/images/2026-07-09-E3UsersCopilotStudioClassicAgents/image1.png)

---

## 무엇이 바뀌었나

기본 라이선스 사용자가 클래식 에이전트를 만들 수 있는 권한 자체는 새 기능이 아닙니다. 달라진 것은 **접근 경로**입니다.

> 2026년 6월 말부터 독립형 Copilot Studio for Teams 앱에서 클래식 챗봇을 새로 만들 수 없게 되었고, 사용자는 Copilot Studio 웹 앱으로 이동하게 됩니다.

이전에는 Teams 안쪽에 있던 기능이 Copilot Studio 웹 앱에 직접 나타나면서, 사용자는 기능을 더 쉽게 발견하고 관리자는 갑자기 권한이 확대된 것처럼 느끼게 됐습니다.

## E3·E5 사용자가 만들 수 있는 이유

Microsoft 365 엔터프라이즈 라이선스에는 **Copilot Studio for Microsoft Teams 플랜**이 포함될 수 있습니다. 이 플랜은 Copilot Studio 전체 기능이 아니라 제한된 하위 집합을 제공합니다.

- 클래식 오케스트레이션 기반 에이전트 제작
- Dataverse for Teams 환경 사용
- Microsoft Teams 채널로 게시

이 권한은 라이선스의 **Power Virtual Agents for Office 365** 서비스 플랜을 통해 제공됩니다. 사용자가 에이전트를 만들면 선택한 팀에 Dataverse for Teams 환경이 자동으로 프로비저닝됩니다.

## 포함되지 않는 기능

이 기본 권한을 독립형 Copilot Studio 라이선스와 혼동하면 안 됩니다.

| 구분 | 기본 Teams 플랜 |
|---|---|
| 클래식 에이전트 | 지원 |
| Dataverse for Teams | 지원 |
| Teams 게시 | 지원 |
| 생성형 오케스트레이션 | 미지원 |
| 프리미엄 커넥터 | 미지원 |
| 임의의 외부 채널 게시 | 미지원 |

Teams에서 이 플랜으로 만든 에이전트를 사용하는 것은 **Copilot Credits를 소비하지 않습니다**. 따라서 이 문제는 추가 과금보다는 거버넌스와 Dataverse for Teams 환경 증가 관점에서 보는 것이 적절합니다.

## 차단 방법: 서비스 플랜 비활성화

해당 사용자가 Copilot Studio 웹 앱과 Teams 앱 양쪽에서 클래식 에이전트를 만들거나 편집하지 못하게 하려면, 라이선스의 **Power Virtual Agents for Office 365** 서비스 플랜을 비활성화합니다.

### 개별 사용자

1. Microsoft 365 admin center에서 **Users > Active users**로 이동합니다.
2. 사용자를 선택하고 **Licenses and apps**를 엽니다.
3. Microsoft 365 라이선스를 펼칩니다.
4. **Power Virtual Agents for Office 365**를 선택 해제합니다.
5. 변경 사항을 저장합니다.

![Power Virtual Agents for Office 365 서비스 플랜 비활성화](/mwkorea/assets/images/2026-07-09-E3UsersCopilotStudioClassicAgents/image2.png)

### 그룹 기반 라이선스

사용자가 많다면 Microsoft Entra ID의 그룹 기반 라이선스를 이용하는 편이 낫습니다.

1. 라이선스 할당에 사용하는 그룹을 엽니다.
2. 할당된 Microsoft 365 라이선스를 편집합니다.
3. **Power Virtual Agents for Office 365** 서비스 플랜을 끕니다.
4. 변경된 할당이 그룹 구성원에게 적용되는지 확인합니다.

그룹 기반으로 설정하면 입사·이동·퇴사에 따라 구성원이 바뀌어도 동일한 정책을 유지하기 쉽습니다.

## 차단 후에도 남는 것

서비스 플랜을 끄는 것만으로 모든 흔적이 정리되지는 않습니다.

- 대상 사용자의 클래식 에이전트 생성·편집은 차단됩니다.
- 이미 만든 에이전트가 자동으로 삭제되지는 않습니다.
- 이미 프로비저닝된 Dataverse for Teams 환경도 자동 정리되지 않습니다.
- 독립형 Copilot Studio 또는 Microsoft 365 Copilot 라이선스에서 부여된 별도 권한에는 영향을 주지 않습니다.

## 관리자가 함께 점검할 항목

- 기존 Dataverse for Teams 환경과 클래식 에이전트 인벤토리를 먼저 확인합니다.
- 실제 업무에 사용 중인 에이전트를 끄지 않도록 사용자·소유자와 검토합니다.
- Managed Environments를 활용해 환경 생성과 사용 위치를 관리합니다.
- DLP 정책을 적용해 허용된 제작자도 정해진 데이터 경계 안에서 작업하도록 합니다.

## 마무리

E3·E5 사용자가 클래식 Teams 에이전트를 만들 수 있는 것은 기존 라이선스 권한이며, 최근의 리디렉션 변경으로 Copilot Studio 웹 앱에서 더 잘 보이게 된 것입니다. 조직 정책상 이를 허용하지 않는다면 **Power Virtual Agents for Office 365** 서비스 플랜을 끄고, 기존 에이전트와 Dataverse for Teams 환경까지 별도로 점검해야 합니다.

---

> **원문**: [Why Your E3 Users Can Suddenly Build Agents in Copilot Studio — and How to Turn It Off (The Custom Engine, Microsoft Copilot Studio CAT, 2026-07-09)](https://microsoft.github.io/mcscatblog/posts/e3-users-build-agents-turn-it-off/)
>
> 자세한 내용은 원문을 참조하세요.
