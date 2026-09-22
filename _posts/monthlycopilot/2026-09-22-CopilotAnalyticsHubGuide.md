---
title: "Copilot 도입 다음 질문, 성과는 어디서 볼까?"
date: 2026-09-22T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - Analytics
  - PowerBI
  - Adoption
  - 월간코파일럿
excerpt: "Copilot 도입 이후 활용, 업무 가치, 비용, 에이전트 품질을 어디서 확인해야 할까요? Microsoft의 공개 Analytics Hub를 기준으로 목적에 맞는 대시보드를 고르고 숫자를 올바르게 해석하는 방법을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 정기남
---

<div class="monthlycopilot-page monthlycopilot-page--adoption">
<div class="mc-issue-strip">Monthly Copilot · October 2026 · 월간 코파일럿 10월호 · Analytics</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">월간 코파일럿 ｜ 2026년 10월호 ｜ 대시보드 활용 가이드</div>
  <div class="mc-cover-title">Copilot 도입 다음 질문,<br/>성과는 어디서 볼까?</div>
  <div class="mc-cover-subtitle">Analytics Hub로 고르는 우리 조직의 대시보드</div>
</div>

<p>Copilot을 도입한 뒤에는 새로운 질문이 생깁니다. 직원들은 꾸준히 활용하고 있을까요? 어떤 부서에 교육이 더 필요할까요? 에이전트가 요청을 잘 해결하고 있는지, 소비량과 비용은 어떻게 변하는지도 알고 싶습니다. 그러나 이 질문들을 <strong>'사용량'</strong>이라는 숫자 하나로 설명하기는 어렵습니다.</p>

<p>Microsoft의 공개 <a href="https://microsoft.github.io/Analytics-Hub/choose-report/">Analytics Hub</a>는 이런 상황에서 참고할 수 있는 보고서 선택 안내서입니다. 목표와 제품을 기준으로 후보를 좁히고, 각 카드에서 설명과 설정 안내, 데모 영상, 템플릿 또는 도구를 살펴보도록 돕습니다. 이 글의 그림은 공개 저장소에 게시된 실제 Preview GIF에서 추출한 정적 화면입니다. 화면의 예시 값은 우리 조직의 실측 성과가 아니며, 최신 템플릿과 화면 구성이 다를 수 있습니다.</p>

<img src="/mwkorea/assets/images/20260922-copilot-analytics-hub/01-super-usage-adoption.png" alt="Super Usage Adoption의 Microsoft 365 Copilot 개요 화면" />
<p class="mc-card-note">그림 1. Super Usage Adoption — M365 Copilot Overview. 공개 Preview GIF의 첫 번째 프레임.</p>

<hr/>

<h2 class="mc-section-title">하나의 화면보다, 하나의 질문부터</h2>

<p>먼저 <strong>"활용이 낮은 부서를 찾아 교육 대상을 정한다"</strong>처럼 결정할 일을 한 문장으로 적어 보세요. 비용을 관리할 때와 업무 가치를 설명할 때 필요한 지표는 다릅니다. Analytics Hub의 장점은 차트를 많이 모으는 데 있지 않습니다. 목적에 맞는 분석 도구를 찾고 다음 행동으로 연결하는 출발점을 제공한다는 데 있습니다.</p>

<p>이 글에서 '대시보드'는 지표를 종합해 보는 화면을 넓게 뜻합니다. 소개된 도구의 상당수는 Power BI 보고서 템플릿이며, Analytics Hub 자체가 조직 데이터를 자동 수집하는 서비스는 아닙니다.</p>

<h2 class="mc-section-title">질문에 따라 달라지는 대시보드 선택</h2>

