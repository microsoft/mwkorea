---
title: "Copilot 커넥터 관리, Agent 365로 통합: 10월 30일 전에 확인할 전역 설정"
date: 2026-10-24T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Agent365
  - CopilotConnectors
  - Governance
  - Administration
excerpt: "Microsoft 365 Copilot 커넥터의 전역 관리가 Agent 365의 Allowed agent types 설정으로 통합됩니다. MC1454973에 공지된 2026년 10월 30일 적용 일정과 기존 CLI 기반 자동화를 점검할 때 주의할 사항을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 커넥터 관리, Agent 365로 통합: 10월 30일 전에 확인할 전역 설정

Copilot 커넥터와 에이전트의 접근 정책을 서로 다른 관리 방식으로 운영하고 있다면, 이제 설정의 기준점을 다시 확인해야 합니다. Microsoft는 Message Center 공지 **MC1454973**을 통해 기존 `setFederatedConnectors` CLI 토글을 폐기하고, Microsoft 365 관리 센터의 **Allowed agent types** 설정으로 커넥터 관리를 통합한다고 안내했습니다.

이 글은 **2026년 10월 23일 수정된 원문**을 기준으로 정리했습니다. 피드 발행 시각을 한국 시간으로 환산하면 10월 24일입니다. 이번 변경은 커넥터의 새로운 사용자 기능보다 **테넌트 전역 거버넌스의 관리 경로가 바뀌는 공지**에 가깝습니다.

원문은 `setFederatedConnectors` CLI 토글을 사용하지 않는 조직이라면 이 공지를 무시해도 된다고 명시합니다. 반대로 해당 토글을 스크립트나 운영 절차에 사용해 왔다면, 기존 명령의 설정값만 보고 접근 정책이 유지된다고 판단하지 않는 것이 중요합니다.

---

## 무엇이 바뀌나요?

기존의 별도 CLI 제어 대신, 커넥터와 에이전트의 접근 제어를 같은 테넌트 전역 설정에서 관리합니다.

| 구분 | 공지된 변경 |
|---|---|
| 기존 제어 | `setFederatedConnectors` CLI 토글 |
| 통합 기준 | **Allowed agent types** |
| 관리 경로 | Microsoft 365 admin center → Agent 365 → Allowed agent types |
| 영향을 받는 서비스 | Microsoft 365 관리 센터, Microsoft 365 Copilot, Copilot Connectors, Agent 365 설정 |
| 주된 확인 대상 | 커넥터 거버넌스와 테넌트 설정을 담당하는 Microsoft 365 관리자 |

**2026년 10월 30일부터** 모든 테넌트의 Copilot Connectors 페이지가 Allowed agent types 설정을 따르기 시작한다는 것이 핵심입니다. 커넥터 거버넌스는 더 이상 별도의 `setFederatedConnectors` CLI 제어에 의존하지 않게 됩니다.

## 일정은 두 단계로 구분해서 읽어야 합니다

| 시점 | 원문에 기재된 내용 |
|---|---|
| 2026년 8월 25일까지 | `setFederatedConnectors` CLI 토글 사용 중단 예정. 관련 스크립트·자동화·관리 절차를 새 설정 방식으로 전환하도록 안내 |
| 2026년 10월 30일부터 | 모든 테넌트의 Copilot Connectors 페이지에서 Allowed agent types 설정 적용 시작 |

주의할 점은 **10월 23일 수정된 공지에도 이미 지난 8월 25일 전환 권고가 그대로 남아 있다**는 사실입니다. 이를 새로운 미래 일정이나 추가 유예 기간으로 해석해서는 안 됩니다. 아직 전환하지 않은 조직은 현재 테넌트 상태를 확인하고, 10월 30일 적용을 앞두고 통합 설정을 우선 점검하는 것이 좋습니다.

이 공지는 프리뷰 또는 GA 기능 발표가 아니라 관리 제어의 전환 안내입니다. 명령이 실제로 언제부터 실행되지 않는지 등 원문에 없는 세부 동작을 별도로 단정하지는 않습니다.

## 아무것도 바꾸지 않으면 어떻게 되나요?

원문에 따르면 별도 조치를 하지 않은 테넌트는 **Allowed agent types의 기존 구성과 기본 정책 상태**에 따라 관리됩니다. 이것이 모든 조직에서 “자동 허용” 또는 “자동 차단”을 뜻하는 것은 아닙니다. 공지는 구체적인 기본값을 제시하지 않습니다.

따라서 관리자는 현재 Allowed agent types 구성이 조직의 커넥터 접근 의도와 일치하는지 직접 확인해야 합니다. 과거 CLI 토글에 의존했던 정책과 새 전역 설정의 실제 결과가 다를 수 있다는 점이 운영상 가장 중요한 확인 사항입니다.

## 도입·운영 담당자의 점검 순서

1. **의존성 확인:** 운영 스크립트, 자동화 작업, 관리자 실행 지침에서 `setFederatedConnectors`를 사용하는지 확인합니다. 사용하지 않는 조직은 원문의 비대상 안내를 참고합니다.
2. **전역 설정 검토:** Microsoft 365 관리 센터의 Agent 365에서 Allowed agent types를 열어 현재 구성이 의도한 커넥터 정책과 일치하는지 검토합니다.
3. **관리 절차 전환:** 기존 CLI 토글을 기준으로 작성된 운영 절차를 통합 설정 중심으로 갱신합니다. 원문은 대체 CLI 명령이나 자동화 API를 제시하지 않으므로 존재하지 않는 명령으로 치환해서는 안 됩니다.
4. **적용 결과 확인:** 10월 30일 적용 시작 전후로 커넥터 접근이 조직의 허용 정책대로 동작하는지 확인합니다. 이는 공지 내용을 바탕으로 한 운영 권고입니다.
5. **담당 팀 공유:** Microsoft 365 Copilot 운영, 보안 거버넌스, 커넥터 관리 담당자가 같은 정책 기준을 사용하도록 변경 내용을 공유합니다.

원문은 별도로 식별된 컴플라이언스 고려사항은 없다고 안내하면서도, 각 조직 상황에 맞게 검토하도록 덧붙였습니다. 따라서 이번 변경만으로 개별 조직의 컴플라이언스 검토가 불필요해진다고 해석해서는 안 됩니다.

## 마무리

이번 변경의 요지는 **커넥터와 에이전트의 전역 접근 정책을 Agent 365의 한 관리 경로로 모으는 것**입니다. 기존 CLI 설정에 의존해 왔다면 명령의 실행 여부보다, 앞으로 실제 정책 기준이 되는 Allowed agent types를 먼저 확인해야 합니다.

특히 10월 23일 수정 공지에 과거 전환 기한과 10월 30일 적용 시작일이 함께 담겨 있으므로, 날짜를 분리해 읽고 현재 테넌트 상태를 기준으로 대응하는 것이 중요합니다.

> 출처: **MC1454973 — Manage Copilot connectors (Global setting) from Agent 365 - SetFederatedConnectors CLI toggle is retiring**
>
> 원문: https://mc.merill.net/message/MC1454973
>
> Microsoft 365 Roadmap: https://www.microsoft.com/microsoft-365/roadmap — 관련 일정 확인용이며, 이 공지 본문에는 개별 Roadmap ID가 제시되어 있지 않습니다.
>
> **실제 출시 일정·기능은 변경될 수 있습니다.**
