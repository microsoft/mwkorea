---
title: "Copilot Studio 비용, 성공한 업무 한 건부터 계산하세요"
date: 2026-11-25T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - CopilotCredits
  - CostManagement
  - PowerPlatform
  - Governance
excerpt: "Copilot Studio 에이전트 비용은 메이커의 실행 측정과 관리자의 예산 통제를 함께 설계해야 합니다. 성공한 업무당 크레딧 예측부터 PPAC 할당, Microsoft 365 관리 센터의 공개 프리뷰 지출 정책까지 실무 관점으로 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio 비용, 성공한 업무 한 건부터 계산하세요

에이전트가 복잡한 업무를 수행할수록 비용은 사용자 수만으로 설명하기 어려워집니다. 같은 요청이라도 검색, 도구 호출, 실패 후 재시도에 따라 실행량이 달라지기 때문입니다. 사용량 기반 과금에서는 “얼마를 충전했는가”뿐 아니라 “무엇을 얼마나 성공적으로 처리했는가”가 중요합니다.

Microsoft는 2026년 11월 24일 UTC에 공개한 Copilot Studio 비용 관리 글에서, Microsoft Copilot harness 도입과 함께 메이커의 크레딧 가시성 및 관리자의 지출 정책을 설명했습니다. 한국 시간으로는 11월 25일 발표입니다.

핵심은 **메이커가 업무당 소비량을 측정하고 관리자가 비용 소유자·재원·한도를 연결하는 지속적인 운영 루프**입니다. 아래 설명은 원문 시점 기준입니다. Microsoft 365 관리 센터의 리소스·환경 정책은 공개 프리뷰이며, 사용자·그룹의 identity 정책은 아직 후속 제공 예정이라는 차이를 분명히 해야 합니다.

---

## 비용 관리는 메이커와 관리자의 공동 업무

![메이커와 관리자가 함께 수행하는 에이전트 비용 관리](/mwkorea/assets/images/2026-11-25-CopilotStudioCostManagement/image1.png)

메이커는 에이전트 설계, 대표 업무 테스트, 결과 품질을 책임집니다. 비싼 실행 경로와 실패·재시도를 찾아 개선하되, 크레딧을 줄인 변경이 업무 완성도를 떨어뜨리지 않는지 확인해야 합니다.

관리자는 비용 센터, 재원, 적용 범위, 한도, 알림과 대응 계획을 관리합니다. 메이커의 측정치는 예산 근거가 되고, 실제 지출 패턴은 다음 설계 개선의 출발점이 됩니다. 두 역할은 대체 관계가 아니라 서로 보완하는 관계입니다.

![메이커 가시성과 PPAC·MAC 관리자 통제의 관계](/mwkorea/assets/images/2026-11-25-CopilotStudioCostManagement/image2.png)

## 메이커: Preview의 추정치와 Monitor의 실제 사용량을 구분하기

![Copilot Studio Preview에 표시되는 실행 크레딧 추정치](/mwkorea/assets/images/2026-11-25-CopilotStudioCostManagement/image3.png)

| 화면 | 확인할 정보 | 해석 시 주의점 |
|---|---|---|
| Preview | 설계 변경 전후 동일 대표 업무의 준실시간 추정치 | 빠른 설계 판단용이며 청구 기록이 아님 |
| History | 대화별 추정치, 비싼 경로, 실패와 재시도 | 문제 경로를 테스트에서 재현해 분석 |
| Evaluate | 전체 추정치와 대화별 상세 소비량 | 응답 생성 비용과 채점 비용을 분리 |
| Monitor | 처리가 완료된 최종 사용량 | 보고 지연 후 확인하며 일부 화면은 테넌트 배포 상황에 따라 다름 |

Evaluate의 채점 비용은 평가를 위한 오버헤드입니다. 반복되는 프로덕션 런타임 비용과 섞어 예측하면 안 됩니다. 또한 모든 harness에서 모든 개발·테스트 활동이 과금되는 것은 아니므로, 자신이 사용하는 harness의 조건을 먼저 확인해야 합니다.

