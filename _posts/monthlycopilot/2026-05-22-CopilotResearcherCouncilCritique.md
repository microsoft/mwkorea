---
title: '이제 AI도 팀플하는 시대'
date: 2026-05-22T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - 멀티모델
  - Researcher
  - Model Council
  - Critique
  - 월간코파일럿
excerpt: 'Copilot의 멀티모델 전략과 Researcher 에이전트의 Critique, Model Council 기능을 통해 어떤 업무에 어떤 모델 협업 방식을 선택하면 좋은지 정리했습니다.'
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 김현지
---

<div class="monthlycopilot-page monthlycopilot-page--agent">
<div class="mc-issue-strip">Monthly Copilot · June 2026 · 월간 코파일럿 소식지 6월호 · Special Feature · Multimodel</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">월간 코파일럿 소식지 ｜ 2026년 6월호</div>
  <div class="mc-cover-title">이제 AI도<br/>팀플하는 시대</div>
  <div class="mc-cover-subtitle">Copilot Researcher의 Critique와 Model Council</div>
</div>

<div style="margin: 0 0 1.3rem; padding: 1rem 1.1rem; border-radius: 16px; background: linear-gradient(135deg, #ecfeff 0%, #f8fafc 100%); border: 1px solid #99f6e4; color: #1f2937;">
  <div style="font-weight: 800; color: #0f766e; margin-bottom: 0.35rem;">Article Summary</div>
  <div style="line-height: 1.85;">Copilot은 WorkIQ와 M365 보안 위에서 여러 모델을 업무에 맞게 선택하고 조합합니다. 특히 Researcher 에이전트의 Critique와 Model Council은 모델이 서로 검토하고 의견을 모으는 새로운 협업 방식을 보여줍니다.</div>
</div>

<img src="/mwkorea/assets/images/20260522-council-vs-critique/image1.png" alt="Copilot Researcher 멀티모델 개요" />

<h2 class="mc-section-title">AI가 하나일 필요는 없다</h2>

<p>얼마 전까지만 해도 "AI = 하나의 모델"이 당연했습니다. 그러나 업무 현장의 요구는 이렇게 단순하지 않습니다. 어떤 작업은 빠른 응답이 중요하고, 어떤 작업은 깊이 있는 추론이 필요합니다. 마케팅 카피 한 줄과 분기 실적 보고서가 같은 모델로 충분할 리 없습니다.</p>

<p>Microsoft 365 Copilot은 이 문제를 "모델을 골라 쓸 수 있게 한다"는 방식으로 풀어 갑니다. 그것도 단순히 모델을 바꾸는 수준이 아니라, 모델끼리 협업하고 서로를 검토하게 만드는 단계로 진화했습니다.</p>

<div class="mc-callout mc-card--blue">
  <div class="mc-card-title">3줄 요약</div>
  <ul>
    <li>Copilot은 WorkIQ로 내 업무 맥락을 이해하고, M365 보안을 그대로 상속합니다.</li>
    <li>Copilot Chat과 Researcher 에이전트 안에서 모델을 직접 고를 수 있습니다.</li>
    <li>여러 모델을 협업시키려면 Critique나 Model Council을 선택하면 됩니다.</li>
  </ul>
</div>

<hr/>

<h2 class="mc-section-title">1. Copilot 멀티모델 전략을 떠받치는 3가지 기반</h2>

<p>Copilot의 멀티모델은 단독으로 존재하지 않습니다. 업무 맥락, 엔터프라이즈 보안, 모델 선택권이 함께 움직일 때 진가가 발휘됩니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title">① WorkIQ</div>
    <div>이메일, 문서, 회의 기록, Teams 대화, 캘린더, OneDrive·SharePoint 파일을 권한 범위 안에서 이해합니다.</div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title">② 엔터프라이즈 보안</div>
    <div>민감도 레이블, DLP, 조건부 액세스, 거버넌스 정책이 그대로 적용됩니다. 기업 데이터는 모델 학습에 사용되지 않습니다.</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title">③ 멀티모델</div>
    <div>빠른 응답, 깊은 추론, 다양한 관점 검토처럼 업무 목적에 맞는 모델 활용 방식을 선택할 수 있습니다.</div>
  </div>
</div>

<hr/>

<h2 class="mc-section-title">2. Copilot Chat에서도 모델을 고를 수 있어요</h2>

<p>멀티모델은 거창한 기능이 아닙니다. 가장 친숙한 Copilot Chat에서 이미 시작됩니다. 새 채팅을 열면 입력창 옆에 모델 선택 버튼이 보입니다.</p>

<img src="/mwkorea/assets/images/20260522-council-vs-critique/image2.png" alt="Copilot Chat 모델 선택" />

