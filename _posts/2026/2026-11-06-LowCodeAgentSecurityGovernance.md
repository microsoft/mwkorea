---
title: "에이전트 보안, 개발을 막지 않고 지킨다: Microsoft의 17만 개인 개발 환경 운영법"
date: 2026-11-06T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - PowerPlatform
  - Agent
  - Security
  - Governance
  - MicrosoftDigital
  - CustomerZero
excerpt: "Microsoft는 17만 개가 넘는 개인 개발 환경을 기반으로 로우코드 앱과 AI 에이전트의 소유권·연결·공유를 관리하고 있습니다. 개인·샌드박스·프로덕션을 나누는 운영 모델과 커넥터 정책, 탐지·조치 체계를 한국 기업의 도입 관점에서 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트 보안, 개발을 막지 않고 지킨다: Microsoft의 17만 개인 개발 환경 운영법

현업 직원이 Copilot Studio로 에이전트를 만들기 시작하면, IT 부서의 고민도 달라집니다. 개발을 허용할지보다 **누가 소유하고, 어떤 데이터에 연결하며, 누구에게 공유하는지**를 지속적으로 파악하는 일이 중요해집니다. Microsoft 역시 사내 테넌트에 회사 데이터를 다루는 로우코드 에이전트와 각종 리소스가 수십만 개 쌓이면서 같은 문제를 경험했습니다.

Microsoft Inside Track은 2026년 11월 5일 17:00 UTC, 한국 시간으로 11월 6일에 Microsoft Digital과 Office of the CISO의 대응 방식을 소개했습니다. 핵심은 모든 직원을 하나의 공용 개발 공간에 모으는 대신, **명확한 단일 소유자가 있는 개인 개발 환경과 위험도에 따른 운영 단계를 제공하는 것**입니다.

이 글은 새로운 제품의 GA 발표가 아니라 Microsoft의 사내 운영 사례입니다. 소개된 공유 제한과 탐지·정지 절차가 모든 고객 테넌트에 기본 적용된다고 해석해서는 안 됩니다.

---

## 공용 기본 환경이 관리의 사각지대가 된 이유

Power Platform의 기본 환경은 직원들이 쉽게 시작할 수 있는 공간입니다. 하지만 앱·플로·연결이 한곳에 쌓이면 과도하게 공유된 리소스, 담당자가 바뀐 뒤 방치된 워크플로, 관리되지 않는 연결이 늘어날 수 있습니다. **환경에 접근할 수 있다는 것과 모든 업무 데이터에 접근할 권한이 있다는 것은 별개의 문제**지만, 공유와 연결을 잘못 설정하면 의도하지 않은 정보 노출 경로가 생깁니다.

![Microsoft Digital의 수석 아키텍트 Naveen Jangir](/mwkorea/assets/images/2026-11-06-LowCodeAgentSecurityGovernance/image1.png)

Microsoft Digital의 Naveen Jangir는 데이터를 AI로부터 무조건 숨기는 대신, 적절한 접근 제한과 거버넌스를 통해 권한 있는 사람과 AI 기능이 안전하게 사용하도록 해야 한다고 설명합니다.

![Office of the CISO의 Mark Jacobs](/mwkorea/assets/images/2026-11-06-LowCodeAgentSecurityGovernance/image2.png)

이를 시작하는 첫 단계는 **정확하고 최신 상태인 인벤토리**입니다. Office of the CISO의 Mark Jacobs가 강조하듯, 어떤 리소스가 있는지 보이지 않으면 위험한 구성도 찾아낼 수 없습니다.

## 17만 개 이상의 PDE: 실험은 개인 공간에서, 확산은 검토 후에

Microsoft 직원들은 2024년 이후 **17만 개가 넘는 Personal Developer Environment(PDE)**를 만들었습니다. 사내에서는 Copilot Studio, Power Apps, Power Automate를 열면 공용 기본 환경 대신 개인 소유의 PDE로 이동하도록 운영합니다.

개념적으로는 OneDrive처럼 개인 소유가 분명한 작업 공간입니다. 그렇다고 개인 환경이 추가 데이터 권한을 부여하는 것은 아닙니다. 그 안의 앱과 에이전트도 메이커가 이미 가진 권한과 조직 정책 안에서 동작합니다.

![2024년 초부터 17만 개 이상으로 증가한 Microsoft의 Power Platform 개인 개발 환경과 다른 환경 유형의 추이](/mwkorea/assets/images/2026-11-06-LowCodeAgentSecurityGovernance/image4.png)

