---
title: "API 밖의 웹 업무까지: Copilot Studio의 GitHub Copilot Harness 기반 Computer Use"
date: 2026-10-20T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - ComputerUse
  - GitHubCopilot
  - Agents
  - WebAutomation
excerpt: "Copilot Studio 에이전트가 자연어 지시로 웹을 탐색하고 정보를 추출하며 파일을 다운로드하는 Computer Use 기능을 예고했습니다. GitHub Copilot Harness 기반이라는 발표의 의미와 2026년 11월 프리뷰 일정을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# API 밖의 웹 업무까지: Copilot Studio의 GitHub Copilot Harness 기반 Computer Use

업무에 필요한 정보가 항상 구성된 지식 원본이나 API로 제공되지는 않습니다. 웹사이트를 열어 자료를 찾고 파일을 내려받아 다른 도구에서 처리하는 일이 여전히 남아 있습니다.

Microsoft는 **GitHub Copilot Harness 기반의 웹 탐색 Computer Use**를 Copilot Studio 에이전트의 기본 기능으로 제공하는 로드맵을 공개했습니다. 웹에서 확보한 정보와 파일을 다른 도구와 연결해 전체 업무 흐름을 수행하도록 범위를 넓히는 방향입니다.

---

## 자연어로 웹 탐색과 정보 수집

원문은 에이전트가 자연어 지시에 따라 다음 작업을 수행하도록 지원한다고 설명합니다.

- 웹페이지 탐색
- 웹사이트와 상호작용
- 정보 추출
- 파일 다운로드
- 수집한 정보와 파일을 다른 도구와 함께 사용

핵심은 단순히 페이지를 읽는 데서 끝나지 않는다는 것입니다. 웹에서 자료를 확보한 뒤 후속 도구를 사용해 **종단 간 워크플로**를 수행하는 방향이 제시됩니다.

## GitHub Copilot Harness와 Copilot Studio의 관계

로드맵은 이 기능이 **GitHub Copilot Harness로 구동된다**고 명시합니다. 다만 공개 설명에는 내부 실행 구조나 별도 GitHub Copilot 라이선스 필요 여부가 제시되어 있지 않습니다.

따라서 이 발표를 GitHub 저장소를 반드시 연결해야 한다거나, 특정 개발자 구독이 필수라는 뜻으로 해석해서는 안 됩니다. 반대로 별도 비용이 없다고 단정할 근거도 없습니다.

## 어떤 흐름을 검토할 수 있을까요?

예를 들어 웹에서 공개 자료를 찾아 파일을 내려받은 뒤, 다른 도구로 내용을 정리하는 흐름을 생각해 볼 수 있습니다. 이는 원문의 기능 설명을 바탕으로 한 **활용 예시**이며 미리 제공되는 템플릿이라는 의미는 아닙니다.

원문은 기존에 구성한 지식 원본과 API 기반 통합을 넘어 에이전트의 활동 범위를 확장한다고 설명합니다. 그렇다고 기존 API 연결을 모두 웹 자동화로 바꿔야 한다는 뜻은 아닙니다. 안정적인 API가 있는 업무와 화면 상호작용이 필요한 업무를 구분해 설계하는 편이 좋습니다.

## 일정과 아직 공개되지 않은 사항

| 항목 | 로드맵 내용 |
|---|---|
| 상태 | In development |
| 프리뷰 예정 | 2026년 11월 |
| GA 예정 | 2027년 1월 |
| 플랫폼 | Web |
| 클라우드 | Worldwide (Standard Multi-Tenant) |

인증이 필요한 사이트 지원 범위, 다운로드 제한, 실행 환경, 사용량·과금, 오류 복구 방식은 이 원문에 나와 있지 않습니다. 운영 설계는 해당 세부사항을 확인한 뒤 확정해야 합니다.

## 도입 체크포인트

한국 조직의 메이커와 관리자는 허용할 사이트, 다룰 데이터, 다운로드 파일의 저장 위치, 외부 사이트에서 변경을 일으키는 작업의 승인 기준을 미리 정리하면 좋습니다. 웹페이지의 내용을 읽는 과정에서 에이전트 지시와 외부 콘텐츠를 구분하는 안전성도 검증 대상입니다.

이 항목들은 도입 시 검토 제안입니다. 원문이 관련 관리 옵션을 모두 기본 제공한다고 발표한 것은 아닙니다.

## 마무리

이번 로드맵은 에이전트가 **웹에서 직접 자료를 확보하고 다른 도구로 업무를 이어가는 방향**을 보여줍니다. 프리뷰 이후에는 실제 지원 범위와 운영 통제를 확인하면서 위험이 낮은 수집 업무부터 검증하는 접근이 적절합니다.

> **출처**: 원문 ID **RM576272**, [Copilot Studio: Computer Use for web browsing on GitHub Copilot Harness](https://mc.merill.net/message/RM576272) · [Microsoft 365 Roadmap 576272](https://www.microsoft.com/en-us/microsoft-365/roadmap?filters=&searchterms=576272). 실제 출시 일정·기능은 변경될 수 있습니다.
