---
title: "Power Platform 관리센터, 'Copilot Studio Authors' 설정 이름을 'Pay-as-you-go 사용자'로 변경"
date: 2026-09-30T00:00:00 KST
categories:
  - Copilot
tags:
  - PowerPlatform
  - CopilotStudio
  - PAYG
  - Governance
excerpt: "Power Platform 관리센터의 'Copilot Studio Authors' 테넌트 설정이 'Copilot Studio pay-as-you-go users'로 이름이 바뀝니다. 기능 자체는 동일하며, 혼동을 줄이기 위한 명칭 정리입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Power Platform 관리센터, 'Copilot Studio Authors' 설정 이름을 'Pay-as-you-go 사용자'로 변경

Power Platform 관리센터에서 Copilot Studio의 과금 방식을 제어하는 테넌트 설정 하나가 이름을 바꿉니다. *Copilot Studio Authors*가 **Copilot Studio pay-as-you-go users**로 변경됩니다. 기능은 그대로지만, 이름 때문에 생기던 오해를 바로잡기 위한 조치입니다.

---

## 이 설정이 실제로 하는 일

이 설정은 **사용자별 종량제(pay-as-you-go, PAYG) 과금 방식으로 Copilot Studio에서 항목을 만들 수 있는지 여부**를 제어합니다. 애초에 거버넌스 기능으로 설계된 것이 아니라, PAYG 요금제 고객이 Copilot Studio 메이커 포털에 접근할 수 있도록 하는 **라이선스 접근 제어 메커니즘**으로 만들어졌습니다. 이 설정이 없으면 순수 PAYG 과금제 고객은 메이커 포털 접근 권한을 부여받을 지원되는 방법이 없었습니다.

## 왜 이름을 바꾸나

새로운 Copilot Studio UI가 도입되면서, 많은 사용자가 이 설정의 이름("Authors")만 보고 "누가 Copilot Studio에 접근할 수 있는지를 제어하는 기능"으로 오해하는 피드백이 접수됐습니다. 이번 명칭 변경은 설정의 실제 의도 — 즉 PAYG 과금 방식 사용 권한 제어 — 를 더 명확히 드러내기 위한 것입니다.

## 조치 사항

이 메시지는 공지용이며, 별도 조치는 필요하지 않습니다. 기능 자체의 동작은 바뀌지 않습니다.

## 한국 조직을 위한 체크포인트

사내 Power Platform 거버넌스 문서나 교육 자료에서 "Copilot Studio Authors" 설정을 언급했다면, 새 이름인 "Copilot Studio pay-as-you-go users"로 갱신해 두는 것이 좋습니다. 특히 PAYG 과금 방식으로 Copilot Studio를 운영 중인 조직이라면 이 설정이 메이커 포털 접근 권한과 직결된다는 점을 다시 확인해둘 만합니다.

---

> **원문**: Power Platform admin center – Update to the Copilot Studio Authors feature name (MC1483430) — [mc.merill.net에서 보기](https://mc.merill.net/message/MC1483430) | [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