<p>선택 페이지는 여섯 가지 목표를 제공합니다. 여기에 M365 Copilot, Copilot Chat, Studio Agents, Cowork, GitHub Copilot 중 관련 제품을 하나 이상 선택할 수 있습니다. 목표만 또는 제품만으로도 탐색할 수 있으며, 이름·데이터 원천·대상 독자로 검색할 수도 있습니다.</p>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>업무 질문 / 목표</th><th>먼저 살펴볼 보고서</th><th>주요 데이터·활용 관점</th></tr>
    </thead>
    <tbody>
      <tr><td>업무 가치를 어떻게 설명할까?<br/><strong>ROI &amp; Impact</strong></td><td>ValueLens for Microsoft Copilot<br/>Super User Impact</td><td>감사 로그 기반 가치 추정 또는 Viva Insights 기반 업무 패턴 분석. 경영진·가치 평가 담당자에게 적합.</td></tr>
      <tr><td>누가 꾸준히 활용할까?<br/><strong>Adoption</strong></td><td>AI-in-One Dashboard<br/>Super Usage Adoption</td><td>Purview·조직 정보 또는 Viva Insights를 바탕으로 IT·도입 담당자가 활용 현황과 확산 대상을 파악.</td></tr>
      <tr><td>소비량과 비용은 적절할까?<br/><strong>Cost &amp; Consumption</strong></td><td>Consumption Central for Microsoft Copilot</td><td>제품별 소비·비용 데이터로 재무·FinOps 담당자가 비용 배분과 예측을 검토.</td></tr>
      <tr><td>에이전트는 잘 해결할까?<br/><strong>Agent quality</strong></td><td>Agent Evaluator for Copilot Studio</td><td>대화 기록과 지원되는 비용 데이터로 에이전트 소유자가 품질·오류·개선 대상을 분석.</td></tr>
      <tr><td>개발팀은 어떻게 활용할까?<br/><strong>Developer productivity</strong></td><td>GitHub Copilot Impact</td><td>GitHub 사용량·멤버 정보와 조직 데이터로 팀별 활용·기능·수락률 추이를 분석.</td></tr>
      <tr><td>나의 활용 습관은 어떨까?<br/><strong>Individual productivity</strong></td><td>Personal Copilot Dashboard</td><td>허용된 Viva Insights 내보내기 또는 Person Query로 개인의 활용·추정 효과·학습 방향을 확인.</td></tr>
    </tbody>
  </table>
</div>

<p class="mc-card-note">표 1. 선택 페이지와 각 공개 저장소를 바탕으로 구성한 대표 후보 안내입니다. 한 보고서가 여러 목적에 쓰일 수 있으며 전체 도구 목록을 나열한 것은 아닙니다.</p>

<h2 class="mc-section-title">보고서 카드를 열었을 때 확인할 세 가지</h2>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>1 · 분석 대상</strong></div>
    <div>조직 전체를 보는 도구인지, 특정 에이전트나 개인을 보는 도구인지 확인합니다.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>2 · 데이터 원천</strong></div>
    <div>원하는 지표가 있어도 필요한 로그나 내보내기 파일을 확보하지 못하면 바로 사용할 수 없습니다.</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>3 · 운영 방식</strong></div>
    <div>설치 난이도뿐 아니라 새로 고침, 게시·공유, 권한 관리까지 함께 살펴봅니다.</div>
  </div>
</div>

<div class="mc-callout mc-callout--dark">
  <p><strong>권장 탐색 순서</strong></p>
  <p>목표 선택 → 관련 제품 선택 → 후보 카드 비교 → 상세 가이드·데모 확인 → 저장소의 최신 README에서 데이터·권한·배포 조건 확인</p>
</div>

<p>카드에 표시된 예상 설정 시간은 비교를 돕는 참고 정보로 보세요. 실제 조직에서는 권한 승인, 데이터 준비, 개인정보 검토가 추가로 필요할 수 있습니다. 템플릿별 조건이 다르므로 하나를 설치하면 나머지도 같은 방식으로 동작한다고 가정하지 않는 것이 좋습니다.</p>

<hr/>

<h2 class="mc-section-title">운영 목적이 다른 네 가지 대표 대시보드</h2>

<h3>1. AI-in-One Dashboard — 전반적인 활용 현황의 출발점</h3>

<p>Microsoft 365 Copilot, Copilot Chat, 에이전트의 활용 신호를 하나의 Power BI 보고서로 살펴보는 도구입니다. 시간에 따른 참여 변화와 부서·역할 등 조직별 차이를 파악해 추가 교육이 필요한 곳이나 활용을 확산할 후보를 찾는 데 활용할 수 있습니다.</p>

