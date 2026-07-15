---
title: "내가 만든 Skill이 SharePoint와 OneDrive를 따라다닙니다: Personal Skills"
date: 2026-07-15T00:00:00 KST
categories:
  - Copilot
tags:
  - SharePoint
  - OneDrive
  - CopilotInSharePoint
  - PersonalSkills
  - AgentSkills
  - Markdown
excerpt: "Copilot in SharePoint에서 개인 Skill을 만들고 SharePoint 사이트와 OneDrive 어디서나 재사용할 수 있게 됩니다. Skill은 사용자의 OneDrive에 Markdown 파일로 저장되며, 사이트마다 같은 절차를 다시 만들 필요가 없습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 내가 만든 Skill이 SharePoint와 OneDrive를 따라다닙니다: Personal Skills

문서 생성 방식이나 검토 절차처럼 자주 사용하는 업무 방법을 SharePoint 사이트마다 다시 설정해야 한다면 개인화의 가치가 줄어듭니다. 사용자가 어디서 일하든 같은 절차를 불러올 수 있어야 진정한 재사용이 가능합니다.

Copilot in SharePoint에 **Personal Skills** 기능이 추가됩니다.

> **한 줄 요약**
> 사용자가 직접 만든 Skill이 SharePoint 사이트와 OneDrive를 따라다니며 어디서나 재사용되고, 사용자의 OneDrive에 Markdown 파일로 저장됩니다.

---

## 무엇이 새로워지나

사용자는 Copilot in SharePoint에서 개인 Skill을 만들 수 있습니다. 이 Skill은 특정 사이트에만 묶이지 않고 다음 위치에서 함께 사용할 수 있습니다.

- 여러 SharePoint 사이트
- 사용자의 OneDrive

예를 들어 문서 생성 Skill을 한 번 만들면 사이트마다 다시 만들지 않고 어디서나 동일한 방식으로 사용할 수 있습니다.

## 저장과 소유권

Personal Skill은 사용자가 소유하며 **OneDrive의 Markdown 파일**로 저장됩니다. 이 구조는 Skill이 개인의 업무 자산으로 이동하고 관리된다는 점을 보여 줍니다.

다만 공지에는 저장 위치·파일 구조·공유 범위·관리 정책의 세부사항이 모두 포함돼 있지 않으므로 Preview와 정식 문서를 통해 확인해야 합니다.

## 활용 시나리오

- 동일한 형식의 프로젝트 보고서 생성
- 문서 검토 체크리스트 적용
- 사이트가 달라도 같은 요약·분류 방식 사용
- OneDrive 문서와 SharePoint 문서에서 동일한 작성 규칙 재사용

## 출시 일정

| 구분 | 일정 |
|---|---|
| Preview | 2026년 8월 |
| GA | 2026년 12월 |
| 저장 형식 | OneDrive의 Markdown 파일 |

## 도입 관점 체크포인트

- Personal Skills에 민감 정보·Secret·과도한 권한 지침을 넣지 않도록 안내합니다.
- OneDrive 보존·퇴사자 처리·공유 정책이 Skill 파일에도 어떻게 적용되는지 확인합니다.
- 개인 Skill과 조직 공식 Enterprise Store 플러그인의 용도를 구분합니다.
- AI나 외부에서 가져온 Skill은 신뢰할 수 없는 코드처럼 검토하도록 교육합니다.
- 파일이 이동·삭제됐을 때 Skill 동작과 복구 방법을 확인합니다.

## Personal Skill과 기업용 플러그인의 차이

| Personal Skill | Enterprise Store Plugin |
|---|---|
| 사용자가 직접 소유 | 조직이 배포·관리 |
| OneDrive Markdown 파일 | Skills·MCP Servers 등을 패키징 |
| 개인 업무 방식 재사용 | 전사 표준 기능 제공 |
| 사이트 간 개인화 | 제품 간 조직 일관성 |

## 마무리

Personal Skills는 사용자의 업무 노하우를 특정 SharePoint 사이트에 가두지 않고 이동 가능한 Markdown 자산으로 만듭니다. 개인 생산성을 높이는 동시에 OneDrive의 수명주기·공유·보안 정책까지 Skill 관리의 일부가 되므로, 조직 공식 플러그인과의 역할 구분이 중요합니다.

---

> ※ 본 글은 Microsoft 365 메시지 센터/로드맵 공지(**RM567668**)를 바탕으로 정리했습니다. 원문은 [Message Center Archive](https://mc.merill.net/message/RM567668)와 [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)에서 확인할 수 있으며, 실제 출시 일정·기능은 변경될 수 있습니다.
