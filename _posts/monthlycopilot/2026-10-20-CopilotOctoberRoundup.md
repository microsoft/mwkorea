---
title: "What's New in Copilot, 쉽게 읽기 — 2026년 10월"
date: 2026-10-20T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - CopilotNotebooks
  - Skills
  - Planner
  - Teams
  - 개인화
  - 월간코파일럿
excerpt: "묻는 AI에서 일을 맡기는 AI로. 새 Copilot 발표부터 Notebooks, 스킬, Planner 보고서, 예약 실행, 개인화와 보안까지 9·10월의 주요 소식 11가지를 쉽게 정리했습니다. 출시 상태와 관리자 확인 사항도 함께 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 최정우
---

<div class="monthlycopilot-page monthlycopilot-page--agent">
<div class="mc-issue-strip">Monthly Copilot · November 2026 · 월간 코파일럿 11월호 · What's New</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">What's New in Copilot, 쉽게 읽기 ｜ 2026년 10월</div>
  <div class="mc-cover-title">묻는 AI에서<br/>일을 맡기는 AI로</div>
  <div class="mc-cover-subtitle">새 Copilot부터 스킬, 개인화, 보안까지 · 9·10월 주요 소식 11가지</div>
</div>

<img src="{{ '/assets/images/20261020-copilot-october-roundup/01-whats-new-cover.webp' | relative_url }}" alt="Copilot 로고와 업무 도구 아이콘을 배치한 What's New in Copilot 표지 일러스트" width="1740" height="580" />

<p>Copilot에게 질문하고 답을 받는 것에서 한 걸음 더 나아가, 이제는 일을 맡기고 결과물을 완성하는 방향으로 변화가 이어지고 있습니다. 반복하던 지침은 스킬로 저장하고, 프로젝트 작업 목록은 보고서로 정리하며, 정해진 시간에 에이전트가 실행되도록 예약하는 식입니다.</p>

<p>이번 11월호에서는 <strong>9월 25일 ‘새 Copilot’ 발표부터 10월의 주요 업데이트까지</strong> 한 번에 살펴봅니다. 새 기능이 무엇인지뿐 아니라, 지금 사용할 수 있는지와 사용자가 직접 확인할 사항도 함께 정리했습니다.</p>

<div class="mc-callout">
  <p><strong>읽기 전에 · 출시 상태부터 확인하세요</strong></p>
  <ul>
    <li><strong>GA</strong>는 정식 출시, <strong>Public Preview</strong>는 공개 미리 보기입니다. GA라도 조직·사용자별로 보이는 시점은 다를 수 있습니다.</li>
    <li><strong>Frontier</strong>는 참여 조건을 갖춘 조직이 새 기능을 먼저 사용해 보는 프로그램입니다. <strong>Private Preview</strong>는 제한된 참여자를 대상으로 합니다.</li>
    <li><strong>출시 예정</strong>은 아직 제공을 기다려야 하는 기능입니다. 아래 일정은 <strong>2026년 10월 20일 기준</strong>이며 변경될 수 있습니다.</li>
    <li>대부분의 기능은 Microsoft 365 Copilot 라이선스와 조직 설정을 확인해야 합니다. 무료 Copilot Chat에서는 보이지 않을 수 있습니다.</li>
  </ul>
</div>

