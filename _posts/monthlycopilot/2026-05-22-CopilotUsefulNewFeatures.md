---
title: 'Copilot의 유용한 새로운 기능'
date: 2026-05-22T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - Cowork Skills
  - Excel
  - SharePoint
  - Outlook
  - 월간코파일럿
excerpt: 'Cowork Skills, Excel Plan 모드와 Python, AI in SharePoint, Outlook 작업 허용까지 2026년 5월 기준 새롭게 공개되거나 확장된 Copilot 기능을 정리했습니다.'
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 이수민
---

<div class="monthlycopilot-page monthlycopilot-page--tour" markdown="1">
<div class="mc-issue-strip">Monthly Copilot · June 2026 · 월간 코파일럿 소식지 6월호 · Copilot News · New Features</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">월간 코파일럿 소식지 ｜ 2026년 6월호</div>
  <div class="mc-cover-title">Copilot의 유용한<br/>새로운 기능</div>
  <div class="mc-cover-subtitle">Cowork Skills, Excel Plan 모드, AI in SharePoint까지</div>
</div>

<div style="margin: 0 0 1.3rem; padding: 1rem 1.1rem; border-radius: 16px; background: linear-gradient(135deg, #ecfeff 0%, #f8fafc 100%); border: 1px solid #99f6e4; color: #1f2937;">
  <div style="font-weight: 800; color: #0f766e; margin-bottom: 0.35rem;">Article Summary</div>
  <div style="line-height: 1.85;">지난 호에서 Copilot Cowork를 소개했다면, 이번 호에서는 그 흐름 위에 추가된 세 가지 기능을 정리합니다. 반복 업무 지시를 저장하는 Cowork Skills, 편집 전 계획을 확인하는 Excel Plan 모드, SharePoint 콘텐츠 자동 정리 기능까지 한눈에 살펴봅니다.</div>
</div>

**Article Summary**

