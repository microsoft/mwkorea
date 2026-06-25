---
title: "텍스트를 넘어서는 Microsoft 365 Copilot: SharePoint Copilot Apps 등장"
date: 2026-06-23T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - SharePoint
  - SPFx
  - MCP
  - MCPApps
  - DeclarativeAgent
  - CopilotExtensibility
excerpt: "Copilot은 언어를 다루는 데 뛰어나지만, 업무는 말만으로 끝나지 않습니다. SharePoint Copilot Apps는 SPFx로 만든 풍부한 인터랙티브 UX 컴포넌트를 Copilot 캔버스 안으로 직접 가져와, 채팅을 떠나지 않고 결재·조회·예약 같은 일을 바로 처리하게 해 줍니다. 2026년 7월 초 미리 보기, 가을 정식 출시 예정입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 텍스트를 넘어서는 Microsoft 365 Copilot: SharePoint Copilot Apps 등장

Microsoft 365 Copilot은 언어를 다루는 데 탁월합니다. 하지만 우리의 업무는 '말'만으로 이루어지지 않습니다. 어떤 일은 채팅으로 길게 주고받으며 *설명*하기보다, 눈으로 **보고, 만지고, 바로 처리**하고 싶을 때가 있습니다. 경비를 승인하거나, 남은 연차를 확인하거나, 책상(좌석)을 예약하는 일 — 이런 작업을 적절한 도구를 찾아 헤매지 않고 채팅 안에서 그대로 끝낼 수 있다면 어떨까요?

