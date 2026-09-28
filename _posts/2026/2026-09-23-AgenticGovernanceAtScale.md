---
title: "에이전트가 늘수록 거버넌스도 달라져야 합니다: 관찰·위험 평가·자동 대응의 운영 루프"
date: 2026-09-23T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Agent365
  - AgenticGovernance
  - Observability
  - PowerPlatform
  - Security
excerpt: "Copilot Studio 에이전트가 실제 업무로 확산되면, 출시 전 심사와 목록 관리만으로는 충분하지 않습니다. Microsoft가 제시한 지속적 관찰, 위험에 비례하는 대응, 정책 기반 자동화의 운영 모델과 한국 기업의 도입 체크포인트를 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트가 늘수록 거버넌스도 달라져야 합니다: 관찰·위험 평가·자동 대응의 운영 루프

에이전트를 만드는 팀이 늘어나는 것은 좋은 신호입니다. 하지만 IT 운영팀에는 새로운 질문이 쌓입니다. 우리 조직에 어떤 에이전트가 있고, 누가 책임지며, 어떤 데이터에 접근하고, 비용과 상태는 어떻게 달라지고 있을까요?

Microsoft Copilot Studio Blog는 2026년 9월 22일 UTC, 한국 시간으로 9월 23일 공개한 글에서 **에이전트 확산에 맞춰 거버넌스 자체도 지속적으로 관찰하고 대응하는 운영 모델로 바뀌어야 한다**고 설명했습니다. 에이전트를 출시할 때 한 번 심사하는 것뿐 아니라, 운영 중 권한·도구·소유자·사용량의 변화를 계속 살펴야 한다는 이야기입니다.

이 글은 특정 기능의 GA나 프리뷰 출시 공지가 아니라, 2026년 10월 Microsoft Power Platform Conference(PPCC)를 앞두고 제시한 운영 방향입니다. 아래에서는 원문의 세 가지 원칙을 정리하고, 조직에서 적용할 때 고려할 점을 구분해 설명합니다.

![Copilot Studio와 기업의 에이전트 운영을 소개하는 원문 대표 이미지](/mwkorea/assets/images/2026-09-23-AgenticGovernanceAtScale/image1.png)

---

## 1. 목록을 넘어, 에이전트의 변화를 계속 관찰하기

에이전트 목록은 출발점이지 운영의 완성은 아닙니다. 원문이 강조하는 관찰 대상은 **소유권, ID, 접근 권한, 사용량, 상태, 행동**입니다.

예를 들어 제작자가 새 도구를 연결하거나, 관리자가 소유자를 바꾸거나, 운영 환경에서 예상하지 못한 사용 패턴이 나타날 수 있습니다. 처음 승인할 때 안전했던 에이전트도 이런 변화 이후에는 다시 평가해야 할 수 있습니다. 텔레메트리로 활동과 행동을 살피는 **observability(관측 가능성)**가 일회성 점검이 아니라 지속적인 운영 요건인 이유입니다.

조직 전체를 보려면 플랫폼 간 경계도 넘어야 합니다. Copilot Studio로 만든 에이전트뿐 아니라 서드파티 플랫폼과 자체 개발 에이전트도 함께 운영되기 때문입니다. 원문은 Microsoft Agent 365 같은 공통 관리 계층을 통해 플랫폼별로 흩어진 신호를 연결하고, 위험·사용량·비용·상태의 변화를 관리 가능한 정보로 만드는 방향을 설명합니다.

![Agent 365 Agents Map에서 에이전트 관계와 운영 상태를 살펴보는 원문 화면](/mwkorea/assets/images/2026-09-23-AgenticGovernanceAtScale/image2.gif)

원문은 Agents Map을 에이전트가 전체 생태계에서 어디에 위치하고, 다른 에이전트와 어떻게 연결되며, 시간에 따라 어떻게 동작하는지 시각화하는 예로 소개합니다. 다만 이 글만으로 모든 플랫폼의 모든 에이전트가 별도 구성 없이 자동 연결된다고 해석해서는 안 됩니다.

## 2. 모든 에이전트를 똑같이 심사하지 않기

승인된 사내 문서로 질문에 답하는 에이전트와 민감한 데이터에 접근해 운영 시스템을 변경하는 에이전트는 위험이 다릅니다. 모두에게 같은 수동 심사를 요구하면 저위험 업무까지 막히고, 반대로 모두를 간단히 통과시키면 고위험 동작을 놓칠 수 있습니다.

