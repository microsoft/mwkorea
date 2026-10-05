---
title: "OneDrive·SharePoint PDF, Copilot가 목차까지 자동으로 만들어줍니다"
date: 2026-10-03T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - OneDrive
  - SharePoint
  - PDF
  - Productivity
excerpt: "목차가 없는 PDF를 열면 Copilot이 문서 구조를 분석해 클릭 가능한 계층형 목차를 즉석에서 만들어줍니다. OneDrive·SharePoint 웹 PDF 뷰어에 추가되는 Smart Table of Contents 기능을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# OneDrive·SharePoint PDF, Copilot가 목차까지 자동으로 만들어줍니다

목차 없는 긴 PDF 보고서나 계약서를 스크롤하며 원하는 섹션을 찾느라 고생한 적 있으신가요? Microsoft는 Microsoft 365 Copilot 라이선스 사용자를 대상으로 OneDrive와 SharePoint 웹 PDF 뷰어에 **Smart Table of Contents(Smart TOC)** 기능을 추가합니다.

문서에 이미 목차가 있다면 적용되지 않지만, 목차가 없는 PDF를 열었을 때 사용자가 명시적으로 요청하면 Copilot이 문서 구조를 분석해 계층형·클릭 가능한 목차를 즉석에서 생성해 줍니다.

---

## 무엇이 새로운가

- PDF를 열었을 때 목차 정보가 없으면 Smart TOC 진입점이 나타납니다.
- Copilot이 문서 구조를 분석해 페이지 또는 페이지 범위에 매핑된 중첩 목차 항목을 만듭니다.
- 편집 권한이 있는 사용자는 생성된 목차를 PDF에 저장할 수 있고, 저장된 목차는 호환되는 PDF 편집기에서도 표시됩니다.
- 보기 전용 권한 사용자는 탐색용으로 Smart TOC를 생성·사용할 수 있지만 저장은 불가능합니다.
- 초기 출시는 **웹 전용**이며, 모바일·데스크톱 앱은 이번 범위에 포함되지 않습니다.
- 생성된 목차에는 AI가 만들었다는 표시가 명확히 붙으며, 특히 스캔본·OCR 기반 PDF는 부정확할 수 있다는 안내가 함께 제공됩니다.

## 일정

| 단계 | 시작 | 완료 예상 |
|---|---|---|
| Targeted Release (Worldwide) | 2026년 12월 초 | 2026년 12월 중순 |
| General Availability (Worldwide/GCC/GCC High/DoD) | 2026년 12월 중순 | 2026년 12월 말 |

점진적 롤아웃이므로 모든 적격 사용자가 동시에 기능을 받지는 않습니다.

## 관리자 체크포인트

관리자의 사전 조치는 필수는 아니지만, 롤아웃 전 다음을 점검하는 것을 권장합니다.

- 이 기능을 사용할 대상 사용자의 Microsoft 365 Copilot 라이선스 할당 현황 검토
- 헬프데스크·지원팀에 새로운 PDF 탐색 경험 사전 공지
- 목차 저장에는 편집 권한이 필요하다는 점을 내부 문서에 반영
- 정확성이 중요한 문서는 AI가 생성한 목차 항목을 사용자가 직접 검증하도록 안내

## 마무리

Smart TOC는 사용자가 명시적으로 요청할 때만 동작하고 기존 파일 권한을 그대로 따르는 "옵트인" 방식의 AI 기능입니다. 대용량 PDF를 자주 다루는 조직이라면 2026년 12월 롤아웃에 맞춰 사용자 안내를 준비해 두시길 권합니다.

---

> 출처: MC1486295, [mc.merill.net 원문](https://mc.merill.net/message/MC1486295) — 실제 출시 일정·기능은 변경될 수 있습니다.
