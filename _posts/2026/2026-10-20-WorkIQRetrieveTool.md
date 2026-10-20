---
title: "에이전트에게 회사의 맥락을 주는 법: Work IQ retrieve 도구 제대로 쓰기"
date: 2026-10-20T00:00:00 KST
categories:
  - Copilot
tags:
  - WorkIQ
  - MCP
  - Retrieval
  - Microsoft365
  - AgentDevelopment
excerpt: "Work IQ의 새 MCP retrieve 도구는 메일·파일·회의·Teams와 연결된 기업 데이터에서 에이전트의 답변 근거를 찾습니다. 검색 전략과 소스 제한, 인용이 포함된 markdown 응답 처리, 개발자가 주의할 파라미터 조합을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트에게 회사의 맥락을 주는 법: Work IQ retrieve 도구 제대로 쓰기

“출시 결정은 무엇이고, 후속 작업 담당자는 누구인가?”라는 질문의 답이 문서 한 곳에만 있지는 않습니다. 결정은 파일에, 담당자는 회의에, 추가 설명은 메일과 Teams 대화에 나뉘어 있을 수 있습니다.

Microsoft 365 Developer Blog는 2026년 10월 20일 **Work IQ의 새 MCP 도구 `retrieve`**를 소개했습니다. 여러 업무 소스에서 관련 근거를 찾고, 에이전트가 이를 바탕으로 답하도록 하는 검색 계층입니다. 소스마다 별도 검색 체계를 만드는 부담을 줄이는 방향입니다.

중요한 전제도 있습니다. 사용자는 **자신에게 접근 권한이 있는 업무 소스의 정보만 조회**할 수 있습니다. 검색 범위가 넓어진다는 것이 권한 경계를 넘어선다는 뜻은 아닙니다.

---

## retrieve는 무엇을 반환하나요?

`retrieve`는 메일, 파일, 회의, Teams 메시지, 사람 정보와 연결된 기업 소스를 검색합니다. 원문은 이를 기존 Copilot Retrieval API를 에이전트 활용에 맞게 발전시킨 도구로 설명합니다.

응답은 크게 두 부분입니다.

| 응답 요소 | 용도 |
|---|---|
| `markdown` | 인라인 인용을 포함하는 모델용 근거 문맥. 답변을 작성할 때 기준으로 사용 |
| `retrievalHits` | 소스별 검색 결과와 구조화된 메타데이터. 인용 연결과 원문 링크 처리에 활용 |

응답 페이로드의 네임스페이스는 `application/vnd.ms-workiq.retrieval`입니다. 개별 hit에는 `id`, `resourceId`, `webUrl`, `entityUrl`, `entityType`, `contentProtection`, `resourceMetadata`, `sensitivityLabel` 등이 포함될 수 있습니다. 모든 결과에 모든 필드가 항상 존재한다고 가정하지 않아야 합니다.

**답변은 `markdown`에 근거해 작성하고, 인용 ID를 `retrievalHits`의 개별 결과와 연결**하는 것이 핵심입니다. 요약 과정에서도 인용을 보존하고, 링크나 소스별 처리가 필요하면 hit의 메타데이터를 사용합니다.

## 검색과 업무 위임을 구분하세요

원문은 검색과 위임을 명확히 구분합니다.

- `retrieve`: 현재 에이전트가 사용할 근거와 문맥 수집
- `ask`, `do_action`: 다른 에이전트에 작업 위임. 필요하면 대상 에이전트 ID 지정

즉, 근거를 찾는 요청에 업무 실행이나 암묵적 라우팅까지 기대하지 않는 설계가 필요합니다. 자료를 수집하는 단계와 다른 에이전트에게 실제 일을 맡기는 단계를 구분하면 동작을 이해하기 쉽습니다.

## strategy: 넓게 찾을지, 인덱스 안에서 찾을지

| 값 | 검색 범위와 사용 기준 |
|---|---|
| `copilot` | 기본값. 인덱싱된 Microsoft 365 콘텐츠뿐 아니라 페더레이션 커넥터, 외부 데이터 소스, MCP 도구도 검색 가능. 자료 위치가 불명확하거나 인덱스 밖에 있을 때 사용 |
| `grounding` | Microsoft 365 인덱스의 SharePoint, OneDrive, Teams, Outlook 콘텐츠로 제한 |

허용되는 값은 이 두 가지뿐이며 **다른 값은 거부**됩니다. 단순한 응답 스타일 옵션이 아니라 검색 대상의 범위 선택입니다.

## capabilities로 소스를 더 좁히기

`capabilities`는 Declarative Agent의 capability 형태를 사용하는 선택적 허용 목록입니다. 지원 항목은 `People`, `Meetings`, `OneDriveAndSharePoint`, `Email`, `TeamsMessages`, `Dataverse`, `GraphConnectors`입니다.

capability별로 지원되는 범위 필드를 사용하면 특정 SharePoint 사이트, OneDrive 위치, SharePoint Embedded 컨테이너, 공유 사서함이나 특정 메일 폴더, 단일 Federated connector 등을 대상으로 지정할 수 있습니다.

**목록을 생략하거나 빈 배열을 전달하면 검색을 차단하는 것이 아닙니다.** 선택한 에이전트가 사용할 수 있는 모든 소스가 범위에 남습니다.

조합 제한도 중요합니다.

