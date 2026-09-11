---
title: "장애 알림 이후의 일까지: Microsoft 네트워크 운영을 돕는 AI 에이전트 3종"
date: 2026-09-11T00:00:00 KST
categories:
  - Copilot
tags:
  - InsideTrack
  - AIAgents
  - CopilotStudio
  - MicrosoftFoundry
  - MicrosoftAgentFramework
  - NetworkOperations
  - Governance
excerpt: "Microsoft Digital은 네트워크 장애의 진단, 다른 팀과의 작업 인계, 상황 전파를 각각 담당하는 AI 에이전트를 운영하고 있습니다. Falcon·Smart Bonding·Network Outage Insights의 역할과 권한 설계, 초기 운영 성과를 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 장애 알림 이후의 일까지: Microsoft 네트워크 운영을 돕는 AI 에이전트 3종

네트워크 장애 대응은 문제 장비를 찾는 것만으로 끝나지 않습니다. 현재 로그를 다시 모으고, 현장 팀이나 통신사에 일을 넘기고, 영향을 받는 사용자에게 상황을 알린 뒤 복구 여부까지 확인해야 합니다. 담당자는 그 사이 여러 시스템을 오가게 됩니다.

Microsoft Inside Track은 사내 IT 조직인 **Microsoft Digital**이 이 반복 업무에 AI 에이전트를 적용한 사례를 공개했습니다. 하나의 거대한 자동화 도구를 만드는 대신 진단·실행, 작업 인계, 장애 커뮤니케이션을 나눠 맡기고, Teams와 내부 인시던트 관리 도구 **ICM**에 연결한 접근입니다.

---

## 월 7만 건의 수작업 티켓에서 출발

원문이 소개한 Microsoft 환경은 900곳 이상의 사이트, 500개 데이터센터, 75,000대 이상의 장비, 300,000명 이상의 사용자, 100만 개가 넘는 연결 엔드포인트를 포함합니다.

사람의 개입이 필요한 월별 티켓은 2025년 1월 최대 **70,000건**까지 늘었습니다. 이후 **18개월 동안 자동화와 AI를 적용해 약 27,000건**으로 줄였다고 설명합니다. 이 감소분 전체를 아래 세 에이전트만의 성과로 돌려서는 안 됩니다. 원문은 기존 자동화와 AI를 적용한 전체적인 진전을 먼저 설명한 뒤 개별 에이전트 사례를 소개합니다.

![Microsoft Digital에서 네트워크 운영을 담당하는 Neeraj Mohan](/mwkorea/assets/images/2026-09-11-AIAgentsNetworkOperations/image1.png)

남은 티켓에도 현재 장비 상태, 인접 장비, 링크, 로그, 이전 조치 기록을 보강하는 일이 필요합니다. 원격으로 끝낼 수 없는 장애는 현장 지원이나 협력사 작업 일정까지 조율해야 합니다. 팀은 티켓과 수작업을 분석해 영향도, 사용자 필요, 개발 노력을 기준으로 우선순위를 정했습니다.

## 역할은 나누고 기존 업무 도구에 연결

| 에이전트 | 주된 역할 | 통제에서 중요한 부분 |
|---|---|---|
| Falcon Agent | 최신 진단, 로그 조회, 도달 가능 여부와 서비스 복구 확인 | 실행 요청은 적절한 엔지니어와 보안 관리 워크스테이션으로 제한 |
| Smart Bonding Agent | 문제·담당 팀 추천, 티켓 생성·추적, 작업 시간 조율 | 티켓 생성 전 사람의 승인 |
| Network Outage Insights Agent | 장애 알림, 자연어 질의 응답, 상황 보고 | 영향을 받는 담당자에게 필요한 정보를 전달 |

구현에 사용한 기술로는 **Azure OpenAI, Microsoft Foundry, Microsoft Agent Framework, Microsoft Copilot Studio, Microsoft Teams**가 소개됩니다. 이들은 Microsoft의 내부 운영 환경에 맞춰 만든 에이전트입니다. 같은 이름의 완제품 세 종이 모든 고객에게 출시됐다는 발표는 아닙니다.

## Falcon Agent: 오래된 진단을 다시 실행하고 결과를 갱신

기존 Falcon은 액세스 포인트 장애처럼 알려진 시나리오에 대한 자동 진단과 복구를 지원했습니다. 서비스 팀이 시나리오와 절차를 한 번 등록하면 반복 티켓에 같은 조치를 적용할 수 있는 방식입니다.

Falcon Agent는 여기에 **필요한 시점에 최신 상태를 다시 확인하는 기능**을 더합니다. 아침에 실행된 결과를 오후 담당자가 그대로 참고하면 이미 상태가 달라졌을 수 있기 때문입니다. 권한이 있는 엔지니어는 진단을 갱신하고 최신 로그, 장비 도달 가능 여부, 서비스 복구 상태를 확인하며 티켓의 요약과 정보를 보강할 수 있습니다.

![Teams와 ICM 안에서 Falcon을 사용할 수 있도록 설계한 제품 담당자 Shayoni](/mwkorea/assets/images/2026-09-11-AIAgentsNetworkOperations/image2.png)

정보를 묻는 요청과 실제 장비에 작업을 수행하는 요청은 구분합니다. **실행 요청은 보안 관리 워크스테이션(SAW)을 사용하는 적절한 엔지니어에게 제한**하고, 정보 조회는 장비 제어 권한을 노출하지 않는 범위에서 더 넓은 사용자에게 제공합니다.

## Smart Bonding Agent: 시스템을 넘나드는 작업 인계

