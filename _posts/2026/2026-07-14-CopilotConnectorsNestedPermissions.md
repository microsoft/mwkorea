---
title: "Copilot 커넥터 권한이 더 정교해집니다: Jira·Confluence·ServiceNow 중첩 권한 지원"
date: 2026-07-14T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - CopilotConnectors
  - Jira
  - Confluence
  - ServiceNow
  - AccessControl
  - Roadmap
excerpt: "Jira, Confluence, ServiceNow용 Copilot 커넥터가 계층형 ACL을 지원합니다. 외부 시스템의 중첩된 권한 구조를 더 정확하게 반영해, 관리자가 Copilot을 통한 콘텐츠 접근을 정교하게 통제할 수 있습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 커넥터 권한이 더 정교해집니다: Jira·Confluence·ServiceNow 중첩 권한 지원

Copilot 커넥터는 Jira, Confluence, ServiceNow 같은 외부 시스템의 콘텐츠를 Microsoft Graph에 연결합니다. 이때 답변 품질만큼 중요한 것이 있습니다. 원본 시스템에서 볼 수 없는 콘텐츠가 Copilot을 통해서도 노출되지 않도록 **기존 접근 권한을 정확하게 반영하는 것**입니다.

이번 Microsoft 365 로드맵 업데이트는 Jira, Confluence, ServiceNow 커넥터에 **계층형 ACL(hierarchical access control lists)** 지원을 추가합니다.

> **한 줄 요약**
> 외부 시스템의 중첩된 권한 구조를 Copilot 커넥터가 더 정확하게 이해해, 관리자가 사용자별 콘텐츠 접근 범위를 정교하게 유지할 수 있습니다.

---

## 무엇이 바뀌나

공지에 명시된 핵심은 Jira, Confluence, ServiceNow 커넥터의 **hierarchical ACL 지원**입니다. 조직·프로젝트·공간·개별 콘텐츠처럼 여러 단계로 이어지는 권한 관계를 커넥터가 반영할 수 있게 됩니다.

단순히 사용자나 그룹 하나만 확인하는 방식보다, 상위와 하위 리소스 사이의 권한 상속·제한 관계를 고려할 수 있다는 의미입니다.

## 왜 중요한가

외부 데이터를 Copilot에 연결할 때 권한 모델이 지나치게 단순하면 두 가지 문제가 생길 수 있습니다.

- 사용자가 원래 볼 수 있어야 하는 콘텐츠를 찾지 못하는 문제
- 사용자가 원래 볼 수 없는 콘텐츠가 검색·답변에 포함될 위험

중첩 권한 지원은 원본 시스템의 권한 구조와 Copilot에서의 콘텐츠 가시성을 더 가깝게 맞추는 기반이 됩니다.

## 적용 대상

| 항목 | 내용 |
|---|---|
| 대상 커넥터 | Jira, Confluence, ServiceNow |
| 핵심 기능 | 계층형 ACL 및 중첩 권한 지원 |
| Preview | 2026년 3월로 안내 |
| GA | 2026년 4월로 안내 |

위 일정은 로드맵에 기재된 계획이며 테넌트와 환경에 따라 실제 제공 시점은 다를 수 있습니다.

## 도입 관점 체크포인트

- 각 원본 시스템의 그룹·프로젝트·공간 권한 구조가 최신 상태인지 점검합니다.
- 테스트 계정을 사용해 허용된 콘텐츠와 제한된 콘텐츠가 Copilot에서 예상대로 구분되는지 확인합니다.
- 커넥터 재동기화 이후 권한 변경이 반영되는 데 걸리는 시간을 운영 기준에 포함합니다.
- 감사·보안팀과 함께 과다 노출과 과도한 차단 사례를 모두 검증합니다.

## 마무리

Copilot 커넥터의 가치는 더 많은 데이터를 연결하는 데서 끝나지 않습니다. **원본 시스템의 권한을 얼마나 충실하게 지키면서 연결하는가**가 실제 도입의 신뢰를 좌우합니다. Jira·Confluence·ServiceNow를 연결한 조직이라면 중첩 권한 반영 여부를 테스트해 보시길 권합니다.

---

> ※ 본 글은 Microsoft 365 메시지 센터/로드맵 공지(**RM503587**)를 바탕으로 정리했습니다. 원문은 [Message Center Archive](https://mc.merill.net/message/RM503587)와 [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)에서 확인할 수 있으며, 실제 출시 일정·기능은 변경될 수 있습니다.
