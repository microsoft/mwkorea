---
title: "Jev가 화제라면, Copilot Studio의 ‘분류’도 써보세요"
date: 2026-09-22T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - CopilotStudio
  - Workflow
  - Classification
  - Jev
  - 월간코파일럿
excerpt: "요즘 주목받는 Jev는 AI가 글을 쓰는 것뿐 아니라 분류하고 판단하는 역할도 중요하다는 점을 보여 줍니다. Copilot Studio 워크플로우에 내장된 Classify 노드로, 이런 활용 개념을 고객 문의 분류와 후속 업무 연결에 적용하는 방법을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 최정우
---

<div class="monthlycopilot-page monthlycopilot-page--agent">
<div class="mc-issue-strip">Monthly Copilot · October 2026 · 월간 코파일럿 10월호 · Copilot Studio · Workflow</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">월간 코파일럿 ｜ 2026년 10월호 ｜ Copilot Studio 활용 가이드</div>
  <div class="mc-cover-title">잘 쓰는 AI에서<br/>잘 나누는 AI로</div>
  <div class="mc-cover-subtitle">Jev가 불러온 관심, Classify 노드로 업무에 연결하기</div>
</div>

<p>최근 AI 관련 소식에서 <strong>Jev</strong>라는 이름이 눈에 띕니다. TypeSafe가 선보인 이 모델은 자연스러운 문장을 길게 생성하는 대신, 주어진 선택지 중 하나를 고르고, 점수를 매기고, 참·거짓을 판단하는 일에 초점을 맞춥니다. AI를 '사람에게 답변하는 도구'뿐 아니라 <strong>'소프트웨어가 다음 행동을 결정하도록 돕는 도구'</strong>로 바라보는 접근입니다.</p>

<p>이 이야기를 듣고 “우리 업무에도 이런 AI를 적용해 보면 좋겠다”고 생각했다면, 함께 살펴볼 기능이 있습니다. <strong>Copilot Studio 워크플로우에 내장된 Classify 노드</strong>입니다. 한국어 화면에서는 <strong>'분류'</strong>로 표시됩니다.</p>

<p>새로운 모델의 등장은 반가운 소식입니다. 하지만 업무에 적용하는 출발점이 반드시 새로운 API를 직접 연결하는 일일 필요는 없습니다. 텍스트의 의미를 읽고, 정해진 기준으로 분류하고, 필요한 다음 작업으로 보내는 흐름은 이미 Copilot Studio 안에서 구성할 수 있습니다.</p>

<img src="/mwkorea/assets/images/20260922-copilot-studio-classify/01-cover.png" alt="여러 고객 문의가 Classify를 거쳐 결제 문의, 기술 지원, 도입 상담으로 나뉘는 개념도" />
<p class="mc-card-note">그림 1. 글을 쓰는 AI에서 업무를 분류하고 연결하는 AI로. 활용 개념을 설명하는 일러스트이며, Jev가 Copilot Studio에 탑재되었다는 의미는 아닙니다.</p>

<hr/>

<h2 class="mc-section-title">1 · 업무에는 '읽고 나누는 일'이 많습니다</h2>

<p>공용 메일함에 들어온 문의를 담당 팀에 전달하고, 접수된 요청의 유형을 지정하고, 고객 피드백을 버그·개선 제안·칭찬으로 나누는 일. 하나씩 보면 작은 작업이지만 매일 반복되면 적지 않은 시간을 차지합니다.</p>

<p>여기서 필요한 것은 반드시 길고 정교한 답변이 아닙니다. <strong>“이 문의는 어느 팀이 맡아야 할까?”</strong>라는 좁고 구체적인 판단이 먼저입니다. Jev에 대한 관심도 AI가 이런 역할을 수행하는 방식에 주목하게 만듭니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>읽기</strong></div>
    <div>메일 본문이나 폼으로 들어온 자유로운 표현을 이해합니다.</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>나누기</strong></div>
    <div>업무에서 정한 카테고리 중 어디에 해당하는지 판단합니다.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>연결하기</strong></div>
    <div>담당 팀·에이전트·검토 절차로 후속 작업을 이어 갑니다.</div>
  </div>
