---
title: "What's New in Copilot, 쉽게 읽기 — 2026년 11월"
date: 2026-11-26T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - CopilotChat
  - CopilotCowork
  - Teams
  - 월간코파일럿
excerpt: "문서 편집부터 앱 블록, 커넥터 쓰기, Teams 회의 요약까지. Copilot 앱 안에서 일을 이어 가는 11월의 변화 13가지와 출시 일정, 관리자 확인 사항을 정리했습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
---

<div class="monthlycopilot-page monthlycopilot-page--agent">
<div class="mc-issue-strip">Monthly Copilot · November 2026 · 월간 코파일럿 11월호 · What's New</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">What's New in Copilot, 쉽게 읽기 ｜ 2026년 11월</div>
  <div class="mc-cover-title">Copilot 앱 안에서<br/>끝내는 업무</div>
  <div class="mc-cover-subtitle">Office 편집부터 앱 블록, 커넥터, 회의 요약까지</div>
</div>

<img src="{{ '/assets/images/20261126-copilot-november-roundup/01-whats-new-cover.webp' | relative_url }}" alt="What's New in Copilot 문구와 Copilot 로고가 들어간 11월 업데이트 표지" width="1740" height="580" />

<p>Copilot에 보고서 초안을 부탁한 뒤, 앱을 옮기지 않고 바로 문서를 편집할 수 있어요. 출장비 계산기는 대화 안에서 만들어 써 보고, 회의에서 나온 후속 작업은 내용을 확인한 뒤 업무 시스템에 등록할 수 있고요. <strong>11월의 키워드는 ‘한곳에서 끝내기’</strong>입니다.</p>

<div class="mc-callout">
  <p><strong>읽기 전에 · 출시 상태부터 확인하세요</strong></p>
  <ul>
    <li><strong>GA</strong>는 정식 출시, <strong>Public Preview</strong>는 공개 미리 보기, <strong>Frontier</strong>는 참여 조직이 새 기능을 먼저 써 보는 프로그램입니다.</li>
    <li>GA라도 조직의 배포 채널과 설정에 따라 내 화면에 보이는 시점은 다를 수 있어요. 대부분의 기능은 Microsoft 365 Copilot 라이선스가 필요하며, 국내 일정과 한국어 지원 범위도 별도로 확인해 주세요.</li>
    <li>일정은 <strong>2026년 11월 26일 기준</strong>입니다. 조직에서 확인할 설정과 절차는 글 아래 <a href="#admin">관리자 참고</a>에 모았습니다.</li>
  </ul>
</div>

<h2 class="mc-section-title">한눈에 보는 이번 달 소식</h2>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th scope="col">구분</th><th scope="col">소식</th><th scope="col">출시 상태</th></tr>
    </thead>
    <tbody>
      <tr><td>Copilot 앱</td><th scope="row"><a href="#office-in-copilot">1 · 앱 안에서 Office 편집</a></th><td>GA · 11월 중순 배포 완료</td></tr>
      <tr><td>Copilot 앱</td><th scope="row"><a href="#office-agents">2 · Office 에이전트 대신 Chat에 요청</a></th><td>11월 중순~12월 말 순차 전환</td></tr>
      <tr><td>Copilot 앱</td><th scope="row"><a href="#app-blocks">3 · 대화 안에서 앱 블록 사용</a></th><td>GA · Premium과 Basic</td></tr>
      <tr><td>Cowork</td><th scope="row"><a href="#cowork-projects">4 · 프로젝트와 이전 대화로 작업 이어 가기</a></th><td>Cowork에서 사용 가능 · Chat Projects는 11월 예정</td></tr>
      <tr><td>Cowork</td><th scope="row"><a href="#scheduled-prompts">5 · 예약 프롬프트를 Tasks에서 관리</a></th><td>11월 30일~12월 31일 순차 적용</td></tr>
      <tr><td>일하는 방식</td><th scope="row"><a href="#accounting">6 · Excel·Cowork 회계 기능</a></th><td>GA · 11월 13일부터</td></tr>
      <tr><td>일하는 방식</td><th scope="row"><a href="#connector-write">7 · 커넥터로 업무 시스템에 반영</a></th><td>GA · Chat·Cowork</td></tr>
      <tr><td>일하는 방식</td><th scope="row"><a href="#content-sources">8 · 질문마다 답변 근거 선택</a></th><td>GA · 11월 중순</td></tr>
      <tr><td>Teams</td><th scope="row"><a href="#meeting-recap">9 · 전사록 없이 회의 요약 남기기</a></th><td>사용 가능 · 예약된 회의</td></tr>
      <tr><td>Teams</td><th scope="row"><a href="#screen-sharing">10 · 두 발표자가 동시에 화면 공유</a></th><td>12월 초~중순 출시 예정</td></tr>
      <tr><td>에이전트</td><th scope="row"><a href="#insights-agent">11 · Insights Agent V2로 피드백 분석</a></th><td>Frontier</td></tr>
      <tr><td>알림</td><th scope="row"><a href="#chat-limits">12 · 라이선스 없는 Copilot Chat의 사용 제한 확대</a></th><td>11월 9일부터 순차 적용</td></tr>
      <tr><td>알림</td><th scope="row"><a href="#usage-based-access">13 · Cowork·Code·Autopilot 메뉴 기본 표시</a></th><td>2027년 1월 말 예정</td></tr>
    </tbody>
  </table>
