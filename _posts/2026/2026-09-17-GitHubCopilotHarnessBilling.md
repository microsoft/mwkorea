---
title: "Copilot Studio, GitHub Copilot harness 기반 에이전트 사용량 과금 2026년 9월 1일부터 시작"
date: 2026-09-17T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - GitHubCopilotHarness
  - CopilotCredits
  - FinOps
  - PowerPlatform
excerpt: "GitHub Copilot harness로 만든 Copilot Studio 에이전트·워크플로의 유예 기간이 끝나고 Copilot Credits 기반 사용량 과금이 시작됩니다. 과금 모델 롤아웃은 2026년 9월 15일 완료됐으며, Standard·Copilot Chat harness는 영향을 받지 않습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio, GitHub Copilot harness 기반 에이전트 사용량 과금 2026년 9월 1일부터 시작

Copilot Studio에서 **GitHub Copilot harness**로 빌드한 에이전트와 워크플로를 무료로 써왔다면, 이제 과금 전환점을 지났습니다. 유예 기간이 끝나고 **Copilot Credits** 기반 사용량 과금이 본격적으로 적용됩니다.

---

## 업데이트: 롤아웃 완료

> **Update**: 사용량 기반 과금 모델의 롤아웃은 **2026년 9월 15일 완료**됐습니다. 관리자는 이 날짜 이후 자신의 환경에서 사용량 기반 과금 관련 변화를 확인할 수 있습니다.

## 무엇이 바뀌었나

**2026년 9월 1일부터**, Copilot Studio에서 GitHub Copilot harness로 구축된 **기존 에이전트와 워크플로의 유예 기간이 종료**됩니다. 이들은 이제 사용량 기반 과금 모델 아래에서 **Copilot Credits를 소비**하기 시작합니다.

이는 **2026년 8월 3일 이전에 생성된 GitHub Copilot harness 에이전트·워크플로**에 적용되며, **Dev 또는 Trial 환경**에서 만들어진 것도 포함됩니다. **메이커의 AI 저작(authoring) 활동**과 **런타임 실행(runtime execution)** 모두 Copilot Credits를 소비합니다.

**Standard harness와 Copilot Chat harness 에이전트는 영향을 받지 않습니다.**

## 이것이 나에게 미치는 영향

2026년 9월 1일부터 해당 환경의 GitHub Copilot harness 에이전트·워크플로는 Copilot Credits를 소비합니다. 소비 정보는 기존 **Power Platform 관리센터(PPAC)**의 리포팅과 용량 관리(capacity management) 화면에서 확인할 수 있습니다.

PPAC에는 과금 이전의 **과거 비청구(non-billed) Copilot Credits 데이터**도 제공되어 현재 사용 패턴을 파악하는 데 도움을 줍니다. 경로는 **PPAC > Licensing > Copilot Studio > Manage Agents**입니다. 단, 이 정보는 **참고용(directional only)**이며 과금 예상치나 향후 비용으로 해석해서는 안 됩니다.

## 조치 사항

이 메시지는 공지용이며 별도 조치는 필요하지 않습니다. 다만 다음을 권장합니다.

- 관리자는 과금 시작 전에 과거 Copilot Credits 소비 내역을 검토하고 활성 상태인 GitHub Copilot harness 에이전트·워크플로를 식별할 것
- 환경별 크레딧 할당, 공유 테넌트 크레딧 풀 접근 제어, PPAC에서의 사용량 모니터링, 종량제 지출에 대한 Azure 예산·알림 활용 등으로 GitHub Copilot harness 소비를 관리할 것

## 더 알아보기

- [Manage costs for agents powered by the GitHub Copilot harness](https://aka.ms/17413-1)
- [Manage Copilot Credits and capacity for Copilot Studio](https://aka.ms/17413-2)
- [Manage Copilot Credits allocations programmatically](https://aka.ms/17413-3)
- [Identify all GitHub Copilot harness agents that have been created in your organization](https://aka.ms/17413-4)
- [Power Platform admin center Environment Group rules - Cost controls - Draw from tenant credit pool](https://aka.ms/17413-5)

## 한국 조직을 위한 체크포인트

- **2026년 8월 3일 이전에 만든 에이전트**를 보유한 조직이라면 이미 과금 대상입니다. 현재 소비 중인 Copilot Credits 규모를 PPAC에서 먼저 확인해보는 것이 급선무입니다.
- **Dev·Trial 환경에서 만든 에이전트도 과금 대상**이라는 점을 놓치기 쉬우므로, 테스트 목적으로 만들어둔 에이전트가 방치되어 있지 않은지 점검이 필요합니다.
- Standard harness·Copilot Chat harness는 영향이 없으므로, 비용에 민감한 시나리오라면 harness 선택 자체를 재검토하는 것도 방법입니다.
- 환경별 크레딧 할당과 Azure 예산·알림 기능을 적극 활용해 예상치 못한 과금 폭증을 방지하는 것을 권장합니다.

---

> **원문**: Copilot Studio - Billing for GitHub Copilot harness built agents begins September 1, 2026 (MC1461678) — [mc.merill.net에서 보기](https://mc.merill.net/message/MC1461678) | [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
