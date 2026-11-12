---
title: "Copilot Studio 에이전트, 어디서 관리할까? 다섯 가지 목표로 정리하는 거버넌스"
date: 2026-11-12T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Agent365
  - PowerPlatform
  - MicrosoftEntra
  - MicrosoftPurview
  - MicrosoftDefender
  - Governance
excerpt: "Copilot Studio 에이전트의 거버넌스는 하나의 관리 센터만으로 끝나지 않습니다. Microsoft가 제시한 다섯 가지 관리 목표를 바탕으로 Power Platform, Entra, Purview, Agent 365, Defender의 역할과 운영팀 간 인계 지점을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio 에이전트, 어디서 관리할까? 다섯 가지 목표로 정리하는 거버넌스

Copilot Studio 에이전트가 질문에 답하는 수준을 넘어 업무를 직접 수행하기 시작하면, 관리자의 질문도 달라집니다. “누가 만들었나?”뿐 아니라 **어떤 계정으로 실행되고, 어디까지 접근하며, 무슨 정보를 내보내고, 비용은 얼마나 쓰는가**를 함께 확인해야 합니다.

Microsoft가 2026년 11월 11일 공개한 *Where do I govern my Copilot Studio agents?*는 이 문제를 관리 포털 목록이 아니라 **다섯 가지 거버넌스 목표와 담당자의 역할**로 설명합니다. 지원되는 에이전트는 agent user account를 통해 자신의 Microsoft 365 계정과 디렉터리 프로필, 조직도상 관계를 갖고, 범위가 정해진 권한으로 Teams와 Outlook 업무에 참여할 수 있기 때문입니다.

원문이 인용한 Microsoft 보고에서는 직원의 **29%가 승인되지 않은 AI 에이전트를 업무에 사용한 경험**이 있으며, **조사 대상 조직의 데이터 보안 사고 중 32%가 생성형 AI 도구와 관련**된 것으로 설명합니다. 두 수치는 서로 다른 지표이며, Copilot Studio만의 사고율이나 국내 조직의 통계로 해석해서는 안 됩니다.

![Copilot Studio 에이전트 거버넌스 개요](/mwkorea/assets/images/2026-11-12-CopilotStudioLayeredGovernance/image1.png)

---

## 먼저 보는 역할 분담: Agent 365가 모든 통제를 대체하지는 않습니다

| 관리 목표 | 주도하는 담당자 | 주요 관리 도구 |
|---|---|---|
| 메이커가 안전하게 개발하고 확장하도록 지원 | Power Platform 관리자 | Power Platform admin center |
| 에이전트 ID와 리소스 접근 제어 | ID 및 액세스 관리자 | Microsoft Entra |
| 입력·출력 정보 보호 | 컴플라이언스 관리자, 데이터 보안팀 | Microsoft Purview |
| 조직 전체 가시성, 소유권, 사용량과 가치 확인 | AI 관리자 | Microsoft Agent 365 |
| 위협 탐지와 사고 대응 | 보안 관리자, SOC 분석가 | Microsoft Defender |

![에이전트 거버넌스의 다섯 가지 목표와 담당 관리자](/mwkorea/assets/images/2026-11-12-CopilotStudioLayeredGovernance/image2.png)

핵심은 **중앙에서 현황을 보고, 전문 통제는 해당 담당자가 자신의 도구에서 수행한다**는 것입니다. Agent 365에서 문제가 보이더라도 권한 검토는 Entra, 정보 노출 평가는 Purview, 위협 조사는 Defender, 환경·커넥터 변경은 Power Platform 관리 영역으로 이어집니다.

## 1. 메이커에게 개발 공간을 주되, 운영으로 가는 길을 정합니다

모든 메이커를 기본 환경에 모으면 일관된 통제가 어려워지고, 반대로 아이디어를 시험할 때마다 개별 승인을 요구하면 도입이 느려집니다. Power Platform 관리자는 **개인 개발에서 팀 공유, 운영 배포로 이어지는 경로**를 먼저 설계해야 합니다.

원문이 제시한 조합은 다음과 같습니다.

- **Environment routing**: 메이커를 기본 환경에만 두지 않고 개인 개발 환경으로 안내합니다.
- **Environment groups와 rules**: 여러 환경에 공통 설정을 일관되게 적용합니다.
- **Advanced connector policies**: 승인한 커넥터와 작업만 허용하고 나머지는 기본 차단하는 허용 목록을 구성합니다.
- **Sharing controls**: 에이전트가 배포·공유되는 범위를 제한합니다.

에이전트의 계정 권한이 넓어지더라도, 환경에서 허용하지 않은 연결과 기능까지 마음대로 사용할 수 있는 것은 아닙니다. 따라서 **계정 권한의 최소화와 플랫폼의 허용 목록을 함께 적용**해야 합니다.