| 환경 | 주요 용도 | Microsoft 사내 운영의 핵심 |
|---|---|---|
| 개인 개발 환경(PDE) | 개인의 앱·워크플로·에이전트 실험 | 단일 소유자, 제한된 공유, 기존 사용자 권한 유지 |
| 샌드박스 환경 | 팀 단위 공동 개발 | 팀 등록과 취급 데이터 분류, 보안·Responsible AI 검토 |
| 프로덕션 환경 | 전사 사용 솔루션 운영 | 더 넓은 사용자·데이터 영향에 대한 추가 검토와 감독 |

개인 환경의 앱은 제한된 인원에게만 공유할 수 있으며, 더 넓게 확산하려면 프로덕션으로 옮기고 추가 검토를 거치는 방식입니다. 원문은 구체적인 공유 인원 상한을 제시하지 않습니다.

소유권은 수명 주기 관리와도 연결됩니다. 직원이 퇴사하면 관련 환경과 리소스를 식별해 정리하는 절차가 작동합니다. 다만 원문은 모든 리소스가 즉시 자동 삭제된다고 설명하지는 않습니다.

## 보안과 거버넌스를 하나의 운영 모델로 묶기

![Office of the CISO의 보안 운영 담당 Andrew Leeland](/mwkorea/assets/images/2026-11-06-LowCodeAgentSecurityGovernance/image3.png)

Microsoft는 정책 수립과 플랫폼 운영을 분리된 조직의 개별 과제로 두지 않았습니다. Office of the CISO는 허용할 커넥터 등 보안 요구사항을 정하고 위험 활동을 모니터링합니다. Microsoft Digital은 테넌트와 환경 구성, 소유권, 거버넌스 운영을 맡습니다.

개인정보보호·법무·Responsible AI 팀도 각 영역의 요구사항을 정의하며, Microsoft Digital이 이를 적용 가능한 테넌트 통제와 운영 절차로 옮깁니다. Andrew Leeland가 강조한 방향은 문제가 생긴 뒤 대응하는 데 그치지 않고, **만들기 전부터 위험한 구성을 예방하는 것**입니다.

한국 기업에서도 보안팀의 금지 목록과 플랫폼팀의 개발 가이드가 서로 다르면 메이커가 혼란을 겪습니다. 정책 결정자, 실제 적용 담당자, 예외 검토 담당자를 함께 정하는 것이 이 사례에서 얻을 수 있는 운영상의 교훈입니다.

## 커넥터 정책으로 데이터가 이동하는 경로 통제하기

커넥터는 앱이나 에이전트가 메일·파일·데이터베이스 등 다른 서비스에 접근하는 통로입니다. Microsoft는 환경 유형별로 사용할 수 있는 커넥터를 미리 정하고, 새 환경에도 해당 규칙이 자동 적용되도록 운영합니다.

![Microsoft Digital의 Copilot Studio 및 에이전트 확장성 담당 Aisha Hasan](/mwkorea/assets/images/2026-11-06-LowCodeAgentSecurityGovernance/image5.png)

사내 개인 환경에서는 대부분의 Microsoft 커넥터를 사용할 수 있지만 다음 두 조건을 충족해야 합니다.

- **메이커 본인의 회사 계정으로 로그인할 것**
- **회사 데이터를 Microsoft 외부 서비스로 보내지 않을 것**

이것은 Microsoft의 사내 정책을 설명한 것이며, 모든 조직이 그대로 적용해야 하는 제품 사양은 아닙니다. 샌드박스와 프로덕션 환경은 팀과 취급 데이터 유형을 등록하고 더 많은 감독을 받는 대신, 표준 목록에 없는 서비스에 접근하기 위한 사용자 지정 커넥터도 만들 수 있습니다.

새 커넥터가 나오면 Microsoft Digital과 Office of the CISO가 기능을 검토해 전체 메이커에게 허용할지, 더 높은 수준의 통제를 받는 환경에서만 허용할지 결정합니다.

**커넥터가 허용되었다고 모든 데이터 사용이 적절해지는 것은 아닙니다.** 민감한 데이터 처리는 ID·권한, 데이터 거버넌스, 커넥터 제한, 모니터링과 필요한 보안·개인정보·법무·Responsible AI 검토를 함께 충족해야 합니다.

## 사전 통제에 탐지·조치를 더하는 방식

정책만으로 모든 예외를 막을 수는 없습니다. Microsoft 사내에서는 기본 환경에 새 리소스가 만들어지면 Microsoft Sentinel이 이를 탐지하고, 메이커에게 알리며, 적절한 환경으로 이동할 수 있도록 해당 리소스를 정지하는 절차를 운영합니다. 외부 탐지 도구도 추가 신호를 제공합니다.

