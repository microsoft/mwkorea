---
layout: single
title: "우리 조직의 Copilot, 제대로 쓰이고 있을까? — 오픈소스 CopilotWatchTower"
permalink: /hidden/copilot-watchtower/
author_profile: true
sitemap: false
search: false
excerpt: "관리자 PC 한 대에서 Microsoft Graph로 Copilot 사용량과 대화를 수집해 로컬에 저장하고, 컴플라이언스와 분석에 활용하는 오픈소스(MIT) 데스크톱 도구 CopilotWatchTower를 소개합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: false
toc_sticky: true
classes: wide
author: 최정우
---

<div class="monthlycopilot-page monthlycopilot-page--agent">
<div class="mc-issue-strip">Monthly Copilot · Open Source · CopilotWatchTower</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">Open Source Spotlight</div>
  <div class="mc-cover-title">우리 조직의 Copilot,<br/>제대로 쓰이고 있을까?</div>
  <div class="mc-cover-subtitle">관리자 PC 한 대로 시작하는 Copilot 사용량·대화 수집 도구 — CopilotWatchTower</div>
</div>

<div class="mc-card mc-card--blue">
  <div class="mc-card-title"><strong>Article Summary</strong></div>
  <div><strong>CopilotWatchTower</strong>는 테넌트 관리자를 위한 오픈소스(MIT) 데스크톱 도구입니다. 관리자 PC 한 대에서 <strong>Microsoft Graph</strong>로 Microsoft 365 Copilot의 사용량과 대화를 수집해 <strong>내 PC의 로컬 데이터베이스</strong>에 저장하고, 컴플라이언스와 분석에 활용합니다. "누가 얼마나 쓰는지, 어떤 앱에서 쓰는지, 라이선스가 낭비되는지"를 <strong>수치와 근거</strong>로 답할 수 있으며, 별도 서버나 외부 네트워크 포트가 필요 없습니다.</div>
</div>

<div class="mc-callout mc-callout--dark">
  <p><strong>⚠️ 컴플라이언스 주의</strong></p>
  <p>이 도구는 Copilot 대화 내용을 <strong>평문(원문 그대로)</strong>으로 읽습니다. eDiscovery, 내부 감사, 규제 대응 보존 등 <strong>법적·정책적 권한이 명확한 테넌트에서만</strong> 사용하세요. 도입 전 <strong>데이터 보호 영향 평가(DPIA)</strong>와 사내 데이터 취급 정책을 반드시 검토해야 합니다.</p>
</div>

<hr/>

<h2 class="mc-section-title">왜 필요할까요 — "우리 회사, Copilot으로 진짜 가치를 얻고 있나요?"</h2>

<p>Copilot을 도입한 뒤 관리자에게 돌아오는 질문은 대체로 비슷합니다. <strong>누가 얼마나 쓰는지</strong>, <strong>어떤 앱(Teams·Word 등)에서 쓰는지</strong>, 그리고 <strong>산 라이선스가 놀고 있지는 않은지</strong>. CopilotWatchTower는 이런 질문에 감이 아니라 <strong>숫자와 근거</strong>로 답하기 위한 관리자용 도구입니다. 무거운 인프라 없이 관리자 PC에서 바로 실행되는, 가볍고 안전한 데스크톱 앱입니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>최신 릴리스</strong></div>
    <div>v2.0.0 · MIT License</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>지원 환경</strong></div>
    <div>Windows 10/11 (x64)</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>구성</strong></div>
    <div>Electron + React · 로컬 전용(Local only)</div>
  </div>
</div>

<hr/>

<h2 class="mc-section-title">설치부터 분석까지, 하나의 도구로 — 핵심 기능 5가지</h2>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>🪄 사전 앱 등록 불필요</strong></div>
    <div>첫 실행 시 마법사가 <strong>디바이스 코드 로그인</strong>으로 Entra ID 앱을 자동 등록하고, 필요한 Graph 권한 부여와 관리자 동의까지 단계별로 안내합니다.</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>🎯 4가지 수집 범위</strong></div>
    <div>LICENSED(라이선스 보유자), ALL_ACTIVE(모든 활성 사용자), GROUP(특정 그룹), CUSTOM(지정 UPN) 모드를 지원합니다.</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>🔁 안전한 증분 수집</strong></div>
    <div>사용자별 워터마크, Retry-After 준수, 지수 백오프, 멱등 upsert로 중간에 멈췄다 다시 돌려도 데이터가 중복되지 않습니다.</div>
  </div>
  <div class="mc-card mc-card--green">
    <div class="mc-card-title"><strong>🔒 로컬 전용 저장</strong></div>
    <div>모든 데이터는 내 PC의 <strong>SQLite</strong>(%LOCALAPPDATA%)에 저장됩니다. 대화 본문 전체에 대한 <strong>FTS5 전문 검색</strong>을 지원합니다.</div>
  </div>
  <div class="mc-card mc-card--amber">
    <div class="mc-card-title"><strong>📊 모던 Electron UI</strong></div>
    <div>대시보드(KPI+차트), 대화 탐색, 실시간 수집 로그 모니터링, CSV/JSON/XLSX 내보내기를 제공합니다.</div>
  </div>
