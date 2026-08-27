---
title: "이름이 바뀌었습니다 — Copilot Studio의 세 가지 하네스, 무엇을 고를 것인가"
date: 2026-08-27T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - CopilotStudio
  - Harness
  - Agent
  - Workflow
  - 월간코파일럿
excerpt: 'Copilot Studio의 새 경험·클래식 경험이 GitHub Copilot 하네스·표준 하네스·Copilot 챗 하네스로 정리되었습니다. 하네스가 무엇인지, 왜 GitHub 이름이 붙었는지, 그리고 다음 에이전트를 만들 때 무엇을 골라야 하는지 정리했습니다.'
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 최정우
---

<div class="monthlycopilot-page monthlycopilot-page--adoption">
<div class="mc-issue-strip">Monthly Copilot · September 2026 · 월간 코파일럿 9월호 · Copilot Studio · Harness</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">월간 코파일럿 ｜ 2026년 9월호 ｜ Copilot Studio</div>
  <div class="mc-cover-title">이름이<br/>바뀌었습니다</div>
  <div class="mc-cover-subtitle">Copilot Studio의 세 가지 하네스, 무엇을 고를 것인가</div>
</div>

<div class="mc-callout">
  <p>Copilot Studio를 오랜만에 열어본 분이라면 낯선 단어를 마주쳤을 겁니다. <strong>하네스(harness)</strong>. 게다가 그중 하나는 이름이 <strong>GitHub Copilot 하네스</strong>입니다. Power Platform 이야기를 하는 줄 알았는데 왜 갑자기 GitHub일까요. 이번 호에서는 이 이름 변경이 무엇을 의미하는지, 그리고 여러분이 다음 에이전트를 만들 때 무엇을 골라야 하는지를 정리합니다.</p>
</div>

<hr/>

<h2 class="mc-section-title">1 · 무엇이 바뀌었나 — '경험'에서 '하네스'로</h2>

<p>그동안 Copilot Studio에는 두 갈래 길이 있었습니다. 홈페이지의 토글로 켜고 끄던 <strong>새 경험(New experience)</strong>과 <strong>클래식 경험(Classic experience)</strong>입니다. 이름만 놓고 보면 UI 개편처럼 들립니다. 새 화면과 옛 화면, 취향껏 고르라는 이야기처럼요.</p>

<p>그런데 실제로 두 경험은 화면만 다른 것이 아니었습니다. 요청을 해석하는 방식, 도구를 부르는 방식, 실패했을 때 대응하는 방식, 심지어 과금 방식까지 달랐습니다. <strong>엔진이 다른데 겉면 이름으로 불러왔던 셈</strong>입니다.</p>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>이전에 부르던 이름</th><th>지금의 정식 명칭</th></tr>
    </thead>
    <tbody>
      <tr><td>새 경험(New experience)</td><td><strong>GitHub Copilot 하네스</strong></td></tr>
      <tr><td>클래식 경험(Classic experience)</td><td><strong>표준 하네스(Standard harness)</strong></td></tr>
      <tr><td>(M365 Copilot 확장)</td><td><strong>Copilot 챗 하네스(Copilot chat harness)</strong></td></tr>
    </tbody>
  </table>
</div>

<p>세 번째 줄이 중요합니다. Microsoft 365 Copilot을 확장하는 시나리오는 예전에도 있었지만, 이제는 <strong>별도의 하네스로 명확히 분리</strong>되어 세 갈래가 되었습니다. "두 개의 경험 중 하나를 고르는 문제"가 <strong>"세 개의 런타임 중 하나를 고르는 설계 결정"</strong>으로 승격된 것입니다.</p>

<hr/>

<h2 class="mc-section-title">2 · 그래서 하네스가 뭔가요</h2>

<img src="/mwkorea/assets/images/20260827-copilot-studio-harness/img00.png" alt="하네스(harness) 개념 설명 이미지" />

<p><code>harness</code>는 원래 <strong>마구(馬具)</strong>를 뜻합니다. 말과 마차를 연결하는 장치죠. 말이 아무리 좋아도 마구가 부실하면 마차는 원하는 곳으로 가지 않습니다. Microsoft가 이 단어를 고른 이유는 정확히 그 그림 때문입니다.</p>

<div class="mc-callout mc-callout--dark">
  <p><strong>여러분이 에이전트를 설계하고, 선택한 모델이 추론과 생성을 담당한다. 하네스는 그 사이에 있는 런타임이다.</strong></p>
