---
title: "Copilot Pages와 Notebooks, OneDrive로: AI 업무 산출물도 기존 거버넌스로 관리하세요"
date: 2026-10-09T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotPages
  - CopilotNotebooks
  - OneDrive
  - Governance
  - MicrosoftPurview
excerpt: "새로 만드는 Copilot Pages와 Copilot Notebooks의 저장 위치가 OneDrive for Business로 바뀝니다. 기존 콘텐츠는 일괄 이전되지 않으며, 새 산출물에는 OneDrive의 DLP·보존·퇴사자 관리 체계를 적용할 수 있습니다. 10월 8일 수정된 출시 일정과 관리자가 점검할 내용을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Pages와 Notebooks, OneDrive로: AI 업무 산출물도 기존 거버넌스로 관리하세요

Copilot이 만든 답변을 팀의 업무 자료로 발전시키면, 다음 질문은 자연스럽게 나옵니다. “이 자료는 어디에 저장되고, 보존 정책과 정보 유출 방지 정책은 어떻게 적용될까요?” Microsoft는 메시지 센터 공지 **MC1449182**에서 새 Copilot Pages와 새 Copilot Notebooks의 저장 위치를 OneDrive for Business로 변경한다고 안내했습니다.

핵심은 AI 산출물을 별개의 관리 대상으로 취급하기보다, 조직이 이미 운영하는 OneDrive의 거버넌스·컴플라이언스·데이터 보호·수명주기 관리 체계에 연결하는 것입니다. 새 콘텐츠는 Word, Excel, PowerPoint 파일과 함께 OneDrive에서 보이게 됩니다.

다만 **기존 자료를 모두 OneDrive로 옮기는 마이그레이션은 아닙니다.** 특히 기존 Notebook에서 앞으로 만드는 페이지는 계속 SharePoint Embedded에 저장된다는 예외를 구분해야 합니다. 이 글은 2026년 10월 8일 수정된 공지를 기준으로 설명합니다.

---

## 무엇이 바뀌나요?

변경 대상은 Copilot Chat, Microsoft 365 Copilot 앱, Copilot Notebooks에서 생성하는 Copilot Pages입니다. 배포 이후 새로 생성되는 Pages는 사용자의 OneDrive for Business에 저장됩니다. 새 Copilot Notebooks와 그 안에서 만들어지는 산출물 역시 다른 OneDrive 파일과 나란히 표시됩니다.

사용자에게는 저장 위치의 변화이고, 관리자에게는 AI 기반 작업 결과를 기존 파일 관리 체계로 다룰 수 있게 되는 변화입니다. Microsoft 365 Copilot, Copilot Chat, Copilot Notebooks, OneDrive for Business, Microsoft Purview를 함께 운영하는 조직에서 특히 의미가 있습니다.

## OneDrive 기반으로 적용할 수 있는 관리 기능

공지에는 기존 거버넌스 기능에 더해 새 Copilot Pages에 적용되는 기능이 다음과 같이 정리되어 있습니다.

| 관리 영역 | 공지에 명시된 기능 |
|---|---|
| 컴플라이언스·법무 | 표준 파일 경로 기반 eDiscovery, 레코드 잠금이 있는 보존 레이블, Information Barriers, Compliance Boundaries |
| 데이터 보호 | DLP 정책과 완화 워크플로, OneDrive 콘텐츠를 지원하는 타사 거버넌스 솔루션 |
| 수명주기 | 보존·수명주기 정책, 기존 OneDrive 퇴사자 처리 워크플로 |
| 모니터링·조사 | OneDrive 저장 공간 보고, OneDrive에 저장된 콘텐츠에 대한 관리자 조사 |

예를 들어 AI로 정리한 업무 페이지도 보존 대상인지, 민감한 내용을 담은 페이지에 DLP 정책이 적용되는지, 작성자가 퇴사했을 때 자료를 어떻게 처리하는지 기존 OneDrive 정책을 중심으로 검토할 수 있습니다. 이는 도입 담당자 관점의 활용 예시이며, 개별 정책의 적용 결과는 조직의 설정과 실제 콘텐츠로 확인해야 합니다.

