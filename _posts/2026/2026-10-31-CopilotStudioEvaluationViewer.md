---
title: "평가 담당자에게 편집 권한까지 줄 필요는 없습니다: Copilot Studio Evaluation Viewer"
date: 2026-10-31T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Evaluation
  - Governance
excerpt: "Copilot Studio의 Evaluation Viewer 역할은 에이전트 편집 권한 없이 평가 결과를 검토하도록 돕습니다. 2026년 10월 15일 GA 기능으로 품질·운영 담당자의 역할 분리에 활용할 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 평가 담당자에게 편집 권한까지 줄 필요는 없습니다: Copilot Studio Evaluation Viewer

에이전트 품질을 검토하는 사람과 에이전트를 수정하는 사람이 항상 같을 필요는 없습니다. 하지만 평가 결과를 보여주기 위해 넓은 작성 권한을 부여하면 책임 경계가 흐려집니다.

Copilot Studio의 **Evaluation Viewer** 역할은 이런 문제를 줄이도록 평가 결과와 관련 정보의 검토를 별도 역할로 분리합니다.

---

## 평가 참여와 작성 권한을 분리

품질 담당자, 운영 담당자 등 지정된 이해관계자는 에이전트 내용을 수정하는 광범위한 권한 없이 평가 워크플로에 참여할 수 있습니다. 평가 결과 접근을 위해 작성자 권한까지 부여하던 관행을 다시 점검할 계기입니다.

원문은 이 역할을 통해 역할 분리와 불필요한 작성 접근 축소, 거버넌스 강화를 지원한다고 설명합니다. 평가에 참여한다고 해서 에이전트 수정 권한이 자동으로 필요한 것은 아니라는 뜻입니다.

## 일정과 적용 방법

기능은 **2026년 10월 15일 GA**에 도달했으며 10월 30일 공지됐습니다. 이 글의 날짜는 공지 피드 시각을 KST로 변환한 기준입니다.

관리자는 평가 결과를 볼 사용자를 식별한 뒤 조직의 기존 보안 역할 관리 절차에 따라 Evaluation Viewer를 할당하면 됩니다. 원문은 추가 구성이 필요하지 않다고 안내합니다.

## 도입 체크포인트

국내 조직에서는 메이커, 품질 검토자, 배포 승인자의 책임을 먼저 정리하는 것이 좋습니다. 역할 이름만으로 필요한 모든 데이터 접근이 충족된다고 가정하지 말고, 실제 대상 에이전트의 평가 결과를 적절히 조회할 수 있는지도 확인하세요.

> **출처**: MC1532073 — [Microsoft Copilot Studio - Evaluation Viewer role](https://mc.merill.net/message/MC1532073). [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap). 원문에 개별 Roadmap ID는 표시되어 있지 않습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