</div>

<p>즉 하네스가 하는 일은 네 가지입니다.</p>

<div class="mc-card-grid mc-card-grid--4">
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>① 언제</strong></div>
    <div>모델을 호출할지 결정</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>② 무엇을</strong></div>
    <div>모델에 보낼지 구성</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>③ 어떻게 해석</strong></div>
    <div>돌아온 응답을 해석하는 방식 결정</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>④ 도구 호출</strong></div>
    <div>해석에 맞는 도구를 실행</div>
  </div>
</div>

<p>여기서 자주 나오는 오해 하나를 짚고 갑니다. <strong>"최신 모델을 쓰니까 좋은 에이전트"가 아닙니다.</strong> 모델은 마구에 매인 말입니다. 같은 모델을 얹어도 하네스가 다르면 결과가 달라집니다. 표준 하네스에 최신 모델을 물려도 여러분이 정의한 토픽 밖으로는 나가지 않고, GitHub Copilot 하네스는 목표만 주면 스스로 단계를 쪼갭니다.</p>

<div class="mc-callout">
  <p><strong>모델 선택은 성능 튜닝이고, 하네스 선택은 아키텍처 결정입니다.</strong> 순서가 뒤바뀌면 안 됩니다.</p>
</div>

<hr/>

<h2 class="mc-section-title">3 · 왜 하필 'GitHub Copilot' 하네스인가</h2>

<p>가장 많이 받는 질문입니다. Power Platform 제품 안에 왜 GitHub 브랜드가 들어왔을까요. 이 작명은 마케팅이 아니라 <strong>엔진의 출처를 밝힌 것</strong>에 가깝습니다. 문서가 설명하는 이 하네스의 구성 요소를 나열해 보면 답이 보입니다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>계획 → 실행 → 복구</strong></div>
    <div>목표를 받아 스스로 단계로 분해하고, 단계가 실패하면 다른 경로를 찾아 재시도합니다.</div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>스킬(Skills)</strong></div>
    <div>재사용 가능한 지시 묶음을 한 번 만들어 여러 에이전트에 붙입니다.</div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>메모리(Memory)</strong></div>
    <div>상호작용에서 얻은 맥락을 사용자별로 기억해 다음에 씁니다.</div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>보안 샌드박스</strong></div>
    <div>각 작업을 격리된 환경에서 실행합니다. 커넥터·지식·MCP·연결된 에이전트를 넘나들며 도구를 호출합니다.</div>
  </div>
</div>

<p>이 목록을 개발자에게 보여주면 곧바로 알아봅니다. <strong>GitHub Copilot CLI와 Copilot 클라우드 에이전트가 이미 쓰고 있는 개념들</strong>과 정확히 겹치기 때문입니다. 스킬, 메모리, 샌드박스, 도구 오케스트레이션, 계획→실행→복구 루프는 코딩 에이전트 세계에서 수년간 다듬어진 패턴입니다.</p>

<div class="mc-callout mc-callout--dark">
  <p>개발자 영역에서 검증된 에이전트 런타임을, 코드를 쓰지 않는 비즈니스 메이커의 로우코드 화면 위로 그대로 끌어올렸다. <em>(이하 필자 해석)</em></p>
</div>

<p>이름을 "고급 하네스"나 "프리미엄 하네스"로 붙였다면 그저 등급처럼 보였을 겁니다. <strong>GitHub Copilot이라는 이름을 붙였다는 건 "이건 개발자용 에이전트와 같은 엔진이다"라는 기술적 선언</strong>입니다. 그리고 뒤에서 볼 과금 방식까지 GitHub 쪽 방식(Copilot Credits)을 따라갑니다. 이름과 실체가 함께 움직인 셈입니다.</p>

<hr/>

<h2 class="mc-section-title">4 · 세 가지 하네스, 세 가지 성격</h2>

<img src="/mwkorea/assets/images/20260827-copilot-studio-harness/img01.png" alt="Copilot Studio의 세 가지 하네스 비교" />

<h3>GitHub Copilot 하네스 — 판단하는 동료</h3>

<p>가장 강력한 선택지입니다. <strong>고정된 스크립트를 따르는 대신 목표를 받아 스스로 계획을 세웁니다.</strong> 커넥터, 지식, MCP, 연결된 에이전트를 오가며 필요한 도구를 고르고, 중간에 단계가 실패하거나 요청이 바뀌면 경로를 수정합니다.</p>

