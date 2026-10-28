---
title: "하나의 SDK로 두 Copilot Studio harness 연결: Entra 로그인과 활동 표시까지"
date: 2026-10-21T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Microsoft365AgentsSDK
  - GitHubCopilot
  - React
  - WebChat
  - EntraID
  - Preview
excerpt: "Copilot Studio SDK 클라이언트가 표준 harness와 GitHub Copilot harness를 같은 대화 방식으로 연결하는 프리뷰 예제가 공개됐습니다. Entra 인증을 유지한 React 연결 방법과 reasoning·도구 호출을 WebChat 활동 그룹에 표시하는 구조, 버전 및 지역 제약을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 하나의 SDK로 두 Copilot Studio harness 연결: Entra 로그인과 활동 표시까지

Copilot Studio 에이전트를 자체 웹앱에 넣을 때 harness가 달라진다고 로그인과 대화 UI까지 새로 만들어야 할까요? Microsoft Copilot Studio Customer Advisory Team의 기술 블로그는 같은 SDK 클라이언트로 표준 harness와 GitHub Copilot harness를 연결하는 방법을 소개했습니다.

핵심은 **environment ID와 agent schema name을 넘기고 기존 대화 메서드를 유지**하는 것입니다. 앱에서는 Entra ID로 사용자를 로그인시키고, 에이전트의 인증 설정은 **Authenticate with Microsoft**로 유지합니다.

다만 이 글은 **2026년 10월 프리뷰 예제**입니다. 원문은 당시 공식 통합 개요가 GitHub Copilot harness 에이전트를 아직 공식 지원 대상으로 표시하지 않는다고 경고합니다. 샘플에서 동작했다는 사실과 공식 안정 버전 지원을 구분해야 합니다.

![두 Copilot Studio harness의 SDK 통합을 소개하는 이미지](/mwkorea/assets/images/2026-10-21-CopilotStudioSdkBothHarnesses/image1.png)

---

## 지원 상태와 먼저 확인할 전제조건

원문 기준으로 새 지원은 JavaScript와 .NET 클라이언트에 포함되어 있고, **Python은 예정**입니다. 지역별 엔드포인트 배포가 진행 중이므로 먼저 **early release environment**에서 시험할 것을 권합니다.

실습에는 다음이 필요합니다.

- **Node.js 22**와 React WebChat 샘플
- 게시된 에이전트, **Authenticate with Microsoft** 인증 설정, 접근 권한이 있는 사용자
- 에이전트와 같은 테넌트의 Entra 앱 등록
- SPA 로그인에 사용할 tenant ID와 application/client ID

WebChat은 스트리밍, 대화 기록 사용자 지정과 접고 펼치는 활동 그룹을 제공하지만 필수는 아닙니다. 이미 자체 프런트엔드가 있다면 같은 SDK를 그 UI에 연결할 수 있습니다.

## 샘플과 패키지 버전을 고정합니다

