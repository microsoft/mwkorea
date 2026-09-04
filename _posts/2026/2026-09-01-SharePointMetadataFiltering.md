---
title: "\"캐나다 육아휴직 정책 알려줘\"가 되는 이유: Copilot Studio의 SharePoint 메타데이터 필터링"
date: 2026-09-01T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - SharePoint
  - Metadata
  - KnowledgeSource
  - GitHubCopilotHarness
  - Agent
  - Governance
excerpt: "GitHub Copilot harness 에이전트가 SharePoint 문서 라이브러리의 메타데이터로 문서를 걸러낸 뒤 그 문서들만 검색할 수 있게 됐습니다. 나라·상태·부서별로 갈리는 문서를 토픽 분기 없이 처리할 수 있으며, 설정이라고 할 것은 라이브러리를 지식 소스로 추가하는 것뿐입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# "캐나다 육아휴직 정책 알려줘"가 되는 이유: Copilot Studio의 SharePoint 메타데이터 필터링

SharePoint 라이브러리에는 **비슷해 보이지만 대상이 다른 문서**가 흔합니다. 복리후생 정책은 나라마다 다르고, 제품 가이드는 특정 시장에만 해당하며, 절차서는 상태가 **승인됨(Approved)** 일 때만 유효합니다.

이런 구분은 대개 **문서 내용이 아니라 메타데이터 열**에 기록되어 있습니다. 그런데 지금까지 에이전트는 이 정보를 활용하기 어려웠습니다. MCSCAT 팀의 표현이 재미있습니다.

> 사람들이 SharePoint 메타데이터를 지식 검색에 쓸 수 있는 간단한 방법을 요청해 온 게 **영원처럼 느껴질 만큼** 오래됐습니다. 대략 **백만 년쯤** 걸렸네요. 진정하세요, 이제 왔습니다.

**GitHub Copilot harness** 기반 에이전트가 이 간극을 메웁니다. 요청을 해석하고, **SharePoint 파일을 메타데이터로 필터링**하고, 매칭된 문서 URL을 모아 **그 문서들만 검색**할 수 있습니다.

![SharePoint 메타데이터 필터링](/mwkorea/assets/images/2026-09-01-SharePointMetadataFiltering/image1.png)

---

## 기존 Standard harness의 한계

원문은 이전 방식의 문제를 명확히 짚습니다.

Standard harness에서는 **사용자 의도 → SharePoint 메타데이터 → 매칭 문서 URL** 로 이어지는 간단하고 구성 가능한 경로가 없었습니다. 메이커가 여러 **토픽**과 범위를 지정한 **Create generative answers** 노드로 비슷하게 흉내 낼 수는 있었지만, 그 노드는 **구성된 소스나 URL로 검색 범위를 좁힐 뿐 문서 라이브러리 메타데이터로는 좁히지 못했습니다.**

결과적으로 **나라, 부서, 문서 상태가 하나 늘어날 때마다 유지해야 할 구성이 늘어났습니다.**

---

## 설정이라고 할 것이 없습니다

이번 방식의 핵심은 오히려 **설정할 게 없다**는 점입니다.

모든 SharePoint 문서 라이브러리에는 **작성자, 수정 날짜** 같은 기본 열이 이미 있고, **나라, 상태, 부서** 같은 사용자 지정 열을 추가할 수 있습니다.

> 라이브러리를 **지식 소스로 추가**하고 에이전트에게 질문하면 됩니다. **메이커가 구성해야 할 별도의 메타데이터 도구가 없습니다.**

메타데이터가 관련 있을 때 에이전트는 **사용 가능한 열을 스스로 찾아내고**, 기록된 값으로 적절한 파일을 식별한 뒤, 그 문서 집합에서 답합니다. Standard harness의 **분기마다 토픽을 만드는 설정이 필요 없습니다.**

### 왜 내용 검색만으로는 부족한가

