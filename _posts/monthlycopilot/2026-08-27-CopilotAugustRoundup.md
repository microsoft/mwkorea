---
title: "8월의 코파일럿, 49건을 다섯 갈래로 — 2026년 8월 신기능 총정리"
date: 2026-08-27T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - 신기능
  - CopilotStudio
  - CopilotCowork
  - Roadmap
  - 월간코파일럿
excerpt: '2026년 8월 한 달간 ModernWork Korea에 올라온 49건의 소식을 다섯 갈래로 다시 묶었습니다. 에이전트가 운영 단계로 넘어가고, 데이터는 옮기지 않고 연결되며, 대화창이 작업 공간이 된 한 달 — 그리고 조용히 취소된 세 가지까지 정리했습니다.'
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 최정우
---

<div class="monthlycopilot-page monthlycopilot-page--agent">
<div class="mc-issue-strip">Monthly Copilot · September 2026 · 월간 코파일럿 9월호 · What's New in August</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">월간 코파일럿 ｜ 2026년 9월호 ｜ What's New</div>
  <div class="mc-cover-title">8월의 코파일럿,<br/>49건을 다섯 갈래로</div>
  <div class="mc-cover-subtitle">2026년 8월 신기능 총정리 — 무엇이 열렸고, 무엇이 닫혔나</div>
</div>

<p>매일 하나씩 올라오는 소식은 각각으로 보면 작은 업데이트입니다. 그런데 한 달치를 모아 놓고 보면 이야기가 달라집니다. <strong>어떤 방향으로 밀고 있는지</strong>가 보이기 때문입니다.</p>

<p>2026년 8월, ModernWork Korea에는 <strong>49건</strong>의 소식이 올라왔습니다. 이번 호에서는 그 49건을 날짜순이 아니라 <strong>다섯 개의 흐름</strong>으로 다시 묶었습니다. 개별 기능 설명은 각 소식 글에 있으니, 여기서는 <strong>"그래서 우리 조직은 무엇을 준비해야 하는가"</strong>에 초점을 맞춥니다.</p>

<div class="mc-card mc-card--blue">
  <div class="mc-card-title"><strong>Article Summary</strong></div>
  <div>8월의 키워드는 <strong>운영(Operations)</strong>입니다. 에이전트를 <em>만드는</em> 이야기에서 <em>점검하고, 평가하고, 비용을 통제하고, 보존하는</em> 이야기로 무게중심이 옮겨 갔습니다. 동시에 데이터는 "복사해서 넣는" 방식에서 "연결해서 쓰는" 방식으로, 결과물은 "다른 앱으로 옮기는" 방식에서 "대화창 안에서 끝내는" 방식으로 이동했습니다.</div>
</div>

<hr/>

<h2 class="mc-section-title">에디터 픽 · 8월에 이것만은 놓치지 마세요</h2>

<div class="mc-card-grid">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>① GitHub Copilot harness 정식 출시</strong></div>
    <div>Copilot Studio의 새 에이전트 엔진이 정식 이름을 얻고 출시됐습니다. Cowork와 GitHub Copilot 코딩 에이전트를 움직이는 바로 그 런타임입니다.<br/><a href="/mwkorea/copilot/CopilotStudioGitHubCopilotHarness/">자세히 보기 →</a></div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>② Federated Copilot Connectors</strong></div>
    <div>MCP로 서드파티 데이터를 <strong>복사하지 않고</strong> 실시간 연결합니다. 인덱싱 없이 사용자 본인 ID로 접근하는 방식입니다.<br/><a href="/mwkorea/copilot/FederatedCopilotConnectors/">자세히 보기 →</a></div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>③ Cowork 노력 수준(Effort Levels)</strong></div>
    <div>Light부터 Max까지 다섯 단계로 품질·속도·비용의 균형을 직접 조절합니다. 크레딧 관리의 실질적인 손잡이입니다.<br/><a href="/mwkorea/copilot/CoworkEffortLevels/">자세히 보기 →</a></div>
  </div>
  <div class="mc-card mc-card--amber">
    <div class="mc-card-title"><strong>④ Purview의 Copilot 메모리 보존</strong></div>
    <div>Copilot이 <strong>기억한 것</strong>도 보존·조사 대상이 됩니다. 메모리를 켠 조직이라면 정책 검토가 필요합니다.<br/><a href="/mwkorea/copilot/PurviewCopilotMemoryRetention/">자세히 보기 →</a></div>
  </div>
  <div class="mc-card mc-card--green">
    <div class="mc-card-title"><strong>⑤ Outlook Copilot Chat 추론 범위 확장</strong></div>
    <div>받은편지함 전체와 캘린더까지 추론 대상이 되며, <strong>Copilot 라이선스가 없는 사용자</strong>에게도 제공됩니다.<br/><a href="/mwkorea/copilot/OutlookCopilotChatEnterpriseReasoning/">자세히 보기 →</a></div>
  </div>
  <div class="mc-card mc-card--red">
    <div class="mc-card-title"><strong>⑥ Excel <code>=COPILOT</code> 함수 취소</strong></div>
    <div>수식 안에서 Copilot을 부르는 계획이 철회됐습니다. 이 함수를 전제로 설계 중이던 시나리오가 있다면 재검토가 필요합니다.<br/><a href="/mwkorea/copilot/ExcelCopilotFunctionCancelled/">자세히 보기 →</a></div>
  </div>
