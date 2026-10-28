---
title: "Copilot 대화 전체 또는 답변 하나를 링크로 공유하는 법"
date: 2026-09-09T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Collaboration
  - Sharing
  - Governance
excerpt: "Microsoft 365 Copilot에서 대화 세션이나 개별 답변을 조직 내부 링크로 공유할 수 있습니다. 공유 시점의 내용만 전달되며 원본 파일 권한은 바뀌지 않고, 관리자 제어는 사용자별이 아닌 테넌트 전체에 적용됩니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 대화 전체 또는 답변 하나를 링크로 공유하는 법

동료에게 Copilot의 유용한 답변을 전달하려고 복사·붙여넣기를 반복하면, 답을 얻기까지의 맥락이 빠지기 쉽습니다. **Session and Response Sharing**은 대화 전체 또는 특정 답변을 링크로 전달하는 기능입니다.

Microsoft 365 Copilot 사용자는 같은 조직의 동료에게 공유할 수 있고, 받는 사람은 읽기 전용으로 내용을 본 뒤 자신의 Copilot 대화에서 이어갈 수 있습니다. 아래 내용은 2026년 9월 8일 업데이트된 MC1461700 기준입니다.

---

## 세션 공유와 답변 공유의 차이

**Session Sharing**은 질문과 답변의 맥락을 함께 전달할 때 적합합니다. **Response Sharing**은 특정 결과 하나만 공유할 때 사용합니다. 공유 대상은 같은 조직 내부 사용자이며, 외부 공개 링크 기능으로 설명된 것은 아닙니다.

수신자는 원래 세션을 공동 편집하는 것이 아니라, 읽기 전용으로 확인하고 자신의 Copilot 세션에서 작업을 이어갑니다.

## 공유 후 추가한 메시지는 포함되지 않습니다

세션 공유는 **링크를 만든 시점에 존재하던 대화 내용**을 담습니다. 이후 원래 대화에 추가한 메시지는 비공개로 남으며 기존 공유 세션에 들어가지 않습니다.

따라서 진행 중인 프로젝트의 실시간 공동 대화방과는 다릅니다. 공유한 결과를 수정하거나 추가 논의를 전달할 때는 수신자가 어떤 시점의 내용을 보고 있는지 구분하는 것이 좋습니다.

## 원본 자료 접근 권한은 별개입니다

대화 또는 답변을 공유해도 참조된 파일, 이메일, 회의, 채팅 등 Microsoft 365 콘텐츠의 권한이 새로 부여되지는 않습니다. 원본 자료에는 기존 권한이 계속 적용됩니다.

다만 **생성된 답변에 담긴 내용 자체를 동료에게 전달하는 행위**는 별도 검토가 필요합니다. 원본 링크를 열 수 없다는 이유만으로 답변 속 민감한 내용까지 자동으로 보호된다고 가정해서는 안 됩니다.

## 관리자는 테넌트 전체로 제어합니다

기본값은 활성화입니다. 비활성화하려면 다음 경로를 사용합니다.

**Microsoft 365 admin center → Copilot → Settings → Copilot session and response sharing → Allow users to share Copilot sessions and responses 선택 해제**

이 제어는 **테넌트 전체**에 적용되며 특정 사용자나 Entra ID 그룹별로 범위를 지정할 수 없습니다. 일부 부서만 허용하는 정책을 이 설정 하나로 구현할 수 없다는 점이 중요합니다.

## 배포 일정과 업무 적용

Worldwide GA 배포는 **2026년 8월 말 시작, 9월 말 완료 예상**으로 안내되었습니다. 이는 해당 공지 시점의 계획입니다.

한국 조직에서는 프롬프트와 우수 답변을 재사용하는 교육 사례로 활용할 수 있습니다. 공유 전 민감정보 확인, 공유 시점 표시, 원본 자료의 별도 권한 요청이라는 세 가지 원칙을 사용자 가이드에 넣는 것이 좋습니다.

> **출처**: [MC1461700 — Session and Response Sharing in M365 Copilot](https://mc.merill.net/message/MC1461700). [Microsoft 365 Roadmap 562353](https://www.microsoft.com/microsoft-365/roadmap?searchterms=562353). **실제 출시 일정·기능은 변경될 수 있습니다**.