</div>

<h2 class="mc-section-title">2 · 분류 기준은 자연어로 설명하면 됩니다</h2>

<p>Classify 노드는 입력된 텍스트를 사용자가 정의한 카테고리 중 하나로 분류하고, 해당 분기로 워크플로우를 진행합니다. 특정 단어가 들어 있는지만 확인하는 조건문과는 다릅니다. <strong>카테고리의 의미를 자연어로 설명하면, AI가 입력의 맥락을 보고 판단</strong>합니다.</p>

<p>예를 들어 '결제 문의'라는 이름만 붙이는 대신, “청구 금액, 중복 결제, 결제 수단 변경에 관한 문의”라고 설명할 수 있습니다. 서로 혼동하기 쉬운 카테고리는 무엇이 포함되고 무엇이 제외되는지 구분해 주는 편이 좋습니다.</p>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>들어온 문의</th><th>분류</th><th>이어질 업무 예시</th></tr>
    </thead>
    <tbody>
      <tr><td>“이번 달 요금이 두 번 청구됐어요.”</td><td><strong>결제 문의</strong></td><td>결제 담당 팀으로 전달</td></tr>
      <tr><td>“설정은 완료했는데 연결이 안 됩니다.”</td><td><strong>기술 지원</strong></td><td>지원 에이전트로 연결</td></tr>
      <tr><td>“우리 회사에서 도입하려면 어떻게 해야 하나요?”</td><td><strong>도입 상담</strong></td><td>영업 담당자에게 알림</td></tr>
      <tr><td>정의한 카테고리에 잘 맞지 않는 내용</td><td><strong>Other · 기타</strong></td><td>담당자가 직접 검토</td></tr>
    </tbody>
  </table>
</div>

<p>실제 업무에서 자주 등장하는 입력과 정답 카테고리를 예시로 추가할 수도 있습니다. “요금이 두 번 나갔어요”라는 입력을 '결제 문의'의 예시로 넣는 식입니다. 많은 예시를 무작정 넣기보다, 헷갈리는 경계 사례를 잘 고르는 것이 중요합니다.</p>

<img src="/mwkorea/assets/images/20260922-copilot-studio-classify/02-classify-settings.png" alt="Classify 실제 설정 화면. 분류할 입력, 결제 문의·기술 지원·도입 상담의 자연어 설명과 결제 문의 예시가 입력되어 있다" />
<p class="mc-card-note">그림 2. 실제 Classify 설정 화면. 샘플 문의, 카테고리 설명, 예시를 입력한 모습입니다. 계정 정보 영역은 캡처에서 제외했습니다. 분류 실행 결과가 아니며, 표시되는 모델은 환경과 제공 상태에 따라 달라질 수 있습니다.</p>

<div class="mc-callout">
  <p><strong>실무 팁 · 이름보다 설명을 다듬으세요.</strong></p>
  <p>'일반 문의'와 '기타 문의'처럼 경계가 겹치는 카테고리보다, 실제 처리 담당과 후속 행동이 구분되는 기준을 먼저 정해 보세요. 분류 체계가 분명해야 다음 업무도 명확해집니다.</p>
</div>

<hr/>

<h2 class="mc-section-title">3 · 분류에서 끝나지 않고, 실제 업무로 이어집니다</h2>

<p>현업에서 중요한 것은 “AI가 무엇이라고 판단했는가”만이 아닙니다. <strong>“그 판단 다음에 어떤 업무가 진행되는가”</strong>가 더 중요할 때가 많습니다.</p>

<p>Classify 노드에 카테고리를 정의하면 각각의 분기 연결 지점이 만들어집니다. 결제 문의는 담당 팀으로 전달하고, 기술 문의는 지원 에이전트로 연결하고, 도입 상담은 영업 담당자에게 알리는 식으로 구성할 수 있습니다. 한 입력에 대해서는 일치하는 분기만 실행됩니다.</p>

