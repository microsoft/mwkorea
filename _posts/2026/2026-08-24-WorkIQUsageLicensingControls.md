---
title: "Work IQ, 어디까지 라이선스에 포함될까? 사용 방식별 과금과 관리 설정"
date: 2026-08-24T00:00:00 KST
categories:
  - Copilot
tags:
  - WorkIQ
  - Microsoft365Copilot
  - CopilotStudio
  - GitHubCopilotHarness
  - MCP
  - CopilotCredits
  - Governance
excerpt: "Work IQ는 같은 이름을 쓰더라도 Microsoft 365 Copilot의 기본 기능으로 이용할 때와 에이전트 도구·API로 호출할 때 과금 조건이 다릅니다. 사용 방식별 라이선스 조건과 Microsoft 365·Power Platform 관리 센터에서 각각 설정해야 할 비용 통제를 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Work IQ, 어디까지 라이선스에 포함될까? 사용 방식별 과금과 관리 설정

에이전트가 메일과 회의, 채팅, 파일을 함께 살펴보고 답하려면 업무 맥락이 필요합니다. Work IQ는 사용자가 접근할 수 있는 정보와 연결된 업무 시스템을 바탕으로 이 맥락을 제공하는 Microsoft의 업무 인텔리전스 계층입니다.

도입할 때 혼동하기 쉬운 부분은 이름보다 **사용 방식**입니다. Microsoft 365 Copilot에 내장된 Work IQ를 이용하는 것과 Copilot Studio에 MCP 도구로 연결하는 것은 같은 과금 조건이 아닙니다. Microsoft 365 Copilot 라이선스가 있다는 이유만으로 모든 Work IQ 호출이 포함된다고 판단하면 안 됩니다.

MCSCAT의 「Work IQ: How It's Used, Licensed, and Controlled」를 바탕으로, 구현 방식을 고를 때와 비용 정책을 설정할 때 필요한 내용을 정리했습니다. 원문 발행일은 2026년 8월 24일이며, 아래 설명은 원문에 명시된 **2026년 9월 라이선싱 가이드**와 9월 9일 확인한 관련 Microsoft Learn 문서를 기준으로 합니다.

---

## 먼저 구분할 것: 내장 기능, 에이전트 도구, 직접 API 호출

Microsoft 365 Copilot은 답변을 업무 정보에 근거하도록 만드는 grounding에 Work IQ를 활용합니다. 선언형 에이전트는 이 Copilot 경험을 지침, 지식, 작업으로 구성하므로 별도의 Work IQ 연결이 필요하지 않습니다.

반면 Copilot Studio에서는 에이전트의 제작·실행 환경인 **harness**에 따라 지원 범위가 달라집니다. 통합 Work IQ를 MCP 도구로 추가하는 방식은 GitHub Copilot harness에서 지원하며, 자체 애플리케이션은 Work IQ API를 직접 호출할 수 있습니다.

![Work IQ의 업무 맥락 활용을 소개하는 MCSCAT 원문 이미지](/mwkorea/assets/images/2026-08-24-WorkIQUsageLicensingControls/image1.png)

| 사용 방식 | 연결·구성 방법 | 라이선스와 Copilot Credits |
|---|---|---|
| Microsoft 365 Copilot 라이선스 사용자의 기본 Copilot 경험 | Work IQ grounding 내장, 별도 연결 불필요 | 기본 grounding은 Microsoft 365 Copilot 경험에 포함 |
| Agent Builder로 만든 선언형 에이전트 | SharePoint, Copilot connectors 등 지원 지식 원본 선택 | 적격 Microsoft 365 Copilot 라이선스 사용자가 Microsoft 채널에서 이용하면 문서상 조건과 fair usage 범위 내 포함 |
| Microsoft 365 Agents Toolkit으로 만든 선언형 에이전트 | manifest에 SharePoint, 메일, Teams 메시지 등 필요한 지원 기능 선언 | 위와 동일한 조건 적용, 별도 Work IQ API 연결 불필요 |
| Cowork | 작업에 필요한 Work IQ 맥락을 기본으로 활용 | Microsoft 365 Copilot 라이선스와 사용량 기반 청구 활성화가 모두 필요하며 Copilot Credits 소비 |
| Copilot Studio의 Standard harness | 통합 Work IQ 연결 미지원 | 이 통합 방식의 과금 비교 대상이 아님 |
| Copilot Studio의 GitHub Copilot harness | 통합 Work IQ MCP 도구 추가 | Microsoft 365 Copilot 라이선스 보유 여부와 관계없이 Copilot Credits 소비 |
| 자체 클라이언트·애플리케이션 | Work IQ API 직접 호출 | Microsoft 365 Copilot 라이선스는 필수가 아니지만 호출 사용자의 사용량 기반 청구를 활성화해야 하며 Copilot Credits 소비 |

