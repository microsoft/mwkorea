---
title: "Copilot Cowork 커넥터, 관리 센터에서 통제합니다: Power Platform DLP는 적용되지 않습니다"
date: 2026-11-07T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotCowork
  - PowerPlatform
  - Connectors
  - Agents
  - Automations
  - Governance
  - Microsoft365AdminCenter
excerpt: "Copilot Cowork의 지원되는 Power Platform 커넥터를 Microsoft 365 관리 센터에서 허용·차단할 수 있게 됩니다. 정책은 기존 연결의 작업 실행과 Cowork Automations에도 적용되지만, Power Platform 관리 센터의 DLP 정책은 Cowork에 적용되지 않으므로 별도의 거버넌스 검토가 필요합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Cowork 커넥터, 관리 센터에서 통제합니다: Power Platform DLP는 적용되지 않습니다

Copilot Cowork가 외부 업무 서비스에 연결해 작업을 수행한다면, 관리자는 어떤 커넥터를 허용할지 결정해야 합니다. 자동화가 연결된 서비스에서 행동하는 만큼, 사용자 편의와 함께 중앙 통제의 범위도 중요해집니다.

Microsoft는 **플러그인으로 게시된 Power Platform 커넥터**를 Cowork에서 지원하고, 지원되는 커넥터의 사용 가능 여부를 **Microsoft 365 관리 센터**에서 관리하도록 안내했습니다. Cowork는 연결 생성과 작업 실행 때 이 설정을 따릅니다.

MC1542062의 발행 시각은 한국시간 2026년 11월 7일이며, 원문은 전 세계 일반 공급 배포가 **2026년 11월 중순까지 완료될 예정**이라고 설명합니다. 특히 도입 전에 확인할 사항은 **Power Platform 관리 센터의 DLP 정책이 Cowork에는 적용되지 않는다**는 점입니다.

---

## 커넥터 허용·차단을 한곳에서 관리합니다

이번 변경은 Cowork를 지원되는 타사 애플리케이션·서비스로 확장하면서, 관리자가 커넥터 가용성을 중앙에서 통제할 수 있도록 합니다.

설정 위치는 **Microsoft 365 관리 센터 → Agents → Tools**입니다. 관리자는 이곳에 표시되는 지원 커넥터를 검토하고 조직의 요구에 따라 허용하거나 차단할 수 있습니다.

“Power Platform 커넥터 지원”은 모든 커넥터가 동시에 제공된다는 뜻은 아닙니다. 원문은 **추가 커넥터가 Microsoft 365 관리 센터에 순차적으로 추가되며, 추가된 커넥터가 Cowork에서 사용 가능해진다**고 설명합니다. 실제 지원 목록은 관리 센터에서 확인해야 합니다.

## 이미 만든 연결과 자동화도 정책 대상입니다

| 적용 지점 | 원문이 안내하는 동작 |
|---|---|
| 새 연결 생성 | Microsoft 365 관리 센터의 커넥터 설정 준수 |
| 커넥터 작업 실행 | 관리 센터의 설정 준수 |
| 차단 전에 생성된 연결의 작업 실행 | 차단 설정 적용 |
| Cowork Automations | 커넥터 정책 적용 |
| 기존 메일·캘린더·Teams·파일 기능 | 이번 변경의 영향 없음 |

눈여겨볼 부분은 **차단 전에 만들어 둔 연결도 작업 실행 시 정책을 따른다**는 점입니다. 차단이 신규 연결 생성에만 적용되고 기존 연결에는 적용되지 않는 방식이 아닙니다.

또한 정책은 Cowork Automations에도 적용됩니다. 따라서 조직이 커넥터를 차단한다면, 그 커넥터에 의존하는 자동화 작업에도 영향을 줄 수 있음을 함께 검토해야 합니다. 원문은 연결 삭제 여부나 자동화 실패 시 구체적인 오류 메시지까지 설명하지는 않으므로, 실제 동작은 조직 환경에서 확인하는 것이 좋습니다.