<p>현재 Rollup 버전은 원본 Purview CSV를 그대로 읽는 방식이 아닙니다. 감사 로그와 사용자·라이선스 정보를 미리 처리한 rollup 입력 파일이 필요하며, 저장소는 PAX를 권장합니다. 3-in-1 에디션은 로컬·SharePoint·OneLake 파일을 읽지만 Power BI Service 예약 새로 고침은 지원하지 않습니다. SharePoint 전용 에디션은 예약 새로 고침을 지원하므로 운영 방식을 먼저 정하세요.</p>

<img src="/mwkorea/assets/images/20260922-copilot-analytics-hub/02-ai-in-one-dashboard.png" alt="AI-in-One Dashboard의 Copilot 전체 추세 화면" />
<p class="mc-card-note"><strong>읽는 순서</strong> · 기간과 조직 필터를 먼저 맞춘 뒤 사용자당 활동 추세와 조직별 활성 사용자를 함께 봅니다. 사용량 차이는 교육·업무 특성·대상 인원 차이를 확인할 출발점입니다.</p>

<h3>2. ValueLens — 활동을 업무 가치의 언어로 설명</h3>

<p>ValueLens는 Copilot과 에이전트 활용을 절감 시간, 금액으로 환산한 지원 가치(Assisted Value), 활용 수준 등의 관점으로 보여 줍니다. 업무 상호작용을 분류하고 연구 기반 시간 기준값에 연결한 뒤 시간당 단가를 적용해 가치를 추정하는 구조입니다.</p>

<p>따라서 화면의 금액을 실제 발생한 매출이나 확정된 인건비 절감으로 읽어서는 안 됩니다. 어떤 기준값과 단가를 썼는지 함께 설명해야 합니다. 경영진 보고에서는 추정 가치와 별도로 실제 업무 처리 시간, 품질, 재작업 변화 같은 현장 근거를 연결하는 접근을 권합니다.</p>

<img src="/mwkorea/assets/images/20260922-copilot-analytics-hub/03-valuelens.png" alt="ValueLens의 성숙도 추세와 사용자당 절감 시간 히트맵" />
<p class="mc-card-note"><strong>읽는 순서</strong> · 색상과 기간별 변화는 추정치 비교를 돕지만 금액·절감 시간의 기준값이나 인과관계를 증명하지는 않습니다.</p>

<h3>3. Consumption Central — 소비량과 비용을 한눈에</h3>

<p>Cowork/Work IQ, Copilot Studio, GitHub Copilot, Azure AI Foundry의 소비·비용을 분석하는 Power BI 템플릿입니다. 확보한 제품 데이터부터 시작할 수 있으며 조직 속성을 연결하면 부서별 분석에도 활용할 수 있습니다. 비용 추세, 청구 기간 말 예측, 최적화 기회를 살펴보는 재무·FinOps 관점에 맞습니다.</p>

<p>핵심은 <strong>가시화</strong>입니다. 비용을 보여 주는 보고서가 지출 한도를 자동으로 강제하는 것은 아닙니다. 비용 수치는 계약 조건과 입력 단가를 확인하고 실제 청구 내역과 대조해야 하며, 정책 설정과 지출 통제는 별도로 관리해야 합니다.</p>

<img src="/mwkorea/assets/images/20260922-copilot-analytics-hub/04-consumption-central.png" alt="Consumption Central의 Copilot 크레딧 소비 화면" />
<p class="mc-card-note"><strong>읽는 순서</strong> · 제품별 집계 기간과 단위를 확인하고 부서별 구성을 살펴봅니다. 공개 GIF는 일부 제품 화면을 보여 주는 예시이며 현재 README의 지원 제품 전체가 한 프레임에 나타나는 것은 아닙니다.</p>

<h3>4. Agent Evaluator — 사용량을 넘어 해결 품질로</h3>

<p>Copilot Studio 에이전트의 세션, 대화 흐름, 오류, 주제, 근거 자료, 사용자 피드백을 분석합니다. 집계된 수치에서 실제 대화 기록으로 내려가 개선할 부분을 찾을 수 있으며, 설계된 담당자 이관과 실패를 구분한다는 점도 중요합니다.</p>

