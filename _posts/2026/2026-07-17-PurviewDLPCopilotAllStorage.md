---
title: "민감도 레이블 파일의 Copilot 처리 차단, 이제 모든 저장 위치에 적용됩니다"
date: 2026-07-17T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftPurview
  - DLP
  - Microsoft365Copilot
  - SensitivityLabels
  - DataSecurity
  - Roadmap
excerpt: "Word·Excel·PowerPoint의 민감 파일을 Microsoft 365 Copilot이 처리하지 못하도록 제한하는 Microsoft Purview DLP 정책이, 파일 저장 위치와 관계없이 적용됩니다. 저장 위치별로 생기던 보호 공백을 없애 일관된 데이터 보안을 제공합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 민감도 레이블 파일의 Copilot 처리 차단, 이제 모든 저장 위치에 적용됩니다

민감한 문서를 Copilot이 근거로 삼지 못하도록 막는 것은 데이터 보안의 기본입니다. 하지만 보호 정책이 특정 저장 위치에만 적용된다면, 같은 파일이라도 어디에 저장됐는지에 따라 보호 여부가 달라지는 공백이 생깁니다.

Microsoft Purview의 **Data Loss Prevention(DLP) 정책**이 이제 **파일 저장 위치와 관계없이 적용**됩니다.

> **한 줄 요약**
> Word·Excel·PowerPoint의 민감 파일에 대해 Microsoft 365 Copilot 처리를 제한하는 Purview DLP 정책이, 파일이 어디에 저장되어 있든 일관되게 적용됩니다.

---

## 무엇이 바뀌나

기존에도 Purview DLP 정책으로 민감도 레이블이 붙은 Word·Excel·PowerPoint 파일을 Microsoft 365 Copilot이 처리하지 못하도록 제한할 수 있었습니다. 이번 업데이트로 이 정책이 **모든 저장 위치(all storage locations)**에 적용됩니다.

즉, 파일이 특정 위치에 있을 때만 보호되던 방식에서 벗어나, 저장 위치와 무관하게 동일한 보호가 적용됩니다.

## 왜 중요한가

데이터 보호에서 가장 위험한 것은 예외와 공백입니다. 같은 민감 문서가 저장 위치에 따라 다르게 취급되면 다음 문제가 생깁니다.

- 특정 위치에 저장된 민감 파일이 Copilot 처리에 노출될 위험
- 보호 여부를 저장 위치별로 추적해야 하는 관리 부담
- 사용자가 저장 위치를 옮겨 보호를 우회할 가능성

이번 변경은 이런 공백을 제거해 일관된 보호를 제공합니다.

## 활용 시나리오

- 기밀 등급 레이블이 붙은 재무 문서를 어느 위치에 두더라도 Copilot 처리 차단
- 민감 계약서가 여러 위치에 복사돼도 동일한 정책 적용
- 조직 전체의 민감도 레이블 기반 보호를 단일 기준으로 운영

## 출시 일정

| 구분 | 내용 |
|---|---|
| GA | 2026년 4월 |
| 대상 앱 | Word, Excel, PowerPoint |
| 적용 범위 | 모든 저장 위치 |

## 도입 관점 체크포인트

- 기존 DLP 정책이 저장 위치를 조건으로 두고 있었다면 영향 범위를 확인합니다.
- 민감도 레이블 체계가 조직 전반에 일관되게 적용돼 있는지 점검합니다.
- 정책 확대로 정상 업무가 과도하게 차단되지 않는지 파일럿으로 검증합니다.
- 보안·컴플라이언스 팀과 함께 예외 처리 기준을 정리합니다.

## 마무리

민감도 레이블 기반 Copilot 처리 차단이 모든 저장 위치로 확대되면서, 조직은 파일이 어디에 있든 일관된 데이터 보호를 유지할 수 있게 됩니다. Copilot 도입과 데이터 보안을 함께 추진하는 조직에 중요한 기반 강화입니다.

---

> ※ 본 글은 Microsoft 365 메시지 센터/로드맵 공지(**RM557255**)를 바탕으로 정리했습니다. 원문은 [Message Center Archive](https://mc.merill.net/message/RM557255)와 [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)에서 확인할 수 있으며, 실제 출시 일정·기능은 변경될 수 있습니다.
