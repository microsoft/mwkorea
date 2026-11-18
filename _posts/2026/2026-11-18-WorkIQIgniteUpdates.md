---
title: "업무 맥락을 아는 에이전트로: Ignite 2026 Work IQ의 실행과 거버넌스"
date: 2026-11-18T00:00:00 KST
categories:
  - Copilot
tags:
  - WorkIQ
  - Ignite2026
  - MCP
  - CopilotStudio
  - Governance
excerpt: "Work IQ가 이벤트 반응, SharePoint 작업, 업무 애플리케이션 맥락과 외부 AI 도구 연결로 확장됩니다. 읽기와 실행 권한의 분리, LLM 외부의 정책 집행, 기능별 프리뷰 상태를 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 업무 맥락을 아는 에이전트로: Ignite 2026 Work IQ의 실행과 거버넌스

좋은 모델만으로는 우리 회사의 고객, 과거 결정, 진행 중 업무를 알 수 없습니다. Microsoft의 Work IQ는 Copilot과 에이전트를 조직 지식·업무 데이터·도구에 연결하는 업무 인텔리전스 계층입니다.

Ignite 2026 발표는 맥락을 읽는 데서 실제 실행으로 나아가는 기능과 이를 통제할 정책을 함께 다룹니다. 개발자는 연결 작업을 줄이고, IT는 에이전트마다 제각각인 권한 대신 공통 가드레일을 적용하는 방향입니다.

![Work IQ Ignite 2026 원문 대표 이미지](/mwkorea/assets/images/2026-11-18-WorkIQIgniteUpdates/image1.png)

---

## 이벤트를 듣고, 실제 작업을 수행

새 **Listen** 기능은 새 메시지나 업무 이벤트가 발생했을 때 에이전트가 반응하도록 합니다. 사용자의 요청이나 반복 폴링을 기다리는 방식에서 벗어나 장기 작업을 진행하고 필요한 정보를 다시 요청하는 흐름입니다.

Word·Excel·PowerPoint 콘텐츠 생성·편집 지원은 원문에서 **예정 기능**으로 소개합니다. 이미 모두 제공된다고 해석하면 안 됩니다.

Work IQ API의 새 SharePoint 도구는 목록·라이브러리·승인·Quick Steps·버전 관리 등 **60개 이상 기본 작업**을 제공합니다. “트래커 만드는 방법”을 설명하는 데서 실제 트래커를 만드는 에이전트로 확장하는 기반이며, SharePoint Copilot과 Cowork의 도구와 연결됩니다.

## 더 넓어진 업무 맥락과 메모리

원문은 Microsoft 365 전체 규모로 데이터 **19.5엑사바이트**, 주당 Teams 채팅·채널 메시지 **150억 건**, 이메일 송수신 **900억 건**, SharePoint·OneDrive 신규 파일 **100억 개**를 제시합니다. Work IQ 기반 Copilot은 분당 **30만 개 아티팩트**에 걸쳐 추론할 수 있다고 설명합니다. 이는 서비스 전체에 관한 수치이지 개별 에이전트의 처리량 보장이 아닙니다.

새 맥락의 범위는 다음과 같습니다.

| 영역 | 발표 내용 |
|---|---|
| Business Applications | Dynamics 365의 ERP(프리뷰)·CRM, Power Platform 데이터를 M365 맥락과 결합 |
| Teams 실시간 대화 기록 | 회의 진행 중에도 회의 콘텐츠 활용 |
| Engage | 사람·팀·업무 방식에 관한 신뢰할 수 있는 조직 데이터 결합, 프리뷰 |
| Memory | 세션과 제품을 넘어 중요한 맥락 유지 |

이를 바탕으로 이메일·회의와 영업 기회를 함께 보거나, Cowork·Autopilot·Code에서 결과물을 만드는 작업에 조직 맥락을 활용할 수 있습니다.

