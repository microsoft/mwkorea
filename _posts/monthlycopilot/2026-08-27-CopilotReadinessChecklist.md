---
title: "Microsoft 365 Copilot 도입을 위한 체크리스트 — 라이선스를 샀다고 준비가 끝나는 것은 아니다"
date: 2026-08-27T00:00:00 KST
categories:
  - monthlycopilot
tags:
  - Copilot
  - 도입가이드
  - Intune
  - Purview
  - 거버넌스
  - 월간코파일럿
excerpt: '"언제 켜면 되나요?"라는 질문에 답하기 전에 확인해야 할 것들. 계정·라이선스·업데이트 채널부터 네트워크, 핀 고정, 새로 늘어난 관리자 스위치, 데이터 과다공유 정비, 그리고 측정까지 — Copilot 도입 기술 준비도를 세 갈래로 정리했습니다.'
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 김은숙
---

<div class="monthlycopilot-page monthlycopilot-page--security">
<div class="mc-issue-strip">Monthly Copilot · September 2026 · 월간 코파일럿 9월호 · 도입 체크리스트</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">월간 코파일럿 ｜ 2026년 9월호 ｜ Readiness</div>
  <div class="mc-cover-title">Microsoft 365 Copilot<br/>도입을 위한 체크리스트</div>
  <div class="mc-cover-subtitle">라이선스를 샀다고 준비가 끝나는 것은 아니다</div>
</div>

<img src="/mwkorea/assets/images/20260827-copilot-readiness-checklist/img00.jpeg" alt="Copilot 기술 준비도 개념 이미지" />
<p class="mc-card-note">그림 1. 기술 준비도는 화려하지 않다. 그러나 도입 성패의 대부분은 여기서 갈린다.</p>

<p>Microsoft 365 Copilot 도입을 준비하는 조직에서 가장 자주 나오는 질문은 <strong>"언제 켜면 되나요?"</strong>다. 그러나 실제로 준비해야 할 일은 크게 세 갈래로 나뉜다. 계정과 라이선스, 기기와 네트워크를 다루는 <strong>기술 준비</strong>, 사용 현황을 들여다보는 <strong>애널리틱스</strong>, 그리고 <strong>데이터 과다공유 정비</strong>다. 스위치 하나가 아니라, 서로 맞물린 작업의 목록이다.</p>

<hr/>

<h2 class="mc-section-title">1 · 기본기: 계정, 라이선스, 그리고 업데이트 채널</h2>

<p>출발점은 예상 가능한 것들이다. 모든 사용자는 로그인을 위해 <strong>Microsoft Entra ID 계정</strong>이 있어야 하고, Copilot을 추가하려면 <strong>필수 Microsoft 365 구독 플랜</strong>이 있어야 하며, Microsoft 365 앱을 포함한 구독이 사용자마다 할당되어 있어야 한다.</p>

<p>현장에서 발이 걸리는 지점은 그다음이다. <strong>업데이트 채널</strong>이다. Copilot 기능을 쓰려면 Windows와 Mac 기기가 <strong>Current Channel</strong> 또는 <strong>Monthly Enterprise Channel</strong> 중 하나에 있어야 한다. 반기 채널(SAC)을 유지해 온 조직이라면 전환이 전제 조건이 된다.</p>

<p>앱 배포 경로는 열려 있다. Microsoft 365 Copilot 앱은 <strong>Intune</strong>(Microsoft Store 앱 또는 Win32 앱)으로도, <strong>Configuration Manager</strong>(애플리케이션 또는 패키지/프로그램)로도, <strong>그룹 정책</strong>으로도 배포할 수 있다. Windows 기기에 Microsoft 365 데스크톱 앱이 설치되어 있으면 Copilot 앱은 자동으로 설치되기도 한다.</p>

<div class="mc-callout mc-callout--dark">
  <p><strong>놓치기 쉬운 한 줄</strong></p>
  <p>Copilot 데스크톱 앱에는 <strong>"업데이트 확인" 버튼이 없다.</strong> 설치 관리자가 사용하는 것과 같은 CDN에서 조용히 업데이트를 받아간다. 따라서 <code>*.office.net</code> 도메인(Microsoft 365 CDN) 접근이 막혀 있으면 설치는 물론 이후 업데이트도 도달하지 못한다. 버전 확인은 <strong>설정 → 일반 → 정보</strong>에서. 앱은 1~2주 주기의 빠른 릴리스 주기를 따르며, 앱 업데이트 없이 기능이 먼저 보이는 경우도 있다.</p>
