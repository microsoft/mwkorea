---
layout: single
title: "방탈출로 탈출한 건 Copilot의 한계였다"
permalink: /hidden/escape-room-copilot/
excerpt: "Microsoft AI Tour 2026 CPS 부스에서 Copilot Studio 에이전트를 탑재한 웹 기반 방탈출 게임이 탄생했습니다. Direct Line API와 Azure Static Web Apps로 구현한 기술 스택부터 현장 방문자들의 뜨거운 반응까지, Gamification으로 Copilot Studio 채널 배포의 가능성을 증명한 팀의 이야기입니다."
tags:
  - Copilot Studio
  - AI Tour
  - Gamification
  - Direct Line API
categories:
  - Copilot
author_profile: true
sitemap: false
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
classes: wide
toc: false
toc_sticky: true
author: 최정우
---

<div class="monthlycopilot-page monthlycopilot-page--tour">
<div class="mc-issue-strip">Monthly Copilot · April 2026 · 월간 코파일럿 4월호 · Behind the Scene</div>

<div class="mc-cover">
  <div class="mc-cover-kicker">Behind the Scene</div>
  <div class="mc-cover-title">방탈출로 탈출한 건 Copilot의 한계였다</div>
  <div class="mc-cover-subtitle">Microsoft AI Tour 2026, CPS 부스에서 방탈출 게임으로<br/>Copilot Studio의 가능성을 증명한 팀의 이야기</div>
</div>

<div style="margin: 0 0 1.3rem; padding: 1rem 1.1rem; border-radius: 16px; background: linear-gradient(135deg, #ecfeff 0%, #f8fafc 100%); border: 1px solid #99f6e4; color: #1f2937;">
  <div style="font-weight: 800; color: #0f766e; margin-bottom: 0.35rem;">Article Summary</div>
  <div style="line-height: 1.85;">COEX를 가득 메운 Microsoft AI Tour 2026 현장. 수십 개의 부스 사이에서 유독 긴 줄이 늘어선 곳이 있었다. 슬라이드 발표도, 영상 데모도 아닌 — 방탈출 게임이었다. Copilot Studio 에이전트를 탑재한 웹 기반 방탈출 게임을 만든 팀의 기획, 기술, 그리고 현장 반응까지 담았다.</div>
</div>

<div style="margin: 0 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.45rem; color: #0f766e;">핵심 키워드</div>
  <div style="line-height: 1.8; color: #374151;">채널 배포 · Gamification · Direct Line API · Copilot Studio · Azure Static Web Apps · 커스텀 웹사이트</div>
</div>

<img src="/mwkorea/assets/images/20260416-escape-room/image1.jpeg" alt="AI Tour 2026 Copilot Studio 부스 현장" style="border-radius: 12px; margin-bottom: 1.4rem;" />

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #0f766e; background: #f8fafc;">문제의 시작: "어떻게 하면 사람들이 진짜로 경험하게 할 수 있을까?"</h2>

<p>AI Tour CPS(Copilot Studio) 부스는 단독 콘텐츠를 추가로 운영할 수 있는 기회를 얻었다. 그 기회 앞에서 팀이 던진 질문은 하나였다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a; font-weight: 700; line-height: 1.85;">
  "슬라이드와 동영상으로는 Copilot Studio의 가능성을 제대로 전달하기 어렵다. 사람들이 직접 손으로 만지고, 눈으로 보고, 느끼게 하려면?"
</div>

<p>답은 뜻밖의 곳에서 나왔다. 팀원 중 방탈출 고인물이 있었던 것이다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f5f3ff; border: 1px solid #c4b5fd; color: #5b21b6; font-weight: 700; line-height: 1.85;">
  "방탈출이야말로 가장 확실한 인터랙티브 포맷이라고 생각했어요. Gamification을 통해 흥미를 유발하면서, 동시에 Copilot Studio가 실제로 어떻게 작동하는지를 자연스럽게 보여줄 수 있으니까요."
</div>

<p>그렇게 탄생한 것이 바로 <strong>aka.ms/aitourcpsbooth</strong> — Copilot Studio 에이전트를 탑재한 웹 기반 방탈출 게임이다.</p>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">기획의 핵심: 단순한 게임이 아니라 "채널 배포"의 증명</h2>