설계 변경의 절감 효과는 Preview에서 가늠하고, Monitor에 반영되는 처리 완료 사용량으로 다시 확인하세요. 관련 설명은 [크레딧 표시와 추정 사용량 문서](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/billing-credit-understand-display)를 참고할 수 있습니다.

## 예측 단위는 질문 한 번이 아니라 성공한 업무 한 건

단순 업무, 복잡한 다단계 업무, 예외 처리 경로를 골라 여러 번 실행합니다. 각 표본에서 런타임 크레딧, 완료 여부, 품질, 재시도를 기록해야 합니다. 실패한 시도와 복구 작업도 **완료된 업무당 비용**에 포함합니다.

원문이 제시한 반복 런타임 예측식은 다음과 같습니다.

```text
예상 반복 런타임 크레딧 =
업무 유형별 합계(
  예상 완료 업무량 × 관측된 완료 업무당 런타임 크레딧
)
```

낮은 수요, 예상 수요, 높은 수요를 각각 계산하고 처리 완료 사용량으로 갱신합니다. 과금되는 개발·테스트·평가 작업은 별도 예산으로 잡습니다. 원문은 특정 크레딧 단가나 일괄 절감률을 제시하지 않으므로, 이 계산을 임의의 원화 금액으로 바꾸지 않습니다.

표본 실행에서 불필요한 검색과 반복 액션을 줄인 뒤, 수정된 크레딧 범위와 업무량 가정을 관리자에게 전달하세요. Standard의 기능 기반 사용량은 [agent usage estimator](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-usage-estimator)를 이용할 수 있습니다.

## 관리자: 계획, 통제, 최적화를 반복하기

![계획·통제·최적화로 이어지는 비용 관리 순환](/mwkorea/assets/images/2026-11-25-CopilotStudioCostManagement/image4.png)

계획 단계에서는 업무 소유자와 비용 센터를 정하고, 측정된 업무 구성·예상량으로 수요를 계산합니다. 리소스 소유자가 부담할지, 자격을 갖춘 사용자가 부담할지에 따라 정책 범위도 달라집니다.

통제 단계에서는 할당과 예산, 지원되는 에이전트별·사용자별 한도를 설정하고 알림 수신자, 승인자, 에스컬레이션 경로를 연결합니다. **사용 가능한 선불 크레딧이나 PAYG 재원이 있어도 적용된 한도를 무시할 수는 없습니다.**

최적화 단계에서는 사용량과 업무 결과를 함께 평가합니다. 완료 업무가 줄어든 덕분에 크레딧 합계가 낮아졌다면 개선이라고 보기 어렵습니다. 설계나 도입 규모가 바뀌면 이 순환을 다시 시작해야 합니다.

## PPAC의 기본: 환경 할당과 에이전트 한도는 다르다

Power Platform admin center(PPAC)는 환경 중심의 기본 비용 관리 도구입니다. 라이선싱 허브에서 선불·소비 용량, PAYG 사용량, 환경별 일간 소비 추세를 확인하고 환경별로 크레딧을 배정할 수 있습니다.

| 구분 | 의미 |
|---|---|
| Allocation, 할당 | 환경의 업무에 사용할 크레딧을 따로 확보함 |
| Limit, 한도 | 에이전트가 사용할 수 있는 상한을 정함. 크레딧을 예약하지는 않음 |

에이전트 한도는 환경에서 사용 가능한 용량을 넘길 수 없습니다. 인기 에이전트 하나가 용량을 독점하지 않게 에이전트별 한도를 설정하고, 환경의 용량 초과 알림으로 사전 대응합니다.

**Draw from tenant credit pool** 환경 그룹 규칙은 자체 할당이 소진된 환경이 공유 테넌트 용량을 추가로 가져가지 못하도록 통제합니다. 그룹 내 새 환경과 개인 개발자 환경에도 적용된다는 점이 중요합니다.