</div>

<hr/>

<h2 class="mc-section-title">2 · 네트워크와 개인 정보 설정: 조용한 차단자들</h2>

<img src="/mwkorea/assets/images/20260827-copilot-readiness-checklist/img01.jpeg" alt="Copilot 네트워크 연결 경로" />
<p class="mc-card-note">그림 2. Copilot은 Microsoft 365 앱과 동일한 연결 경로를 사용한다.</p>

<p>Copilot 환경은 Microsoft 365 앱이 사용하는 것과 <strong>동일한 네트워크 연결과 엔드포인트</strong>를 사용한다. 그래서 배포 전 Copilot 네트워크 연결 테스트는 건너뛸 수 없는 단계다. Microsoft 365 연결 테스트 도구와 관리 센터의 네트워크 성능 화면을 함께 쓰면 된다. 사용자가 Copilot에 접근하지 못하는 상황에서 <strong>WebSocket 프로토콜 차단</strong>이 의심될 때가 이 도구를 꺼내야 할 대표적인 순간이다.</p>

<p>개인 정보 설정은 더 은밀하다. Microsoft 365 앱의 <strong>'연결된 환경 사용 허용'</strong> 정책이 비활성화되어 있으면 일부 앱에서 Copilot 기능 자체가 나타나지 않는다. Word·Excel·PowerPoint·Outlook의 핵심 Copilot 환경을 위해서는 <strong>Office Feature Updates 작업</strong>이 정상 일정대로 실행되고 필요한 네트워크 리소스에 접근할 수 있어야 한다. Teams 회의 내용을 회의 종료 후 참조하려면 <strong>전사·기록 정책</strong>도 켜져 있어야 한다.</p>

<hr/>

<h2 class="mc-section-title">3 · 보이지 않으면 쓰이지 않는다</h2>

<p>의외로 손이 많이 가는 주제가 <strong>'핀 고정'</strong>이다. 이유는 단순하다. <strong>발견 가능성이 곧 사용률</strong>이기 때문이다. 작업 표시줄에 고정해 두면 승인된 AI 도구에 한 번의 클릭으로 접근할 수 있고, 마찰이 줄면 일상적 사용이 늘며, 데스크톱이든 브라우저든 일관된 진입점이 생긴다. 무엇보다 <strong>Copilot Chat은 자격을 갖춘 Microsoft 365 구독에 추가 비용 없이 포함</strong>되어 있다.</p>

<div class="mc-card-grid">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>전사 적용</strong></div>
    <div>관리 센터의 <strong>Copilot &gt; 설정 &gt; 사용자 액세스</strong>에서 한 번에 처리.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>일부 사용자만</strong></div>
    <div>보안 그룹을 만든 뒤 <strong>Intune 설정 카탈로그(Start Layout)</strong> 또는 <strong>GPO 보안 필터링</strong>으로 범위를 좁힌다.</div>
  </div>
</div>

<p>작업 표시줄 XML에 넣을 식별자는 하나다.</p>

<div class="mc-callout">
  <p><code>Microsoft.MicrosoftOfficeHub_8wekyb3d8bbwe!Microsoft.MicrosoftOfficeHub</code></p>
</div>

<p>레이아웃 적용 후에는 사용자가 <strong>로그아웃·재로그인</strong>해야 반영된다. 지난해 10월부터는 Copilot 앱과 함께 <strong>사람·파일·일정 컴패니언 앱</strong>도 작업 표시줄에 고정할 수 있게 됐다. 반대로 사용을 제한해야 한다면, <strong>설정 &gt; 통합 앱</strong>에서 Copilot Chat 접근 대상을 그룹 단위로 좁히거나, 개인용 Copilot 접근과 다중 계정 접근을 차단하는 선택지도 마련되어 있다.</p>

<hr/>

<h2 class="mc-section-title">4 · 새로 늘어난 스위치들: Frontier, Anthropic, 그리고 에이전트</h2>

<p>최근 1년 사이 관리자가 다뤄야 할 설정도 늘었다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>Frontier</strong></div>
    <div>관리 센터의 Copilot 설정에서 켜면 전체 사용자 또는 특정 Entra ID 그룹에 <strong>조기 액세스</strong>를 부여할 수 있다(대상자는 Copilot 라이선스 필요).</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>AI 공급자 설정</strong></div>
    <div>Microsoft의 하위 처리자로 동작하는 <strong>Anthropic 모델</strong>의 사용 대상을 지정. 제품 사용 조건, 데이터 보호 부칙, EDP, 고객 저작권 보장이 그대로 적용된다.</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>자사 에이전트</strong></div>
    <div>Researcher·Analyst는 관리 센터 <strong>에이전트</strong> 페이지에서 게시자를 Microsoft로 필터링해 설치. 관리 역할은 <strong>AI 관리자</strong>, 보기 전용은 <strong>전역 읽기 권한자</strong>.</div>
  </div>