<p>데이터 연결 방식에 따라 가능한 화면이 달라집니다. 현재 공개 가이드는 Local CSV·Dataverse·Fabric 경로를 안내하며, 메시지 크레딧 관련 페이지는 Power Platform 관리 센터 내보내기를 수집하는 Fabric 경로가 필요하다고 설명합니다. 대화 분석만 연결했다고 비용 화면도 채워지는 것은 아닙니다.</p>

<img src="/mwkorea/assets/images/20260922-copilot-analytics-hub/05-agent-evaluator.png" alt="Agent Evaluator의 품질 및 성능 분석 화면" />
<p class="mc-card-note"><strong>읽는 순서</strong> · 해결·이관·이탈 비율을 함께 보고 이상 징후가 있는 에이전트의 대화 기록을 검토합니다. 원본에서 흐리게 처리된 식별 정보는 그대로 유지했습니다.</p>

<hr/>

<h2 class="mc-section-title">차트를 다음 행동으로 연결하는 방법</h2>

<h3>Super Usage Adoption — 활용 습관과 교육 대상을 찾기</h3>

<p>AI-in-One으로 조직별 차이를 살펴본 뒤, Viva Insights 데이터를 사용할 수 있다면 Super Usage Adoption에서 지속적으로 활용하는 사용자의 패턴을 봅니다. '누가 많이 썼나'에서 끝내지 않고 어떤 기능과 업무 흐름이 습관 형성에 연결되는지 탐색해 교육 주제를 정합니다.</p>

<h3>GitHub Copilot Impact — 개발팀의 활용을 좁혀 보기</h3>

<p>개발팀에는 GitHub Copilot Impact가 별도의 출발점입니다. 팀별 참여, 기능별 활용, 코드 제안 수락 등의 추이를 봅니다. 개인에게는 Personal Copilot Dashboard가 앱별 활용, 추정 절감 시간, 활용 여정과 학습 방향을 돌아보는 도구가 될 수 있습니다. 두 경우 모두 활동량이나 순위를 사람의 업무 성과 점수로 곧바로 바꾸지 않는 것이 중요합니다.</p>

<img src="/mwkorea/assets/images/20260922-copilot-analytics-hub/06-github-copilot-impact.png" alt="GitHub Copilot Impact 대시보드" />
<p class="mc-card-note">그림 6. GitHub Copilot Impact 공개 Preview GIF의 세 번째 프레임.</p>

<h3>Super User Impact — 활용 이후의 업무 패턴을 보기</h3>

<p>Super Usage Adoption이 활용 습관과 확산 경로에 초점을 맞춘다면, Super User Impact는 Viva Insights를 바탕으로 사용 수준과 회의·협업 등 업무 패턴의 관계를 살펴보는 보완 도구입니다. 사용 계층별·팀별 차이를 비교해 더 살펴볼 업무 흐름을 찾습니다.</p>

<img src="/mwkorea/assets/images/20260922-copilot-analytics-hub/07-super-user-impact.png" alt="Super User Impact의 업무 패턴 분석 화면" />
<p class="mc-card-note"><strong>해석 주의</strong> · 많이 사용하는 집단과 적게 사용하는 집단의 차이는 인과적 효과의 증명이 아닙니다. 직무·업무량·비교 기간과 집계 기준을 함께 확인하고 시간 지표를 개인 성과 평가로 곧바로 바꾸지 마세요.</p>

<h3>Copilot Chat &amp; Agent Intelligence — 채팅과 에이전트의 활용 깊이</h3>

<p>Purview 감사 로그와 Entra 사용자·조직 정보를 바탕으로 Copilot Chat 및 에이전트 사용을 분석하는 보고서입니다. 채팅의 프롬프트·세션·사용 표면, 참여 수준과 조직별 분포를 보고 교육 대상을 좁힐 수 있습니다.</p>