</div>

<hr/>

<h2 class="mc-section-title">흐름 ① · 에이전트가 '만들기'에서 '운영'으로 넘어갔습니다</h2>

<p>7월까지의 에이전트 소식이 "무엇을 만들 수 있는가"였다면, 8월은 <strong>"만든 것을 어떻게 책임질 것인가"</strong>였습니다. 게시 전 점검, 평가, 비용 통제, 감사 — 운영 조직이 요구하던 항목들이 한 달 사이에 한꺼번에 올라왔습니다.</p>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>소식</th><th>핵심</th><th>운영 관점</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><a href="/mwkorea/copilot/CopilotStudioGitHubCopilotHarness/">GitHub Copilot harness 정식 출시</a></td>
        <td>두 달 프리뷰를 마치고 정식 이름과 함께 출시. 자체 벤치마크에서 코드 분석 40.6% → 88.1%</td>
        <td>새 에이전트의 <strong>기본 선택지</strong>가 바뀝니다</td>
      </tr>
      <tr>
        <td><a href="/mwkorea/copilot/CopilotStudioAgentReadiness/">Agent Readiness</a></td>
        <td>정책 제한·누락된 평가 등 게시를 막을 요소를 빌드 화면에서 미리 표시</td>
        <td>"게시 직전에 막히는" 사고를 줄입니다</td>
      </tr>
      <tr>
        <td><a href="/mwkorea/copilot/CopilotStudioAgentEvaluations/">에이전트 평가(Evaluations) 대폭 개선</a></td>
        <td>추론 추적, 인용 지식 소스, 실행 간 비교, 대용량 데이터셋, 맞춤 테스트 생성</td>
        <td>왜 통과·실패했는지 <strong>근거</strong>가 남습니다</td>
      </tr>
      <tr>
        <td><a href="/mwkorea/copilot/AgentReviewToolCopilotStudio/">Agent Review Tool</a></td>
        <td>저장된 구성 자체를 점검해 스킬 중복·없는 기능 참조·평가 공백을 탐지</td>
        <td>"Preview에서 잘 되는데요"를 검증합니다</td>
      </tr>
      <tr>
        <td><a href="/mwkorea/copilot/CopilotHarnessCostGovernance/">harness 크레딧 비용 거버넌스</a></td>
        <td>빌드·미리 보기·평가 단계에서도 크레딧 소비. 개발 환경과 프로덕션 환경 분리 통제</td>
        <td><strong>PoC 예산</strong>을 다시 잡아야 합니다</td>
      </tr>
      <tr>
        <td><a href="/mwkorea/copilot/Agent365WhatsNewJuly2026/">Agent 365 업데이트</a></td>
        <td>파트너 위험 신호 통합, 비용 관리, 도입 대시보드 GA, Registry sync GA, 멀티테넌트 미리 보기</td>
        <td>에이전트를 <strong>자산으로 관리</strong>하는 체계</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="mc-callout mc-callout--dark">
  <p>💡 <strong>읽는 방법</strong> — 이 여섯 건은 따로 떨어진 기능이 아니라 하나의 파이프라인입니다. <strong>만들고(harness) → 점검하고(Readiness) → 평가하고(Evaluations · Review Tool) → 비용을 통제하고(Cost Governance) → 자산으로 관리한다(Agent 365).</strong> 에이전트를 몇 개 만들어 본 조직이라면, 다음 분기 과제는 이 파이프라인을 갖추는 일이 됩니다.</p>
</div>

<hr/>