</div>

<p>에이전트 사용량에 대비한 <strong>종량제(PAYG) 청구</strong>는 Power Platform 관리 센터에서 Azure 구독과 리소스 그룹을 연결해 설정한다.</p>

<div class="mc-callout mc-callout--dark">
  <p><strong>한 번은 짚고 넘어가야 할 경계선</strong></p>
  <p>프롬프트와 응답은 Microsoft 365 서비스 경계 안에서 <strong>엔터프라이즈 데이터 보호(EDP)</strong>의 적용을 받는다. <strong>웹 검색 쿼리는 다르다.</strong> 관리자가 웹 검색을 켠 경우에만 경계 밖으로 나가며, 전체 프롬프트가 아닌 짧은 검색어 형태로 전달되고 사용자·테넌트 식별자는 제거된다. 쿼리 데이터는 Bing 개선이나 광고 프로필, 파운데이션 모델 학습에 사용되지 않는다. 다만 <strong>HIPAA·EUDB 준수는 웹 검색 쿼리에는 적용되지 않는다.</strong></p>
</div>

<hr/>

<h2 class="mc-section-title">5 · 데이터 과다공유: 켜기 전에 정리해야 할 것</h2>

<img src="/mwkorea/assets/images/20260827-copilot-readiness-checklist/img02.jpeg" alt="데이터 과다공유와 권한 관리" />
<p class="mc-card-note">그림 3. Copilot이 무엇을 볼 수 있는지는 결국 권한이 결정한다.</p>

<p>Copilot은 <strong>사용자의 권한을 그대로 따른다.</strong> 그래서 "Copilot이 이걸 어떻게 알았지?"라는 질문의 답은 대개 Copilot이 아니라 <strong>권한 설정</strong>에 있다. 출발점은 <a href="https://aka.ms/Copilot/SecureGovern">aka.ms/Copilot/SecureGovern</a>의 데이터 과다공유 블루프린트이며, 작업은 세 단계로 나뉜다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--red">
    <div class="mc-card-title"><strong>① 과다공유 개선</strong></div>
    <div>고위험 사이트와 콘텐츠의 과다공유를 정리한다.</div>
  </div>
  <div class="mc-card mc-card--red">
    <div class="mc-card-title"><strong>② 가드레일 구성</strong></div>
    <div>유출·내부 위험을 사전에 막는 통제를 설정한다.</div>
  </div>
  <div class="mc-card mc-card--red">
    <div class="mc-card-title"><strong>③ 규제 요구 충족</strong></div>
    <div>보존·감사 등 규제 요구 사항을 충족시킨다.</div>
  </div>
</div>

<p>실무적으로는 <strong>SharePoint 고급 관리의 데이터 접근 거버넌스 보고서</strong>로 과다 노출된 사이트를 식별하고, 사이트 접근 검토를 시작하며, SharePoint·OneDrive의 외부 공유 설정을 조직·사이트 단위로 정비한다. 이 보고서는 SharePoint 관리 센터의 <strong>보고서 &gt; 데이터 접근 거버넌스</strong>에서 열 수 있고, '조직 전체의 사이트 권한', '공유 링크', "외부 사용자를 제외한 모든 사람과 공유됨" 같은 항목으로 위험 사이트를 좁혀 준다.</p>

<p>여기에 <strong>Purview DSPM for AI</strong>(데이터 보안 태세 관리) 평가를 실행해 권고 사항을 적용하고, 보존·삭제 정책으로 노출 표면 자체를 줄인다. 통합 감사 로깅과 보존 설정도 함께 점검해야 한다.</p>

<hr/>

<h2 class="mc-section-title">6 · 그리고, 측정</h2>

<img src="/mwkorea/assets/images/20260827-copilot-readiness-checklist/img03.jpeg" alt="Copilot 준비도 보고서와 대시보드" />
<p class="mc-card-note">그림 4. 준비도 보고서와 대시보드가 도입 속도를 보여 준다.</p>