<img src="/mwkorea/assets/images/20260922-copilot-analytics-hub/08-copilot-chat-agent-intelligence.png" alt="Copilot Chat Intelligence 스냅샷 화면" />
<p class="mc-card-note"><strong>해석 주의</strong> · 감사 로그를 완전한 사용량이나 라이선스의 단일 기준으로 삼지 않습니다. 이 도구는 Chat·Agents의 공식 보고를 대체하지 않으므로 Microsoft 365 관리 센터와 Viva Insights를 함께 확인하세요.</p>

<h3>M365 Copilot Readiness Report — 도입·교육의 우선순위</h3>

<p>Purview의 Microsoft 365 감사 로그와 Entra 사용자 정보를 이용해 앱 활용과 Copilot 준비도 신호를 함께 봅니다. 부서별 준비도, 활성화·교육 후보를 탐색하는 도구이며, 전 직원에게 같은 순서로 배포하기보다 업무 특성과 활용 기반을 살펴보는 출발점입니다. 공개 저장소는 합성 데이터 DEMO PBIX와 실제 데이터 연결용 PBIT를 구분합니다.</p>

<img src="/mwkorea/assets/images/20260922-copilot-analytics-hub/09-m365-copilot-readiness.png" alt="Microsoft 365 Copilot Readiness 부서별 벤치마크 화면" />
<p class="mc-card-note"><strong>해석 주의</strong> · 준비도 점수와 추천은 배포 검토를 돕는 신호이지 성과 보장이나 자동 라이선스 회수 근거가 아닙니다. 실제 업무 수요·접근성·교육 기회를 함께 검토하세요.</p>

<hr/>

<h2 class="mc-section-title">숫자를 읽을 때 함께 물어야 할 질문</h2>

<p>같은 '활성 사용자'라도 데이터 원천, 집계 기간, 라이선스 대상, 활동 정의에 따라 값이 달라질 수 있습니다. 감사 로그 기반 보고서를 완전한 사용량 또는 라이선스의 단일 기준으로 삼지 말고, 필요한 경우 Microsoft 365 관리 센터와 Viva Insights 지표를 함께 확인하세요.</p>

<p>또한 사용량과 업무 패턴의 관계가 보인다고 해서 Copilot이 그 변화의 유일한 원인이라고 단정할 수는 없습니다. 직무와 업무량, 교육 시점, 비교 기간을 함께 검토해야 합니다. 대시보드는 다음 조사와 개선의 방향을 제시하는 도구이지 인과관계를 자동으로 입증하는 장치는 아닙니다.</p>

<div class="mc-callout mc-callout--dark">
  <p><strong>실무 제안</strong></p>
  <p>정기 검토 때 <strong>이번에 발견한 변화 1개 → 추가로 확인할 근거 → 실행할 조치 → 다음 검토일</strong>을 함께 기록하세요. 차트를 늘리는 것보다 의사결정의 연결 고리를 남기는 편이 유용합니다.</p>
</div>

<h2 class="mc-section-title">시작은 작게, 운영 기준은 분명하게</h2>

<p>첫 단계에서는 가장 중요한 질문 하나와 대표 보고서 하나를 고르는 것을 권합니다. 제공되는 샘플 데이터가 있다면 먼저 열어 화면이 질문에 답하는지 확인하세요. 이후 실제 데이터를 연결하고 유용성이 확인된 뒤 새로 고침과 공유를 운영 체계로 확장하는 편이 합리적입니다.</p>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>시작 전 확인</th><th>실무에서 정할 내용</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>데이터와 최신성</strong></td><td>원천 시스템, 필요한 파일·필드, 집계 기간, 누락 여부, 마지막 수집·새로 고침 시점을 확인합니다.</td></tr>
      <tr><td><strong>권한과 라이선스</strong></td><td>Purview·Viva Insights·Dataverse·GitHub 등의 접근 권한과 Power BI 게시·공유, 선택한 Fabric 경로의 요구 사항을 구분합니다.</td></tr>
      <tr><td><strong>개인정보와 공유</strong></td><td>분석 목적에 필요한 최소 데이터만 사용합니다. 개인 식별 여부, 최소 집계 단위, 대화 기록 열람 범위, 보관·공유 기준을 검토합니다.</td></tr>
      <tr><td><strong>운영과 해석</strong></td><td>담당자, 수집·갱신 주기, 오류 대응, 지표 정의와 단가·가정 변경 절차를 정합니다. 지원 경로와 프리뷰 조건도 확인합니다.</td></tr>
    </tbody>
  </table>
