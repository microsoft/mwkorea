---
title: "Agent 365 2026년 6월 업데이트: 로컬 에이전트 가시성 강화와 온보딩 간소화"
date: 2026-07-08T00:00:00 KST
categories:
  - Copilot
tags:
  - Agent365
  - AIGovernance
  - MicrosoftPurview
  - MicrosoftDefender
  - MicrosoftEntra
  - MicrosoftGraph
  - LocalAgents
  - Security
excerpt: "Agent 365의 2026년 6월 업데이트가 공개되었습니다. 로컬 에이전트를 위한 레지스트리·Purview 감사·Defender 보호·격리 실행 컨테이너가 강화되고, Agent 365 Skills로 온보딩이 간소화되며, Graph API와 Entra ID Governance가 확대됩니다. Agent 365가 엔터프라이즈 에이전트의 통제 계층(control plane)으로서 한 걸음 더 진화했습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Agent 365 2026년 6월 업데이트: 로컬 에이전트 가시성 강화와 온보딩 간소화

AI 에이전트가 엔터프라이즈 운영의 핵심 축으로 자리 잡으면서, 조직은 클라우드·로컬·파트너 개발 환경에 걸쳐 점점 더 분산되는 에이전트 생태계를 **일관된 방식으로 관찰·관리·거버넌스·보안**할 방법이 필요해졌습니다. [지난 5월 정식 출시(GA)](https://techcommunity.microsoft.com/blog/agent-365-blog/whats-new-in-agent-365-may-2026/4516340) 이후에도 Agent 365는 **엔터프라이즈 에이전트의 통제 계층(control plane)**으로 계속 진화하고 있습니다.

2026년 6월 업데이트는 세 가지 방향에 집중합니다. **로컬 에이전트에 대한 가시성과 보호 강화**, **온보딩과 수명주기 관리 간소화**, 그리고 **프로그래매틱 거버넌스 기능 확장**입니다. 이번 글에서는 이 업데이트를 하나씩 정리해 드립니다.

---

## 로컬 에이전트를 위한 가시성·통제·보호

사용자 디바이스에서 직접 실행되는 **로컬 에이전트**가 엔터프라이즈 AI 환경의 비중 있는 한 축으로 자리 잡으면서, Agent 365는 이 영역에 대한 종단 간(end-to-end) 가시성·거버넌스·보호를 확장하고 있습니다. Agent 365 레지스트리에서 로컬 에이전트를 발견·인벤토리화하는 것부터, Microsoft Purview로 에이전트 활동을 감사하고, Microsoft Defender로 런타임 동작을 보호하며, Microsoft Execution Containers(MXC)로 격리 실행을 강제하는 것까지 — 사용자 생산성을 희생하지 않으면서도 로컬 에이전트를 안심하고 관리·보안·거버넌스할 수 있는 통제 수단을 확보하게 됩니다.

### Agent 365 레지스트리의 로컬 에이전트 (공개 미리보기)

조직이 사용자 디바이스에서 직접 실행되는 로컬 에이전트에 점점 더 의존하게 되었지만, 이런 에이전트는 종종 AI 가시성 범위 밖에서 동작해 왔습니다. 이번 업데이트로 **로컬 에이전트가 Agent 365 레지스트리에 공개 미리보기로 추가**되어, IT·보안팀이 환경 전반에서 감지된 섀도우(shadow) 로컬 에이전트를 통합된 시야로 확인할 수 있게 됩니다.

레지스트리는 각 에이전트의 **게시자(publisher), 감지된 디바이스 수, 마지막 스캔 일자**를 보여주고, 에이전트별 상세 화면으로 들어가면 해당 에이전트가 관측된 모든 엔드포인트를 디바이스 이름·모델·운영체제와 함께 목록으로 확인할 수 있습니다. 관리 대상 엔드포인트 전반에서 로컬 에이전트의 발견과 디바이스 수준 컨텍스트를 중앙화함으로써, 팀은 사용자가 어떤 섀도우 AI 에이전트를 실행하고 있는지 짚어내고, 디바이스별로 그 범위를 파악하며, 조사 속도를 높일 수 있습니다.

![Agent 365 레지스트리의 로컬 에이전트 화면](/mwkorea/assets/images/2026-07-08-Agent365JuneUpdate/image1.png)

### GitHub Copilot CLI, Claude Code, OpenAI Codex, OpenClaw까지 확대된 Microsoft Purview 감사 범위

Agent 365의 **Microsoft Purview Audit**은 사람-에이전트, 에이전트-에이전트, 에이전트-도구 상호작용 전반에서 접근·행동·활동에 대한 풍부한 컨텍스트 메타데이터를 담은 감사 로그를 캡처·모니터링해 왔습니다. 이번 6월 업데이트에서는 이 감사 범위가 **GitHub Copilot CLI, Claude Code, OpenAI Codex, OpenClaw**를 포함한 신흥 로컬·개발자 중심 에이전트로 확장됩니다.

이를 통해 조직은 점점 더 분산되는 에이전트 사용 환경에서도 이런 로컬 에이전트 전반의 활동을 일관되게 감사할 수 있게 되어, 가시성 공백을 메울 수 있습니다. 익숙한 Microsoft Purview 감사 워크플로가 이 새로운 에이전트 경험까지 확장됨에 따라, 기업은 사고를 더 효과적으로 조사하고, 컴플라이언스 요건을 충족하며, 종단 간의 포괄적인 관찰 가능성을 갖추고 자신 있게 AI 도입을 확장할 수 있습니다.

### Microsoft Defender와 Purview, 로컬 에이전트까지 보안 역량 확장 (공개 미리보기)

Agent 365의 **Microsoft Defender**는 로컬 AI 에이전트를 위한 보안 태세 관리, 온디바이스 런타임 보호, XDR 경고, 고급 헌팅(advanced hunting) 기능을 확장합니다. 6월 2일 릴리스 이후 Defender는 관리 대상 Windows·macOS 디바이스 전반에서 로컬 에이전트와 MCP 서버 발견 범위를 넓혀, 이제 미리보기 상태에서 **35개 이상의 알려진 에이전트 유형**을 지원합니다. 이번 릴리스에서는 로컬 에이전트의 **노출 위험(exposure risk)** 개념도 도입되어, 보안팀이 구성·권한·노출도를 기준으로 가장 위험도가 높은 로컬 에이전트를 식별하고 우선순위를 정하며, 위험을 낮추기 위한 권고까지 받을 수 있습니다.

공개 미리보기로 제공되는 Defender의 온디바이스 런타임 보호 기능은 **Claude Code, GitHub Copilot CLI, GitHub Copilot 앱, Codex CLI, OpenClaw** 및 유사한 Node 기반 클로(claw)들을 대상으로, 에이전트 네이티브 이벤트 검사와 온디바이스 네트워크 기반 런타임 검사를 활용합니다. Defender는 프롬프트 인젝션 시도를 통해 유입된 악성 지시를 감사하거나 차단할 수 있으며, 공격이 감지되면 Microsoft Defender XDR 경고를 생성합니다. Microsoft Purview와의 통합은 Purview 정책에 기반해 프롬프트와 도구 호출을 실시간으로 감사·차단함으로써 민감 데이터 유출 방지 보호를 확장합니다. 고급 헌팅을 통해 보안팀은 로컬 에이전트 활동을 조사하고, 노출 위험을 헌팅하며, 에이전트 인벤토리를 기존 엔드포인트 텔레메트리와 상호 연관 지을 수 있습니다.

### 로컬 에이전트를 위한 Microsoft Execution Containers (공개 미리보기)

조직이 사용자 디바이스에서 직접 실행되는 로컬 AI 에이전트를 도입하면서, 가시성·통제·위험에 관한 새로운 과제가 함께 따라옵니다. 이런 에이전트는 종종 전통적인 거버넌스 경계 밖에서 동작하고, 민감한 데이터나 도구에 접근할 수 있으며, 관리되지 않는 환경에서 실행될 수 있습니다. **Microsoft Execution Container(MXC)**는 로컬 에이전트를 위한 안전하고 격리된 런타임을 강제함으로써 이 문제를 해결하고, 이들을 중앙 관리 통제 아래로 되돌려 놓습니다.

공개 미리보기 상태의 MXC를 통해 IT는 로컬 에이전트가 강화된(hardened) Windows 컨테이너 안에서 실행되도록 요구할 수 있으며, 이를 통해 관리되지 않는 실행으로 인한 노출을 줄이고 전체 환경에 걸쳐 보안 보호를 표준화할 수 있습니다. 격리와 중앙 정책 시행을 결합함으로써, MXC는 조직이 로컬 에이전트 사용에 대해 더 큰 확신을 가질 수 있도록 하고, 런타임 동작에 대한 가시성을 높이며, 일관된 거버넌스를 가능케 하고, 사용자 생산성을 저해하지 않으면서 데이터 유출이나 악성 활동의 위험을 완화합니다.

![Microsoft Execution Containers 격리 실행 개념도](/mwkorea/assets/images/2026-07-08-Agent365JuneUpdate/image2.png)

---

## 에이전트 온보딩과 엔터프라이즈 에이전트 플릿 관리를 위한 새 기능

조직에는 엔터프라이즈 준비 상태로 가는 더 빠른 경로와, 지속적인 거버넌스를 위한 더 강력한 통제가 필요합니다. Agent 365는 **Agent 365 Skills**로 에이전트 온보딩을 간소화하고, **Microsoft Graph API**로 프로그래매틱 관리를 확장하며, **Microsoft Entra ID Governance**를 생태계 파트너 에이전트까지 확장함으로써 이 두 목표를 함께 발전시킵니다.

### Agent 365 Skills로 빌더의 에이전트 온보딩 가속화

**Agent 365 Skills**를 통해 에이전트 개발자는 자신의 에이전트를 Microsoft Agent 365로 가져오는 과정을 대폭 단순화할 수 있습니다. [관련 블로그 포스트](https://techcommunity.microsoft.com/blog/agent-365-blog/agent-365-skills-bring-your-agents-into-microsoft-agent-365-in-minutes/4529838)에서 설명하듯, 이 혁신은 기존에 개발자가 아이덴티티·관찰 가능성·거버넌스·Microsoft 365 데이터에 대한 안전한 접근을 수동으로 구성해야 했던 온보딩의 "마지막 단계" 마찰을 제거합니다.

Agent 365 Skills를 사용하면 개발자는 선호하는 코딩 환경 안에서 자연어로 직접 "관찰 가능성 추가"나 "도구 통합" 같은 원하는 결과를 요청할 수 있고, 플랫폼이 필요한 구성을 자동으로 적용·검증합니다. 복잡한 다단계 설정을 안내형(guided), 결과 지향(outcome-driven) 경험으로 전환함으로써, Agent 365 Skills는 엔터프라이즈 준비 완료까지 걸리는 시간을 단축하고, 조직이 더 빠르고 자신 있게 AI 에이전트를 대규모로 운영할 수 있도록 돕습니다.

![Agent 365 Skills를 통한 온보딩 화면](/mwkorea/assets/images/2026-07-08-Agent365JuneUpdate/image3.png)

### 확장된 Microsoft Graph API 지원

Agent 365는 Microsoft Graph API의 범위를 계속 확장하여, AI 관리자에게 에이전트 생태계에 대한 강력한 프로그래매틱 제어권을 부여합니다. [Agent 365 Graph API 문서](https://learn.microsoft.com/microsoft-agent-365/admin/graph-api)에서 설명하듯, 이 API들은 수동 또는 UI 기반 워크플로를 넘어 엔터프라이즈급 거버넌스·리포팅·수명주기 자동화를 지원하는 확장 가능하고 자동화된 에이전트 관리를 가능하게 합니다.

큰 틀에서 Agent 365 Graph API는 관리자가 다음을 수행할 수 있게 합니다.

- 조직 전체 에이전트의 완전한 인벤토리 조회
- 감사·컴플라이언스·수명주기 관리를 위한 상세 메타데이터 접근
- 온보딩, 거버넌스 워크플로, 운영 프로세스의 대규모 자동화
- 에이전트 차단, 차단 해제, 소유권 재할당 같은 관리 작업 수행

이런 기능은 IT팀이 에이전트 관리를 기존 툴체인과 워크플로에 통합해 가시성·일관성·통제력을 높이는 데 도움이 됩니다.

이번 릴리스의 일환으로, 두 가지 기본 패키지 관리 API인 **List packages**와 **Get package details**가 베타에서 **Microsoft Graph v1.0**으로 이전되어, 프로덕션 수준 자동화를 향한 중요한 걸음을 내디뎠습니다. 단, 이 패키지 관리 API는 에이전트만 반환하며 앱과 추가 기능(add-in)은 API 응답에 포함되지 않는다는 점에 유의하세요. 이 API를 통해 AI 관리자는 다음을 할 수 있습니다.

- **List packages** (`GET /copilot/admin/catalog/packages`): 거버넌스와 리포팅을 위해 조직 내 모든 에이전트의 전체 인벤토리 조회
- **Get package details** (`GET /copilot/admin/catalog/packages/{id}`): 구성, 소유권, 배포 세부 정보를 포함한 특정 에이전트의 풍부한 메타데이터 접근

더불어 고객 피드백에서 직접 도출된 몇 가지 핵심 개선 사항도 함께 도입됩니다.

- **역할 기반 접근 확대**: Global Reader와 AI Reader 역할 지원으로, 상위 관리자 권한 없이도 이 API에 대한 읽기 전용 가시성을 확보할 수 있어 위임과 운영 유연성이 향상됩니다.
- **애플리케이션 권한 지원**: 고객은 이제 앱 전용(app-only) 권한으로 이 API를 호출할 수 있어, 안전한 무인(unattended) 자동화 시나리오가 가능해집니다.

이 API들을 Graph API v1.0으로 가져옴으로써, Agent 365는 인벤토리 리포팅, 컴플라이언스 점검, 수명주기 관리 워크플로 같은 맞춤형 자동화 솔루션을 Microsoft Graph 위에 직접 구축할 수 있는 더 안정적이고 지원되는 기반을 제공합니다. 이는 Agent 365가 엔터프라이즈 에이전트 거버넌스의 통제 계층으로서의 역할을 한층 강화하여, 관리자가 사용자·애플리케이션 관리에 쓰던 것과 동일한 엄격함·규모·자동화로 에이전트를 관리할 수 있게 합니다. Agent Package Management API에 대해 더 알아보려면 [여기](https://learn.microsoft.com/microsoft-365/copilot/extensibility/api/admin-settings/package/overview)를 참고하세요.

### 생태계 파트너 에이전트를 위한 Microsoft Entra ID Governance

에이전트 자격(entitlement)을 위한 **Microsoft Entra ID Governance**는 검증된 아이덴티티 거버넌스 통제를 AI 워크포스에 적용하여, 조직이 범위화된 권한(scoped permission), 소유권 책임, 시한부 접근을 통해 사람 사용자와 동일한 엄격함으로 에이전트 접근을 관리할 수 있게 합니다. 6월 업데이트로 이 지원 범위가 **Agent 365 SDK를 통해 통합된 생태계 파트너 에이전트**까지 확장되어, 기업은 내부에서 개발한 에이전트와 서드파티 에이전트 모두에 걸쳐 일관되게 자격 관리를 적용할 수 있습니다.

이를 통해 이런 에이전트들이 접근 패키지(access package), 수명주기 워크플로, 최소 권한(least-privilege) 원칙을 통해 거버넌스되도록 보장하여 과도하게 프로비저닝된 에이전트의 위험을 줄입니다. 이는 통합된 대규모 접근 거버넌스를 제공하여, 내부 및 파트너 구축 에이전트 전반으로 에이전트 생태계가 확장됨에 따라 정책을 시행하고 컴플라이언스를 유지하며 명확한 소유권과 책임을 제공하는 데 도움이 됩니다.

---

## 마무리

2026년 6월 업데이트는 Agent 365를 엔터프라이즈 에이전트의 통제 계층으로 계속 발전시킵니다. 로컬 에이전트에 대한 가시성과 보안을 확장하고, 엔터프라이즈 온보딩을 간소화하며, 자동화와 거버넌스 기능을 강화함으로써, Agent 365는 조직이 더 큰 확신·통제력·운영 우수성을 갖고 AI 도입을 확장할 수 있도록 돕습니다.

### 다음 단계

- [Microsoft 365 admin center에서 Agent 365 시작하기](https://admin.cloud.microsoft/)
- [MS Learn에서 Agent 365 자세히 알아보기](https://review.learn.microsoft.com/microsoft-agent-365/overview?branch=main&branchFallbackFrom=pr-en-us-416)

---

> **원문**: [What's new in Agent 365 – June 2026 (Microsoft Tech Community, Agent 365 Blog, 2026-07-08, 작성: Alex Pozin, Samer Baroudi, Brendan Powers)](https://techcommunity.microsoft.com/t5/agent-365-blog/what-s-new-in-agent-365-june-2026/ba-p/4535107)
>
> 자세한 내용은 원문을 참조하세요.