## Power Platform DLP가 자동으로 따라오지는 않습니다

이번 공지의 가장 중요한 거버넌스 경계는 다음과 같습니다.

> **Power Platform 관리 센터의 Data Loss Prevention(DLP) 정책은 Cowork에 적용되지 않습니다.**

같은 Power Platform 커넥터를 사용한다고 해서 Power Platform 관리 센터에서 설정한 DLP가 Cowork의 연결·작업에도 자동 적용된다고 가정하면 안 됩니다.

이번에 안내된 제어는 Microsoft 365 관리 센터에서 **지원 커넥터의 사용 가능 여부를 허용·차단**하는 것입니다. 이를 Power Platform DLP의 모든 정책 기능과 동일한 보호라고 해석해서도 안 됩니다.

그렇다고 이 공지가 “Cowork에는 어떠한 보호도 없다”고 말하는 것은 아닙니다. 명확하게 확인된 사실은 **Power Platform 관리 센터 DLP가 적용되지 않고, 지원 커넥터의 가용성은 Microsoft 365 관리 센터가 통제한다**는 범위입니다.

## 도입 담당자가 준비할 사항

원문은 관리자가 사용 가능한 커넥터를 검토하고, 조직 요구에 맞게 설정하며, 활성화 전에 거버넌스 요구를 확인할 것을 권고합니다. 실무에서는 다음과 같이 준비할 수 있습니다.

1. **Agents → Tools**에서 현재 지원되는 Power Platform 커넥터를 확인합니다.
2. 어떤 타사 애플리케이션·서비스와 연결할지, 업무 목적과 필요한 데이터 범위를 검토합니다.
3. 조직 정책에 따라 커넥터 허용·차단을 설정합니다.
4. 기존 연결과 Cowork Automations가 해당 커넥터에 의존하는지 확인합니다.
5. Power Platform DLP가 적용된다는 전제 없이 보안·데이터 거버넌스 요구를 다시 검토합니다.

예를 들어 한 부서가 타사 업무 시스템으로 반복 작업을 자동화하려는 경우, 먼저 관리 센터에 해당 커넥터가 지원되는지 확인해야 합니다. 지원 여부와 허용 설정을 확인한 뒤, 조직의 데이터 정책에 적합한지를 검토하는 순서가 필요합니다. 이는 도입을 이해하기 위한 예시이며, 원문이 특정 타사 서비스 지원을 보장하는 것은 아닙니다.

## 일정과 변경 범위

원문은 이 변경의 **General Availability, Worldwide 배포 완료 예정 시점을 2026년 11월 중순**으로 안내합니다. 모든 조직에서 지금 즉시 동일한 커넥터 목록이 보인다는 의미는 아니므로, 테넌트의 실제 설정 화면을 확인하세요.

기존 Microsoft 365의 **메일·캘린더·Teams·파일 기능은 이번 변경으로 영향을 받지 않습니다.** 변경 범위는 Cowork의 지원되는 Power Platform 커넥터 통합과 그 가용성 통제입니다.

## 마무리

Cowork에 외부 업무 연결이 확대되는 것은 활용 범위를 넓혀 줍니다. 동시에 관리자는 **커넥터 지원 목록, 기존 연결의 실행 통제, 자동화 영향, DLP 적용 경계**를 함께 확인해야 합니다.

이번 공지를 도입 체크리스트로 요약하면 “Microsoft 365 관리 센터에서 허용된 커넥터만 사용하도록 검토하고, Power Platform DLP가 Cowork까지 보호한다고 가정하지 않는다”입니다. 일정과 지원 범위는 원문 시점 기준이며 실제 테넌트 제공 상태가 달라질 수 있습니다.

> 출처: **MC1542062** — [Copilot Cowork: Power Platform connectors now follow Microsoft 365 admin center settings](https://mc.merill.net/message/MC1542062). 원문에는 개별 Roadmap ID가 기재되어 있지 않습니다. [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)에서 후속 공개 정보를 확인할 수 있습니다. 실제 출시 일정·기능은 변경될 수 있습니다.
