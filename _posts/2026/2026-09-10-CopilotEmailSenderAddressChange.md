---
title: "Copilot 안내 메일 발신 주소 변경: 허용 목록과 메일 흐름 규칙 점검"
date: 2026-09-10T00:00:00 KST
categories:
  - Copilot
tags:
  - MicrosoftCopilot
  - ExchangeOnline
  - DefenderForOffice365
  - EmailSecurity
  - Administration
excerpt: "Copilot 교육 및 제품 활용 안내 메일의 발신 주소가 microsoftcopilotupdates@microsoft.com으로 바뀝니다. 2026년 9월 중순 전 세계 적용에 앞서 기존 주소를 참조하는 허용 목록과 메일 흐름 규칙을 점검해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 안내 메일 발신 주소 변경: 허용 목록과 메일 흐름 규칙 점검

Microsoft 365 Copilot에서 Microsoft Copilot으로 브랜드가 전환되면서 사용자 교육과 제품 활용 안내 메일의 발신자 표시도 함께 정리됩니다. 메일의 내용이나 목적은 달라지지 않지만, 보안 정책이 이전 주소를 기준으로 작성돼 있다면 전달에 영향을 받을 수 있습니다.

이번 변경은 테넌트에서 켜는 기능이 아니라 Microsoft가 자동으로 적용하는 발신자 변경입니다. 따라서 관리자는 배포 설정 대신 Exchange Online과 Microsoft Defender for Office 365에 남아 있는 주소 기반 규칙을 살펴봐야 합니다.

---

## 무엇이 바뀌나요

Copilot 기능을 새로 사용할 수 있게 된 사용자에게 보내는 서비스 활성화 메일과 기존 사용자를 위한 교육·제품 활용 메일이 앞으로 다음 주소에서 발송됩니다.

- 새 주소: **microsoftcopilotupdates@microsoft.com**
- 이전 주소: **m365copilotupdates@microsoft.com**

메일은 사용자가 구독에 포함된 Copilot 기능을 이해하고, 새 기능과 생산성 활용법을 알아볼 수 있도록 제공됩니다. 발신 주소만 바뀌며 안내 내용과 전송 목적은 그대로 유지됩니다.

## 영향을 받는 조직과 서비스

영향 대상은 Copilot 기능이 활성화된 사용자에게 Microsoft 제품 및 서비스 커뮤니케이션을 보내도록 선택한 조직입니다. 새로 Copilot 서비스를 사용할 수 있게 된 사용자뿐 아니라 이미 관련 메일을 받고 있는 사용자도 포함됩니다.

관리 측면에서는 다음 영역을 담당하는 팀이 확인해야 합니다.

- Exchange Online 메일 흐름 규칙
- Microsoft Defender for Office 365 정책
- 안전한 보낸 사람 목록
- 조직 또는 보안 게이트웨이의 발신자 허용 목록
- Microsoft 365 최종 사용자 커뮤니케이션 운영 절차

주소를 기준으로 허용하거나 분류하는 규칙이 없다면 사용자 경험 변화는 크지 않을 수 있습니다. 반대로 이전 주소만 허용한 환경에서는 새 메일이 격리되거나 다른 경로로 분류될 가능성을 점검해야 합니다.

## 관리자가 확인할 체크리스트

먼저 `m365copilotupdates@microsoft.com`을 직접 참조하는 메일 흐름 규칙, 안전한 보낸 사람 등록, 스팸 예외와 보안 제품의 허용 목록을 검색합니다. 해당 규칙이 Copilot 안내 메일 수신을 보장하기 위한 것이라면 새 주소 `microsoftcopilotupdates@microsoft.com`을 반영해야 합니다.

조직이 사용자 커뮤니케이션을 별도 아카이브나 지원 프로세스로 보내는 경우에도 발신 주소 조건을 확인하는 편이 좋습니다. 헬프 데스크에는 새 발신자 이름과 주소를 알려 정상적인 안내 메일이 피싱으로 오인되지 않도록 할 수 있습니다.

다만 발신 주소 변경만을 근거로 기존 보안 검사를 낮출 필요는 없습니다. 실제 메일 인증 결과와 조직의 표준 보안 정책을 계속 적용해야 합니다.

## 일정과 변경 성격

| 구분 | 내용 |
|---|---|
| 일반 공급 | 2026년 9월 중순, 전 세계 |
| 적용 방식 | 자동 적용 |
| 테넌트 설정 | 변경 불필요 |
| 메일 콘텐츠와 목적 | 변경 없음 |

Microsoft는 이 변경과 관련해 별도의 규정 준수 고려 사항을 식별하지 않았다고 안내합니다. 그래도 조직 고유의 메일 보존, 분류, 보안 정책이 발신 주소에 의존한다면 자체 검토가 필요합니다.

---

> **출처**
>
> - 원문 ID: **MC1469962** — *Change in sender email address for Copilot emails*
> - 원문: [https://mc.merill.net/message/MC1469962](https://mc.merill.net/message/MC1469962)
> - [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