원문은 [React WebChat 샘플](https://github.com/microsoft/Agents/tree/main/samples/nodejs/copilotstudio-webchat-react)의 특정 리비전과 패키지를 고정해 재현 조건을 명확히 합니다.

| 항목 | 원문에서 사용한 값 |
|---|---|
| 저장소 | `https://github.com/microsoft/Agents.git` |
| 샘플 리비전 | `1544bcae38f8865b1f095ffcf8df51561e302065` |
| 샘플 폴더 | `samples\nodejs\copilotstudio-webchat-react` |
| `@microsoft/agents-copilotstudio-client` | `1.10.0-beta.8.g158a2c07ad` |
| `@microsoft/agents-activity` | `1.10.0-beta.8.g158a2c07ad` |
| `botframework-webchat` | `4.19.2` |
| `botframework-webchat-fluent-theme` | `4.19.2` |
| `rxjs` | `7.8.2` |

저장소를 받은 뒤 해당 리비전으로 체크아웃하고, 샘플 폴더에서 위 버전을 `npm install --save-exact`로 설치하는 흐름입니다. **WebChat과 Fluent theme 버전은 일치시켜야 합니다.** 안정 버전 반영 여부는 [JavaScript 클라이언트 릴리스 노트](https://github.com/microsoft/Agents-for-js/releases)를 확인하세요. 이 글에서 최신 안정 버전 지원을 별도로 검증한 것은 아닙니다.

## Entra 앱 등록: 비밀 키를 브라우저에 넣지 않습니다

앱 등록에는 **`http://localhost:3000`을 Single-page application 리디렉션 URI로 등록**합니다. API 권한은 **Power Platform API > Delegated permissions > `CopilotStudio.Copilots.Invoke`**를 추가하고, 조직 정책에 따른 동의를 처리합니다.

이 구성은 **브라우저용 client secret을 요구하지 않으며, 에이전트를 manual authentication으로 전환할 필요도 없습니다.** 앱의 MSAL이 로그인과 액세스 토큰 획득을 담당하고, 샘플이 이 토큰을 Copilot Studio 클라이언트에 전달합니다.

권한과 로그인 구성의 자세한 내용은 [고정 리비전의 샘플 README](https://github.com/microsoft/Agents/blob/1544bcae38f8865b1f095ffcf8df51561e302065/samples/nodejs/copilotstudio-webchat-react/README.md#3-create-an-application-registration-in-entra-id)와 [SDK 통합 가이드](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-integrate-web-or-native-app-m365-agents-sdk#configure-your-app-registration-for-user-interactive-sign-in)를 참고하세요.

## 에이전트 연결 정보를 채웁니다

GitHub Copilot harness UI에는 당시 복사할 SDK endpoint가 없으므로 다음 값을 직접 확인합니다.

| 값 | 확인 위치 |
|---|---|
| Environment ID | Copilot Studio URL의 `/environments/` 뒤 값 |
| GitHub Copilot harness schema name | **… > Settings > Agent details** |
| 표준 harness schema name | **Settings > Advanced > Metadata** |
| Tenant ID, application/client ID | Entra 앱 등록의 **Overview** |

![Agent details에서 Schema name을 복사하는 화면](/mwkorea/assets/images/2026-10-21-CopilotStudioSdkBothHarnesses/image4.png)

Schema name은 화면에 전부 표시되지 않을 수 있으므로 복사 버튼을 사용합니다. 샘플의 `src\settings.js`에는 `ConnectionSettings`를 확장한 설정을 만들고 `environmentId`, `schemaName`, **`cloud: PowerPlatformCloud.Prod`**, **`copilotAgentType: AgentType.Published`**를 지정합니다. MSAL용 `tenantId`, `appClientId`, `authority`도 같은 설정 파일에서 관리하며 authority는 `https://login.microsoftonline.com`입니다.

**`directConnectUrl`은 설정하지 않습니다.** 이후 `npm start`를 실행하고 `http://localhost:3000`에서 로그인해 대화를 확인하는 흐름입니다.

원문 작성자는 같은 환경과 앱 등록으로 두 harness의 게시된 에이전트를 시험하면서 **`schemaName`만 변경**했다고 설명합니다. 두 경우 모두 스트리밍 활동과 같은 대화 안의 인사·후속 질문 응답을 확인한 범위의 결과이지, 모든 기능의 동일 동작을 검증했다는 뜻은 아닙니다.

## reasoning과 도구 호출을 기존 WebChat 그룹에 표시합니다

GitHub Copilot harness는 답변 외에 reasoning과 도구 호출 활동을 보낼 수 있습니다. 기본 React 샘플은 이를 표시하지 않으므로, 원문은 SDK 활동을 WebChat이 기대하는 활동 그룹 형식으로 변환하는 헬퍼를 제공합니다.

![접힌 Agent activity 그룹](/mwkorea/assets/images/2026-10-21-CopilotStudioSdkBothHarnesses/image2.png)

![펼친 그룹의 reasoning과 Get items 도구 호출 완료 상태](/mwkorea/assets/images/2026-10-21-CopilotStudioSdkBothHarnesses/image3.png)

기존 샘플의 `src` 폴더에 넣는 파일은 다음 세 가지이며, 원문은 다운로드 코드를 MIT 라이선스로 제공합니다.

| 파일 | 역할 |
|---|---|
| [activityDetails.ts](https://microsoft.github.io/mcscatblog/assets/posts/copilot-studio-sdk-both-harnesses/activityDetails.ts) | thought 갱신과 도구 상태 수집 |
| [agentActivity.ts](https://microsoft.github.io/mcscatblog/assets/posts/copilot-studio-sdk-both-harnesses/agentActivity.ts) | 수집한 활동을 WebChat 기본 그룹에 연결 |
| [Chat.tsx](https://microsoft.github.io/mcscatblog/assets/posts/copilot-studio-sdk-both-harnesses/Chat.tsx) | 로그인·오류 표시·연결 정리를 포함한 대체 컴포넌트 |

기존 **`acquireToken.ts`는 유지**합니다. 인증을 바꾸는 작업이 아니라 표시 계층을 확장하는 작업이기 때문입니다.

`Chat.tsx`에서는 `CopilotStudioWebChat.createConnection` 대신 헬퍼의 `createAgentActivityConnection`을 사용합니다. 이 연결은 `CopilotStudioClient`를 받아 활동을 변환하며, `showReasoning`, `showToolCalls`로 표시 여부를 제어하고 `onBusyChange`, `onError`로 UI 상태와 오류 표시를 연결합니다.

**이 두 표시 옵션은 SDK 공식 옵션이 아니라 샘플 헬퍼의 옵션**입니다. 하나만 켜거나 둘 다 켜거나 모두 끌 수 있습니다.

## 활동을 어떻게 변환하고 무엇을 숨기나요?

| 서비스에서 받은 내용 | 화면 표시 |
|---|---|
| 스트리밍 또는 완성된 답변 | 일반 WebChat 답변 |
| `thought` 엔터티 | 엔터티의 `text`를 reasoning 단계로 표시 |
| `toolCall` 엔터티 | `toolCallId`로 연결한 도구 단계와 Started·Finished·Failed 상태 |

thought 텍스트가 추가될 때마다 메시지를 새로 만들지 않고 기존 단계를 갱신합니다. 같은 도구를 두 번 호출하면 별도 호출로 구분하고, 턴마다 그룹을 나누며, 중단된 턴은 중단 상태로 표시합니다.

레거시 도구 이벤트도 처리하고 일반 메시지와 추천 답장은 통과시킵니다. 반면 **도구 인자·실행 결과·비공개 planner 메타데이터는 활동 기록에 넣지 않습니다.** 별도의 노출 범위를 정한 예제라는 점이 중요합니다.

표시는 기존 `FluentThemeProvider`, `Composer`, `BasicWebChat`을 이용합니다. 전체 컴포넌트는 busy 또는 오류 상태에서 입력을 비활성화하고, 컴포넌트 밖의 `styleOptions`에 **`partGroupDefaultOpen: false`**를 지정합니다. 예제 범위를 대화에 집중시키기 위해 파일 업로드도 비활성화합니다.

## 구현 시 놓치지 말아야 할 제한

`showReasoning`을 켠다고 에이전트가 reasoning을 새로 생성하거나 모든 진행 메시지가 thought가 되는 것은 아닙니다. **서비스가 클라이언트에 실제 보내는 내용만 표시**하며, 수신 내용은 harness와 모델에 따라 달라집니다.

따라서 테스트에서는 로그인·권한·스트리밍뿐 아니라 반복 도구 호출, 실패와 중단, 연결 해제, 표시해서는 안 되는 데이터의 비노출까지 확인하는 것이 좋습니다. 이는 실무 검증을 위한 권고이며, 원문의 프리뷰 예제를 운영 지원 보장으로 해석해서는 안 됩니다.

## 마무리

이번 예제의 가치는 harness가 달라도 **인증과 대화 클라이언트는 재사용하고, 활동 표시만 확장할 수 있는 구조**를 보여준다는 데 있습니다. 고정된 버전과 early release 환경으로 재현한 뒤 공식 지원 상태와 지역별 엔드포인트 제공을 확인하면서 적용하세요.

> **출처**: [One SDK Client for Both Copilot Studio Harnesses (Preview)](https://microsoft.github.io/mcscatblog/posts/copilot-studio-sdk-both-harnesses/). 자세한 내용은 원문 참조.
