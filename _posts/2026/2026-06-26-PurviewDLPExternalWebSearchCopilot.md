---
title: "Copilot이 민감정보를 외부 웹 검색에 쓰지 않도록: Purview DLP가 웹 검색까지 보호한다"
date: 2026-06-26T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftPurview
  - DLP
  - Microsoft365Copilot
  - CopilotChat
  - CopilotStudio
  - DataSecurity
excerpt: "Microsoft Purview DLP가 Microsoft 365 Copilot과 Copilot Chat의 외부 웹 검색까지 보호 범위를 넓힙니다. Copilot과 에이전트가 민감 데이터를 외부 웹 검색에 사용하지 못하도록 실시간으로 차단해, 데이터 유출과 과다 공유 위험을 줄입니다. 2026년 7월 정식 출시 예정입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot이 민감정보를 외부 웹 검색에 쓰지 않도록: Purview DLP가 웹 검색까지 보호한다

Copilot은 업무 데이터와 웹을 함께 활용할 때 가장 강력합니다. 하지만 바로 그 지점에서 보안팀의 고민도 커집니다. 사용자가 사내 민감정보를 포함해 질문하고, Copilot이 그 내용을 바탕으로 외부 웹 검색을 수행한다면 어떻게 될까요? 의도치 않게 민감 데이터가 조직 밖으로 새어 나갈 수 있습니다.

Microsoft 365 Roadmap 항목 RM565870에 따르면, Microsoft는 **Microsoft Purview DLP(데이터 손실 방지)**를 Microsoft 365 Copilot과 Copilot Chat의 **외부 웹 검색**까지 확장합니다. 민감 데이터가 포함된 웹 검색을 실시간으로 통제해, 데이터 유출과 과다 공유(oversharing) 위험을 줄이는 것이 핵심입니다.

이 기능은 현재 **Microsoft 365 Copilot**과, **Copilot Studio에서 만들어 Microsoft 365 Copilot에 게시된 에이전트**에 적용됩니다.

---

## 무엇이 새로운가

- **외부 웹 검색에 대한 DLP 확장**: 기존 Purview DLP 보호가 Copilot/Copilot Chat의 외부 웹 검색 시나리오까지 넓어집니다.
- **실시간 통제(real-time control)**: 민감 데이터가 포함된 검색을 그 순간에 차단해, Copilot과 에이전트가 민감 데이터를 외부 웹 검색에 사용하지 못하도록 합니다.
- **적용 범위**: Microsoft 365 Copilot, 그리고 Copilot Studio에서 빌드되어 Microsoft 365 Copilot에 게시된 에이전트.

---

## 왜 중요한가

생성형 AI 도입에서 가장 흔한 우려는 "내부 데이터가 외부로 나가지 않는가"입니다. 특히 Copilot이 웹 검색으로 답변을 보강할 때, 사용자의 질문에 담긴 민감정보(고객 정보, 계약 조건, 내부 코드명 등)가 검색 쿼리에 포함될 가능성이 있습니다.

이번 업데이트는 그 경로를 정조준합니다.

> 민감 데이터가 외부 웹 검색에 쓰이지 않도록, DLP 정책으로 실시간 차단.

덕분에 조직은 Copilot의 웹 활용 가치를 유지하면서도, 데이터 경계를 넘는 위험을 정책 기반으로 통제할 수 있습니다. 이는 기존 Purview DLP 정책 체계를 Copilot 시나리오로 자연스럽게 확장한다는 점에서도 의미가 큽니다.

---

## 활용 시나리오

- **민감 라벨 데이터 보호**: 특정 민감도 레이블이 붙은 정보가 외부 웹 검색에 활용되지 않도록 차단
- **규제 산업 대응**: 금융·공공·의료처럼 데이터 외부 반출이 엄격히 통제되는 환경에서 Copilot 도입 장벽 완화
- **에이전트 거버넌스**: Copilot Studio로 만든 사내 에이전트가 외부 웹 검색을 수행할 때도 동일한 데이터 보호 기준 적용

---

## 출시 일정

| 항목 | 내용 |
|------|------|
| 기능 | Purview DLP의 외부 웹 검색 보호(Microsoft 365 Copilot·Copilot Chat) |
| 적용 대상 | Microsoft 365 Copilot, Copilot Studio에서 게시된 에이전트 |
| 정식 출시(GA) | **2026년 7월 (예정)** |

---

## 도입 관점 체크포인트

- **기존 DLP 정책과의 연계**: 이미 운영 중인 Purview DLP 정책·민감도 레이블 체계가 Copilot 웹 검색 시나리오에 어떻게 적용되는지 점검하세요.
- **차단 vs 사용성 균형**: 과도한 차단은 사용자 경험을 해칠 수 있으므로, 어떤 민감 데이터 유형을 외부 웹 검색에서 막을지 우선순위를 정하는 것이 좋습니다.
- **에이전트 게시 가이드**: Copilot Studio 에이전트를 Microsoft 365 Copilot에 게시하는 메이커들에게, 외부 웹 검색 시 DLP가 적용된다는 점을 사전에 안내하세요.
- **모니터링·감사**: DLP 이벤트를 모니터링해 어떤 검색이 차단되는지 파악하고, 정책을 점진적으로 정교화하는 운영 루틴을 마련하세요.

---

## 마무리

이 업데이트는 "Copilot을 도입하되, 데이터는 통제 가능해야 한다"는 기업의 현실적 요구에 답합니다. 웹 검색이라는 가치 있는 기능을 유지하면서도 민감 데이터의 외부 노출을 실시간으로 막아 주므로, Copilot 도입을 검토하는 보안·컴플라이언스팀에게 반가운 변화입니다. 출시 시점에 맞춰 DLP 정책 범위를 Copilot 시나리오까지 점검해 두기를 권합니다.

---

> **출처**: Microsoft 365 Roadmap 항목 **RM565870** · [mc.merill.net/message/RM565870](https://mc.merill.net/message/RM565870) · [Microsoft 365 Roadmap에서 보기](https://www.microsoft.com/en-us/microsoft-365-roadmap?searchterms=565870)
>
> *실제 출시 일정·기능은 변경될 수 있습니다.*