<h2 class="mc-section-title">흐름 ② · 데이터를 옮기지 않고 연결합니다</h2>

<p>지금까지 "Copilot에 우리 데이터를 넣는다"는 말은 대체로 <strong>복사·인덱싱</strong>을 뜻했습니다. 8월의 소식들은 그 전제를 흔듭니다. 원본은 그대로 두고, 필요할 때 <strong>연결해서 읽는</strong> 방식이 늘어났습니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>Federated Copilot Connectors</strong></div>
    <div>MCP 기반 실시간 연결. Microsoft에 저장·인덱싱하지 않고 사용자 본인 ID로 접근하며, 관리자는 관리 센터에서 통제권 유지.<br/><a href="/mwkorea/copilot/FederatedCopilotConnectors/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>Self-serve 동기화 커넥터</strong></div>
    <div>Jira·Confluence Cloud를 사용자가 직접 연결. 본인 권한으로 접근 가능한 콘텐츠만 동기화되고, 관리자는 단계적 롤아웃·비활성화로 통제.<br/><a href="/mwkorea/copilot/SelfServeSyncConnectors/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>Dataverse 네이티브 지식 소스</strong></div>
    <div>레코드·고객 데이터·운영 데이터를 Copilot Studio 에이전트의 근거로 직접 연결.<br/><a href="/mwkorea/copilot/CopilotStudioDataverseKnowledge/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>Azure SQL 지식 소스</strong></div>
    <div>사내 DB의 핵심 데이터를 기존 지식 소스와 동일한 방식으로 에이전트에 그라운딩.<br/><a href="/mwkorea/copilot/CopilotStudioAzureSQLKnowledge/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>선언적 에이전트의 스캔 PDF 이해</strong></div>
    <div>SharePoint의 스캔 PDF·이미지 기반 문서를 근거로 답변. 그동안 잠겨 있던 대규모 기업 콘텐츠가 열립니다.<br/><a href="/mwkorea/copilot/DeclarativeAgentsScannedPDF/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>PowerPoint 에이전트 모드 파일 참조</strong></div>
    <div>SharePoint 라이브러리·OneDrive 폴더의 파일을 참조해 슬라이드 생성. 붙여넣기 없이 사내 문서를 근거로.<br/><a href="/mwkorea/copilot/PowerPointAgentModeFileReference/">→ 소식 보기</a></div>
  </div>
</div>

<h3>Copilot Notebooks는 8월 한 달 동안 참조 유형을 네 번 늘렸습니다</h3>

<p>따로 보면 각각 작은 업데이트지만, 모아 놓으면 <strong>"노트북에 못 넣는 파일이 거의 없어졌다"</strong>는 결론이 나옵니다.</p>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>날짜</th><th>추가된 참조 유형</th><th>대표 활용</th></tr>
    </thead>
    <tbody>
      <tr><td>8/11</td><td><a href="/mwkorea/copilot/CopilotNotebooksCSVTSV/">CSV · TSV</a></td><td>정형 목록·표를 그대로 근거로</td></tr>
      <tr><td>8/11</td><td><a href="/mwkorea/copilot/CopilotNotebooksImageRefs/">JPG · PNG</a></td><td>이미지 속 차트·다이어그램 읽기</td></tr>
      <tr><td>8/13</td><td><a href="/mwkorea/copilot/CopilotNotebooksTextFormats/">MD · TXT · RTF</a></td><td>README·로그·회의 트랜스크립트</td></tr>
      <tr><td>8/26</td><td><a href="/mwkorea/copilot/CopilotNotebooksPowerBI/">Power BI 보고서</a></td><td>조직 데이터에 근거한 요약·브리프</td></tr>
    </tbody>
  </table>
</div>

<p>여기에 <a href="/mwkorea/copilot/CopilotNotebooksGovCloud/">DoD·GCC·GCC High 지원</a>까지 더해지며, 새 Notebooks 디자인이 규제 클라우드에도 도달했습니다.</p>

<hr/>

<h2 class="mc-section-title">흐름 ③ · 대화창이 작업 공간이 됩니다</h2>

