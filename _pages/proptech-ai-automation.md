---
layout: single
title: "데이터가 흐르는 속도로, 현업이 움직인다"
permalink: /hidden/proptech-ai-automation/
author_profile: true
sitemap: false
search: false
excerpt: "코드 한 줄 없이 에이전톤 무대에 오른 비개발자 팀의 현업 주도 부동산 데이터 자동 수집·검증·분석 에이전트 이야기입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 김현지
---

<div class="monthlycopilot-page monthlycopilot-page--agent">
<div class="mc-issue-strip">월간 코파일럿&nbsp; · &nbsp;2026년 8월호</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">월간 코파일럿 ｜ 2026년 8월호</div>
  <div class="mc-cover-title">데이터가 흐르는 속도로,<br/>현업이 움직인다</div>
  <div class="mc-cover-subtitle">현업 주도 AI 자동화 전략</div>
</div>

<div class="mc-card mc-card--amber">
  <div class="mc-card-title"><strong>🎖️ SPECIAL MENTION · 심사위원특별상 수상</strong></div>
  <p><strong>에이전톤 심사위원특별상 수상팀</strong></p>
  <p>구성: <strong>서비스 운영 · 데이터 분석 · DX인프라 담당자 3인</strong></p>
  <p>프로젝트: <strong>부동산 데이터 『자동 수집·검증·분석』 에이전트</strong></p>
</div>

<hr/>

<h2 class="mc-section-title">01. MEET THE TEAM</h2>

<h3>코드 한 줄 없이, 무대 위에 오른 사람들</h3>

<p>코드 한 줄 쓰지 않고도 에이전톤의 무대에 오를 수 있을까요. <strong>AI Tour Agenthon in Seoul 2026</strong>의 답은 “그렇다”였습니다. 주인공은 <strong>전원 비개발자로 구성된 한 팀</strong>이었습니다. 이들의 모토는 단순했습니다. <em>“문제를 한 조각씩 나누어 해결한다”</em>. 한입에 삼키기엔 너무 큰 문제도, 조각으로 나누면 결국 풀린다는 믿음입니다.</p>

<p>서비스 운영을 맡은 사람, 데이터를 들여다보던 사람, 클라우드를 다루던 사람, 부서도 역할도 달랐던 세 명이 한 자리에 모인 이유는 단 하나였습니다. <strong>’현업의 문제는 현업이 가장 잘 푼다’</strong>는 단순한 진실을 증명해 보고 싶었기 때문입니다.</p>

<p>프롭티어는 부동산 데이터의 속도와 정확성이 곧 서비스의 신뢰이자 핵심 경쟁력이라는 믿음 아래, 현업 중심의 AI 자동화를 실무에 전격 도입하여 데이터 가치를 극대화하고 있습니다. 이번 에이전톤에서는 본 수상은 아니지만, <strong>인상적인 발표와 현업 밀착형 에이전트 사례</strong>로 심사위원의 마음을 움직여 <strong>‘심사위원특별상’</strong>을 거머쥐었습니다. 트로피의 무게보다 더 묵직했던 것은 “우리도 바꿀 수 있다”라는 자부심이었습니다.</p>

<p>거창한 비전 대신 이들이 꺼내 든 것은 <strong>데이터 사업 담당자의 평범한 하루 일과 안에서의</strong> 매일 같은 시간, 같은 한숨, 같은 반복, 그 작은 균열에서 시작된 자동화 이야기를 현업의 시각으로 한 조각씩 풀어가는 과정을 보여줍니다.</p>

<img src="/mwkorea/assets/images/20260719-proptech-ai-automation/agenthon-team.jpeg" alt="AI Tour Agenthon in Seoul 2026 행사장에 선 프롭티어 팀원 3명" />

<hr/>

<h2 class="mc-section-title">02. THE PROBLEM</h2>

<h3>매일 아침, 전국 지자체 사이트와 마주하는 사람들</h3>

<p>데이터사업팀 개발 고시문 담당자의 하루는 <strong>전국 지자체의 고시문 사이트를 한 곳씩 확인</strong>하는 일로 시작되었습니다. 신규 고시문이 올라왔는지 수동으로 살피고, 변경 내용은 육안으로 비교하며, 필요하면 파일을 내려받아 서비스 어드민 페이지에 일일이 옮겨 적었습니다.</p>

<div class="mc-callout mc-card--amber">
  <p>이 단순 반복 업무에 <strong>하루 평균 2~3시간</strong>이 사라졌고, 고시문이 몰리는 날에는 하루를 통째로 내어주어야 했습니다. <em>“다른 일도 많은데, 고시문이 계속 올라와요…”</em>라는 한숨은 일상이 되었습니다.</p>
</div>

<hr/>

<h2 class="mc-section-title">03. WHY NOT EARLIER?</h2>

<h3>사실, 우리도 처음부터 자동화하고 싶었습니다</h3>