</div>

<p>개인별 화면의 필터는 접근 통제와 다릅니다. 다른 사용자의 행을 보지 못하게 하려면 게시 환경의 권한과 행 수준 보안(RLS)을 별도로 구성·확인해야 합니다. Consumption Central은 Viva의 최소 그룹 크기가 Power BI 연결에서 자동 적용되지 않는다고 안내하므로 개인정보 보호 기준을 보고서에서도 검토해야 합니다.</p>

<p>Analytics Hub의 공개 템플릿을 Microsoft 365의 기본 제공 관리 기능이나 정식 지원 제품과 동일하게 취급해서는 안 됩니다. ValueLens와 Agent Evaluator는 실험적 템플릿임을 명시하며, Consumption Central을 포함한 해당 저장소들은 Microsoft 일반 지원 채널 대신 저장소의 이슈 경로를 안내합니다. 라이선스·기능·지원 범위는 사용할 저장소의 최신 안내를 확인하세요.</p>

<div class="mc-callout mc-callout--dark">
  <p><strong>좋은 대시보드는 "그래서 무엇을 할까?"에 답합니다.</strong></p>
  <p>도입 현황을 볼지, 업무 가치를 설명할지, 비용과 에이전트 품질을 관리할지에 따라 필요한 화면은 달라집니다. Copilot의 성과를 이야기하는 출발점은 더 많은 차트가 아니라 더 분명한 질문입니다.</p>
</div>

<hr/>

<h2 class="mc-section-title">공개 참고 자료</h2>

<ul>
  <li><a href="https://microsoft.github.io/Analytics-Hub/choose-report/">Analytics Hub — Which report should I use?</a></li>
  <li><a href="https://github.com/microsoft/AI-in-One-Dashboard">AI-in-One Dashboard</a></li>
  <li><a href="https://github.com/microsoft/ValueLens-for-Microsoft-Copilot">ValueLens for Microsoft Copilot</a></li>
  <li><a href="https://github.com/microsoft/ConsumptionCentral-for-Microsoft-Copilot">Consumption Central for Microsoft Copilot</a></li>
  <li><a href="https://github.com/microsoft/AgentEvaluator-for-Copilot-Studio">Agent Evaluator for Copilot Studio</a></li>
  <li><a href="https://github.com/microsoft/DecodingSuperUsage/tree/DecodingSuperUsage">Super Usage Adoption / DecodingSuperUsage</a></li>
  <li><a href="https://github.com/microsoft/superuserimpact">Super User Impact</a></li>
  <li><a href="https://github.com/microsoft/GitHubCopilotImpact">GitHub Copilot Impact</a></li>
  <li><a href="https://github.com/microsoft/Personal-Dashboard">Personal Copilot Dashboard</a></li>
  <li><a href="https://github.com/microsoft/CopilotChatAnalytics">Copilot Chat &amp; Agent Intelligence</a></li>
  <li><a href="https://github.com/microsoft/M365UsageAnalytics">M365 Copilot Readiness Report</a></li>
</ul>

<p class="mc-card-note">공개 자료 확인일: 2026년 9월 21일. Microsoft의 공식 공개 페이지와 microsoft 조직의 공개 저장소만 참고했습니다. 본문은 한글 요약이며 활용 제안은 편집상 제안입니다. 내부 업무 자료·비공개 제품 정보·Code NDA 자료는 사용하지 않았습니다.</p>

<details class="mc-card">
  <summary><strong>이미지 출처와 MIT 라이선스 고지</strong></summary>
  <p>그림 1·2·3·4·6·8·9: Copyright (c) Microsoft Corporation.<br/>그림 5: Copyright (c) 2026 Keith McGrane.<br/>그림 7: Copyright (c) 2026 Microsoft.</p>
  <p>Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:</p>
  <p>The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.</p>
  <p>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</p>
</details>

</div>