---
title: "최근 30일 에이전트 사용자를 CSV로: Agent 365 Active Users 내보내기"
date: 2026-08-28T00:00:00 KST
categories:
  - Copilot
tags:
  - Agent365
  - ActiveUsers
  - UsageReport
  - Licensing
  - AdminCenter
excerpt: "Microsoft Agent 365 Registry에 등록된 에이전트를 최근 30일 동안 사용한 사용자의 인벤토리를 CSV로 내보낼 수 있습니다. AI Admin과 Global Admin이 확인할 필드, 보고서의 한계와 개인정보 보호 운영 포인트를 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 최근 30일 에이전트 사용자를 CSV로: Agent 365 Active Users 내보내기

에이전트 도입이 늘면 라이선스 검토 담당자는 등록된 에이전트 수뿐 아니라 실제로 누가 얼마나 사용했는지 확인해야 합니다. Microsoft Agent 365의 새 **Active Users** 내보내기는 테넌트 Registry에 등록된 에이전트를 최근 30일 동안 사용한 사용자 인벤토리를 CSV로 제공합니다.

메시지 센터 **MC1462914**는 이 기능을 라이선스 검토와 계획을 돕는 읽기 전용 보고 기능으로 설명합니다. 사용자를 자동으로 라이선스에 할당하거나 청구를 바꾸는 기능은 아닙니다.

---

## 내보내기 위치와 권한

새 옵션은 Microsoft 365 관리 센터의 다음 경로에 제공됩니다.

**Agents > All Agents > Export > Active Users**

대상 관리자는 **AI Admin**과 **Global Admin**입니다. Agent 365에 이미 접근할 수 있는 해당 관리자에게 기본으로 활성화됩니다. 일반 사용자나 모든 보고서 열람자가 같은 CSV를 내려받을 수 있다는 내용은 아닙니다.

## CSV에 포함되는 필드

보고서는 Agent 365 Registry에 표시되는 에이전트를 지난 30일 동안 적극적으로 사용한 사용자를 대상으로 하며 다음 값을 포함합니다.

- User Principal Name(UPN)
- 사용한 전체 에이전트 수
- 전체 세션 수
- 마지막 활동 날짜

이 정보로 도입 규모와 반복 사용 여부를 검토하고 라이선스 계획 논의를 지원할 수 있습니다. 그러나 CSV는 30일 활동의 요약이며 사용 목적, 업무 성과, 에이전트 응답 품질을 설명하지 않습니다. 세션 수만으로 사용자의 가치나 라이선스 필요성을 단정해서는 안 됩니다.

## 기존 환경에 미치는 영향

이번 변경으로 기존 에이전트, 사용자 권한, 청구 프로세스가 바뀌지 않습니다. 보고서는 이미 존재하는 에이전트 활동 정보를 관리자가 꺼내 볼 수 있게 하는 기능입니다.

읽기 전용이라는 말은 원본 에이전트와 사용자 권한을 CSV에서 수정하지 못한다는 뜻입니다. 내보낸 파일 자체에는 UPN이라는 사용자 식별자와 활동 지표가 있으므로, 파일의 저장·공유·삭제는 조직의 개인정보 및 보고 데이터 정책을 따라야 합니다.

## 출시 일정

| 단계 | 일정 |
|---|---|
| 정식 출시, 전 세계 | 2026년 8월 말 배포 시작 및 완료 예정 |

공지는 8월 말의 짧은 배포 창을 안내하지만 테넌트에서 메뉴가 보이는 정확한 날짜는 달라질 수 있습니다. 별도 준비 작업은 없으며 기능은 적격 관리자에게 기본 제공됩니다.

## 실무에서 활용할 때의 체크포인트

Microsoft는 에이전트 라이선스 의사 결정 담당자에게 적절한 관리 권한을 부여하고, 내보낸 데이터를 도입 현황과 내부 계획에 활용할 것을 권합니다. 운영 과정에서는 다음을 함께 정해 두세요.

1. AI Admin과 Global Admin 중 누가 보고서를 내려받을지 최소 권한 검토
2. 월별 또는 분기별 라이선스 검토 일정에 30일 데이터를 연결
3. UPN과 활동 지표가 포함된 CSV의 보관 위치 및 보존 기간 지정
4. 공유 대상 제한과 파일 삭제 절차 마련
5. 활동량이 낮은 경우 사용자·업무 소유자와 맥락 확인

CSV는 채택을 파악하는 출발점입니다. 실제 라이선스 결정에서는 사용한 에이전트의 업무 중요도, 계절성, 다음 달 계획, 사용자 피드백과 비용을 함께 보는 것이 좋습니다.

---

> **출처**
>
> - 원문 ID: **MC1462914** — *Microsoft Agent 365: Active Users export for agent usage reporting*
> - 원문: [MC1462914](https://mc.merill.net/message/MC1462914)
> - [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
