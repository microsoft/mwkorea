---
title: "Copilot 예약 프롬프트가 바뀝니다: Tasks에서 관리하고 Power Platform 없이 실행"
date: 2026-11-13T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotChat
  - ScheduledPrompts
  - Tasks
  - Automation
  - PowerPlatform
  - Governance
excerpt: "Microsoft 365 Copilot 예약 프롬프트가 Power Platform 기반에서 Copilot 자체 예약 인프라로 전환됩니다. 2026년 12월 31일 기존 방식 종료에 앞서 일정 재생성, Tasks 화면 전환, 사용자별 예약 한도를 확인해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 예약 프롬프트가 바뀝니다: Tasks에서 관리하고 Power Platform 없이 실행

매주 정해진 시간에 업무를 정리하거나, 나중에 필요한 결과를 미리 예약해 두는 Copilot 사용 방식이 바뀝니다. Microsoft는 예약 프롬프트의 실행 기반을 Power Platform에서 **Copilot 자체 예약 인프라**로 옮긴다고 발표했습니다.

2026년 11월 12일 UTC에 게시된 메시지 센터 공지 MC1550533은 관리 화면의 변화와 함께 **기존 Power Platform 기반 예약 프롬프트가 2026년 12월 31일 종료**된다고 안내합니다. 자동으로 이전되지 않는 예약은 사용자가 다시 만들어야 하므로, 현재 예약을 활용하는 조직이라면 전환 준비가 필요합니다.

새 방식은 사용자가 자리를 비운 상태에서도 일회성 또는 반복 작업을 실행하고, 관련 대화에 결과를 반환합니다. 다만 승인이 필요한 작업은 사용자의 응답을 기다리며 멈추므로, 예약했다고 모든 작업이 무인으로 끝나는 것은 아닙니다.

---

## Power Platform과 분리되는 예약 실행

사용자는 자연어로 일회성 또는 반복 작업을 예약할 수 있습니다. 새 인프라는 **Power Automate가 비활성화된 환경에서도 동작**하며, 예약 작업 데이터는 **Microsoft 365 컴플라이언스 경계 안에서 처리·저장**됩니다.

이 변화는 기존 Power Platform 정책만으로 Copilot 예약 작업의 동작을 판단해서는 안 된다는 의미가 있습니다. 조직은 적용 가능한 Microsoft 365 Copilot 제어와 내부 정책을 함께 검토해야 합니다.

원문에서 대상 사용자는 **Microsoft 365 Copilot premium 라이선스가 있는 예약 작업 사용자**로 설명하며, 조직의 제어가 적용됩니다. 모든 무료 Copilot Chat 사용자에게 동일하게 제공된다는 발표는 아닙니다.

## Tasks > Scheduled에서 관리하세요

Copilot Chat의 예약은 Microsoft 365 Copilot 앱의 **Tasks > Scheduled**에서 관리하게 됩니다.

![Microsoft가 안내한 Copilot 예약 작업 관리 화면](/mwkorea/assets/images/2026-11-13-CopilotNativeScheduledTasks/image1.png)

사용자는 개별 예약에 대해 실행, 편집, 일시 중지, 재개, 삭제를 할 수 있습니다. 사용자별 한도는 다음과 같습니다.

| 항목 | 한도·동작 |
|---|---|
| 활성 예약 | 사용자당 10개 |
| 전체 예약 | 사용자당 50개 |
| 실행 형태 | 일회성 또는 반복 |
| 결과 확인 | 관련 Copilot 대화 |
| 사용자 승인 필요 작업 | 해당 대화에서 응답할 때까지 일시 정지 |

### 기존 메뉴는 30일 동안 함께 제공됩니다

사용자에게 Scheduled 탭이 제공된 뒤 **30일 동안**은 기존 공통 헤더의 **More options (...)** 메뉴와 새 **Tasks > Scheduled** 양쪽에서 예약 작업에 접근할 수 있습니다. 이후 기존 메뉴 항목은 제거됩니다.

30일은 조직 전체에 동일한 특정 날짜부터 계산하는 기간이 아니라, **각 사용자에게 탭이 제공된 시점 기준**입니다. 도움말 문서에는 새 화면 경로와 과도기 화면을 함께 안내하는 편이 좋겠습니다.

## 전환 일정과 기존 결과 보존

| 단계 | 원문에 안내된 일정 |
|---|---|
| Frontier/TAP | 2026년 11월 11일 |
| 전 세계 배포 | 2026년 11월 30일~12월 31일 |
| 기존 Power Platform 방식 종료 | 2026년 12월 31일 |

관련 서비스는 Microsoft 365 Copilot, Copilot Chat, Copilot 앱의 Tasks이며, 플랫폼은 **Web과 Windows 데스크톱**입니다. 원문은 안정성과 이전 준비 상태에 따라 일정이 변경될 수 있다고 명시합니다.

**이미 완료된 예약 실행의 응답은 계속 남습니다.** 완료 결과 보존을 위해 별도 작업을 할 필요는 없지만, 이것이 기존의 모든 예약 설정이 자동 이전된다는 뜻은 아닙니다.

## 도입 담당자가 지금 확인할 사항

1. 예약 프롬프트를 사용하는 부서와 반복 업무를 파악하고, 전환 일정을 안내합니다.
2. **자동 이전되지 않는 예약을 12월 31일 전에 다시 만들도록** 사용자에게 안내합니다. 원문은 자동 이전 대상의 상세 기준까지 설명하지 않으므로, 모든 예약의 이전을 가정하지 않습니다.
3. 사내 매뉴얼과 헬프데스크 안내를 **Tasks > Scheduled** 기준으로 업데이트합니다.
4. Microsoft 365 Copilot 제어, 무인 실행 범위, 데이터 처리·저장 경계를 조직 정책과 대조합니다.
5. 승인이 필요한 작업은 중간에 멈출 수 있으므로, 결과 확인과 승인 응답의 담당자를 정합니다.

이 체크리스트는 새 기능을 일괄 허용하자는 제안이 아닙니다. 실제 라이선스와 테넌트 제어를 확인하면서 기존 예약 업무가 끊기지 않도록 준비하는 것이 목적입니다.

## 마무리

이번 업데이트는 예약 화면을 옮기는 것에 그치지 않습니다. **실행 인프라와 데이터 처리 경계가 바뀌고, 기존 방식의 종료일도 정해진 전환**입니다. 현재 예약 목록의 이전 여부를 확인하고, 다시 만들어야 하는 작업을 식별하는 일이 가장 먼저입니다.

> **출처**: [MC1550533 — Scheduled prompts in Microsoft 365 Copilot are moving to native Copilot scheduling and the Tasks view](https://mc.merill.net/message/MC1550533)  
> **Microsoft 365 Roadmap**: [공식 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap) — 이 공지에는 개별 Roadmap ID가 기재되어 있지 않습니다.  
> 실제 출시 일정·기능은 변경될 수 있습니다.
