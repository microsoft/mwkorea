---
title: "Word Copilot 문서 요약, 문서 상단에서 Copilot 화면과 프롬프트로 이동"
date: 2026-09-03T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft 365 Copilot
  - Word
  - Document Summarization
  - Generative AI
  - User Experience
excerpt: >-
  Word 문서 상단에 표시되던 Top of Doc 요약 경험이 2026년 9월부터 다른 Copilot 진입점으로 이동합니다.
  요약 기능 자체는 유지되며 사용자는 Copilot의 ‘Summarize this document’ 제안이나 자연어 프롬프트를 통해 같은 문서 요약을 요청할 수 있습니다.
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Word Copilot 문서 요약, 문서 상단에서 Copilot 화면과 프롬프트로 이동

Word에서 문서를 열었을 때 상단에 나타나던 **Top of Doc** 요약 경험이 사라집니다. 하지만 문서를 요약하는 Copilot 기능이 폐지되는 것은 아닙니다. Microsoft는 같은 기능을 Word 안의 다른 Copilot 화면으로 옮겨 접근 방식을 통합합니다.

사용자는 Copilot에서 표시되는 ‘Summarize this document’ 제안을 선택하거나, Copilot을 열고 자연어로 문서 요약을 요청할 수 있습니다. 기능은 유지되고 진입점만 달라지는 변화이므로 사용자 안내에서 “요약 기능 종료”로 오해하지 않도록 구분해야 합니다.

---

## 없어지는 것과 남는 것

변경되는 것은 문서 맨 위에 있던 **Top of Doc 요약 UI**입니다. 기존에 그 위치를 기준으로 작성된 매뉴얼이나 교육 자료는 더 이상 실제 화면과 일치하지 않을 수 있습니다.

반면 다음 기능은 계속 제공됩니다.

- 현재 문서의 내용을 Copilot으로 요약
- 지원되는 상황에서 표시되는 **Summarize this document** 선제 제안
- Word의 Copilot을 열고 “이 문서를 요약해 줘”와 같은 자연어 프롬프트 입력
- 생성형 AI를 사용해 문서 내용을 이해하는 기존 요약 역량

즉, Microsoft는 요약 기능을 제거하는 대신 Copilot 안에서 제안과 대화를 통해 접근하도록 바꾸고 있습니다. 사용자가 문서 상단에서 자동으로 보던 경험과 직접 Copilot을 여는 경험의 차이가 가장 큰 변화입니다.

## 대상 사용자와 지원 범위

대상은 **Word에서 Copilot을 사용할 수 있도록 라이선스가 부여된 사용자**입니다. 별도의 신규 라이선스나 추가 기능 구매는 안내되지 않았습니다. 기존에 Copilot in Word에 접근할 수 없는 사용자는 이번 변경의 직접 대상이 아닙니다.

플랫폼과 서비스는 **Microsoft Word 및 Microsoft 365 Copilot in Word**로 명시됐습니다. 다만 이번 공지에는 Windows, Mac, 웹, 모바일 가운데 어느 Word 클라이언트가 포함되는지, 또는 필요한 앱 빌드 번호가 구체적으로 적혀 있지 않습니다. 지원팀은 특정 클라이언트를 임의로 가정하지 말고 조직의 대상 환경에서 실제 UI를 확인해야 합니다.

## 2026년 9월 초부터 배포

2026년 9월 2일 업데이트로 일정이 명확해졌으며, **전 세계 일반 공급은 2026년 9월 초 시작**됩니다. 완료일이나 테넌트별 도달 시점은 공지되지 않았습니다. 순차 배포 과정에서 일부 사용자는 Top of Doc을 계속 보고, 다른 사용자는 새 Copilot 진입점을 먼저 볼 수 있습니다.

관리자가 사전에 변경할 설정은 없습니다. Microsoft는 **관리자 조치가 필요하지 않다**고 명시했고, 이번 UI 이동을 제어하는 새 정책이나 토글도 안내하지 않았습니다. 기존 Copilot 접근 권한과 조직의 정책이 그대로 적용됩니다.

## 사용자 경험은 어떻게 달라지나

기존 사용자는 문서를 열자마자 보이는 요약을 기대할 수 있습니다. 변경 후에는 지원되는 경우 Copilot이 ‘Summarize this document’를 제안하며, 제안이 보이지 않더라도 Copilot을 열어 직접 요청할 수 있습니다.

권장 사용자 안내 문구는 간단합니다. “Word 문서 요약은 계속 사용할 수 있지만 문서 상단의 기존 요약 화면은 종료됩니다. Word에서 Copilot을 열고 ‘이 문서를 요약해 줘’라고 요청하세요.” 이 설명은 기능 종료와 위치 변경을 분리해 전달합니다.

## 조직이 준비할 사항

기술적 설정 대신 변화 관리가 필요합니다.

1. Top of Doc 화면을 캡처한 교육 자료와 헬프 데스크 문서를 찾습니다.
2. 안내를 Copilot 제안 또는 자연어 프롬프트 방식으로 수정합니다.
3. 사용자에게 요약 역량이 없어지는 것이 아니라 접근 위치가 바뀐다고 공지합니다.
4. 지원되는 클라이언트와 화면을 실제 테넌트에서 확인해 문서에 반영합니다.
5. 중요한 문서의 요약은 원문과 대조한다는 기존 생성형 AI 검토 원칙을 유지합니다.

이 변경은 Word 안의 Copilot 경험을 하나로 모으는 UI 정리입니다. 새로운 처리 방식이나 저장 정책이 발표된 것은 아니며, 공지가 확인한 규정 준수 영향은 생성형 AI와 상호작용하는 진입점과 사용자 작업 흐름이 달라진다는 점입니다.

---

> **출처**
> - Message Center ID: **MC1454113**
> - 원문 제목: **Microsoft Copilot Word: Document summarization experience moving**
> - 원문: <https://mc.merill.net/message/MC1454113>
> - Microsoft 365 Roadmap: <https://www.microsoft.com/microsoft-365/roadmap>
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