<p>마지막으로 남는 일은 <strong>"얼마나 쓰이는가"</strong>를 볼 수 있게 만드는 것이다. 관리 센터의 <strong>Copilot 준비도 보고서</strong>는 필수 라이선스 보유자, 적격 업데이트 채널 사용자, 라이선스 상태와 함께 <strong>'Copilot 추천 후보'</strong>를 보여 준다. 지난달 Microsoft 365 앱 사용량 기준 <strong>상위 25%의 미할당 사용자</strong>다. 라이선스를 어디에 먼저 줄지 고민할 때 가장 실용적인 출발점이다.</p>

<p><strong>Viva Insights의 Copilot 대시보드</strong>는 Entra ID의 관리자 계층 정보를 바탕으로 자동 할당되며, AI 관리자가 수동으로 부여할 수도 있다. 다만 데이터 처리가 시작되려면 Viva Insights 라이선스 또는 Copilot 라이선스(Viva Insights 서비스 플랜 포함)가 <strong>최소 50개</strong> 할당되어 있어야 하고, 할당 후 <strong>최대 7일</strong>이 걸린다. 파일럿 규모를 정할 때 미리 알아두면 좋은 숫자다.</p>

<hr/>

<h2 class="mc-section-title">정리하며</h2>

<div class="mc-callout mc-callout--dark">
  <p>Copilot 도입에서 실패하는 지점은 대개 모델이나 프롬프트가 아니라, <strong>채널이 반기 채널로 남아 있었고, CDN이 막혀 있었으며, 연결된 환경이 꺼져 있었고, 아무도 앱을 찾지 못했다</strong>는 훨씬 평범한 이유들이다.</p>
</div>

<p>모든 항목을 한 번에 다 할 필요는 없다. 다만 <strong>어떤 항목이 아직 열리지 않았는지는 알고 있어야 한다.</strong> 다음 회의 전에, 세 개의 트랙 가운데 우리 조직의 현재 위치를 함께 짚어 보시기를 권해 드린다.</p>

<hr/>

<h2 class="mc-section-title">함께 보면 좋은 자료</h2>

<div class="mc-table-wrap">
  <table>
    <thead>
      <tr><th>자료</th><th>쓰임새</th><th>링크</th></tr>
    </thead>
    <tbody>
      <tr><td>Microsoft 365 네트워크 연결 테스트 도구</td><td>배포 전 Copilot 연결·WebSocket 상태 진단</td><td><a href="https://learn.microsoft.com/en-us/microsoft-365/enterprise/office-365-network-mac-perf-onboarding-tool?view=o365-worldwide">connectivity.m365.cloud.microsoft</a></td></tr>
      <tr><td>연결 테스트 도구 안내 문서</td><td>테스트 단계와 결과 해석 방법</td><td><a href="https://learn.microsoft.com/en-us/microsoft-365/enterprise/office-365-network-mac-perf-onboarding-tool?view=o365-worldwide">learn.microsoft.com</a></td></tr>
      <tr><td>SharePoint 데이터 접근 거버넌스 보고서</td><td>과다 공유·과다 노출 사이트 식별</td><td><a href="https://learn.microsoft.com/en-us/sharepoint/data-access-governance-reports">learn.microsoft.com</a></td></tr>
      <tr><td>SharePoint 고급 관리(SAM) 개요</td><td>Copilot 대비 거버넌스 통제 전반</td><td><a href="https://learn.microsoft.com/en-us/sharepoint/advanced-management">learn.microsoft.com</a></td></tr>
      <tr><td>Copilot Success Kit</td><td>역할별 도입 가이드·기술 준비 가이드</td><td><a href="https://adoption.microsoft.com/en-us/copilot/success-kit/">adoption.microsoft.com</a></td></tr>
      <tr><td>Copilot Chat Success Kit</td><td>관리 제어·라이선스·온보딩 템플릿</td><td><a href="https://adoption.microsoft.com/en-us/copilot-chat/success-kit/">adoption.microsoft.com</a></td></tr>
      <tr><td>Copilot 도입 필수 가이드</td><td>단계별 구현 프레임워크</td><td><a href="https://adoption.microsoft.com/en-us/copilot/essential-guide/">adoption.microsoft.com</a></td></tr>
      <tr><td>Copilot Prompt Gallery</td><td>사용자 스킬링·바로 쓰는 프롬프트</td><td><a href="https://m365.cloud.microsoft/copilot-prompts">m365.cloud.microsoft</a></td></tr>
      <tr><td>Prompt Gallery 관리자 안내</td><td>아키텍처·데이터 흐름·규정 준수</td><td><a href="https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-prompt-gallery">learn.microsoft.com</a></td></tr>
    </tbody>
  </table>
</div>

</div>