- `capabilities` 목록은 기본값이 아닌 `agentId`와 함께 사용할 수 없습니다.
- `grounding` 전략에는 `Dataverse`와 `GraphConnectors`를 함께 사용할 수 없습니다.

구체적인 범위 필드 이름은 capability별 공식 스키마를 확인해야 합니다. 임의의 필드를 추가해 범위가 제한될 것이라고 가정해서는 안 됩니다.

## 파라미터 한눈에 보기

| 파라미터 | 의미와 주의점 |
|---|---|
| `query` | 필수 자연어 검색 요청. 빈 문자열이나 공백만 있는 입력은 유효하지 않음 |
| `includeDeveloperCard` | 기본값 `false`. `true`이면 백엔드의 에이전트 메타데이터, 도구 호출 정보, 검색 요약 등 선택적 진단 정보 요청 |
| `agentId` | 사용자 지정 Copilot 에이전트(`bizchat-as-gpt-scenario`) 대상 지정. ID가 요청에 포함됨 |
| `strategy` | `copilot` 또는 `grounding` |
| `capabilities` | 선택적 소스 허용 목록과 해당 capability의 지원 범위 |

진단이 필요할 때는 `includeDeveloperCard: true`를 요청하고, 일반 검색 흐름에서는 기본값 `false`를 사용하는 방식이 원문에 제시됩니다.

## Interactive Demo에서 시작하기

[Interactive Demo](https://aka.ms/copilot.dev)에서 Work IQ MCP 도구를 확인할 수 있습니다. 원문의 개념 예제를 한국어 업무 질문으로 바꾸면 다음과 같습니다.

```json
{
  "query": "최신 출시 결정과 후속 작업 담당자, 그 근거가 된 회의나 문서를 찾아줘",
  "strategy": "copilot",
  "includeDeveloperCard": false
}
```

이는 MCP 도구의 입력을 설명하는 예시이며, 인증이나 연결 설정까지 포함한 독립 실행 코드는 아닙니다.

![Work IQ retrieve 도구를 실행하는 Interactive Demo 화면](/mwkorea/assets/images/2026-10-20-WorkIQRetrieveTool/image1.webp)

같은 질문을 `"strategy": "grounding"`으로 실행하면 인덱스 중심 검색과 비교할 수 있습니다. 더 좁은 범위가 필요하면 지원되는 capability 객체 배열을 전달하되 위 조합 제한을 지켜야 합니다.

### 실제 데모 영상

원문에 포함된 **Work IQ: MCP Retrieve Tool** 데모입니다.

{% include video id="mwl4fev1hDI" provider="youtube" %}

## 응답을 애플리케이션에 연결하는 순서

1. `application/vnd.ms-workiq.retrieval` 안의 `markdown`을 모델이 참고할 근거로 사용합니다.
2. 답변에 남긴 인용 ID를 `retrievalHits`의 `id`와 연결합니다.
3. 원문 이동에는 `webUrl` 등 실제 제공된 링크 메타데이터를 사용합니다.
4. 민감도나 콘텐츠 보호에 따른 처리가 필요하면 해당 메타데이터를 확인합니다.

원문의 축약 응답 예시에는 `resultCount`와 `stoppedReason`도 나옵니다. 예시의 건수나 URL은 실제 결과가 아니라 구조를 설명하기 위한 값이므로 애플리케이션에 고정하지 않아야 합니다.

한국 조직에서는 특히 부서별 문서 권한과 공유 사서함 범위를 확인하고, 접근 권한이 다른 사용자로 결과를 비교하는 검증을 권합니다. 이는 도입 검토 제안입니다. 검색 결과가 있다는 사실만으로 모든 사용자에게 같은 근거를 재공유해도 된다고 판단해서는 안 됩니다.

## 공개 시점과 공식 문서

이 글은 **2026년 10월 20일 Developer Blog의 도구 소개**를 기준으로 합니다. 원문은 Interactive Demo와 사용 문서를 안내하지만 별도의 GA 선언이나 테넌트별 제공 일정을 명시하지는 않습니다.

구현 시에는 [retrieve 도구 문서](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/mcp/retrieve)와 [Copilot Retrieval API 마이그레이션 안내](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/mcp/migrate-retrieval-api)를 확인해야 합니다. 문서가 이후 갱신될 수 있으므로 원문 시점의 설명과 실제 적용 시점의 스키마를 구분하는 것이 좋습니다.

원문은 추가 논의를 위한 행사로 **2026년 11월 17~20일 샌프란시스코 Microsoft Ignite**도 안내합니다. 이 행사 일정은 도구의 출시일을 뜻하지 않습니다.

## 마무리

`retrieve`의 핵심은 검색 결과를 나열하는 데 있지 않습니다. **모델이 읽을 근거, 사용자에게 보여줄 인용, 애플리케이션이 처리할 소스 메타데이터를 함께 연결**한다는 점입니다.

개발자는 검색 전략과 범위를 명시적으로 선택하고, 반환된 인용을 보존하며, 조회와 실행 위임을 분리하는 것부터 시작하면 됩니다.

> **출처**: [Work IQ: the new retrieve tool](https://devblogs.microsoft.com/microsoft365dev/work-iq-retrieve-october-2026/) — Microsoft 365 Developer Blog, 2026년 10월 20일. 자세한 내용은 원문 참조.
