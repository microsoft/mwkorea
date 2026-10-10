---
title: "Copilot 대시보드에서 바로 설문을, Viva Pulse 타겟 오디언스 서베이"
date: 2026-10-06T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - VivaInsights
  - VivaPulse
  - CopilotDashboard
  - Survey
excerpt: "Copilot 대시보드에서 수신자 명단 없이 Viva Pulse 설문을 보낼 수 있는 타겟 오디언스 서베이 기능이 추가됩니다. 50개 이상 Copilot 라이선스를 보유한 조직의 CxO/위임자가 대상이며, 정식 출시 일정이 10월 말로 한 차례 조정됐습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 대시보드에서 바로 설문을, Viva Pulse 타겟 오디언스 서베이

Copilot 도입 담당자가 가장 궁금해하는 질문 중 하나는 "직원들이 실제로 어떻게 느끼고 있는가"입니다. 사용량 지표만으로는 체감 만족도나 업무 적용도를 파악하기 어렵기 때문에, 결국 설문조사를 돌려야 하는데 수신자 명단을 만들고 관리하는 일이 생각보다 번거롭습니다.

Microsoft는 이런 수고를 줄이기 위해 **Copilot 대시보드에 타겟 오디언스 서베이** 기능을 도입합니다. 대시보드 데이터를 기반으로 미리 정의된 Copilot 사용자 그룹에게 별도의 수신자 명단 없이 Viva Pulse 설문을 바로 보낼 수 있는 기능입니다.

이번 글은 **2026년 10월 6일 일정이 업데이트된 MC1446805 공지**를 기준으로 정리합니다. 공지는 해당 날짜에 일정만 갱신됐으며, 기능 자체가 그 시점에 새로 발표된 것은 아닙니다.

---

## 무엇이 달라지나요?

기존에는 Copilot 사용자 대상 설문을 보내려면 관리자가 별도로 대상자 명단을 뽑아 Viva Pulse 캠페인을 구성해야 했습니다. 이번 기능은 이 과정을 생략하고, **Copilot 대시보드 데이터에서 바로 설문 오디언스를 생성**합니다.

- 설문 대상은 Copilot 대시보드 데이터로 동적으로 산정되며, 기존 대시보드 필터를 적용해 범위를 좁힐 수 있습니다.
- 제공되는 기본 오디언스는 **모든 Copilot 라이선스 보유 사용자**와 **모든 Copilot 활성 사용자** 두 가지입니다.
- 오디언스 선택 과정에서 **개별 직원의 신원은 노출되지 않습니다.**
- 기존에 설정된 **Viva Insights 제외 목록(exclusion list)**은 이 기능에서도 그대로 적용됩니다.
- 설문 결과는 기존 Pulse 화면과 Copilot 대시보드에 함께 표시됩니다.

![Copilot 대시보드 타겟 오디언스 서베이 화면](/mwkorea/assets/images/2026-10-06-VivaCopilotTargetedSurveys/image1.png)

## 누가 쓸 수 있나요?

공지가 명시한 적용 대상은 다음과 같습니다.

| 구분 | 조건 |
|---|---|
| 조직 규모 | Copilot 라이선스 50개 이상 |
| 사용자 역할 | Copilot 대시보드의 CxO 또는 CxO 위임자(delegate) 역할 |
| 전제 서비스 | Microsoft Viva Pulse 및 Copilot 대시보드 사용 조직 |

즉 모든 관리자가 쓸 수 있는 기능이 아니라, **대시보드에서 CxO 또는 위임자 권한을 가진 사용자**로 한정됩니다. 도입 전에 누가 해당 역할을 보유하고 있는지 점검이 필요합니다.

## 출시 일정: 이번에 한 차례 미뤄졌습니다

| 단계 | 공지에 기재된 일정 |
|---|---|
| Public Preview | 2026년 8월 중순 시작, 9월 말 완료 예상 |
| General Availability (Worldwide) | 2026년 10월 말 시작(기존 9월 말에서 변경), 11월 중순 완료 예상(기존 9월 말에서 변경) |

공지 상단에는 "일정을 업데이트했다(We have updated the timeline)"는 안내가 있으며, GA 시작·완료 시점 모두 **기존 9월 말에서 10월 말~11월 중순으로 순연**됐습니다. 이 글에서 실제 테넌트별 배포 완료 여부를 확인한 것은 아니므로, 위 일정은 공지에 기재된 계획으로 참고하시기 바랍니다.

## 기본 활성화, 관리자 통제는 어떻게 하나요?

이 기능은 **자격을 갖춘 조직에서 기본적으로 활성화**되며, 사용자가 별도로 켜야 할 작업은 없습니다.

관리자가 수행할 수 있는 권고 조치는 다음과 같습니다.

- Copilot 대시보드에서 CxO 또는 CxO 위임자 역할이 할당된 사용자를 점검합니다.
- 변화 관리 담당자에게 타겟 오디언스 서베이 기능을 안내합니다.
- Viva Insights 제외 목록이 최신 상태이며 제외 대상이 정확히 반영됐는지 확인합니다.

기능을 끄고 싶다면 **Microsoft 365 관리 센터 → 설정 → Microsoft Viva → Feature access management → Viva Pulse**에서 **Targeted Audience Surveys** 항목을 비활성화하면 됩니다.

## 컴플라이언스 관점에서 확인할 점

공지의 컴플라이언스 Q&A를 요약하면 다음과 같습니다.

- **관리자 통제 여부**: 가능합니다. Viva Pulse의 Feature access management에서 기능을 끌 수 있습니다.
- **사용자 커뮤니케이션 방식 변화 여부**: 있습니다. 권한을 가진 사용자가 Copilot 대시보드에서 미리 정의된 오디언스에게 Viva Pulse 설문을 보내는 새로운 방법이 추가됩니다.
- **고객/조직 데이터의 새로운 처리 방식 여부**: 있습니다. 설문 대상자는 Copilot 대시보드 데이터와 기존 오디언스 필터를 이용해 산정됩니다.
- **역할 기반 접근 제어(RBAC) 적용 여부**: 적용됩니다. Copilot 대시보드에서 CxO 또는 CxO 위임자 역할을 가진 사용자만 설문을 만들 수 있습니다.

조직·직무 메타데이터가 포함되지 않는 비식별 오디언스 구조이지만, 새로운 데이터 처리 경로가 추가되는 만큼 내부 데이터 취급 기준에 맞춰 사전 검토를 권장합니다.

## 마무리

타겟 오디언스 서베이는 Copilot 사용자 피드백 수집을 "명단 관리"에서 "대시보드 기반 자동 타겟팅"으로 바꾸는 변화입니다. 50개 라이선스 조건과 CxO/위임자 역할 보유 여부를 먼저 확인하고, GA 일정이 다시 조정될 수 있다는 점을 감안해 테넌트별 실제 제공 여부를 확인한 뒤 적용을 준비하시기 바랍니다.

> 출처: **MC1446805 — Microsoft Viva: Targeted audience surveys in the Copilot dashboard**  
> 원문: https://mc.merill.net/message/MC1446805  
> Microsoft 365 Roadmap: https://www.microsoft.com/microsoft-365/roadmap?filters=&searchterms=568072  
> **실제 출시 일정·기능은 변경될 수 있습니다.**
