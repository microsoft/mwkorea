---
title: "매번 승인할 필요 없는 청구서 메일: Payables Agent의 Known Senders"
date: 2026-10-17T00:00:00 KST
categories:
  - Copilot
tags:
  - BusinessCentral
  - PayablesAgent
  - Governance
excerpt: "Payables Agent에 이메일 검토 정책과 Known Senders 목록이 추가됩니다. 발신자별 Ask·Approve·Reject를 설정해 반복 승인을 줄이되, 신뢰 판단의 예외와 버전별 차이를 확인해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 매번 승인할 필요 없는 청구서 메일: Payables Agent의 Known Senders

같은 공급업체가 보낸 청구서도 매번 사람이 승인해야 한다면 자동화의 효과가 줄어듭니다. Business Central의 Payables Agent는 이메일 검토 정책과 Known Senders 목록으로 이 과정을 세분화합니다.

핵심은 검토를 일괄 해제하는 것이 아니라, **어떤 발신자는 자동 처리하고 어떤 발신자는 검토·차단할지 명시적으로 결정**하는 데 있습니다.

---

## 검토 정책과 발신자별 설정

새 Email review 필드에는 `Always`(모든 메일 승인), `Never`(승인 없음), `Only if untrusted`(신뢰하지 않는 발신자만 검토, 권장)가 제시됩니다. 관리자가 적극적으로 선택하도록 기본값은 미리 지정되지 않습니다.

Known Senders의 개별 정책은 다음과 같습니다.

| 정책 | 의미 |
|---|---|
| Ask | 사람이 승인해야 처리 |
| Approve | 검토 없이 청구서 처리 |
| Reject | 발신자 차단, 첨부 미처리 |

원문은 이와 함께 `Manage per sender` 정책에서의 평가 순서를 설명합니다. 설정 명칭이 혼재하므로 실제 버전의 UI와 정책 연결을 확인해야 합니다.

## 평가 순서와 주의할 예외

이메일이 아닌 직접 업로드 청구서는 검토하지 않습니다. 모니터링 하위 폴더가 구성되면 그 폴더의 모든 메일을 신뢰하고, 그렇지 않으면 Known Senders의 개별 설정을 적용합니다.

목록에 없는 내부 발신자도 검토 없이 처리하는 설명이 있지만, **메일 인증 헤더 기반 내부 판별은 2026 wave 2, 버전 29.0 제공 예정**으로 따로 명시됩니다. 현재 모든 환경에서 적용된다고 가정해서는 안 됩니다.

`Manage per sender`가 활성화된 상태에서 메일 검토 후 계속 진행하면 발신자가 목록에 자동 추가되고 보안 텔레메트리가 기록됩니다. 따라서 자동 추가와 신뢰 폴더의 운영 권한도 함께 관리하는 것이 좋습니다.

## 일정과 도입

원문은 2026 release wave 1의 8월 마이너 릴리스부터 제공된다고 설명하며 GA 표기도 **2026년 8월**입니다. 반복 거래처부터 정책을 검증하고, 미확인 발신자와 차단 대상의 실제 처리 결과를 확인하세요.

> 출처: 원문 ID **RM576777**, [MC 아카이브](https://mc.merill.net/message/RM576777), [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap?id=576777). 실제 출시 일정·기능은 변경될 수 있습니다.
