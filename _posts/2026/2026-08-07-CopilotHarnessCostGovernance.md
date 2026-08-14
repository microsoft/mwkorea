---
title: "GitHub Copilot harness 크레딧, 만들다가 다 쓰기 전에 — 비용 통제와 거버넌스"
date: 2026-08-07T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - CopilotCredits
  - Governance
  - PowerPlatform
  - PPAC
  - GitHubCopilotHarness
excerpt: "GitHub Copilot harness 에이전트는 게시하기 전 빌드·미리 보기·평가 단계에서도 Copilot Credit을 소비합니다. 메이커 개발 환경과 자금이 배정된 프로덕션 환경을 구분해 통제하는 반복 가능한 거버넌스 절차를 PPAC와 Power Platform API 구현 예제와 함께 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# GitHub Copilot harness 크레딧, 만들다가 다 쓰기 전에 — 비용 통제와 거버넌스

지금까지 Copilot Studio의 비용 관리는 비교적 단순한 전제 위에 있었습니다. **에이전트를 게시(publish)해서 사용자가 쓰기 시작하면 크레딧이 나간다**는 것이었죠. 그래서 통제도 "프로덕션에 올라간 다음"에 신경 쓰면 됐습니다.

**GitHub Copilot harness**가 이 전제를 바꿨습니다. 메이커가 harness로 에이전트를 **빌드하고, 미리 보고, 평가하는 과정에서도 Copilot Credit이 소비**됩니다. 즉 **한 번도 게시된 적 없는 환경이 크레딧을 쓰고 있을 수 있습니다.**

Microsoft Copilot Studio 고객 자문 팀(CAT)이 이 문제를 다루는 **반복 가능한 거버넌스 절차**를 공개했습니다. PPAC 화면 조작부터 Power Platform API를 통한 대규모 자동화까지 구체적인 구현 방법이 담겨 있습니다.

![GitHub Copilot harness 비용 통제와 거버넌스](/mwkorea/assets/images/2026-08-07-CopilotHarnessCostGovernance/image1.png)

---

## 무엇이 달라졌나

> 메이커 개발(maker development)이 이제 에이전트가 정식 프로덕션 수명 주기에 들어가기 **전에도** Copilot Credit을 소비할 수 있습니다.

이 한 문장이 핵심입니다. 그리고 여기서 두 가지 성격이 다른 소비가 생깁니다.

| 구분 | 성격 |
|---|---|
| **메이커 개발(maker development)** | 탐색·빌드·미리 보기·평가 과정의 소비. 게시되지 않을 수도 있음 |
| **자금 배정 프로덕션(funded production usage)** | 승인된 부서/전사 프로세스를 지원. 명확한 자금과 소유권 필요 |

두 시나리오는 **용량, 소유권, 연속성에 대한 접근 방식이 서로 달라야** 합니다. 환경 유형이 무엇이든 마찬가지입니다.

---

## 노출을 줄이는 실무 기준선 5단계

원문이 제시하는 기본 절차입니다.

1. **GitHub Copilot harness 에이전트**와 그것이 속한 환경을 찾는다.
2. 해당 환경을 **메이커 개발** 또는 **자금 배정 프로덕션**으로 분류한다.
3. **할당량(allocation), 테넌트 풀 접근, 종량제(pay-as-you-go) 청구, 적용 규칙**을 검토한다.
4. 개별 소비에 더 엄격한 경계가 필요한 곳에 **에이전트 수준 한도**를 적용한다.
5. 주기적으로 반복하거나, 신규 생성 환경·에이전트 **탐지를 자동화**한다.

---

## 1단계: 대상 에이전트와 환경 찾기

각 GitHub Copilot harness 에이전트에 대해 다음을 먼저 파악합니다.

- 그것이 속한 **환경**
- 그 환경이 **메이커 개발**인지 **자금 배정 프로덕션**인지
- **에이전트 소유자**와 소비에 대한 **책임자(accountable cost owner)**
- 현재 **할당량, 초과 설정, 실제 소비**가 그 목적에 부합하는지

### `isCLIAgent` 속성이 핵심입니다

**Power Platform Inventory**로 Copilot Studio 에이전트와 환경을 찾을 수 있습니다. 규모가 작으면 PPAC의 인벤토리로 충분하고, 규모가 크면 **Azure Resource Graph** 또는 **Power Platform Inventory API**로 반복 가능하게 만듭니다.

