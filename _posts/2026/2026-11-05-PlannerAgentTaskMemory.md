---
title: "Planner Agent가 업무 배정과 밀린 일 챙기기까지: 12월 업데이트 미리 보기"
date: 2026-11-05T00:00:00 KST
categories:
  - Copilot
tags:
  - Planner
  - Agent
  - Microsoft365Copilot
  - Memory
excerpt: "Planner Agent에 공동 플랜의 작업 배정, 예약형 업무 따라잡기, Copilot 메모리 연동이 추가될 예정입니다. 사용자 확인 전에는 초안으로 남는 동작과 지원 플랜의 제한을 함께 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Planner Agent가 업무 배정과 밀린 일 챙기기까지: 12월 업데이트 미리 보기

프로젝트가 바빠질수록 중요한 일은 메일, 채팅, 회의 사이에 흩어집니다. 해야 할 일을 찾는 것만큼, 담당자를 정하고 실제 작업으로 저장하는 과정도 부담입니다.

Microsoft는 MC1539002에서 Microsoft Copilot Chat의 Planner Agent 확장을 예고했습니다. 핵심은 **작업 배정, 예약형 task catch-up, Copilot 메모리 활용**이며, AI가 제안한 변경을 사용자가 검토하고 확정하는 흐름을 유지합니다.

---

## 공동 기본 플랜에서 작업을 배정합니다

공유된 기본 플랜에서 한 명 또는 여러 명에게 작업을 배정하고, 여러 작업을 한꺼번에 배정할 수 있게 됩니다. 담당자 재지정과 제거, 사람별 작업 묶어 보기도 지원합니다.

변경 제안은 저장 전에 검토할 수 있습니다. 따라서 “에이전트에게 담당자를 정해 달라고 요청했다”와 “공식 작업 배정이 저장됐다”는 서로 다른 단계입니다.

## 밀린 일을 찾아주는 task catch-up

최근 메일, 채팅, 회의를 바탕으로 미완료 업무, 약속한 일, 내 입력을 기다리는 항목을 제안합니다. 필요할 때 실행하거나 반복 일정을 구성할 수 있으며, 제안이 준비되면 이메일 알림을 받는 옵션도 있습니다.

제안에는 출처가 포함되고 **Planner에 저장할 때까지 수정 가능한 초안**으로 남습니다. 사용자가 반복 일정을 수정·일시 중지·삭제할 수 있으며, 반복 일정이 자동으로 만들어지지는 않습니다.

## 메모리와 대규모 플랜 지원

Planner Agent는 저장된 메모리와 이전 Copilot 대화에서 추론한 선호를 활용해 응답을 개인화합니다. 사용자는 에이전트를 통해 메모리를 저장·갱신·삭제하고, Copilot 개인화 설정에서 검토·삭제하거나 끌 수 있습니다.

기존의 **플랜 생성 시 30개 작업 제한이 제거**되며, 복잡한 플랜에 대한 더 완전한 응답도 개선 사항에 포함됩니다. 모델 선택, Microsoft 365 콘텐츠를 활용한 grounding, 속도와 안정성 향상도 안내되어 있습니다.

## 사용 전에 알아둘 제한

| 항목 | 원문 안내 |
|---|---|
| 지원 범위 | 개인 작업과 공유 기본 플랜 |
| 미지원 플랜 | Premium 플랜 |
| 지원하지 않는 작업 | 작업 삭제, 변경 실행 취소 |
| 저장 조건 | AI 생성 작업·플랜·배정 등은 사용자 검토·확인 전까지 초안 |
| 데이터 접근 | 로그인한 사용자가 이미 접근할 수 있는 Microsoft 365 콘텐츠만 사용 |

기능 개선은 Planner Agent에 접근 가능한 사용자에게 기본 활성화되지만, 반복 catch-up은 사용자가 직접 설정해야 합니다.

## 제공 일정과 조직 준비

전 세계 일반 공급은 **2026년 12월 초 시작 및 같은 달 초 완료 예상**입니다. 대상은 활성 Microsoft Copilot 라이선스와 Planner Agent 접근 권한이 있는 사용자이며, 웹 Copilot과 Microsoft Teams의 Copilot, Planner가 관련 서비스입니다.

사용자는 `Agents & Skills`에서 찾거나 고정하고, 채팅에서 `@Planner Agent`로 호출할 수 있습니다. 관리자는 라이선스와 에이전트 접근 설정을 확인하고, 초안 검토 및 예약 실행 방법을 교육하는 것이 좋습니다.

조직 차원의 고정은 `Agents > All agents > Manage pinned agents`에서 설정합니다. **AI Administrator 역할**이 필요하며 사용자에게 표시되기까지 최대 **6시간**이 걸릴 수 있습니다.

## 마무리

이번 업데이트는 작업을 작성하는 도구에서 **해야 할 일을 찾아 배정까지 준비하는 에이전트**로 범위를 넓힙니다. 실제 도입에서는 Premium 플랜 미지원, 삭제·실행 취소 미지원, 사용자 확정 전 초안이라는 경계를 먼저 공유해야 합니다.

> **출처**: [MC1539002 — Microsoft Copilot Chat: Planner Agent task assignment, catch-up, and Copilot memory integration](https://mc.merill.net/message/MC1539002). [Microsoft 365 Roadmap 573168](https://www.microsoft.com/microsoft-365/roadmap?filters=&searchterms=573168). 실제 출시 일정·기능은 변경될 수 있습니다.
