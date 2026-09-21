---
title: "Viva Glint Copilot, 교차 테넌트 게스트에게 더 이상 제공되지 않습니다"
date: 2026-09-10T00:00:00 KST
categories:
  - Copilot
tags:
  - VivaGlint
  - MicrosoftEntra
  - B2BCollaboration
  - GuestAccess
  - PeopleAnalytics
excerpt: "Microsoft Entra 교차 테넌트 게스트 사용자는 2026년 8월 26일부터 Viva Glint의 Copilot 요약과 채팅 기능을 사용할 수 없습니다. 기반 Copilot 서비스의 제약이 원인이므로 라이선스 할당이나 VFAM 정책 변경으로 접근을 복구할 수 없습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Viva Glint Copilot, 교차 테넌트 게스트에게 더 이상 제공되지 않습니다

외부 조직 계정으로 Viva Glint 프로그램에 참여하는 사용자는 설문과 보고서를 계속 이용할 수 있지만, Copilot 기반 요약 기능은 더 이상 볼 수 없습니다. Microsoft는 오류가 반복되는 대신 지원되지 않는 기능을 화면에서 숨기는 방식으로 경험을 바꿨습니다.

이 제한은 Viva Glint 라이선스 정책이나 관리자가 구성한 접근 정책 때문에 생긴 것이 아닙니다. Viva Glint가 사용하는 Copilot 대규모 언어 모델 서비스가 Microsoft Entra 교차 테넌트 게스트를 현재 지원하지 않는 것이 직접적인 이유입니다.

---

## 대상은 B2B 협업 게스트 계정입니다

변경 대상은 다른 테넌트에 계정이 있고 조직의 Viva Glint에 게스트로 접근하는 Microsoft Entra B2B 협업 사용자입니다. 이전에는 이들이 Copilot을 열 때 인증 오류를 만나거나 기능이 로드되지 않는 현상이 생길 수 있었습니다.

2026년 8월 26일부터 Viva Glint는 이런 사용자에게 지원되지 않는 Copilot 진입점을 표시하지 않습니다. 조직 내부 테넌트에 계정이 있는 사용자의 Copilot 경험에는 이번 제한이 적용되지 않습니다.

## 사용할 수 없게 된 기능

교차 테넌트 게스트에게는 다음 기능이 더 이상 제공되지 않습니다.

- Team Summary와 Executive Summary 보고서의 **Copilot Highlights**
- 의견 요약에 사용하는 **Copilot 버튼과 채팅 패널**
- 의견 패널의 **Copilot Summarize** 명령

반면 설문, 대시보드, 일반 보고서, 의견과 관련 Viva Glint 기능은 그대로 유지됩니다. 사용자 역할과 권한, 기존 VFAM 정책, Viva Glint 라이선스 요구 사항도 바뀌지 않습니다.

## Copilot 라이선스로 해결되지 않는 이유

Viva Glint의 Copilot 기능에는 Microsoft Copilot 라이선스가 필수 조건이 아닙니다. 따라서 교차 테넌트 게스트에게 별도로 Microsoft Copilot 라이선스를 배정해도 사라진 기능이 복구되지 않습니다.

관리자가 VFAM 정책을 완화해도 마찬가지입니다. 이번 제한은 Viva Feature Access Management 설정이 아니라 기반 Copilot 서비스의 게스트 지원 범위에 있기 때문입니다. 불필요한 라이선스 추가나 정책 변경을 문제 해결책으로 안내하지 않는 것이 중요합니다.

## 운영팀이 확인할 부분

관리 구성 변경은 필요하지 않습니다. 다만 인사, 피플 애널리틱스, 설문 프로그램 담당자는 외부 컨설턴트나 관계사 인력이 게스트 계정으로 Viva Glint 프로그램에 참여하는지 확인할 필요가 있습니다.

해당 사용자가 기대할 수 있는 기능 범위를 사전에 안내하고, 과거에 접수된 Copilot 인증 실패나 로딩 오류가 이번 제약과 관련됐는지도 검토할 수 있습니다. 일반 설문과 보고서 기능까지 중단된 것으로 오해하지 않도록 영향 범위를 구체적으로 전달하는 것이 좋습니다.

## 배포 일정

| 구분 | 일정 |
|---|---|
| 변경 적용 시작 | 2026년 8월 26일 |
| 일반 공급, 전 세계 | 2026년 8월 말 시작, 9월 말 완료 예정 |

Microsoft는 별도의 규정 준수 고려 사항이나 필수 관리 작업을 제시하지 않았습니다. 향후 기반 서비스가 게스트를 지원하는지 여부는 이번 공지만으로 확정할 수 없으므로 현재 제한을 기준으로 지원 문서와 사용자 안내를 정리해야 합니다.

---

> **출처**
>
> - 원문 ID: **MC1469961** — *Microsoft Viva Glint: Copilot features are no longer available for cross-tenant guest users*
> - 원문: [https://mc.merill.net/message/MC1469961](https://mc.merill.net/message/MC1469961)
> - [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
