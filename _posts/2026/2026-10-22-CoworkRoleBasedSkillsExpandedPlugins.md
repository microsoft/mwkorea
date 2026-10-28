---
title: "Cowork에 직무별 스킬 추가: 영업·서비스·교육·법무의 반복 업무를 연결합니다"
date: 2026-10-22T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotCowork
  - Plugins
  - RoleBasedSkills
  - PowerPlatform
  - EventDrivenTasks
excerpt: "Copilot Cowork의 리빙 블로그에 영업·서비스·교육·법무용 스킬과 확장 플러그인 안내가 추가됐습니다. 연결된 상세 발표를 바탕으로 직무별 업무, Power Platform·MCP 연결, 이벤트 기반 실행과 사용자 승인 경계를 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Cowork에 직무별 스킬 추가: 영업·서비스·교육·법무의 반복 업무를 연결합니다

고객 미팅을 준비하고, 지원 문의의 우선순위를 정하고, 계약서를 검토하는 일은 한 번의 프롬프트보다 긴 흐름을 가집니다. 여러 앱의 정보를 모으고 같은 지침을 반복해야 한다면, 업무 단위를 재사용 가능한 스킬로 묶는 접근이 필요합니다.

Copilot Cowork의 **(Co)work in Progress**에 직무별 스킬과 플러그인 확장 섹션이 추가됐습니다. 이 글은 새 섹션과 거기서 연결한 [상세 발표](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-cowork-expanded-plugins-and-role-based-skills/4566221)를 함께 읽고 한국 독자 관점으로 정리한 것입니다.

**이 글은 하나의 글에 Cowork 업데이트가 누적되는 리빙 블로그의 최신 섹션입니다.** 파일 날짜는 수집기가 섹션에 부여한 원문 수정 시각을 한국 시간으로 환산한 2026년 10월 22일입니다. 섹션의 독립적인 최초 공개 시각을 따로 검증한 날짜는 아닙니다.

![Cowork 리빙 블로그의 해당 업데이트 이미지](/mwkorea/assets/images/2026-10-22-CoworkRoleBasedSkillsExpandedPlugins/image1.png)

---

## 연결 선택지는 넓어지고 관리 권한은 유지됩니다

상세 발표는 기존 plugin registry를 플러그인을 찾고 관리하는 통합 지점으로 설명합니다. 이미 Cowork에서 플러그인을 쓰고 있다면 찾아서 활성화하는 기본 방식은 유지되며, 선택할 수 있는 범위가 확대됩니다.

| 유형 | 확장 내용과 제공 상태 |
|---|---|
| Power Platform connectors | 기존 업무 앱·서비스 연결 활용. **향후 몇 주 동안 순차 배포** |
| Federated Copilot connectors | MCP로 외부 시스템의 실시간 데이터 활용. 해당 시스템의 **사용자 본인 권한** 적용 |
| Role-based plugins | 영업·서비스·교육·법무용 스킬. 상세 발표 시점 **Roles & Industry에 제공** |

플러그인과 커넥터 중 조직에서 사용할 수 있는 대상은 관리자가 결정합니다. 목록에 보이지 않는다면 관리자 허용이나 접근 요청이 먼저 필요할 수 있습니다.

## 영업: 미팅 이후의 후속 작업까지

**Sales for Cowork**는 계정 조사, 미팅 준비, 구매 의사결정 그룹 파악, 후속 연락과 기회 우선순위 판단을 지원합니다. 이메일·회의·파일을 grounding에 사용하며 **CRM 데이터는 선택 사항**입니다.

대표 스킬은 미팅 후속 작업, 파이프라인 우선순위, 딜 변경 사항 따라잡기, 경쟁 전략, 비즈니스 사례 작성과 참여 위험 인사이트입니다. 단순 기록 갱신과 실제 고객 움직임을 구분하고 근거·불확실성을 보여주는 방향입니다.

예를 들어 `/post-meeting-follow-up`으로 미팅 결정·담당자·기한을 정리하고 고객 후속 메일 **초안 검토**를 요청할 수 있습니다. `/pipeline-prioritizer`, `/deal-catchup`도 원문이 제시한 시작 명령입니다. Dynamics 365 Sales 사용자는 별도의 Dynamics 365 Sales 플러그인도 추가할 수 있습니다.

## 서비스: 분류부터 재사용 가능한 지식까지

**Service for Cowork**는 케이스 분류, 다음 응대 전 브리핑, 출처 기반 답변 조사, 고객 답장 초안, 해결 지식 추출을 지원합니다. 이 역시 이메일·회의·파일을 기반으로 하며 CRM 연결은 필수가 아닙니다.

`/case-triage`로 기한·고객 영향·약속·미응답 연락을 고려한 작업 목록을 만들고, `/draft-customer-reply`로 검증된 사실과 정책을 구분한 답장을 준비하는 식입니다. `/knowledge-harvest`는 검증된 해결책을 고객 식별 정보를 제외한 안내 초안으로 만드는 스킬로 소개됩니다.

