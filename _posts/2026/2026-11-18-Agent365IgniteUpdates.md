---
title: "Ignite 2026의 Agent 365: 에이전트 발견부터 보안·비용·가치까지"
date: 2026-11-18T00:00:00 KST
categories:
  - Copilot
tags:
  - Agent365
  - Ignite2026
  - EntraAgentID
  - Governance
  - FinOps
  - Security
excerpt: "Microsoft Agent 365가 타사·로컬·섀도 에이전트까지 관측하고 관리하는 방향으로 확장됩니다. Ignite 2026 발표의 신원·도구 거버넌스·동적 위험·Business Analytics 기능을 GA와 프리뷰로 나눠 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Ignite 2026의 Agent 365: 에이전트 발견부터 보안·비용·가치까지

Microsoft는 2026년 5월 출시 이후 Agent 365에 등록된 에이전트가 **5,000만 개 이상**이라고 밝혔습니다. 에이전트가 늘수록 “누가 소유하고, 어떤 권한으로 무엇을 하며, 비용 대비 가치가 있는가”를 함께 파악해야 합니다.

Ignite 2026 발표는 Agent 365를 Microsoft와 타사 에이전트를 함께 관측하는 플랫폼으로 확장합니다. IT·보안·비즈니스 조직이 같은 맥락을 공유하되, 각자 사용하는 도구에서 조치하도록 연결하는 것이 핵심입니다.

![Microsoft Agent 365 Ignite 2026 발표 대표 이미지](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image1.png)

---

## 먼저 구분할 것: GA와 프리뷰

원문 발표 시점의 상태를 요약하면 다음과 같습니다. 같은 제품 안에서도 기능별 단계와 플랫폼 지원 범위가 다릅니다.

| 기능 | 제공 상태 |
|---|---|
| Defender의 로컬 에이전트 발견 | GA, 관리형 Windows·macOS 대상 |
| Windows 로컬 에이전트 런타임 보호 | GA |
| Tools Registry | GA |
| 플러그인·스킬 거버넌스 | GA |
| 적격 M365 구독의 Microsoft 에이전트 기본 사용 인사이트 | 라이선스 변경 GA |
| Connected platforms 확장·비밀 없는 인증 | 프리뷰, 플랫폼별 차이 있음 |
| 동적 에이전트 위험·로컬 신원·멀티테넌트 관리 | 프리뷰 |
| Agent 365 Business Analytics | Frontier 프리뷰 |
| 외부 도구 카탈로그 연결 | 12월 비공개 프리뷰 예정 |
| Action center | 12월 프리뷰 예정 |

## 1. 타사 플랫폼과 로컬 에이전트를 하나의 인벤토리로

### Connected platforms와 Entra Agent ID

지원 플랫폼을 한 번 연결하면 에이전트 코드를 바꾸지 않고 Agent 365 레지스트리로 동기화할 수 있습니다. 출처 플랫폼, 소유자, 도구 등의 정보를 제공하며, 지원되는 플랫폼에서는 요청·실행·모델 및 도구 호출·성공 여부도 확인합니다.

Entra Agent ID 확장 대상은 Salesforce Agentforce, Amazon AgentCore, Google Vertex AI, Databricks, Snowflake, Anthropic Claude Managed Agents, OpenAI, Oracle, SAP, ServiceNow, UiPath 등이며 **12월까지 배포 완료 예정**입니다. 플랫폼별 역량은 동일하지 않습니다.

단계별 연결 마법사는 원본 플랫폼과 Agent 365 양쪽의 권한·검증 절차를 안내합니다. 지원 연결의 **secretless authentication**은 Entra workload identity federation을 사용해 장기 비밀 생성·저장·교체 부담을 줄입니다.

![Connected platforms 관련 원문 화면](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image2.png)

### 로컬·섀도 에이전트 발견

Defender와 Entra Global Secure Access는 Claude Code, GitHub Copilot CLI 등 **60종 이상 로컬 AI 에이전트**와 구성된 MCP 서버의 발견을 지원합니다. Defender는 관리형 Windows·macOS 장치의 사용자·장치와 연결하고, Global Secure Access는 목적지·MCP 서버·리소스의 네트워크 가시성을 더합니다.

Defender의 로컬 발견은 GA이지만 Global Secure Access의 네트워크 발견과 Agent 레지스트리의 섀도 AI 발견은 프리뷰입니다.

![로컬 및 섀도 에이전트 관련 원문 화면](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image3.png)

발견된 로컬 에이전트에 별도 Entra Agent ID를 부여하는 기능은 GitHub Copilot CLI와 Claude Code부터 시작하는 프리뷰입니다. 사람과 에이전트의 활동을 구분하고 지원 접근 제어를 적용하는 기반이 됩니다. Entra Agent ID의 Microsoft Autopilot 확장도 프리뷰입니다.

