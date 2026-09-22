---
title: "2026년 9월 Copilot 주요 업데이트"
date: 2026-09-22T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - CopilotStudio
  - CopilotCowork
  - Analytics
  - 신기능
  - 월간코파일럿
excerpt: "9월의 94개 Copilot 업데이트 가운데 조직의 비용과 정책, 사용자 안내에 영향을 주는 변화를 골랐습니다. Copilot Studio 과금, 도메인 제외, 새 모델, Cowork 앱 생성과 가치 측정, 앱 주소 전환, 취소된 로드맵을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 최정우
---

<div class="monthlycopilot-page monthlycopilot-page--agent">
<div class="mc-issue-strip">Monthly Copilot · October 2026 · 월간 코파일럿 10월호 · What's New</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">월간 코파일럿 ｜ 2026년 10월호</div>
  <div class="mc-cover-title">2026년 9월<br/>Copilot 주요 업데이트</div>
  <div class="mc-cover-subtitle">기능보다 먼저 확인해야 할 비용·정책·운영의 변화</div>
</div>

<p>9월 Copilot 업데이트 자료에는 94개의 변화가 담겼습니다. 모두 같은 무게로 읽을 필요는 없습니다. 이번 달에는 특히 <strong>Copilot Studio의 과금 방식</strong>, <strong>도메인 제외 기능의 복귀</strong>, <strong>새 모델에 대한 관리 판단</strong>처럼 조직의 예산과 정책을 바꾸는 소식이 눈에 띕니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>94</strong></div>
    <div>번호가 매겨진 9월 업데이트</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>6</strong></div>
    <div>먼저 볼 핵심 변화</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>2</strong></div>
    <div>취소된 로드맵 항목</div>
  </div>
</div>

<hr/>

<h2 class="mc-section-title">1 · Copilot Studio는 이제 빌드할 때부터 비용이 듭니다</h2>

<p>두 달간의 프리뷰를 거친 <strong>GitHub Copilot harness</strong>가 Copilot Studio에서 정식 출시됐습니다. 긴 시간 동안 여러 단계를 수행하고, 매 단계의 정답이 분명하지 않은 업무를 맡기는 데 초점을 둔 실행 방식입니다.</p>

<p>이번 변화에서 가장 중요한 문장은 기능 설명이 아니라 과금 조건입니다. 새 하네스의 에이전트는 <strong>Microsoft 365 Copilot 라이선스 보유 여부와 관계없이 수행한 모든 작업에 대해 Copilot Credits를 사용</strong>합니다. 더구나 비용은 운영 환경에서 에이전트가 실행될 때만 발생하지 않습니다. 제작자가 빌드하고, 미리 보고, 평가하는 과정에서도 크레딧이 소비됩니다.</p>

<div class="mc-callout mc-callout--dark">
  <p><strong>예산의 시작점이 바뀌었습니다.</strong></p>
  <p>파일럿이 실제 서비스로 출시되지 않더라도 실험 과정에서 비용이 발생할 수 있습니다. 개발·테스트 예산을 운영 예산과 함께 설계해야 합니다.</p>
</div>

<p>Power Platform 관리 센터의 <strong>관리 &gt; Copilot Studio</strong>에서 Harness 열을 확인하면 GitHub Copilot, Standard, Copilot Chat 유형별로 에이전트를 구분할 수 있습니다. 환경별 선불 용량을 배정하고, 소진 시 경고와 실행 차단을 각각 설정하며, 실험적인 에이전트에는 별도의 한도를 두는 운영이 필요합니다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>프로덕션</strong></div>
    <div>경고는 켜고 차단은 업무 연속성을 고려해 결정합니다.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>메이커 샌드박스</strong></div>
    <div>환경·에이전트 한도를 명확히 하고 증액 요청 절차를 함께 안내합니다.</div>
  </div>
</div>

<p><a href="https://techcommunity.microsoft.com/blog/copilot-studio-blog/more-powerful-agents-and-workflows-for-autonomous-business-processes-introducing/4542969">GitHub Copilot harness 발표</a> · <a href="https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/billing-credit-overview">Copilot Credits 과금 개요</a> · <a href="https://learn.microsoft.com/en-us/power-platform/admin/manage-usage-github-copilot-harness">새 하네스 사용량 관리</a></p>