<img src="/mwkorea/assets/images/20260922-copilot-studio-classify/03-classify-branches.png" alt="실제 워크플로 캔버스에서 시작 노드와 연결된 분류 노드에 결제 문의, 기술 지원, 도입 상담, 기타 분기가 표시되어 있다" />
<p class="mc-card-note">그림 3. 카테고리를 정의하면 분기별 연결 지점이 표시됩니다. 이 화면은 후속 작업을 연결하기 전의 데모 초안이며, 게시하거나 실행하지 않았습니다.</p>

<p>어느 카테고리에도 잘 맞지 않는 입력을 처리하는 기본 <strong>Other(기타)</strong> 분기도 자동으로 제공됩니다. 이 분기를 비워 두기보다, 담당자가 직접 검토하거나 기록을 남기는 후속 처리로 연결하는 것이 좋습니다.</p>

<img src="/mwkorea/assets/images/20260922-copilot-studio-classify/04-workflow-concept.png" alt="고객 문의 텍스트가 Classify에서 분류되어 결제 담당 팀, 지원 에이전트, 영업 담당자 또는 수동 검토로 이어지는 구성 예시" />
<p class="mc-card-note">그림 4. 분류 이후의 업무를 연결하는 구성 예시. 실제 제품 화면이나 실행 결과가 아닌 설명용 도식입니다. 담당 팀 전달·에이전트 호출·검토 같은 후속 동작은 각 분기에 별도로 구성해야 합니다.</p>

<div class="mc-callout mc-callout--dark">
  <p><strong>분류 모델을 직접 붙이는 것과, 업무 흐름을 만드는 것은 다른 일입니다.</strong></p>
  <p>Copilot Studio에서는 분류 결과를 해석하고 다음 경로를 코드로 작성하는 대신, 같은 워크플로우 안에서 분류와 후속 처리를 함께 설계할 수 있습니다.</p>
</div>

<h2 class="mc-section-title">4 · Jev와 같은 모델이라는 뜻은 아닙니다</h2>

<p>여기서 구분할 점이 있습니다. Jev와 Classify 노드는 같은 층위의 제품이 아닙니다. Jev는 정해진 타입의 판단과 확률을 반환하도록 설계된 <strong>모델</strong>이고, Classify는 선택한 모델을 활용해 분류와 분기를 구성하는 <strong>워크플로우 기능</strong>입니다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>Jev · 판단을 수행하는 모델</strong></div>
    <div>선택지 판단, 점수화, 참·거짓 판단과 확률을 제공합니다. TypeSafe는 보정된 판단을 위한 학습 방식(RLCD)을 차별점으로 설명합니다.</div>
  </div>
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>Classify · 업무 흐름 안의 기능</strong></div>
    <div>입력, 카테고리 설명, 예시, 사용할 모델을 설정하고 결과를 후속 작업에 연결합니다.</div>
  </div>
</div>

<p>따라서 학습 방식이나 성능, 속도, 비용이 같다고 말할 수는 없습니다. Jev의 확률 관련 특성이 Classify에서도 그대로 제공된다는 뜻도 아닙니다. 다만 <strong>텍스트를 이해하고, 정해진 기준으로 판단하고, 알맞은 작업으로 연결한다는 업무 활용 개념은 많이 겹칩니다.</strong></p>

<p>새로운 모델의 기술적 차별점을 평가하는 일과, 지금 사용할 수 있는 도구로 업무를 개선하는 일은 함께 진행할 수 있습니다. 이 글이 전하고 싶은 메시지는 “새 모델이 필요 없다”가 아니라, <strong>“그런 활용에 관심이 생겼다면 이미 가까이에 있는 도구도 써보자”</strong>입니다.</p>

<hr/>

<h2 class="mc-section-title">5 · 공용 메일함 하나부터 시작해 보세요</h2>

<p>처음부터 복잡한 프로세스 전체를 자동화할 필요는 없습니다. 반복적으로 읽고 나누는 업무 하나를 골라, 어떤 카테고리와 후속 처리가 필요한지 정리하는 것으로 시작할 수 있습니다.</p>

