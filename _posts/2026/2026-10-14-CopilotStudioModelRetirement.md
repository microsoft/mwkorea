---
title: "Copilot Studio, 일부 AI 모델 지원 종료: 2026년 11월 12일 에이전트 자동 마이그레이션 대비하기"
date: 2026-10-14T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Model
  - Retirement
  - GPT
  - Agent
  - Admin
excerpt: "Copilot Studio의 Standard·GitHub Copilot 하네스에서 GPT-4.1, GPT-5 계열 등 일부 모델 지원이 2026년 11월 12일 종료되고 에이전트는 대체 모델로 자동 이전됩니다. 영향 에이전트를 확인하고 사전 테스트하는 방법을 정리했습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio, 일부 AI 모델 지원 종료: 2026년 11월 12일 에이전트 자동 마이그레이션 대비하기

Microsoft는 Message Center(MC1506318, 2026년 10월 13일 게시)를 통해 **Copilot Studio의 Standard 및 GitHub Copilot 하네스에서 일부 AI 모델의 지원을 종료**한다고 공지했습니다. 각 모델의 마이그레이션 날짜 이후에는 해당 모델을 쓸 수 없고, 해당 모델로 구성된 에이전트는 **대체 모델로 자동 이전**됩니다.

대체 모델과 날짜는 모델과 하네스 조합에 따라 다르므로, 운영 중인 에이전트를 하네스·모델별로 점검하고 소유자와 사전 테스트를 준비하는 것이 중요합니다.

---

## 종료 대상 모델과 대체 모델

| 종료 모델 | 하네스 | 대체 모델 | 마이그레이션 날짜 |
|---|---|---|---|
| GPT-4.1* | Standard | GPT Chat Latest | 2026-11-12 |
| GPT-4.1 Mini | Standard | GPT Chat Latest | 2026-11-12 |
| GPT-5 Chat* | Standard | GPT Chat Latest | 2026-11-12 |
| GPT-5 Chat* | GitHub Copilot | GPT 5.6 Terra | 2026-11-12 |
| GPT-5 Auto | Standard | GPT Chat Latest | 2026-11-12 |
| GPT-5 Reasoning | Standard | GPT Chat Latest | 2026-11-12 |
| GPT 5.6 Sol | GitHub Copilot | GPT 6 Sol | 2026-11-12 |
| GPT 5.6 Luna | GitHub Copilot | GPT 6 Luna | 2026-11-12 |

\* 교차 지역 데이터 이동(cross-geo data movement)이 활성화된 **미국 기반 테넌트**는 GPT-4.1과 GPT-5가 계속 지원되며 이번 마이그레이션에서 종료되지 않습니다.

## GPT Chat Latest란?

Standard 하네스의 향후 지원 채팅 모델 옵션입니다. 현재 주 버전 내 스냅샷이 갱신되어도 **최신 지원 GPT 채팅 모델**을 유지합니다. 새 주(major) 버전으로 옮기는 것은 별도 변경이며, **최소 30일 전에 공지**됩니다.

## 해야 할 일

1. Power Platform 관리 센터 **관리 > Copilot Studio**에서 하네스·모델별 에이전트를 확인합니다. 모델 필드는 현재 **프리뷰**이며, 인벤토리는 **게시된 구성**을 반영하므로 게시되지 않은 모델 변경은 보이지 않을 수 있습니다.
2. 해당 에이전트 소유자에게 알립니다.
3. 대체 모델 또는 품질·성능·비용에 더 맞는 지원 모델로 **마이그레이션 전에 테스트**합니다.
4. 응답 정확도, 핵심 워크플로, 도구·액션 실행, 업무 핵심 연동을 검증하고 필요하면 지침이나 구성을 조정합니다.
5. 모델 제공 지역, 교차 지역·외부 모델 제공자 요건을 검토합니다.

모델 가용성은 하네스, 지역, 관리자 설정에 따라 다릅니다.

## 참고

- Claude Opus·Sonnet 이전 버전의 종료 일정은 별도 공지 예정입니다.
- GitHub Copilot 하네스에서는 Opus 5.5와 Sonnet 5.5를 이미 에이전트에서 사용할 수 있습니다.
- Copilot Studio 모델 수명 주기(lifecycle) 문서와 "Test your agent" 문서를 참고하세요.

---

> **원문**: MC1506318 — [Copilot Studio - Information regarding the end of support for selected AI models](https://mc.merill.net/message/MC1506318) / [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