<p>8월의 사용자 경험 업데이트를 관통하는 문장은 하나입니다. <strong>"결과물을 다른 곳으로 옮기지 말 것."</strong> 코드도, 초안도, 에이전트 호출도 채팅 안에서 끝나도록 바뀌고 있습니다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>코드 블록(Code Blocks)</strong></div>
    <div>코드·차트·다이어그램을 별도 캔버스로 넘어가지 않고 대화 흐름 안에서 바로 미리 보기. 기존 나란히 보기에 인라인 방식이 추가됩니다.<br/><a href="/mwkorea/copilot/M365CopilotCodeBlocks/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>쓰기 블록(Writing Blocks)</strong></div>
    <div>초안·메모·이메일을 Chat 안에서 인라인 편집. 앱을 오가지 않고 수정과 반복이 가능해집니다.<br/><a href="/mwkorea/copilot/M365CopilotWritingBlocks/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>Plus 메뉴의 Agents &amp; Skills</strong></div>
    <div>프롬프트를 쓰다가 특정 에이전트·스킬을 직접 호출. <code>/</code>와 <code>@</code> 입력으로도 접근합니다.<br/><a href="/mwkorea/copilot/CopilotPlusMenuAgentsSkills/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>Chat 진입점이 리본에서 캔버스로</strong></div>
    <div>Word·Excel·PowerPoint의 Copilot Chat 버튼이 앱 캔버스로 이동. 발견 가능성을 높이려는 변화입니다.<br/><a href="/mwkorea/copilot/CopilotChatEntryPointCanvas/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--amber">
    <div class="mc-card-title"><strong>Cowork 노력 수준 + <code>/cost</code></strong></div>
    <div>Light~Max 다섯 단계로 품질·속도·비용 조절, <code>/cost</code>로 남은 크레딧 비율·누적 사용량·초기화 시점 확인.<br/><a href="/mwkorea/copilot/CoworkEffortLevels/">노력 수준</a> · <a href="/mwkorea/copilot/CoworkCostSkillCredits/">/cost</a></div>
  </div>
  <div class="mc-card mc-card--amber">
    <div class="mc-card-title"><strong>OneDrive Copilot의 파일 스킬</strong></div>
    <div>파일 검색을 넘어 데이터 분석·요약·대시보드·프레젠테이션 생성까지 채팅 한곳에서. 8월 미리 보기, 12월 정식 출시 예정.<br/><a href="/mwkorea/copilot/CopilotOneDriveFileSkills/">→ 소식 보기</a></div>
  </div>
</div>

<h3>Researcher는 '한 명'에서 '팀'이 됐습니다</h3>

<p>8월 5일 하루에만 Researcher 관련 소식이 세 건 올라왔습니다. 세 건을 이어 붙이면 하나의 그림이 됩니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--green">
    <div class="mc-card-title"><strong>Memory</strong></div>
    <div>이전 대화 맥락을 기억해 매번 처음부터 설명할 필요를 줄입니다.<br/><a href="/mwkorea/copilot/ResearcherCopilotMemory/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--green">
    <div class="mc-card-title"><strong>Council</strong></div>
    <div>여러 공급사의 모델을 동시에 돌려 합의와 충돌을 한눈에 비교합니다.<br/><a href="/mwkorea/copilot/ResearcherCouncil/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--green">
    <div class="mc-card-title"><strong>Critique</strong></div>
    <div>GPT가 초안을 쓰고 Claude가 검토합니다. 정확성·완결성·인용 무결성을 서로 다른 모델이 교차 확인합니다.<br/><a href="/mwkorea/copilot/ResearcherCritique/">→ 소식 보기</a></div>
  </div>
</div>

<hr/>

<h2 class="mc-section-title">흐름 ④ · 통제와 규제 — 관리자의 손잡이가 늘었습니다</h2>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>소식</th><th>무엇이 달라지나</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><a href="/mwkorea/copilot/PurviewCopilotMemoryRetention/">Purview의 Copilot 메모리 보존</a></td>
        <td>저장된 메모리와 채팅에서 추론된 정보의 과거 버전을 보안·컴플라이언스·조사 목적으로 보존. 비활성 메모리 항목의 버전 관리도 지원</td>
      </tr>
      <tr>
        <td><a href="/mwkorea/copilot/DelegatedPromptPublishing/">조직 프롬프트 위임 게시</a></td>
        <td>관리자가 특정 사용자·보안 그룹에 게시 권한을 위임하면, Prompt Lab에서 직접 조직 프롬프트 관리 가능</td>
      </tr>
      <tr>
        <td><a href="/mwkorea/copilot/GCCHCustomEngineAgents/">GCC High 커스텀 엔진 에이전트</a></td>
        <td>규제 클라우드에도 커스텀 엔진 에이전트가 열립니다</td>
      </tr>
      <tr>
        <td><a href="/mwkorea/copilot/VivaGlintCopilotAdminAssist/">Viva Glint 관리자 어시스턴트</a></td>
        <td>설정 방법을 자연어로 물으면 단계별 안내와 해당 설정 페이지 딥링크까지 제공</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="mc-callout">
  <p>⚠️ <strong>메모리를 켠 조직이라면</strong> — Copilot 메모리는 편의 기능이지만, 보존 정책이 붙는 순간 <strong>기록 관리의 대상</strong>이 됩니다. 도입 전에 사내 보존·삭제 정책과의 정합성을 먼저 확인하는 편이 안전합니다.</p>