<div class="mc-card-grid">
  <div class="mc-card mc-card--teal"><div class="mc-card-title">일상 작업</div><div>요약, 검색, 간단한 질문은 신속한 응답 계열이 잘 맞습니다.</div></div>
  <div class="mc-card mc-card--blue"><div class="mc-card-title">깊은 분석</div><div>분석과 다단계 추론은 깊이 생각하기 계열을 선택합니다.</div></div>
  <div class="mc-card mc-card--purple"><div class="mc-card-title">특화 작업</div><div>코드, 수식, 정형 작업은 Claude 또는 GPT 계열 특화 모델을 직접 지정할 수 있습니다.</div></div>
  <div class="mc-card mc-card--amber"><div class="mc-card-title">모를 때</div><div>어떤 모델이 맞을지 모른다면 자동을 유지하면 Copilot이 상황에 맞춰 선택합니다.</div></div>
</div>

<p>이 정도는 메뉴판에서 음료 하나 고르는 정도의 단순한 선택입니다. 진짜 재미있는 영역은 그다음에 있습니다. Researcher 에이전트에 들어가면 모델 선택이 솔로 작업에서 팀 작업으로 진화합니다.</p>

<img src="/mwkorea/assets/images/20260522-council-vs-critique/image3.png" alt="Researcher 에이전트 모델 선택" />

<hr/>

<h2 class="mc-section-title">3. Researcher 에이전트 — 모델 선택의 진짜 무대</h2>

<p>Researcher는 단순한 챗봇이 아니라 리서치를 대신해 주는 에이전트입니다. 자료를 모으고, 비교하고, 인사이트를 도출하는 작업 흐름 안에서 사용자에게 세 가지 모델 선택 옵션을 제공합니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--teal"><div class="mc-card-title">직접 모델 선택</div><div>내가 원하는 모델을 메뉴에서 직접 고릅니다.</div><div class="mc-card-note">사용해 본 모델이 명확하고 결과 스타일에 익숙할 때</div></div>
  <div class="mc-card mc-card--blue"><div class="mc-card-title">Critique</div><div>한 모델이 작성한 결과를 다른 모델이 점검하고 검증합니다.</div><div class="mc-card-note">정확성·신뢰성이 중요한 보고서나 외부 문서</div></div>
  <div class="mc-card mc-card--purple"><div class="mc-card-title">Model Council</div><div>여러 모델이 동시에 답변하고 의견을 모아 종합합니다.</div><div class="mc-card-note">전략 기획·시장 진단처럼 다양한 시각이 필요할 때</div></div>
</div>

<p>같은 질문을 던져도 어떤 옵션을 고르느냐에 따라 결과의 깊이와 신뢰도가 완전히 달라집니다.</p>

<hr/>

<h2 class="mc-section-title">4. Critique — 한 번 더 검토받고 싶을 때</h2>

<p>Critique는 GPT 모델이 작성한 결과를 Claude 모델이 점검·검증하는 방식입니다. 사람으로 치면 "내가 쓴 보고서를 옆 부서 전문가에게 한 번 봐 달라"는 것과 같습니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue"><div class="mc-card-title">Step 1</div><div>메인 모델이 사용자의 질문에 대해 초안을 작성합니다.</div></div>
  <div class="mc-card mc-card--blue"><div class="mc-card-title">Step 2</div><div>다른 모델이 초안을 읽고 사실관계·논리·누락·편향을 점검합니다.</div></div>
  <div class="mc-card mc-card--blue"><div class="mc-card-title">Step 3</div><div>검토 의견이 반영된 최종 결과가 사용자에게 전달됩니다.</div></div>
</div>

<div class="mc-callout mc-card--blue">
  <div class="mc-card-title">Critique를 한 줄로 말하면</div>
  <div>"내 글, 다른 전문가에게 한 번 검토 부탁할게요." 정확성과 신뢰성을 한 단계 끌어올리는 안전장치입니다.</div>
</div>

<img src="/mwkorea/assets/images/20260522-council-vs-critique/image4.png" alt="Researcher Critique 기능" />

<hr/>

<h2 class="mc-section-title">5. Model Council — 여러 시각이 필요할 때</h2>

<p>Model Council은 여러 모델이 같은 질문에 동시에 답변하고, 그 의견을 모아 종합하는 방식입니다. 사람으로 치면 "여러 전문가에게 동시에 자문을 구해 봅시다"에 가깝습니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--purple"><div class="mc-card-title">Step 1</div><div>사용자의 질문이 여러 모델에 동시에 전달됩니다.</div></div>
  <div class="mc-card mc-card--purple"><div class="mc-card-title">Step 2</div><div>각 모델이 자신의 강점에 따라 독립적으로 답변을 생성합니다.</div></div>
  <div class="mc-card mc-card--purple"><div class="mc-card-title">Step 3</div><div>답변이 비교·정렬되고 공통점, 차이점, 종합 인사이트가 도출됩니다.</div></div>