<p>차별점 중 실무에서 가장 크게 체감되는 것은 <strong>파일 처리</strong>입니다. Word, Excel, PowerPoint, PDF를 네이티브로 만들고 편집하고 그 내용을 근거로 추론합니다. 문서가 곧 업무인 조직에서는 이 한 줄이 도입 여부를 가르기도 합니다.</p>

<div class="mc-card mc-card--blue">
  <div class="mc-card-title"><strong>적합한 예</strong></div>
  <div>송장을 읽어 발주서와 대조하고, 예외 건은 승인 라인으로 보내는 <strong>매입채무(AP) 처리 프로세스</strong>. 계약서 검토, 채용 프로세스처럼 판단과 적응이 필요한 다단계 업무.</div>
</div>

<h3>표준 하네스 — 약속대로 움직이는 창구</h3>

<p><strong>예측 가능성이 무기</strong>입니다. 여러분이 토픽, 프롬프트, 분기를 정의하면 그대로 동작합니다. 같은 질문에 같은 답이 나옵니다. 기존 프롬프트 라이브러리와 사내 지식을 그대로 활용할 수 있고, 지금까지 만들어 둔 자산이 여기 쌓여 있습니다.</p>

<p>"AI가 알아서 판단하는 게 늘 좋은 것 아닌가요?"라는 질문에 대한 답이 여기 있습니다. <strong>규정 안내, 승인 조건, 요금 계산처럼 답이 흔들리면 안 되는 영역에서는 창의성이 리스크입니다.</strong> 자율적 추론이 필요 없는 자리에 자율성을 넣으면 관리 비용만 늘어납니다.</p>

<div class="mc-card mc-card--teal">
  <div class="mc-card-title"><strong>적합한 예</strong></div>
  <div>자주 묻는 질문에 답하고 간단한 요청을 라우팅하는 <strong>사내 헬프데스크</strong>.</div>
</div>

<h3>Copilot 챗 하네스 — 이미 있는 자리로 답을 배달</h3>

<p>목표가 다릅니다. 새 채널을 만드는 게 아니라, <strong>직원이 이미 매일 쓰는 Microsoft 365 Copilot Chat 안으로 사내 지식을 연결</strong>합니다. 직원 입장에서는 별도 앱을 열 이유가 없습니다. 늘 쓰던 창에서 사내 문서에 근거한 답이 나옵니다.</p>

<p>대신 성격이 분명합니다. 현재의 챗 모델 위에서 동작하고, <strong>게시 대상은 사내 팀으로 한정</strong>됩니다. 파일 생성이나 복잡한 오케스트레이션은 이 하네스의 목표가 아닙니다.</p>

<div class="mc-card mc-card--purple">
  <div class="mc-card-title"><strong>적합한 예</strong></div>
  <div>SharePoint의 온보딩 문서를 근거로 신규 입사자의 질문에 답하는 <strong>온보딩 에이전트</strong>, 사내 정책 FAQ.</div>
</div>

<h3>한 장 비교표</h3>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>고려 항목</th><th>GitHub Copilot 하네스</th><th>표준 하네스</th><th>Copilot 챗 하네스</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>가장 잘 맞는 곳</strong></td><td>복잡한 다단계 업무 프로세스</td><td>규칙 기반 에이전트 · 정형 대화</td><td>사내 지식으로 M365 Copilot Chat 확장</td></tr>
      <tr><td><strong>동작 방식</strong></td><td>목표를 스스로 단계로 쪼개 추론</td><td>정의한 토픽과 규칙을 따름</td><td>사내 지식을 M365 Copilot Chat에 연결</td></tr>
      <tr><td><strong>문제 발생 시</strong></td><td>재시도 · 대체 경로 자동 탐색</td><td>만들어 둔 경로대로</td><td>해당 없음</td></tr>
      <tr><td><strong>파일 작업</strong></td><td>Word · Excel · PPT · PDF 생성/편집/추론</td><td>해당 없음</td><td>해당 없음</td></tr>
      <tr><td><strong>스킬 · 메모리</strong></td><td>지원</td><td>해당 없음</td><td>해당 없음</td></tr>
      <tr><td><strong>게시 대상</strong></td><td>사내 + 외부 고객</td><td>사내 + 외부 고객</td><td><strong>사내 전용</strong></td></tr>
      <tr><td><strong>과금</strong></td><td>Copilot Credits (사용량 기반)</td><td>Copilot Studio 라이선스 · 용량</td><td>사용량 기반 또는 M365 Copilot USL에 포함</td></tr>
    </tbody>
  </table>