[지난 5월호](https://microsoft.github.io/mwkorea/monthlycopilot/CopilotCowork/)에서 Copilot에 Copilot Cowork를 통해 "질문에 답하는 AI"에서 "업무를 끝까지 해내는 AI"로 진화했다는 소식을 전했다면, 이번 호에서는 그 흐름 위에 새롭게 추가된 세 가지 새로운 기능을 소개합니다. 반복 업무 지시를 스킬로 저장하는 **Cowork Skills**, 시트 편집 전에 계획을 먼저 확인하는 **Excel Plan 모드 + Python**, 그리고 SharePoint 콘텐츠를 AI가 자동으로 정리하는 **AI in SharePoint**입니다.

------------------------------------------------------------------------

**1. Cowork Skills: 내 업무 프로세스를 통째로 저장**

🧪 Frontier 프로그램을 통해 이용 가능 (2026년 5월 기준)

필요 라이선스: Microsoft 365 Copilot

[Copilot Cowork: From conversation to action across skills, integrations, and devices \| Microsoft 365 Blog](https://www.microsoft.com/en-us/microsoft-365/blog/2026/05/05/copilot-cowork-from-conversation-to-action-across-skills-integrations-and-devices/)

Copilot에게 "우리 팀 주간보고 양식으로 이 내용을 정리해줘"라고 할 때마다, 양식 구조·톤·포함할 항목을 매번 설명해야 합니다. 메모리가 선호도나 대화 맥락을 기억해주긴 하지만, "이 업무는 이 순서로, 이 도구를 써서, 이 양식에 맞춰 처리해"라는 구체적인 작업 프로세스까지 저장해주지는 않습니다.

Cowork Skills는 바로 이 부분을 해결합니다. Copilot이 특정 업무를 수행할 때 따라야 할 재사용 가능한 지침 세트로, 한 번 만들어두면 매번 같은 프롬프트를 반복하지 않아도 정해진 구조와 톤, 프로세스대로 일관되게 작업합니다.

문서 작성, 회의 조율, 리서치 등 공통 업무에 대한 빌트인 스킬이 기본 탑재되어 있고, 팀 고유의 프로세스를 정의하는 커스텀 스킬도 직접 만들 수 있습니다.

**프롬프트 대신 스킬로 일합니다**

단순히 프롬프트 하나를 저장하는 수준이 아닙니다. 스킬 하나가 여러 단계의 작업을 순서대로 실행할 수 있다는 점이 핵심입니다. 예를 들어 이런 워크플로가 가능합니다.

**AI 뉴스 브리핑**: 최신 AI 뉴스를 웹에서 검색하고, 핵심 내용을 정리한 Word 문서와 발표용 PPT를 자동으로 생성한 뒤, 완성된 파일을 본인 메일로 발송합니다. 아침에 Copilot에게 "/ai-news-briefing" 한마디면 출근길에 브리핑 자료가 메일함에 도착해 있습니다.

**조직 맞춤 발표 자료**: 회사 PPT 템플릿의 폰트·색상·레이아웃 규칙, 슬라이드 구성 방식을 스킬에 정의해두면, 매번 "우리 회사 양식으로 만들어줘"라고 설명하지 않아도 Copilot이 처음부터 조직 표준에 맞춰 자료를 만듭니다.

**하루 업무 마무리**: 오늘 참석한 회의 내용, 받은 메일, Teams 대화를 종합해서 하루 업무 요약 문서를 생성하고 메일로 보내줍니다. 퇴근 전에 "/daily-wrap-up" 한마디면 오늘 뭘 했는지 정리할 필요가 없습니다.

**Skills 의 구조**

커스텀 스킬은 OneDrive의 폴더에 **SKILL.md** 파일로 저장됩니다. YAML 헤더에 이름과 설명을 적고, 본문에 단계별 지침을 마크다운으로 작성하는 구조입니다. 최대 50개까지 만들 수 있고, 복잡한 스킬은 하위 폴더에 참조 문서나 템플릿을 함께 넣어 활용할 수도 있습니다.

[M365 Agent Templates — 즉시 활용 가능한 템플릿 허브](https://microsoft.github.io/KoreaCopilotAgent/)에서 AI 뉴스 브리핑, 하루 마무리 등 즉시 활용 가능한 스킬 템플릿과 설치 가이드를 확인할 수 있습니다.

*현재 Cowork Skills는 **Frontier 프로그램**에서만 이용 가능합니다 [Frontier 프로그램 안내](https://adoption.microsoft.com/en-us/copilot-frontier/)*

------------------------------------------------------------------------

**2. Excel Plan 모드 + Python: 편집 전에 계획을 먼저 보여줍니다**

🚀 2026년 5월 롤아웃 중 (테넌트 순차 배포)

필요 라이선스: Microsoft 365 Copilot \| 제품: Excel (Windows · Mac · 웹)

[공식 발표 — What's New, April 2026 (Tech Community)](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935)

기존에는 프롬프트를 입력하면 Copilot이 바로 시트를 편집했고, 결과가 마음에 들지 않으면 Ctrl+Z로 되돌리는 수밖에 없었습니다. Plan 모드에서는 Copilot이 시트를 수정하기 전에 실행 계획을 먼저 보여줍니다. 어떤 데이터를 쓰고, 어떤 기능을 적용할지 단계별로 확인한 뒤 승인하면 그때 실제 편집이 진행됩니다.

<img src="/mwkorea/assets/images/20260522-copilot-new-features/image1.png" style="width:6.10417in;height:5.875in" />

**Before vs After**

|  | Before (기존) | After (Plan 모드) |
|----|----|----|
| 흐름 | 프롬프트 입력 → **바로 시트 편집** | 프롬프트 입력 → **계획 확인** → 승인 → 편집 |
| 투명성 | 결과만 보임 | 어떤 데이터를 쓰고, 어떤 기능을 쓸지 단계별로 확인 |
| 되돌리기 | Ctrl+Z 연타 | 승인 전에 계획을 수정하면 됨 |
| 적합한 상황 | 단순 작업 | 다단계 작업, 민감한 데이터 |

사용법은 프롬프트 입력창 위에서 "계획 (Plan)" 을 선택하면 됩니다.

**Python 지원**

같은 시기에 **Python 지원**도 추가되었습니다. 프롬프트에 "Python 사용해서"라고 지정하거나, Copilot이 필요하다고 판단하면 자동으로 Python을 호출해 회귀 분석, 이상치 탐지, 고급 시각화까지 수행합니다. 별도 설치나 코딩 지식은 필요 없습니다.

"이번 달 매출 데이터에서 이상치를 찾고, 지역별 추세선을 그려줘. Python 사용해서."

→ Plan 모드에서 계획 확인 → 승인 → Python 자동 실행 → 분석 결과 + 시각화 생성

특히 민감한 파일을 다루는 경우, 편집 전에 계획을 확인할 수 있다는 점이 유용합니다.

*위 기능들은 5월부터 순차 롤아웃 중입니다.*

------------------------------------------------------------------------

**3. AI in SharePoint: 메타데이터 태깅, 이제 AI가 합니다.**

🧪 Public Preview (관리자 옵트인 필요)

필요 라이선스: Microsoft 365 Copilot (추가 비용 없음) \| 제품: SharePoint Online

[AI in SharePoint 개요 (Microsoft Support)](https://support.microsoft.com/en-us/topic/ai-in-sharepoint-an-overview-c0b1efc3-81d0-4981-8be9-7ba3a75fae15) · [관리자 설정 가이드 (Microsoft Learn)](https://learn.microsoft.com/en-us/sharepoint/ai-in-sharepoint-get-started)

2025년 9월 "Knowledge Agent"라는 이름으로 처음 등장했던 기능이, "AI in SharePoint"으로 이름을 바꾸고 본격적으로 확장되었습니다.

주요 기능은 세 가지입니다.

1.  **파일 이해** 문서에 대해 자연어로 질문하고, 요약하고, 파일 간 비교까지 가능합니다. FAQ도 자동 생성합니다.

2.  **라이브러리 자동 정리** 가장 실용적인 기능은 "**Autofill columns**"입니다. 파일 내용을 AI가 분석해서 계약 유형, 만료일, 고객명 같은 메타데이터를 자동으로 추출합니다. 지금까지 수작업으로 하던 태깅이 자동화됩니다. "500만원 이상 인보이스가 추가되면 알림"처럼 자연어로 워크플로 규칙도 만들 수 있습니다.

3.  **자연어 사이트 생성** "신입사원 온보딩 포털을 만들어줘"라고 말하면, AI가 페이지·목록·라이브러리 구조를 제안하고 승인하면 자동으로 생성합니다.

**관리자 설정 안내**

AI in SharePoint는 현재 **Public Preview**이며, 사용하려면 관리자 설정이 필요합니다.

- **PowerShell로 옵트인:** 테넌트 또는 사이트 단위 활성화 필요 (기본값: 비활성)

- **Anthropic 모델 활성화** (선택, 권장): 관리 센터에서 AI 하위 프로세서로 활성화하면 전체 Preview 경험 이용 가능

- **Copilot 라이선스** 필요 (추가 비용 없음)

참고로, SharePoint의 메타데이터가 잘 정리되어 있으면 Copilot 전체의 검색 및 응답 품질도 향상됩니다.

------------------------------------------------------------------------

**\[보너스\] Outlook에도 등장한 에이전트**

🧪 Frontier 프로그램 (2026년 4~5월 롤아웃)

[Microsoft 365 Message Center MC1296874](https://mc.merill.net/message/MC1296874) (2026.04.30)

<img src="/mwkorea/assets/images/20260522-copilot-new-features/image2.png" style="width:6.26806in;height:3.67014in" />

Outlook 내 Copilot Chat에서 "작업 허용(Allow Actions)"을 켜면, 자연어로 정한 규칙에 따라 Copilot이 일정을 자동으로 관리합니다.

"매니저가 보낸 회의 초대는 일정이 비면 자동 수락해줘", "취소된 미팅은 바로 삭제해줘" 와 같은 규칙을 설정하면 Copilot이 처리하고, 활동 기록에 내역을 남깁니다.

현재 Frontier 프로그램 사용자만 이용 가능하며, 일반 출시 일정은 아직 발표되지 않았습니다.

더 자세한 내용은 아래 글에서 확인할 수 있습니다.

👉 [Outlook의 Copilot, 에이전트로 진화하다: 받은편지함과 캘린더를 알아서 챙겨주는 새로운 경험 - ModernWork Korea](https://microsoft.github.io/mwkorea/copilot/CopilotOutlookAgentic/)

**한눈에 보기 (2026년 5월 기준)**

| 기능                     | 상태           | 관리자 조치        |
|--------------------------|----------------|--------------------|
| Cowork Skills            | Frontier       | Frontier 신청      |
| Excel Plan 모드 + Python | 5월 롤아웃 중  | 업데이트 채널 확인 |
| AI in SharePoint         | Public Preview | PowerShell 옵트인  |
| Outlook "작업 허용"      | Frontier       | Frontier 신청      |

*본 기사의 모든 내용은 Microsoft 공식 블로그, Microsoft Learn, Microsoft 365 Message Center를 출처로 작성되었습니다. 출시 일정은 변경될 수 있으며, 테넌트 환경에 따라 기능 제공 시점이 다를 수 있습니다.*

</div>