</div>

<div class="mc-callout mc-card--purple">
  <div class="mc-card-title">Model Council을 한 줄로 말하면</div>
  <div>"여러 전문가에게 동시에 자문을 구해 봅시다." 다양한 시각으로 사각지대를 줄이는 집단지성 모드입니다.</div>
</div>

<img src="/mwkorea/assets/images/20260522-council-vs-critique/image5.png" alt="Researcher Model Council 기능" />

<hr/>

<h2 class="mc-section-title">6. 한눈에 보는 Critique vs Model Council</h2>

<div class="mc-table-wrap">
  <table>
    <tr><th>구분</th><th>Critique</th><th>Model Council</th></tr>
    <tr><td>핵심 컨셉</td><td>한 모델이 작성하고 다른 모델이 점검·보완</td><td>여러 모델이 동시에 답변하고 의견을 모아 합의안 도출</td></tr>
    <tr><td>작동 방식</td><td>초안 작성 → 사실관계·논리·누락 점검 → 최종 보완 결과 제시</td><td>동일 질문에 각자 답변 → 답변 비교·종합 → 합의된 인사이트 도출</td></tr>
    <tr><td>강점</td><td>정확성·신뢰성 강화, 오류·환각 감소</td><td>다양한 시각 확보, 사각지대 최소화, 의사결정 균형</td></tr>
    <tr><td>적합한 업무</td><td>경영진 보고서, 계약·법무 검토, 재무 분석, 외부 발신 콘텐츠</td><td>전략 기획, 시장 진단, 신사업 아이디어, 리스크 시나리오 분석</td></tr>
    <tr><td>결과물 특징</td><td>정제된 단일 결과와 검토 코멘트</td><td>모델별 의견과 종합 요약</td></tr>
    <tr><td>한 줄 비유</td><td>내 글, 다른 전문가에게 한 번 검토 부탁할게요.</td><td>여러 전문가에게 동시에 자문을 구해 봅시다.</td></tr>
  </table>
</div>

<hr/>

<h2 class="mc-section-title">7. 언제 무엇을 쓸까 — 실무 시나리오</h2>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title">Critique가 어울리는 순간</div>
    <ul>
      <li>임원진에게 보낼 분기 실적 요약을 다듬을 때</li>
      <li>외부 고객 제안서의 사실관계 오류를 없애야 할 때</li>
      <li>법무팀 검토 전 계약서 초안을 정제하고 싶을 때</li>
    </ul>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title">Model Council이 어울리는 순간</div>
    <ul>
      <li>내년 사업 전략 초안 전에 다양한 관점을 모으고 싶을 때</li>
      <li>새로운 시장 진입 리스크와 기회를 폭넓게 검토할 때</li>
      <li>내가 놓친 관점이 두려울 때</li>
    </ul>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title">직접 모델 선택이 어울리는 순간</div>
    <ul>
      <li>이미 사용해 본 모델의 스타일을 잘 아는 반복 업무</li>
      <li>빠른 응답이 더 중요한 회의록 요약과 표 정리</li>
      <li>특정 모델의 추론 깊이를 직접 활용하고 싶을 때</li>
    </ul>
  </div>
</div>

<hr/>

<h2 class="mc-section-title">8. 마무리 — AI도 골라 쓰는 시대</h2>

<p>하나의 AI로 모든 일을 처리한다는 시대는 이미 지났습니다. 빠른 답이 필요할 때, 깊은 분석이 필요할 때, 다른 시각이 필요할 때마다 가장 적합한 도구를 고를 수 있어야 진짜 생산성이 따라옵니다.</p>

<p>Copilot의 멀티모델 전략은 단순한 모델 스위치가 아니라, 업무 품질을 끌어올리는 협업 프레임워크입니다. Critique로 정확성을 한 단계 더 다듬고, Model Council로 시야를 넓혀 보세요.</p>

<div class="mc-callout mc-callout--dark">
  <div style="font-weight: 800; margin-bottom: 0.5rem; font-size: 1.05rem;">이번 호 액션 아이템</div>
  <div>1. Copilot Chat에서 새 채팅을 열고 모델 선택 메뉴를 클릭해 보세요.<br/>2. 다음 보고서 작업에서 Researcher의 Critique를 적용해 보세요.<br/>3. 다음 전략 미팅 준비 시 Model Council로 다양한 시각을 모아 보세요.</div>
</div>

</div>
