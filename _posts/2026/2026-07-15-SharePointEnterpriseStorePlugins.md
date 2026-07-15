---
title: "SharePoint Copilot이 기업용 플러그인을 불러옵니다: Skills·MCP Server를 한 번에 배포"
date: 2026-07-15T00:00:00 KST
categories:
  - Copilot
tags:
  - SharePoint
  - CopilotInSharePoint
  - EnterpriseStore
  - Plugins
  - AgentSkills
  - MCP
  - Governance
excerpt: "Copilot in SharePoint가 조직의 Enterprise Store에 게시된 플러그인을 지원합니다. Skills, MCP Servers 등 여러 기능을 하나의 플러그인으로 묶어 SharePoint를 포함한 에이전틱 제품에 일관되게 제공하고 Microsoft 365 관리자가 통제할 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# SharePoint Copilot이 기업용 플러그인을 불러옵니다: Skills·MCP Server를 한 번에 배포

조직 고유의 업무 능력을 Copilot 제품마다 따로 구현하면 유지관리와 거버넌스가 어려워집니다. 같은 접근성 규칙이나 업무 절차가 SharePoint·다른 에이전틱 제품에서 서로 다르게 동작할 수도 있습니다.

Copilot in SharePoint가 **Microsoft 365 Enterprise Store의 플러그인**을 지원합니다.

> **한 줄 요약**
> Skills, MCP Servers 등 여러 능력을 플러그인 하나로 묶어 조직에 배포하고, SharePoint Copilot에서 바로 사용하며, Microsoft 365 관리자가 통제할 수 있습니다.

---

## 플러그인에 포함할 수 있는 것

로드맵 공지에 따르면 플러그인은 다음과 같은 기능을 묶을 수 있습니다.

- Skills
- MCP Servers
- Copilot을 확장하는 기타 기능

관리자가 테넌트 전체에 설치한 플러그인이나 사용자가 Enterprise Store에서 추가한 플러그인은 Copilot in SharePoint에서 직접 동작합니다.

## 조직 전체에 일관된 기능 제공

예를 들어 조직이 전사 접근성 플러그인을 한 번 게시하면 SharePoint Copilot을 포함한 여러 에이전틱 제품에서 같은 접근성 경험을 제공할 수 있습니다.

이 방식은 다음 문제를 줄입니다.

- 제품별 중복 구현
- 서로 다른 버전과 정책
- 분산된 배포·업데이트
- 개별 사용자의 임의 확장

## 거버넌스

Enterprise Store의 플러그인은 Microsoft 365 관리자의 통제를 받습니다. 기술적 기능뿐 아니라 다음 운영 기준이 중요합니다.

- 누가 플러그인을 게시할 수 있는가
- 어떤 사용자·그룹에 제공할 것인가
- 포함된 MCP Server와 Tool이 어떤 데이터에 접근하는가
- 버전 업데이트와 철회 절차는 무엇인가
- 조직 전체 설치와 개인 추가를 어떻게 구분할 것인가

## 출시 일정

| 구분 | 일정 |
|---|---|
| Preview | 2026년 8월 |
| GA | 2026년 12월 |
| 대상 | Copilot in SharePoint |

## 도입 관점 체크포인트

- 전사 공통으로 재사용할 Skills와 MCP Servers를 먼저 식별합니다.
- 플러그인 검토·승인·게시·업데이트 책임자를 지정합니다.
- MCP Server의 인증 방식과 최소 권한을 검토합니다.
- 테스트 그룹에서 SharePoint와 다른 에이전틱 제품의 동작 일관성을 확인합니다.
- 플러그인 중단 시 업무 영향과 Rollback 방안을 마련합니다.

## 마무리

Enterprise Store 플러그인은 조직 고유의 Copilot 역량을 제품별로 반복 구축하지 않고 일관되게 배포하는 기반입니다. Skills와 MCP Servers를 함께 패키징할 수 있는 만큼, 앱 배포뿐 아니라 에이전트 능력의 공급망·보안·수명주기 관리 관점에서 준비해야 합니다.

---

> ※ 본 글은 Microsoft 365 메시지 센터/로드맵 공지(**RM567669**)를 바탕으로 정리했습니다. 원문은 [Message Center Archive](https://mc.merill.net/message/RM567669)와 [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)에서 확인할 수 있으며, 실제 출시 일정·기능은 변경될 수 있습니다.