`Country` 열이 있는 라이브러리를 생각해 봅시다. 사용자가 묻습니다.

> "캐나다에는 어떤 육아휴직 복리후생이 적용되나요?"

에이전트는 `Country` 값이 `Canada`인 모든 문서를 찾은 뒤, **그 파일들 안에서만** 육아휴직 정보를 검색합니다.

여기가 중요합니다. **"캐나다"라는 단어가 정책 문서 본문에는 안 나올 수도 있습니다.** 라이브러리 메타데이터에만 존재할 수 있죠. 내용만 검색하면 **맞는 문서를 놓치거나, 다른 나라용 정책 정보를 섞어 버릴 수 있습니다.**

### 같은 패턴이 통하는 메타데이터

- 승인 상태와 검토 날짜
- 부서, 사업부, 대상 독자
- 제품, 서비스, 시장
- 문서 유형, 소유자, 최종 수정 날짜
- 폴더 위치와 파일 형식

원문은 이렇게 마무리합니다. **"이게 설정의 전부입니다. SharePoint 문서 라이브러리를 지식 소스로 추가하세요. 그 외에 구성할 것은 없습니다."**

---

## 내장 도구 두 개, 서로 다른 역할

GitHub Copilot harness 에이전트는 SharePoint 지식에 대해 **두 개의 내장 도구**를 받습니다. 각각 고유한 스키마가 있어 에이전트가 하나만 호출할지, 둘을 연결할지 판단합니다.

| 도구 | 주요 입력 | 반환 값 |
|---|---|---|
| **`sharepoint_metadata_filter`** | 작성자, 편집자, 날짜, 파일 형식, 폴더, 사용자 지정 열 필터, 포함할 열, 그룹화 기준 열 | 매칭 파일명과 URL, 열 값, 사용 가능한 열, **실제 매칭 수**, 빈 값 개수, 그룹별 합계 |
| **`knowledge_search_sharepoint`** | 필수 `query`, 선택적 `search_query`(재작성 쿼리), 선택적 `scopeUrls` | 선택된 SharePoint 범위의 검색 결과 — 문서 제목, URL, 참조 ID |

### 메타데이터 도구 단독 사용

메타데이터 도구는 **독립적으로 동작**할 수 있습니다. 예를 들어 **"나라별로 문서가 몇 건씩 배정돼 있나?"** 라는 질문에는 모든 파일을 열어 검색할 필요가 없습니다.

에이전트가 보내는 입력:

```json
{"groupByColumn":"Country"}
```

도구가 반환하는 값 — 에이전트에게 표시된 행만이 아니라 **서버에서 계산한 합계**입니다.

```json
{
  "aggregation": true,
  "groupBy": "Country",
  "totalMatched": 9,
  "blankCount": 6,
  "availableColumns": ["Image Tags", "Country", "Author", "Modified By"],
  "groups": [
    {"value": "US", "count": 2},
    {"value": "EU", "count": 1}
  ],
  "backend": "sharepoint_rest"
}
```

`totalMatched`, `blankCount`, `availableColumns` 같은 값이 함께 나온다는 점이 실무적으로 유용합니다. **"Country 값이 비어 있는 문서가 6건"** 같은 정보를 바로 얻을 수 있으니까요.

### 두 도구를 연결하기

더 흥미로운 경우는 **체이닝**입니다. `Country` 열이 있는 라이브러리에 이런 질문이 들어옵니다.

> "Contoso가 미국에서 제공하는 직원 복리후생은 무엇인가요?"

**1단계** — `sharepoint_metadata_filter`를 `Country = US`로 호출합니다. 매칭 파일과 URL이 반환됩니다.

**2단계** — 그 URL들을 지식 검색 도구에 넘깁니다.