![로컬 에이전트 신원 관련 원문 화면](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image4.png)

## 2. 실행 추적과 도구·업무 가시성

**Export Agent Activity**는 에이전트 추적 데이터를 조직의 Azure Monitor와 Application Insights로 지속 동기화합니다. 관리자에게 에이전트·플랫폼 필터와 프롬프트·응답 포함 여부 제어를 제공해 개발자·SRE가 기존 대시보드와 쿼리로 실행·모델·도구 호출을 분석하도록 합니다. 원문 본문은 이 기능의 별도 GA 여부를 명시하지 않습니다.

![Agent Activity 내보내기 관련 원문 화면](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image5.png)

GA인 **Tools Registry**는 에이전트가 사용하는 도구와 연결 리소스를 중앙에서 파악하는 기반입니다. GitHub·Databricks Unity Catalog·게이트웨이 등 외부 카탈로그 연결은 12월 비공개 프리뷰 예정입니다.

![Tools Registry 관련 원문 화면](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image6.png)

**Agent Map use cases**는 세션을 수행 업무별로 분류해 중복 에이전트와 도입 경향을 찾는 프리뷰 기능입니다.

![Agent Map 사용 사례 관련 원문 화면](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image7.png)

## 3. 여러 테넌트와 기본 구독의 관리 범위

멀티테넌트 관리는 파트너나 여러 자회사를 가진 기업이 테넌트별 에이전트 구성과 접근자를 비교하고, 보안·규정 준수·위험 정보를 검토하며, 대규모 승인·차단을 수행하는 프리뷰입니다.

![멀티테넌트 관리 관련 원문 화면](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image8.png)

적격 Microsoft 365 구독에는 Microsoft 사전 제작 에이전트와 Microsoft 플랫폼에서 만든 에이전트의 개요·활성 사용자·활동·세션·예외율·실행 시간 등 기본 인사이트 접근이 확대됩니다. 이 라이선스 변경은 GA입니다.

반면 타사 에이전트 관리 인사이트와 고급 거버넌스·보안 등 프리미엄 역량에는 계속 **Agent 365 또는 ME7** 라이선스가 필요합니다.

![기본 에이전트 사용 인사이트 관련 원문 화면](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image9.png)

## 4. 플러그인·스킬·MCP와 에이전트 수명 주기 거버넌스

관리자는 Microsoft 365 Copilot·Cowork의 플러그인과 스킬을 사용자·그룹에 할당합니다. MCP 서버를 차단하기 전에 사용하는 에이전트와 의존 플러그인을 확인해 영향을 검토할 수 있습니다.

플러그인·스킬 거버넌스는 GA이며 **Azure AI Gateway·LiteLLM 게이트웨이 지원은 프리뷰**입니다.

![도구 거버넌스 관련 원문 화면 1](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image10.png)

![도구 거버넌스 관련 원문 화면 2](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image11.png)

![도구 거버넌스 관련 원문 화면 3](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image12.png)

로컬·섀도 에이전트 거버넌스도 프리뷰입니다. 미승인 에이전트에 Intune·Defender·Global Secure Access 제어를 적용하고, 승인된 에이전트에는 Intune 정책과 Windows의 Microsoft Execution Containers(MXC), 작업 범위 권한 및 위험 기반 제어를 조합합니다.

**Cowork용 Agent 365 플러그인**은 자연어로 인벤토리를 조사하고 거버넌스 작업을 수행하는 프리뷰입니다. 퇴사자 에이전트의 운영 유지나 손상된 커넥터에 노출된 에이전트 격리 같은 시나리오를 지원하며, 중대한 조치 전에는 관리자 승인을 위해 멈춥니다.

![Cowork와 Agent 365 플러그인 관련 원문 화면](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image13.png)

12월 프리뷰 예정인 **Action center**는 비활성·소유자 없는 에이전트부터 검토·정리 대상으로 제시합니다.

## 5. 정적 점검에서 동적 위험과 실행 보호로

**Dynamic agent risk**는 신원·접근·데이터·엔드포인트·클라우드·네트워크의 런타임 신호와 노출·영향 범위를 결합해 에이전트별 위험 수준을 갱신합니다. 관리 센터·Defender·Entra·Purview에서 같은 위험 수준을 공유하는 프리뷰이며, Microsoft Perception에서는 확장된 제한 프리뷰로 안내됩니다.

Entra Conditional Access 동적 제어는 로그인 시점뿐 아니라 **행동 시점**에 정책을 평가해 민감 작업 제한이나 사람 승인을 요구하는 방향입니다. 사용자 대신 행동하는 에이전트의 정책을 사용자 본인 정책과 구분하는 기능도 소개됩니다. 원문은 지원 시나리오 범위 내 적용임을 강조합니다.

