---
title: "Microsoft 365 E5·E7에 Security Copilot 포함: 기본 제공량과 추가 비용 구분하기"
date: 2026-09-25T00:00:00 KST
categories:
  - Copilot
tags:
  - SecurityCopilot
  - Microsoft365
  - MicrosoftDefender
  - MicrosoftPurview
  - Licensing
excerpt: "Microsoft 365 E5·E7 조직에 Security Copilot 기능과 에이전트가 포함된다는 공지가 나왔습니다. 월별 SCU 제공량과 상한, 포함 혜택 밖에서 발생할 수 있는 비용을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Microsoft 365 E5·E7에 Security Copilot 포함: 기본 제공량과 추가 비용 구분하기

보안팀이 AI 에이전트를 업무에 도입할 때는 기능만큼 라이선스와 사용량을 먼저 확인해야 합니다. MC1478465는 Microsoft 365 **E5 또는 E7**을 보유한 조직이 기존 권한의 일부로 Security Copilot 기능과 에이전트를 이용할 수 있다고 안내합니다.

별도 구매 없이 포함된다는 점은 반갑지만, 모든 연계 서비스가 무제한 무료라는 뜻은 아닙니다. 포함된 컴퓨팅 제공량과 혜택 밖의 과금 항목을 나누어 이해해야 합니다.

---

## 어디에서 사용할 수 있나요?

원문이 열거한 서비스는 **Microsoft Defender, Entra, Intune, Purview, Security Copilot 포털**입니다. 각 보안 업무 흐름에서 핵심 에이전트 경험을 사용할 수 있으며, 사용자 지정 에이전트와 통합을 만드는 개발 도구 및 API도 제공된다고 설명합니다.

기존 보안·컴플라이언스·접근 정책은 계속 적용됩니다. 라이선스에 기능이 포함되었다고 해서 조직의 기존 권한과 통제가 사라지는 것은 아닙니다.

## 포함된 월별 SCU 제공량

| 항목 | 공지 내용 |
|---|---|
| 기준 제공량 | 라이선스 사용자 1,000명당 월 400 Security Compute Units(SCU) |
| 월별 상한 | 테넌트당 최대 10,000 SCU |
| 별도 구매 | 포함 혜택을 위한 별도 구매 불필요 |
| 활성화 작업 | 원문은 별도 조치 불필요로 안내 |

원문은 1,000명 단위 미만 인원의 산정 방식, 이월, 초과 사용 처리의 세부 규칙까지 설명하지 않습니다. 예산을 확정할 때는 실제 테넌트에 표시되는 권한과 사용량 조건을 추가 확인해야 합니다.

## 추가 비용 가능성이 있는 항목

공지에는 포함된 권한 밖에서 추가 요금이 발생할 수 있는 다음 항목이 명시되어 있습니다.

- **Microsoft Sentinel data lake**의 컴퓨팅 또는 스토리지
- Purview의 **비에이전트형 Data Security Investigations**
- Security Copilot과 함께 사용하는 **Azure Logic Apps**
- **Microsoft Security Store**에서 구매하는 타사 에이전트

따라서 Copilot 자체의 제공량뿐 아니라 연결된 워크플로와 외부 에이전트 구매까지 비용 검토 범위에 넣는 것이 좋습니다.

## “오늘부터”는 누구에게 해당하나요?

원문은 해당 공지를 받은 조직이 **“beginning today”** 혜택을 이용할 수 있다고 표현합니다. 이 글은 공개 Message Center 아카이브의 내용을 설명하는 것이므로, 모든 한국 고객의 활성화 날짜를 동일한 날로 확정하는 근거로 사용해서는 안 됩니다.

대상 조직은 Microsoft 365 E5·E7이며, 기능을 켜기 위한 별도 조치는 없다고 안내합니다. 이 혜택에서 제외되기를 원하는 경우에는 [Microsoft 지원](https://support.microsoft.com/topic/customer-service-phone-numbers-c0389ade-5640-e588-8b0e-28de8afeb3f2)에 문의하도록 되어 있습니다.

## 보안팀의 첫 점검

실무 적용 전에는 테넌트의 제공량과 접근 권한을 확인하고, 어떤 보안 워크플로부터 시작할지 정리하세요. “포함 라이선스로 시작할 수 있다”는 것과 “연계 비용 없이 모든 작업을 수행한다”는 것을 구분하는 것이 이번 공지를 읽는 핵심입니다.

> 출처: [MC1478465 — Security Copilot is now included as part of your Microsoft 365 E5/E7 plan](https://mc.merill.net/message/MC1478465)  
> [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap) — 원문에 개별 Roadmap ID는 명시되어 있지 않습니다.  
> 실제 출시 일정·기능은 변경될 수 있습니다.