</div>

<hr/>

<h2 class="mc-section-title">무엇을, 어떤 기술로, 어떤 권한으로 수집하나요</h2>

<p>수집 소스마다 사용하는 기술, 필요한 권한, 제약이 다릅니다. 앱의 <strong>데이터 수집 → 개요</strong> 화면에서 동일한 내용을 확인할 수 있습니다.</p>

<div class="mc-table-wrap">
<table>
  <thead>
    <tr>
      <th>소스</th>
      <th>기술</th>
      <th>주요 수집 데이터</th>
      <th>필요 권한</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>💬 대화 수집 (API)</td>
      <td>Microsoft Graph(beta) · getAllEnterpriseInteractions · 앱 전용(client credentials) 토큰</td>
      <td>프롬프트/응답 본문, 앱 출처(BizChat·Word·Teams·Excel·PowerPoint·Outlook·Loop 등), 첨부·링크·멘션 메타데이터, 원본 JSON</td>
      <td>AiEnterpriseInteraction.Read.All · User.Read.All · Organization.Read.All</td>
    </tr>
    <tr>
      <td>🤝 대화 수집 (e-Discovery)</td>
      <td>Purview eDiscovery(Graph) · 위임 인증</td>
      <td>라이선스 미보유 사용자를 포함한 Copilot 대화 본문, 케이스·검색·내보내기 결과에서 복원한 메시지</td>
      <td>eDiscovery.ReadWrite.All(위임) · eDiscovery Manager 역할</td>
    </tr>
    <tr>
      <td>🤖 대화 수집 (Teams)</td>
      <td>Dataverse 자동 로그인(웹 자동화) · 트랜스크립트 테이블</td>
      <td>Copilot Studio 커스텀 에이전트의 Teams 대화 기록(트랜스크립트), 에이전트·환경별 대화 세션</td>
      <td>Dataverse System Administrator(환경별) · PPAC 자동 로그인 계정</td>
    </tr>
    <tr>
      <td>🧩 에이전트</td>
      <td>Microsoft Graph Copilot 관리 API(에이전트 등록·카탈로그) + 감사 로그</td>
      <td>에이전트 인벤토리(등록 정보·카탈로그 패키지), 정책 구성 신호, 감사 로그 기반 실사용 신호</td>
      <td>AgentRegistration.Read.All · CopilotPackages.Read.All · CopilotPolicySettings.Read</td>
    </tr>
    <tr>
      <td>🪙 Power Platform 크레딧</td>
      <td>Power Platform 관리 센터(PPAC) 자동 로그인 · 소비 보고서 다운로드</td>
      <td>Copilot Studio 메시지 소비, AI Builder 크레딧 소비, Power Platform 요청(API) 소비</td>
      <td>Power Platform Administrator · PPAC 자동 로그인 계정</td>
    </tr>
    <tr>
      <td>🛡️ 감사 이벤트</td>
      <td>Graph security.auditLog.queries(비동기 Purview 통합 로그) + Entra 감사/로그인</td>
      <td>차단·거부 등 보안 이벤트, 민감 자료 접근 기록, 접근·정책 관련 감사 이벤트</td>
      <td>AuditLog.Read.All · AuditLogsQuery.Read.All · Purview/Exchange roleManagement</td>
    </tr>
    <tr>
      <td>📈 공식 사용량</td>
      <td>Microsoft Graph Reports API(Copilot 사용 CSV)</td>
      <td>공식 M365 Copilot 사용 보고서 스냅샷, 기간별(D7/D30/D90/D180) 사용 집계</td>
      <td>Reports.Read.All · ReportSettings.ReadWrite.All</td>
    </tr>
  </tbody>
</table>
</div>

<div class="mc-callout mc-card--blue">
  <strong>참고 —</strong> API 경로는 Copilot 라이선스 보유자를 대상으로 하며, 라이선스가 없는 사용자의 대화 본문은 <strong>eDiscovery 경로</strong>로 별도 복원합니다. eDiscovery·Teams·Power Platform·감사 경로는 비동기 단계(케이스 생성 → 검색 → 추정 → 내보내기 → 다운로드)로 진행되며, 중단되더라도 <strong>단계별 이어하기</strong>가 가능합니다.
</div>

<hr/>

<h2 class="mc-section-title">실제 화면 미리보기</h2>

