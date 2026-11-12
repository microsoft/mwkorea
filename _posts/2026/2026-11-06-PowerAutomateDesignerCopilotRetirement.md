---
title: "11월 30일 Power Automate 디자이너의 Copilot 지원 종료: 기존 플로는 유지됩니다"
date: 2026-11-06T00:00:00 KST
categories:
  - Copilot
tags:
  - PowerAutomate
  - CopilotStudio
  - GitHubCopilot
  - MCP
  - CloudFlows
excerpt: "2026년 11월 30일 클라우드 플로와 에이전트 플로 디자이너의 Copilot 지원이 종료됩니다. 기존 플로는 삭제되거나 변경되지 않으며, 자연어 개발을 이어가는 대안과 사용자 안내 포인트를 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 11월 30일 Power Automate 디자이너의 Copilot 지원 종료: 기존 플로는 유지됩니다

Power Automate와 Copilot Studio로 자동화를 만드는 분들이 확인해야 할 지원 종료 공지가 나왔습니다. Microsoft의 MC1540258에 따르면 **2026년 11월 30일 클라우드 플로 또는 에이전트 플로 디자이너 안의 Copilot 지원이 종료**됩니다.

가장 중요한 구분은 자동화 자체의 종료가 아니라는 점입니다. **Copilot으로 만들거나 수정한 것을 포함해 기존 플로는 삭제·이동·변경되지 않습니다.** 영향을 받는 것은 디자이너에서 Copilot을 이용하는 제작 경험입니다.

---

## 종료되는 것과 유지되는 것

| 구분 | 공지 내용 |
|---|---|
| 디자이너 내 Copilot | 지원 종료 후 클라우드 플로·에이전트 플로 디자이너에서 사용할 수 없음 |
| 기존 플로 | 이번 폐지로 삭제되거나 이동·변경되지 않음 |
| 디자이너 사용 | 플로 생성·편집·테스트·실행 계속 가능 |
| 템플릿 | 템플릿에서 플로 만들기 계속 가능 |
| 수식과 문제 해결 | 수식 편집기, 플로 검사기, 실행 기록 계속 활용 가능 |

따라서 이번 공지만을 이유로 운영 중인 플로를 모두 재작성할 필요가 있다고 안내해서는 안 됩니다.

## 자연어로 계속 만들려면

Microsoft는 자연어로 플로를 만들고 수정하는 대안으로 다음 경로를 안내합니다.

- GitHub Copilot 등 지원되는 AI 도우미의 [Power Automate 플러그인](https://aka.ms/ADO18366a)
- [MCP를 통해 Microsoft Copilot Studio에 연결](https://aka.ms/ADO18366b)

이 두 경로는 원문이 제시한 대안입니다. 기존 디자이너의 대화나 설정이 자동 이관된다고 공지한 것은 아니며, 지원 환경과 연결 조건은 각 연결 문서에서 확인해야 합니다.

## 메이커와 교육 담당자가 준비할 일

우선 Power Automate 및 Copilot Studio 사용자에게 지원 종료일과 영향 범위를 알리는 것이 공지의 권고입니다. 내부 교육에서 디자이너 Copilot 버튼을 이용하는 과정을 안내하고 있다면 해당 부분을 점검하는 것이 좋습니다.

업무 중단을 피하려면 자연어 보조 없이도 디자이너에서 편집·테스트하고, 수식 편집기와 실행 기록으로 문제를 분석하는 흐름을 함께 안내하세요. 자연어 개발이 중요한 팀은 지원되는 대안의 접근 조건을 별도로 확인할 필요가 있습니다.

## 플로 운영과 제작 도구 전환을 나누어 보세요

이번 변경은 기존 자동화 자산의 폐지가 아니라 제작 보조 인터페이스의 지원 종료입니다. 운영팀은 기존 플로의 연속성을, 메이커 지원팀은 자연어 개발 경로와 교육 자료의 전환을 각각 관리하면 혼선을 줄일 수 있습니다.

> 출처: **MC1540258 — Power Automate - Information regarding the end of support for Copilot in the designer for cloud flows or agent flows.**  
> [Message Center 원문](https://mc.merill.net/message/MC1540258) · [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)  
> 지원 종료 공지에는 개별 Roadmap ID가 명시되어 있지 않습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