</div>

<hr/>

<h2 class="mc-section-title">5 · 그럼 어떤 하네스를 골라야 하나</h2>

<p>세 문장으로 줄이면 이렇습니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>GitHub Copilot 하네스</strong></div>
    <div>긴 작업을 추론하고, 여러 도구를 넘나들고, 파일을 다루고, 실제 업무 프로세스를 끝까지 자동화해야 한다</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>표준 하네스</strong></div>
    <div>시나리오가 명확하고 규칙 기반이며, 일관되고 예측 가능한 답이 필요하다</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>Copilot 챗 하네스</strong></div>
    <div>새 채널을 만들 게 아니라, 직원이 쓰는 M365 Copilot Chat에 사내 지식을 얹고 싶다</div>
  </div>
</div>

<h3>실무 판단 순서</h3>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>순서</th><th>질문</th><th>예</th><th>아니오</th></tr>
    </thead>
    <tbody>
      <tr><td>Q1</td><td>직원이 이미 쓰는 M365 Copilot Chat 안에서 답만 주면 되는가?</td><td><strong>Copilot 챗 하네스</strong></td><td>↓ Q2로</td></tr>
      <tr><td>Q2</td><td>업무 절차를 내가 전부 그릴 수 있는가? (경로가 유한하고 명확)</td><td>↓ Q3으로</td><td>↓ Q4로</td></tr>
      <tr><td>Q3</td><td>답이 항상 똑같아야 하는가?</td><td><strong>표준 하네스</strong></td><td>↓ Q4로</td></tr>
      <tr><td>Q4</td><td>문서 생성·편집, 여러 도구 연계, 실패 복구가 필요한가?</td><td><strong>GitHub Copilot 하네스</strong></td><td><strong>표준 하네스</strong></td></tr>
    </tbody>
  </table>
</div>

<h3>판단을 도와주는 세 가지 질문</h3>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--amber">
    <div class="mc-card-title"><strong>Q1. "경로를 내가 다 그릴 수 있는가?"</strong></div>
    <div>그릴 수 있다면 표준 하네스로 충분합니다. 그리는 순간 경우의 수가 폭발한다면 그게 GitHub Copilot 하네스가 필요하다는 신호입니다.</div>
  </div>
  <div class="mc-card mc-card--amber">
    <div class="mc-card-title"><strong>Q2. "결과물이 대화인가, 산출물인가?"</strong></div>
    <div>답변으로 끝나면 표준 또는 챗 하네스. 보고서·정산표·요약본처럼 <strong>파일이 나와야 한다면</strong> GitHub Copilot 하네스가 사실상 유일한 선택입니다.</div>
  </div>
  <div class="mc-card mc-card--amber">
    <div class="mc-card-title"><strong>Q3. "누가 쓰는가?"</strong></div>
    <div>외부 고객에게 노출해야 한다면 Copilot 챗 하네스는 후보에서 빠집니다. 사내 전용이기 때문입니다.</div>
  </div>
</div>

<hr/>

<h2 class="mc-section-title">6 · 에이전트만 있는 게 아닙니다 — 워크플로우까지 넣은 선택지</h2>

<img src="/mwkorea/assets/images/20260827-copilot-studio-harness/img02.png" alt="Copilot Studio의 빌딩 블록과 하네스 대응 관계" />

<p>여기서 한 단계 더 들어갑니다. Copilot Studio에서 만들 수 있는 것은 에이전트만이 아니고, <strong>빌딩 블록마다 탈 수 있는 하네스가 정해져 있습니다.</strong> 이 대응 관계를 모르면 "왜 이 메뉴에서는 저 기능이 안 보이지?"에서 막힙니다.</p>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>빌딩 블록</th><th>무엇인가</th><th>어떤 하네스에서 도나</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>에이전트(Agents)</strong></td><td>대화하고 판단해 작업을 수행</td><td><strong>세 하네스 모두</strong></td></tr>
      <tr><td><strong>워크플로우(Workflows)</strong></td><td>드래그앤드롭 캔버스로 만드는 자동화. 단계마다 추론·행동 가능</td><td><strong>GitHub Copilot 하네스 전용</strong></td></tr>
      <tr><td><strong>에이전트 플로우(Agent flows)</strong></td><td>기존 방식의 플로우. Power Automate와 유사한 경험</td><td><strong>표준 하네스</strong></td></tr>
    </tbody>
  </table>