<h2 class="mc-section-title">한눈에 보는 이번 달 소식</h2>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th scope="col">소식</th><th scope="col">핵심 변화</th><th scope="col">출시 상태</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row"><a href="#new-copilot">1 · 새 Copilot</a></th><td>Home·Code·Autopilot 발표</td><td>Frontier·Private Preview부터 순차 제공</td></tr>
      <tr><th scope="row"><a href="#notebooks">2 · Notebooks</a></th><td>자료 수집부터 결과물 완성까지</td><td>일부 GA, 일부 Frontier·출시 예정</td></tr>
      <tr><th scope="row"><a href="#skills">3 · 스킬</a></th><td>반복 지침과 편집 작업 재사용</td><td>Chat·PowerPoint GA 순차 배포, Agent Builder Frontier</td></tr>
      <tr><th scope="row"><a href="#planner">4 · Planner 보고서</a></th><td>작업 목록을 상태 보고서로 정리</td><td>Public Preview → 10월 말부터 GA 예정</td></tr>
      <tr><th scope="row"><a href="#scheduled-agents">5 · 예약 실행</a></th><td>내 에이전트를 정해진 시간에 실행</td><td>10월 말부터 순차 배포 예정</td></tr>
      <tr><th scope="row"><a href="#teams-recap">6 · Teams 회의 요약</a></th><td>회의 후 요약을 원하는 언어로 보기</td><td>GA</td></tr>
      <tr><th scope="row"><a href="#work-insights">7 · 업무 맥락 개인화</a></th><td>메일·회의·문서의 업무 맥락 활용</td><td>GA 순차 배포</td></tr>
      <tr><th scope="row"><a href="#memory-sources">8 · 메모리 출처</a></th><td>답변에 쓰인 개인화 정보 확인</td><td>GA · 웹</td></tr>
      <tr><th scope="row"><a href="#security-storage">9 · 보안과 저장 위치</a></th><td>DLP 보호와 새 결과물의 OneDrive 저장</td><td>일부 GA·순차 적용, 일부 보호 기능 Preview</td></tr>
      <tr><th scope="row"><a href="#copilot-address">10 · 웹 주소 변경</a></th><td>copilot.cloud.microsoft로 전환</td><td>자동 전환 진행</td></tr>
      <tr><th scope="row"><a href="#environment-retirement">11 · 환경 종료 안내</a></th><td>관리되지 않는 개발자 환경·Dataverse for Teams 전환 준비</td><td>11월 15일부터 신규 생성 중단</td></tr>
    </tbody>
  </table>
</div>

<hr/>

<p class="mc-card-note"><strong>Part 1 · 새 Copilot</strong></p>

<h2 class="mc-section-title" id="new-copilot">1 · Copilot, ‘일을 맡기는 AI’로</h2>

<p>9월 25일 Microsoft가 발표한 새 Copilot의 방향은 <strong>묻고(Chat), 맡기고(Cowork), 만들고(Code), 자동화하는(Autopilot)</strong> 경험을 연결하는 것입니다. 사용자가 도구를 일일이 옮겨 다니기보다, 원하는 일에 맞는 방식으로 작업을 이어 가도록 하는 데 초점이 있습니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>Home · 한곳에서 시작</strong></div>
    <div>Chat과 Cowork를 하나의 입력창에서 오가고, Copilot 앱 안에서 Word·Excel·PowerPoint 파일을 만들고 편집하며 동료와 함께 작업하는 출발점입니다.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>Code · 말로 설명해 만들기</strong></div>
    <div>“지역별 영업 현황 대시보드를 만들어 줘”처럼 요청해 앱, 트래커, 대시보드를 만드는 경험입니다. 만든 결과물은 팀과 공유할 수 있습니다.</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>Autopilot · 이어서 일하는 팀원</strong></div>
    <div>이름·역할·목표와 경계를 정해 주면 후속 조치와 반복 업무를 이어 가는 디지털 팀원입니다. Teams와 Outlook에서 동료처럼 @멘션할 수 있습니다.</div>
  </div>
</div>

<img src="{{ '/assets/images/20261020-copilot-october-roundup/02-copilot-home.webp' | relative_url }}" alt="하나의 요청 입력창에서 Chat과 Cowork를 선택하는 새 Copilot Home의 참고 화면" width="1190" height="659" loading="lazy" />

<p><strong>“아직 내 화면에 없는데요?”</strong> 모든 기능이 한꺼번에 정식 출시된 것은 아닙니다. Home은 Frontier 순차 제공 예정으로, Code는 9월 말부터 Frontier로 안내됐고, Autopilot은 9월 말 Private Preview 확대 단계입니다. 국내 제공 일정과 한국어 지원도 별도로 확인해야 합니다.</p>

<p>모델 선택에서는 <strong>Auto</strong>가 요청마다 정확도·속도·비용을 고려해 적합한 모델로 연결합니다. 다만 Cowork·Code·Autopilot 같은 작업 위임 경험은 사용량 기반 과금과 조직의 지출 정책을 함께 확인해야 합니다. 새로운 이름이 보인다고 모두 기존 정액 라이선스 안에서 제한 없이 사용할 수 있다고 생각하지 마세요.</p>

