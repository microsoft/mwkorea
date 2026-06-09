---
title: '완전히 새로워진 Copilot Studio'
date: 2026-06-10T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - CopilotStudio
  - Agent
  - Workflow
  - 월간코파일럿
excerpt: 'Copilot Studio가 처음부터 재설계되어 정식 출시(GA)되고, 자연어로 만드는 새 에이전트 경험이 미리 보기로 등장했습니다. 무엇이 달라졌고 무엇을 먼저 챙겨야 할지 한눈에 정리합니다.'
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 최정우
---

<div class="monthlycopilot-page monthlycopilot-page--adoption">
<div class="mc-issue-strip">Monthly Copilot · June 2026 · 월간 코파일럿 소식지 6월호 · Breaking · Copilot Studio</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">월간 코파일럿 ｜ 2026년 6월호 ｜ Breaking</div>
  <div class="mc-cover-title">완전히 새로워진<br/>Copilot Studio</div>
  <div class="mc-cover-subtitle">복잡한 다단계 업무를 위해, 처음부터 다시 설계되다</div>
</div>

<img src="/mwkorea/assets/images/20260610-copilotstudio-update/comic.png" alt="Classic vs New 비교 만화: 토픽·플로 노드를 일일이 짜야 했던 기존(Classic) 방식과, 자연어 한 줄로 에이전트를 구성하는 새 경험(New)을 대비하고, 화면 구분법과 선택 기준·마이그레이션 불가까지 보여주는 4컷 만화" />

<p><strong>▲ 한 컷으로 보는 Classic vs New</strong> 정해진 토픽·플로우 레일대로만 움직이던 '스크립트 봇'(Classic)과, 에이전틱 AI 코어로 스스로 추론·계획·실행하는 '진짜 AI 에이전트'(New). 목표와 도구만 주면 여러 단계를 끝까지 자율로 해냅니다. 단, 두 경험은 다른 런타임이라 마이그레이션은 불가합니다.</p>

<div style="margin: 0 0 1.3rem;padding: 1rem 1.1rem; border-radius: 16px; background: linear-gradient(135deg, #ecfeff 0%, #f8fafc 100%); border: 1px solid #99f6e4; color: #1f2937;">
  <div style="font-weight: 800; color: #0f766e; margin-bottom: 0.35rem;">Article Summary</div>
  <div style="line-height: 1.85;">재구축된 Copilot Studio가 전 세계 정식 출시(GA)됐고, <strong>에이전틱 AI 코어</strong>를 도입한 ‘새 에이전트 경험’이 미리 보기로 추가됐습니다. 정해진 토픽·플로우대로만 움직이던 봇을 넘어, 스스로 추론·계획·실행하는 <strong>진짜 AI 에이전트</strong>로 진화했습니다. 새 워크플로, 컴퓨터 사용 에이전트 GA, 실시간 음성까지 한 번에 도착했습니다.</div>
</div>

<div class="mc-callout mc-card--purple">
  <div><strong>“한두 단계는 잘 되는데, 여러 단계가 얽히면 중간에 끊긴다.”</strong> 에이전트를 만들어 본 사람이라면 누구나 부딪힌 벽입니다. 이번 개편의 출발점이 바로 그 피드백이었습니다.</div>
</div>

<p>Microsoft가 <strong>Copilot Studio를 처음부터 다시 설계(rebuilt)</strong>했습니다. 새 작성 경험과 현대화된 AI 코어로, 에이전트와 워크플로가 <strong>더 일관되고 신뢰할 수 있는 결과</strong>를 내도록 만든 것이 핵심입니다. 무엇보다 이 업데이트는 <strong>전 세계에 정식 출시(GA)</strong>되어 곧바로 프로덕션 용도로 쓸 수 있습니다.</p>

<hr/>

<h2 class="mc-section-title">더 안정적인 에이전트</h2>

<p>핵심 구성만 전면에 배치해 <strong>구성 탭을 9개에서 4개로</strong> 줄였습니다. 더 빠르고, 더 유능하고, 더 효율적으로 에이전트를 만들 수 있습니다.</p>

<ul>
  <li><strong>새 agentic 오케스트레이터</strong> — 코딩 하네스·CLI 레이어 위에 구축되어 지시 준수력과 장기 과제 수행력이 강해졌고, 재귀적 작업 실행·대용량 콘텐츠·파일 출력을 지원합니다.</li>
  <li><strong>한 화면 빌딩</strong> — 지시·스킬·도구·지식을 한 화면에서 보고, 인라인 사고 과정(chain-of-thought)과 도구 호출까지 테스트 중에 확인합니다.</li>
  <li><strong>스킬(Skills)</strong> — 재사용 지시를 Markdown으로 작성하고, 기존 GitHub Copilot·Claude Code 스킬도 그대로 임포트할 수 있습니다.</li>
</ul>

<hr/>

<h2 class="mc-section-title">‘진짜 AI 에이전트’가 되다 — 새 에이전트 경험 (미리 보기)</h2>

<p>이번 변화의 진짜 핵심은 단순한 자연어 작성이 아니라 <strong>에이전틱(agentic) AI 코어의 도입</strong>입니다. 기존(Classic)이 미리 짜둔 토픽·플로우 레일대로만 움직이는 <strong>스크립트 봇</strong>에 가까웠다면, 새 경험은 새 <strong>agentic 오케스트레이터</strong> 위에서 <strong>스스로 추론하고, 도구를 호출하고, 여러 단계를 끝까지 수행</strong>하는 <strong>진짜 AI 에이전트</strong>입니다. 목표와 지시·지식·도구만 주면 나머지 실행 계획은 에이전트가 알아서 세웁니다.</p>

