---
title: "Jira·Confluence를 사용자가 직접 연결한다: Self-serve 동기화 커넥터"
date: 2026-08-21T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotConnectors
  - Jira
  - Confluence
  - MicrosoftSearch
  - Governance
  - Roadmap
excerpt: "Self-serve 동기화 커넥터로 사용자가 Jira, Confluence Cloud 같은 외부 데이터 소스를 직접 Microsoft 365 Copilot에 연결할 수 있습니다. 본인 자격 증명과 권한으로 이미 접근 가능한 콘텐츠만 동기화되며, 관리자는 단계적 롤아웃·표시 관리·커넥터 비활성화로 통제권을 유지합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Jira·Confluence를 사용자가 직접 연결한다: Self-serve 동기화 커넥터

"Copilot이 우리 팀 Jira 티켓도 좀 봐 주면 좋겠는데요."

Copilot을 도입한 조직에서 자주 나오는 요청입니다. 그런데 실제로 연결하려면 IT 부서가 테넌트 수준에서 커넥터를 구성하고, 인증을 설정하고, 권한 매핑을 검토해야 합니다. 팀 하나의 요청 때문에 이 과정을 돌리기는 부담스럽고, 그러다 보니 요청은 쌓이는데 처리는 안 되는 상황이 반복됩니다.

메시지 센터 공지 **RM568788**로 안내된 **Self-serve sync connectors**는 이 순서를 바꿉니다. **사용자가 자기 데이터 소스를 직접 연결**하고, 관리자는 그 위에서 통제권을 유지하는 구조입니다.

---

## 무엇이 달라지나요

Microsoft가 공지에서 밝힌 내용입니다.

> Self-serve 동기화 커넥터를 사용하면 사용자가 **Jira, Confluence Cloud** 같은 자신의 외부 데이터 소스를 Microsoft 365 Copilot에 안전하게 연결할 수 있습니다. **본인의 자격 증명과 권한을 사용해** 이미 접근 권한이 있는 콘텐츠를 동기화하며, 해당 콘텐츠는 **Copilot Chat과 Microsoft Search**에서 검색 가능해집니다. 관리자는 **단계적 롤아웃, 표시 관리, 커넥터 비활성화**를 포함한 테넌트 수준 제어로 감독을 유지합니다.

### 핵심 세 가지

**1. 사용자가 직접 연결한다**

IT 티켓을 열고 기다릴 필요 없이 사용자가 스스로 외부 소스를 연결합니다. 명시된 예시는 **Jira**와 **Confluence Cloud**입니다.

**2. 본인 권한 범위 안에서만 동기화된다**

**사용자 본인의 자격 증명(credentials)과 권한(permissions)** 을 사용합니다. 즉 **원래 볼 수 없던 데이터가 Copilot을 통해 보이게 되는 일은 없습니다.** 이미 접근 권한이 있는 콘텐츠만 동기화 대상입니다.

**3. 관리자 통제권은 유지된다**

사용자가 자유롭게 연결한다고 해서 관리자가 손을 놓는 것은 아닙니다. 테넌트 수준에서 다음을 제어합니다.

| 제어 항목 | 내용 |
|---|---|
| **단계적 롤아웃(staged rollout)** | 일부 그룹부터 순차적으로 열어 줄 수 있음 |
| **표시 관리(visibility management)** | 어떤 커넥터를 사용자에게 노출할지 관리 |
| **커넥터 비활성화(connector disablement)** | 특정 커넥터를 끌 수 있음 |

### 검색 가능해지는 범위

동기화된 콘텐츠는 두 곳에서 찾을 수 있게 됩니다.

- **Copilot Chat**
- **Microsoft Search**

즉 Copilot에게 물어보는 것뿐 아니라 일반 검색에서도 결과에 반영됩니다.

---

## Federated 커넥터와는 무엇이 다른가

며칠 전 안내된 **Federated Copilot Connectors**(RM569212, MCP 기반 실시간 조회)와 이름이 비슷해 헷갈릴 수 있습니다. 두 기능은 접근 방식이 다릅니다.

| 구분 | Self-serve **동기화** 커넥터 | Federated 커넥터 |
|---|---|---|
| 데이터 처리 | **동기화(synchronize)** | 실시간 조회, 저장·인덱싱 없음 |
| 프로토콜 | 커넥터 방식 | Model Context Protocol(MCP) |
| 연결 주체 | **사용자 본인** | 사용자 본인 ID로 접근 |
| 명시된 예시 | Jira, Confluence Cloud | 서드파티 소스 일반 |
| 검색 반영 | Copilot Chat + **Microsoft Search** | Researcher 에이전트 + M365 Chat |

