---
title: '10분이 2분으로, 연 6,300시간을 되찾았다'
date: 2026-05-22T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - Copilot Studio
  - AI Agent
  - 효성
  - 에이전톤
  - 월간코파일럿
excerpt: '효성 AI 팀이 AI Tour Seoul 2026에서 소개한 SmartChem 사례를 통해, 화학물질 분류 업무를 Teams와 Copilot Studio 기반 에이전트로 자동화해 연 6,300시간과 4억 원의 효과를 만든 과정을 정리했습니다.'
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 김현지
---

<div class="monthlycopilot-page monthlycopilot-page--agent">
<div class="mc-issue-strip">Monthly Copilot · June 2026 · 월간 코파일럿 소식지 6월호 · Agenthon Highlight · 효성 AI</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">월간 코파일럿 소식지 ｜ 2026년 6월호</div>
  <div class="mc-cover-title">10분이 2분으로,<br/>연 6,300시간을 되찾았다</div>
  <div class="mc-cover-subtitle">효성 AI 팀 SmartChem 사례로 보는 업무 자동화 ROI</div>
</div>

<div style="margin: 0 0 1.3rem; padding: 1rem 1.1rem; border-radius: 16px; background: linear-gradient(135deg, #ecfeff 0%, #f8fafc 100%); border: 1px solid #99f6e4; color: #1f2937;">
  <div style="font-weight: 800; color: #0f766e; margin-bottom: 0.35rem;">Article Summary</div>
  <div style="line-height: 1.85;">무대 위에 오른 것은 화려한 신기술이 아니라 매일 반복되던 5만여 건의 화학물질 분류 업무였습니다. 효성 AI 팀이 Teams, Copilot Studio, Excel Script, SAP 연동으로 만든 업무 변화와 ROI를 정리했습니다.</div>
</div>

<p>무대 위에 오른 것은 화려한 신기술이 아니었습니다. 매일 책상 위에 쌓이던 <strong>5만여 건의 화학물질 분류 업무</strong>였습니다. 효성 AI 팀은 AI Tour Seoul 2026 라이트닝 토크 무대에서, <strong>연 4억 원·6,300시간</strong>이라는 숫자로 그 무게를 뒤집어 보였습니다.</p>

<p>객석을 놓친 독자들을 위해, 편집팀이 그날의 이야기를 다시 펼쳐 듭니다.</p>

<div class="mc-callout">
  <div style="line-height: 1.85; color: #374151;">글. <strong>월간 코파일럿 편집팀</strong> · 사례. <strong>효성 AI 팀 — 은성용, 박선희, 김한민</strong></div>
</div>

<img src="/mwkorea/assets/images/20260522-hyosung-ai-review/image1.jpeg" alt="효성 AI 팀 SmartChem 사례" />

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title">10 → 2분</div>
    <div>건당 판정 소요 시간</div>
    <div class="mc-card-note">약 80% 단축</div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title">6,300시간</div>
    <div>연간 절감 업무 시간</div>
    <div class="mc-card-note">매년 돌아오는 시간</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title">4억 원</div>
    <div>연간 비용 절감 효과</div>
    <div class="mc-card-note">구조적 재투자 여력</div>
  </div>
</div>

<div class="mc-callout mc-card--blue">
  <div class="mc-card-title">한눈에 보는 변화</div>
  <div style="line-height: 1.85;">연 53,739건 규모의 반복 분류 업무가 표준화됐고, 판정 근거는 자동으로 관리됩니다. 담당자는 SAP 화면을 오가며 수동 판별하던 역할에서, Teams 안에서 AI 판정 결과를 검토하고 의사결정하는 역할로 이동했습니다.</div>
</div>

<hr/>

<h2 class="mc-section-title">왜 하필, 화학물질이었나</h2>

<p>화학물질 관리는 법령에 따른 강제 관리 항목입니다. 단 한 건의 오분류도 행정처분과 사고 책임으로 이어질 수 있습니다.</p>

<p>그럼에도 현실의 판단은 여전히 담당자의 경험과 수기 검색, 신청자의 유선 문의에 기대고 있었습니다. 판단은 경험에 의존하고, 근거는 개인의 머릿속에만 머무는 구조였습니다.</p>

<div class="mc-callout">
  <div class="mc-card-title">효성 AI 팀의 출발점</div>
  <div>담당자의 최종 책임은 그대로 두되, 반복 업무만 에이전트에게 옮겨 담는 것. SmartChem은 바로 이 지점에서 시작됐습니다.</div>
</div>

<hr/>

<h2 class="mc-section-title">한 번의 대화, 네 개의 동사</h2>

<p>업무 흐름은 네 개의 동사로 압축됩니다. <strong>Ask · Analyze · Approve · Share.</strong></p>

<p>담당자는 <strong>Teams 창 하나</strong>에서 질의하고, 자재를 내려받고, 판정하고, 검토하고, 등록까지 마칩니다. 창을 옮길 일도, 맥락이 끊길 일도 없습니다.</p>

<div class="mc-card-grid mc-card-grid--4">
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title">STEP 1 · Ask</div>
    <div>최신 규제·통제 기준과 자재 내역을 자연어로 묻고, 근거 답변을 받습니다.</div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title">STEP 2 · Analyze</div>
    <div>신규 자재 리스트를 내려받고, 3만 건 이상 기등록 내역 기반으로 1차 판정합니다.</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title">STEP 3 · Approve</div>
    <div>Human-in-the-loop 구조로 전건 검토·수정하고, 판정 불가 건은 담당자가 최종 판단합니다.</div>
  </div>
  <div class="mc-card mc-card--amber">
    <div class="mc-card-title">STEP 4 · Register & Share</div>
    <div>검토 완료 파일을 SharePoint에 저장하고 관련 부서 메일링과 SAP 등록 흐름으로 이어집니다.</div>
  </div>