</div>

<hr/>

<p class="mc-card-note"><strong>Part 1 · Copilot 앱 안에서 끝내요</strong></p>

<h2 class="mc-section-title" id="office-in-copilot">1 · Office가 Copilot 앱 안으로 들어왔어요</h2>

<p>Chat이나 Cowork에서 문서 초안을 요청하면 대화 옆에 Word·Excel·PowerPoint 파일이 열려요. 후속 프롬프트로 내용을 다듬거나, 익숙한 리본 메뉴로 직접 편집할 수 있습니다. 같은 화면에서 댓글과 공동 편집도 가능해요. <strong>‘Word에서 열기’</strong>처럼 데스크톱 앱으로 넘어가도 같은 파일을 이어서 작업합니다.</p>

<p>새 파일은 내 OneDrive에 저장되고 서식, 댓글, 공유 권한과 버전 기록이 유지됩니다. 일반 배포는 11월 중순까지 완료됐고, 지연 배포(Deferred release) 조직은 12월 초부터 적용될 예정입니다.</p>

<p><a href="https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/introducing-office-in-the-new-microsoft-copilot-app/4561230">Microsoft Copilot Blog · Office in Copilot 소개</a> · <a href="{{ '/copilot/OfficeInCopilot/' | relative_url }}">ModernWork Korea · Office in Copilot 사용 흐름</a></p>

<h2 class="mc-section-title" id="office-agents">2 · Word·Excel·PowerPoint 에이전트 대신 Chat에 직접 요청하세요</h2>

<p>11월 중순부터 12월 말까지 세 에이전트가 왼쪽 메뉴와 에이전트 검색에서 순차적으로 빠집니다. 예전처럼 고정하거나 <code>@Word</code>로 부르지 않아도 돼요. Chat에 “Q4 킥오프 결과를 경영진 브리프로 만들어 줘”라고 요청하면 됩니다.</p>

<p>이미 만든 파일은 원래 OneDrive나 SharePoint 위치에 권한과 보존 정책이 유지된 채 남아요. 이전 에이전트 대화는 열어 볼 수 있지만, 이어서 작업하려면 Chat에서 새 대화를 시작해야 합니다.</p>

<p><a href="{{ '/copilot/CopilotOfficeAgentsTransition/' | relative_url }}">ModernWork Korea · Word·Excel·PowerPoint 에이전트 전환 안내</a></p>

<h2 class="mc-section-title" id="app-blocks">3 · 답변이 바로 쓰는 앱이 돼요: 앱 블록</h2>

<p>계산기, 비교표나 양식이 필요하면 대화에서 원하는 입력과 결과를 설명해 보세요. 앱 블록(App Blocks)은 별도 앱 화면을 열지 않고도 대화 안에서 조작할 수 있어요. 예를 들어 출장 일수나 숙박비를 바꾸면 총액과 차트가 즉시 갱신됩니다. Microsoft 365 Copilot(Premium)과 Copilot Chat(Basic) 모두 대상입니다.</p>

<p><a href="https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes">Microsoft Learn · Microsoft 365 Copilot 릴리스 노트</a></p>

<hr/>

<p class="mc-card-note"><strong>Part 2 · Cowork로 이어서 일해요</strong></p>

<h2 class="mc-section-title" id="cowork-projects">4 · 프로젝트와 이전 대화로 맥락을 이어 가요</h2>