## 기존 Pages·Notebooks와 Loop는 어떻게 되나요?

저장 위치 변경의 경계를 명확히 알아두는 것이 중요합니다.

| 콘텐츠 | 변경 후 저장 방식 |
|---|---|
| 새 Copilot Pages | 사용자의 OneDrive for Business |
| 변경 후 생성한 새 Copilot Notebooks의 페이지 | OneDrive |
| 기존 Copilot Pages | 현재 위치 유지, 이번 변경으로 이전하지 않음 |
| 기존 Copilot Notebooks에서 새로 만드는 페이지 | 계속 SharePoint Embedded에 저장 |
| Loop workspaces | 영향 없음, 기존 저장 위치 유지 |

따라서 “배포 이후 만든 페이지는 모두 OneDrive에 있다”는 설명은 정확하지 않습니다. **기존 Notebook 안에서 만드는 새 페이지는 예외**입니다. 내부 사용자 안내와 조사 절차에도 이 차이를 반영하는 편이 좋습니다.

## 출시 일정: 10월 8일 공지에서 변경됐습니다

| 환경 | GA 배포 시작 예정 | 완료 예정 |
|---|---|---|
| Worldwide | 2026년 10월 중순 | 2026년 11월 말 |
| GCC, GCC High, DoD | 2026년 11월 중순 | 2026년 12월 초 |

Worldwide 일정은 이전의 8월 중순~9월 말에서 변경됐고, 미국 정부 클라우드 일정도 이전의 9월 중순~10월 초에서 변경됐습니다. 이는 **GA의 순차 배포 예정 일정**이지, 모든 테넌트에서 이미 제공된다는 뜻은 아닙니다.

## 관리자가 확인할 네 가지

Microsoft는 배포 자체를 위해 필요한 조치는 없다고 안내합니다. 다만 다음 점검을 권고합니다.

1. OneDrive for Business에 적용 중인 DLP·보존·컴플라이언스 정책을 검토합니다.
2. 타사 거버넌스와 eDiscovery 솔루션이 OneDrive 콘텐츠를 적절히 모니터링하도록 설정되어 있는지 확인합니다.
3. AI 생성 콘텐츠에 관한 내부 문서와 거버넌스 지침을 갱신합니다.
4. 새 Copilot Pages가 사용자 OneDrive에 저장된다는 점을 안내합니다.

**Create and view Copilot Pages and Copilot Notebooks** 관리 설정을 Disabled로 둔 조직은 변경 후에도 해당 설정이 존중됩니다. Microsoft는 이 관리 제어를 향후 폐지할 계획이라고 밝혔지만, 폐지 전에 별도 공지와 전환 지침을 제공한다고 설명했습니다. 이번 저장 위치 변경과 관리 설정 폐지를 같은 시점의 확정 조치로 해석해서는 안 됩니다.

## 마무리: 저장 위치보다 정책의 적용 경계가 중요합니다

이번 변화는 Copilot의 작업 결과를 기존 Microsoft 365 파일 관리 체계로 가져오는 업데이트입니다. 도입 조직에서는 신규 Pages에 대한 OneDrive 정책을 검토하면서, 기존 Pages와 기존 Notebooks는 다른 저장 경로를 유지한다는 점도 함께 관리해야 합니다.

사용자에게는 “새 자료를 어디서 찾는가”, 관리자에게는 “어떤 자료에 어떤 정책이 적용되는가”를 구분해 안내하면 혼선을 줄일 수 있습니다.

---

> 출처: Microsoft 365 Message Center **MC1449182**, [Microsoft 365 Copilot: Copilot Pages and Notebooks Creation in OneDrive](https://mc.merill.net/message/MC1449182) — 2026년 10월 8일 수정 공지 기준.
>
> 관련 일정 확인: [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap). 원문에서 개별 Roadmap ID는 확인되지 않아 전체 Roadmap 링크를 제공합니다.
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
