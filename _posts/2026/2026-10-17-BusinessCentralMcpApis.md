---
title: "Business Central 데이터를 에이전트 도구로: MCP의 표준 API·쿼리 확장"
date: 2026-10-17T00:00:00 KST
categories:
  - Copilot
tags:
  - BusinessCentral
  - MCP
  - API
  - Agent
excerpt: "Business Central MCP 서버가 Microsoft 표준 API 전체와 API queries를 도구로 노출하는 방향으로 확장됩니다. 개발자는 더 넓은 업무 데이터와 사전 집계된 데이터셋을 활용할 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Business Central 데이터를 에이전트 도구로: MCP의 표준 API·쿼리 확장

에이전트가 ERP 업무를 수행하려면 안정적으로 호출할 수 있는 데이터와 동작 인터페이스가 필요합니다. Business Central MCP 서버 확장은 더 넓은 표준 API 범위를 에이전트 도구로 연결하는 데 초점을 둡니다.

특히 보고·분석에서는 원시 레코드를 반복 조회하기보다 목적에 맞게 집계된 데이터를 가져오는 것이 중요합니다. 이번 항목은 이를 위한 API queries 지원도 함께 설명합니다.

---

## 두 가지 핵심 개선

첫째, **Business Central의 Microsoft 표준 API 전체를 MCP 서버에서 노출**할 수 있도록 확장합니다. 더 다양한 엔터티와 동작에 접근해 일부 사용자 지정 확장의 필요를 줄이는 방향입니다.

둘째, **API queries를 MCP 구성에서 사용**할 수 있습니다. 사전 집계·최적화된 데이터셋을 직접 가져와 보고와 분석에서 일관성·성능을 높이려는 변화입니다.

이는 모든 사용자 지정 API가 자동 공개되거나 모든 사용자의 권한이 확대된다는 설명은 아닙니다.

## 개발 체크포인트

에이전트가 실제로 필요한 API와 쿼리부터 선택하고, 조회와 변경 작업을 구분하세요. 분석 목적이라면 API query가 반환하는 집계 단위와 업무 정의가 사용자의 보고서와 일치하는지 확인하는 것이 좋습니다.

원문은 정확한 호출 성능 수치나 구성 예제 코드를 제공하지 않으므로 절감 효과를 수치로 단정할 수는 없습니다.

## 일정

로드맵에는 GA **2026년 6월**, 최종 사용자 자동 활성화 항목으로 기재되어 있습니다. 실제 도구 노출과 접근 범위는 해당 MCP 구성과 환경에서 확인해야 합니다.

> 출처: 원문 ID **RM576789**, [MC 아카이브](https://mc.merill.net/message/RM576789), [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap?id=576789). 실제 출시 일정·기능은 변경될 수 있습니다.
