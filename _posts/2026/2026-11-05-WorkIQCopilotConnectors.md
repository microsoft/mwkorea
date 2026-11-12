---
title: "기존 Copilot 커넥터를 Work IQ API로: 사내 시스템과 에이전트의 연결 확대"
date: 2026-11-05T00:00:00 KST
categories:
  - Copilot
tags:
  - WorkIQ
  - CopilotConnectors
  - Agent
  - Governance
excerpt: "Work IQ API가 Copilot 커넥터를 통해 연결된 기업 시스템의 데이터와 도구를 활용하도록 확장됩니다. 별도 커넥터 재구성 없이 기존 연결과 권한·거버넌스 제어를 이어가는 변화입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 기존 Copilot 커넥터를 Work IQ API로: 사내 시스템과 에이전트의 연결 확대

기업 업무의 맥락은 Microsoft 365 안에만 있지 않습니다. 외부 업무 시스템의 데이터와 도구를 에이전트가 함께 활용하려면 연결 설정과 운영 정책을 반복해서 구성해야 하는지부터 고민하게 됩니다.

MC1538999는 기존 **Copilot connectors 투자를 Work IQ APIs에서도 활용**하도록 확장하는 변경입니다. 새로운 경로로 활용 범위가 넓어지지만, 기존 권한과 관리자 제어를 없애는 변화는 아닙니다.

---

## 무엇이 달라지나요?

Work IQ API를 사용하는 AI 에이전트가 Copilot 커넥터로 연결된 기업 시스템의 데이터와 도구를 활용할 수 있게 됩니다. 별도의 커넥터 설정이나 관리 체계를 다시 만드는 대신 기존 연결을 재사용하는 방향입니다.

원문은 사용자가 Copilot Chat에서 이미 연결한 데이터 원본이 **기존 권한 및 관리자 제어에 따라 Work IQ API에서도 자동으로 사용 가능**해진다고 설명합니다. 조직의 모든 데이터가 무조건 공개되거나, 모든 외부 시스템이 새로 연결된다는 뜻은 아닙니다.

## 기존 거버넌스는 유지됩니다

Copilot 커넥터의 기존 관리자 제어, 권한, 거버넌스 정책은 계속 적용됩니다. 영향 대상은 **Work IQ API와 Copilot 커넥터를 사용하는 조직**입니다.

추가 관리자 작업은 요구되지 않습니다. 다만 자동으로 활용 경로가 확대되는 만큼, 국내 도입 담당자는 현재 연결된 원본과 접근 권한이 의도에 맞는지 확인하는 것이 좋습니다. 이는 원문이 요구하는 필수 조치가 아니라 운영상 권장하는 점검입니다.

## 개발·도입 체크포인트

에이전트 개발자는 새 데이터 원본을 무조건 추가하기보다, 기존 Copilot Chat 연결로 필요한 업무 맥락을 확보할 수 있는지 먼저 살펴볼 수 있습니다.

실무 검증에서는 사용자별 접근 가능 범위가 유지되는지, 권한이 없는 콘텐츠가 응답에 섞이지 않는지 확인하는 것이 중요합니다. 원문에는 구체적인 API 호출 예제나 추가 라이선스 조건이 없으므로, 이 변경만으로 호출 규격이나 비용을 단정하면 안 됩니다.

## 제공 일정과 마무리

전 세계 일반 공급은 **2026년 11월 말 시작, 12월 말 완료 예상**입니다. 발표 시점의 예정 일정이며 모든 테넌트에서 즉시 활성화되었다는 의미는 아닙니다.

핵심은 기존 연결을 재사용해 에이전트의 업무 맥락을 넓히는 것입니다. 새 연결을 만드는 수고를 줄이는 동시에, 기존 접근 정책이 실제 사용 경로에서도 일관되게 적용되는지 확인해야 합니다.

> **출처**: [MC1538999 — Microsoft 365 Copilot: Copilot connectors in Work IQ APIs](https://mc.merill.net/message/MC1538999). [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 제공되지 않았습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
