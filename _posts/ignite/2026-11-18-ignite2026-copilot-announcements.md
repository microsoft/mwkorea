---
title: "Ignite 2026 Copilot 발표 현황: GA부터 Frontier·Public Preview까지"
date: 2026-11-18T17:20:00+09:00
categories:
  - ignite
tags:
  - AI
  - Microsoft Ignite
  - Copilot
  - Agent365
  - FinOps
excerpt: "Ignite 2026에서 Copilot 제품별 제공 단계가 어디까지 이동했는지 정리했습니다. Home, Office in Copilot, Managed Runtime의 GA와 Code, Autopilot, Today, Work IQ, 에이전트 기능의 Frontier·Preview 상태를 한눈에 살펴봅니다."
header:
  overlay_image: /assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
---

Microsoft Ignite 2026에서는 Copilot의 기능 이름보다 **어떤 사용 단계로 제공되는지**를 살펴보는 일이 더 중요합니다. 같은 발표 안에도 일반 제공(GA), Frontier 공개 제공, Frontier 비공개 제공, Public Preview가 함께 있기 때문입니다.

이 글은 아래 안내 이미지에서 **2026년 11월 17일 Ignite 시점의 상태**와 오른쪽 추가 발표만 정리합니다. 이전 시점인 9/25 상태는 비교하지 않습니다.

![Ignite 2026 Copilot 제품별 발표 현황](/mwkorea/assets/images/2026-11-18-IgniteCopilotAnnouncements/overview.png)

---

## Ignite 시점 Copilot 제품 제공 현황

| 제품·기능 | Ignite 2026 기준 상태 | 확인할 포인트 |
|---|---|---|
| Home: Chat + Cowork | **GA** | Copilot 사용 경험의 중심 경로로 전환 |
| Office in Copilot | **GA** | Office 작업과 Copilot 연결이 정식 제공 단계로 이동 |
| Code | **GA 예정 — 2026년 12월** | Ignite 당일 바로 제공되는 것으로 오해하지 않도록 일정 확인 |
| Autopilot | **Frontier Public — 배포 시작** | Frontier 대상 공개 단계지만 테넌트별 순차 적용 가능 |
| Copilot Managed Runtime | **GA** | Copilot 실행 기반을 정식 운영 환경으로 전환 |
| Today | **Frontier Private** | 일반 사용자나 모든 Frontier 고객에게 공개된 상태는 아님 |
| Hybrid intelligence: context, actions | **Public Preview** | 업무 맥락과 행동을 함께 연결하는 기능의 공개 평가 단계 |
| Dynamics 365 / Sales Plugin in Copilot | **Public Preview** | CRM·영업 업무 연결은 프리뷰 조건에서 검증 |
| MCS: Agents w/ accounts | **Frontier Public** | 계정 연결이 필요한 Copilot Studio 에이전트가 Frontier 공개 단계로 이동 |

가장 눈에 띄는 변화는 **Home, Office in Copilot, Copilot Managed Runtime이 GA**라는 점입니다. 반면 Code, Autopilot, Today, Hybrid intelligence, 플러그인과 계정 연결 에이전트는 제공 일정과 대상이 서로 다릅니다.

## GA라도 모든 기능이 즉시 같은 날 열리는 것은 아님

Code의 **2026년 12월 GA** 표기는 특히 확인이 필요합니다. Ignite에서 계획을 발표했다고 모든 사용자가 행사 당일 바로 사용할 수 있는 것은 아닙니다. 조직의 테넌트가 Frontier인지, 정식 배포를 받았는지, 제품별 지원 지역과 라이선스가 일치하는지를 별도로 확인해야 합니다.

Autopilot도 Frontier Public 배포가 시작되는 단계입니다. “Frontier Public”은 일반 제공이 아니라 **Frontier 프로그램 범위에서 공개 테스트·이용이 시작되는 상태**로 읽는 편이 안전합니다.

Today는 아직 Frontier Private입니다. Public Preview와 혼동하면 고객이 없는 기능을 탐색하려 하거나, 외부 사용자에게 시연을 약속하는 문제가 생길 수 있습니다.

## 오른쪽 추가 발표도 함께 봐야 하는 이유

슬라이드 오른쪽은 새로운 업무 경험뿐 아니라 Copilot과 에이전트를 운영하는 데 필요한 비용, 분석, 협업, 자산, 개발 통제를 묶어서 보여줍니다.

### 1. FinOps for AI: 사용량과 비용을 모델 수준에서 보기

FinOps for AI 업데이트는 AI 사용을 총액 하나로 보는 데서 벗어나 다음 정보를 확인할 수 있도록 확장합니다.

- 모델 수준의 사용량·지출 인사이트
- 위임 접근 제어
- 사용자 지정 보고
- 부서별 비용 배부와 차지백

같은 Copilot 라이선스를 사용해도 어떤 팀이 어떤 모델과 에이전트를 사용했는지 구분해야 비용 정책을 설계할 수 있습니다. 제공 상태는 기능마다 다르므로 **사용량 인사이트, 접근 위임, 비용 배부 기능을 각각 확인**해야 합니다.

### 2. Agent 365 Business Analytics: 지출보다 가치까지 보기

Agent 365 Business Analytics는 **Frontier Public** 단계로 소개됐습니다. 단순한 비용 보고서가 아니라 다음 항목을 함께 검토하는 방향입니다.

- 가치 인사이트
- 최적화 제안
- 비용·사용량 예측
- 에이전트형 Q&A

사용량과 비용을 확인하는 것만으로는 도입 효과를 판단하기 어렵습니다. 어떤 업무에서 사용됐고 어떤 가치가 발생했는지를 연결해야 하는데, Agent 365 Business Analytics가 이 영역을 담당합니다.