원문은 Dynamics 365 Sales·Customer Service·Customer Insights에 걸친 **30개의 CRM 스킬**이 이전 주에 소개됐다고도 언급합니다. 이는 이번 네 직무 플러그인의 전체 스킬 개수를 뜻하지 않습니다.

## 교육: 기관 운영과 접근성 업무를 지원합니다

**Education for Cowork**의 주요 업무는 기관 평가·인증 근거 패키지 작성, AI 도구 거버넌스 검토, 단계적 AI 도입 계획, 학습 토론 인사이트, 접근 가능한 교육 자료와 수업 연속성 준비입니다.

예를 들어 `/evidence-package-for-education`은 요구사항 대비 근거의 공백을, `/accessible-learning-materials`는 구조·읽기 순서·링크·이미지 설명·자막·문서 탐색 문제를 점검하는 출발점입니다. `/instructional-continuity`는 다음 학기의 계획과 자료를 묶는 작업에 활용할 수 있습니다.

토론 인사이트는 비식별화된 학습 토론과 피드백의 **집단 수준 패턴**을 찾는 것으로 소개됩니다. 학생 개인을 자동 평가하거나 개인정보 처리를 면제하는 기능으로 해석하면 안 됩니다.

## 법무: Word의 검토에서 여러 문서의 업무 흐름으로

**Legal for Cowork**는 Word에서도 제공되는 스킬을 바탕으로 **20개 법무 스킬**을 제공합니다. Word에서 검토·redline을 수행하고, Cowork에서 계약·메일·회의·파일을 가로지르는 후속 업무로 확장하는 방식입니다.

계약서의 playbook 부합 여부 검토, redline 영향 요약, 의무와 기한 추출, 핵심 조항 비교, 서명 준비 상태 확인과 사건 연표 구성이 예로 제시됩니다.

`/compare-key-terms`로 여러 계약의 조항을 출처와 연결한 Excel 추적표로 정리하거나, `/create-playbook`으로 NDA 선례에서 표준 입장·허용 대안·거부 입장을 정리할 수 있습니다. 원문 예시는 중요한 쟁점과 입장을 **사람이 확인·승인한 뒤** 후속 문서를 작성하는 흐름을 강조합니다. 전문 법률 판단을 대체한다는 의미는 아닙니다.

## 찾는 위치와 작업 카탈로그

직무 플러그인은 **Customize > Roles & Industry library**에서 Sales, Service, Education, Legal for Cowork를 찾는 방식입니다.

업데이트된 task catalog는 Customer Service·Executives·Finance·Marketing·Sales용 시작 아이디어를 제공합니다. Cowork 프롬프트 입력창 아래 **“Show more”**에서 접근하며, 상세 발표는 **2026년 10월 말까지 순차 배포**한다고 안내합니다. 즉, 직무 플러그인의 제공 상태와 카탈로그 전체 배포 완료 시점은 구분해야 합니다.

## 업무 시스템 이벤트로 시작하되 실행 권한은 사용자가 통제합니다

기존 이메일·Teams 메시지 트리거에 더해, 플러그인과 Power Platform 커넥터를 통해 새 케이스나 영업 단계 변경 같은 외부 시스템 이벤트로 작업을 시작하는 흐름을 소개합니다.

사용자가 감시할 변화와 수행할 작업을 자연어로 설명하면, Cowork는 이벤트·할 일·필요 권한을 보여주는 자동화 카드를 제안합니다. 사용자가 검토하고 승인한 뒤 실행되며 **Automations**에서 일시 중지·수정·실행 이력을 확인합니다. 새 자동화 경로는 **Automations > Add > Create with Cowork**입니다.

중요한 경계는 **자동으로 작업을 시작하는 것과 외부 시스템을 수정하는 것이 다르다**는 점입니다. 원문은 작업이 사용자 권한으로 실행되고, 메시지 전송이나 다른 시스템의 레코드 변경은 준비한 뒤 사용자 승인을 기다린다고 설명합니다. 지원 트리거는 파트너가 정의하므로 각 플러그인·커넥터 문서를 확인해야 합니다.

## 마무리

Cowork의 직무별 스킬은 빈 입력창에서 매번 업무 절차를 설명하는 부담을 줄이는 방향입니다. 한국 조직에서는 한 직무의 반복 업무부터 적용하고, 커넥터 허용 범위·데이터 권한·최종 승인 지점을 함께 점검하는 접근이 좋습니다.

> **출처 섹션**: [Introducing role-based skills for Sales, Service, Education, and Legal roles along with an expanded library of plugins](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/cowork-in-progress/4511672#community-4511672-toc-hId-2052082034). 자세한 내용은 원문 참조.
>
> **연결된 상세 발표**: [What’s New in Cowork: Expanded plugins and role-based skills](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-cowork-expanded-plugins-and-role-based-skills/4566221).
>
> 이 글은 하나의 글에 Cowork 업데이트가 누적되는 리빙 블로그의 최신 섹션입니다.