![Work IQ의 업무 맥락 확장 관련 원문 이미지](/mwkorea/assets/images/2026-11-18-WorkIQIgniteUpdates/image2.png)

## 권한은 LLM 밖에서 집행

관리자는 관리 센터에서 에이전트 행동의 **테넌트 전체 상한**을 정합니다. 예를 들어 읽기·생성·수정은 허용하되 삭제는 금지할 수 있습니다. 개별 에이전트 정책은 이 범위를 더 좁힐 수 있지만 넓힐 수는 없습니다.

Agent 365에 등록된 에이전트는 제작자가 정책을 제안하고 관리자가 승인·거부합니다. Work IQ는 에이전트 자체 신원을 사용해 **매 호출마다 정책을 검사**하며, CRM·ERP의 기존 권한과 업무 스킬도 존중하도록 설계되었습니다.

새 **WorkIQ.Read**와 **WorkIQ.Act** 권한은 Microsoft 365·업무 애플리케이션·연결 소스 전반에서 읽기와 실행을 구분합니다. 정책은 작업을 허용·차단하거나 사람의 확인을 먼저 요구할 수 있습니다. 단순히 시스템 프롬프트에 금지사항을 쓰는 것과는 다른 통제 계층입니다.

## 프롬프트 인젝션과 출처 신뢰

에이전트에 콘텐츠를 전달하기 전 도구 접근 권한이 없는 격리 모델로 입력을 정제해 프롬프트 인젝션 위험을 줄이는 접근도 소개됩니다. 데이터의 출처·무결성·신뢰성을 판단할 provenance 신호는 **개발 중인 방향**으로 설명됩니다.

이러한 보호가 모든 공격을 완전히 차단한다는 보장은 아닙니다. 실제 구현에서는 데이터 권한, 행동 승인, 감사와 함께 다층으로 검토해야 합니다.

![Work IQ 실행과 제어 관련 원문 이미지](/mwkorea/assets/images/2026-11-18-WorkIQIgniteUpdates/image3.png)

## 어디에서 사용할 수 있나요?

원문은 Work IQ가 **Foundry와 Copilot Studio에서 GA**이며 MCP·REST·A2A 프로토콜로 제공된다고 설명합니다. 다만 전체 기반의 GA와 위에서 소개한 개별 신기능의 단계는 구분해야 합니다.

**ChatGPT Business·Enterprise**용 Work IQ 플러그인은 ChatGPT 플러그인 디렉터리에 제공된다고 발표했습니다. 연결 후 Outlook 메일·Teams 대화·SharePoint 파일로 고객 회의 준비나 제안서 초안을 작성하되 사용자가 접근 가능한 정보만 조회합니다. **Anthropic용 플러그인은 예정**입니다.

## 개발·도입 체크포인트

한국 조직에서는 처음부터 광범위한 실행 권한을 주기보다 읽기와 쓰기를 나누고, 삭제·외부 전송·주요 레코드 변경 같은 작업에 어떤 승인 정책이 필요한지 정하는 것이 좋습니다. 메모리와 여러 제품 간 맥락 공유도 내부 데이터 관리 기준과 함께 검토해야 합니다.

SharePoint 구현은 [Introducing SharePoint tools in Work IQ](https://techcommunity.microsoft.com/blog/SPBlog/introducing-sharepoint-tools-in-work-iq/4569917)를, 행사 설명은 Ignite의 BRK304·BRK210·BRK299 및 거버넌스 세션 BRK296을 참고할 수 있습니다. 원문 본문에는 실제 영상 임베드가 없습니다.

> **출처**: [What's new in Work IQ at Ignite 2026: agents that get work done](https://techcommunity.microsoft.com/t5/microsoft-365-blog/what-s-new-in-work-iq-at-ignite-2026-agents-that-get-work-done/ba-p/4572219), TechCommunity Microsoft 365 Blog. 자세한 내용은 원문 참조.