</div>

<img src="/mwkorea/assets/images/20260522-hyosung-ai-review/image2.png" alt="SmartChem 업무 흐름" />

<hr/>

<h2 class="mc-section-title">ROI를 고정한 두 개의 결정</h2>

<p>4억 원과 6,300시간이라는 숫자는 저절로 나오지 않았습니다. 효성 AI 팀은 수많은 시행착오를 거쳐, 두 개의 기술적 결정 위에 ROI를 고정해 냈습니다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title">DECISION ① 판정 엔진: Excel Script</div>
    <div>정확도를 수학으로 잠그는 선택이었습니다.</div>
    <ul>
      <li>기등록 자재 3만 건 이상을 학습 데이터로 활용</li>
      <li>통계 편향도와 자연어 유사도 수치화</li>
      <li>판정 불가 건은 담당자 필수 검토로 자동 분기</li>
      <li>표본·비율·유사도 기반 Explainable Reason 자동 생성</li>
    </ul>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title">DECISION ② SAP 실시간 연동: Custom Connector</div>
    <div>보안 체계를 흔들지 않으면서 물리적 제약을 풀었습니다.</div>
    <ul>
      <li>Cloud API Gateway 기반 컴플라이언스 보안 체계 수립</li>
      <li>사번 기반 권한 자동 인식으로 사용자별 리스트 제공</li>
      <li>SAP 접속 없이 어디서나 업무 가능한 Anywhere Work 구현</li>
      <li>현업 최대 페인포인트였던 물리적 제약 해소</li>
    </ul>
  </div>
</div>

<img src="/mwkorea/assets/images/20260522-hyosung-ai-review/image3.png" alt="SmartChem 판정 엔진 구조" />
<img src="/mwkorea/assets/images/20260522-hyosung-ai-review/image4.png" alt="SmartChem SAP 연동 구조" />

<div class="mc-callout mc-card--purple">
  <div style="font-weight: 800; margin-bottom: 0.45rem;">발표 중에서</div>
  <div style="line-height: 1.85;"><em>"에이전트의 답변에서 최신 정보가 중요한가, 정해진 절차가 중요한가, 결과의 정확도가 중요한가. 그 질문에 따라 지식과 지침에 자유도를 맡길지, Flow로 묶을지, Excel Script로 할루시네이션을 완벽히 배제할지를 고르는 것 — 그게 에이전트 설계의 가장 핵심적인 역량이었습니다."</em></div>
  <div style="margin-top: 0.55rem; color: #6b7280;">— 효성 AI 팀 박선희 PM 발표 중에서</div>
</div>

<hr/>

<h2 class="mc-section-title">숫자 너머의 가치</h2>

<p>시간과 비용은 ROI의 절반입니다. 나머지 절반은 업무의 체질 변화에 있습니다.</p>

<p>판정 기준이 표준화되고, 모든 판정은 <strong>왜 그렇게 결론 났는가</strong>에 대한 설명 가능한 근거를 남깁니다. 담당자의 역할은 수동 판별자에서 <strong>AI 판정 결과의 의사결정자</strong>로 이동했습니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--teal"><div class="mc-card-title">VALUE ① 완결성</div><div>Ask · Analyze · Approve · Register & Share를 하나의 End-to-End로 연결</div></div>
  <div class="mc-card mc-card--blue"><div class="mc-card-title">VALUE ② 신뢰성</div><div>표본·비율·유사도 기반 Explainable Reason 자동 생성</div></div>
  <div class="mc-card mc-card--purple"><div class="mc-card-title">VALUE ③ 확장성</div><div>SAP 연동 검증 이후 타 업무 프로세스로 Agentification 확산</div></div>
</div>

<div class="mc-callout mc-callout--dark">
  <div style="font-weight: 800; margin-bottom: 0.5rem; font-size: 1.05rem;">CLOSING</div>
  <div>"이번 에이전톤을 하고 나니까, <strong>이것도 할 수 있지 않을까?</strong> 하는 영역이 보이기 시작했습니다."</div>
  <div style="margin-top: 0.75rem; color: #cbd5e1;">정형화된 보고 업무, 반복적인 관리 업무 — 에이전트에게 맡길 수 있는 후보는 도처에 있습니다. SmartChem은 그 확장 가능성에 대한 가장 정직한 증거입니다.</div>
</div>

<div class="mc-callout mc-card--blue">
  <div class="mc-card-title">BROCHURE · 에이전트 사례집</div>
  <div>AI Tour Seoul 2026 에이전톤 <strong>Top 10 전체 사례</strong>가 궁금하신가요? 수상팀의 에이전트 설계 방법론과 비즈니스 임팩트를 한 권에 담은 에이전트 사례집 브로셔에서 확인하실 수 있습니다.</div>
  <div style="margin-top: 0.75rem;"><a href="https://aka.ms/aiagents_abs" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 0.45rem 0.8rem; border-radius: 999px; background: #1d4ed8; color: #ffffff; font-weight: 700; text-decoration: none;">브로셔 바로가기</a></div>
</div>

<div class="mc-callout" style="text-align: center;">
  <div class="mc-card-title">COMING NEXT</div>
  <div><strong>에이전톤 Top 10, 다음 호에서 계속됩니다.</strong></div>
  <div style="margin-top: 0.45rem; color: #6b7280;">SmartChem 외에도 현장을 바꿔놓은 에이전트 사례들이 기다리고 있습니다. 월간 코파일럿 7월호에서 만나보세요.</div>
</div>

</div>