<hr/>

<h2 class="mc-section-title">2 · 도메인 제외 기능이 다시 돌아왔습니다</h2>

<p>7월 28일 발표됐다가 8월 4일 철회됐던 <strong>Domain Exclusion</strong>이 9월 9일 다시 제공됐습니다. 관리자가 외부 도메인을 지정하면 Microsoft Copilot, Copilot Chat, Cowork가 공개 웹 콘텐츠를 근거로 답변할 때 해당 도메인의 콘텐츠를 사용하지 않도록 할 수 있습니다.</p>

<p>오래된 제품 정보를 담은 사이트나 신뢰하기 어려운 콘텐츠가 반복적으로 답변에 섞일 때 사용할 수 있는 통제입니다. 최대 1,000개 도메인을 지정할 수 있지만, 하위 도메인 처리와 웹페이지에 적용되는 범위 등 제한 사항을 먼저 확인해야 합니다.</p>

<div class="mc-callout">
  <p><strong>지금 할 일</strong></p>
  <p>지난달 중단했던 제외 목록 검토를 다시 시작하되, 차단 목록을 늘리는 것보다 제외 이유와 검토 책임자, 재검토 날짜를 함께 기록하세요.</p>
</div>

<p><a href="https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/update-domain-exclusion-for-microsoft-365-copilot/4553126">Microsoft의 Domain Exclusion 업데이트</a></p>

<hr/>

<h2 class="mc-section-title">3 · 모델 선택은 기능보다 계약과 지역부터 봐야 합니다</h2>

<p>9월에는 Copilot Cowork와 Copilot Studio에 <strong>GPT-6 Astra</strong>와 <strong>Claude Fable 5.1</strong>이 추가됐습니다. 두 모델이 Chat이 아니라 작업을 위임하는 Cowork와 Studio에 먼저 들어왔다는 점이 특징입니다. 기존 Fable 5를 기준으로 테스트나 내부 가이드를 만들었다면 Fable 5.1에서 다시 확인해야 합니다.</p>

<p><strong>Grok</strong> 모델도 선택지에 추가됐지만 기본값은 꺼짐입니다. EU, EFTA, 영국과 정부·소버린 클라우드에서는 제공되지 않습니다. 새 하위 처리자가 추가되는 일은 단순한 기능 공개가 아니라 규정 준수 검토의 대상입니다. 켜기 전에 법무·개인정보·보안 담당자가 적용 조건과 데이터 처리 경계를 확인해야 합니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>GPT-6 Astra</strong></div>
    <div>Cowork·Copilot Studio에서 큰 작업을 위임하는 시나리오 중심.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>Claude Fable 5.1</strong></div>
    <div>Fable 5를 대체. 기존 테스트와 정책 문구를 다시 확인.</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>Grok</strong></div>
    <div>기본 비활성화. 지원 지역과 계약 조건을 먼저 검토.</div>
  </div>
</div>

<p><a href="https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/available-today-openai-gpt-6-astra-in-microsoft-copilot/4552808">GPT-6 Astra 발표</a> · <a href="https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/available-today-anthropic-claude-fable-5-1-in-microsoft-copilot/4551974">Claude Fable 5.1 발표</a> · <a href="https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/expanding-model-choice-in-copilot-with-grok/4555749">Grok 모델 선택 안내</a></p>

<hr/>

<h2 class="mc-section-title">4 · Cowork가 앱을 만들고, 사용자는 비용을 확인합니다</h2>

<p>Frontier Program에 <strong>App skill</strong>이 추가됐습니다. 설명만 입력하면 가벼운 대화형 앱을 만들고, 채팅에서 다듬은 뒤 열고 게시해 조직 구성원과 공유할 수 있습니다. 중요한 것은 코드 생성 자체보다 제작부터 배포·공유까지 한 흐름으로 이어진다는 점입니다.</p>

<p>작은 내부 도구 하나로 먼저 검증하는 편이 좋습니다. 어떤 데이터에 접근하는지, 누가 앱을 게시하고 공유할 수 있는지, 앱이 만든 결과를 누가 책임지는지 확인한 뒤 범위를 넓혀야 합니다.</p>