![Power Platform 관리 센터의 환경 라우팅 설정](/mwkorea/assets/images/2026-11-12-CopilotStudioLayeredGovernance/image3.png)

실무에서는 개발 환경을 제공하는 것과 함께 “어떤 데이터·커넥터·공유 범위까지 허용되는가”를 메이커에게 알려주는 편이 좋습니다. 환경 통제는 초기 개발 때만 쓰는 장치가 아니라 배포 범위가 넓어져도 유지해야 하는 경계입니다.

## 2. 에이전트 ID, 사용자 위임, 에이전트 사용자 계정을 구분합니다

처음에는 적절했던 권한도 에이전트에 기능이나 연결이 추가되면 과도해질 수 있습니다. ID 및 액세스 관리자는 Microsoft Entra에서 **실행 주체를 식별하고, 리소스 접근 범위와 접근 조건을 주기적으로 검토**해야 합니다.

[Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/manage-agent-identities-admin)는 에이전트 ID 관리 기능을 제공합니다. 에이전트용 Conditional Access는 **지원되는 접근 패턴**에 조건을 적용합니다.

특히 다음 세 가지를 같은 것으로 취급하면 안 됩니다.

- 에이전트 자체의 ID
- 사용자를 대신해 동작하는 에이전트의 위임 접근
- 자체 사용자 계정을 가진 에이전트의 접근

각 방식은 접근 권한과 관리 방식이 동일하지 않습니다. “사용자의 권한을 그대로 따른다”는 설명을 모든 에이전트에 일괄 적용하지 말고, 실제 사용하는 계정·인증 패턴을 먼저 확인해야 합니다.

![Microsoft Entra에서 에이전트의 액세스 패키지를 구성하는 화면](/mwkorea/assets/images/2026-11-12-CopilotStudioLayeredGovernance/image4.png)

## 3. 접근할 수 있는 정보와 공개해도 되는 정보는 다릅니다

어떤 문서에 정상적인 접근 권한이 있다고 해서, 그 내용을 모든 대화 상대에게 전달해도 되는 것은 아닙니다. 데이터 보안팀과 컴플라이언스 관리자는 **에이전트가 사용하는 정보뿐 아니라 생성하고 전달하는 결과물**도 살펴야 합니다.

Microsoft Purview에서는 다음 수단을 조합합니다.

- **Data Security Posture Management**로 AI 관련 데이터 위험 파악
- 정보 분류와 **민감도 레이블** 적용
- **Data Loss Prevention(DLP)**으로 부적절한 정보 이동 통제
- **감사**를 통한 사용 이력과 행위 가시성 확보

다만 보호 범위는 에이전트와 상호작용 유형에 따라 다릅니다. 지원 시나리오를 확인하고 필요한 경우 해당 에이전트 인스턴스를 정책에 포함해야 합니다. Copilot Studio의 데이터 정책은 연결과 기능을 통제하는 보완 수단이지, Purview의 정보 보호를 대체하는 수단이 아닙니다.

![Microsoft Purview에서 민감도 레이블을 설정하고 관리하는 화면](/mwkorea/assets/images/2026-11-12-CopilotStudioLayeredGovernance/image5.png)

자체 사용자 계정을 가진 에이전트는 자신의 접근 권한과 지식 범위를 가질 수 있습니다. 사용자 위임만을 전제로 검토하지 말고, **과도한 공유와 외부 유출 위험을 별도로 확인**하는 것이 중요합니다.

## 4. Agent 365로 전체 지도를 보고, 소유권과 비용을 연결합니다

에이전트가 여러 부서와 플랫폼에 퍼지면 개별 환경만 봐서는 조직 전체 현황을 이해하기 어렵습니다. AI 관리자는 Agent 365를 중심으로 무엇이 존재하고, 누가 소유하며, 어떻게 사용되고, 어떤 에이전트가 점검 대상인지 연결합니다.

원문에 따르면 Copilot Studio 에이전트는 Microsoft 365 관리 센터의 **agent registry**에 Microsoft 및 타사 에이전트와 함께 표시되며, 사용 현황 인사이트는 기본 활성화됩니다. **Agent map**은 에이전트와 사용자·도구의 연결 관계를 보여줍니다.

![에이전트와 사용자·도구의 연결 관계를 보여주는 Agent 365 지도](/mwkorea/assets/images/2026-11-12-CopilotStudioLayeredGovernance/image6.png)

에이전트 상세 페이지에서는 소유권, 사용량, 보안 신호를 살펴보고 관련 관리자에게 조치를 넘깁니다. 각 담당자는 자신의 기존 권한으로 해당 포털에서 작업합니다.