정책 집행 초기에는 경고가 급증했지만 이후 감소했습니다. 원문에 따르면 대부분의 메이커는 한두 차례 안내를 받은 뒤 처음부터 올바른 환경을 사용하게 되었습니다. 이는 **Microsoft가 구성한 운영 흐름**이지, Sentinel을 켜기만 하면 모든 고객에게 동일하게 작동한다는 의미는 아닙니다.

도입 조직에 필요한 것은 경고 수 자체보다 대응 경로입니다. 누가 알림을 받고, 어떤 환경으로 옮기며, 무엇을 확인한 뒤 다시 운영할지까지 함께 설계해야 합니다.

## 에이전트에는 환경 통제 이상의 보안이 필요하다

![Office of the CISO에서 거버넌스와 위험 관리를 담당하는 Prathiba Enjeti](/mwkorea/assets/images/2026-11-06-LowCodeAgentSecurityGovernance/image6.png)

AI 에이전트는 고정된 로직을 실행하는 앱과 달리 맥락을 해석하고 행동을 동적으로 선택할 수 있습니다. 따라서 허용할 수 없는 행동이 무엇인지 정의하고, 피해가 발생하기 전에 차단할 통제를 마련해야 합니다.

Copilot Studio는 Power Platform의 커넥터 정책을 이어받습니다. 에이전트 역시 생성된 환경에 연결되므로 소유자와 연결 대상을 추적할 수 있습니다. 하지만 이것만으로 충분하지는 않습니다. **에이전트 ID, 권한, 데이터 접근, 실행 중 활동**까지 별도로 살펴야 합니다.

![Office of the CISO의 보안 프로그램 담당 Henry Duncan](/mwkorea/assets/images/2026-11-06-LowCodeAgentSecurityGovernance/image7.png)

Microsoft의 담당팀은 에이전트 구성을 평가하고 정책 위반을 모니터링합니다. Customer Zero로서 Microsoft Defender 제품팀과 매주 만나 발견 사항을 공유하고 새 기능도 시험합니다. 초기 보안 구성을 제대로 하는 기본 원칙과 실행 중의 지속적 검증을 함께 가져가는 접근입니다.

## 한국 조직의 도입 체크포인트

다음은 원문의 운영 원칙을 국내 도입 상황에 맞게 풀어 쓴 제안입니다.

1. **인벤토리부터 만들기**: 앱·플로·에이전트의 환경, 소유자, 연결, 공유 대상과 데이터 위험도를 함께 관리합니다.
2. **개인 실험과 조직 운영을 분리하기**: 개인 공간에서 시작하되 팀·전사 배포로 넘어가는 검토 경로를 명확히 합니다.
3. **기본 환경 이전과 커넥터 제한을 병행하기**: 이전 일정을 안내하면서 제한을 단계적으로 적용해 업무 단절을 줄입니다.
4. **탐지 후 복구 절차까지 설계하기**: 경고·정지뿐 아니라 담당자 통지, 이전, 재검토와 재개 경로를 준비합니다.
5. **에이전트 위험도로 우선순위 정하기**: 민감 데이터나 큰 영향력을 가진 작업에 연결된 에이전트를 먼저 검토합니다.

구현을 살펴보려면 원문이 연결한 [Copilot Agent Kit의 Power Shield 안내](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/kit-power-shield)와 [GitHub의 Power Shield 문서](https://github.com/microsoft/Power-CAT-Copilot-Studio-Kit/blob/main/POWER_SHIELD.md)를 참고할 수 있습니다. 이 글은 해당 도구의 현재 지원 상태나 설치 절차를 별도로 검증한 가이드는 아닙니다.

## 마무리: 개발의 자유를 유지하는 안전한 경로

이 사례의 핵심은 개발 환경의 숫자가 아닙니다. **누가 책임지는지 분명하게 하고, 데이터 이동 경로를 통제하며, 넓게 확산하기 전에 검토하는 구조**를 만들었다는 점입니다.

Microsoft도 일부 제품 기능이 여전히 기본 환경에 의존하며, 에이전트의 진화에 따라 새로운 위험이 생긴다고 설명합니다. 개인 환경은 보안을 완성하는 해법이 아니라 출발점입니다. 환경·커넥터·ID·데이터·런타임을 함께 관리해야 현업의 실험을 안전한 조직 역량으로 확장할 수 있습니다.

> **출처**: [Securing low-code platforms at Microsoft in the age of AI](https://www.microsoft.com/insidetrack/blog/securing-low-code-platforms-at-microsoft-in-the-age-of-ai/) — Microsoft Inside Track, 2026년 11월 5일(UTC). 자세한 내용은 원문 참조.