<p>이 프로젝트의 목적은 두 가지였다. 사용자의 흥미를 유발하는 것, 그리고 Copilot Studio 에이전트가 커스텀 웹사이트에 탑재될 수 있다는 <strong>채널 배포의 가능성</strong>을 실제로 보여주는 것.</p>

<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem; border-radius: 14px; background: #ecfeff; border: 1px solid #99f6e4; color: #115e59;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">목적 1</div>
    <div>Gamification으로 사용자 흥미 유발</div>
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #fff7ed; border: 1px solid #fdba74; color: #c2410c;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">목적 2</div>
    <div>커스텀 웹사이트 채널 배포의 실증</div>
  </div>
</div>

<p>게임은 <strong>2-Stage 구조</strong>로 설계됐다. 현실의 방탈출처럼 첫 번째 방을 통과하면 두 번째 방으로 넘어가는 구조이며, 동시에 두 팀원 간의 업무 분담을 자연스럽게 나눌 수 있는 장치이기도 했다.</p>

<img src="/mwkorea/assets/images/20260416-escape-room/image2.jpeg" alt="방탈출 게임 화면 - Copilot Studio 에이전트 탑재" style="border-radius: 12px; margin-bottom: 1.4rem;" />

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #1d4ed8; background: #f8fafc;">기술 스택: Copilot Studio가 게임의 두뇌가 되다</h2>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a; font-weight: 700; line-height: 1.85;">
  "Copilot Studio로 에이전트를 만들면 빠르게 만들 수 있고, Teams 채널 연결도 간편하다는 걸 이미 알고 있었어요. 이번엔 웹사이트와의 연동에 도전한 거죠."
</div>

<p>게임의 핵심 AI 동작은 <strong>WebSocket + Direct Line API</strong> 기반으로 구현됐다. 플레이어가 게임을 진행하면, 웹사이트는 현재 스테이지 레벨과 수집한 힌트 개수 등 여러 Global 변수를 Payload로 CPS 에이전트에 전달한다.</p>

<p>에이전트는 이 Context를 받아 두 가지 Topic을 활용한다.</p>

<div style="display: grid; grid-template-columns: 1fr; gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #ecfeff; border: 1px solid #99f6e4; color: #115e59;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">상태 동기화용 Topic</div>
    <div>현재 게임 상태를 에이전트에 주입</div>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1d4ed8;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">추론용 Topic</div>
    <div>플레이어의 현재 상황에 맞는 힌트를 생성</div>
  </div>
</div>

<p>단순히 힌트 개수만 참고하는 게 아니라 다양한 Global 변수를 종합적으로 고려해 에이전트가 맥락에 맞는 답변을 내놓는다. 그 결과, 플레이어는 막힌 구간에서 자연스럽게 AI에게 도움을 요청하고, AI는 게임의 흐름을 읽어 적절한 힌트를 건넨다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #dbe4f0; color: #111827;">
  <div style="font-weight: 800; margin-bottom: 0.45rem; color: #1d4ed8;">배포 환경</div>
  <div style="line-height: 1.8; color: #374151;">배포는 <strong>Azure Static Web Apps(ASW)</strong>를 활용했다. React 기반 TypeScript 웹앱을 GitHub에 올리고, Azure Static Web Apps와 연결해 동기화 방식으로 배포하는 구조다.</div>
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #7c3aed; background: #f8fafc;">AI가 AI를 만들다: Copilot이 제작에도 참여한 방식</h2>

<p>이 게임을 만들면서 팀은 AI를 협업 파트너로 적극 활용했다. Ideation은 사람이 직접 했지만, 기본 스테이지 구성과 UI/UX 프레임워크는 AI의 힘을 빌렸다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f5f3ff; border: 1px solid #c4b5fd; color: #5b21b6; font-weight: 700; line-height: 1.85;">
  "기본 UI/UX는 Antigravity로 제작하고, 스테이지 및 인증서 페이지 개발에는 Codex와 함께했어요. 다만 CPS 에이전트의 분기 로직은 전부 직접 수정했습니다. AI가 생각보다 마음에 안 드는 부분이 있더라고요."
</div>

<p>촉박한 행사 데드라인 안에서 아이디어에서 완성까지 빠르게 진행할 수 있었던 데는, AI와의 협업이 결정적인 역할을 했다. 그리고 그 경험은 팀에게 중요한 교훈을 남겼다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #fefce8; border: 1px solid #fde68a; color: #854d0e; font-weight: 700; line-height: 1.85;">
  🔑 "AI는 빠른 조력자이지만, 에이전트의 핵심 로직과 최종 결정은 여전히 사람이 해야 합니다."
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #ea580c; background: #f8fafc;">AI Tour 현장: "생각보다 어렵던데요?" — 그리고 "어떻게 만들었어요?"</h2>

