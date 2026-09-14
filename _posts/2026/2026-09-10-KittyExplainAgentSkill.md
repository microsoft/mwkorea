---
title: "복잡한 개념을 고양이 그림으로 설명하기: Copilot 에이전트에 Kitty Explain 스킬 추가"
date: 2026-09-10T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotCamp
  - DeclarativeAgents
  - AgentBuilder
  - CustomSkills
  - Microsoft365AgentsToolkit
  - KittyExplain
excerpt: "Kitty Explain은 복잡한 내용을 고양이가 등장하는 한 장의 시각 자료로 설명하는 커스텀 스킬입니다. Agent Builder에 스킬 패키지를 추가하는 방법과 에이전트 지침의 역할, 프리뷰에서 확인할 제약을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 복잡한 개념을 고양이 그림으로 설명하기: Copilot 에이전트에 Kitty Explain 스킬 추가

기술을 쉽게 설명해 달라고 했는데 또 긴 글이 돌아오는 경우가 있습니다. 개념 사이의 관계를 한 장의 그림으로 보여 주면 이해하기 쉬울 때도 있죠. 여기에 고양이 사진과 손글씨 주석을 더한다면 어떨까요?

Copilot Camp의 **Kitty Explain** 실습은 선언형 에이전트에 커스텀 스킬을 추가해 이런 설명 이미지를 만드는 사례입니다. 겉으로는 고양이 밈이지만, 개발 관점에서 중요한 부분은 **작업 지침과 참고 자료를 하나의 패키지로 묶고, 필요할 때 에이전트가 사용하도록 연결하는 방법**입니다.

원문 데모는 Microsoft Learn 문서를 쉽게 설명하는 *Simple Learn* 에이전트에 이 스킬을 붙입니다. 이 글은 해당 실습을 소개하면서 2026년 9월 12일 확인한 Microsoft Learn의 프리뷰 조건도 함께 반영했습니다.

---

## Kitty Explain은 무엇을 만드나요

사용자가 전달한 내용을 읽고 핵심 개념을 골라 **고양이 사진과 스케치 노트가 어우러진 설명 이미지 한 장**으로 표현합니다. 공개된 스킬 지침은 사실적인 고양이 사진 느낌을 유지하고, 주변에 손으로 그린 화살표·도식·짧은 문구를 배치하도록 구성되어 있습니다.

![Kitty Explain 스킬로 Azure Blob Storage를 설명한 원문 데모 화면](/mwkorea/assets/images/2026-09-10-KittyExplainAgentSkill/image1.png)

스킬은 먼저 참고 이미지를 살펴보고, 내용에서 중요한 아이디어를 3~5개로 추립니다. 숫자와 용어를 임의로 만들지 않도록 하고, 글자를 너무 빽빽하게 넣지 않는 것도 지침에 포함됩니다. 단순히 “고양이로 그려 줘”라고 요청하는 것보다 결과의 구성과 작업 순서를 구체적으로 정의한 예입니다.

## 스킬은 긴 프롬프트와 무엇이 다른가요

Kitty Explain의 기본 구조는 간단합니다.

```text
kitty-explain
|-- SKILL.md
`-- references
    |-- kitty01.png
    |-- kitty02.png
    `-- ...
```

`SKILL.md`에는 YAML 형식의 이름·설명과 작업 지침이 들어갑니다. `references` 폴더는 이미지 생성 시 참고할 고양이 사진을 담습니다. 에이전트의 기본 지침은 “어떤 질문에 답하는가”를 맡고, 스킬은 “이 작업을 어떤 절차와 자료로 수행하는가”를 맡는 식으로 역할을 나눌 수 있습니다.

![에이전트에 설명 기능과 Kitty Explain 스킬을 연결하는 예시](/mwkorea/assets/images/2026-09-10-KittyExplainAgentSkill/image2.png)

Microsoft Learn은 스킬이 필요할 때 상세 지침을 불러오는 *progressive disclosure* 방식이라고 설명합니다. 모든 작업 절차를 기본 지침에 한꺼번에 넣는 대신, 필요한 기능을 별도 구성 요소로 관리하는 접근입니다.

원문은 같은 스킬 아이디어를 다른 에이전트에도 활용할 수 있다고 소개합니다. 다만 공식 지원 표에는 **현재 프리뷰에서 에이전트 간 재사용이 지원되지 않는다**고 적혀 있습니다. 소스 파일을 참고해 다른 에이전트용 패키지를 준비하는 것과, 한 번 등록한 스킬을 여러 에이전트가 공유·동기화하는 제품 기능은 구분해야 합니다.