```json
{
  "search_query": "What employee benefits does Contoso offer in the US?",
  "query": "What employee benefits do we offer in the US?",
  "scopeUrls": [
    "https://pplatform.sharepoint.com/Shared%20Documents/Contoso%20HR%20Documents/Contoso%20Benefits.docx",
    "https://pplatform.sharepoint.com/Shared%20Documents/Contoso%20HR%20Documents/Contoso%20HR%20policies.docx"
  ]
}
```

**결과** — 지정된 URL 범위 안에서만 검색해 매칭 문서를 반환합니다.

```
[2 results]

Title: Contoso Benefits.docx
URL: https://pplatform.sharepoint.com/.../Contoso Benefits.docx
ReferenceId: turn1doc1

Title: Contoso HR policies.docx
URL: https://pplatform.sharepoint.com/.../Contoso HR policies.docx
ReferenceId: turn1doc2
```

에이전트가 **매번 체이닝할 필요는 없습니다.** 인벤토리·집계 질문에는 메타데이터 필터링만, 일반 내용 질문에는 지식 검색만, 메타데이터가 문서 범위를 결정할 때만 둘 다 사용합니다.

---

## 안내는 하되, 모든 결정을 스크립트로 짜지 않기

[Knowledge Source Router 스킬](https://microsoft.github.io/cat-agent-skills/skills/knowledge-source-router/)은 **의도적으로 엄격한** 국가 라우팅 워크플로를 보여 줍니다. 라이브러리 메타데이터를 검사하고, 매칭 파일을 모두 가져오고, 그 파일 URL만 검색하고, **미배정·제외 문서를 보고**하도록 지시합니다.

원문은 이 수준의 안내가 **언제 필요한지**를 분명히 합니다.

> 순서가 **반복 가능하고 검사하기 쉬워야 할 때** 유용합니다. **모든 에이전트에 필요한 것은 아닙니다.** 명확한 에이전트 지시문과 잘 설명된 지식 소스가 있으면, 메타데이터 필터링이 언제 관련 있는지와 지식 검색과 어떻게 결합할지를 **에이전트가 판단하게 둘 수도** 있습니다.

권장 접근은 이렇습니다.

**가장 가벼운 안내로 시작하세요.** 사용 사례에서 신뢰할 만한 결과가 나오는 수준으로요. 테스트에서 에이전트가 더 필요로 한다고 확인되면 그때 엄격한 단계를 추가합니다.

---

## 반드시 알아야 할 제약

원문이 별도로 강조하는 세 가지입니다.

### 1. 내장 도구는 공개 API가 아닙니다

> 내장 메타데이터·지식 검색 도구는 **구현 세부사항이지 공개 API가 아닙니다.** 이름, 매개변수, 동작이 **예고 없이 바뀔 수 있습니다.** 특정 내부 도구 계약에 의존하지 말고 **지원되는 Copilot Studio 기능을 중심으로** 설계하세요.

위에 나온 JSON 예시는 동작을 이해하기 위한 것이지, 그 스키마에 코드를 묶으라는 뜻이 아닙니다.

### 2. 권한을 대체하지 않습니다

> 메타데이터 필터링은 답변에 고려되는 콘텐츠를 **좁힐 뿐**입니다. **SharePoint 권한을 대체하거나 사용자가 읽을 수 없는 문서에 접근 권한을 주지 않습니다.** 로그인한 사용자에 대한 **SharePoint 권한 트리밍은 계속 적용**됩니다.

### 3. 메타데이터 품질이 여전히 관건입니다

> 좋은 메타데이터는 여전히 필수적입니다. 에이전트는 **라이브러리에 기록된 값**을 사용해야 하며, 파일명이나 문서 본문에서 나라·상태·소유자를 **추측해서는 안 됩니다.**

---

## 이것이 열어 주는 것

원문이 정리한 세 가지 활용입니다.

**수명 주기를 인지한 답변(Lifecycle-aware answers)**
라이브러리가 상태를 기록하고 있다면, 에이전트가 **승인된 최신 문서를 선호하고 초안이나 폐기된 자료를 피할** 수 있습니다.

**대상별 맞춤 안내(Audience-specific guidance)**
같은 SharePoint 사이트에 여러 부서·제품·시장 자료를 함께 두면서도, **각각을 위한 별도 지식 소스가 필요 없습니다.**

**라이브러리 인벤토리 질문**
"소유자별로 정책이 몇 건인가?", "Country 값이 없는 파일은 무엇인가?" 같은 질문에 **문서 텍스트에서 추론하는 대신 라이브러리 메타데이터로** 답할 수 있습니다.

원문의 마무리가 핵심을 짚습니다.

> 중요한 변화는 구성할 도구가 하나 더 생긴 것이 아닙니다. **어떤 문서가 해당되는가**와 **그 문서가 무엇을 말하는가**를 분리하는 **더 간단한 방법**입니다. 이로써 모든 변형을 하드코딩된 라우팅 분기로 만들지 않고도 메타데이터 인지 지식 시나리오가 가능해집니다.

---

## 한국 메이커·도입 담당자를 위한 체크포인트

- **라이브러리 열 정비가 선행 조건**: 이 기능의 효과는 **메타데이터가 얼마나 잘 채워져 있느냐**에 정비례합니다. `blankCount`로 빈 값을 확인할 수 있지만, 애초에 값이 없으면 필터링이 무의미합니다. **기존 라이브러리의 열 입력 상태부터 점검**하세요.
- **국내 조직에서 특히 유용한 시나리오**: 계열사·사업부별로 다른 규정, 사업장별 안전 수칙, 지역별 인사 정책처럼 **"같은 주제인데 대상이 갈리는" 문서**가 많은 조직에 잘 맞습니다.
- **문서 상태 관리와 연계**: 승인 상태 열이 있다면 **초안·폐기 문서를 답변에서 배제**할 수 있습니다. 문서 관리 프로세스와 에이전트를 연결하는 실질적 방법입니다.
- **권한 정리는 별개로 유지**: 메타데이터 필터링이 권한을 대체하지 않습니다. **SharePoint 권한 트리밍이 그대로 적용**되므로, 권한 설정이 느슨하면 여전히 노출 범위가 넓습니다.
- **내부 도구 스키마에 의존하지 마세요**: 도구 이름과 매개변수는 예고 없이 바뀔 수 있습니다. 커스텀 로직을 짤 때 이 계약에 묶지 마세요.
- **가벼운 안내부터 시작**: Knowledge Source Router 스킬 같은 엄격한 워크플로는 **반복 가능성과 검사 용이성이 중요할 때** 쓰세요. 처음부터 모든 단계를 스크립트로 짜면 유지 부담만 커집니다.
- **harness 확인 필수**: 이 기능은 **GitHub Copilot harness** 기반 에이전트의 것입니다. Standard harness 에이전트에는 해당하지 않습니다.

---

## 마무리

메타데이터를 활용한 지식 검색은 오래 요청되어 온 기능이었고, 그동안 우회 방법은 **분기마다 토픽을 만드는 방식**이었습니다. 나라가 하나 늘면 설정도 하나 늘어나는 구조였죠.

이번 변화는 그 부담을 없앱니다. **라이브러리를 지식 소스로 추가하는 것이 설정의 전부**이고, 나머지는 에이전트가 판단합니다. 대신 그만큼 **메타데이터를 제대로 관리하는 일**이 중요해졌습니다.

원문은 이렇게 묻습니다. **여러분이 만들고 싶었던 메타데이터 기반 시나리오는 무엇인가요?**

---

> **출처**
>
> - 원문 제목: *SharePoint Metadata Filtering in Copilot Studio: From Topic Logic to Agent Decisions*
> - 링크: [https://microsoft.github.io/mcscatblog/posts/sharepoint-metadata-filtering/](https://microsoft.github.io/mcscatblog/posts/sharepoint-metadata-filtering/)
>
> 자세한 내용은 원문을 참조하세요.