여기서 **`isCLIAgent` 속성이 GitHub Copilot harness를 사용하는 에이전트를 식별**합니다. 이 에이전트들이 설계 시점(design time)의 메이커 경험에서 크레딧을 소비할 수 있는 대상입니다.

```
POST https://api.powerplatform.com/resourcequery/resources/query?api-version=2024-10-01
Content-Type: application/json

{
  "TableName": "PowerPlatformResources",
  "Clauses": [
    {
      "$type": "where",
      "FieldName": "type",
      "Operator": "==",
      "Values": ["'microsoft.copilotstudio/agents'"]
    },
    {
      "$type": "where",
      "FieldName": "properties.isCLIAgent",
      "Operator": "==",
      "Values": ["true"]
    },
    {
      "$type": "project",
      "FieldList": [
        "name",
        "properties.displayName",
        "properties.environmentId",
        "properties.ownerId",
        "properties.isCLIAgent"
      ]
    }
  ]
}
```

Inventory는 **에이전트·소유자·환경 사이의 기술적 관계**를 돌려줍니다. 여기에 환경 명명 규칙, 환경 그룹, 거버넌스 메타데이터, 승인 기록 같은 **비즈니스 맥락**을 결합해 분류하시면 됩니다. **Copilot Agent Kit**이나 **Compliance Hub**를 이미 쓰고 계시다면 그 인벤토리를 확장하는 방식도 가능합니다.

---

## 2단계: 목적에 따라 통제 방식 정하기

### 메이커 개발 환경

에이전트가 정식 프로덕션 수명 주기에 들어가기 전에 통제가 필요합니다.

- GitHub Copilot harness 에이전트 **탐지**
- **기본 에이전트 한도** 적용
- 테넌트 풀 또는 종량제 접근이 적절한지 **결정**
- 에이전트 소유자에게 **경계선 통지**
- 추가 용량을 **요청하는 방법 정의**

### 자금 배정 프로덕션 환경

승인된 부서·전사 프로세스를 지원하므로 **책임 있는 소유권과 의도적 자금 배정**이 필요합니다.

- **비용 소유자와 자금 모델 확인**
- 용량 할당 또는 청구를 **의도적으로 구성**
- **예상 사용량과 서비스 중요도**에 기반해 한도 설정
- 프로덕션 서비스를 **중단시킬 수 있는 소비 모니터링**

---

## 3단계: 환경 수준 통제 적용

환경을 분류한 뒤, 크레딧 접근 방식과 용량 소진 시 동작을 검토합니다.

| 결정 사항 | 사용 가능한 통제 |
|---|---|
| 이 환경에 선불 용량을 예약해야 하는가? | **환경에 Copilot Credit 할당** |
| 테넌트 풀의 미할당 용량을 쓸 수 있게 할 것인가? | **테넌트 풀 draw 활성화/비활성화** |
| 승인된 Azure 구독을 통해 소비를 계속할 수 있게 할 것인가? | **종량제(pay-as-you-go) 청구 활성화/비활성화** |
| 용량에 근접하거나 소진되면 무슨 일이 일어나야 하는가? | **알림 구성 또는 추가 소비 거부(deny)** |

**메이커 개발 환경**은 보통 탐색이 다른 업무용 용량을 잠식하지 않도록 **의도적인 경계선**이 필요합니다. **자금 배정 프로덕션**의 경우, 테넌트 풀이나 종량제 접근은 오히려 그 에이전트에 자금을 대는 팀이 소유하는 **의도적인 연속성 결정**일 수 있습니다.

### PPAC에서 설정하기

PPAC에서 **Licensing > Copilot Studio > Manage Copilot Credits**로 이동합니다. 환경을 선택하고, 필요한 만큼 선불 용량을 할당한 뒤, 용량 소진 시 동작을 구성합니다.

![환경별 선불 Copilot Credit 예약](/mwkorea/assets/images/2026-08-07-CopilotHarnessCostGovernance/image2.png)

> **⚠️ 중요한 주의사항**: 테넌트의 **애드온 용량 할당 설정(add-on capacity assignment setting)**이 누가 크레딧을 할당할 수 있는지를 통제합니다. 환경 관리자에게 할당 관리를 허용하면 **그들이 관리하는 환경으로만 제한되지 않습니다.** 테넌트 내 **모든 환경**에 대한 할당 권한이 부여됩니다. 이 광범위한 접근이 의도된 것이 아니라면 **할당은 테넌트 관리자로 제한**하십시오.

### API로 대규모 설정하기

규모가 크다면 **Update Allocations By Environment**로 할당과 적용 규칙을 한 요청에 구성합니다.

