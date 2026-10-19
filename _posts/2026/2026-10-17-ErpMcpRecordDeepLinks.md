---
title: "Copilot 답변에서 ERP 원장으로 바로: MCP 응답의 레코드 딥링크"
date: 2026-10-17T00:00:00 KST
categories:
  - Copilot
tags:
  - Dynamics365
  - ERP
  - MCP
  - DeepLinks
excerpt: "Dynamics 365 ERP MCP 서버 기반 응답에 근거 데이터로 이동하는 딥링크가 추가됩니다. 답변에서 실제 업무 레코드로 연결해 투명성과 추적성을 높이는 변화입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 답변에서 ERP 원장으로 바로: MCP 응답의 레코드 딥링크

Copilot이 ERP 데이터를 설명해 주더라도, 실제 업무에 반영하려면 근거 레코드를 확인해야 합니다. 답변을 읽은 뒤 다시 메뉴를 찾아가는 과정은 검토 시간을 늘립니다.

Dynamics 365 ERP MCP 서버의 새 기능은 **응답을 생성하는 데 사용한 데이터로 연결되는 딥링크**를 제공합니다. 답변과 시스템 기록 사이의 연결을 분명하게 만드는 변화입니다.

---

## 답변의 근거를 열어 봅니다

원문은 ERP MCP 서버 기반 응답에 인용과 레코드 딥링크를 포함해 투명성·추적성·신뢰를 높인다고 설명합니다. 사용자는 설명만 받아들이는 대신 연결된 업무 데이터를 직접 확인할 수 있습니다.

딥링크가 있다고 답변의 해석까지 항상 정확하다는 뜻은 아닙니다. 특히 금액·기간·회사 등 중요한 조건은 열린 레코드와 비교해야 합니다.

## 개발자가 확인할 사항

링크가 의도한 환경과 레코드로 이동하는지, 사용자가 해당 레코드를 볼 권한이 있는지 점검하는 것이 좋습니다. 원문은 링크를 통한 권한 우회나 별도 접근 권한 부여를 설명하지 않습니다.

여러 레코드를 종합한 응답이라면 어떤 주장에 어떤 근거가 대응하는지 검토하는 절차도 필요합니다. 구체적인 적용 범위는 [ERP MCP 딥링크 문서](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/mcp/mcp-deep-links)를 참고하세요.

## 일정

로드맵에는 프리뷰 **2026년 5월**, GA **2026년 8월**이 기재되어 있습니다. 관리자·메이커·마케터 자동 활성화 항목이며, 실제 사용 가능 여부는 연결한 환경에서 확인해야 합니다.

> 출처: 원문 ID **RM576825**, [MC 아카이브](https://mc.merill.net/message/RM576825), [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap?id=576825). 실제 출시 일정·기능은 변경될 수 있습니다.
