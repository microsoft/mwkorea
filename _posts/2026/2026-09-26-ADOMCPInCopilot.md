---
title: "Azure DevOps MCP 커넥터, Copilot Deep Work에서 자연어로 작업 항목 조회"
date: 2026-09-26T00:00:00 KST
categories:
  - Copilot
tags:
  - Copilot
  - AzureDevOps
  - MCP
  - DeepWork
excerpt: "Azure DevOps MCP 커넥터가 Microsoft 365 Copilot Deep Work와 통합되어 자연어로 작업 항목과 프로젝트 데이터를 조회할 수 있게 됩니다. 2026년 10월 전 세계에 순차 적용됩니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Azure DevOps MCP 커넥터, Copilot Deep Work에서 자연어로 작업 항목 조회

개발팀·PM이 Azure DevOps의 작업 항목이나 프로젝트 현황을 확인하려면 보통 ADO 보드를 직접 열어야 했습니다. 이제 **Azure DevOps MCP 커넥터**가 Microsoft 365 Copilot **Deep Work**와 통합되어, 자연어 질의만으로 ADO 데이터를 조회할 수 있게 됩니다.

---

## 핵심 기능

- Azure DevOps 작업 항목과 프로젝트 데이터를 **자연어 질의**로 조회
- **다단계 워크플로(multi-step workflows)** 지원 — 단순 조회를 넘어 여러 단계에 걸친 작업 처리 가능
- **관리자 제어(admin controls)** 제공
- **쓰기 작업은 사용자 확인(user-confirmed write actions)**을 거쳐야 실행됨 — 자동으로 데이터가 변경되지 않도록 안전장치 마련

## 롤아웃 일정

**2026년 10월** 전 세계에 순차 적용됩니다.

## 한국 개발팀을 위한 체크포인트

MCP(Model Context Protocol) 기반 커넥터가 쓰기 작업에도 사용자 확인 단계를 두었다는 점은, 실수로 작업 항목이 변경되거나 닫히는 사고를 방지하는 장치입니다. ADO를 중심으로 협업하는 개발팀이라면 Deep Work와의 연동을 통해 "어떤 스프린트에 어떤 작업이 지연됐는지"와 같은 분석성 질의를 자연어로 빠르게 받아볼 수 있을 것으로 기대됩니다. 관리자는 사전 제공되는 admin controls로 커넥터 접근 범위를 설계해두는 것이 좋습니다.

---

> **원문**: ADO MCP in Copilot (MC1479505) — [mc.merill.net에서 보기](https://mc.merill.net/message/MC1479505) | [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