선언형 에이전트도 라이선스가 없는 사용자에게 무조건 무료는 아닙니다. Microsoft 365 Copilot 라이선스가 없는 사용자가 SharePoint나 Copilot connector 데이터를 사용하는 에이전트를 이용하면, 사용량 기반 청구가 활성화된 환경에서 Copilot Credits가 소비됩니다. 이는 **선언형 에이전트 사용에 대한 요금**이지 별도 Work IQ API 호출 요금이 아닙니다. Agent Builder와 Agents Toolkit 모두 이 구분을 적용하되, 제작 도구별 지원 사용자 조건도 함께 확인해야 합니다.

## 비용 설정은 두 관리 센터에서 나눠 확인하세요

Copilot Studio에서 Work IQ를 연결한다면 한쪽 관리 센터만 설정해서는 충분하지 않습니다.

| 관리 위치 | 담당하는 범위 | 적용 시나리오 |
|---|---|---|
| Power Platform admin center, PPAC | 환경별 선불 크레딧 할당, 초과 용량 사용, 에이전트별 한도·알림 | Copilot Studio 에이전트 |
| Microsoft 365 admin center, MAC | Work IQ 지출 정책의 사용자·그룹 범위, 청구 방식, 정책·사용자별 한도, 알림 | Studio의 Work IQ MCP 연결과 자체 Work IQ API 호출 |
| Microsoft 365 admin center, MAC | Cowork를 선택한 지출 정책과 대상 사용자·그룹 | Cowork |

따라서 GitHub Copilot harness 에이전트에 Work IQ를 추가한다면 **PPAC의 에이전트 비용 통제와 MAC의 사용자 Work IQ 지출 정책을 함께** 구성해야 합니다. 한쪽 설정이 다른 쪽을 자동으로 만들어 주지는 않습니다.

선불 Copilot Credit 용량 팩은 두 관리 센터가 관리하는 지원 서비스에 쓰일 수 있습니다. 다만 Power Platform 환경에 할당하거나 Copilot Studio에서 소비한 용량은 Microsoft 365의 지원 서비스가 사용할 수 있는 선불 용량을 줄입니다. 공통으로 사용할 수 있는 용량이 있다고 해서 통제 설정까지 통합되는 것은 아닙니다.

## MAC에서 Work IQ·Cowork 지출 정책 설정하기

사용량 기반 청구를 활성화한 뒤 **Copilot > Cost Management > Configuration**에서 지출 정책을 추가하거나 수정합니다. 다음 항목을 빠짐없이 지정하세요.

1. 적용 대상을 전체 사용자 또는 특정 보안 그룹으로 정합니다.
2. **Select agents and services**에서 목적에 맞게 Work IQ, Cowork 또는 둘 다 선택합니다.
3. 청구 방식을 선택하고 정책의 월별 지출 한도와 필요한 경우 사용자별 한도를 설정합니다. 청구 방식 관리는 Global 또는 Billing administrator가 담당합니다.
4. 임계값 알림과 대응 담당자를 정하고, 같은 사용자를 포함하는 다른 지출 정책도 살펴봅니다.

이 Work IQ 정책은 자체 애플리케이션뿐 아니라 Studio MCP 연결에도 필요합니다. 정책은 지출 한도를 정하는 장치이며, 크레딧 일부를 미리 떼어 예약하는 기능은 아닙니다. 실제 비용은 선불 크레딧이나 종량제(pay-as-you-go)로 충당합니다.

**Cowork 접근 차단을 낮은 비용 한도로 대신하지 마세요.** Cowork를 선택한 지출 정책은 한도가 매우 낮아도 정책 범위 안의 사용자에게 접근을 허용합니다. 접근을 막으려면 그 사용자가 Cowork를 선택한 모든 정책의 범위에서 제외되어야 합니다. 한도 적용에 지연이 생겨 한도 도달 뒤에도 추가 작업이 시작될 수 있다는 점도 고려해야 합니다.

지출 승인과 데이터 접근 권한은 별개입니다. Work IQ의 테넌트 활성화와 필요한 동의 절차는 따로 충족해야 하며, 비용을 사용할 수 있다고 해서 다른 사람의 자료를 읽을 수 있는 것은 아닙니다.

## PPAC에서 환경 용량과 에이전트 한도 설정하기

GitHub Copilot harness 에이전트는 배포 후 실행뿐 아니라 **제작·테스트·평가 과정에서도 크레딧을 소비**할 수 있습니다. 테스트를 시작하기 전에 다음 설정을 확인하는 편이 안전합니다.

1. **Licensing > Copilot Studio > Manage Copilot Credits**에서 환경을 선택하고 선불 크레딧 할당량을 정합니다.
2. **Capacity overages**의 **Draw from the available capacity in my tenant**를 확인합니다. 할당량 소진 뒤 미할당 테넌트 크레딧을 사용하지 못하게 하려면 이 옵션을 해제합니다.
3. 환경에 종량제 청구 플랜이 연결되어 있는지 확인합니다. 연결되어 있다면 선불 크레딧이 소진돼도 종량제로 사용이 이어질 수 있습니다.
4. **Licensing > Copilot Studio > Manage Agents**에서 에이전트의 월별 한도와 알림을 설정합니다. 한도 도달 시 중단하려면 **Stop usage**도 켭니다.