</div>

<h3>에이전트와 워크플로우, 무엇이 다른가</h3>

<p>같은 하네스 위에 있어도 성격이 반대입니다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>에이전트는 비결정적입니다</strong></div>
    <div>같은 요청이라도 상황에 따라 다른 경로로 갈 수 있습니다. 그게 장점입니다.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>워크플로우는 결정적입니다</strong></div>
    <div>같은 입력이면 같은 출력이 나옵니다. 트리거와 액션으로 구성되고, 노드 단위 테스트와 휴먼인더루프(사람 승인) 제어가 들어갑니다.</div>
  </div>
</div>

<div class="mc-callout mc-callout--dark">
  <p><strong>워크플로우가 절차를 붙잡고, 판단이 필요한 지점에서만 에이전트를 호출한다.</strong></p>
</div>

<p>예를 들어 매월 정산 프로세스라면 — 일정 트리거 → 데이터 수집(워크플로우) → <strong>예외 건 판단(에이전트 호출)</strong> → 승인 요청(휴먼인더루프) → 보고서 생성 → 발송. 절차의 뼈대는 예측 가능하게 두고, 사람의 판단이 필요했던 지점만 에이전트에게 넘기는 구조입니다. 워크플로우는 에이전트를 호출할 수 있고, 반대로 <code>에이전트가 플로우를 호출할 때</code> 트리거를 쓰면 워크플로우를 에이전트의 도구로 붙일 수도 있습니다.</p>

<h3>확장된 의사결정 지도</h3>

<img src="/mwkorea/assets/images/20260827-copilot-studio-harness/img03.png" alt="하네스와 빌딩 블록 조합 의사결정 지도" />

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>상황</th><th>권장 조합</th></tr>
    </thead>
    <tbody>
      <tr><td>절차가 고정, 판단 불필요</td><td>표준 하네스 + 에이전트 플로우</td></tr>
      <tr><td>절차가 고정, 일부 단계만 판단 필요</td><td>GitHub Copilot 하네스 + <strong>워크플로우</strong>(에이전트 호출 노드 포함)</td></tr>
      <tr><td>절차가 유동적, 목표만 명확</td><td>GitHub Copilot 하네스 + <strong>에이전트</strong></td></tr>
      <tr><td>대화가 중심, 답변 일관성이 최우선</td><td>표준 하네스 + 에이전트</td></tr>
      <tr><td>사내 지식 질의응답, 별도 채널 불필요</td><td>Copilot 챗 하네스 + 에이전트</td></tr>
    </tbody>
  </table>
</div>

<hr/>

<h2 class="mc-section-title">7 · 시작하기 전에 반드시 알아야 할 세 가지</h2>

<h3>① 하네스는 나중에 바꿀 수 없습니다</h3>

<div class="mc-callout mc-callout--dark">
  <p>⚠️ <strong>GitHub Copilot 하네스로 만든 에이전트는 표준 하네스로 옮길 수 없고, 그 반대도 불가능합니다.</strong> 하네스는 생성 시점에 정하는 결정이며, 되돌리려면 다시 만들어야 합니다.</p>
</div>

<p>그래서 PoC 단계에서 "일단 익숙한 걸로 만들고 나중에 옮기죠"라는 계획은 성립하지 않습니다. <strong>파일럿을 시작하기 전에 목적지를 정해야 합니다.</strong></p>

<h3>② 만드는 방식 자체가 다릅니다</h3>

<p>표준 하네스에서는 토픽을 만들고 분기를 그렸습니다. GitHub Copilot 하네스는 <strong>자연어 우선(natural-language-first)</strong>입니다. 에이전트를 말로 설명하면 시스템이 내부 구성을 생성합니다. 화면도 단일 서피스로 통합되어 <strong>Build / Preview / Evaluate / Monitor</strong> 네 탭으로 정리됩니다.</p>

<p>또 하나. 표준 하네스에서는 오케스트레이션 동작을 설정할 수 있었지만, <strong>GitHub Copilot 하네스는 향상된 오케스트레이션이 모든 에이전트에 기본 적용</strong>되며 선택 항목이 아닙니다. 조정 손잡이가 줄어든 대신 기본값이 올라간 셈입니다.</p>