</div>

<hr/>

<h2 class="mc-section-title">흐름 ⑤ · 모델과 플랫폼</h2>

<div class="mc-card-grid">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>MAI-Image-2.6 — Arena 2위</strong></div>
    <div>이전 버전 대비 종합 +79 Elo, 텍스트 렌더링 +91 Elo. Google·Meta·xAI의 주요 모델을 앞섰습니다.<br/><a href="/mwkorea/copilot/MAIImage26ArenaNo2/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>MAI-Code-1.1-Flash — 가격은 4분의 1</strong></div>
    <div>Terminal-Bench 2.1에서 22%, .NET 작업에서 15% 개선. 토큰 25% 절감, 25% 빠른 스트리밍, 가격은 1.0의 4분의 1.<br/><a href="/mwkorea/copilot/MAICode11Flash/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>Work IQ Developer Tools 미리 보기</strong></div>
    <div>스캐폴딩 → 검증 → 평가 → 게시 → 모니터링을 하나의 흐름으로. 사람과 코딩 에이전트가 같은 문법으로 실행합니다.<br/><a href="/mwkorea/copilot/WorkIQDeveloperToolsPreview/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>파트너 에이전트 생태계</strong></div>
    <div>LegalZoom 에이전트를 Copilot 안에서 호출해 법률 자료를 얻고 변호사 연결까지. 업무 흐름의 단절을 줄이는 사례입니다.<br/><a href="/mwkorea/copilot/CopilotLegalWorkflow/">→ 소식 보기</a></div>
  </div>
</div>

<hr/>

<h2 class="mc-section-title">그리고, 조용히 닫힌 세 가지</h2>

<p>새로 열린 것만큼 중요한 것이 <strong>계획대로 오지 않은 것</strong>입니다. 로드맵을 전제로 설계 중이던 시나리오가 있다면 이 세 건은 반드시 확인해야 합니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--red">
    <div class="mc-card-title"><strong>Excel <code>=COPILOT</code> 함수 — 취소</strong></div>
    <div>수식 안에서 텍스트를 생성·분류·요약하려던 계획이 철회됐습니다. 동일 기능의 로드맵 항목 세 개가 함께 종료됐습니다.<br/><a href="/mwkorea/copilot/ExcelCopilotFunctionCancelled/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--red">
    <div class="mc-card-title"><strong>Domain Exclusion — 롤백</strong></div>
    <div>웹 그라운딩 시 특정 도메인을 제외하던 기능이 되돌려졌습니다. Microsoft는 중요성을 인지하고 다음 단계를 검토 중이라고 밝혔습니다.<br/><a href="/mwkorea/copilot/DomainExclusionRollback/">→ 소식 보기</a></div>
  </div>
  <div class="mc-card mc-card--red">
    <div class="mc-card-title"><strong>Copilot Create AI 이미지 대체 — 취소</strong></div>
    <div>영상 속 스톡 이미지를 AI 생성 이미지로 교체하는 기능이 최종적으로 도입되지 않기로 결정됐습니다.<br/><a href="/mwkorea/copilot/CopilotCreateAIImageCancelled/">→ 소식 보기</a></div>
  </div>
</div>

<hr/>

