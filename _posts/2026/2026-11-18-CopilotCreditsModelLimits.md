---
title: "Copilot 모델 한도 이후에도 계속 사용하기: Auto와 Credits의 차이"
date: 2026-11-18T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotCredits
  - Billing
  - Microsoft365Copilot
  - FinOps
excerpt: "Copilot에서 라이선스에 포함된 모델 사용 한도에 도달한 뒤 Auto로 계속하거나 Copilot Credits로 선택 모델을 유지할 수 있게 됩니다. 새로운 비용 표시와 지출 정책의 확인 사항을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 모델 한도 이후에도 계속 사용하기: Auto와 Credits의 차이

Microsoft가 MC1557754를 통해 Copilot Chat과 Office의 모델 사용 한도 이후 선택지를 안내했습니다. 핵심은 **Auto로 계속하기**와 **Copilot Credits를 사용해 선택 모델을 유지하기**를 구분하는 것입니다.

모든 사용이 자동으로 추가 과금으로 바뀌는 것은 아닙니다. 사용량 기반 청구(UBB)가 허용된 사용자에게만 크레딧을 사용하는 선택지가 제공되므로, 사용자 안내와 관리자 지출 정책을 함께 정비해야 합니다.

---

## 한도에 도달하면 무엇이 달라지나요?

Microsoft 365 Copilot 라이선스에 포함된 해당 모델 한도에 도달해도 Auto로 계속하면 Copilot Credits를 소비하지 않습니다. 반면 UBB가 활성화되어 있고 사용 가능한 크레딧이 있으면 선택한 모델을 크레딧으로 계속 사용할 수 있습니다.

적용 범위는 Microsoft Copilot 앱의 Copilot Chat, Word·Excel·PowerPoint의 Copilot이며 웹·데스크톱·모바일을 포함합니다. 모델 선택기에는 제공 모델이 표시되지만, 접근 권한이 없는 모델은 회색으로 표시되어 선택할 수 없습니다.

## 비용을 알려 주는 새 표시

![Copilot 크레딧 아이콘과 사용량 세부 정보](/mwkorea/assets/images/2026-11-18-CopilotCreditsModelLimits/image1.jpg)

채워진 크레딧 아이콘은 현재 사용이 계량되며 Credits를 소비한다는 의미입니다. 비어 있는 아이콘은 크레딧을 소비하지 않는 상태를 뜻합니다. 아이콘에 마우스를 올리면 세부 정보와 추가 정보 창을 여는 옵션이 나타납니다.

Copilot에 `/cost`를 입력해 현재 세션의 비용 관련 정보를 확인할 수도 있습니다.

![UBB가 허용된 사용자가 크레딧으로 계속할 수 있음을 알리는 배너](/mwkorea/assets/images/2026-11-18-CopilotCreditsModelLimits/image2.jpg)

## 관리자가 확인할 지출 정책

Microsoft 365 관리 센터의 **Copilot > Cost Management > Configuration**에서 적용 정책을 확인합니다.

1. 정책에 **Models with usage-based billing in Chat and Office** 서비스가 포함되어 있는지 확인합니다.
2. 청구 방식과 가용 크레딧을 확인합니다.
3. 전체 사용자 또는 Microsoft Entra ID 보안 그룹 등 정책 대상을 점검합니다.
4. 지출 한도와 알림을 설정하고 Auto와 유료 모델 유지의 차이를 안내합니다.

기존 정책의 **Auto-apply new services**가 켜져 있으면 새 지원 서비스가 자동 포함됩니다. 꺼져 있으면 관리자가 직접 추가해야 합니다. 자동 적용 여부가 의도하지 않은 비용 접근으로 이어지지 않는지 살펴볼 필요가 있습니다.

## 제공 일정과 도입 포인트

원문 시점에 Frontier 배포는 진행 중이며, Worldwide 운영 클라우드의 GA는 **2026년 12월 초**로 계획되어 있습니다.

이 발표는 기존 과금 변경 공지 MC1479276 및 UBB 전용 모델 공지 MC1519122와 연결됩니다. 지원팀은 단순히 “한도 이후 유료”라고 안내하기보다 **크레딧 없는 Auto 경로가 남아 있다**는 점을 명확히 전달해야 합니다.

설정 방법은 [Copilot Credits UBB 설정](https://learn.microsoft.com/copilot/implement/usage-based-billing-copilot-credits-setup)과 [지출 정책 관리](https://learn.microsoft.com/en-us/copilot/implement/usage-based-billing-manage-copilot-credits)를 참고하세요.

> **출처**: [MC1557754](https://mc.merill.net/message/MC1557754), Microsoft 365 Message Center Archive. [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 제시되지 않았습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
