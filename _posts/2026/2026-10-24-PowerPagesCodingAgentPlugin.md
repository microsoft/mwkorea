---
title: "Power Pages의 기존 사이트도 AI 코딩 에이전트로: Copilot CLI·Claude Code 플러그인"
date: 2026-10-24T00:00:00 KST
categories:
  - Copilot
tags:
  - PowerPages
  - GitHubCopilot
  - ClaudeCode
  - PowerPlatformCLI
excerpt: "Power Pages 플러그인이 GitHub Copilot CLI와 Claude Code에서 전통적인 비-SPA 사이트 생성·편집을 지원하는 방향을 안내했습니다. 페이지와 템플릿뿐 아니라 폼·목록·권한 메타데이터를 다루므로 변경 검토와 환경별 배포 통제가 중요합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Power Pages의 기존 사이트도 AI 코딩 에이전트로: Copilot CLI·Claude Code 플러그인

Power Pages를 사용하는 조직에는 이미 운영 중인 전통적인 사이트가 많습니다. AI 개발 지원이 새로운 단일 페이지 앱에만 머문다면 기존 사이트 유지보수에는 활용 범위가 좁을 수밖에 없습니다.

RM577900은 **GitHub Copilot CLI와 Claude Code용 Power Pages 플러그인의 전통적 비-SPA 사이트 지원**을 안내합니다. 자연어 요청으로 사이트를 생성하거나 기존 메타데이터를 내려받아 수정하는 개발 흐름입니다.

---

## 어떤 작업을 지원하나요?

개발자는 AI 코딩 에이전트에 자연어로 요청해 새 전통적 사이트를 만들거나, 기존 사이트 메타데이터를 다운로드하고 검토·수정할 수 있습니다. 원문에 명시된 범위는 다음과 같습니다.

| 영역 | 메타데이터 예 |
|---|---|
| 콘텐츠 | 웹 페이지, 웹 템플릿, 콘텐츠 조각 |
| 입력 화면 | 기본 폼, 다단계 폼 |
| 데이터 표시 | 목록 |
| 접근 제어 | 테이블 권한, 웹 역할 |
| 구성 | 사이트 설정 |

변경 사항은 **Power Platform CLI를 이용해 환경에 다시 업로드**하는 흐름으로 설명됩니다.

## 자연어로 바꾼다고 검토가 사라지는 것은 아닙니다

특히 테이블 권한과 웹 역할은 화면 표현이 아니라 데이터 접근에 영향을 줍니다. 생성된 변경을 그대로 운영에 반영하기보다는 변경 내역과 테스트 환경에서의 권한 동작을 확인해야 합니다.

국내 개발팀에서는 콘텐츠 수정과 권한 수정을 구분하고, 버전 관리 및 배포 검토 과정에 AI가 만든 메타데이터 변경을 포함하는 것이 좋습니다. 이 권고는 원문이 자동 승인·배포 기능을 제공한다는 의미는 아닙니다.

## 일정은 계획으로 읽어야 합니다

원문에는 Preview **2026년 10월**, GA **2026년 11월**이 기재되어 있으며 상태는 **In development**입니다. 본문에 “now supports”라는 표현이 있더라도, 이 정보만으로 전체 일반 공급이 완료됐다고 단정하면 안 됩니다.

또한 원문은 구체적인 설치 명령이나 플러그인 버전을 제공하지 않습니다. 실제 적용 시 사용하는 CLI·플러그인의 문서와 환경 지원 여부를 확인해야 합니다.

## 마무리

이번 지원의 의미는 기존 Power Pages 자산도 AI 코딩 에이전트의 개발 흐름에 포함된다는 데 있습니다. 생산성을 높이되, 데이터 권한과 환경 업로드의 통제는 기존 개발 프로세스 안에 유지하는 것이 중요합니다.

> **출처**: 원문 ID [RM577900](https://mc.merill.net/message/RM577900) · [Microsoft 365 Roadmap 577900](https://www.microsoft.com/microsoft-365/roadmap?id=577900)  
> 실제 출시 일정·기능은 변경될 수 있습니다.
