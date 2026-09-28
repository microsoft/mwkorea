---
title: "새로운 Copilot, 이제 묻고 맡기고 만들고 자동화한다"
date: 2026-09-28T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - CopilotCode
  - Autopilot
  - CopilotManagedRuntime
  - FinOps
  - 월간코파일럿
excerpt: "Home, Office in Copilot, Code, Copilot Managed Runtime, Autopilot, Microsoft IQ와 새 가격 모델까지. 2026년 9월 발표된 새로운 Copilot의 핵심과 조직이 지금 준비할 일을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 최정우
---

<div class="monthlycopilot-page monthlycopilot-page--agent">
<div class="mc-issue-strip">Monthly Copilot · October 2026 · 월간 코파일럿 10월호 · Wave 4</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">월간 코파일럿 ｜ 2026년 10월호 ｜ 새로운 Copilot</div>
  <div class="mc-cover-title">이제 묻고, 맡기고,<br/>만들고, 자동화한다</div>
  <div class="mc-cover-subtitle">Home · Code · Autopilot부터 가격 모델까지</div>
</div>

<p>2026년 9월 25일 Microsoft가 발표한 새로운 Copilot은 기능 몇 개를 더한 업데이트가 아닙니다. 질문에 답하는 <strong>Chat</strong>, 복잡한 일을 완성하는 <strong>Cowork</strong>, 업무용 앱을 만드는 <strong>Code</strong>, 며칠에 걸쳐 스스로 일하는 <strong>Autopilot</strong>을 하나의 경험으로 연결하려는 변화입니다.</p>

<p>아래 영상은 이번 발표를 13분으로 압축해 설명합니다. 이 글에서는 영상의 흐름을 따라 일곱 가지 발표를 다시 살펴보고, 조직이 기능보다 먼저 결정해야 할 비용과 거버넌스 항목을 정리했습니다.</p>

<div style="position: relative; width: 100%; padding-bottom: 56.25%; height: 0; overflow: hidden; margin: 1.2rem 0 0.6rem;">
  <iframe src="https://www.youtube.com/embed/w-qT5IAyl3Q" title="새로운 Copilot 총정리 - Home, Code, Autopilot부터 가격 모델까지" style="position: absolute; inset: 0; width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
<p class="mc-card-note">영상 · 매일매일코파일럿, 「새로운 Copilot 총정리 — Home · Code · Autopilot부터 가격 모델까지」, 2026년 9월 27일.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>묻기</strong></div>
    <div>Chat으로 질문하고 초안을 만듭니다.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>맡기기</strong></div>
    <div>Cowork에 복잡한 결과물을 위임합니다.</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>만들고 자동화하기</strong></div>
    <div>Code로 앱을 만들고 Autopilot이 일을 이어갑니다.</div>
  </div>
</div>

<hr/>

<h2 class="mc-section-title">1 · Home은 Copilot의 새로운 출발점입니다</h2>

<p><strong>Home</strong>은 최근 활동을 확인하고 하던 일을 이어 가는 시작 화면입니다. 여기서 Chat과 Cowork가 만납니다. 빠른 질문과 초안은 Chat에서 처리하고, 여러 자료를 모아 고객 브리핑이나 재무 결산 패키지처럼 완성된 결과물을 만드는 일은 Cowork에 맡깁니다.</p>

<p>중요한 변화는 사용자가 매번 도구를 먼저 고르는 방식에서 벗어난다는 점입니다. 앞으로는 원하는 결과를 설명하면 Copilot이 Chat, Cowork, Code 가운데 적합한 작업 방식으로 연결하는 방향으로 발전합니다. 영상에서 소개한 <strong>Today</strong>도 Home에 들어올 예정입니다. 일정, Teams 회의, 할 일을 모아 놓친 일과 지금 챙길 일을 구분하고 후속 조치를 준비하는 개인용 업무 화면입니다.</p>

<div class="mc-callout mc-callout--dark">
  <p><strong>Copilot의 첫 화면이 앱 목록에서 업무 흐름으로 바뀝니다.</strong></p>
  <p>사용자는 제품 이름보다 원하는 결과를 말하고, Copilot은 그 일을 수행할 경험을 연결합니다.</p>
</div>

<h2 class="mc-section-title">2 · Office 파일과 앱이 같은 업무 흐름에 들어옵니다</h2>

<p><strong>Office in Copilot</strong>은 Word, Excel, PowerPoint의 작성·편집 경험을 Copilot 안으로 가져옵니다. 출시 브리프, 예산 모델, 발표 자료를 요청하면 설명문으로 끝나는 것이 아니라 팀이 계속 편집하고 공동 작업할 수 있는 Office 파일을 만드는 방향입니다.</p>