<h2 class="mc-section-title">이 밖에도 — 놓치기 아까운 소식들</h2>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>날짜</th><th>소식</th><th>한 줄 요약</th></tr>
    </thead>
    <tbody>
      <tr><td>8/05</td><td><a href="/mwkorea/copilot/SMBCopilotAdoption30Days/">Copilot in 30 (SMB)</a></td><td>25명 · 30일 무료 체험. CSP New Commerce로 2026년 12월 31일까지</td></tr>
      <tr><td>8/06</td><td><a href="/mwkorea/copilot/WordReadAloudVoiceQA/">Word Read Aloud 음성 Q&amp;A</a></td><td>읽어 주는 도중에 말로 질문하고 즉시 답변</td></tr>
      <tr><td>8/06</td><td><a href="/mwkorea/copilot/CopilotBackToSchoolTasks/">Copilot Tasks 활용법</a></td><td>반복 리마인더·학습 퀴즈·리서치를 Tasks에 위임</td></tr>
      <tr><td>8/07</td><td><a href="/mwkorea/copilot/TeamsQueuesIntelligentRecap/">Teams Queues 지능형 통화 요약</a></td><td>콜 큐 통화의 요약·핵심 논의·후속 조치를 Recap 탭에서</td></tr>
      <tr><td>8/07</td><td><a href="/mwkorea/copilot/TeamsQueuesCopilotChat/">Teams Queues 통화 후 Copilot Chat</a></td><td>사이드카로 요약을 받고 세부 내용을 질문</td></tr>
      <tr><td>8/10</td><td><a href="/mwkorea/copilot/OneDriveIOSPDFCopilot/">OneDrive iOS PDF Ask Copilot</a></td><td>텍스트를 선택해 설명·요약·번역·질문</td></tr>
      <tr><td>8/11</td><td><a href="/mwkorea/copilot/SharePointHTMLPages/">SharePoint HTML 페이지</a></td><td>Copilot으로 HTML을 생성하거나 업로드해 페이지로 렌더링</td></tr>
      <tr><td>8/13</td><td><a href="/mwkorea/copilot/PowerPointIPadCopilot/">PowerPoint iPad 공동 제작</a></td><td>메모·메일·사진으로 덱 생성, 백그라운드 작업 지원</td></tr>
      <tr><td>8/13</td><td><a href="/mwkorea/copilot/TeamsAgentCollaborationNoise/">Teams 에이전트 소음 줄이기</a></td><td>이모지 반응·스레드 답글·인용 답글 세 가지 설계 패턴</td></tr>
      <tr><td>8/19</td><td><a href="/mwkorea/copilot/TeamsCopilotChatSummary/">Teams 채팅 요약 강화</a></td><td>대화창 진입 시 안 읽은 메시지를 자동 요약</td></tr>
    </tbody>
  </table>
</div>

<hr/>

<h2 class="mc-section-title">그래서, 9월에 무엇을 해야 할까요</h2>

<p>8월 소식을 근거로 관리자와 메이커가 <strong>이번 달 안에 확인해 볼 만한 세 가지</strong>를 정리했습니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>① 하네스 선택 기준을 정하세요</strong></div>
    <div>GitHub Copilot harness가 정식 출시되면서 새 에이전트의 출발점이 달라졌습니다. <strong>하네스는 나중에 바꿀 수 없으므로</strong>, 팀 차원의 선택 기준을 먼저 문서화해 두는 편이 좋습니다.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>② 크레딧 예산에 '개발분'을 넣으세요</strong></div>
    <div>빌드·미리 보기·평가 단계에서도 크레딧이 소모됩니다. 메이커 개발 환경과 프로덕션 환경을 분리하고, 환경별 선불 용량을 지금 점검해 보세요.</div>
  </div>
  <div class="mc-card mc-card--amber">
    <div class="mc-card-title"><strong>③ 메모리·보존 정책을 맞춰 두세요</strong></div>
    <div>Copilot 메모리에 보존 정책이 붙습니다. 사내 기록 관리 정책과 어긋나는 부분이 없는지, 켜기 전에 한 번 검토가 필요합니다.</div>
  </div>
</div>

<div class="mc-callout mc-callout--dark">
  <p>8월의 소식을 한 문장으로 줄이면 이렇습니다. <strong>"에이전트를 만드는 시대는 지나갔고, 이제는 운영하는 시대입니다."</strong></p>
  <p>만드는 일은 며칠이면 됩니다. 점검하고, 평가하고, 비용을 통제하고, 기록을 남기는 일은 체계가 필요합니다. 8월에 열린 기능들은 대부분 그 체계를 만들라는 신호였습니다.</p>
</div>

<div class="mc-card mc-card-note">
  <div>이 글은 2026년 8월 ModernWork Korea에 게시된 소식 49건을 편집자 관점에서 재구성한 요약입니다. 각 기능의 정확한 사양·제공 시점·라이선스 요건은 원문 소식과 Microsoft 공식 로드맵을 확인해 주세요. 미리 보기 단계의 기능과 출시 일정은 변경될 수 있습니다.</div>
</div>

</div>