Microsoft는 2026년 6월 23일 Microsoft 365 Developer Blog를 통해, 바로 그것을 가능하게 하는 **SharePoint Copilot Apps**를 공개했습니다. [SharePoint Framework(SPFx)](https://aka.ms/spfx)로 만든 풍부한 인터랙티브 UX 컴포넌트를 **Copilot 캔버스 안으로 직접** 가져오는 새로운 방식입니다.

이는 Copilot 캔버스의 [UX 컴포넌트](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugin-mcp-apps)를 **MCP Apps 모델** 위에서 구현한 것으로, 한국 기업이 이미 SharePoint·Teams에 쌓아 온 자산을 Copilot이라는 완전히 새로운 표면(surface)으로 확장한다는 점에서 의미가 큽니다.

{% include video id="mpSVo47LDHE" provider="youtube" %}

---

## 채팅과 텍스트는 강력하지만, 항상 충분하지는 않다

간단한 작업이 어떻게 긴 대화로 번지는지 떠올려 보세요. 무언가를 *빠르게 검토*받고 싶을 뿐인데, 필요한 *최신 도구*가 인트라넷에 있는지 아니면 전혀 다른 곳에 있는지부터 찾아야 합니다. 그 모든 것을 텍스트로 설명하는 데는 우리에게 없는 '시간'이 듭니다.

다른 앱·포털·도구로 한 번씩 건너뛸 때마다 집중이 깨지고, 수천 명에게 누적되면 그 시간은 어마어마해집니다. 바로 조직 전체에 부과되는 **상시적인 컨텍스트 스위칭 세금(context-switching tax)**입니다.

만약 필요한 경험이 **업무 흐름 속, Copilot 캔버스 안에 그냥 있다면** 어떨까요? 보고 싶거나 하고 싶은 것을 요청하면, 알맞은 UX 컴포넌트가 즉시 나타나 바로 사용할 수 있습니다. SharePoint Copilot Apps가 제공하는 것이 정확히 이것입니다. **목적에 맞게 설계된 UX 컴포넌트가, 유용한 바로 그 순간에 Copilot에 나타나** 사용자가 대화를 떠나지 않고 검토하고, 결정하고, 실행하게 합니다.

---

## 개발자 관점: 그냥 컴포넌트만 가져오세요

개발자가 가장 반길 부분이 여기입니다. Copilot UX 컴포넌트를 만들 때 신경 쓸 것은 **단 하나 — UX 컴포넌트를 만드는 것**뿐입니다. 나머지는 플랫폼이 모두 제공합니다.

게다가 **이미 알고 있는 JavaScript 스택**으로 만듭니다. SPFx는 React, Angular, Vue, Svelte, 순수 TypeScript 등 **원하는 어떤 JavaScript 라이브러리나 프레임워크든 지원**합니다. (예시에는 가장 널리 쓰이는 React가 자주 등장하지만, React가 필수는 아닙니다.) 팀이 이미 생산적으로 쓰는 도구로 출시할 수 있다는 것은 분명한 장점입니다.

이 표준 기반(standards-based) 토대는 또 다른 이점을 엽니다. **여러분의 AI 코딩 에이전트가 이미 이것을 만들 줄 안다**는 점입니다. 먼저 배워야 할 독자적 플랫폼이나 별도 런타임이 없기 때문에, **GitHub Copilot, Claude, Codex** 같은 도구는 물론 팀이 선호하는 어떤 코딩 에이전트든 IDE 안에서 이 컴포넌트를 스캐폴딩하고, 생성하고, 리팩터링하고, 디버깅할 수 있습니다. 실제로 코딩 에이전트는 SPFx 개발에 이미 매우 능숙합니다.

**핵심 개발 이점**

- **웹 스택 개발**: 팀이 이미 아는 기술과 프레임워크를 그대로 사용. 어떤 웹 개발자든, 선호하는 JavaScript 라이브러리로 만들 수 있음
- **독자 개발 플랫폼 불필요**: 개방적이고 익숙한 웹 기술 위에서, 업계 표준 패턴 기반으로 구축
- **자동 호스팅**: 어디에 호스팅할지 고민할 필요 없음. 외부 운영·관리도 불필요 — 솔루션이 고객 테넌트에 직접 호스팅됨
- **인프라 복잡성 없음**: Azure나 외부 호스팅 플랫폼 위에 무언가를 만들고 운영할 필요가 없음
- **엔터프라이즈급 보안·거버넌스**: SharePoint 플랫폼 기반이라, 조직이 이미 의존하는 보안·규정 준수·거버넌스가 기본 내장

무엇보다 이것은 **기존 투자를 Copilot 캔버스로 확장**하는 일입니다. 조직이 이미 만들어 둔 SPFx 컴포넌트와 패턴이 그대로 이어지며, 새로운 표면에 도달합니다. SPFx 생태계는 검증되지 않은 신생 토대가 아니라, **매일 수천만 명의 최종 사용자**가 맞춤형 SPFx 컴포넌트에 의존하는 거대한 기반입니다.

더 좋은 점은, 동일한 UX 컴포넌트가 하나의 표면에 묶이지 않는다는 것입니다. **한 번 작성해 Microsoft 365 전반에 노출** — **Copilot**, **SharePoint**, **Microsoft Teams** 어디서든 단일 컴포넌트를 재사용해, 사람들이 이미 일하는 모든 채널에 도달하고 투자 가치를 극대화합니다. 다시 만들지 말고, **이미 만든 것을 재사용**하세요.

{% include video id="ofgERb5Zlbo" provider="youtube" %}

---

## 어떤 것을 만들 수 있나: 예시 시나리오

그래서 실제로 무엇을 만들 수 있을까요? **이전에 SharePoint 포털이나 Teams 개인용 앱으로 노출했던 거의 모든 것**입니다. 한때 포털에서 웹 파트나 UX 요소로 노출하던 시나리오라면, 이제 에이전트를 활용해 **Copilot에 직접 UX 컴포넌트로** 노출할 수 있습니다. 같은 컴포넌트를 여러 위치에 동시에 노출해, 사용자가 선호하는 경험을 골라 동일한 기능에 접근하도록 할 수도 있습니다.

![SharePoint Copilot Apps 예시 시나리오](/mwkorea/assets/images/2026-06-23-SharePointCopilotApps/image1.webp)

가능성의 영역을 보여 주는 세 가지 예시입니다.

### 🏢 LOB(현업 업무) 에이전트

LOB 시스템의 정보를 Copilot 캔버스에 바로 노출 — 영업 정보, 차트로 표현된 비즈니스 데이터, 구내식당 메뉴, 재고, 칭찬(praise), 휴일, 휴가, 헬프데스크, 설문, Customer 360 뷰, 예약, 출장 예약, 경비, 급여명세서 등.

### 📣 사내 커뮤니케이션·서비스 에이전트

전형적인 인트라넷 시나리오를 Copilot UX 컴포넌트로 — 사용자 맞춤 뉴스, 최신 정보, 개인 대시보드, 조직 정보, 온보딩 작업, 시각적 Q&A, 지도 등.

### ⚙️ 관리·거버넌스 에이전트

관리·운영·거버넌스 작업을 앱으로 — 사이트 프로비저닝, 정책 적용, 사이트 대시보드 등 전형적인 거버넌스·관리 작업을 위한 UX 제공.

---

## 업계 표준 위에서, 엔터프라이즈 신뢰와 함께

SharePoint Copilot Apps는 업계 표준을 기반으로 **MCP Apps 모델**을 구현합니다. 닫힌 토대가 아니라 개방적이고 상호 운용 가능한 토대 위에서 만든다는 뜻입니다. 개방형 패턴, 락인(lock-in) 없음, 하나의 표면에 갇히지 않고 여러 표면에서 동작하는 컴포넌트 — 그리고 여러분의 스택을 이미 이해하는 도구(AI 코딩 에이전트 포함). 모든 원칙이 일관됩니다.

일반적인 MCP Apps 모델과의 **핵심 차이는 호스팅과 도구 라우팅이 자동**이라는 점입니다. UX 컴포넌트는 Microsoft 365 테넌트에 자동으로 호스팅되고, 요청은 알맞은 도구로 자동 라우팅됩니다. 설정하거나, 세우거나, 연결할 것이 없습니다. **컴포넌트만 가져오면 나머지는 플랫폼이 처리**합니다.

---

## 왜 중요한가

이 경험을 만들고 투자하는 사람들에게 가치는 분명합니다.

- **더 빠른 가치 실현(Time to value)**: 어떤 웹 개발자든 이미 아는 JavaScript 스택으로 만들 수 있고, AI 코딩 에이전트가 작업을 가속하므로, 보유한 팀과 역량 그대로 출시
- **더 낮은 총비용**: 새로 라이선스할 플랫폼도, 세우고 운영하고 보안을 책임질 인프라도 없음 — 내 테넌트에 호스팅됨
- **시작에 라이선스 장벽 없음**: [선언적 에이전트(declarative agents)](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent) 기반이라, Microsoft 365 사용자 라이선스만으로 기본 에이전트 경험을 시작 가능 (최신 요건은 [에이전트 기능 및 라이선싱 모델](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites#agent-capabilities-and-licensing-models) 참조)
- **투자 극대화**: 한 번 작성해 Copilot·SharePoint·Teams에서 재사용. 기존 SPFx 컴포넌트를 다시 만들지 않고 그대로 활용
- **리스크 감소**: 엔터프라이즈 보안·규정 준수·거버넌스가 덧붙이는 것이 아니라 기본 내장

---

## 출시 일정

| 단계 | 시점 | 비고 |
|------|------|------|
| 미리 보기(Preview) | **2026년 7월 초** | SharePoint Framework(SPFx) **v1.24** 미리 보기와 함께 제공 |
| 정식 출시(GA) | **2026년 가을 중** | 순차 롤아웃 |

---

## 한국 조직을 위한 시사점

- **"인트라넷 자산"이 곧바로 Copilot 자산으로**: SharePoint 포털·Teams 앱에 이미 구축한 웹 파트와 SPFx 컴포넌트가, 다시 만들 필요 없이 Copilot 캔버스로 확장됩니다. 인트라넷 투자가 많은 국내 대기업·공공 조직일수록 재사용 효과가 큽니다.
- **낮은 진입 장벽**: 별도 Azure 인프라나 독자 플랫폼 없이, M365 사용자 라이선스와 SPFx만으로 시작할 수 있어 PoC 부담이 작습니다.
- **거버넌스 친화적**: 테넌트 내부 호스팅 + SharePoint 기반 보안·규정 준수가 기본 내장되어, 데이터가 외부로 나가는 것을 꺼리는 보안팀 검토를 통과하기 수월합니다.
- **AI 코딩 에이전트와의 시너지**: GitHub Copilot·Claude·Codex 등으로 SPFx 컴포넌트를 빠르게 스캐폴딩·디버깅할 수 있어, 메이커·개발팀의 생산성을 첫날부터 끌어올릴 수 있습니다.

---

## 시작하기

인터랙티브 UX를 Copilot으로 가져오는 것은, 텍스트만으로는 불가능했던 AI 기반 업무 경험의 거대한 혁신 공간을 엽니다. 미리 보기가 출시되면 직접 시도해 보세요. Microsoft는 앞으로 몇 주에 걸쳐 더 많은 데모·영상·가이드·샘플을 오픈소스 및 커뮤니티 채널에서 공유할 예정이며, [주간 커뮤니티 콜](https://aka.ms/community/calls)과 [LinkedIn](https://www.linkedin.com/showcase/microsoft365dev/)·[X](https://x.com/microsoft365dev)에서 최신 소식을 확인할 수 있습니다.

---

> **원문**: [Going beyond text in Microsoft 365 Copilot – Introducing SharePoint Copilot Apps (Microsoft 365 Developer Blog)](https://devblogs.microsoft.com/microsoft365dev/going-beyond-text-in-microsoft-365-copilot-introducing-sharepoint-copilot-apps/) · 자세한 내용은 원문을 참조하세요.