<p>행사 당일 부스에는 30대 초반의 IT 직군 방문자들이 특히 열심히 참여했다. 게임을 마친 이들이 가장 많이 한 말은 두 가지였다.</p>

<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem; border-radius: 14px; background: #fff7ed; border: 1px solid #fdba74; color: #9a3412;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">반응 1</div>
    <div>"게임이 생각보다 어렵다"</div>
  </div>
  <div style="padding: 1rem; border-radius: 14px; background: #ecfdf5; border: 1px solid #86efac; color: #166534;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">반응 2</div>
    <div>"Copilot Studio로 에이전트는 어떻게 만드나요?"</div>
  </div>
</div>

<p>그리고 팀이 가장 기억에 남는 한마디.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); border: 1px solid #93c5fd; color: #1e3a8a; font-weight: 700; line-height: 1.85; font-size: 1.05rem;">
  "와, Copilot Studio로 만든 에이전트가 웹사이트에 붙는 줄은 몰랐네요."
</div>

<p>이 한 문장은 이 프로젝트가 달성하고자 했던 목표 그 자체였다. 에이전트를 Teams나 정해진 채널에만 배포하는 것이 아니라, 직접 만든 웹사이트에 자연스럽게 녹아들 수 있다는 것 — 많은 이들이 미처 알지 못했던 Copilot Studio의 가능성이 현장에서 생생하게 증명된 순간이었다.</p>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #0891b2; background: #f8fafc;">🧑‍💻 제작 팀</h2>

<div style="display: grid; grid-template-columns: 1fr; gap: 14px; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #ecfeff; border: 1px solid #99f6e4; color: #115e59;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">이영서 매니저</div>
    <div>Next.js 기반 UI/상태관리/시나리오 인터랙션 & 스테이지 1 & ASW 배포</div>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1d4ed8;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">김유연 매니저</div>
    <div>시나리오 기획, UX 및 스테이지 2, 인증서 구현 & CPS 에이전트 전송 로직</div>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 14px; background: #f5f3ff; border: 1px solid #c4b5fd; color: #5b21b6;">
    <div style="font-weight: 800; margin-bottom: 0.35rem;">최치원 매니저</div>
    <div>기술 코칭</div>
  </div>
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #059669; background: #f8fafc;">👉 지금 바로 체험해보세요</h2>

<p>이 방탈출 게임은 지금도 공개되어 있습니다.</p>

<div style="margin: 1rem 0 1.4rem; padding: 1.15rem 1.2rem; border-radius: 16px; background: linear-gradient(135deg, #ecfeff 0%, #cffafe 100%); border: 1px solid #67e8f9; text-align: center;">
  <a href="https://aka.ms/aitourcpsbooth" target="_blank" style="font-size: 1.3rem; font-weight: 800; color: #0f766e; text-decoration: none;">🎮 aka.ms/aitourcpsbooth</a>
</div>

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a; font-weight: 700; line-height: 1.85;">
  팀의 추천 플레이 방법: "에이전트가 제공하는 단계 안내와 힌트를 적극 활용해서 게임을 돌파해보세요. 그 과정에서 Copilot Studio 에이전트가 어떻게 상황을 읽고 답변을 생성하는지, 자연스럽게 느끼실 수 있을 거예요."
</div>

<hr/>

<div style="margin: 1rem 0 0; padding: 1.15rem 1.2rem; border-radius: 18px; background: linear-gradient(135deg, #111827 0%, #1f2937 100%); color: #f9fafb; line-height: 1.85;">
  <div style="font-weight: 800; margin-bottom: 0.5rem; font-size: 1.05rem;">🎯 한 줄 요약</div>
  "방탈출을 탈출하는 건 플레이어지만, 한계를 탈출한 건 Copilot Studio였다."
  <div style="margin-top: 0.8rem; font-size: 0.92rem; color: #9ca3af;">이 기사는 Copilot Studio가 슬라이드 밖으로 나와 현실과 만나는 순간을 담은 생생한 현장 기록입니다. 월간 코파일럿은 앞으로도 AI와 함께 만들어가는 혁신의 현장을 여러분께 전하겠습니다.</div>
</div>

</div>