<p>Cowork의 <strong>Projects</strong>에 관련 작업과 대화, 지침을 모으면 매번 보고 대상이나 형식을 설명하지 않아도 돼요. 프로젝트에서 시작한 작업에는 프로젝트 지침이 전체 지침보다 먼저 적용됩니다. <strong>Project context</strong>에서는 관련 파일·회의·채팅을, <strong>Outputs</strong>에서는 결과물을 확인할 수 있어요. 프로젝트는 만든 사람만 볼 수 있고, 등록한 모든 자료가 작업마다 쓰이는 것은 아닙니다.</p>

<p>지난 Chat 대화나 Cowork 작업을 새 요청의 자료로 넣으려면 입력창의 <strong>컨텍스트 추가 → Copilot</strong>에서 고르세요. 예를 들어 Chat에서 조사한 고객 동향을 불러와 Cowork에 제안서 초안을 맡길 수 있습니다. Projects는 Cowork에서 사용할 수 있고, Copilot Chat에는 11월 제공 예정으로 안내됐어요.</p>

<p><a href="https://learn.microsoft.com/en-us/copilot/cowork/cowork-projects">Microsoft Learn · Cowork 프로젝트 사용하기</a></p>

<h2 class="mc-section-title" id="scheduled-prompts">5 · 예약 프롬프트는 이제 Tasks에서 관리해요</h2>

<p>매주 월요일 일정 요약처럼 반복하는 요청은 <strong>Tasks → Scheduled</strong>에서 다음 실행 시각을 확인하고, 즉시 실행하거나 수정·일시 정지·삭제할 수 있어요. Power Automate를 사용하지 않는 조직에서도 Microsoft 365 Copilot 라이선스가 있다면 이용할 수 있습니다. 사용자당 활성 예약은 10개, 전체 예약은 50개까지이고, 승인이 필요한 작업은 대화에서 응답할 때까지 기다립니다.</p>

<div class="mc-callout">
  <p><strong>기존 예약을 확인하세요.</strong> 11월 30일부터 12월 31일까지 순차 전환됩니다. 새 화면이 열리고 30일 동안은 기존 메뉴에서도 볼 수 있지만, Power Platform 기반의 기존 방식은 <strong>12월 31일 종료</strong>됩니다. 자동으로 옮겨지지 않은 예약은 종료 전에 다시 만들어 주세요. 이미 완료된 실행 결과는 유지됩니다.</p>
</div>

<hr/>

<p class="mc-card-note"><strong>Part 3 · 일하는 방식이 달라져요</strong></p>

<h2 class="mc-section-title" id="accounting">6 · Excel과 Cowork에서 계정 대사와 전표 초안을</h2>

<p>재무팀은 <code>@reconciliation</code>으로 잔액과 거래의 차이를 찾고, 조정 항목이나 전표 초안을 준비할 수 있어요. <code>@variance-analysis</code>로 계획 대비 실적과 변동 요인을 살펴보거나, 예산·감사 업무를 지원하는 스킬도 쓸 수 있습니다. Excel에서는 Copilot이 무엇을 왜 바꿨는지 채팅 기록에 남기도록 선택할 수 있고, Cowork의 감사 추적은 지원 예정입니다.</p>

<p>11월 13일부터 정식 출시가 시작돼 Frontier 등록 없이 사용할 수 있지만, Copilot 라이선스는 필요합니다. Copilot은 검토용 초안을 준비하고 <strong>승인과 회계 시스템 반영은 사람이 맡습니다.</strong></p>

<p><a href="https://support.microsoft.com/en-us/excel/copilot/copilot-in-excel-built-in-skills">Microsoft Support · Excel의 기본 제공 스킬</a> · <a href="{{ '/copilot/CopilotAccountingExcelCowork/' | relative_url }}">ModernWork Korea · Excel·Cowork 회계 기능</a></p>

<h2 class="mc-section-title" id="connector-write">7 · 읽기만 하던 커넥터로 업무 시스템에 반영해요</h2>

<p>지원되는 커넥터가 연결돼 있다면 Copilot 안에서 Jira 이슈를 만들거나 Notion 페이지를 갱신할 수 있어요. 쓰기·삭제 도구에는 기본적으로 승인이 필요합니다. 확인 카드에서 대상과 보낼 값을 보고 승인하면 <strong>내 권한 범위에서만</strong> 실행되고, 취소하면 변경되지 않아요. 도구의 승인 설정은 <strong>설정 → Sources</strong>에서 확인할 수 있습니다.</p>

