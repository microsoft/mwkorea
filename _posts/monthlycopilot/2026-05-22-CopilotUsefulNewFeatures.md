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

<div class="monthlycopilot-page monthlycopilot-page--tour">
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

<p><a href="https://microsoft.github.io/mwkorea/monthlycopilot/CopilotCowork/" target="_blank" rel="noopener noreferrer">지난 5월호</a>에서 Copilot Cowork를 통해 "질문에 답하는 AI"에서 "업무를 끝까지 해내는 AI"로 진화했다는 소식을 전했다면, 이번 호에서는 그 흐름 위에 새롭게 추가된 기능들을 살펴봅니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--teal"><div class="mc-card-title">Cowork Skills</div><div>반복 업무 지시를 재사용 가능한 스킬로 저장합니다.</div></div>
  <div class="mc-card mc-card--blue"><div class="mc-card-title">Excel Plan + Python</div><div>시트를 편집하기 전에 계획을 보고 승인합니다.</div></div>
  <div class="mc-card mc-card--purple"><div class="mc-card-title">AI in SharePoint</div><div>파일 이해와 메타데이터 정리를 AI가 돕습니다.</div></div>
</div>

<hr/>

<h2 class="mc-section-title">1. Cowork Skills: 내 업무 프로세스를 통째로 저장</h2>

<div class="mc-callout mc-card--amber">
  <div class="mc-card-title">이용 가능 상태</div>
  <div>Frontier 프로그램을 통해 이용 가능 (2026년 5월 기준) · 필요 라이선스: Microsoft 365 Copilot</div>
  <div style="margin-top: 0.55rem;"><a href="https://www.microsoft.com/en-us/microsoft-365/blog/2026/05/05/copilot-cowork-from-conversation-to-action-across-skills-integrations-and-devices/" target="_blank" rel="noopener noreferrer">공식 블로그 보기</a></div>
</div>

<p>Copilot에게 "우리 팀 주간보고 양식으로 이 내용을 정리해줘"라고 할 때마다 양식 구조, 톤, 포함할 항목을 매번 설명해야 합니다. Cowork Skills는 이 반복을 줄여줍니다.</p>

<p>Cowork Skills는 Copilot이 특정 업무를 수행할 때 따라야 할 재사용 가능한 지침 세트입니다. 한 번 만들어두면 매번 같은 프롬프트를 반복하지 않아도 정해진 구조와 톤, 프로세스대로 일관되게 작업합니다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--teal"><div class="mc-card-title">AI 뉴스 브리핑</div><div>최신 AI 뉴스를 웹에서 검색하고 Word 문서와 발표용 PPT를 만든 뒤 메일로 발송합니다.</div></div>
  <div class="mc-card mc-card--blue"><div class="mc-card-title">조직 맞춤 발표 자료</div><div>회사 템플릿, 폰트, 색상, 레이아웃 규칙을 스킬에 정의해 조직 표준에 맞게 자료를 만듭니다.</div></div>
  <div class="mc-card mc-card--purple"><div class="mc-card-title">하루 업무 마무리</div><div>회의, 메일, Teams 대화를 종합해 하루 업무 요약 문서를 생성하고 메일로 보내줍니다.</div></div>
  <div class="mc-card mc-card--amber"><div class="mc-card-title">SKILL.md 구조</div><div>커스텀 스킬은 OneDrive 폴더의 SKILL.md 파일로 저장되며, YAML 헤더와 단계별 지침으로 구성됩니다.</div></div>
</div>

<div class="mc-callout">
  <div class="mc-card-title">템플릿 허브</div>
  <div><a href="https://microsoft.github.io/KoreaCopilotAgent/" target="_blank" rel="noopener noreferrer">M365 Agent Templates</a>에서 AI 뉴스 브리핑, 하루 마무리 등 즉시 활용 가능한 스킬 템플릿과 설치 가이드를 확인할 수 있습니다.</div>
</div>

<hr/>

<h2 class="mc-section-title">2. Excel Plan 모드 + Python: 편집 전에 계획을 먼저 보여줍니다</h2>

<div class="mc-callout mc-card--blue">
  <div class="mc-card-title">롤아웃 상태</div>
  <div>2026년 5월 롤아웃 중 (테넌트 순차 배포) · 제품: Excel Windows, Mac, 웹 · 필요 라이선스: Microsoft 365 Copilot</div>
  <div style="margin-top: 0.55rem;"><a href="https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--april-2026/4510935" target="_blank" rel="noopener noreferrer">공식 발표 보기</a></div>
</div>

<p>기존에는 프롬프트를 입력하면 Copilot이 바로 시트를 편집했고, 결과가 마음에 들지 않으면 Ctrl+Z로 되돌리는 수밖에 없었습니다. Plan 모드에서는 Copilot이 시트를 수정하기 전에 실행 계획을 먼저 보여줍니다.</p>

<img src="/mwkorea/assets/images/20260522-copilot-new-features/image1.png" alt="Excel Plan 모드 화면" />

<div class="mc-table-wrap">
  <table>
    <tr><th>구분</th><th>Before</th><th>After: Plan 모드</th></tr>
    <tr><td>흐름</td><td>프롬프트 입력 → 바로 시트 편집</td><td>프롬프트 입력 → 계획 확인 → 승인 → 편집</td></tr>
    <tr><td>투명성</td><td>결과만 보임</td><td>어떤 데이터를 쓰고 어떤 기능을 쓸지 단계별로 확인</td></tr>
    <tr><td>되돌리기</td><td>Ctrl+Z 연타</td><td>승인 전에 계획을 수정하면 됨</td></tr>
    <tr><td>적합한 상황</td><td>단순 작업</td><td>다단계 작업, 민감한 데이터</td></tr>
  </table>