<ol>
  <li><strong>업무 하나를 고릅니다.</strong> 공용 메일함, 지원 요청 폼, 고객 피드백처럼 실제로 분류가 반복되는 입력을 선택합니다.</li>
  <li><strong>카테고리와 처리 담당을 함께 정합니다.</strong> 이름과 자연어 설명을 작성하고, 각 분기에서 무슨 일을 할지 연결합니다.</li>
  <li><strong>샘플과 경계 사례를 준비합니다.</strong> 흔한 표현뿐 아니라 두 카테고리 사이에서 헷갈리는 입력, 어느 쪽에도 맞지 않는 입력을 포함합니다.</li>
  <li><strong>작게 확인한 뒤 운영에 연결합니다.</strong> 분류 품질을 확인하고, 중요한 판단에는 사람의 검토를 두며, 기타 분기의 처리 방법도 정합니다.</li>
</ol>

<p>분류에 사용할 모델도 선택할 수 있습니다. 카테고리의 차이가 미묘하거나 긴 입력을 해석해야 할 때와, 구분이 명확하고 처리량이 많은 경우에 필요한 모델은 다를 수 있습니다. 속도와 판단 품질, 비용을 실제 업무 입력으로 함께 살펴보세요.</p>

<div class="mc-callout">
  <p><strong>Classify와 에이전트 노드는 역할이 다릅니다.</strong></p>
  <p>알려진 카테고리 중 하나로 분류하고 분기하는 것이 전부라면 Classify가 간단한 선택입니다. 외부 도구를 호출하거나 지식을 찾아오고, 여러 입력을 종합해 판단한 뒤 행동까지 수행해야 한다면 에이전트 노드를 함께 검토하세요.</p>
</div>

<div class="mc-callout mc-callout--dark">
  <p><strong>새로운 모델 소식을, 실제 업무의 변화로 옮겨 보세요.</strong></p>
  <p>“이 모델을 어디에 붙일까?”와 함께 “우리 업무에서 매일 읽고 나누는 일은 무엇일까?”를 생각해 보세요. 그 첫 번째 흐름을 만드는 도구가 이미 Copilot Studio 안에 있습니다.</p>
</div>

<hr/>

<h2 class="mc-section-title">기능과 화면을 볼 때 참고하세요</h2>

<p>본문은 <strong>GitHub Copilot 하네스 기반 워크플로우의 Classify 노드</strong>를 기준으로 작성했습니다. 기능 안내와 공개 자료는 2026년 9월 22일 확인했으며, 실제 스크린샷은 같은 날짜에 Copilot Studio 미리 보기 환경에서 촬영했습니다. 사용 환경에 따라 화면, 사용 가능한 모델, 기능 제공 상태가 다를 수 있습니다.</p>

<p>새 하네스에서는 운영 실행뿐 아니라 빌드·테스트·평가 과정에서도 Copilot Credits가 소비될 수 있습니다. 운영에 적용하기 전에 관리자와 라이선스·권한·데이터 처리·비용 조건을 확인하세요.</p>

<p class="mc-card-note">이미지 안내: 그림 1·4는 직접 제작한 설명용 도식입니다. 그림 2·3은 가상의 고객 문의를 입력한 실제 제품 화면으로, 계정 정보 영역을 제외했습니다. 데모는 게시하거나 실행하지 않았으며, 실제 분류 성능이나 후속 업무 실행을 검증한 사례는 아닙니다.</p>

<h2 class="mc-section-title">공개 참고 자료</h2>

<ul>
  <li><a href="https://docs.typesafe.ai/concepts/system-one">TypeSafe — System One과 Jev</a></li>
  <li><a href="https://docs.typesafe.ai/introduction/machine-learning-primer">TypeSafe — RLCD와 보정된 판단</a></li>
  <li><a href="https://learn.microsoft.com/microsoft-copilot-studio/workflows-experience/classify-node-workflow">Microsoft Learn — Add a classify node to a workflow</a></li>
  <li><a href="https://learn.microsoft.com/microsoft-copilot-studio/workflows-experience/flow-designer">Microsoft Learn — Edit and manage your workflow in the designer</a></li>
</ul>

<p class="mc-card-note">모델의 특성과 제품 기능은 각 제공자의 공식 설명을 기준으로 정리했습니다. 업무 사례와 시작 순서는 독자의 활용을 돕기 위한 편집상 제안이며, 두 제품의 성능 우열을 비교한 결과가 아닙니다.</p>

</div>