환경 할당량은 그 환경의 에이전트가 공유하는 용량이고, 에이전트 한도는 개별 작업의 소비를 제한합니다. 둘은 서로 대체할 수 없습니다. 또한 **Azure 예산 알림은 비용을 알려 줄 뿐 Copilot Studio 소비를 중단시키지 않습니다.**

MAC와 PPAC를 다른 팀이 운영한다면 에이전트 이름, 환경, 대상 사용자, Work IQ 활용 목적을 함께 전달해 양쪽 담당자가 같은 범위를 설정하도록 해야 합니다.

## Studio 연결 전 알아둘 지원 범위와 제한

원문이 다루는 **통합 Work IQ 연결은 preview이며 GitHub Copilot harness에서만 지원**합니다. Microsoft Learn은 preview 기능을 프로덕션 용도로 사용하기 위한 기능이 아니며 기능 제한이 있을 수 있다고 안내합니다.

연결할 때는 에이전트의 **Tools > Add tool > Model Context Protocol**에서 **Work IQ (preview)**를 선택하고 연결을 만들거나 기존 연결을 선택합니다. 인증과 구성 절차를 마친 뒤, 메일·회의·채팅·파일의 맥락이 필요한 질문으로 테스트합니다. 에이전트 지침에는 어떤 경우에 Work IQ를 참고해야 하는지 적어 두세요. 도구를 추가했다고 모든 메시지에서 반드시 호출하는 것은 아닙니다.

관련 [Microsoft Learn 연결 가이드](https://learn.microsoft.com/microsoft-copilot-studio/add-work-iq)는 다음 제한도 안내합니다.

- Microsoft 365 Work IQ는 관리자가 쓰기 작업을 명시적으로 활성화하기 전까지 읽기 전용입니다.
- Work IQ 사용에는 별도 지출 정책이 필요합니다.
- MAC에서 도구와 MCP 서버를 허용하거나 금지하는 기능은 지역에 따라 아직 제공되지 않을 수 있습니다.

Standard harness에서 보이는 **Tenant graph grounding with semantic search**는 통합 Work IQ MCP와 다릅니다. Generative AI 페이지에서 Work IQ 관련 토글로 표시된 적이 있지만, 지식 검색을 개선하는 별도 기능입니다. 활성화했을 때 Microsoft 365 Copilot 라이선스 사용자의 이 사용량은 zero-rated, 즉 Copilot Credits가 부과되지 않으며, 라이선스가 없는 사용자는 Copilot Studio 과금 기준을 적용받습니다.

일부 개별 MCP 도구 설명에 Work IQ가 남아 있는 것도 통합 연결 지원을 뜻하지는 않습니다. 원문은 이 개별 도구들이 향후 deprecated될 가능성을 언급하지만, 확정된 종료 일정으로 안내하지는 않습니다.

## 지식 원본과 Work IQ를 어떻게 나눠 쓸까요

지식 원본은 선택한 자료에서 관련 내용을 검색하고, 에이전트가 그 내용을 사용해 응답을 만듭니다. 반면 Work IQ의 대화형 `ask` 도구는 로그인한 사용자의 메일·회의·채팅·파일 맥락을 바탕으로 추론한 응답을 에이전트에 돌려줍니다.

둘 중 하나만 골라야 하는 것은 아닙니다. 원문은 회의 준비 에이전트에서 승인된 브리핑 형식은 지식 원본으로 참고하고, 최근 업무 상황은 Work IQ로 파악하는 예를 듭니다. 어떤 정보에 어떤 도구를 쓸지 지침에 구분해 두는 접근입니다.

처음에는 대표 업무 하나로 시작하세요. 그 업무가 짧은 질문인지 여러 단계를 거치는 작업인지에 따라 소비량이 달라질 수 있으므로, 실제 테스트 결과에 대상 사용자 수와 반복 빈도를 적용해 예상 사용량을 잡는 것이 좋습니다. 이 글의 원문은 모든 작업에 적용할 단일 크레딧 단가나 고정 소비량을 제시하지 않습니다.

---

> **출처**
>
> - MCSCAT Blog — The Custom Engine: [Work IQ: How It's Used, Licensed, and Controlled](https://microsoft.github.io/mcscatblog/posts/work-iq-context-layer-you-already-have/)
> - 관련 문서: [Work IQ in Copilot Studio (preview)](https://learn.microsoft.com/microsoft-copilot-studio/add-work-iq)
> - 관련 문서: [Manage costs for agents powered by the GitHub Copilot harness](https://learn.microsoft.com/power-platform/admin/manage-usage-github-copilot-harness)
>
> 자세한 내용은 원문 참조. 라이선스 조건과 preview 지원 범위는 변경될 수 있으므로 실제 도입 시 최신 가이드를 확인하세요.