두 기능 모두 **사용자 권한을 승계**한다는 공통점이 있지만, 하나는 콘텐츠를 동기화해 검색 대상으로 만들고 다른 하나는 저장 없이 실시간으로 가져옵니다. 조직 상황에 따라 선택지가 넓어진 셈입니다.

---

## 왜 의미가 있나요

한국의 개발·기획 조직에서 Jira와 Confluence는 사실상 표준에 가깝습니다. 그런데 이 안에 쌓인 정보 — 이슈 이력, 회의록, 기획 문서, 기술 결정 기록 — 는 Copilot이 볼 수 없는 영역이었습니다.

Self-serve 방식이 열리면 이런 활용이 가능해집니다.

- **이슈 맥락 파악** — "이 기능 관련해서 지금까지 어떤 이슈가 있었지?"를 Copilot에게 물어봄
- **문서 연계 검색** — Confluence 기획서와 SharePoint 자료를 한 번에 찾음
- **팀 단위 시범 도입** — 전사 커넥터 구성 없이 관심 있는 팀부터 먼저 활용

특히 **IT 부서의 병목 없이 팀 단위로 시작할 수 있다**는 점이 실무적으로 큽니다.

---

## 일정

| 구분 | 시점 |
|---|---|
| 미리 보기(Preview) | 2026년 8월 |
| 정식 출시(GA) | 2026년 9월 |

미리 보기가 이미 시작되는 시점이고, 정식 출시까지 한 달 남짓입니다. 준비를 서둘러야 하는 일정입니다.

---

## 도입 담당자를 위한 체크포인트

- **먼저 정책을 정하세요**: 사용자가 직접 연결하는 구조이므로, **어떤 커넥터를 허용할지** 미리 정해 두지 않으면 나중에 정리하기 어렵습니다. 표시 관리 기능으로 노출 범위를 통제할 수 있으니 출시 전에 목록을 확정하세요.
- **단계적 롤아웃 활용**: 전사에 한 번에 열지 말고 **파일럿 그룹부터** 시작하세요. 단계적 롤아웃이 기본 제공되므로 이를 활용해 사용 패턴과 이슈를 먼저 확인하는 것이 안전합니다.
- **권한 승계의 의미 이해**: 사용자 본인 권한으로 동기화되므로 **원본 시스템의 권한 설정이 그대로 반영**됩니다. Jira·Confluence의 권한이 느슨하다면 Copilot을 통한 노출 범위도 그만큼 넓어집니다. **원본 시스템 권한 정리를 선행**하세요.
- **Microsoft Search 반영 고려**: 동기화된 콘텐츠는 Copilot Chat뿐 아니라 **Microsoft Search에도 나타납니다.** 검색 결과에 외부 시스템 콘텐츠가 섞이는 것에 대한 사용자 안내가 필요할 수 있습니다.
- **비활성화 절차 준비**: 커넥터 비활성화 기능이 제공됩니다. 문제가 생겼을 때 **누가 어떤 기준으로 끌 것인지** 절차를 미리 정해 두세요.
- **라이선스 전제**: 공지의 제품 분류에 **Microsoft Copilot (Microsoft 365)** 가 포함되어 있습니다.

---

## 마무리

Copilot에 외부 데이터를 붙이는 일은 지금까지 **IT 부서의 프로젝트**였습니다. 이번 변화는 그 일부를 **사용자의 선택**으로 옮깁니다. 대신 관리자에게는 단계적 롤아웃·표시 관리·비활성화라는 통제 수단을 남겨 두었습니다.

권한을 넓히는 것이 아니라 **이미 가진 권한 안에서 연결 경로를 열어 주는 것**이라는 점이 이 설계의 핵심입니다. 미리 보기가 2026년 8월, 정식 출시가 9월이니 지금이 정책을 정리할 시점입니다.

---

> **출처**
>
> - 원문 ID: **RM568788** — *Microsoft Copilot (Microsoft 365): Self-serve sync connectors*
> - 메시지 센터: [https://mc.merill.net/message/RM568788](https://mc.merill.net/message/RM568788)
> - Microsoft 365 로드맵: [https://www.microsoft.com/microsoft-365/roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
