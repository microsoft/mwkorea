---
title: "Power BI 독립형 Copilot 프리뷰 종료 예고: 12월부터 전환을 준비하세요"
date: 2026-11-10T00:00:00 KST
categories:
  - Copilot
tags:
  - PowerBI
  - MicrosoftFabric
  - Microsoft365Copilot
  - Preview
  - Retirement
excerpt: "Power BI의 독립형 Copilot 프리뷰가 2027년 1월 종료될 예정입니다. Microsoft 365 Copilot in Power BI는 2026년 12월 8일부터 기본 활성화되지만, 대체 경험 역시 프리뷰이므로 조직별 가용성과 요건을 확인해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Power BI 독립형 Copilot 프리뷰 종료 예고: 12월부터 전환을 준비하세요

Power BI에서 AI로 데이터를 분석하는 사용자라면 앞으로 **어느 Copilot 진입점을 사용해야 하는지**를 확인할 필요가 있습니다. Microsoft는 MC1546429에서 독립형(standalone) Copilot 프리뷰 경험의 종료를 예고했습니다.

대신 Microsoft 365 Copilot in Power BI가 2026년 12월 8일부터 기본 활성화될 예정입니다. 다만 이번 공지는 Power BI의 모든 Copilot 기능이 종료된다는 뜻이 아니며, 대체 경험이 이미 GA라는 의미도 아닙니다.

---

## 종료되는 범위는 어디까지인가요?

이번 공지의 대상은 다음 위치에서 제공되던 **독립형 Copilot 경험**입니다.

- Power BI Home 페이지
- Power BI 모바일 앱
- Microsoft Teams
- Power BI workspace 앱 내부의 app-scoped Copilot

관련 탐색 진입점과 설정도 제거됩니다. 원문이 구체적으로 언급한 항목은 **standalone Copilot 테넌트 설정**과 **Show Copilot in app navigation** 설정입니다.

현재 교육 자료나 헬프데스크 안내가 이 진입점을 기준으로 작성되어 있다면 사용자 문서도 함께 수정해야 합니다. 반대로 이 공지를 Power BI 전반의 AI 지원 기능 폐지로 확대 해석해서는 안 됩니다.

## 전환 일정을 확인하세요

| 예정일 | 변경 |
|---|---|
| 2026년 12월 8일 | Microsoft 365 Copilot in Power BI 기본 활성화, Worldwide |
| 2027년 1월 | 독립형 Copilot 프리뷰 종료 |

종료 시점은 원문 안에서도 표현에 차이가 있습니다. 도입부에는 **1월 초**, 별도의 Rollout Schedule에는 **1월 중순**이라고 적혀 있습니다. 따라서 특정 종료일을 확정하기보다는 **12월 8일 기본 활성화 전에 전환 준비를 진행하고, 정확한 종료 시점은 후속 공지로 확인**하는 것이 안전합니다.

## 대체 경험도 프리뷰입니다

Microsoft는 **Microsoft 365 Copilot in Power BI and Microsoft Fabric (preview)**를 대안으로 안내합니다. Power BI와 Fabric 안으로 Microsoft 365 Copilot을 가져와 AI 기반 데이터 분석을 이어 갈 수 있도록 하는 방향입니다.

여기서 기본 활성화는 모든 조직·모든 사용자가 추가 조건 없이 사용할 수 있다는 보장과 다릅니다. 원문도 조직의 **가용성과 요구사항**을 사전에 검토하라고 권고합니다. 이 공지 자체에는 상세 라이선스나 용량 조건이 제시되어 있지 않으므로, 기존 독립형 프리뷰의 조건이 그대로 적용된다고 가정하지 않아야 합니다.

## 도입 담당자의 전환 체크포인트

1. 기존 사용자가 Home·모바일·Teams·workspace 앱 중 어떤 경로로 Copilot을 사용하는지 파악합니다.
2. 원문이 연결한 [Power BI 및 Microsoft Fabric의 Microsoft 365 Copilot 프리뷰 안내](https://community.fabric.microsoft.com/blog/fbc_pbiupdatesblog/power-bi-september-2026-feature-summary/5325831#community-5325831-mcetoc_1k32v0uak_5)에서 가용성과 요구사항을 확인합니다.
3. 조직의 대표 분석 시나리오를 대체 경험에서 확인하고 사용자 안내를 준비합니다.
4. 종료되는 탐색 메뉴와 설정을 설명한 내부 문서를 갱신합니다.

대표 업무를 실제로 확인하는 것은 전환을 위한 권고입니다. 원문이 기존 경험과 새 경험의 완전한 기능 동등성이나 모든 사용 경로의 일대일 대체를 보장한 것은 아닙니다.

## 마무리

이번 변화는 독립형 프리뷰의 종료와 Microsoft 365 Copilot 중심 경험으로의 전환입니다. **12월 8일 기본 활성화와 1월 종료를 따로 관리**하고, 사용자가 익숙한 진입점이 사라지기 전에 새 경로와 적용 조건을 안내하는 것이 중요합니다.

> 출처: [MC1546429 — Power BI retiring standalone Copilot experiences (preview)](https://mc.merill.net/message/MC1546429)
>
> 참고: [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap). 이 공개 공지에는 개별 Roadmap ID가 제시되어 있지 않습니다.
>
> 일정은 원문 공지 시점 기준이며 종료 시점의 표현 차이는 본문에 구분했습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
