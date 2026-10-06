---
title: "Copilot Studio 에이전트, Microsoft Entra Agent ID로 마이그레이션하기"
date: 2026-09-25T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - EntraID
  - AgentID
  - Governance
  - ConditionalAccess
excerpt: "2026년 5월 이전에 만든 Copilot Studio 에이전트는 여전히 레거시 앱 등록 자격 증명을 쓰고 있을 수 있습니다. Microsoft Entra Agent ID로의 자동·자율 마이그레이션이 진행 중이며, Power Platform Advisor에서 직접 마이그레이션하는 절차를 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot Studio 에이전트, Microsoft Entra Agent ID로 마이그레이션하기

Copilot Studio로 만든 에이전트가 많아질수록, "이 에이전트가 정확히 무엇에 접근할 수 있는가"를 파악하고 통제하는 일이 중요해집니다. Microsoft는 2026년 8월 24일부터 **Microsoft Entra Agent ID로의 자율 서비스(self-service) 마이그레이션**을 단계적으로 시작했고, 9월부터는 **Entra Agent ID가 없는 에이전트에 대한 자동 마이그레이션**도 함께 시작했습니다.

---

## 배경 — 레거시 자격 증명이 남아있는 이유

**2026년 5월 이전에 생성된 Copilot Studio 에이전트**는 여전히 레거시 앱 등록(app-registration) 자격 증명을 사용하고 있을 수 있습니다. Microsoft는 아직 마이그레이션되지 않은 에이전트가 남아 있다면 Microsoft Entra Agent ID로 옮길 것을 권장합니다.

## 마이그레이션이 가져다주는 혜택

Microsoft Entra Agent ID로 통합하면 다음과 같은 이점이 있습니다.

- **Microsoft Entra ID 감사 로깅(audit logging)**
- **에이전트 생명주기 관리(lifecycle management)**
- **[Entra ID Governance](https://aka.ms/17699/1)**와의 통합
- 커넥터 권한을 에이전트 ID상의 API 권한으로 가시화 — Entra·Microsoft 365 관리자가 Power Platform 관리센터를 열지 않고도 에이전트가 무엇을 할 수 있는지 확인 가능
- **조건부 액세스(Conditional Access) 정책**(네트워크 위치, 디바이스 준수 상태, 위험 조건 등)으로 해당 커넥터 권한을 타겟팅하는 기능

## 마이그레이션 절차 (Power Platform Advisor 권장 사항 기준)

1. 테넌트에 **Power Platform 인벤토리(inventory)**가 활성화되어 있는지 확인합니다.
2. Power Platform 관리센터에서 **Actions > [Recommendations](https://aka.ms/17699/2) > Active**로 이동해, "Migrate Copilot Studio agents to Microsoft Entra Agent ID for enhanced agent governance" 권장 사항을 엽니다.
3. 권장 사항 패널에서 **Why is this important?**를 펼쳐 마이그레이션 가이드를 검토합니다.
4. 마이그레이션 대상 에이전트 목록을 검토합니다. **Suggested migration order**와 **Migration notes**를 참고해 초기 파일럿이나 다음 마이그레이션 배치를 선정합니다. 표에는 환경, 환경 유형, 소유자, 최근 활동, 인증 방식 등이 함께 표시됩니다.
5. 마이그레이션할 각 에이전트 옆 체크박스를 선택합니다(단일 또는 다수 선택 가능). **Migrate** 버튼이 활성화되고, 선택된 에이전트 수가 액션 바에 표시됩니다.
6. **Migrate**를 선택하고 확인 화면을 검토한 뒤 마이그레이션을 확정합니다. 비핵심(noncritical) 에이전트의 소규모 배치부터 시작하는 것을 권장합니다.
7. 선택한 각 에이전트의 **Action, Action state, Action date** 열을 검토합니다. 모든 권장 사항에 걸친 조치 이력을 확인하려면 **Action history** 탭을 사용합니다.
8. 에이전트를 소유한 메이커와 검증 일정을 조율합니다.
9. 마이그레이션 이후, 다음 배치를 진행하기 전에 각 에이전트의 채널·인증·액션·커넥터·플로우·통합을 검증합니다.
10. Microsoft Entra 로그인 로그와 해당되는 조건부 액세스 결과를 검토합니다. 에이전트가 검증을 통과하지 못하면 다음 단계를 진행하기 전에 되돌립니다(revert).

## 조치 필요 여부

이 메시지는 공지용이며 별도 조치는 필요하지 않습니다. 다만 Microsoft는 남은 적격 에이전트를 식별하고 마이그레이션할 것을 권장합니다. 자세한 내용은 [Migrate Copilot Studio agents to Microsoft Entra Agent ID](https://aka.ms/17699/3) 문서를 참고하세요.

## 한국 조직을 위한 체크포인트

- 2026년 5월 이전부터 Copilot Studio를 운영해온 조직이라면, 레거시 앱 등록 자격 증명을 쓰는 에이전트가 다수 남아 있을 가능성이 높습니다. Advisor 권장 사항으로 현황을 먼저 파악하는 것이 출발점입니다.
- 조건부 액세스 정책을 에이전트 단위로 적용할 수 있다는 점은, 제로 트러스트 보안 모델을 운영하는 한국 기업의 보안 거버넌스 요구사항과 잘 맞습니다.
- 마이그레이션 후 채널·인증·커넥터·플로우를 검증하는 절차를 생략하지 말고, 비핵심 에이전트부터 소규모 배치로 검증해 가며 단계적으로 확대하는 접근이 안전합니다.

---

> **원문**: Migrate Copilot Studio agents to Microsoft Entra Agent ID (MC1478488) — [mc.merill.net에서 보기](https://mc.merill.net/message/MC1478488) | [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap)
>
> 실제 출시 일정·기능은 변경될 수 있습니다.