<p>PowerPoint는 조직의 브랜드를 지키고, Excel은 무엇이 왜 바뀌었는지 설명하며, Excel의 재무 스킬과 Word의 법무 스킬처럼 직무 맥락을 담은 기능도 더해집니다. 생성형 AI의 결과가 채팅창에 머무르지 않고 실제 업무 파일로 이어진다는 점이 핵심입니다.</p>

<hr/>

<h2 class="mc-section-title">3 · Code는 앱을 네 번째 업무 문서로 만듭니다</h2>

<p>그동안 지식 근로자의 기본 결과물은 문서, 스프레드시트, 프레젠테이션이었습니다. <strong>Code</strong>는 여기에 작은 업무용 앱을 더합니다. 필요한 앱이나 대시보드, 자동화를 자연어로 설명하면 Copilot이 만들고 실행합니다. 개인용 데스크톱 위젯부터 팀과 공유하는 클라우드 앱까지 대상이 될 수 있습니다.</p>

<p>Microsoft CEO 사티아 나델라는 영상에 소개된 인터뷰에서 웹사이트, 앱, 문서의 경계가 희미해지고 있다고 설명합니다. 앱을 만드는 일이 전문 개발자만의 별도 프로젝트가 아니라 메모나 스프레드시트를 만드는 것처럼 일상적인 업무 역량으로 이동한다는 의미입니다.</p>

<p>그러나 동작하는 코드는 출발점일 뿐입니다. 인증, 데이터 접근, 보안 정책, 배포, 버전 관리, 감사와 운영까지 해결해야 조직에서 쓸 수 있습니다. 이 문제를 맡는 기반이 현재 미리 보기로 제공되는 <strong>Copilot Managed Runtime</strong>입니다.</p>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>단계</th><th>역할</th><th>조직이 확인할 것</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>만들기</strong></td><td>Cowork, Copilot Studio, SDK·CLI 등에서 앱 제작</td><td>누가 어떤 데이터와 커넥터로 앱을 만들 수 있는가</td></tr>
      <tr><td><strong>실행하기</strong></td><td>Microsoft 365 테넌트 정책을 상속하는 관리형 환경에서 호스팅</td><td>Entra 인증, 조건부 액세스, DLP, 공유 범위가 적절한가</td></tr>
      <tr><td><strong>관리하기</strong></td><td>Microsoft 365 관리 센터에서 인벤토리·사용량·상태·수명 주기 관리</td><td>앱 소유자, 검토 주기, 장애와 폐기 절차가 정해졌는가</td></tr>
    </tbody>
  </table>
</div>

<p>Copilot Managed Runtime의 약속은 <strong>만드는 도구는 다양하게, 운영은 일관되게</strong>입니다. 앱을 어떤 경로에서 만들었든 테넌트의 인증과 정책, 중앙 인벤토리 안에서 다루려는 구조입니다. 단, 현재 미리 보기 기능이므로 정식 서비스와 동일한 안정성·지원 범위를 전제로 도입해서는 안 됩니다.</p>

<hr/>

<h2 class="mc-section-title">4 · Autopilot은 기다리는 비서가 아니라 이어서 일하는 팀원입니다</h2>

<p><strong>Autopilot</strong>은 이전에 Scout로 소개됐던 기능입니다. 이름과 역할, 목표를 주면 매번 프롬프트를 기다리지 않고 채널을 살피고, 후속 조치를 준비하고, 반복 업무를 수행하며 며칠 뒤에도 프로젝트를 이어 갑니다. 클라우드에서 실행되고 자체 ID와 메모리, 컴퓨터를 가지며 Teams와 Outlook에서 동료처럼 멘션할 수 있는 디지털 팀원을 지향합니다.</p>

<p>예를 들어 공급업체 검토를 맡기면 일정 수립, 회의 준비, 후속 조치, 이해관계자 확인을 이어 갈 수 있습니다. 그렇다고 Chat과 Cowork가 사라지는 것은 아닙니다. Autopilot이 일을 진행하더라도 결과를 판단하고 수정하고 승인하는 사람의 역할은 남습니다. 이때 Chat과 Cowork는 사람이 결과를 검토하고 다음 지시를 내리는 접점이 됩니다.</p>

<div class="mc-callout">
  <p><strong>자율성보다 먼저 물어야 할 질문</strong></p>
  <p>어떤 행동까지 스스로 해도 되는가? 누가 중단하고 수정할 수 있는가? 어떤 로그를 얼마 동안 남길 것인가? 최종 승인과 책임은 누구에게 있는가?</p>
</div>

<p>영상에서 전한 인터뷰의 핵심도 신뢰입니다. 기업에서는 에이전트가 무엇을 했는지 관찰하고 통제하며 감사할 수 있어야 합니다. 사람은 시작과 결과 양쪽에서 계속 의사결정의 루프 안에 있어야 합니다.</p>

<hr/>