수요 급증 시에는 용량 초과 설정에 따라 남은 테넌트 용량을 사용하거나 Azure 구독에 연결된 PAYG 요금제로 청구해 연속성을 확보할 수 있습니다. 이것은 무조건적인 자동 초과 사용 보장이 아니라 설정에 따른 동작입니다. 환경·에이전트·사용자별 보고서로 재할당 근거를 확인하세요.

세부 설정은 [PPAC Copilot Credits 용량 관리 문서](https://learn.microsoft.com/en-us/power-platform/admin/manage-copilot-studio-copilot-credits-capacity)를 참고하세요.

## MAC의 추가 기능: 환경을 옮기지 않고 예산을 연결하기

![Microsoft 365 관리 센터에 표시되는 Copilot Studio 서비스](/mwkorea/assets/images/2026-11-25-CopilotStudioCostManagement/image5.png)

Microsoft 365 admin center(MAC)는 Cowork, Work IQ 같은 사용량 기반 AI 서비스와 일관된 지출 관리 경험을 Copilot Studio에 확장합니다. 환경과 리소스는 PPAC에 그대로 두고 예산 정책을 연결하는 방식입니다.

| 정책 범위 | 대상 | 원문 시점 상태 |
|---|---|---|
| Resource | 특정 에이전트 등 리소스 | 공개 프리뷰 |
| Environment | 하나 이상의 환경 | 공개 프리뷰 |
| Identity | 사용자 또는 그룹 | 후속 제공 예정 |

![특정 리소스 또는 환경 컬렉션을 선택하는 정책 범위 화면](/mwkorea/assets/images/2026-11-25-CopilotStudioCostManagement/image6.png)

지출 정책은 얼마까지 쓸지, 어떤 서비스를 포함할지, 어떤 재원으로 부담할지를 연결합니다. 단일 에이전트 또는 리소스·환경 묶음에 한도와 청구 방식을 지정해 부서나 중요 업무의 비용 책임을 분리할 수 있습니다.

![선불 크레딧과 PAYG 청구 방식 선택 예시](/mwkorea/assets/images/2026-11-25-CopilotStudioCostManagement/image7.png)

원문은 정책 한도가 선불과 PAYG에 모두 적용돼 설정한 상한에서 지출을 멈추는 방식이라고 설명합니다. 모든 환경을 대상으로 하는 정책에 기본 에이전트별 한도를 두면 앞으로 생성되는 에이전트에도 적용할 수 있습니다. 알림은 한도 도달 전에 실제 조치할 담당자에게 전달하도록 설계해야 합니다.

MAC 보고서는 서비스와 에이전트에 소비를 귀속해 증가 추세를 찾도록 돕습니다. 정책을 Azure 구독·리소스 그룹과 연결하면 부서가 자기 비용을 확인하고 책임지는 비용 배분에도 활용할 수 있습니다.

![MAC 사용량 개요 화면](/mwkorea/assets/images/2026-11-25-CopilotStudioCostManagement/image8.png)

정책이 적용되는 사용량에서는 **MAC가 PPAC보다 우선**합니다. 에이전트의 리소스·환경 정책은 identity 정책보다 먼저 적용되며, 두 예산은 합산되지 않습니다. 다만 identity 정책 자체는 아직 예정 기능이므로 현재 사용할 수 있는 통제로 가정하지 않아야 합니다.

## 비용 소유자에 따라 달라지는 두 가지 시나리오

### 인사팀의 AskHR: 공유 업무 비용은 소유 부서가 관리

![중요 에이전트 또는 환경에 소유자 예산을 연결하는 예시](/mwkorea/assets/images/2026-11-25-CopilotStudioCostManagement/image9.png)

직원이 AskHR에 질문할 때마다 직원 개인이 비용을 부담하도록 하기보다, 인사팀이 에이전트나 환경 범위 정책으로 비용을 관리하는 시나리오입니다. 한도, 알림, 승인된 재원을 정하고 메이커는 실행 경로와 완료율을, 관리자는 실제 지출과 잔여 여력을 확인합니다.

### 메이커 실험: 개인별 예산은 후속 identity 정책으로

![메이커의 통제된 실험을 지원하는 identity 예산 시나리오](/mwkorea/assets/images/2026-11-25-CopilotStudioCostManagement/image10.png)

메이커 보안 그룹에 identity 정책을 적용해 개인 한도로 실험하도록 하는 방향입니다. **원문에서는 제공 예정 시나리오**이므로 현재 테넌트의 지원 여부를 확인해야 합니다. Preview·평가 추정치를 설계 비교에 활용하되, 개발 예산과 반복 운영 예산을 구분하는 원칙은 동일합니다.

## 도입 체크포인트: 역할을 먼저 부여하고 환경 하나부터

MAC 정책은 자체 역할 체계를 사용합니다. 기존 Power Platform 역할이 자동으로 넘어오지 않는다는 점부터 점검하세요.

| 담당자 | 원문이 안내한 역할 |
|---|---|
| Power Platform·Dynamics 365 관리자 | 지출 정책 설정을 위해 AI Administrator 필요. 자동 부여되지 않음 |
| 환경 관리자 | 해당 환경의 지출 확인을 위해 AI Reader |
| Global Administrator | 기존 테넌트 전체 및 청구 접근 유지 |
| 메이커 | 새 역할 불필요. Copilot Studio의 개발·테스트·모니터링 가시성 사용 |

원문의 시작 절차는 다섯 단계입니다.

1. 첫 정책 생성 전에 필요한 역할을 부여합니다.
2. 각 환경의 현재 크레딧, 청구 계획, 에이전트 한도, 소유자를 확인합니다.
3. 부서에는 환경 정책, 중요 에이전트에는 리소스 정책 등 비용 책임에 맞는 범위를 선택합니다. 메이커 identity 정책은 제공 후 검토합니다.
4. 환경 하나에서 한도·알림을 설정하고 비용 배분용 Azure 구독을 연결해 파일럿을 진행합니다.
5. 환경별로 확대하고 identity 정책은 실제 제공 시 추가합니다.

정책을 만들고 환경을 연결하기 전에는 아무것도 바뀌지 않는다고 원문은 안내합니다. 사용량 기반 권장 한도, 팀별 권장 역할, 코드로 역할을 설정하는 기능은 **2027년 초 계획**이지 현재 제공 확정 기능이 아닙니다.

설정 전 [MAC의 Copilot Studio 비용 관리](https://learn.microsoft.com/en-us/copilot/implement/usage-based-billing-manage-copilot-studio-costs)와 [Copilot Credits 지출 정책](https://learn.microsoft.com/en-us/copilot/implement/usage-based-billing-manage-copilot-credits)의 적용 조건을 확인하세요. 문서는 이후 갱신될 수 있으므로 실제 적용 시점의 지원 범위는 원문 발표 당시의 상태와 구분해야 합니다.

## 마무리

Copilot Studio 비용 관리의 출발점은 적게 쓰는 에이전트가 아니라 **주어진 품질로 업무를 끝내는 데 얼마가 드는지 아는 에이전트**입니다. 대표 업무의 실제 측정, 명확한 비용 소유자, 재원과 분리된 한도, 중단에 대비한 운영 대응을 함께 준비해야 도입 규모가 커져도 관리할 수 있습니다.

> 출처: TechCommunity Microsoft Copilot Studio Blog, [How to manage costs for Copilot Studio agents](https://techcommunity.microsoft.com/t5/copilot-studio-blog/how-to-manage-costs-for-copilot-studio-agents/ba-p/4576413). 자세한 내용은 원문 참조. 리소스·환경 정책은 원문 시점 공개 프리뷰이며 identity 정책과 2027년 초 기능은 제공 계획입니다.