<p><a href="https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/">Microsoft — 새 Copilot의 Home·Code·Autopilot 발표</a></p>

<hr/>

<p class="mc-card-note"><strong>Part 2 · 일하는 방식이 달라집니다</strong></p>

<h2 class="mc-section-title" id="notebooks">2 · Notebooks, 자료를 모으는 공간에서 일을 끝내는 공간으로</h2>

<p>Copilot Notebooks는 관련 자료를 모아 질문하는 공간에서, <strong>작업을 맡기고 결과물까지 완성하는 공간</strong>으로 확장됩니다. 텍스트(TXT)와 Markdown 파일을 참고 자료로 넣는 기능부터, 노트북 안에서 문서를 편집하거나 반복 작업을 예약하는 경험까지 포함됩니다.</p>

<img src="{{ '/assets/images/20261020-copilot-october-roundup/03-notebooks.webp' | relative_url }}" alt="프로젝트 목표와 참고 자료, 추천 작업을 함께 보여 주는 Copilot Notebooks의 참고 화면" width="975" height="577" loading="lazy" />

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th scope="col">할 수 있는 일</th><th scope="col">상태</th></tr>
    </thead>
    <tbody>
      <tr><td>참고 자료 형식 확대, 결과물 추천</td><td>GA</td></tr>
      <tr><td>간단한 작업 맡기기, Word·Excel·PowerPoint 편집, 인터랙티브 보고서·PDF 생성</td><td>Frontier</td></tr>
      <tr><td>대화로 노트북 만들기, 반복 작업 예약, 오디오 개요 개선</td><td>출시 예정 · 원문 기준 향후 몇 주 내</td></tr>
    </tbody>
  </table>
</div>

<p>예를 들어 “지난주 프로젝트 자료를 찾아 추가해 줘”, “이 자료로 보고서 파일을 만들어 줘”처럼 요청하는 방식입니다. 다만 위 기능들은 출시 단계가 서로 다릅니다. <strong>Notebooks를 사용할 수 있다고 모든 새 작업 기능이 함께 켜진 것은 아닙니다.</strong></p>

<div class="mc-callout">
  <p><strong>반복 작업 예약이 제공되면 이렇게 요청해 보세요</strong></p>
  <p>“매주 금요일 오후 4시에 [주제]의 한 주 활동을 요약해서 주간 현황 PowerPoint로 만들어 줘.”</p>
</div>

<p><a href="https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/whats-new-in-notebooks--october-2026/4559105">Microsoft Copilot Blog — 10월 Notebooks 업데이트</a> · <a href="https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-microsoft-365-copilot-notebooks">Microsoft Support — Copilot Notebooks 시작하기</a></p>

<h2 class="mc-section-title" id="skills">3 · 매번 쓰던 지침, 이제 스킬로 정리하세요</h2>

<p>“이번에도 같은 보고서 양식으로”, “우리 팀 작성 원칙에 맞춰”라는 말을 반복하고 있다면 <strong>스킬(Skill)</strong>을 살펴보세요. 자주 쓰는 업무 지침을 저장해 다시 사용하는 방식이 Chat, PowerPoint, 에이전트로 넓어집니다.</p>

<h3>Copilot Chat · 지침을 재사용하기</h3>

<p>10월부터 GA 순차 배포되는 Chat 스킬은 요청과 관련 있는 지침을 적용하도록 돕습니다. 자동 적용을 끄고 <strong>Agents and Skills</strong> 메뉴에서 직접 선택할 수도 있습니다. 스킬을 만들고 편집해 동료와 공유하거나 회사에서 배포한 스킬을 사용할 수 있으며, Chat에서 만든 스킬은 Cowork에서도 활용할 수 있습니다.</p>

<h3>PowerPoint · 한 번 해 본 편집을 기록하기</h3>

<p>표 정리, 차트 스타일, 로고 배치 같은 반복 편집은 <strong>Record Skill</strong>로 기록할 수 있습니다. 작업을 한 번 수행하면 Copilot이 스킬 지침 초안을 만들고, 검토·저장한 뒤에는 메뉴나 <code>@스킬이름</code>으로 다시 부릅니다.</p>