케이블을 다시 연결하거나 현장에서 장비를 점검하거나 통신사에 회선 장애를 의뢰해야 한다면, 다음 단계는 원격 진단이 아니라 조율입니다. Smart Bonding Agent는 그 인계 과정에서 맥락이 끊기지 않도록 돕습니다.

1. **추천 에이전트**가 인시던트를 살펴 예상 문제와 참여할 팀을 식별합니다.
2. **티켓 관리 에이전트**가 사람의 승인을 받은 뒤 적절한 티켓을 생성하고 변경 사항을 추적합니다.
3. **작업 시간 조율 흐름**이 Microsoft 엔지니어의 도움이 필요한 경우 관련 담당자를 연결합니다.

![Smart Bonding Agent를 담당하는 Suvodip Moitra](/mwkorea/assets/images/2026-09-11-AIAgentsNetworkOperations/image3.png)

사람의 승인은 의도적으로 남긴 단계입니다. 내부 팀의 일을 줄이려다 협력사에 불필요한 티켓을 쏟아내지 않기 위해서입니다. 신뢰가 쌓이면 위험이 낮은 작업부터 자동화를 확대하는 방향입니다.

원문에 따르면 Global Datacenter Operations와 Puget Sound Network Operations를 이미 지원하며, 문제 유형과 통신사·네트워크 장비 공급업체 범위를 확대하고 있습니다.

## Network Outage Insights Agent: 알림과 질문 응답을 한곳에서

장애가 나면 엔지니어 외에도 지역 IT 관리자, 경영진, 헬프데스크가 상황을 알아야 합니다. **Copilot Studio로 만든 Network Outage Insights Agent**는 정보를 먼저 전달하는 방식과 필요할 때 질문하는 방식을 함께 지원합니다.

영향을 받는 IT 관리자에게 Teams 알림을 보내고, “우리 캠퍼스에 진행 중인 사이트 장애가 있나요?” 같은 자연어 질문에도 답합니다. 응답에는 인시던트 링크, 현재 상태, 예상 해결 시간, 영향, 지역별 정보와 과거 추세가 포함될 수 있습니다.

![장애 커뮤니케이션과 사용자 피드백을 담당하는 Laxman Bhinnale](/mwkorea/assets/images/2026-09-11-AIAgentsNetworkOperations/image4.png)

사용자 피드백도 백로그에서 추적하고 요청한 사람에게 개선 결과를 연결합니다. 단순히 답변을 제공하는 데 그치지 않고 운영 과정에서 개선할 항목을 모으는 방식입니다.

## 초기 성과는 수치의 범위를 나눠 읽어야 합니다

| 지표 | 원문이 보고한 결과 |
|---|---|
| Falcon Agent 사용자 시간 절감 | 운영 초기 몇 달 동안 약 300시간, 티켓당 10~15분 |
| Falcon Agent 유지율 | 60% |
| Falcon Agent 긍정적 사용자 피드백 | 100% |
| Falcon이 현재 처리할 수 있는 인시던트 비중 | 전체의 약 60% |
| 시나리오 성숙 후 기대하는 처리 비중 | 약 80% |
| Network Outage Insights의 월간 사례 | 장애 149건, 커뮤니케이션·보고에 32시간 절감 |

여기서 **80%는 현재 달성한 수치가 아니라 기대치**입니다. 사용자 유지율 60%와 인시던트 처리 범위 약 60%도 서로 다른 지표입니다. 긍정적 피드백 100% 역시 원문이 보고한 사용자 의견이며, 오류가 없거나 모든 조직에서 동일한 효과를 낸다는 보장은 아닙니다.

원문은 영향 측정이 아직 초기라고 설명합니다. 고객 조직에서 평가할 때는 티켓 종류, 사용 기간, 응답 품질, 다시 사용하는 사용자 비율 등을 함께 기록해야 결과를 제대로 해석할 수 있습니다.

## 다음 단계는 에이전트 사이의 연결

향후 구상은 Smart Bonding이 적절한 내부·외부 팀을 연결하고, Falcon이 복구를 확인하며, 장애 정보 에이전트가 영향과 회복 상태를 전달한 뒤 사후 분석 에이전트가 보고서를 만드는 흐름입니다. 이는 원문이 **앞으로 연결하려는 운영 방식**으로 설명한 내용이지 전체 흐름이 이미 완성됐다는 뜻은 아닙니다.

![다중 에이전트 협업 방향을 설명한 Raghavendran Loganathan](/mwkorea/assets/images/2026-09-11-AIAgentsNetworkOperations/image5.png)

이 사례를 적용할 때 Microsoft의 네트워크 구조나 티켓 시스템을 그대로 복제할 필요는 없습니다. 먼저 자체 텔레메트리와 티켓에서 반복 업무를 찾고, 읽기 전용 정보 제공이나 사람이 승인하는 작업으로 범위를 좁혀 시작할 수 있습니다.

사용자가 이미 일하는 도구에 에이전트를 배치하고, 조회와 실행 권한을 분리하며, 민감하거나 협력사에 영향을 주는 작업에는 승인 단계를 두세요. 성공 여부는 에이전트 수보다 **담당자가 다시 사용하는지, 수작업과 인계 누락이 줄었는지**로 판단하는 것이 이 사례의 실무적 교훈입니다.

---

> **출처**
>
> - Microsoft Inside Track: [From alerts to action: How AI agents are reshaping network operations at Microsoft](https://www.microsoft.com/insidetrack/blog/from-alerts-to-action-how-ai-agents-are-reshaping-network-operations-at-microsoft/)
>
> 자세한 내용은 원문 참조. 본문 수치는 Microsoft 내부 운영 사례에서 보고한 결과이며 일반적인 성능 보장을 뜻하지 않습니다.