<h2 class="mc-section-title">5 · Microsoft IQ는 에이전트에 업무의 맥락을 더합니다</h2>

<p>에이전트가 유용하려면 언어 능력만으로는 부족합니다. 조직에서 말하는 고객, 매출, 위험, 우선순위가 무엇인지 이해해야 합니다. <strong>Microsoft IQ</strong>는 이 맥락을 제공하는 지능 계층입니다. Work IQ가 사람의 업무 맥락을, Fabric IQ가 비즈니스 데이터와 의미 체계를, Foundry IQ가 조직의 지식과 정책을, Web IQ가 공개 웹의 맥락을 담당합니다.</p>

<p>이번 발표에서 강조된 Fabric IQ 연결은 Power BI 보고서와 의미 모델의 데이터를 Cowork 업무에 이어 줍니다. 보고서에서 수치를 찾는 데 그치지 않고 그 결과로 메일을 작성하거나 문서를 만들고 검토 일정을 잡는 흐름입니다. Dynamics 365와 Power Platform의 고객·거래·지원 맥락도 앱을 오가며 복사하지 않고 활용하는 방향으로 확장됩니다.</p>

<p>플러그인 레지스트리는 Microsoft, 파트너, 조직이 만든 플러그인을 한 카탈로그에서 찾고 IT가 승인·관리하도록 돕습니다. 에이전트가 무엇을 알고 어떤 행동을 할 수 있는지 중앙에서 파악하는 것이 목적입니다.</p>

<hr/>

<h2 class="mc-section-title">6 · 가격은 '일상 업무'와 '맡긴 업무'로 나뉩니다</h2>

<p>새 가격 모델을 이해하려면 작업의 성격을 구분해야 합니다. 일상적인 답변·초안·요약과 모델 선택은 사용자 구독 라이선스인 <strong>USL(User Subscription License)</strong>이 담당합니다. 더 많은 시간과 컴퓨팅 자원, 전문 모델이 필요한 에이전트 작업은 <strong>UBB(Usage-Based Billing)</strong>로 Copilot Credits를 사용합니다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>USL · 일상적인 AI 업무</strong></div>
    <div>사용자당 고정 구독. 답변, 초안, 요약과 Auto 중심의 모델 라우팅 등 매일 사용하는 기반 경험을 제공합니다.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>UBB · 고급 에이전트 업무</strong></div>
    <div>사용량 기반 과금. Cowork, Code, Autopilot과 일부 고급·프런티어 모델처럼 더 많은 작업을 수행하는 경험에 적용됩니다.</div>
  </div>
</div>

<p>Microsoft는 USL을 평소 쓰는 배터리, UBB를 더 먼 거리를 갈 때 쓰는 연료 탱크에 비유합니다. 중요한 점은 UBB 경험을 쓰려면 USL만으로 충분하지 않다는 것입니다. 조직의 관리자가 지원되는 서비스, 대상 사용자·그룹, 예산과 알림, 결제 방법을 포함한 지출 정책을 구성해야 합니다.</p>

<p><strong>FinOps for AI</strong>는 이 사용량을 관리하는 체계입니다. Microsoft 365 관리 센터의 비용 관리 화면에서 조직·사용자 수준의 한도와 알림을 정하고, 정책·사용자·그룹·에이전트·서비스·자금 원천별 소비를 확인할 수 있습니다. 기능을 켜는 일과 비용 대비 가치를 검토하는 일을 같은 운영 절차에 넣어야 합니다.</p>

<div class="mc-callout mc-callout--dark">
  <p><strong>프롬프트 수가 아니라 완료한 일의 가치로 판단하세요.</strong></p>
  <p>사용한 크레딧과 함께 절감된 처리 시간, 결과물 품질, 재작업 감소, 의사결정 속도를 측정해야 사용량 과금이 합리적인지 설명할 수 있습니다.</p>
</div>

<hr/>

<h2 class="mc-section-title">7 · Auto가 모델 선택 자체를 제품 경험으로 만듭니다</h2>

<p>Copilot에는 여러 회사의 모델과 서로 다른 추론 수준이 함께 들어옵니다. 모든 사용자가 요청마다 모델 이름과 옵션을 비교하는 방식은 오래가기 어렵습니다. <strong>Auto</strong>는 정확도, 속도, 비용을 고려해 작업에 맞는 모델과 추론 수준을 선택합니다.</p>

<p>따라서 조직의 모델 전략도 특정 모델 하나를 표준으로 고정하는 데서 달라질 수 있습니다. 어떤 데이터와 업무를 어떤 모델군에 맡길 수 있는지 정책을 정하고, 품질·지연 시간·비용을 시나리오별로 평가하는 일이 중요해집니다. 자동 선택을 쓰더라도 민감 데이터, 지역, 계약 조건과 하위 처리자 검토가 사라지는 것은 아닙니다.</p>