<p>Chat과 Cowork에서 정식 출시됐습니다. Word·Excel·PowerPoint에는 제공 예정이며, Researcher는 읽기 전용입니다.</p>

<p><a href="https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/turn-copilot-insights-into-action-with-connector-write-capabilities/4571160">Microsoft Copilot Blog · 커넥터 쓰기 기능</a></p>

<h2 class="mc-section-title" id="content-sources">8 · 답변 근거는 질문마다 직접 골라요</h2>

<p>Copilot Chat에 “Salesforce 자료만 보고 답해 줘”라고 요청할 때, 콘텐츠 소스 메뉴에서도 해당 출처를 선택해 검색 범위를 좁힐 수 있어요. 켜 둔 소스에서만 답을 찾고 인용을 표시합니다. 이 선택은 <strong>지금 질문에만</strong> 적용되며, 볼 수 있는 자료의 권한은 바뀌지 않아요. 아무것도 고르지 않으면 기존처럼 Copilot이 자료를 찾아요.</p>

<img src="{{ '/assets/images/2026-11-11-CopilotChatContentSourceFilters/image1.png' | relative_url }}" alt="Copilot Chat에서 질문의 근거로 쓸 콘텐츠 소스를 선택하는 메뉴" loading="lazy" />

<p>11월 중순 정식 출시됐으며 Microsoft 365 Copilot 라이선스 사용자에게 기본으로 켜집니다. <a href="https://support.microsoft.com/en-us/microsoft-365-copilot/control-review-sources-copilot-chat">Microsoft Support · Copilot Chat 답변 소스 제어</a> · <a href="{{ '/copilot/CopilotChatContentSourceFilters/' | relative_url }}">ModernWork Korea · 콘텐츠 소스 필터 사용법</a></p>

<hr/>

<p class="mc-card-note"><strong>Part 4 · Teams 회의가 달라져요</strong></p>

<h2 class="mc-section-title" id="meeting-recap">9 · 전사록을 저장하지 않아도 회의 요약을 남겨요</h2>

<p>예약된 Teams 회의에서는 녹화나 전사록을 남기지 않아도 결정 사항, 후속 작업, 하이라이트를 AI 요약으로 확인할 수 있어요. 주최자가 회의 옵션에서 Copilot을 켜 두거나, 주최자·공동 주최자·발표자가 회의 중 <strong>Meeting AI</strong>로 제어할 수 있습니다. 회의 뒤에는 채팅의 <strong>Recap</strong> 탭에서 확인하세요.</p>

<p>전사록을 저장하지 않는다고 해서 아무 기록도 남지 않는 것은 아니에요. <strong>요약은 주최자 OneDrive의 Meetings 폴더에 읽기 전용 Word 문서</strong>로 저장됩니다. 주최자와 열람자 모두 Microsoft 365 Copilot 라이선스가 필요하며, 외부 참석자와 게스트는 이 요약을 볼 수 없어요.</p>

<p><a href="https://learn.microsoft.com/en-us/microsoftteams/intelligent-recap-without-saving-transcripts">Microsoft Learn · 전사록을 저장하지 않는 Teams 회의의 Intelligent Recap</a></p>

<h2 class="mc-section-title" id="screen-sharing">10 · 두 발표자가 동시에 화면을 공유해요</h2>

<p>한 발표자가 공유를 멈출 때까지 기다리지 않아도 두 번째 발표자가 화면을 띄울 수 있어요. 참석자는 두 화면을 나란히 보며 견적서나 발표 자료를 비교할 수 있습니다. 기본으로 켜지지만 주최자가 회의 옵션에서 허용 여부를 바꿀 수 있어요. 데스크톱과 웹에서 12월 초부터 순차 배포해 중순에 완료될 예정입니다.</p>

<hr/>

<p class="mc-card-note"><strong>Part 5 · 에이전트를 만든 분이라면</strong></p>

<h2 class="mc-section-title" id="insights-agent">11 · Insights Agent V2로 에이전트 피드백을 살펴봐요</h2>

<p>에이전트 소유자는 Copilot Chat에서 좋아요·싫어요 수뿐 아니라, 원문 의견과 반복되는 주제를 확인할 수 있어요. “이번 주 [에이전트 이름]의 부정 평가에서 반복된 의견을 보여 줘”라고 물어보고, 요약을 원문과 대조해 보세요. 지침이나 지식 소스를 수정한 뒤 다시 테스트하고 다음 피드백을 확인하는 데 활용할 수 있습니다. 현재는 <strong>Frontier</strong> 대상이며, 관리자가 에이전트 피드백 공유를 허용해야 합니다.</p>