<p>자동화의 필요성은 명확했지만, 실행에는 넘어야 할 과제가 있었습니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>개발 의존 구조 —</strong></div>
    <div>기존 자동화는 채널이 추가될 때마다 개발자 개입이 필요해 현업의 빠른 대응이 어려웠습니다.</div>
  </div>
  <div class="mc-card mc-card--amber">
    <div class="mc-card-title"><strong>비정형 데이터의 추출 오류 리스크 —</strong></div>
    <div>부동산 고시문은 형식이 다양해 핵심 필드 추출 시 검증이 필수입니다.</div>
  </div>
  <div class="mc-card mc-card--red">
    <div class="mc-card-title"><strong>공공 데이터 기반의 정보 제공 —</strong></div>
    <div>행정·법률 효력이 있는 고시문의 정보를 근거로 데이터를 제공하기에, 서비스 반영 전 담당자의 확인이 필요합니다.</div>
  </div>
</div>

<div class="mc-callout mc-callout--dark">
  <strong>“개발자만 수정할 수 있는 블랙박스를 만들고 싶지 않았습니다.”</strong>
</div>

<hr/>

<h2 class="mc-section-title">04. THE TURNING POINT</h2>

<h3>에이전톤이라는 기회, 그리고 세 가지 원칙</h3>

<p>AI Tour 에이전톤은 이들에게 <strong>현업 주도의 확장 가능한 자동화</strong>를 시도할 기회였습니다. 이들은 세 가지 설계 원칙을 세웠습니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>현업 주도 확장성 —</strong></div>
    <div>현업 담당자가 채널을 직접 추가하고, 즉시 자동화에 반영할 수 있는 구조</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>검증 가능한 자동화 —</strong></div>
    <div>Human-in-the-Loop(HITL) 구조로 법적 리스크를 원천 차단하고 데이터 신뢰도 확보</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>데이터 오케스트레이션 —</strong></div>
    <div>수집을 넘어 흐름 전체를 추적·관리하는 데이터 플랫폼 관점의 설계.</div>
  </div>
</div>

<p>이 원칙은 자연스럽게 <strong>Microsoft Power Platform</strong> 위에서 구현되었습니다. 추가 인프라 구성없이도 업무와 즉시 연동 가능하다는 점이 결정적이었습니다.</p>

<img src="/mwkorea/assets/images/20260719-proptech-ai-automation/automation-architecture.png" alt="데이터 필터링, 데이터 수집 및 처리, 데이터 분석 및 활용으로 이어지는 자동화 구성" />

<hr/>

<h2 class="mc-section-title">05. HOW IT WORKS</h2>

<h3>여섯 조각으로 완성되는 자동화 에이전트</h3>

<p>이들의 핵심 설계는 <strong>총 6단계의 데이터 오케스트레이션 워크플로우</strong>입니다. Power Automate, Copilot Studio, AI Builder, Power BI, Teams가 유기적으로 연결되어 한 흐름을 이룹니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>STEP 01</strong><br/>수집 대상 필터링</div>
    <div>정기 스케줄 기반 사이트 자동 모니터링과<br/>신규 고시 게시물 자동 탐지</div>
    <div class="mc-card-note">🔧 Power Automate</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>STEP 02</strong><br/>데이터 수집·적재</div>
    <div>첨부파일을 자동 다운로드하고<br/>규칙 기반으로 분류·저장</div>
    <div class="mc-card-note">🔧 Power Automate / Dataverse</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>STEP 03</strong><br/>데이터 추출</div>
    <div>OCR과 LLM 기반 핵심 필드 자동 추출 후<br/>정제 단계로 신뢰성 확보</div>
    <div class="mc-card-note">🔧 Power Automate / Copilot Studio</div>
  </div>
  <div class="mc-card mc-card--amber">
    <div class="mc-card-title"><strong>STEP 04</strong><br/>데이터 시각화</div>
    <div>추출 데이터를 한눈에 검토할 수 있는<br/>대시보드 제공</div>
    <div class="mc-card-note">🔧 Power BI</div>
  </div>
  <div class="mc-card mc-card--green">
    <div class="mc-card-title"><strong>STEP 05</strong><br/>완료 알림</div>
    <div>Teams로 진행 상황과 결과를<br/>담당자에게 즉시 발송</div>
    <div class="mc-card-note">🔧 Power Automate / Workflows</div>
  </div>
  <div class="mc-card mc-card--red">
    <div class="mc-card-title"><strong>STEP 06</strong><br/>검증 (HITL)</div>
    <div>현업 담당자의 승인·예외 처리로<br/>법적 리스크를 원천 차단</div>
    <div class="mc-card-note">🔧 User · Power BI · Power Apps</div>
  </div>
</div>

<p>에이전트가 수집과 추출, 알림까지 처리하는 동안 <strong>담당자는 오직 승인과 예외 처리에만 집중</strong>합니다. 더 이상 전국 지자체 사이트를 한 곳씩 확인할 필요가 없습니다.</p>

