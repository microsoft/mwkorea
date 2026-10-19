---
title: "에이전트도 자기 신원으로 일하게: Dataverse와 Entra agent identity"
date: 2026-10-17T00:00:00 KST
categories:
  - Copilot
tags:
  - Dataverse
  - MicrosoftEntra
  - AgentIdentity
  - Governance
excerpt: "Microsoft Entra agent identity를 Dataverse agent user로 프로비저닝하는 기능이 안내됐습니다. 에이전트별 최소 권한 역할과 작업 감사를 통해 자율 실행과 사용자 대행 작업의 추적성을 높이는 접근입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트도 자기 신원으로 일하게: Dataverse와 Entra agent identity

에이전트가 업무 데이터를 읽고 변경하기 시작하면, 어떤 주체가 어떤 권한으로 작업했는지를 구분해야 합니다. Microsoft는 기업이 관리하는 Entra agent identity를 Dataverse의 agent user로 연결하는 기능을 안내했습니다.

핵심은 사람 계정을 그대로 공유하기보다 **에이전트의 목적에 맞는 신원과 최소 권한 역할을 부여하는 것**입니다. 자율 실행과 사용자 대행 모두에서 통제와 추적성을 확보하려는 방향입니다.

---

## 신원·권한·감사를 연결합니다

에이전트를 Dataverse agent user로 프로비저닝하고, 의도한 기능에 맞춘 전용 보안 역할을 부여합니다. 역할을 신원에 연결하며, 에이전트가 수행한 동작을 감사해 데이터 접근과 변경을 추적하도록 설명합니다.

에이전트와 사람 사용자 모두에 보안·준수 정책을 적용할 기반이 되지만, 전용 신원을 만들었다는 사실만으로 역할 설계가 자동으로 안전해지는 것은 아닙니다.

## 구현 전에 정할 사항

조회만 필요한 에이전트와 레코드를 바꾸는 에이전트의 역할을 분리하고, 필요한 테이블·작업 범위를 먼저 정의하는 것이 좋습니다. 또한 감사 기록에서 신원과 실행 목적을 연결해 볼 수 있는지 확인하세요. 이는 도입 권고이며 원문이 세부 설정 절차까지 제공하는 것은 아닙니다.

프로비저닝 조건은 [Dataverse agent users 문서](https://learn.microsoft.com/en-us/power-platform/admin/create-users#agent-users-preview)를 출발점으로 확인할 수 있습니다.

## 일정 해석

로드맵 표기는 프리뷰 **2026년 6월**, GA **2026년 8월**입니다. 다만 연결 문서의 앵커에는 `preview`가 남아 있으므로 로드맵의 날짜와 문서·환경의 실제 상태를 구분해야 합니다. 이 글은 해당 로드맵의 설명을 정리한 것이며 별도 최신 문서의 GA 확인을 대신하지 않습니다.

> 출처: 원문 ID **RM576843**, [MC 아카이브](https://mc.merill.net/message/RM576843), [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap?id=576843). 실제 출시 일정·기능은 변경될 수 있습니다.