## Agent Builder에서 추가하기

먼저 조직이 **Microsoft Frontier Preview** 대상인지 확인하세요. 공식 Agent Builder 문서는 적격 Microsoft 365 Copilot 라이선스 또는 종량제 접근과 조직의 Frontier 참여를 사전 조건으로 안내합니다. 모든 사용자에게 이미 정식 출시된 기능으로 보면 안 됩니다.

1. [공개 샘플 폴더](https://github.com/microsoft/m365-copilot-agents-playbook/tree/main/01-extend/demo-kitty-explain/kitty-explain)에서 `SKILL.md`와 `references`를 준비합니다.
2. 이 파일들을 `kitty-explain.zip`으로 묶습니다. 공식 패키지 예시는 ZIP을 열었을 때 루트에 `SKILL.md`가 있는 구조이므로, 불필요한 상위 폴더가 한 겹 더 들어가지 않았는지 확인합니다.
3. [Microsoft 365 Copilot](https://m365.cloud.microsoft/)에서 사용할 선언형 에이전트를 열거나 만듭니다. 원문처럼 문서나 URL의 내용을 쉽게 설명하는 에이전트로 시작할 수 있습니다.
4. **Configure > Skills > Add**에서 완성된 ZIP 패키지를 업로드합니다. `SKILL.md` 하나만 업로드하는 방식은 지원하지 않습니다.
5. 등록된 스킬의 이름, 설명, 지침과 포함 파일을 확인합니다.
6. 에이전트 지침에 스킬을 사용할 조건을 적고, **Suggested prompts**에 호출 예시를 넣은 뒤 **Preview**에서 시험합니다.

ZIP 내부는 다음처럼 준비합니다.

```text
kitty-explain.zip
|-- SKILL.md
`-- references
    |-- kitty01.png
    `-- kitty02.png
```

## 스킬을 사용할 때를 알려 주는 지침

파일을 올리는 것과 적절한 순간에 사용하는 것은 별개의 문제입니다. 에이전트가 일반 텍스트 설명과 고양이 시각 설명을 구분하도록 호출 조건을 적어 주세요.

아래는 원문의 취지를 바탕으로 작성한 한국어 지침 예시입니다.

```text
사용자가 "고양이로 설명해 줘", "Kitty Explain" 또는
"Explain [주제] by cats"라고 요청하면 kitty-explain 스킬을 사용한다.
스킬로 만든 설명 이미지를 주된 결과로 제시한다.
고양이 시각 설명을 요청하지 않았다면 기존 에이전트의 설명 방식을 따른다.
```

추천 프롬프트는 제목을 `Kitty Explain visual`, 내용을 `Explain [concept] by cats.`로 만들 수 있습니다. 한국어로 운영한다면 “이 문서의 핵심을 고양이 그림으로 설명해 줘”처럼 바꾸되, 입력한 표현이 호출 조건에도 반영되어 있는지 확인하세요.

시험할 때는 이미지만 생성됐는지 보지 말고 원래 개념이 정확히 전달되는지, 중요한 글자가 읽히는지, 고양이 설명을 요청하지 않았을 때 기존 응답 방식이 유지되는지도 살펴보는 것이 좋습니다.

## Agents Toolkit 경로는 원문과 최신 안내를 나눠 보기

Copilot Camp 원문은 Microsoft 365 Agents Toolkit 지원을 **Sneak Peek**로 소개하며 GA 때 제공될 예정이라고 설명합니다. 반면 이번에 확인한 Microsoft Learn에는 Toolkit의 **프리뷰 추가 절차**가 공개되어 있습니다. 원문의 전망을 현재 지원 상태로 그대로 옮기지 않고 구분해야 하는 부분입니다.

최신 안내는 선언형 에이전트 manifest **1.9**와 `TEAMSFX_AGENT_SKILLS=true` 환경 변수를 요구합니다. CLI의 `atk add skill --from PATH_TO_SKILL` 또는 Visual Studio Code 확장의 **Add Skill**을 이용하는 절차를 설명하며, 환경 변수를 나중에 설정했다면 VS Code를 완전히 다시 시작하도록 안내합니다.

원문에서 제시하는 패키지 구조의 핵심은 앱 패키지 안에 스킬 디렉터리를 넣고, 통합 `manifest.json`의 `agentSkills`에서 그 폴더를 참조하는 것입니다.

```text
appPackage
|-- manifest.json
|-- declarativeAgent.json
|-- instruction.txt
`-- skills
    `-- kitty-explain
        |-- SKILL.md
        `-- references
```

`manifest.json`에 병합하는 속성의 예시는 다음과 같습니다. 완전한 앱 manifest가 아니라 스킬 경로를 보여 주는 일부입니다.

```json
{
  "agentSkills": [
    {
      "folder": "./skills/kitty-explain"
    }
  ]
}
```

Toolkit에서는 ZIP이 아닌 **디렉터리**로 스킬을 추가합니다. 나머지 앱 정보와 선언형 에이전트 정의는 유지하고, 호환되는 manifest 및 배포 절차는 [공식 Toolkit 안내](https://learn.microsoft.com/microsoft-365/copilot/extensibility/build-declarative-agents-add-custom-skills)를 기준으로 맞추세요.

## 프리뷰에서 놓치기 쉬운 제약

| 항목 | 공식 문서의 안내 |
|---|---|
| 에이전트당 스킬 | 최대 8개 |
| `SKILL.md` 작업 지침 | 20,000자 미만, YAML 이름·설명 필수 |
| Agent Builder 업로드 | 스킬 ZIP 최대 50MB, 개별 파일 최대 25MB |
| Toolkit 패키지 | 스킬 디렉터리 사용, 전체 앱 패키지 최대 10MB |
| 디렉터리 깊이 | 최대 3 |
| 스킬과 embedded files의 동시 사용 | 현재 프리뷰에서 지원하지 않음 |
| 스크립트 실행 | 샌드박스 안에서 실행, 런타임 네트워크 접근·패키지 설치 불가 |

특히 스킬에 코드를 넣었다고 외부 URL이나 인증된 API를 스크립트에서 자유롭게 호출할 수 있는 것은 아닙니다. 공식 문서는 활성화된 커넥터·API 플러그인·MCP 기능은 에이전트의 오케스트레이터를 통해 사용하며, 샌드박스 스크립트가 이를 직접 호출하지는 못한다고 구분합니다.

업로드한 스킬 파일은 테넌트 범위의 SharePoint Embedded 컨테이너에 저장됩니다. 민감도 레이블과 관련 정책은 유지·적용되지만, 사용자 정의 권한이나 Double Key Encryption은 지원하지 않는다고 안내되어 있습니다.

샘플은 참고할 출발점입니다. 고객 자료나 내부 문서를 그림으로 바꿀 때도 결과물을 누구에게 보여 줄지, 이미지 안에 공개하면 안 되는 내용이 포함됐는지 검토해야 합니다.

## 원문 데모 영상

다음은 원문에 연결된 실제 데모입니다.

{% include video id="173fx_0X7gg" provider="youtube" %}

Kitty Explain을 통해 배울 수 있는 것은 고양이 그림을 만드는 요령만이 아닙니다. 작업 절차, 참고 이미지, 결과 형식을 패키지로 분리하고 에이전트 지침에는 호출 조건을 남기는 방법입니다. 같은 설계 원리를 교육용 도식이나 팀에서 반복해 만드는 설명 자료에도 적용해 볼 수 있습니다.

---

> **출처**
>
> - Copilot Camp: [A Fun Way to Learn with Kitty-Explain Skill for Agents](https://microsoft.github.io/copilot-camp/pages/beyond-labs/blogs/kitty-explain-skill/)
> - 공개 샘플: [Kitty Explain — Microsoft 365 Copilot Agent's Playbook](https://github.com/microsoft/m365-copilot-agents-playbook/tree/main/01-extend/demo-kitty-explain)
> - Microsoft Learn: [Custom skills in declarative agents (preview)](https://learn.microsoft.com/microsoft-365/copilot/extensibility/declarative-agent-skills)
> - Microsoft Learn: [Add custom skills in Agent Builder](https://learn.microsoft.com/microsoft-365/copilot/extensibility/agent-builder-add-skills)
> - Microsoft Learn: [Add custom skills with Microsoft 365 Agents Toolkit](https://learn.microsoft.com/microsoft-365/copilot/extensibility/build-declarative-agents-add-custom-skills)
>
> 자세한 내용은 원문 참조. 프리뷰 지원 범위는 변경될 수 있습니다. 최신 문서 확인일: 2026년 9월 12일.
>
> 원문 작성자: Tomomi Imura. 파일 날짜는 원문에 표시된 발행일인 2026년 9월 10일을 따릅니다.
>
> 본문 샘플 이미지는 Microsoft의 공개 Playbook 저장소에서 제공한 자료입니다. Copyright (c) 2026 Microsoft, [MIT License](/mwkorea/assets/images/2026-09-10-KittyExplainAgentSkill/LICENSE.txt).