<ul>
  <li><strong>자율 추론·실행</strong> — 재귀적(recursive) 작업과 장기 과제(long-horizon)를 중간에 끊기지 않고 끝까지 처리</li>
  <li><strong>자연어 우선 작성</strong> — 토픽·노드를 짜는 대신 에이전트의 정체성·역할·행동 규칙을 말로 기술하고, 지식·도구·스킬·모델을 <strong>Build</strong> 탭에서 구성</li>
  <li><strong>단일 화면</strong> — <strong>Build · Preview · Evaluate · Monitor</strong> 네 탭으로 통합되어 품질 평가·모니터링이 작성 루프의 일부가 됨</li>
</ul>

<div class="mc-callout">
  <p><strong>지금 내 화면, 어느 경험일까?</strong></p>
  <p>왼쪽에 <strong>Topics / Knowledge / Actions / Settings</strong>가 따로 보이면 <strong>기존(Classic)</strong>, 상단에 <strong>Build / Preview / Evaluate / Monitor</strong> 탭이 보이면 <strong>새 경험(New)</strong>입니다.</p>
  <p><strong>⚠ 두 경험은 다른 런타임이라 마이그레이션은 불가합니다.</strong> 새 경험을 쓰려면 새 에이전트를 새로 만들어야 하고, 기존 에이전트는 그대로 동작합니다. 자율적인 다단계 작업이나 M365 데이터 추론이 주 용도라면 새 경험을, 정해진 흐름을 정밀하게 제어해야 하면 기존 경험을 선택하세요.</p>
</div>

<hr/>

<h2 class="mc-section-title">함께 도착한 소식</h2>

<p><strong>새 워크플로 디자이너</strong> — 단일 캔버스에서 end-to-end로 설계하고, 노드 단위 테스트·버전 관리를 지원합니다. <strong>에이전트 노드</strong>로 워크플로 안에서 에이전트를 직접 호출하고, <strong>MCP 서버(미리 보기)</strong>로 외부 도구 생태계에 안전하게 연결합니다.</p>

<p><strong>컴퓨터 사용 에이전트 GA</strong> — API가 없는 레거시·포털도 UI로 직접 조작해 자동화합니다. <strong>실시간 음성 에이전트</strong>는 Dynamics 365 Contact Center에서 북미 지역 GA로, 맥락을 유지한 채 상담사 인계까지 지원합니다. <strong>Work IQ</strong>는 REST API·CLI와 에이전트 간(A2A) 통신 GA로 시스템 간 협업을 넓혔습니다.</p>

<hr/>

<h2 class="mc-section-title">한눈에 보기 — 성숙도 구분</h2>

<div class="mc-callout mc-card--purple">
  <p><strong>중요 — 어디까지 GA이고 어디부터 미리 보기일까?</strong></p>
  <p>전면 재구축된 <strong>Copilot Studio 플랫폼 자체와 빌딩 경험은 전 세계 GA</strong>로, 곧바로 프로덕션에 쓸 수 있습니다. 다만 그 안의 <strong>개별 기능들은 성숙도가 제각각</strong>입니다 — 일부는 GA, 상당수는 <strong>공개 미리 보기(public preview)</strong>, 그리고 <strong>아직 개발 중</strong>이라 순차 출시되는 기능도 있습니다. 미리 보기·개발 중 기능은 정식 출시 전까지 동작과 범위가 바뀔 수 있으니, 프로덕션 채택 시 각 기능의 상태를 꼭 확인하세요.</p>
</div>

<div class="mc-callout">
  <p><strong>빌딩 경험·플랫폼 재구축</strong> — 새 agentic 오케스트레이터, 구성 탭 9→4개, 스킬 · <strong>GA</strong></p>
  <p><strong>새 에이전트 경험(작성 화면)</strong> — 에이전틱 코어·자연어 작성·단일 화면 · <strong>공개 미리 보기</strong></p>
  <p><strong>새 워크플로 디자이너 / 에이전트 노드</strong> — 단일 캔버스 설계 · <strong>미리 보기·얼리 릴리스</strong></p>
  <p><strong>MCP 서버 연결 / 워크플로 내 컴퓨터 사용</strong> — 외부 도구·UI 자동화 임베드 · <strong>미리 보기(일부 개발 중)</strong></p>
  <p><strong>컴퓨터 사용 에이전트</strong> — UI 자동화 · <strong>GA</strong></p>
  <p><strong>실시간 음성 에이전트</strong> — Contact Center · <strong>GA(북미)</strong></p>
  <p><strong>Work IQ</strong> — REST·CLI · <strong>미리 보기</strong> / 에이전트 간(A2A) 통신 · <strong>GA</strong></p>
</div>

<div class="mc-callout mc-callout--dark">
  <div style="font-weight: 800; margin-bottom: 0.5rem; font-size: 1.05rem;">지금, 바로 시작.</div>
  <div>복잡한 다단계 업무를 에이전트에게 맡겨 보고 싶었지만 안정성 때문에 망설였다면, 지금이 그 시점입니다.<br/>Copilot Studio 홈 상단의 <strong>‘Try now’</strong>를 눌러 새 경험을 가볍게 시험해 보세요.</div>
  <div style="margin-top: 0.8rem; font-size: 0.92rem; color: #9ca3af;">월간 코파일럿 · 2026년 6월호 · Breaking by Editorial Desk</div>
</div>

</div>