Microsoft가 제안하는 기준은 **위험에 비례하는 대응**입니다. 에이전트의 ID, 권한, 접근 데이터, 자율성, 수행 가능한 작업을 함께 살펴 적용 정책과 추가 검토 필요성을 판단합니다.

원문에 등장하는 예는 새 데이터 원본 연결입니다.

| 변화와 맥락 | 대응 방향 |
|---|---|
| 새 접근 권한이 기존 정책과 위험 허용 범위 안에 있음 | 추가 개입 없이 기존 통제 안에서 운영할 수 있음 |
| 민감한 데이터 접근 등 더 높은 위험을 도입함 | 더 강한 통제 또는 사람의 검토가 필요할 수 있음 |
| 기존 정책으로 적절한 대응을 결정하기 어려움 | 판단 가능한 담당자에게 전달할 기준이 필요함 |

![여러 플랫폼의 에이전트를 위험 수준에 따라 바라보는 원문 개념도](/mwkorea/assets/images/2026-09-23-AgenticGovernanceAtScale/image3.png)

중요한 것은 **사용한 플랫폼 이름만으로 위험을 확정하지 않는 것**입니다. 실제 데이터 접근과 실행 권한, 자율 동작의 범위가 함께 판단 기준이 되어야 합니다. 원문의 개념도 역시 제품별 보안 등급표가 아니라, 전체 에이전트 환경을 위험 관점에서 보자는 설명으로 이해하는 것이 적절합니다.

원문은 Microsoft 내부에서도 이러한 위험 기반 감독 원칙을 적용하고 있다고 설명하며, PPCC에서 Copilot Studio, Agent 365, Microsoft Defender, Microsoft Purview를 아우르는 접근을 공유할 예정이라고 안내합니다.

## 3. 정해진 정책 안에서는 자동으로 대응하기

변화를 관찰하고 위험을 평가한 다음, 같은 대응을 매번 사람이 실행해야 할까요? 원문은 반복 가능한 거버넌스 업무를 다음과 같은 루프로 설명합니다.

**Observe → assess → act → escalate**

![관찰, 평가, 실행, 담당자 전달로 이어지는 거버넌스 운영 루프](/mwkorea/assets/images/2026-09-23-AgenticGovernanceAtScale/image4.png)

1. **관찰**: 운영에 영향을 주는 신호나 변화를 감지합니다.
2. **평가**: 조직이 정한 정책과 에이전트의 맥락을 기준으로 판단합니다.
3. **실행**: 적절한 대응이 명확하고 허용된 범위 안에 있으면 자동 통제를 실행합니다.
4. **담당자 전달**: 정책 경계를 벗어나거나 별도의 판단이 필요하면 사람에게 넘깁니다.

핵심은 모든 결정을 AI에 맡기는 것이 아닙니다. **이미 어떻게 결정해야 하는지 알고 있는 반복 업무를 자동화하는 것**입니다. 정책 설정, 위험 허용 수준, 사람의 판단이 필요한 경계에 대한 책임은 계속 사람에게 있습니다.

이 모델에서 IT와 Center of Excellence(CoE)의 역할도 달라집니다. 에이전트를 하나씩 검사하고 설정하는 업무에서, 신뢰할 수 있는 운영 패턴과 위험 기준, 개입 조건을 설계하는 업무로 무게중심이 이동합니다.

원문은 PPCC의 Agentic Governance 세션에서 실시간 인벤토리와 텔레메트리, 자동 통제와 보안, 그리고 기업 거버넌스를 확장하는 계층으로서의 Power Platform API를 다룰 예정이라고 설명합니다. 특정 API 호출만으로 위 루프 전체가 완성된다는 구현 안내는 아닙니다.

## 원문 영상으로 살펴보기

아래는 원문에 실제로 포함된 Microsoft Medius 영상입니다.

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.34%; overflow: hidden;"><iframe src="https://medius.microsoft.com/Embed/video-nc/7541e375-99de-45df-91cc-99b5e0cfa02e?r=513044258042" title="Product Week" allowfullscreen allow="fullscreen; picture-in-picture" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" sandbox="allow-scripts allow-same-origin allow-forms"></iframe></div>

## 한국 기업에서 시작할 도입 체크포인트

다음은 원문의 원칙을 국내 조직의 운영에 적용하기 위한 제안이며, Microsoft가 발표한 필수 제품 설정이나 자동 제공 기능 목록은 아닙니다.