또한 **tool governance**로 플러그인·스킬·커넥터를 누구에게 제공할지 관리하고, 비용 관리에서는 **Copilot Credit 사용량, 지출 정책, 알림**을 확인합니다. 등록된 에이전트 수만 세는 것이 아니라 사용·지출과 업무상 가치를 함께 검토하는 구조입니다.

Agent 365는 Power Platform, Entra, Purview, Defender의 통제를 **보완하고 연결**합니다. 표시되는 정보와 가능한 조치는 에이전트 종류, 게시 상태, 도구 유형에 따라 달라집니다.

## 5. 위협 대응은 SOC와 에이전트 운영팀이 함께 수행합니다

사전 정책만으로 모든 위험을 제거할 수는 없습니다. 원문은 지침을 무시하게 만드는 **jailbreak**, 메일·문서·웹 페이지에 숨은 **prompt injection**, 과도한 권한을 가진 도구의 오용, 비정상적인 활동량 증가를 예로 듭니다.

보안 관리자와 SOC 분석가는 Microsoft Defender에서 에이전트 보안 상태와 위협을 조사합니다. 실시간 보호는 **지원되고 구성된 시나리오**에 적용되므로 모든 에이전트가 등록만으로 자동 보호된다고 가정하면 안 됩니다.

![Microsoft Defender에서 에이전트 관련 보안 사고를 조사하는 화면](/mwkorea/assets/images/2026-11-12-CopilotStudioLayeredGovernance/image7.png)

원문이 설명하는 협업 흐름은 다음과 같습니다.

1. AI 관리자가 경고를 에이전트와 소유자에게 연결해 업무 목적과 접근 범위를 제공합니다.
2. SOC가 발생한 일을 재구성하고, ID 관리자가 계정 권한을 점검하거나 제한합니다.
3. 컴플라이언스 관리자가 민감정보 노출 여부를 평가합니다.
4. Power Platform 관리자가 커넥터·공유·환경 설정을 변경하거나 에이전트를 비활성화합니다.

이 흐름은 모든 조치를 한 사람이 순서대로 수행하라는 뜻이 아닙니다. 필요한 전문팀이 같은 에이전트 맥락을 공유하고, 조사 결과를 다음 권한·데이터·플랫폼 정책 개선에 반영하라는 의미입니다.

## 우리 조직에서 시작하는 방법

다음은 원문의 프레임워크를 도입 담당자가 실행 항목으로 바꾼 체크리스트입니다.

1. 다섯 가지 관리 목표마다 주담당자와 에스컬레이션 경로를 정합니다.
2. 운영 전환, 새 리소스 연결, 공유 대상 확대 때 다른 관리자의 검토가 필요한 조건을 합의합니다.
3. [Power Platform 관리 센터 안내](https://learn.microsoft.com/en-us/power-platform/admin/admin-documentation)를 참고해 개발 환경 라우팅, 환경 그룹, 커넥터 정책을 마련합니다.
4. [Microsoft Agent 365 시작하기](https://learn.microsoft.com/en-us/microsoft-agent-365/get-started)를 참고해 전체 에이전트의 가시성과 소유권을 확인합니다.
5. 소유권·권한·정보 보호·사용량·위험을 정기적으로 함께 검토합니다.

**이 글은 2026년 11월 11일 원문의 거버넌스 안내를 정리한 것이며, 개별 기능의 GA 또는 프리뷰 전환을 일괄 발표하는 글은 아닙니다.** 실제 도입 시에는 연결된 공식 문서에서 현재 지원 범위와 구성 요건을 확인해야 합니다.

## 마무리: 포털보다 해결할 문제를 먼저 정하세요

“어느 관리 센터로 들어가야 하나?”보다 먼저 물어야 할 것은 **“지금 해결하려는 문제가 무엇인가?”**입니다. 소유자가 없는 에이전트, 과도한 권한을 얻은 에이전트, 민감정보를 노출할 수 있는 에이전트는 서로 다른 대응을 요구합니다.

Copilot Studio 거버넌스의 핵심은 포털을 하나로 줄이는 데 있지 않습니다. 메이커의 개발 속도를 살리면서 환경, ID, 정보 보호, 가시성, 위협 대응의 경계를 연결하고 **팀 사이의 인계를 명확히 하는 것**에 있습니다.

---

> 출처: Microsoft Copilot Studio Blog, [Where do I govern my Copilot Studio agents?](https://techcommunity.microsoft.com/t5/copilot-studio-blog/where-do-i-govern-my-copilot-studio-agents/ba-p/4572592), 2026년 11월 11일(원문 표시일). 자세한 내용은 원문 참조.
