---
title: "Business Central, 에이전트 생성 내용을 업무 화면에서 바로 검토한다"
date: 2026-10-01T00:00:00 KST
categories:
  - Copilot
tags:
  - BusinessCentral
  - HumanInTheLoop
  - AgentReview
  - Dynamics365
excerpt: "Business Central 사용자가 에이전트가 만든 설명·텍스트·필드 변경안을 현재 페이지에서 바로 검토하고 수정할 수 있게 됩니다. 별도 작업 창을 오가는 대신 업무 맥락 안에서 승인하는 human-in-the-loop 경험입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Business Central, 에이전트 생성 내용을 업무 화면에서 바로 검토한다

Dynamics 365 Business Central이 에이전트가 생성한 내용을 **실제 업무 페이지 안에서** 검토하고 승인할 수 있도록 개선됩니다. 문서가 에이전트에 의해 만들어졌는지 확인하려고 별도의 작업 창으로 이동할 필요가 줄어듭니다.

설명, 텍스트 제안, 특정 필드 업데이트가 적용될 위치에 바로 나타나므로 사용자는 주변 데이터와 함께 내용을 평가하고 수정한 뒤 반영할 수 있습니다.

---

## 업무 맥락 안의 승인

기존에는 에이전트 작업을 확인하기 위해 별도 패널이나 작업 화면으로 이동해야 하는 경우가 있었습니다. 새 경험은 Business Central의 기존 autofill UI 패턴을 활용해 제안을 현재 페이지에 표시합니다.

- 제안이 적용될 필드와 문서 맥락을 함께 확인
- 적용 전에 에이전트 생성 내용을 수정
- 별도 화면 전환과 클릭 감소
- 최종 결과에 대한 사용자 통제 유지

이는 에이전트가 자동으로 결과를 확정하는 방식이 아니라, 사람이 업무 맥락 안에서 판단하는 **human-in-the-loop** 패턴에 가깝습니다.

## 도입 체크포인트

조직은 어떤 제안을 단순 확인으로 처리하고 어떤 변경에 명시적 승인을 요구할지 정해야 합니다. 금액, 계정, 거래처와 같이 재무 영향이 큰 필드는 일반 텍스트보다 엄격한 검토가 필요합니다.

또한 사용자 교육에서는 에이전트 제안을 완성된 정답이 아니라 검토 대상 초안으로 설명해야 합니다. 수정 내용과 최종 승인자를 감사 기록에서 확인할 수 있는지도 배포 후 검증하는 것이 좋습니다.

## 일정

GA는 **2026년 10월**로 예정되어 있습니다. 공개된 설명에는 Preview 일정이나 지원 페이지 범위가 명시되지 않았으므로 테넌트 배포 후 실제 적용 화면을 확인해야 합니다.

> **출처**: 원문 ID **RM573366** · [mc.merill.net 원문](https://mc.merill.net/message/RM573366) · [Microsoft 365 Roadmap 573366](https://www.microsoft.com/en-us/microsoft-365/roadmap?featureid=573366)  
> 실제 출시 일정·기능은 변경될 수 있습니다.