<img src="/mwkorea/assets/images/20260719-proptech-ai-automation/data-automation-results.png" alt="데이터 자동 수집, Teams 자동 알림, 데이터 시각화 및 분석으로 이어지는 자동화 이후 데이터 활용 방식" />

<hr/>

<h2 class="mc-section-title">06. THE NUMBERS</h2>

<h3>숫자로 보는 변화 — 시간은 줄고, 가능성은 무한이 됩니다</h3>

<p>자동화가 가져온 변화는 분명했습니다. <strong>데이터 수집 시간은 80% 이상 절감</strong>되었고, 데이터 확보는 24시간·무제한으로 확장되었습니다.</p>

<div class="mc-card-grid mc-card-grid--4">
  <div class="mc-card mc-card--blue" style="text-align:center;">
    <div class="mc-card-title"><strong>작업 시간</strong></div>
    <div style="font-size:1.8rem; font-weight:800;">30분</div>
    <div>Daily 2~3시간 → 30분 (83%↓)</div>
  </div>
  <div class="mc-card mc-card--teal" style="text-align:center;">
    <div class="mc-card-title"><strong>데이터 수집</strong></div>
    <div style="font-size:1.8rem; font-weight:800;">무중단</div>
    <div>24시간 자동 수집 체계 구축</div>
  </div>
  <div class="mc-card mc-card--purple" style="text-align:center;">
    <div class="mc-card-title"><strong>데이터 확장</strong></div>
    <div style="font-size:1.8rem; font-weight:800;">∞</div>
    <div>37개 채널 → 무한 확장</div>
  </div>
  <div class="mc-card mc-card--amber" style="text-align:center;">
    <div class="mc-card-title"><strong>업무 효율</strong></div>
    <div style="font-size:1.8rem; font-weight:800;">4.2배</div>
    <div>처리 속도 개선</div>
  </div>
</div>

<p>기존에 2~3시간이 걸리던 작업은 이제 30분 만에 마무리되며, 수집은 중단 없이 이어집니다. 수집 채널과 추출 필드는 더 이상 개발자에 의존되지 않고, 현업의 판단으로 무한히 확장될 수 있게 되었습니다.</p>

<div class="mc-callout mc-callout--dark">
  <strong>“이제 데이터를 확인하는 게 아니라, 데이터를 확장하는 일에 시간을 씁니다.”</strong>
</div>

<hr/>

<h2 class="mc-section-title">07. WHAT'S NEXT</h2>

<h3>한 조각의 자동화에서, 프롭티어 전체의 자산으로</h3>

<p>이번 프로젝트를 통해 얻은 가장 큰 가치는 <em>“하나의 자동화를 넘어, 다양한 데이터 수집에 활용 가능한 구조”</em>라는 사실입니다. 한 업무에서 출발한 흐름이 다른 업무로 복제되고, 부서를 넘어 회사 전체의 자산으로 진화하는 모습을 그리고 있습니다.</p>

<ul>
  <li>Power Apps 기반 조회·검색 기능을 추가하여 현업 활용도를 높일 예정입니다.</li>
  <li>비개발 담당자도 자동화 로직을 직접 설계할 수 있도록 현업 확산 프로그램을 운영합니다.</li>
  <li>Dataverse·SharePoint·AI Builder 도입으로 데이터 플랫폼으로 확장해 나갑니다.</li>
</ul>

<img src="/mwkorea/assets/images/20260719-proptech-ai-automation/data-platform-roadmap.png" alt="서비스 고도화, 운영 안정화, AI 자동화 확대, 현업 확산으로 구성된 데이터 플랫폼 확장 계획" />

<div class="mc-callout mc-callout--dark">
  <p><strong>“마이크로소프트 로우코드 솔루션으로 완성하고, 현업의 손으로 움직입니다.”</strong></p>
  <p><strong>프롭티어는 빠르고 정확한 부동산 데이터 경험을 위해, 지속 가능한 AI 자동화를 현업 중심으로 실현해 나갑니다.</strong></p>
</div>

<hr/>

<h2 class="mc-section-title">NEXT ISSUE</h2>

<h3>9월호에서 만나요</h3>

<p>이번 호에서는 한 수상팀의 이야기를 한 조각 깊이 들여다보았습니다. <strong>다음 9월호</strong>에서는 또 다른 에이전톤 우수팀의 사례, 현업 자동화 확산 노하우, 그리고 Copilot 신규 기능 활용 ㄴ팁이 이어집니다. 더 많은 영감과 인사이트를 기대해 주세요.</p>

<p><strong>에이전톤 사례집 전체</strong>가 궁금하시다면 아래 브로셔에서 모든 우승·수상팀의 여정을 만나 보실 수 있습니다.</p>

<p><a href="https://aka.ms/agenthon-brochure"><strong><u>📘 에이전톤 사례집 브로셔 바로가기</u></strong></a></p>

</div>