<img src="{{ '/assets/images/20261020-copilot-october-roundup/04-record-skill.webp' | relative_url }}" alt="PowerPoint에서 장표 변경을 기록 중이며 Stop 버튼이 표시된 Copilot 스킬 기록 참고 화면" width="551" height="413" style="max-width:551px;" loading="lazy" />

<p>시작 경로는 <strong>+ → Choose skills → Manage plugins &amp; skills → Custom skills → Add skill → Record Skill</strong>입니다. 기록은 <strong>10분 미만</strong>으로 하고, 원하는 변경이 실제 장표에 반영된 뒤 멈추세요. 자세한 활용법과 예시는 이번 호의 <a href="{{ '/monthlycopilot/CopilotSkillsPowerPoint/' | relative_url }}">‘PowerPoint에서 회사 서식, 스킬로 한 번에 맞추기’</a>에서 이어집니다.</p>

<h3>Agent Builder · 에이전트에도 업무 절차를</h3>

<p>Agent Builder로 만든 에이전트에도 업무 절차를 담은 스킬을 붙일 수 있습니다. 이 기능은 <strong>Frontier 참여 조직 대상</strong>입니다. Chat이나 PowerPoint의 스킬과 출시 단계가 같다고 생각하지 않는 것이 좋습니다.</p>

<img src="{{ '/assets/images/20261020-copilot-october-roundup/05-agent-builder-skills.webp' | relative_url }}" alt="Agent Builder의 릴리스 노트 에이전트에 스킬을 추가한 참고 화면" width="845" height="705" loading="lazy" />

<p><a href="https://support.microsoft.com/en-us/powerpoint/copilot/record-skill-copilot-powerpoint">Microsoft Support — PowerPoint 스킬 기록</a> · <a href="https://support.microsoft.com/en-us/powerpoint/copilot/copilot-in-powerpoint-skills">PowerPoint 스킬 사용</a> · <a href="https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills">Microsoft Learn — Agent Builder에 스킬 추가</a></p>

<h2 class="mc-section-title" id="planner">4 · Planner 에이전트, 작업 목록을 보고서로</h2>

<p>Planner에 쌓인 작업, 담당자, 마감일, 진행 상태를 모아 <strong>상태 보고서</strong>를 만들 수 있습니다. 완료한 일뿐 아니라 위험 요인과 다음 단계까지 정리해, 작업 목록을 다시 보고서로 옮겨 적는 수고를 줄이는 기능입니다.</p>

<img src="{{ '/assets/images/20261020-copilot-october-roundup/06-planner-report.webp' | relative_url }}" alt="프로젝트 진행 상황과 위험 요인, 작업 현황 차트를 담은 Planner 에이전트 상태 보고서 예시" width="930" height="910" loading="lazy" />

<p>보고 기간, 포함할 항목, 추가 지침, 길이 등을 조절할 수 있습니다. 생성한 보고서는 검토·편집하고 링크나 Loop 구성 요소로 공유할 수 있습니다. 보고서 생성 자체가 원래 플랜의 작업을 변경하는 것은 아닙니다.</p>

<div class="mc-callout">
  <p><strong>시작 전 확인할 조건</strong></p>
  <ul>
    <li>Microsoft 365 그룹과 공유된 기본 또는 프리미엄 플랜이어야 하며, Planner Agent가 활성화돼 있어야 합니다.</li>
    <li>플랜에 <strong>작업이 10개 이상</strong> 있어야 합니다.</li>
    <li>보고서 생성자는 <strong>Microsoft 365 Copilot 라이선스</strong>가 필요합니다. 라이선스가 없는 사용자도 접근 권한이 있으면 생성된 보고서를 보고 편집할 수 있습니다.</li>
  </ul>
</div>

<p><strong>출시 상태:</strong> Public Preview에서 GA로 전환되며, 원문 기준 10월 말부터 순차 배포해 11월 중순 완료 예정입니다.</p>

<p><a href="https://support.microsoft.com/en-us/planner/copilot/generate-automatic-status-reports-with-planner-agent">Microsoft Support — Planner Agent로 상태 보고서 만들기</a></p>