<p><a href="https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/explore-user-feedback-with-microsoft-365-insights-agent/4565981">Microsoft Copilot Blog · Insights Agent 피드백 소개</a> · <a href="https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/insights-agent-quickstart">Microsoft Learn · Insights Agent 시작하기</a></p>

<hr/>

<p class="mc-card-note"><strong>Part 6 · 미리 확인할 변경 사항</strong></p>

<h2 class="mc-section-title" id="chat-limits">12 · 라이선스 없는 Copilot Chat의 사용 제한이 확대돼요</h2>

<p>이미지 생성에 적용되던 공정 사용(fair use) 제한이 11월 9일부터 Copilot Chat의 다른 기능으로 확대됩니다. Microsoft 365 Copilot 라이선스가 없는 웹·데스크톱·모바일 사용자가 대상이에요. 한도에 도달하면 앱에서 언제 다시 사용할 수 있는지 알려 줍니다. 진행 중인 답변은 끊기지 않고, 한도는 하루 중에도 달라질 수 있어요. Microsoft 365 Copilot 라이선스 사용자는 이번 변경 대상이 아닙니다.</p>

<p><a href="https://support.microsoft.com/en-us/microsoft-365-copilot/standard-versus-priority-access-to-features-in-microsoft-365-copilot-chat">Microsoft Support · Copilot Chat 표준 액세스와 우선 액세스</a> · <a href="{{ '/copilot/CopilotChatNovemberLimits/' | relative_url }}">ModernWork Korea · 11월 사용 제한 안내</a></p>

<h2 class="mc-section-title" id="usage-based-access">13 · Cowork·Code·Autopilot 메뉴가 보여도 바로 과금되지는 않아요</h2>

<p>2027년 1월 말부터 Microsoft 365 Copilot 라이선스 사용자에게 세 메뉴가 기본으로 표시될 예정입니다. 조직에서 사용을 허용하지 않았다면 바로 실행되는 대신 안내 화면이 열려요. 회사 설정에 따라 <strong>Request access</strong>로 접근을 요청하거나 사내 안내 페이지를 볼 수 있습니다. <strong>메뉴 표시와 실제 사용은 별개</strong>이며, 사용에는 조직의 지출 정책과 Copilot Credits가 필요합니다.</p>

<p><a href="https://learn.microsoft.com/en-us/copilot/implement/request-access-usage-based-billing-experiences">Microsoft Learn · 사용량 기반 기능에 대한 접근 요청</a></p>

<div class="mc-callout">
  <p><strong>이런 프롬프트부터 써 보세요</strong></p>
  <ul>
    <li>Office: “Q4 킥오프 결과를 1페이지 경영진 브리프로 만들어 줘. 결정 사항, 리스크, 다음 단계를 넣어 줘.”</li>
    <li>앱 블록: “출장 일수, 숙박비, 식비, 교통비를 바꾸면 총 경비와 예산 초과 여부를 바로 보여 주는 계산기를 만들어 줘.”</li>
    <li>예약 프롬프트: “매주 월요일 오전 9시에 이번 주 회의 중 미리 준비해야 할 항목을 정리해 줘.”</li>
  </ul>
</div>

<hr/>

<h2 class="mc-section-title" id="admin">관리자 참고 · 배포 전에 확인할 것</h2>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th scope="col">항목</th><th scope="col">확인할 일</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">Office·앱 블록</th><td>Office in Copilot에는 기존 Copilot 정책과 민감도 레이블이 적용됩니다. 에이전트 전환에 맞춰 가이드와 헬프데스크의 시작 경로를 Chat으로 바꾸세요.</td></tr>
      <tr><th scope="row">콘텐츠 소스·커넥터</th><td>커넥터 이름과 검색 권한, 읽기·쓰기·삭제 도구, 게시자 유형과 허용 사용자 범위를 점검하세요.</td></tr>
      <tr><th scope="row">예약 프롬프트</th><td>11월 30일~12월 31일 전환을 알리고, 자동 이전되지 않은 예약은 12월 31일 전에 다시 만들도록 안내하세요.</td></tr>
      <tr><th scope="row">Excel·Cowork 회계</th><td>타사 회계 커넥터에는 별도 라이선스나 관리자 활성화가 필요할 수 있습니다.</td></tr>
      <tr><th scope="row">Insights Agent 피드백</th><td>관리 센터의 <strong>Agents → Settings → Agent feedback sharing</strong>을 확인하세요.</td></tr>
      <tr><th scope="row">Teams 동시 화면 공유</th><td>12월 배포 전에 테넌트의 화면 공유 정책과 회의별 기본 동작을 점검하세요.</td></tr>
      <tr><th scope="row">라이선스 없는 Copilot Chat</th><td>관리자가 개별 한도를 조회하거나 조정할 수는 없습니다. 한도 안내와 사내 라이선스 신청 절차를 헬프데스크에 공유하세요.</td></tr>
    </tbody>
  </table>
