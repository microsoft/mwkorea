---
title: "wiqd 하나로: Microsoft Copilot 플러그인 가져오기·만들기·패키징까지"
date: 2026-09-30T00:00:00 KST
categories:
  - Copilot
tags:
  - WorkIQ
  - WIQD
  - MicrosoftCopilot
  - MCP
  - PluginDevelopment
excerpt: "Work IQ Developer Tools(WIQD)로 기존 에이전트 플러그인을 가져오거나 자연어로 새 플러그인을 설명해 Microsoft Copilot 패키징 워크플로를 완성하는 방법을 정리합니다. 스킬·MCP 커넥터·에이전트를 하나의 패키지로 묶는 CLI 흐름을 소개합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# wiqd 하나로: Microsoft Copilot 플러그인 가져오기·만들기·패키징까지

이미 만들어 둔 MCP 서버나 스킬, 다른 고객사를 위해 구축한 에이전트가 있다면, 그걸 처음부터 다시 만들어야 할까요? Microsoft 365 Developer Blog가 소개한 **Work IQ Developer Tools(WIQD)**는 기존 자산을 Microsoft Copilot 플러그인으로 바로 가져오거나, 자연어로 새 플러그인을 설명해 만들 수 있는 CLI 도구입니다.

이번 글은 해당 원문을 기준으로 정리하며, 자세한 내용은 원문을 참조하시기 바랍니다.

---

## 플러그인이란?

플러그인은 Microsoft Copilot에게 일을 처리하는 새로운 방법을 제공합니다. **스킬, MCP 서버, 에이전트** 중 하나 이상의 기능을 패키징해, Copilot이 조직에 중요한 워크플로를 지원할 수 있게 합니다.