<h2 class="mc-section-title" id="scheduled-agents">5 · 내가 만든 에이전트, 정해진 시간에 실행</h2>

<p>Agent Builder로 만든 에이전트에 <strong>요청 내용과 실행 시간</strong>을 정해 두면, 매번 대화를 시작하지 않아도 정기적으로 실행할 수 있게 됩니다. “매주 금요일 오후 1시 30분에 프로젝트 현황 정리”처럼 반복되는 요청에 활용하는 방식입니다.</p>

<img src="{{ '/assets/images/20261020-copilot-october-roundup/07-scheduled-workflow.webp' | relative_url }}" alt="에이전트의 요청 내용과 반복 실행 일정을 입력하는 Create a workflow 참고 화면" width="1536" height="1024" loading="lazy" />

<ul>
  <li><strong>설정 위치:</strong> Agent Builder 편집 화면 오른쪽 위 메뉴 → ‘이 에이전트에 대한 워크플로 만들기’</li>
  <li><strong>주기:</strong> 매시간·매일·매주·매월·매년 가운데 선택하고 날짜와 시간을 지정</li>
  <li><strong>실행 대상:</strong> 게시된 에이전트에서 실행하며, 예약은 수정하거나 끌 수 있음</li>
</ul>

<p>여기서 기억할 점은 <strong>예약은 나만의 설정</strong>이라는 것입니다. 에이전트를 동료에게 공유해도 예약까지 함께 공유되지는 않습니다. 동료가 같은 주기로 실행하려면 자신의 예약을 따로 만들어야 합니다.</p>

<p><strong>출시 상태:</strong> 원문 기준 10월 말부터 순차 배포, 11월 완료 예정입니다. 예약을 설정한다고 기존 데이터 접근 권한이 확대되는 것은 아닙니다.</p>

<p><a href="https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder">Microsoft Learn — Agent Builder 개요</a></p>

<h2 class="mc-section-title" id="teams-recap">6 · Teams 회의 요약, 원하는 언어로 다시 보기</h2>

<p>글로벌 회의에서 사용한 언어와 내가 편하게 읽는 언어가 다를 때가 있습니다. 이제 회의가 끝난 뒤 <strong>요약(Recap)을 원하는 언어로 바꿔 보는 경험</strong>이 제공됩니다.</p>

<p>회의 중 번역 자막이나 통역에서 선택한 언어로 요약이 먼저 표시되고, 이후 다른 언어로 바꿀 수 있습니다. 같은 회의에 참석했더라도 각자 편한 언어로 확인할 수 있으며, <strong>원본 녹음이나 대본 자체가 바뀌는 것은 아닙니다.</strong></p>

<img src="{{ '/assets/images/20261020-copilot-october-roundup/08-teams-recap.webp' | relative_url }}" alt="Teams 회의 요약의 언어 메뉴에서 표시 언어를 선택하는 참고 화면" width="390" height="245" style="max-width:390px;" loading="lazy" />

<p><strong>출시 상태:</strong> 원문은 10월 초 GA 배포 완료로 안내하며 Windows·Mac·웹·모바일을 지원합니다. 실제 표시 여부와 언어 선택지는 조직 및 사용 환경에서 확인하세요.</p>

<p><a href="https://support.microsoft.com/en-us/teams/meetings/multilingual-speech-recognition-in-microsoft-teams">Microsoft Support — Teams의 다국어 음성 인식</a></p>

<hr/>

<p class="mc-card-note"><strong>Part 3 · 나를 아는 Copilot, 제어는 내가</strong></p>

<h2 class="mc-section-title" id="work-insights">7 · Copilot이 내 업무 맥락을 이해합니다</h2>

<p>새 채팅을 열 때마다 담당 업무와 관심 프로젝트를 다시 설명했다면, <strong>작업 인사이트(Work insights)</strong>를 살펴보세요. Copilot이 메일, Teams 대화, 회의 대본 등 Microsoft 365 업무 콘텐츠에서 파악한 맥락을 활용해 더 개인화된 답변을 제공하는 기능입니다.</p>