| 점검 영역 | 먼저 정할 내용 |
|---|---|
| 책임과 식별 | 에이전트별 업무 소유자, 기술 담당자, 실행 ID, 소유자 변경 시 인수인계 기준 |
| 접근과 행동 | 개인정보·기밀정보 접근 여부, 읽기와 쓰기 권한, 외부 전송 및 운영 시스템 변경 범위 |
| 변화 감지 | 데이터 원본·도구·권한 변경과 사용량·비용·오류 증가를 어떤 신호로 볼지 |
| 위험별 통제 | 표준 승인으로 처리할 범위와 추가 보안·업무 검토가 필요한 조건 |
| 자동화 경계 | 자동으로 실행 가능한 조치와 사람이 승인하거나 판단해야 하는 조치 |
| 운영 책임 | 알림 수신자, 예외 처리 담당자, 결정과 대응 이력을 남기는 방법 |

처음부터 모든 판단을 자동화하기보다는, 책임자가 명확한 소규모 에이전트 집합에서 시작하는 편이 현실적입니다. 먼저 변화를 볼 수 있게 만들고, 위험 기준을 합의한 뒤, 반복되는 대응부터 자동화하는 순서입니다.

개발팀은 [Agent 365 observability 문서](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/observability)에서 실제 계측 방식을 확인할 수 있습니다. **수집 시점에 확인한 문서는 Microsoft OpenTelemetry Distro 사용을 안내하고, 기존 접근도 호환성을 유지한다고 설명합니다.** 이는 운영 방향을 다룬 원문과 별도로 확인한 구현 문서 정보입니다. 실제 적용 전에는 최신 문서에서 SDK와 인증·권한 요건을 다시 확인해야 합니다.

## PPCC에서 이어지는 논의

원문은 2026년 10월 PPCC에서 이 주제를 더 깊게 다룰 예정이라고 안내합니다. 원문 배너의 행사 일정은 **2026년 10월 27~29일, 라스베이거스**입니다.

![2026년 10월 27일부터 29일까지 라스베이거스에서 열리는 PPCC 안내 배너](/mwkorea/assets/images/2026-09-23-AgenticGovernanceAtScale/image5.png)

관심사에 따라 다음 세션과 워크숍을 살펴볼 수 있습니다.

- [Governance of All Your Agents at Scale](https://powerplatformconf.com/sessions/Governance-of-all-your-agents-at-scale): 전체 에이전트 환경의 거버넌스
- [How Microsoft Does IT: Managing and Governing Agents with Risk-Aligned Oversight](https://powerplatformconf.com/sessions/How-Microsoft-Does-IT%3A-Managing-and-Governing-Agents---Empower-with-Risk-Aligned-Oversight): Microsoft 내부의 위험 기반 운영
- [Agent 365: Securely Managing and Governing Agents at Scale](https://powerplatformconf.com/workshops/Agent-365%3A-Securely-Managing-and-Governing-Agents-at-Scale): Agent 365 통제와 운영 실무
- [Agentic Governance: Secure, Govern, and Operate Your Power Platform at Scale](https://powerplatformconf.com/sessions/Agentic-Governance%3A-Secure%2C-Govern%2C-and-Operate-Your-Power-Platform-at-Scale): 관측 정보와 자동 통제를 연결하는 접근
- [Governance First, Agents at Scale: How Wells Fargo Built Copilot Studio Agents in a Regulated Bank](https://powerplatformconf.com/sessions/Governance-First%2C-Agents-at-Scale%3A-How-Wells-Fargo-Built-Copilot-Studio-Agents-in-a-Regulated-Bank): 규제 산업의 에이전트 구축 사례

행사와 세션 안내는 원문 시점 기준입니다. 이 글은 특정 기능의 출시일, 라이선스 포함 범위 또는 한국 지역의 제공 여부를 확정하지 않습니다.

## 마무리

에이전트 확산의 다음 과제는 단순히 심사 인력을 늘리는 것이 아닙니다. **변화를 지속적으로 보고, 실제 위험에 맞게 대응하며, 정해진 정책 안의 반복 업무를 자동화하는 운영 구조**를 만드는 것입니다.

그 과정에서 사람의 역할이 사라지는 것도 아닙니다. 사람이 책임져야 할 판단에 더 집중할 수 있도록, 언제 자동화하고 언제 개입할지를 분명하게 설계하는 것이 agentic governance의 핵심입니다.

> **출처**: [Governance is becoming agentic, too: How enterprises can operate AI at scale](https://techcommunity.microsoft.com/t5/copilot-studio-blog/governance-is-becoming-agentic-too-how-enterprises-can-operate/ba-p/4556820) — Microsoft Tech Community, Microsoft Copilot Studio Blog, 2026년 9월 22일 UTC. 자세한 내용은 원문 참조.