처음 시작하는 경우라면 [Work IQ Developer Tools(WIQD) 공개 프리뷰 공지](https://devblogs.microsoft.com/microsoft365dev/announcing-the-preview-of-the-work-iq-developer-tools/)부터 참고할 수 있습니다. 하지만 대부분의 개발자는 빈 폴더에서 시작하지 않습니다. 이미 업무 흐름을 담은 스킬, 시스템에 연결된 MCP 서버, 다른 클라이언트를 위해 만든 에이전트가 있을 가능성이 큽니다. WIQD는 이런 기존 자산을 Copilot 플러그인의 출발점으로 삼을 수 있게 도와줍니다.

첫 선택은 단순합니다 — **가져오기(import) 또는 새로 만들기(create)**. 어느 쪽이든 GitHub Copilot 같은 선호하는 코딩 하네스를 통해 WIQD에 원하는 바를 말하면, 동일한 WIQD 명령 체계를 사용하게 됩니다.

> **프리뷰:** wiqd plugin 명령 체계는 현재 공개 프리뷰이며 변경될 수 있습니다.

## 가진 것으로 시작하기

기존 플러그인이 [Agent Plugins 포맷](https://agent-plugins.org/)을 사용한다면 WIQD로 바로 가져올 수 있습니다. 이 포맷은 스킬과 MCP 서버 설정을 패키징하며, WIQD는 지원되는 부분을 직접 수작업으로 재구성하지 않고 검토·확장 가능한 프로젝트로 가져옵니다.

[WIQD를 설치](https://microsoft.github.io/wiqd/getting-started/installation/)한 뒤 플러그인을 가져옵니다.

```bash
wiqd plugin import --path ./my-agent-plugin \
  --privacy-url https://contoso.com/privacy \
  --terms-url https://contoso.com/terms
```

가져오기 후에는 WIQD가 프로젝트에 무엇을 가져왔는지 확인하고, Microsoft Copilot에서 동작하는 방식을 다듬은 다음 검증·패키징 단계로 넘어갈 수 있습니다.

## 플러그인이 없다면? 말로 설명하세요

Copilot이 수행하길 원하는 작업부터 시작하면 됩니다. GitHub Copilot CLI용 WIQD 플러그인은 자연어로 원하는 결과를 설명하면 WIQD 명령으로 플러그인을 구성하고, 각 단계를 진행하며 보고합니다.

예를 들어 다음과 같이 요청할 수 있습니다.

```text
Create a standalone plugin called Triage Helper. Add a skill that triages incoming customer issues and connect it to our incident-management MCP server.
```

이 요청 뒤에서 WIQD는 다음과 같은 명령을 실행할 수 있습니다.

```bash
wiqd plugin create --name "Triage Helper"
wiqd plugin add skill --name "Triage Issues"
wiqd plugin add connector --name "Incident Management" \
  --description "Triage and manage customer incidents" \
  --url https://incidents.contoso.com/mcp
```

명령 체계를 먼저 익히지 않아도 아이디어에서 플러그인 프로젝트로 바로 이어갈 수 있으며, 같은 명령들은 터미널에서 직접 제어하고 싶을 때도 그대로 쓸 수 있습니다.

## 터미널에서 직접 플러그인 빌드하기

GitHub Copilot CLI 플러그인이 사용하는 WIQD 명령은 로컬 개발과 반복 가능한 자동화를 위해 터미널에서도 직접 사용할 수 있습니다. 아래 Bash 예제를 따라 하기 전에 [WIQD를 설치](https://microsoft.github.io/wiqd/getting-started/installation/)하세요.

`triage-helper`를 만들고, 신규 이슈를 위한 스킬을 스캐폴딩하고, 인시던트 관리 MCP 서버를 등록합니다.

```bash
# Create the plugin
wiqd plugin create --name triage-helper
cd triage-helper

# Add the capabilities it needs
wiqd plugin add skill --name "Triage Issues"
wiqd plugin add connector \
  --name "Incident Management" \
  --description "Triage and manage customer incidents" \
  --url https://incidents.contoso.com/mcp
```

명령은 프로젝트 구조를 만들어 줄 뿐, 스킬의 분류 지시문 작성과 MCP 서버에 필요한 인증 설정은 직접 해야 합니다. 플러그인 준비가 끝나면, CLI로 만들었든 자연어로 설명했든 기존 작업을 가져왔든 다음 단계는 동일합니다.

## 플러그인 검증 및 패키징

플러그인을 가져왔든 자연어나 WIQD 명령으로 만들었든, 플러그인 프로젝트 디렉터리에서 이어갑니다. Microsoft 365에 아무것도 프로비저닝하기 전에 로컬에서 먼저 점검합니다.

```bash
# Check declarative-agent artifacts, if present
wiqd plugin validate
```

이는 **오프라인 점검**이며 플러그인 전체 리뷰가 아닙니다. 스킬 콘텐츠나 최상위 앱 매니페스트는 검사하지 않으므로, 스킬+커넥터 플러그인이라면 이 결과가 깨끗하다고 해서 전부 괜찮다는 의미는 아닙니다.

다음으로 로그인하고 Microsoft 365 리소스를 프로비저닝합니다. 프로비저닝은 환경을 변경하고 WIQD가 패키지를 만드는 데 필요한 정보를 제공합니다.

```bash
wiqd auth login --interactive
wiqd plugin provision
wiqd plugin package
wiqd plugin validate --mode deep
```

**딥 검증(deep validation)**은 빌드된 Microsoft 365 앱 패키지를 점검합니다. 이 패키지는 스킬과 MCP 커넥터 설정, 그리고 시나리오에 필요하다면 선언적 에이전트까지 하나의 단위로 묶어, 팀이 버전 관리·배포·지원할 수 있게 해줍니다.

검증된 패키지라고 해서 모든 Copilot 표면(surface)에서 같은 경험을 보장하지는 않습니다. 공유·게시 전에 각 표면이 플러그인에 필요한 기능을 지원하는지 확인해야 합니다.

## 사용자에게 플러그인 전달하기

조직 내부용이라면 WIQD로 특정 사용자 또는 전체 테넌트에 공유할 수 있습니다.

```bash
wiqd plugin share --scope users --email developer@contoso.com
# Or make it available across the tenant
wiqd plugin share --scope tenant
```

조직 외부 고객을 대상으로 하는 ISV라면, 패키지 자체가 제출·지원하는 플러그인이 되며 고객이 스킬·매니페스트·커넥터 설정을 직접 조합할 필요가 없습니다. 이 패키지를 **Partner Center**에 제출해 Microsoft 인증을 받고, 출시 전 피드백을 반영하면 됩니다. WIQD는 패키지를 준비하고, 공개 제출·인증은 Partner Center가 처리합니다.

## 한 번 빌드하고, 표면마다 검증하기

Agent Plugins 포맷은 스킬과 MCP 서버 설정에 이식 가능한 형태를 부여합니다. WIQD는 지원되는 기존 작업을 Microsoft 365 플러그인 프로젝트로 가져오거나 새로 만들도록 돕고, 배포용으로 패키징합니다. Microsoft Copilot의 **플러그인 레지스트리**는 참여 중인 Microsoft 경험들이 플러그인을 찾을 수 있는 관리형 레코드를 제공합니다.

하나의 패키지가 하나의 런타임을 의미하지는 않습니다. 각 Copilot 경험이 어떤 기능을 지원하는지, 사용자가 플러그인을 어떻게 받는지, 해당 기능이 어떻게 실행되는지를 각자 결정합니다. 스킬·MCP 커넥터·에이전트를 모두 담은 플러그인이라도 모든 표면에서 동일한 경험을 제공하지 않을 수 있습니다.

기존 자산을 가져오든 새로 만들든, 결국 하나의 패키지로 참여 경험 전반을 아우르되, 실제 사용자가 쓰는 표면에서 호환성을 확인하는 구조입니다.

## 시작하기

- [WIQD 시작하기](https://microsoft.github.io/wiqd/getting-started/installation/)
- [Agent Plugins 사양](https://agent-plugins.org/specification) 검토
- [WIQD 플러그인 안내](https://github.com/microsoft/wiqd/blob/main/docs/src/content/docs/getting-started/build-a-plugin.md) 따라하기
- [wiqd plugin 명령 레퍼런스](https://github.com/microsoft/wiqd/blob/main/docs/src/content/docs/cli/reference.md#wiqd-plugin) 탐색
- WIQD가 패키징·검증한 뒤 [Microsoft 365 Copilot 게시 개요](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/publish) 및 [Partner Center 마켓플레이스 제출 안내](https://learn.microsoft.com/en-us/partner-center/marketplace-offers/submit-to-appsource-via-partner-center) 따라하기

## 마무리

WIQD는 "플러그인을 또 처음부터 만들어야 하나"라는 질문에 대한 답을 "가져오거나, 말로 설명하거나, 명령으로 직접 빌드하라"로 바꿔줍니다. 스킬·MCP 커넥터·에이전트를 이미 운영 중인 조직이라면, 공개 프리뷰 단계에서 `wiqd plugin import`부터 시도해 보는 것을 추천합니다.

> 출처: **Bring your plugin to Microsoft Copilot with Work IQ Developer Tools**
> 원문: https://devblogs.microsoft.com/microsoft365dev/bring-your-plugin-to-microsoft-copilot-with-wiqd/
> 자세한 내용은 원문 참조