자세한 내용은 [Ignite 2026의 Agent 365]({{ '/copilot/Agent365IgniteUpdates/' | relative_url }})와 [Agent 365 Business Analytics 공개 프리뷰]({{ '/copilot/AgentBusinessAnalytics/' | relative_url }})에서 이어서 확인할 수 있습니다.

### 3. Copilot Workspaces: 개인 대화에서 팀 협업으로

**Copilot Workspaces의 새 경험은 Private Preview**입니다. Home이나 Today처럼 개인이 Copilot을 시작하는 경험과 달리, Workspaces는 여러 사람이 에이전트와 공유된 업무 맥락을 중심으로 협업하는 공간을 지향합니다.

따라서 단일 사용자 데모보다 **공유 권한, 문서 소유권, 팀의 역할, 에이전트의 접근 범위**를 함께 설계해야 합니다.

### 4. Microsoft 365 Resources for Agents

Microsoft 365 Resources for Agents가 **Frontier Public**으로 소개됐습니다. 에이전트를 만들 때마다 파일, 문서, 정책, 업무 데이터 연결 방식을 따로 구성하는 부담을 줄이고, 업무에 필요한 Microsoft 365 자원을 에이전트 실행 환경과 연결하려는 방향입니다.

도입 검토 시에는 리소스를 연결할 수 있는지만 보지 말고, 다음도 확인해야 합니다.

- 에이전트가 접근 가능한 범위
- 사용자 권한 상속 방식
- 민감 정보와 보존 정책
- 사용 기록과 감사 가능성

### 5. Plugin Registry와 Work IQ MCP 업데이트

**Plugin registry, functional plugins, Work IQ MCP 업데이트는 GA**로 표시됐습니다. 에이전트가 외부 기능과 도구를 연결할 때 필요한 기반 요소가 정식 제공 단계로 이동한 것입니다.

여기서 중요한 변화는 연결 수가 아니라 **등록된 도구를 조직 정책에 맞춰 찾고 사용하고 관리할 수 있는지**입니다. MCP나 플러그인을 연결할 수 있어도 어떤 테넌트와 권한에서 허용되는지는 별도의 관리 정책이 필요합니다.

Work IQ의 구체적인 확장과 거버넌스는 [Ignite 2026 Work IQ 업데이트]({{ '/copilot/WorkIQIgniteUpdates/' | relative_url }})에서 자세히 설명합니다.

### 6. Copilot Studio 에이전트의 GitHub 버전 관리와 공동 제작

MCS, 즉 Copilot Studio 에이전트가 **GitHub를 사용한 버전 관리와 공동 제작을 GA로 지원**합니다. 여러 제작자가 같은 에이전트의 변경을 리뷰하고 이력을 남겨야 할 때 중요한 변화입니다.

가능해지는 운영 방식은 다음과 같습니다.

- YAML 변경을 GitHub에서 검토
- 브랜치와 Pull Request로 변경 이력 관리
- 여러 제작자의 공동 작업
- 환경별 배포 전 변경 비교

다만 GitHub 연동 자체가 개발·검증·운영 환경 분리와 배포 승인을 대신하지는 않습니다. 기존 Copilot Studio ALM 기준과 함께 사용해야 합니다.

## 역할별로 확인할 우선순위

| 역할 | 먼저 확인할 항목 |
|---|---|
| Copilot 도입 담당자 | Home, Office in Copilot, Managed Runtime GA 범위 |
| 에이전트 제작자 | Hybrid intelligence, MCS accounts, Plugin Registry, Work IQ MCP |
| IT·보안 관리자 | Frontier 범위, 계정 연결, 리소스 접근, 도구 정책 |
| FinOps 담당자 | 모델별 지출, 위임 접근, 보고서·비용 배부, Business Analytics |
| 팀 협업 담당자 | Copilot Workspaces Private Preview 참여 여부 |
| 개발·ALM 담당자 | Copilot Studio의 GitHub 버전 관리와 공동 제작 |

## 도입 전 체크리스트

1. 기능 이름과 제공 상태를 정확히 구분합니다.
2. GA·Public Preview·Frontier Public·Frontier Private를 혼동하지 않습니다.
3. Code의 12월 GA처럼 **발표일과 실제 제공일**을 따로 확인합니다.
4. Frontier 또는 프리뷰 기능이 테넌트에 배포됐는지 확인합니다.
5. 지역, 라이선스, 관리자 정책, 보안 정책을 점검합니다.
6. 사용자에게 기능을 안내하기 전에 직접 파일럿 테스트를 진행합니다.

> 이 글은 이미지에 표시된 Ignite 2026 시점 상태를 중심으로 정리한 것입니다. 제품별 최신 제공 단계와 일정은 지역·테넌트·라이선스에 따라 달라질 수 있으므로 [Microsoft Ignite 2026 Book of News](https://news.microsoft.com/events/ignite/2026/book-of-news/)와 각 제품 공지를 최종 기준으로 확인하세요.

## 마무리

Ignite 2026 Copilot 발표는 사용자 경험만 넓힌 것이 아닙니다. GA로 이동하는 핵심 경험, Frontier와 Preview에서 검증 중인 에이전트 기능, 비용과 가치를 보는 Agent 365, 조직 맥락을 연결하는 Work IQ, 개발 이력을 관리하는 GitHub 연동까지 **사용자·관리자·개발자 모두를 위한 운영 기반**을 함께 보여줍니다.

전체 발표 구조를 먼저 이해하려면 [Ignite 2026 Book of News 한눈에 보기]({{ '/ignite/ignite2026-book-of-news/' | relative_url }})를, 한국어 키노트 영상을 보려면 [Ignite 2026 한국어 더빙 영상]({{ '/ignite/ignite2026-korean-keynote-videos/' | relative_url }})을 함께 참고하세요.
