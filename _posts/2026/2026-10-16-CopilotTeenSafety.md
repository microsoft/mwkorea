---
title: "13~17세 학생의 Copilot, 연령에 맞는 콘텐츠 안전 보호가 기본 적용됩니다"
date: 2026-10-16T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftCopilot
  - Education
  - ContentSafety
  - EntraID
excerpt: "Microsoft Copilot이 Entra ID에서 13~17세 청소년으로 식별된 사용자에게 추가 콘텐츠 안전 보호를 자동 적용합니다. 2026년 10월 중순부터 시작되는 배포의 대상과 학교 IT 담당자가 확인할 사항을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 13~17세 학생의 Copilot, 연령에 맞는 콘텐츠 안전 보호가 기본 적용됩니다

학생에게 생성형 AI를 제공하는 학교는 답변의 유용성뿐 아니라 연령에 적합한 경험도 함께 고려해야 합니다. Microsoft는 메시지 센터 공지 MC1509805에서 **13~17세 사용자를 위한 추가 콘텐츠 안전 보호**를 안내했습니다.

이번 변경은 별도 설정을 켜야 받을 수 있는 기능이 아닙니다. Copilot에 접근할 수 있고 Entra ID의 `ageGroup` 속성에서 청소년으로 식별되는 사용자에게 기본 적용됩니다. 다만 학생 계정을 사용한다는 사실만으로 연령 속성까지 올바르게 설정되어 있다고 가정해서는 안 됩니다.

---

## 누구에게 적용되나요?

공지의 대상은 Microsoft Copilot 사용이 허용되어 있고, 필요한 라이선스와 접근 권한을 갖춘 13~17세 사용자입니다. 대상 식별에는 **Entra ID의 `ageGroup` 값 `teen`**을 사용합니다.

Microsoft Copilot 외에 Copilot과 통합된 일부 앱과 에이전트에도 해당되는 경우 보호가 적용됩니다. 모든 에이전트와 외부 서비스에 동일한 보호가 제공된다는 의미로 확대 해석해서는 안 됩니다.

## 사용 경험에서 달라지는 점

추가 보호는 청소년이 더 안전하고 연령에 적합한 답변을 받도록 설계되었습니다. 이에 따라 **민감한 주제에 대한 응답이 더 제한될 수 있습니다.**

학교의 실습 자료나 도움말에 성인 사용자 화면을 기준으로 한 예시가 있다면, 학생의 답변 결과와 차이가 날 수 있다는 점을 안내하는 것이 좋습니다. 이는 공지가 설명하는 응답 제한을 고려한 운영상의 제안이며, 특정 주제의 허용·차단 목록이 발표되었다는 뜻은 아닙니다.

## 배포 일정과 관리자 확인 사항

원문은 **2026년 10월 중순부터 전 세계 일반 공급(GA) 배포를 시작**한다고 안내합니다. 시작 시점이 모든 계정의 적용 완료를 뜻하지는 않습니다.

업데이트를 받기 위한 추가 구성 변경은 필요하지 않습니다. 운영 담당자는 다음 사항을 확인할 수 있습니다.

- 학생의 `ageGroup` 정보가 실제 연령 구분에 맞는지 점검합니다.
- 학생과 교사에게 연령에 따른 응답 차이가 있을 수 있음을 안내합니다.
- 내부 Copilot 사용 지침과 지원 문서에 이번 변경을 반영합니다.

연령 속성의 의미는 [Microsoft Graph 사용자 리소스 문서](https://learn.microsoft.com/graph/api/resources/user?view=graph-rest-1.0#agegroup-values), 교육 환경의 설정 절차는 [학생 연령 그룹 설정 문서](https://learn.microsoft.com/microsoft-365/education/guide/2-baseline/setup/baseline-setup-set-student-age-group)에서 확인할 수 있습니다.

## 마무리

핵심은 **보호 기능은 자동 적용되지만, 대상 식별은 디렉터리의 연령 정보에 의존한다**는 점입니다. 학교에서는 새 기능을 별도로 활성화하기보다 계정 정보와 사용자 안내를 확인하는 데 초점을 맞추는 것이 좋습니다.

> 출처: [MC1509805 — Microsoft Copilot: Additional content safety protections for students under 18](https://mc.merill.net/message/MC1509805). [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 제시되지 않았습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