<p>내가 접근할 수 있는 업무 데이터와 조직의 정책 범위 안에서 작동합니다. 내게 맞춰 주는 편리함만큼, <strong>어떤 정보를 개인화에 활용할지 내가 제어할 수 있다는 점</strong>도 중요합니다.</p>

<ul>
  <li><strong>전체 사용 제어:</strong> 설정 → 개인 설정 → ‘채팅 기록 및 작업 인사이트’ 토글을 확인합니다.</li>
  <li><strong>끄면:</strong> 이 기능이 이전 대화와 업무 콘텐츠에서 파악한 개인화용 메모리가 삭제됩니다. 원본 메일이나 문서를 삭제하는 기능은 아닙니다.</li>
  <li><strong>30일 안에 다시 켜면:</strong> 해당 개인화용 메모리가 복원됩니다.</li>
  <li><strong>특정 내용만 제외:</strong> 채팅에서 “이 정보는 개인화에 쓰지 마”라고 요청할 수 있습니다.</li>
</ul>

<p><strong>출시 상태:</strong> 10월 GA 순차 배포로 안내됐습니다. 조직 단위 제어와 제공 플랜에 따라 사용 가능 여부가 달라질 수 있습니다.</p>

<p><a href="https://support.microsoft.com/en-us/microsoft-365-copilot/personalize-what-microsoft-365-copilot-remembers">Microsoft Support — Copilot이 기억하는 내용 개인화하기</a></p>

<h2 class="mc-section-title" id="memory-sources">8 · 이 답변은 왜 이렇게 나왔을까? 메모리 출처 확인</h2>

<p>보고서를 부탁했는데 답이 너무 짧다면, 예전에 저장해 둔 “항상 짧게 요약해 줘”라는 지침이 영향을 주었을 수 있습니다. 메모리 출처 표시는 <strong>답변에 어떤 개인화 정보가 쓰였는지 확인하는 기능</strong>입니다.</p>

<p>답변 아래 <strong>출처 → 개인 설정</strong> 탭에서 사용자 지정 지침, 저장된 메모리, 대화에서 학습한 메모리, 답변에 영향을 준 이전 채팅을 살펴봅니다. 불필요한 메모리는 검토하고 삭제할 수 있습니다. 메모리 기능이 켜져 있을 때 표시되며, 원문은 <strong>10월 GA·웹 제공</strong>으로 안내합니다.</p>

<div class="mc-callout">
  <p><strong>답이 기대와 다르면, 프롬프트뿐 아니라 개인화도 확인하세요.</strong></p>
  <p>새 요청과 과거의 작성 지침이 충돌하고 있지는 않은지 살펴보는 것이 좋습니다. 메모리 출처를 확인하는 것은 답변 내용의 사실 검증과는 별개의 점검입니다.</p>
</div>

<p><a href="https://support.microsoft.com/en-us/microsoft-365-copilot/control-review-sources-copilot-chat">Microsoft Support — Copilot Chat 답변의 출처 제어와 검토</a></p>

<hr/>

<p class="mc-card-note"><strong>Part 4 · 보안과 운영 알림</strong></p>

<h2 class="mc-section-title" id="security-storage">9 · 회사 보안 정책과 결과물 저장 위치도 확인하세요</h2>

<p>Microsoft Purview DLP는 Copilot, Copilot Chat, Cowork에서 민감한 정보를 다루는 방식을 제어할 수 있습니다. 조직이 구성한 정책에 따라 민감도 레이블이 있는 파일·메일을 답변 근거에서 제외하거나, 민감한 정보가 담긴 요청에서 <strong>외부 웹 검색을 제한하고 허용된 내부 자료로만 답하도록</strong> 할 수 있습니다.</p>

<p>프롬프트 처리 자체를 제한하는 기능과 외부 메일을 답변 근거에서 제외하는 기능은 <strong>Preview</strong>입니다. 모든 보호 기능이 같은 출시 단계이거나, 별도 정책 구성 없이 자동으로 적용된다고 이해하지 마세요. 제한 안내가 보이면 조직의 정책과 적용 범위를 IT 담당자에게 확인하는 것이 좋습니다.</p>