아래 요청은 **10,000 크레딧을 할당**하고, **관리자 알림을 켜고**, **테넌트 풀 draw를 차단**하고, **종량제 초과를 허용**하며, **추가 소비 거부는 비활성화**한 상태로 둡니다.

```
PATCH https://api.powerplatform.com/licensing/allocationsByEnvironment?api-version=2024-10-01
Content-Type: application/json

{
  "environmentId": "<environment-id>",
  "currencyAllocations": [
    {
      "currencyType": "MCSMessages",
      "allocated": 10000,
      "enforcementRules": [
        { "ruleType": "Alert",      "enabled": true  },
        { "ruleType": "TenantPool", "enabled": false },
        { "ruleType": "PayGo",      "enabled": true  },
        { "ruleType": "Deny",       "enabled": false }
      ]
    }
  ]
}
```

> **주의**: 이 요청은 **할당된 크레딧을 포함한 현재 구성을 패치**합니다. 먼저 현재 할당을 읽어 유지해야 할 기존 값을 보존한 뒤, **의도한 전체 구성**을 제출하십시오.

C#·Python SDK와 PowerShell 예제는 Microsoft Learn의 크레딧 할당 프로그래밍 튜토리얼에 있으며, **Power Platform for Admins V2 커넥터** 액션도 곧 제공될 예정입니다.

---

## 4단계: 신규·기존 환경 주기적 점검

신규 환경은 **테넌트 풀 draw가 켜진 채로 생성될 수 있고**, 기존 환경 설정은 승인된 통제에서 **드리프트(drift)**할 수 있습니다. 반복 점검·교정 프로세스는 다음과 같습니다.

1. Power Platform Inventory에서 `microsoft.powerplatform/environments` 조회 (앞의 Inventory API 요청에서 리소스 타입 필터만 바꾸면 됩니다)
2. 결과를 **거버넌스 환경 등록부**와 비교
3. 신규·미분류 환경은 **분류하고 승인 통제를 기록**, 기존 환경은 기록된 분류와 승인 통제를 조회
4. **Get Allocations By Environment**로 현재 할당·적용 규칙 읽기
5. 현재 구성과 승인 통제 **비교**
6. **승인된 예외는 보존**, 그 외 불일치는 **교정**

```
GET https://api.powerplatform.com/licensing/allocationsByEnvironment/<environment-id>?api-version=2024-10-01
```

---

## 5단계: 에이전트 수준 한도 적용

환경 통제가 **공유 용량의 경계**를 정한다면, 에이전트 수준 한도는 **개별 사용 사례에 대한 월간 경계**를 더합니다. 해당 환경이 선불 용량을 쓰든 종량제를 쓰든 관계없이 적용됩니다.

메이커 개발 에이전트에 대한 반복 프로세스는 다음과 같습니다.

1. **신규 생성된 harness 에이전트 탐지**
2. 메이커 개발 환경인지 **확인**
3. 조직의 **기본 개발 한도 적용**
4. 에이전트 소유자에게 **한도와 도달 시 동작 통지**
5. 추가 용량 요청을 **적절한 승인 절차로 라우팅**
6. 에이전트가 자금 배정 프로덕션으로 이동하면 개발 한도를 **재검토 또는 교체**

> **한도는 사용자가 아니라 에이전트에 적용됩니다.** 기본값과 에스컬레이션 절차를 정할 때 **한 메이커가 몇 개의 에이전트를 만들 수 있는지**를 함께 고려하십시오.

### ⚠️ 현재의 공백: 환경 단위 총량 제한

원문이 명확히 짚는 제약입니다.

> 에이전트 수준 한도는 **환경 전체의 합산 소비를 제한하지 않습니다.** 2026년 8월 기준, Microsoft는 메시지 센터 항목 **MC1451872**를 통해 **환경 수준 한도**를 발표했으며 이것이 이 공백을 메웁니다. 그전까지는 **사용량을 검토하고 청구 정책(billing policy) 연결을 해제해 환경 수준 소비를 차단**할 수 있습니다.

### PPAC에서 에이전트 한도 설정

PPAC에서 **Licensing > Copilot Studio > Manage Agents**로 이동합니다. 에이전트를 선택해 **월간 Copilot Credit 한도**를 설정하고, 소비가 한도에 근접할 때 관리자에게 알릴지, 한도 도달 시 추가 사용을 중지할지 선택합니다.

![에이전트 수준 크레딧 한도 설정](/mwkorea/assets/images/2026-08-07-CopilotHarnessCostGovernance/image3.png)

