---
title: "Dynamics 365 Sales 도구와 워크플로가 Copilot Cowork로 들어온다"
date: 2026-10-01T00:00:00 KST
categories:
  - Copilot
tags:
  - Dynamics365Sales
  - CopilotCowork
  - MCP
  - SalesAgent
  - Microsoft365Copilot
excerpt: "Copilot Cowork의 Sales 플러그인이 Dynamics 365 Sales 컨텍스트와 작업을 확장합니다. 영업 담당자는 업무 흐름을 벗어나지 않고 데이터를 조회하고 지원되는 작업을 실행할 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Dynamics 365 Sales 도구와 워크플로가 Copilot Cowork로 들어온다

Microsoft가 Copilot Cowork용 Sales 플러그인에 Dynamics 365 Sales의 컨텍스트, 실행 작업, 안내형 워크플로를 확대합니다. 영업 담당자는 Cowork에서 작업을 이어 가면서 고객과 영업 기회를 확인하고 지원되는 후속 작업을 수행할 수 있습니다.

핵심은 단순 요약이 아니라 **Dynamics 365 MCP 서버가 공개한 도구를 호출해 실제 영업 컨텍스트를 조회하고 작업하는 구조**입니다.

---

## Sales 플러그인의 구성

Cowork에는 이미 기본 Sales skills가 제공되고 있습니다. 이번 업데이트는 이 기술을 Sales 플러그인에 포함해 다음 범위를 넓힙니다.

- Dynamics 365 Sales 데이터와 컨텍스트 조회
- 지원되는 영업 작업 실행
- 반복 영업 흐름을 안내형 워크플로로 진행
- Dynamics 365 Sales 화면으로 전환하는 횟수 감소

기본 Sales skills는 Dynamics 365 MCP 서버를 통해 게시된 도구를 사용합니다. 따라서 어떤 데이터와 작업이 노출되는지는 MCP 도구와 Dynamics 365 권한 범위에 의해 결정됩니다.

## 관리와 배포

업데이트된 Sales 플러그인은 Sales 앱의 **MOS 패키지**를 통해 제공됩니다. 관리자는 패키지를 기준으로 기능을 배포하고 관리할 수 있으므로, 개인별 임의 연결보다 조직 차원의 통제가 용이합니다.

도입 시에는 다음을 확인하는 것이 좋습니다.

- Cowork 사용자에게 필요한 Dynamics 365 Sales 라이선스와 권한
- MCP 서버가 공개한 도구 및 허용된 작업 범위
- 읽기 작업과 변경 작업의 승인·감사 정책
- 테스트 환경에서의 플러그인 패키지 배포 절차

## 제공 일정

GA는 **2026년 9월**로 안내되었습니다. 이미 배포 시점에 도달한 기능이므로 테넌트별 실제 제공 여부와 MOS 패키지 상태를 관리 센터에서 확인해야 합니다.

영업팀 파일럿에서는 계정 조회, 영업 기회 업데이트, 후속 작업처럼 빈도가 높은 시나리오부터 검증하고, Cowork가 실행한 변경도 기존 Dynamics 365 감사 체계에서 추적되는지 확인하는 것이 중요합니다.

> **출처**: 원문 ID **RM573373** · [mc.merill.net 원문](https://mc.merill.net/message/RM573373) · [Microsoft 365 Roadmap 573373](https://www.microsoft.com/en-us/microsoft-365/roadmap?featureid=573373)  
> 실제 출시 일정·기능은 변경될 수 있습니다.