<p>저장 위치에도 변화가 있습니다. <strong>10월 중순부터 새로 만드는 Copilot Pages와 Notebooks는 내 OneDrive에 저장</strong>되는 방식으로 순차 전환됩니다. 다른 업무 파일과 함께 확인하고 OneDrive의 관련 정책을 적용할 수 있습니다. <strong>이미 만든 Pages는 기존 위치에 남습니다.</strong></p>

<p><a href="https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about">Microsoft Learn — Microsoft 365 Copilot 및 Cowork용 Purview DLP</a></p>

<h2 class="mc-section-title" id="copilot-address">10 · Copilot 웹 주소가 바뀝니다</h2>

<p>Copilot 웹 주소가 <code>m365.cloud.microsoft</code>에서 <strong><a href="https://copilot.cloud.microsoft/">copilot.cloud.microsoft</a></strong>로 바뀌고 있습니다. 기존 주소로 접속해도 새 주소로 자동 연결되므로, 일반 사용자는 즐겨찾기와 내부 안내 링크를 갱신하면 됩니다.</p>

<p>회사 네트워크에서 접속 문제가 있다면 사내 IT 담당자에게 확인하세요. 관리자는 <code>*.cloud.microsoft</code> 도메인 허용 여부와 연결 상태를 점검할 필요가 있습니다. 원문은 남은 사용자 전환을 <strong>11월 초</strong>로 안내합니다.</p>

<p><a href="https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-app-overview">Microsoft Learn — Microsoft Copilot 앱 개요</a></p>

<h2 class="mc-section-title" id="environment-retirement">11 · 개발자 환경을 쓰는 메이커라면 전환 일정을 확인하세요</h2>

<p>Power Apps·Power Automate·에이전트를 만들어 쓰는 분은 <strong>관리되지 않는 개발자 환경</strong>과 <strong>Dataverse for Teams 환경</strong>의 종료 일정을 확인해야 합니다. 모든 Power Platform 환경이나 Teams 자체가 종료되는 것은 아닙니다.</p>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th scope="col">대상</th><th scope="col">신규 생성 중단</th><th scope="col">기존 환경 일정</th><th scope="col">필요한 준비</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">관리되지 않는 개발자 환경</th><td>2026년 11월 15일</td><td>2026년 12월 15일부터 중지, 2027년 1월 15일부터 삭제</td><td>중지 전에 관리형 환경으로 전환하거나 지원되는 환경으로 솔루션 이전</td></tr>
      <tr><th scope="row">Dataverse for Teams 환경</th><td>2026년 11월 15일</td><td>미전환 환경은 2027년 9월 15일 중지, 10월 30일 폐기</td><td>업무 중단을 피하도록 중지 전에 Dataverse 업그레이드 계획 수립</td></tr>
    </tbody>
  </table>
</div>

<p>이미 관리형인 개발자 환경과 프로덕션·샌드박스·평가판·기본 환경은 이 개발자 환경 종료 대상이 아닙니다. Dataverse for Teams 종료도 해당 환경의 앱·흐름·에이전트·데이터에 관한 것이며, <strong>Teams의 팀·채널·채팅·파일 자체에는 영향을 주지 않습니다.</strong></p>

<p>앱이나 흐름을 직접 이전하기 전에 IT 담당자와 사용 중인 환경을 확인하세요. 관리형 전환과 Dataverse 업그레이드에는 <strong>라이선스 및 용량 검토</strong>가 필요합니다. ‘개발자 환경이니 무료로 계속 쓸 수 있다’고 가정하지 않는 것이 좋습니다.</p>

<p><a href="https://learn.microsoft.com/en-us/power-platform/important-changes-coming#deprecation-of-unmanaged-developer-environments-and-the-power-apps-developer-plan">Microsoft Learn — 관리되지 않는 개발자 환경 종료</a> · <a href="https://learn.microsoft.com/en-us/power-platform/important-changes-coming#deprecation-of-microsoft-dataverse-for-teams-environments">Dataverse for Teams 환경 종료</a> · <a href="https://learn.microsoft.com/en-us/power-platform/admin/managed-environment-overview">관리형 환경 개요</a></p>

<hr/>

<h2 class="mc-section-title">관리자 참고 · 일정과 설정을 따로 모았습니다</h2>

