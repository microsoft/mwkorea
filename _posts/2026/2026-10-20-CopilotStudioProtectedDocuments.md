---
title: "보호 레이블을 유지한 채 문서 활용: Copilot Studio의 MPIP 지원 예고"
date: 2026-10-20T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - MicrosoftPurview
  - InformationProtection
  - SensitivityLabels
  - Agents
excerpt: "Microsoft 365 채널에 배포된 Copilot Studio 에이전트가 MPIP 민감도 레이블이 적용된 업로드 문서를 처리하도록 지원할 예정입니다. 계정 권한과 레이블 보호를 유지한다는 원문의 범위와 도입 확인사항을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 보호 레이블을 유지한 채 문서 활용: Copilot Studio의 MPIP 지원 예고

조직에서 중요한 문서에 보호 레이블을 붙여도 에이전트가 이를 다루지 못하면 업무 흐름이 끊길 수 있습니다. 그렇다고 에이전트에 전달하려고 보호를 제거하는 것은 바람직한 해결책이 아닙니다.

Microsoft는 **Microsoft Purview Information Protection(MPIP) 민감도 레이블로 보호된 문서**를 Copilot Studio 에이전트에 업로드해 활용하도록 지원하는 로드맵을 공개했습니다. 발표의 핵심은 접근 제한을 없애는 것이 아니라, 권한과 레이블 보호를 적용하면서 내용을 처리한다는 점입니다.

---

## 지원 대상은 Microsoft 365 채널의 에이전트

원문이 명시한 대상은 **Microsoft 365 채널에 배포된 Copilot Studio 에이전트**입니다. 사용자가 MPIP 민감도 레이블이 적용된 파일을 업로드할 때 발생하는 제약을 해소하는 방향입니다.

이 설명을 모든 배포 채널이나 모든 지식 원본으로 확대해서는 안 됩니다. 원문은 파일 업로드를 다루며, 지원 파일 형식과 크기, 레이블별 차이까지 열거하지는 않습니다.

## 계정 권한과 레이블 보호가 전제입니다

로드맵은 에이전트가 **사용자 또는 에이전트 계정의 권한에 따라 내용을 처리**하고, 레이블 보호를 종단 간 적용한다고 설명합니다.

따라서 “보호된 문서도 이제 누구나 읽는다”는 의미가 아닙니다. 어떤 계정의 권한이 실제 처리에 사용되는지와 해당 계정이 가진 문서 접근 권한을 확인해야 합니다.

| 원문에서 확인되는 내용 | 아직 확인해야 할 내용 |
|---|---|
| MPIP 민감도 레이블 적용 파일 업로드 지원 예고 | 구체적인 지원 형식·크기·레이블 조합 |
| Microsoft 365 채널 배포 에이전트 대상 | 다른 채널의 지원 여부 |
| 사용자·에이전트 계정 권한에 따른 처리 | 상황별 인증·권한 적용 방식 |
| 레이블 보호의 종단 간 적용 | 생성 결과의 레이블 처리 세부 동작 |

특히 입력 문서의 보호를 유지한다는 설명만으로 생성 답변이나 내보낸 파일에 동일 레이블이 자동 상속된다고 단정해서는 안 됩니다.

## 출시 일정은 어떻게 되나요?

원문에는 **프리뷰와 GA 모두 2026년 10월**로 기재되어 있습니다. 플랫폼은 Web, 클라우드는 Worldwide (Standard Multi-Tenant)이며, 확인 시점인 2026년 10월 20일에도 상태는 **In development**로 표시됩니다.

따라서 이번 달 일정이라는 이유만으로 이미 조직에서 사용 가능하다고 판단하지 말고 실제 테넌트 제공 상태와 후속 문서를 확인해야 합니다.

## 한국 조직의 도입 체크포인트

운영 전에는 대표적인 보호 문서를 준비해 권한이 있는 사용자와 없는 사용자의 처리 결과를 각각 확인하는 접근을 권합니다. 에이전트 계정에 필요 이상의 권한이 부여되어 있지 않은지도 살펴봐야 합니다.

답변 공유와 파일 저장 경로 역시 함께 점검할 항목입니다. 이는 도입 검증을 위한 제안이며, 원문에 특정 감사 기능이나 자동 레이블 상속이 발표된 것은 아닙니다.

## 마무리

이번 변화의 방향은 **보호를 풀고 AI를 쓰는 것**이 아니라 **보호 체계 안에서 AI 활용 범위를 넓히는 것**입니다. Microsoft 365 채널이라는 범위와 실제 권한 적용을 확인하는 것이 도입의 출발점입니다.

> **출처**: 원문 ID **RM571305**, [Microsoft Copilot Studio: Support for sensitive documents protected with Microsoft Purview Information Protection (MPIP)](https://mc.merill.net/message/RM571305) · [Microsoft 365 Roadmap 571305](https://www.microsoft.com/en-us/microsoft-365/roadmap?filters=&searchterms=571305). 실제 출시 일정·기능은 변경될 수 있습니다.