</div>

<div class="mc-callout mc-card--teal">
  <div class="mc-card-title">Python 지원</div>
  <div>프롬프트에 "Python 사용해서"라고 지정하거나 Copilot이 필요하다고 판단하면 Python을 호출해 회귀 분석, 이상치 탐지, 고급 시각화까지 수행합니다. 별도 설치나 코딩 지식은 필요 없습니다.</div>
  <div style="margin-top: 0.55rem; color: #6b7280;">예: 이번 달 매출 데이터에서 이상치를 찾고, 지역별 추세선을 그려줘. Python 사용해서.</div>
</div>

<hr/>

<h2 class="mc-section-title">3. AI in SharePoint: 메타데이터 태깅, 이제 AI가 합니다</h2>

<div class="mc-callout mc-card--purple">
  <div class="mc-card-title">Public Preview</div>
  <div>관리자 옵트인이 필요하며, Microsoft 365 Copilot 라이선스에서 추가 비용 없이 사용할 수 있습니다.</div>
  <div style="margin-top: 0.55rem;"><a href="https://support.microsoft.com/en-us/topic/ai-in-sharepoint-an-overview-c0b1efc3-81d0-4981-8be9-7ba3a75fae15" target="_blank" rel="noopener noreferrer">개요</a> · <a href="https://learn.microsoft.com/en-us/sharepoint/ai-in-sharepoint-get-started" target="_blank" rel="noopener noreferrer">관리자 설정 가이드</a></div>
</div>

<p>2025년 9월 Knowledge Agent라는 이름으로 처음 등장했던 기능이 AI in SharePoint로 이름을 바꾸고 본격적으로 확장되었습니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--teal"><div class="mc-card-title">파일 이해</div><div>문서에 대해 자연어로 질문하고, 요약하고, 파일 간 비교까지 가능합니다. FAQ도 자동 생성합니다.</div></div>
  <div class="mc-card mc-card--blue"><div class="mc-card-title">라이브러리 자동 정리</div><div>Autofill columns로 계약 유형, 만료일, 고객명 같은 메타데이터를 자동으로 추출합니다.</div></div>
  <div class="mc-card mc-card--purple"><div class="mc-card-title">자연어 사이트 생성</div><div>신입사원 온보딩 포털처럼 원하는 사이트 구조를 자연어로 제안받고 승인 후 생성합니다.</div></div>
</div>

<div class="mc-callout">
  <div class="mc-card-title">관리자 설정 안내</div>
  <ul>
    <li>PowerShell로 테넌트 또는 사이트 단위 활성화 필요 (기본값: 비활성)</li>
    <li>Anthropic 모델 활성화 선택 가능 (권장)</li>
    <li>SharePoint 메타데이터가 잘 정리되어 있으면 Copilot 전체 검색 및 응답 품질도 향상</li>
  </ul>
</div>

<hr/>

<h2 class="mc-section-title">보너스: Outlook에도 등장한 에이전트</h2>

<div class="mc-callout mc-card--amber">
  <div class="mc-card-title">Frontier 프로그램</div>
  <div>2026년 4~5월 롤아웃 · <a href="https://mc.merill.net/message/MC1296874" target="_blank" rel="noopener noreferrer">Microsoft 365 Message Center MC1296874</a></div>
</div>

<img src="/mwkorea/assets/images/20260522-copilot-new-features/image2.png" alt="Outlook 작업 허용 기능" />

<p>Outlook 내 Copilot Chat에서 작업 허용(Allow Actions)을 켜면, 자연어로 정한 규칙에 따라 Copilot이 일정을 자동으로 관리합니다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--teal"><div class="mc-card-title">자동 수락</div><div>매니저가 보낸 회의 초대는 일정이 비면 자동 수락하도록 설정할 수 있습니다.</div></div>
  <div class="mc-card mc-card--blue"><div class="mc-card-title">일정 정리</div><div>취소된 미팅은 바로 삭제하도록 규칙을 만들 수 있고 활동 기록에 내역이 남습니다.</div></div>
</div>

<p>현재 Frontier 프로그램 사용자만 이용 가능하며 일반 출시 일정은 아직 발표되지 않았습니다. 더 자세한 내용은 <a href="https://microsoft.github.io/mwkorea/copilot/CopilotOutlookAgentic/" target="_blank" rel="noopener noreferrer">Outlook의 Copilot, 에이전트로 진화하다</a>에서 확인할 수 있습니다.</p>

<hr/>

<h2 class="mc-section-title">한눈에 보기 (2026년 5월 기준)</h2>

<div class="mc-table-wrap">
  <table>
    <tr><th>기능</th><th>상태</th><th>관리자 조치</th></tr>
    <tr><td>Cowork Skills</td><td>Frontier</td><td>Frontier 신청</td></tr>
    <tr><td>Excel Plan 모드 + Python</td><td>5월 롤아웃 중</td><td>업데이트 채널 확인</td></tr>
    <tr><td>AI in SharePoint</td><td>Public Preview</td><td>PowerShell 옵트인</td></tr>
    <tr><td>Outlook 작업 허용</td><td>Frontier</td><td>Frontier 신청</td></tr>
  </table>
</div>

<div class="mc-callout mc-callout--dark">
  <div style="font-weight: 800; margin-bottom: 0.5rem; font-size: 1.05rem;">참고</div>
  <div>본 기사의 모든 내용은 Microsoft 공식 블로그, Microsoft Learn, Microsoft 365 Message Center를 출처로 작성되었습니다. 출시 일정은 변경될 수 있으며, 테넌트 환경에 따라 기능 제공 시점이 다를 수 있습니다.</div>
</div>

</div>
