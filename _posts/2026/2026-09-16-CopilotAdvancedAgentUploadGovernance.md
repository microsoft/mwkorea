---
title: "고급 Copilot 에이전트 업로드, 이제 Entra 그룹으로 통제하세요"
date: 2026-09-16T00:00:00 KST
categories:
  - Copilot
tags:
  - Agent
  - Governance
  - EntraID
  - MCP
excerpt: "고급 Copilot 에이전트와 플러그인 패키지의 사용자 업로드 권한을 관리자 설정으로 제한할 수 있습니다. actions 또는 MCP 서버를 포함한 패키지가 대상이며, 기본 패키지와 기존 에이전트 전체를 차단하는 설정은 아닙니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 고급 Copilot 에이전트 업로드, 이제 Entra 그룹으로 통제하세요

에이전트가 외부 도구를 호출하고 MCP 서버와 연결되기 시작하면, 누가 확장 패키지를 올릴 수 있는지가 중요한 관리 지점이 됩니다. Microsoft는 **고급 에이전트와 플러그인의 사용자 업로드 권한**을 제한하는 관리 설정을 도입합니다.

2026년 9월 15일 업데이트된 MC1472007은 전체 허용뿐 아니라 특정 사용자·Microsoft Entra ID 그룹만 허용하거나 모두 차단하는 선택지를 설명합니다. 파일 날짜는 RSS의 pubDate를 한국 시간으로 변환한 기준이며, 아래 일정은 해당 공지 시점의 계획입니다.

---

## 어떤 패키지가 고급 에이전트인가요?

공지의 정의는 구체적입니다. **actions 또는 MCP 서버가 있는 Declarative Agent를 포함한 패키지**가 고급 패키지입니다. 나머지 패키지는 기본 패키지로 분류됩니다.

기본 패키지 업로드는 이 변경의 영향을 받지 않습니다. 또한 이 설정은 사용자가 업로드하는 패키지에 적용되며 Microsoft나 외부 공급자가 제작한 1P·3P 에이전트 전체를 제어하는 설정이 아닙니다.

## 관리자 설정과 적용 일정

![고급 패키지 업로드 권한을 선택하는 관리자 설정](/mwkorea/assets/images/2026-09-16-CopilotAdvancedAgentUploadGovernance/image1.png)

| 시점 | 공지의 안내 |
|---|---|
| 2026년 9월 25일 | Microsoft 365 admin center의 Copilot Settings에 제어 표시 시작 |
| 2026년 10월 25일까지 | 모든 사용자, 아무도 허용하지 않음, 특정 사용자·그룹 중 정책 선택 |
| 2026년 10월 25일부터 | 제한을 설정하지 않았다면 고급 패키지 업로드 기본 허용 |
| 2026년 10월 말 | Worldwide GA 배포 완료 예상 |

현재 동작을 유지하려면 필수 조치는 없습니다. 반대로 승인된 메이커만 업로드하도록 운영하려면 기본 허용 상태를 그대로 두지 말고 조직 정책을 설정해야 합니다.

## 적용 범위를 오해하지 않기

대상 서비스에는 Microsoft 365 Copilot·Cowork 경험, ATK Copilot 에이전트, Copilot 플러그인과 Entra ID가 포함됩니다. 관리자는 admin center에서 사용자 업로드 패키지와 패키지 구성요소를 확인할 수 있습니다.

중요한 제한은 **제어가 제공된 이후 업로드되는 고급 에이전트와 플러그인에 적용**된다는 점입니다. 이 공지만으로 기존에 배포된 모든 에이전트가 소급 차단된다고 해석해서는 안 됩니다.

## 한국 조직의 운영 체크포인트

업로드 담당자용 Entra 그룹을 만들고 가입·탈퇴 승인 절차를 정하면 담당자가 바뀌어도 정책을 유지하기 쉽습니다. 패키지 검토 시에는 actions와 MCP 연결의 존재를 먼저 확인하고, 업로드 승인과 실제 데이터 접근 권한 검토를 별도 절차로 운영하는 것이 좋습니다.

헬프데스크에는 기본 패키지와 고급 패키지의 차이를 안내하세요. 이 설정은 확장 기능 도입의 관리 지점을 제공하지만, 외부 도구의 권한 검토까지 자동으로 대신하지는 않습니다.

> **출처**: [MC1472007 — Manage who can upload advanced agents and plugins](https://mc.merill.net/message/MC1472007). [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)도 함께 확인하세요. 이 공지 본문에는 개별 Roadmap ID가 명시되어 있지 않습니다. **실제 출시 일정·기능은 변경될 수 있습니다**.