Purview DLP의 Microsoft·주요 로컬 에이전트 지원 및 개별·그룹·조직 단위 정책 범위는 프리뷰입니다. 로컬 예시에는 Claude Code·Desktop, GitHub Copilot CLI·앱, VS Code의 Copilot·Claude Code 확장이 포함됩니다.

**Defender 런타임 보호는 Windows에서 GA**입니다. Claude Code, GitHub Copilot CLI, OpenClaw, ChatGPT Desktop(Chat) 등 지원 에이전트의 실행 루프 중요 지점을 검사합니다. Audit 또는 Block 모드를 Defender 포털·Intune에서 설정하며, Block 모드에서는 악성 지시를 차단하고 사용자에게 알립니다. 경고에는 에이전트·세션 맥락이 포함되어 SOC 인시던트와 연결됩니다.

타사 보안 태세 평가는 Amazon Bedrock·Google Gemini·Vertex AI·Anthropic Claude 에이전트로 확장되는 프리뷰입니다. Connected platforms 연결이 범위 편입의 출발점입니다.

Intune의 로컬 에이전트 제어와 Global Secure Access의 에이전트·MCP 네트워크 제어도 프리뷰입니다. MXC의 파일·네트워크 경계는 에이전트 외부에서 적용되어 스스로 권한을 늘릴 수 없도록 하며, 장치 전체를 비준수로 지정하는 옵션과는 구분됩니다.

![Intune 및 Global Secure Access 제어 관련 원문 화면](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image14.png)

## 6. AI 지출을 실제 업무 가치와 연결

**Agent 365 Business Analytics**는 지출·사용·가치를 한곳에서 보고, 사용 사례별 지원 시간·추정 가치·성공률·만족도 및 직원 설문을 결합하는 Frontier 프리뷰입니다. 예측과 시나리오 계획, 자연어 분석, Outlook·Teams를 통한 보기 공유도 소개됩니다.

![Business Analytics 개요 관련 원문 화면](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image15.png)

![Business Analytics 비용·예측 관련 원문 화면](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image16.png)

![Business Analytics 사용 사례 관련 원문 화면](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image17.png)

![Business Analytics 예측 조정 관련 원문 화면](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image18.png)

이 종합 발표는 Microsoft 서비스 분석에 테넌트 내 Copilot 라이선스 최소 1개가 필요하다고 설명합니다. 실제 순차 배포는 별도 MC1557727에서 **50개 이상 보유 Frontier 테넌트부터 시작해 12월 7일까지 전체 Frontier로 확대**한다고 안내하므로, 최소 라이선스 조건과 배포 순서를 구분해야 합니다. 연결된 타사 서비스 분석에는 Agent 365 및/또는 ME7이 필요합니다.

Cost Management는 사용자·그룹·조직·리소스별 한도·알림, 모델 접근 제어, 위임된 예산 관리, Graph API·데이터 내보내기·Fabric 연결을 통한 비용 배부를 지원하는 방향으로 확장됩니다.

![Agent 365 Cost Management 관련 원문 화면](/mwkorea/assets/images/2026-11-18-Agent365IgniteUpdates/image19.png)

## 한국 조직의 도입 순서

실무적으로는 승인 에이전트뿐 아니라 로컬·섀도 사용까지 인벤토리를 확보하고, 소유자·신원·권한과 도구 의존성을 연결하는 것이 먼저입니다. 이후 위험 제어와 민감정보 정책, 비용 한도 및 가치 계산 가정을 단계적으로 적용하는 편이 적절합니다.

모든 플랫폼이 같은 로그·차단·신원 기능을 제공한다고 가정하지 말고 [Connected platforms 문서](https://learn.microsoft.com/microsoft-agent-365/admin/connected-platforms)와 [Agent 365 시작 안내](https://learn.microsoft.com/microsoft-agent-365/get-started)에서 실제 지원 범위를 확인하세요. 원문의 일부 문서 링크는 검토용 주소이므로 공개 문서와 동일하게 접근 가능하다고 단정하지 않아야 합니다.

Ignite는 11월 17~20일 진행되며 원문은 BRK214(기업 규모 관리·보안), BRK260(FinOps), BRK345(거버넌스), BRK339(로컬 에이전트) 등의 세션을 안내합니다. Breakout은 온라인 및 행사 후 주문형 제공 예정이지만 Lightning talk와 Theater는 현장 참석자 대상입니다. 본문에 실제 임베드 영상은 없으며 [공식 세션 사이트](https://ignite.microsoft.com/)에서 제공 상태를 확인할 수 있습니다.

> **출처**: [What's new in Microsoft Agent 365: Ignite 2026](https://techcommunity.microsoft.com/t5/agent-365-blog/what-s-new-in-microsoft-agent-365-ignite-2026/ba-p/4571753), TechCommunity Agent 365 Blog. 자세한 내용은 원문 참조.
