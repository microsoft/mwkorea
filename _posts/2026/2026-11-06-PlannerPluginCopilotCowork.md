---
title: "할 일 목록에서 실행까지: Copilot Cowork에 연결되는 Planner 플러그인"
date: 2026-11-06T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotCowork
  - Planner
  - Plugins
  - Agents
excerpt: "Planner 플러그인이 Copilot Cowork에 작업 메모·체크리스트·첨부파일을 연결합니다. 우선순위 정리부터 산출물 작성과 계획 보고서까지 지원하며, 실제 변경에는 사용자 검토와 승인이 필요합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 할 일 목록에서 실행까지: Copilot Cowork에 연결되는 Planner 플러그인

Planner에 할 일을 기록해도, 자료를 찾고 문서를 작성하고 진행 상태를 갱신하는 일은 별도로 남습니다. Microsoft가 안내한 Planner Plugin은 이 간격을 Copilot Cowork로 연결합니다.

Cowork는 작업의 메모, 체크리스트, 첨부파일을 맥락으로 삼아 조사·초안 작성·분석·파일 생성을 돕습니다. 중요한 경계는 **Planner의 변경과 Microsoft 365 작업 실행 전에 사용자가 검토하고 승인한다는 점**입니다.

---

## 플러그인은 어디에서 찾나요?

사용자는 Microsoft Copilot의 **Plugins > Cowork**에서 Microsoft Corporation이 게시한 Planner Plugin을 찾을 수 있습니다. 플러그인 제공과 필요한 계정 연결을 마친 뒤 사용합니다.

![Copilot Cowork에 Planner 플러그인 추가](/mwkorea/assets/images/2026-11-06-PlannerPluginCopilotCowork/image1.png)

대상 사용자는 활성 Microsoft 365 Copilot 라이선스, Copilot Cowork 및 Microsoft Planner 접근 권한, Planner Plugin 사용 권한이 있어야 합니다. 플러그인은 **로그인한 사용자의 기존 Planner 권한 안에서만** 동작하며 추가 접근 권한을 부여하지 않습니다.

## 우선순위를 정하고 실제 작업을 돕습니다

여러 계획에 흩어진 담당 작업을 모아 기한 초과와 예정 작업을 확인하고, 먼저 집중할 일을 추천받을 수 있습니다.

![여러 계획에 배정된 작업 확인](/mwkorea/assets/images/2026-11-06-PlannerPluginCopilotCowork/image2.png)

작업 설명과 체크리스트, 첨부자료를 바탕으로 조사나 초안 작성, 분석, 산출물 생성을 요청할 수도 있습니다. 승인 후에는 진행 상태 갱신, 체크리스트 완료, 산출물 링크 추가, 작업 완료 표시를 수행할 수 있습니다.

![Planner 작업의 실행을 지원하는 Cowork](/mwkorea/assets/images/2026-11-06-PlannerPluginCopilotCowork/image3.png)

## 기존 자료를 계획과 보고서로 연결하기

스프레드시트, 문서, 프레젠테이션, 회의 메모, 목표에서 계획과 작업의 **검토용 제안**을 만들 수 있습니다. 보고서는 진행 상황, 예정·지연 작업, 담당자와 버킷별 업무, 목표 진척, 장애 요인과 다음 행동을 시각적으로 정리합니다.

Planner 맥락을 이용해 메일 초안과 발송, 회의 예약, Teams 업데이트, 문서·발표자료·스프레드시트 작성으로 이어가는 것도 공지된 활용 범위입니다. 이 역시 실제 실행 전 승인 흐름을 전제로 이해해야 합니다.

반복 작업은 작업 요약과 계획 보고서의 예약 실행, 메일이나 Teams 메시지 이벤트 기반 요청으로 연결할 수 있습니다. **예약했다고 Planner 변경 승인까지 생략되는 것은 아닙니다.**

## 관리자 배포와 사용자 연결은 별개입니다

관리자는 Microsoft 365 관리 센터의 **Agents > Tools** 또는 **Agents > All agents**에서 Planner Plugin을 찾아 대상 사용자·그룹에 설치하거나, 적격 사용자가 직접 획득할 수 있도록 제공 범위를 설정합니다. 관리자가 배포한 플러그인은 대상 사용자에게 자동으로 획득됩니다.

필요한 커넥터 로그인과 동의는 사용자가 직접 완료해야 하며, 관리자가 대신 로그인할 수 없습니다. 사용자는 Sources & Skills 패널에서 자신이 획득한 플러그인을 대화별로 켜거나 끌 수 있습니다. 이미 대상자에게 배포했다면 추가 배포 작업은 필요하지 않습니다.

## 일정과 데이터 활용을 함께 확인하세요

공지에서는 전 세계 GA 배포가 **2026년 10월 말 시작되어 11월 말 완료 예상**이라고 설명하며, 현재 Frontier에서 이용할 수 있고 GA 목표가 11월이라고 함께 안내합니다. 조직에 실제로 노출되는 시점은 확인이 필요합니다.

이 기능은 작업 메모·체크리스트·첨부파일·담당자·기한 등의 기존 Planner 데이터를 Microsoft 365 업무 수행 맥락으로 사용합니다. 따라서 단순한 작업 목록 UI 변경이 아니라 데이터 활용과 에이전트 동작의 변화로 검토하는 것이 좋습니다.

시작할 때는 좁은 사용자 그룹에서 권한과 승인 흐름을 먼저 확인하세요. 운영 참고 자료로는 [플러그인 관리](https://learn.microsoft.com/copilot/cowork/cowork-manage-plugins), [플러그인 사용](https://learn.microsoft.com/copilot/cowork/cowork-plugins), [Planner 활용 범위](https://support.microsoft.com/planner/planner-cowork-capabilities)가 공지에 연결되어 있습니다.

> 출처: **MC1540339 — Microsoft Planner: Planner capabilities in Copilot Cowork through the Planner Plugin**  
> [Message Center 원문](https://mc.merill.net/message/MC1540339) · [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)  
> 공지에 개별 Roadmap ID는 명시되어 있지 않습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