<p>Cowork에는 작업 품질·속도·크레딧 사용량을 조절하는 <strong>Light, Medium, High, Extra High, Max</strong>의 노력 수준도 생겼습니다. 기본값은 Medium입니다. <code>/cost</code> 스킬은 현재 작업의 예상 비용뿐 아니라 월간 크레딧 잔여 비율, 월 누적 사용량, 초기화 날짜를 보여 줍니다.</p>

<p><a href="https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new">Copilot Cowork의 새로운 기능</a></p>

<hr/>

<h2 class="mc-section-title">5 · 프롬프트 수보다 완료한 일의 가치를 봅니다</h2>

<p>Insights의 Consumption Dashboard가 Cowork의 <strong>지원 시간(assisted hours)</strong>과 <strong>지원 가치(assisted value)</strong>를 보여 주기 시작했습니다. 몇 번 프롬프트를 보냈는지보다 Cowork가 사람에게 돌려준 것으로 추정되는 시간을 측정하려는 변화입니다.</p>

<p>이 수치는 재무 확정값이 아니라 의도적으로 보수적으로 계산한 대리지표입니다. 경영 보고에 넣기 전에 추정 방식과 가정을 합의하고, 실제 업무 처리 시간·품질·재작업률 같은 현장 지표와 함께 읽어야 합니다.</p>

<p>Copilot 및 Agent 365 대시보드의 데이터 내보내기도 공개 미리 보기로 제공됩니다. 특히 식별 가능한 데이터 내보내기는 관리자가 켜고 끌 수 있으므로, 분석가가 데이터를 반출하기 전에 익명 데이터라고 가정하지 말고 설정을 확인해야 합니다. Consumption Dashboard에는 GitHub Copilot AI 크레딧 사용 페이지도 추가되어 개발자 도구 소비를 다른 Copilot 지출과 함께 볼 수 있습니다.</p>

<p><a href="https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/measuring-the-value-of-cowork-from-ai-interactions-to-completed-work/4554464">Cowork 가치 측정 안내</a> · <a href="https://learn.microsoft.com/en-us/viva/insights/org-team-insights/export-copilot-metrics">Copilot 메트릭 내보내기</a> · <a href="https://learn.microsoft.com/en-us/viva/insights/org-team-insights/ai-cost-dashboard">Consumption Dashboard</a></p>

<hr/>

<h2 class="mc-section-title">6 · 10월 전에 <code>*.cloud.microsoft</code>를 확인하세요</h2>

<p>Copilot 앱은 개인·업무 계정을 아우르는 하나의 앱 경험으로 정리되고 있습니다. Chat, Pages, Notebooks, Search, 에이전트, Cowork가 한 앱에 모이면서 웹 주소도 바뀝니다.</p>

<p>새 호스트를 차단한 조직은 2026년 10월 초 리디렉션이 시작될 때 사용자가 앱에 접근하지 못할 수 있습니다. 네트워크와 Microsoft 365 관리자는 10월 전에 <code>*.cloud.microsoft</code> 도메인이 허용되어 있는지 확인해야 합니다.</p>

<p><a href="https://learn.microsoft.com/en-us/windows/client-management/deploy-unified-copilot-app">통합 Copilot 앱 배포 안내</a></p>

<hr/>

<h2 class="mc-section-title">계획에서 빼야 할 두 가지</h2>

<div class="mc-card-grid">
  <div class="mc-card mc-card--red">
    <div class="mc-card-title"><strong>모바일 선제 알림</strong></div>
    <div>Copilot 모바일 앱의 'Your Day at a Glance' 선제 푸시 알림 로드맵이 8월 26일 취소됐습니다.</div>
  </div>
  <div class="mc-card mc-card--red">
    <div class="mc-card-title"><strong>Teams 대화형 회의 에이전트</strong></div>
    <div>Teams 회의·통화용 Interactive Agents 로드맵이 8월 17일 취소됐습니다.</div>
  </div>
</div>

