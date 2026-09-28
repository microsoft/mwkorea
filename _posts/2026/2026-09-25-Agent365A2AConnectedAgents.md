---
title: "Copilot 선언형 에이전트에 A2A 연결: Agent 365 에이전트를 함께 쓰는 방법"
date: 2026-09-25T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Agent365
  - A2A
  - DeclarativeAgents
  - Governance
excerpt: "Microsoft 365 선언형 에이전트가 Agent2Agent 프로토콜을 지원하는 Agent 365 에이전트와 연결됩니다. 개발자가 알아야 할 연결 방식과 관리자의 설치·승인 절차를 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 선언형 에이전트에 A2A 연결: Agent 365 에이전트를 함께 쓰는 방법

하나의 Copilot 에이전트가 모든 업무를 직접 처리해야 할까요? Microsoft의 MC1478975 공지는 **Agent2Agent(A2A) 프로토콜을 구현한 Microsoft Agent 365 에이전트를 선언형 에이전트의 연결된 에이전트로 사용할 수 있다**고 안내합니다.

Microsoft 365 Agents Toolkit으로 에이전트를 만드는 개발자에게는 연결 대상이 넓어지는 변화입니다. 조직 도입 담당자에게는 에이전트 간 연결을 사용자가 임의로 추가하는 것이 아니라, 관리 센터에서 검토하고 승인한다는 점이 중요합니다.

---

## OpenAPI·MCP에 A2A 연결이 더해집니다

이번 지원은 기존 OpenAPI와 Model Context Protocol(MCP) 서버 연결을 대체하지 않습니다. 여기에 A2A를 지원하는 에이전트 연결이 추가되어, 자연어 상호작용과 더 복잡한 업무 흐름을 구성할 선택지가 늘어납니다.

대상은 **A2A를 지원하고 조직이 승인한 Microsoft Agent 365 에이전트**입니다. 모든 외부 에이전트가 별도 검토 없이 자동으로 연결된다는 뜻은 아닙니다.

## 관리자의 설치와 연결 검토가 선행됩니다

1. Microsoft 365 관리 센터의 **All agents**에서 사용하려는 A2A 지원 Agent 365 에이전트를 검토하고 설치합니다.
2. 선언형 에이전트 상세 화면의 **Connected agents** 탭에서 연결된 에이전트를 확인합니다.
3. 고객 데이터와 상호작용하는 방식과 조직 정책을 검토한 뒤 사용을 승인하고, 필요한 사용자에게 접근을 제공합니다.

![Microsoft 365 관리 센터의 연결된 에이전트 검토 화면](/mwkorea/assets/images/2026-09-25-Agent365A2AConnectedAgents/image1.png)

**최종 사용자는 A2A 지원 Microsoft Agent 365 에이전트를 직접 설치할 수 없습니다.** 따라서 개발팀의 기능 구현 계획과 관리자 승인 프로세스를 함께 준비해야 합니다.

## 배포 일정은 공지 시점의 계획입니다

원문은 Worldwide 일반 공급(GA) 배포가 **2026년 8월 말 시작되어 9월 말 완료될 예정**이라고 설명합니다. Microsoft 내부 배포(MSIT)는 원문 시점에 이미 제공 중입니다.

이 글의 날짜는 피드 발행 시각을 한국 시간으로 변환한 날짜이며, 기능의 최초 출시일을 뜻하지 않습니다. 특히 이번 공지는 배포 시작 예정일보다 늦게 게시되었으므로, 실제 테넌트의 제공 여부는 관리 센터에서 확인해야 합니다.

## 도입 체크포인트

한국 기업의 도입 관점에서는 연결된 에이전트가 접근하는 데이터, 승인 책임자, 사용자 할당 범위를 먼저 정리하는 것이 좋습니다. 이는 원문의 거버넌스 권고를 실무에 적용한 점검 항목이며, 이 공지가 별도의 데이터 접근 권한을 자동 부여한다고 해석해서는 안 됩니다.

개발자는 연결 기능만 시연하기보다 관리자에게 **어떤 에이전트와 왜 연결되는지** 설명할 자료를 함께 준비하세요. 선언형 에이전트의 활용 범위가 넓어질수록 연결 대상까지 포함한 검토가 중요해집니다.

> 출처: [MC1478975 — Microsoft 365 Copilot: Use Microsoft Agent 365 agents as connected agents in declarative agents](https://mc.merill.net/message/MC1478975)  
> [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 명시되어 있지 않습니다.  
> 실제 출시 일정·기능은 변경될 수 있습니다.
