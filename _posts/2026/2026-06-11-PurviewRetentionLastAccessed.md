---
title: "마지막 액세스 기준 보존(Retention): OneDrive·SharePoint 파일을 '쓰임'에 맞춰 관리한다"
date: 2026-06-11T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftPurview
  - DataLifecycle
  - Retention
  - SharePoint
  - OneDrive
  - CopilotControlSystem
  - Roadmap
excerpt: "Microsoft Purview 데이터 수명 주기 관리에 '마지막 액세스(Last Accessed) 기준 보존'이 추가됩니다. 파일이 마지막으로 사용된 시점을 기준으로 OneDrive·SharePoint 항목별 보존 정책을 적용할 수 있어, Copilot 시대의 데이터 위생과 거버넌스에 직접 기여합니다. 프리뷰 6월·GA 7월 일정으로 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 마지막 액세스 기준 보존: 파일을 '쓰임'에 맞춰 관리하기

조직의 데이터는 시간이 지날수록 쌓입니다. 문제는 그중 상당수가 **더 이상 아무도 열어보지 않는 파일**이라는 점입니다. 이런 오래된 콘텐츠는 저장 비용을 늘릴 뿐 아니라, Copilot이 검색·요약할 때 **낡거나 부정확한 정보의 출처**가 되어 답변 품질을 떨어뜨릴 수 있습니다.

이번 Microsoft 365 로드맵 업데이트는 그 해묵은 과제에 정밀한 도구를 더합니다. **Microsoft Purview**의 데이터 수명 주기 관리(Data Lifecycle Management)에 **"마지막 액세스(Last Accessed) 기준 보존"**이 추가되어, 파일이 **사용자에 의해 마지막으로 열린 시점**을 기준으로 OneDrive·SharePoint 항목별 보존 정책을 적용할 수 있게 됩니다.

> **이 글의 한 줄 요약**
> OneDrive·SharePoint의 각 항목에 대해 "마지막으로 액세스된 시점"을 기준으로 보존(Retention)을 적용할 수 있습니다. 생성·수정일이 아니라 실제 '쓰임'을 기준으로 데이터 수명을 관리합니다. (#copilotcontrolsystem)

---

## 무엇이 바뀌나: '마지막 액세스'가 보존 기준이 된다

기존의 보존 정책은 보통 **생성일** 또는 **수정일**을 기준으로 동작했습니다. 하지만 이 기준은 "최근까지 실제로 활용된 파일"과 "오래전 만들어 둔 뒤 방치된 파일"을 잘 구분하지 못합니다.

이번 기능의 핵심은 보존 기준에 **마지막 액세스 시점(Last Accessed)**을 추가한 것입니다.

- OneDrive·SharePoint의 **개별 항목(item) 단위**로 적용
- 사용자가 **마지막으로 액세스한 시점**을 기준으로 보존 기간 산정
- 실제 사용 패턴에 맞춘 **데이터 수명 주기 관리**

즉, "오래됐지만 여전히 쓰는 파일"은 지키고, "한참 전에 잊힌 파일"은 정책에 따라 정리하는 식의 정교한 관리가 가능해집니다.

---

## 왜 중요한가: Copilot 시대의 '데이터 위생'

이 기능에는 **#copilotcontrolsystem** 태그가 붙어 있습니다. Copilot의 답변 품질과 거버넌스를 위한 통제 체계의 일부라는 의미입니다.

- **답변 품질**: 오래 방치된 콘텐츠를 정리하면, Copilot이 최신·유효한 정보에 그라운딩될 가능성이 높아집니다.
- **위험 축소**: 더 이상 쓰지 않는 민감 정보를 적시에 정리해 노출 위험을 줄입니다.
- **저장·비용 효율**: 실제 쓰임 기준으로 정리해 불필요한 저장 부담을 낮춥니다.
- **정밀한 거버넌스**: 일괄 기준이 아닌 항목별·사용 기반 정책으로 규정 준수를 강화합니다.

Copilot 도입을 준비하는 조직이라면, 무엇을 Copilot에 노출할지를 결정하는 **데이터 위생(data hygiene)** 작업의 강력한 수단이 됩니다.

---

## 활용 시나리오

- **부서 공유 사이트 정리**: 수년간 누적된 SharePoint 자료 중 오래 액세스되지 않은 항목에 보존·정리 정책 적용
- **개인 OneDrive 수명 관리**: 마지막 사용 기준으로 오래된 초안·임시 파일 정리
- **Copilot 사전 준비**: Copilot 검색 범위에서 낡은 콘텐츠의 영향을 줄여 답변 신뢰도 향상

---

## 출시 일정

| 구분 | 내용 |
|------|------|
| **대상** | Microsoft Purview 데이터 수명 주기 관리 (OneDrive · SharePoint, Web) |
| **서비스** | Microsoft Copilot(Microsoft 365) · Microsoft Purview |
| **상태** | In development |
| **Preview** | 2026년 6월 (CY2026) |
| **General Availability (GA)** | 2026년 7월 (CY2026) |
| **클라우드** | Worldwide (Standard Multi-Tenant) |
| **관련 로드맵** | RM472030 |

---

## 도입 관점 체크포인트

- **액세스 신호 검증**: "마지막 액세스" 판정 기준(어떤 동작이 액세스로 집계되는지)을 사전에 확인했는가
- **정책 충돌 점검**: 기존 생성·수정일 기반 보존 정책과의 우선순위·중복을 정리했는가
- **사용자 영향 고지**: 자주 안 쓰지만 중요한 파일이 정리되지 않도록 예외·레이블 전략을 마련했는가
- **Copilot 거버넌스 연계**: Copilot Control System 관점에서 데이터 정리와 노출 범위를 함께 설계했는가

---

## 마무리

데이터 보존의 기준이 "언제 만들었나"에서 "언제 마지막으로 썼나"로 옮겨가는 것은 작아 보여도 큰 변화입니다. 실제 쓰임에 맞춰 데이터를 관리하면, 저장 효율과 규정 준수는 물론 Copilot 답변의 신뢰도까지 함께 끌어올릴 수 있습니다. Copilot 도입을 준비하는 조직의 데이터 위생 전략에 유용한 도구가 될 것입니다.

---

> ※ 본 글은 Microsoft 365 로드맵 공지(**RM472030**)를 바탕으로 정리했습니다. 원문은 [RM472030](https://mc.merill.net/message/RM472030)과 [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)에서 확인할 수 있으며, 실제 출시 일정과 기능은 변경될 수 있습니다.