> **알림 대상 주의**: 내장 한도 알림은 **테넌트 및 환경 관리자**에게 전송되며, **반드시 에이전트 소유자에게 가는 것은 아닙니다.** 누가 그 알림을 검토하고, 맥락이 필요할 때 누가 소유자에게 연락하며, 누가 한도 증액을 승인하거나 에이전트 중지를 허용할지 정해 두십시오.

제품 내장 알림 대신 자체 소비 검토·알림 프로세스를 구현하려면 **Get Many Environment Entitlements**로 환경의 entitlement 소비 데이터를 가져올 수 있습니다.

```
GET https://api.powerplatform.com/licensing/environments/<environment-id>/entitlements?api-version=2024-10-01
```

### API로 에이전트 한도 설정

**Update Resource Threshold**로 승인된 한도, 알림 임계값, 중지 동작을 적용합니다. 아래는 **한도 1,000 크레딧, 80%에서 관리자 알림, 한도 도달 시 추가 소비 차단** 설정입니다.

```
PUT https://api.powerplatform.com/licensing/environments/<environment-id>/entitlements/MCSMessages/resources/<agent-resource-id>/threshold?api-version=2024-10-01
Content-Type: application/json

{
  "stopResource": false,
  "limit": 1000,
  "stopIfOverCapacity": true,
  "notifyIfOverCapacity": true,
  "notificationThreshold": 80
}
```

> **필수 주의**: `stopResource`를 반드시 **`false`로 설정**하십시오. 이 값은 한도와 무관하게 **요청 시점에 즉시 에이전트 사용을 중지**시키며, PPAC의 **Manage Agents**에서 제공하는 "에이전트 중지" 액션과 동일하게 작동합니다.

---

## 한국 조직을 위한 실행 순서

원문 내용을 국내 도입 현실에 맞춰 정리하면 다음과 같습니다.

1. **먼저 현황부터 파악하세요.** `isCLIAgent = true` 쿼리 한 번으로 harness 에이전트가 몇 개나 있고 어느 환경에 있는지 확인됩니다. 대부분의 조직이 이 숫자를 모르고 있습니다.
2. **테넌트 설정부터 조입니다.** 애드온 용량 할당 권한이 환경 관리자에게 열려 있다면 **테넌트 전체 할당 권한**이 열려 있는 것입니다. 의도한 게 아니라면 즉시 조정하십시오.
3. **개발용 기본 한도를 정하세요.** 메이커 한 명이 만들 수 있는 에이전트 수를 고려해 1인 기준이 아니라 **에이전트 기준**으로 산정해야 합니다.
4. **알림 수신자와 대응 절차를 문서화하세요.** 알림이 관리자에게만 가므로, 소유자 연락 담당과 증액 승인권자를 정해 두지 않으면 알림이 방치됩니다.
5. **MC1451872(환경 수준 한도)를 추적하세요.** 현재는 에이전트 한도만으로 환경 총량을 막을 수 없습니다. 그전까지는 청구 정책 연결 해제가 임시 방편입니다.
6. **자동화는 API로.** 신규 환경 탐지와 드리프트 교정은 주기적 수작업으로는 유지되지 않습니다. Inventory API + Allocations API 조합으로 스크립트화하시길 권합니다.

---

## 마무리

GitHub Copilot harness로 만든 에이전트는 **크레딧 소비를 관리해야 하는 시점을 앞당겼습니다.** 게시 전 단계가 이미 비용 발생 구간이 됐기 때문입니다.

원문이 제시하는 균형점은 명확합니다.

> 메이커 개발 시나리오에서는 **어느 정도의 탐색을 허용하는 에이전트 한도**를 설정하고, 자금 배정 프로덕션 사용에는 **사용 사례에 맞는 통제와 한도**를 적용하는 — 통제와 활성화 사이의 세심한 균형.

그리고 원문은 이렇게 묻습니다. **"이 프로세스 중 어느 부분을 PPAC에서 관리하고, 어느 부분을 Power Platform API로 자동화하시겠습니까?"**

Copilot Studio를 전사로 확산 중인 조직이라면, 지금이 그 답을 정할 시점입니다.

---

> **출처**: [*Adopting the GitHub Copilot Harness: Cost Control and Governance in Copilot Studio*](https://microsoft.github.io/mcscatblog/posts/copilot-harness-cost-governance/) (MCSCAT Blog — The Custom Engine, Microsoft Copilot Studio Customer Advisory Team)
>
> 자세한 내용은 원문 참조.