<h3>③ 과금 모델이 갈라집니다</h3>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>하네스</th><th>과금</th></tr>
    </thead>
    <tbody>
      <tr><td>GitHub Copilot 하네스 (에이전트 · 워크플로우)</td><td><strong>Copilot Credits</strong> — 사용량 기반</td></tr>
      <tr><td>표준 하네스 (에이전트 · 에이전트 플로우)</td><td>Copilot Studio 라이선스 · 용량 모델</td></tr>
      <tr><td>Copilot 챗 하네스</td><td>사용량 기반 또는 M365 Copilot 사용자 구독에 포함</td></tr>
    </tbody>
  </table>
</div>

<p>주의할 점이 하나 더 있습니다. <strong>사용량 기반 과금은 운영뿐 아니라 빌드·테스트·평가에도 적용</strong>됩니다. 개발 단계에서도 크레딧이 소모된다는 뜻이므로, PoC 예산을 잡을 때 이 항목을 빼놓으면 안 됩니다.</p>

<p>워크플로우 쪽도 확인이 필요합니다. 워크플로우는 <strong>실행하는 액션마다 용량을 소모</strong>하고, 환경의 선불 용량을 모두 쓰면 새 실행이 차단됩니다(이미 실행 중인 건은 정상 완료). Power Platform 관리 센터에서 플로우별 액션 사용량을 주기적으로 확인하고, 필요하면 종량제 과금을 켜두는 편이 안전합니다.</p>

<div class="mc-card mc-card--green">
  <div class="mc-card-title"><strong>참고 — 지금 화면에서 찾는 법</strong></div>
  <div>기존 자산을 계속 쓰려면 홈페이지의 <strong>새 경험(New experience) 토글을 끄면</strong> 됩니다. 새로 만들 때는 홈페이지의 <strong>다른 방법으로 만들기(Other ways to build)</strong>에서 표준 하네스 에이전트와 에이전트 플로우를 생성할 수 있습니다.</div>
</div>

<hr/>

<h2 class="mc-section-title">8 · 한 줄로 정리하면</h2>

<p>이번 변화의 본질은 메뉴 개편이 아닙니다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>이름이 아니라 선택지가 명확해졌습니다</strong></div>
    <div>'새 경험 vs 클래식'은 취향처럼 들렸지만, '세 가지 하네스'는 설계 결정입니다.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>모델이 아니라 하네스를 먼저 고르십시오</strong></div>
    <div>모델은 튜닝이고 하네스는 아키텍처입니다. 게다가 하네스는 나중에 바꿀 수 없습니다.</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>자율성은 필요한 만큼만</strong></div>
    <div>판단이 필요 없는 자리에 판단하는 엔진을 넣으면 비용과 변동성만 늘어납니다.</div>
  </div>
  <div class="mc-card mc-card--amber">
    <div class="mc-card-title"><strong>워크플로우와 에이전트는 경쟁 관계가 아닙니다</strong></div>
    <div>절차는 워크플로우가, 판단은 에이전트가 — 이 조합이 실무에서 가장 오래 갑니다.</div>
  </div>
</div>

<div class="mc-callout mc-callout--dark">
  <p><strong>"만들기 전에 골라야 하는 것은 모델이 아니라 하네스입니다."</strong></p>
</div>

<p>GitHub Copilot이라는 이름이 Copilot Studio 안으로 들어온 것은, 개발자가 쓰던 에이전트 엔진과 비즈니스 메이커가 쓰던 로우코드 도구 사이의 경계가 옅어지고 있다는 신호이기도 합니다. 다음 에이전트를 만들 때 첫 화면에서 잠깐 멈춰 서서 물어보시길 권합니다 — <strong>이 일은 절차인가, 판단인가.</strong></p>

<div class="mc-card mc-card-note">
  <div>이 기사는 Microsoft Learn의 Copilot Studio 공식 문서(Choose a harness, Agents overview, Workflows overview, Agents powered by GitHub Copilot Harness overview, Copilot Studio overview)를 바탕으로 정리했으며, 명명 배경에 대한 해석은 필자의 견해입니다. 기능과 과금 정책은 업데이트될 수 있으므로 도입 전 최신 문서를 확인하시기 바랍니다.</div>
</div>

</div>