</div>

<h3>Copilot Search에서 공식 자료를 먼저 보여 주세요</h3>

<p>Microsoft 365 관리 센터의 <strong>Copilot → Search → Authoritative content</strong>에서 공식 출처로 지정한 SharePoint 사이트는 검색 결과에서 우선 고려됩니다. 문서가 아닌 사이트 단위로 최대 100개를 지정할 수 있어요. 출장비나 보안 지침처럼 최신본이 중요한 규정부터 지정하고, 자주 묻는 검색어로 결과가 어떻게 바뀌는지 확인해 보세요. 사용자가 <a href="#content-sources">질문마다 답변 소스를 고르는 기능</a>과는 별개입니다.</p>

<h3>Teams의 AI 사용 정책과 전사 정책을 따로 확인하세요</h3>

<p><strong>Meeting AI</strong>는 Copilot·Facilitator·Intelligent Recap 같은 기능의 사용 여부를, <strong>Transcription With Meeting AI</strong>는 AI를 켤 때 전사도 시작할지를 정합니다. 전사 자체의 허용 여부를 정하는 기존 <strong>Transcription</strong> 정책은 그대로예요. 기존 Copilot 정책은 자동으로 매핑되므로 새로 만들 필요는 없지만, PowerShell과 자동화 스크립트는 새 설정으로 바꿔 주세요. 대상 지정 릴리스는 12월 초, 일반 배포는 2027년 1월 초로 안내됐습니다.</p>

<p>전사록 없는 요약에 별도 정책은 없습니다. 회의 정책에서 <code>-AllowIntelligentRecap $false</code>를 적용하면 전사 여부와 관계없이 요약이 꺼져요. 요약 문서는 기본 120일 뒤 만료되며 <code>-IntelligentRecapDocxFileExpirationDays</code>로 1~9,999일 또는 만료 없음(<code>-1</code>)을 설정할 수 있습니다. 요약 생성에 쓰인 임시 데이터는 하루 안에 삭제되며, 저장된 문서는 eDiscovery와 법적 보존의 대상이 될 수 있어요.</p>

<p><a href="{{ '/copilot/TeamsMeetingAIControls/' | relative_url }}">ModernWork Korea · Teams 회의 AI 정책 변경</a> · <a href="https://learn.microsoft.com/en-us/microsoftteams/intelligent-recap-calls-meetings">Microsoft Learn · Teams Intelligent Recap 관리</a></p>

<h3>1월 말 전에 사용량 기반 기능의 접근 요청 범위를 정하세요</h3>

<p>전역 관리자는 Microsoft 365 관리 센터의 <strong>Copilot → Settings → Access requests to usage-based billing experiences</strong>에서 모든 사용자(기본값), 특정 사용자·그룹, 또는 아무도 요청할 수 없도록 설정할 수 있어요. 12월 중순에는 사내 안내 URL 옵션이 추가될 예정입니다. 메뉴와 새 설정은 2027년 1월 말부터 적용되며 지연 배포 조직은 2월 말 예정입니다. 요청을 검토할 담당자를 정하고, 사내 안내 페이지와 지출 정책, Copilot Credits를 미리 점검해 주세요.</p>

<div class="mc-callout mc-callout--dark">
  <p><strong>이번 호 한 줄 요약</strong></p>
  <p>문서는 Copilot 앱에서 완성하고, 하던 일은 프로젝트로 이어 가세요. 답변의 근거는 직접 좁히고, 업무 시스템에 반영하기 전에는 바뀔 값을 확인하세요.</p>
</div>

<p class="mc-card-note">기능 제공 일정과 범위는 바뀔 수 있습니다. 최신 정보는 <a href="https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes">Microsoft 365 Copilot 릴리스 노트</a>와 Microsoft 365 관리 센터의 메시지 센터에서 확인하세요.</p>
</div>