<p>아래 배포 일정과 메시지 센터 번호는 제공된 10월 20일자 원문 기준입니다. 실제 테넌트 적용 일정과 후속 변경은 Microsoft 365 관리 센터의 해당 공지에서 다시 확인하세요.</p>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th scope="col">항목</th><th scope="col">일정</th><th scope="col">확인할 일</th><th scope="col">공지·자료</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">새 Copilot·Code·Autopilot</th><td>Frontier·Preview 순차</td><td>Copilot 라이선스, 지출 정책과 사용량 기반 과금 확인</td><td>MC1479277</td></tr>
      <tr><th scope="row">Copilot Chat 스킬</th><td>10월~11월 중순</td><td>관리 센터의 Agents → Tools에서 배포·차단·검토</td><td>MC1493223</td></tr>
      <tr><th scope="row">Planner 보고서</th><td>10월 말~11월 중순</td><td>에이전트 사용 정책과 보고서 생성 조건 확인</td><td>MC1506735</td></tr>
      <tr><th scope="row">Agent Builder 예약 실행</th><td>10월 말~11월</td><td>기존 권한 범위 내 실행, 예약은 사용자별 설정임을 안내</td><td>MC1302906</td></tr>
      <tr><th scope="row">작업 인사이트 개인화</th><td>10월</td><td>조직의 향상된 개인화(Enhanced personalization) 설정 확인</td><td>MC1492154</td></tr>
      <tr><th scope="row">Pages·Notebooks 저장 위치</th><td>10월 중순~11월 말</td><td>새 항목에 적용할 OneDrive DLP·보존 정책 점검</td><td>MC1449182</td></tr>
      <tr><th scope="row">Purview DLP</th><td>사용 가능·일부 Preview</td><td>웹 검색 제한, 레이블 기반 제한, 프롬프트·외부 메일 제한을 구분</td><td><a href="https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about">Microsoft Learn</a></td></tr>
      <tr><th scope="row">Copilot 주소 전환</th><td>남은 사용자 11월 초</td><td><code>*.cloud.microsoft</code> 허용과 연결 상태, 내부 안내 링크 점검</td><td>MC1462915</td></tr>
      <tr><th scope="row">Power Platform 환경 전환</th><td>11월 15일 신규 생성 중단부터</td><td>미관리 개발자 환경·Teams 환경 목록과 전환 담당자, 라이선스·용량 확인</td><td><a href="https://learn.microsoft.com/en-us/power-platform/important-changes-coming">Microsoft Learn</a></td></tr>
    </tbody>
  </table>
</div>

<div class="mc-callout mc-callout--dark">
  <p><strong>이번 호 한 줄 요약</strong></p>
  <p>Copilot은 질문에 답하는 도구에서 일을 맡기는 도구로 넓어지고 있습니다. <strong>반복 업무는 스킬로, 개인화는 내가 제어하고, 결과물은 조직 정책에 맞게 관리하세요.</strong></p>
</div>

<p>다음 호에서는 11월 Microsoft Ignite 소식과 함께 새 기능의 활용 방법을 이어서 살펴보겠습니다.</p>

<h2 class="mc-section-title">더 보기</h2>

<ul>
  <li><a href="{{ '/monthlycopilot/CopilotSkillsPowerPoint/' | relative_url }}">이번 호 실습 — PowerPoint에서 회사 서식, 스킬로 한 번에 맞추기</a></li>
  <li><a href="https://techcommunity.microsoft.com/category/microsoft365copilot/blog/microsoft365copilotblog">Microsoft 365 Copilot Blog</a></li>
  <li><a href="https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes">Microsoft 365 Copilot 릴리스 노트</a></li>
</ul>

<p class="mc-card-note">이 글은 제공된 ‘What's New in Copilot, 쉽게 읽기 – 2026년 10월’ 원고를 바탕으로 월간 코파일럿 11월호에 맞게 재구성했습니다. 기준일은 2026년 10월 20일이며, 기능 제공 일정·지원 언어·라이선스와 조직별 적용 범위는 변경될 수 있습니다. 화면은 원고에 포함된 참고 이미지로, 실제 메뉴와 표시 내용은 버전 및 조직 설정에 따라 다를 수 있습니다.</p>

</div>