<h3>대시보드 — 전체 사용 현황을 한눈에</h3>
<p>활성 사용자, 총 스레드·메시지·프롬프트, 의미 있는 상호작용, 라이선스 미활성 사용자 등 핵심 지표(KPI)와 함께 최근 30일 사용 추이 그래프, 상위 사용자 TOP 5를 보여줍니다.</p>
<img src="/mwkorea/assets/images/20260719-copilot-watchtower/01-dashboard.png" alt="CopilotWatchTower 대시보드 화면 — 활성 사용자·총 턴·의미있는 상호작용·라이선스 미활성 KPI 카드, 최근 30일 Copilot 사용 추이 그래프, 상위 사용자 TOP 5" />

<h3>사용 인사이트 — 사용자·날짜·앱별 상세 분석</h3>
<p>기간·사용자·앱 단위로 Copilot 활동을 필터링해 분석합니다. 날짜별 스레드·메시지 추이, 앱별 메시지 분포, 사용자별 요약 표를 제공합니다.</p>
<img src="/mwkorea/assets/images/20260719-copilot-watchtower/02-usage-insights.png" alt="CopilotWatchTower 사용 인사이트 화면 — 기간·사용자·앱 필터, 날짜별 스레드/메시지 추이 그래프와 앱별 메시지 막대그래프, 사용자 요약과 일자별 상세 표" />

<h3>대화 탐색 — 실제 대화 기록 확인</h3>
<p>Graph API로 수집한 운영 대화 기록을 제목·본문으로 검색하고, 사용자·앱으로 필터링해 개별 대화의 전체 내용을 확인합니다. 관련 감사 이벤트와 함께 Markdown 등으로 내보낼 수 있습니다.</p>
<img src="/mwkorea/assets/images/20260719-copilot-watchtower/03-conversations.png" alt="CopilotWatchTower 대화 탐색 화면 — 왼쪽 스레드 목록과 오른쪽 대화 상세의 프롬프트·응답 타임라인, Markdown 내보내기" />

<hr/>

<h2 class="mc-section-title">지금 시작하기</h2>

<p>Releases 페이지에서 <code>CopilotWatchTower-x.y.z-setup.zip</code>을 내려받아 압축을 풀고, 설치 배치 파일을 관리자 권한으로 실행하면 됩니다.</p>

<div class="mc-card-grid mc-card-grid--3">
  <div class="mc-card mc-card--blue">
    <div class="mc-card-title"><strong>STEP 1</strong></div>
    <div>setup.zip 다운로드 후 압축 해제</div>
  </div>
  <div class="mc-card mc-card--teal">
    <div class="mc-card-title"><strong>STEP 2</strong></div>
    <div>Install-CopilotWatchTower.bat을 관리자 권한으로 실행(인증서 신뢰 + 앱 설치)</div>
  </div>
  <div class="mc-card mc-card--purple">
    <div class="mc-card-title"><strong>STEP 3</strong></div>
    <div>앱을 실행한 뒤 온보딩 마법사로 테넌트 연결</div>
  </div>
</div>

<div class="mc-callout mc-card--amber">
  자체 서명 인증서를 사용하므로 설치 전에 <strong>인증서 신뢰 등록</strong>이 필요합니다. 자세한 절차는 압축 파일 안의 INSTALL.txt를 참고하세요.
</div>

<h3>개발자라면 — 소스에서 바로 실행</h3>
<p>Python 3.11+ 가상 환경에서 편집 가능(editable) 모드로 설치하면 바로 실행할 수 있습니다.</p>

```powershell
# 1. Python 3.11+ 가상 환경 생성
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
# 2. 개발 의존성 포함 편집 가능 설치
pip install -e ".[dev]"
# 3. 실행
copilot-watchtower
```

<hr/>

<div class="mc-callout mc-callout--dark">
  <div style="font-weight: 800; margin-bottom: 0.5rem; font-size: 1.05rem;">함께 만드는 오픈소스</div>
  <div>사용 중 떠오른 질문, 새 기능 제안, 버그 리포트는 GitHub 이슈 보드에 남겨 주세요. 바로가기: <a href="https://aka.ms/cpwt" style="color:#93c5fd;">aka.ms/cpwt</a> · <a href="https://github.com/microsoft/CopilotWatchTower" style="color:#93c5fd;">GitHub 저장소</a> · <a href="https://github.com/microsoft/CopilotWatchTower/releases/latest" style="color:#93c5fd;">최신 릴리스</a> · <a href="https://github.com/microsoft/CopilotWatchTower/issues" style="color:#93c5fd;">이슈 보드</a></div>
  <div style="margin-top: 0.8rem; font-size: 0.92rem; color: #9ca3af;">© 2026 Microsoft · CopilotWatchTower · MIT License</div>
</div>

</div>