<hr/>

<h2 class="mc-section-title">영상에서 정리한 제공 일정</h2>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>시점</th><th>발표 내용</th><th>확인할 점</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>현재</strong></td><td>Copilot Managed Runtime 공개 미리 보기, Fabric IQ의 Chat·Cowork 연결</td><td>테넌트·지역·라이선스별 실제 제공 여부와 미리 보기 조건</td></tr>
      <tr><td><strong>9월 말</strong></td><td>Code의 Frontier 제공, Autopilot과 Teams의 <code>@Copilot</code> 비공개 미리 보기 확대</td><td>초대·등록 대상과 데이터 처리 조건</td></tr>
      <tr><td><strong>향후 몇 주</strong></td><td>Home의 Frontier 제공</td><td>기존 Copilot 진입 화면과 사용자 안내 변경</td></tr>
      <tr><td><strong>10월</strong></td><td>Today 비공개 미리 보기 시작</td><td>국내 일정과 한국어 지원 여부</td></tr>
      <tr><td><strong>11월 17일 이후</strong></td><td>Microsoft Ignite에서 후속 발표 예정</td><td>정식 출시·가격·관리 기능의 변경 사항</td></tr>
    </tbody>
  </table>
</div>

<p class="mc-card-note">일정은 영상 공개 시점의 발표를 기준으로 하며 변경될 수 있습니다. 국내 제공 일정과 한국어 지원, 라이선스 조건은 담당 팀과 최신 공식 문서에서 다시 확인하세요.</p>

<h2 class="mc-section-title">지금 준비할 다섯 가지</h2>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>1 · 파일럿 업무 선택</strong></div>
    <div>Cowork, Code, Autopilot에 맡길 반복적이고 결과를 검증하기 쉬운 업무를 하나씩 고릅니다.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>2 · 비용 정책 설계</strong></div>
    <div>대상 사용자·그룹, 한도, 알림, 증액 승인과 자금 원천을 정합니다.</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>3 · 앱 인벤토리 확보</strong></div>
    <div>소유자, 데이터, 커넥터, 공유 범위, 마지막 검토일을 기록합니다.</div>
  </div>
  <div class="mc-card mc-card--amber">
    <div class="mc-card-title"><strong>4 · 비즈니스 맥락 정리</strong></div>
    <div>Power BI 의미 모델, Dynamics 데이터, 승인할 플러그인과 기준 문서를 점검합니다.</div>
  </div>
  <div class="mc-card mc-card--green">
    <div class="mc-card-title"><strong>5 · 사람의 승인선 정의</strong></div>
    <div>에이전트가 제안·실행·외부 전달할 수 있는 범위와 중단 권한을 구분합니다.</div>
  </div>
</div>

<div class="mc-callout mc-callout--dark">
  <p><strong>새로운 Copilot의 핵심은 기능의 수가 아니라 업무 단위의 변화입니다.</strong></p>
  <p>질문에 답하는 AI에서 일을 맡고, 앱을 만들고, 며칠 동안 업무를 이어 가는 AI로 범위가 넓어집니다. 이제 조직이 준비할 것은 더 긴 프롬프트가 아니라 비용·데이터·권한·책임을 함께 설계하는 운영 방식입니다.</p>
</div>

<hr/>

<h2 class="mc-section-title">공개 참고 자료</h2>

<ul>
  <li><a href="https://youtu.be/w-qT5IAyl3Q">매일매일코파일럿 — 새로운 Copilot 총정리</a></li>
  <li><a href="https://learn.microsoft.com/partner-center/announcements/2026-september">Microsoft Partner Center — September 2026 announcements</a></li>
  <li><a href="https://learn.microsoft.com/microsoft-365/managed-apps/">What is Copilot Managed Runtime (preview)</a></li>
  <li><a href="https://learn.microsoft.com/microsoft-365/admin/manage/apps/">Copilot Managed Runtime overview for admins (preview)</a></li>
  <li><a href="https://learn.microsoft.com/microsoft-365/copilot/user-subscription-license-usage-based-billing">Understanding USL and UBB</a></li>
  <li><a href="https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-overview-copilot-credits">Copilot Credits 사용량 기반 과금과 비용 관리</a></li>
  <li><a href="https://learn.microsoft.com/fabric/iq/overview">What is Fabric IQ?</a></li>
  <li><a href="https://learn.microsoft.com/fabric/iq/connectors/cowork-overview">Fabric IQ in Microsoft 365 Copilot Cowork</a></li>
</ul>

<p class="mc-card-note">공개 자료 확인일: 2026년 9월 28일. 영상과 Microsoft 공식 공개 문서를 바탕으로 국내 독자를 위해 재구성했습니다. 미리 보기 기능, 제공 일정, 명칭과 과금 조건은 변경될 수 있습니다.</p>

</div>