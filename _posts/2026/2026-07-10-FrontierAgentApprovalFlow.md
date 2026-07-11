---
title: "차단된 Copilot 에이전트, 이제 사용자가 직접 요청하고 관리자가 승인합니다"
date: 2026-07-10T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Frontier
  - AdminCenter
  - CopilotControlSystem
  - AgentGovernance
  - Roadmap
excerpt: "Microsoft 365 admin center에서 Frontier 프로그램과 Microsoft 제작 에이전트에 대한 사용자 요청·승인 흐름이 추가됩니다. 조직 정책으로 차단된 에이전트를 사용자가 직접 요청하면, 관리자가 승인·거부를 결정할 수 있게 됩니다. GA는 2026년 7월 예정입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 차단된 Copilot 에이전트, 이제 사용자가 직접 요청하고 관리자가 승인합니다

조직 정책 때문에 특정 에이전트가 차단되어 있으면, 사용자는 보통 IT 담당자에게 이메일을 보내거나 티켓을 등록하는 수밖에 없었습니다. 이런 요청·승인 과정이 표준화되어 있지 않으면, 정작 필요한 사람이 필요한 에이전트를 쓰기까지 시간이 오래 걸리기 마련입니다.

이번 Microsoft 365 로드맵 업데이트는 이 과정을 **admin center 안에서 표준화된 흐름**으로 만듭니다.

> **이 글의 한 줄 요약**
> Microsoft 365 admin center의 Copilot Control System에서 관리자는 Frontier 프로그램 에이전트와 Microsoft 제작 에이전트의 전체 인벤토리를 확인할 수 있고, 사용자는 조직 정책으로 차단된 에이전트를 직접 요청할 수 있으며, 관리자는 이 요청을 승인하거나 거부할 수 있습니다. GA는 **2026년 7월** 예정입니다.

---

## 무엇이 새로워지나

관리자 입장에서 **Frontier 프로그램**에 속한 에이전트들은 Microsoft 365 admin center를 통해 관리할 수 있게 됩니다. Copilot Control System의 **agents & connectors** 탭 아래에 나열되어, 조직 전체의 에이전트 인벤토리를 한눈에 확인할 수 있습니다. Microsoft가 만들고 Frontier 프로그램을 통해 제공되는 에이전트는 **Agent Store**에도 표시됩니다.

이번 업데이트의 핵심은 **사용자 요청 기능**입니다. 조직 정책으로 인해 특정 에이전트가 차단되어 있는 경우, 사용자는 해당 에이전트를 직접 요청할 수 있습니다. 관리자는 이 요청을 검토해 **승인하거나 거부**할 수 있는 권한을 갖게 됩니다.

## 왜 중요한가

에이전트 도입이 늘어날수록, "이 에이전트를 써도 되는지" 판단하는 절차가 표준화되어 있지 않으면 관리 부담이 커집니다. 이번 업데이트는 다음 두 가지를 동시에 만족시킵니다.

- **사용자 편의성**: 필요한 에이전트를 별도 채널 없이 admin center 흐름 안에서 바로 요청
- **관리자 통제력**: 전체 에이전트 인벤토리를 한눈에 파악하고, 요청 건별로 승인·거부를 결정

이 공지에는 `#copilotcontrolsystem` 태그가 붙어 있어, Copilot 거버넌스 체계의 일환으로 다뤄지고 있음을 알 수 있습니다.

## 활용 시나리오

- **신규 에이전트 시범 도입**: 특정 부서에서 새로운 Frontier 에이전트가 필요할 때, 담당자가 직접 요청하고 IT 관리자가 빠르게 승인
- **정책 위반 사전 방지**: 조직 정책상 차단된 에이전트라도, 정당한 사유가 있는 경우 요청·승인 절차를 거쳐 예외적으로 허용
- **에이전트 인벤토리 감사**: admin center에서 조직 내 모든 Frontier·Microsoft 제작 에이전트 현황을 정기적으로 점검

## 출시 일정

| 구분 | 내용 |
|------|------|
| **General Availability (GA)** | 2026년 7월 (CY2026) |
| **위치** | Microsoft 365 admin center → Copilot Control System → Agents & connectors |
| **적용 대상** | Frontier 프로그램 에이전트, Microsoft 제작 에이전트 |

## 도입 관점 체크포인트

- 에이전트 요청을 승인할 관리자·역할을 사전에 지정하고, 승인 기준(SLA, 검토 항목)을 문서화
- Agent Store에 노출되는 에이전트 범위와 조직 정책 간의 정합성 재확인
- 요청·승인 이력을 추적할 수 있는 감사(audit) 체계와 연계 여부 확인

## 마무리

에이전트 사용 요청이 이메일이나 티켓 같은 비정형 채널이 아니라 admin center 안에서 표준화된 흐름으로 처리되면, 관리자와 사용자 모두에게 예측 가능한 프로세스가 생깁니다. 2026년 7월 GA를 앞두고 조직 내 승인 정책을 미리 정비해 두시길 권합니다.

---

> ※ 본 글은 Microsoft 365 메시지 센터/로드맵 공지(**RM494809**)를 바탕으로 정리했습니다. 원문은 [Message Center Archive](https://mc.merill.net/message/RM494809)와 [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)에서 확인할 수 있으며, 실제 출시 일정과 기능은 변경될 수 있습니다.
