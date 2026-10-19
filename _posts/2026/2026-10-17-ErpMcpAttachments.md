---
title: "ERP 레코드의 첨부파일까지 읽는다: Dynamics 365 MCP 서버 확장"
date: 2026-10-17T00:00:00 KST
categories:
  - Copilot
tags:
  - Dynamics365
  - ERP
  - MCP
  - Attachments
excerpt: "Dynamics 365 ERP MCP 서버가 첨부파일 생성·삭제와 내용 읽기·추론을 지원하는 방향으로 확장됩니다. 문서 기반 업무 맥락을 활용할 수 있지만 읽기와 변경 권한은 구분해서 설계해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# ERP 레코드의 첨부파일까지 읽는다: Dynamics 365 MCP 서버 확장

ERP 레코드의 의미는 필드 값만으로 설명되지 않을 때가 많습니다. 첨부 문서에 거래 배경이나 세부 조건이 담겨 있기 때문입니다.

Microsoft는 Dynamics 365 ERP MCP 서버를 통해 에이전트가 첨부파일을 다루는 기능을 안내했습니다. 구조화된 레코드와 함께 문서 내용까지 업무 흐름에 활용하는 것이 핵심입니다.

---

## 무엇이 추가되나요?

원문은 첨부파일의 **생성, 삭제, 내용 읽기와 추론**을 명시합니다. 단순 파일 목록 조회를 넘어, 에이전트 흐름에서 문서 내용에 근거해 작업하는 시나리오를 열어 줍니다.

다만 지원 파일 형식, 크기 한도, OCR 지원 여부나 모든 문서의 자동 처리는 이 항목에 명시되지 않습니다. 업무별 검증 없이 일반 문서 처리 서비스처럼 가정해서는 안 됩니다.

## 개발·도입 체크포인트

문서를 읽는 권한과 생성·삭제하는 권한은 위험도가 다릅니다. 조회 중심 흐름부터 확인하고, 파일을 변경하는 작업에는 사용자 확인과 감사 기준을 별도로 두는 것이 좋습니다. 이는 운영 권고이며 원문이 특정 승인 UI를 보장하는 것은 아닙니다.

첨부 내용이 어느 ERP 레코드에 연결되는지, 민감정보가 포함되어 있는지, 실패 시 원본이 보존되는지도 확인할 사항입니다.

## 일정

로드맵 표기는 프리뷰 **2026년 4월**, GA **2026년 7월**이며 관리자·메이커·마케터에게 자동 활성화되는 항목으로 분류됩니다. 이 구분을 모든 최종 사용자의 무제한 파일 변경 허용으로 해석하지 마세요.

> 출처: 원문 ID **RM576826**, [MC 아카이브](https://mc.merill.net/message/RM576826), [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap?id=576826). 실제 출시 일정·기능은 변경될 수 있습니다.