<p>둘 다 사용자가 요청하기 전에 에이전트가 먼저 행동하는 기능이었습니다. Microsoft는 취소 이유를 밝히지 않았습니다. 원인을 추측하기보다 관련 파일럿과 사용자 안내, 일정에서 두 항목을 제거하는 것이 먼저입니다.</p>

<p><a href="https://www.microsoft.com/en-us/microsoft-365/roadmap?filters=&amp;searchterms=560339">모바일 선제 알림 로드맵 560339</a> · <a href="https://www.microsoft.com/en-us/microsoft-365/roadmap?filters=&amp;searchterms=490564">Teams 대화형 에이전트 로드맵 490564</a></p>

<hr/>

<h2 class="mc-section-title">이번 달 관리자 체크리스트</h2>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>확인할 일</th><th>담당</th><th>시점</th></tr>
    </thead>
    <tbody>
      <tr><td>누가 Copilot Credits를 쓸 수 있는지 확인</td><td>Power Platform 관리자</td><td>지금</td></tr>
      <tr><td><code>*.cloud.microsoft</code> 도메인 허용 여부 확인</td><td>네트워크·Microsoft 365 관리자</td><td>10월 전</td></tr>
      <tr><td>Grok의 지역·계약·데이터 처리 조건 검토</td><td>Microsoft 365 관리자·법무·보안</td><td>활성화 전</td></tr>
      <tr><td>Domain Exclusion 목록과 운영 책임 재정의</td><td>Microsoft 365 관리자</td><td>지금</td></tr>
      <tr><td>Cowork 지원 시간·가치의 해석 기준 합의</td><td>리더·분석 담당자</td><td>이번 달</td></tr>
      <tr><td>대시보드 내보내기의 식별 가능 설정 확인</td><td>관리자·분석가·개인정보 담당자</td><td>내보내기 전</td></tr>
    </tbody>
  </table>
</div>

<div class="mc-callout mc-callout--dark">
  <p><strong>9월의 핵심은 기능 수가 아니라 운영 책임의 이동입니다.</strong></p>
  <p>에이전트는 제작 단계부터 비용을 만들고, 모델 추가는 법무 검토를 요구하며, 분석 데이터는 내보내기 전에 식별 가능성을 확인해야 합니다. 새 기능을 켜는 사람과 비용·정책을 책임지는 사람이 같은 정보를 보도록 만드는 일이 먼저입니다.</p>
</div>

<hr/>

<h2 class="mc-section-title">더 살펴볼 업데이트</h2>

<ul>
  <li><strong>Copilot Chat</strong> — 웹과 업무 채팅이 하나로 합쳐지고 Work IQ 버튼으로 조직 콘텐츠를 명시적으로 불러옵니다.</li>
  <li><strong>Copilot Notebooks</strong> — Copilot 앱의 가벼운 경험과 OneNote의 전체 작업 공간으로 나뉘고 서로 동기화됩니다.</li>
  <li><strong>PowerPoint</strong> — 승인된 템플릿 고정, 슬라이드 노트 기반 생성, 사용자 정의 스킬이 추가됐습니다.</li>
  <li><strong>Excel</strong> — Copilot 편집 과정에서 Python을 활용하고 변경 내용과 변경자를 설명할 수 있습니다.</li>
  <li><strong>Outlook</strong> — 사용자 지정 엔진 에이전트가 Outlook에서 작동하며 자연어 메일·일정 명령이 확대됐습니다.</li>
  <li><strong>Planner</strong> — Copilot Chat에서 작업을 만들고 조회하며 Planner Agent가 상태 보고서를 작성합니다.</li>
</ul>

<p class="mc-card-note">기능의 정확한 사양과 제공 시점, 라이선스 요건은 연결된 Microsoft 공식 문서를 확인해 주세요. 미리 보기 기능과 출시 일정은 변경될 수 있습니다.</p>

<p><strong>원문 자료</strong> · Susanth Sutheesh, <a href="https://www.aguidetocloud.com/blog/microsoft-365-copilot-september-2026-updates/">What's New in Microsoft 365 Copilot — September 2026</a>. 이 글은 제공된 2026년 9월 업데이트 자료를 바탕으로 국내 독자를 위해 핵심 항목을 선별·요약했습니다.</p>

</div>