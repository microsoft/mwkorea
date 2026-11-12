---
title: "Copilot의 Claude, EU 데이터 경계로 이동…12월 9일 기본 활성화 전 확인할 설정"
date: 2026-11-10T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - Claude
  - Anthropic
  - EUDataBoundary
  - Governance
excerpt: "EU·EFTA의 적격 테넌트에서 Copilot의 Claude 모델 처리가 2026년 12월 초 EU Data Boundary로 이동할 예정입니다. 12월 9일에는 미설정 테넌트의 기본 활성화와 일부 기존 옵션의 폐지가 함께 진행되므로, 유럽 법인을 운영하는 조직은 현재 설정을 확인해야 합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot의 Claude, EU 데이터 경계로 이동…12월 9일 기본 활성화 전 확인할 설정

Copilot에서 어떤 모델을 쓸 수 있는지만큼 중요한 것이 **그 모델의 데이터 처리 위치와 조직의 접근 정책**입니다. Microsoft는 MC1546438을 통해 EU와 EFTA의 적격 테넌트에서 Claude 모델의 처리를 EU Data Boundary 안으로 옮길 계획을 안내했습니다.

이번 변경에는 관리자 설정 변화도 포함됩니다. Anthropic 사용 여부를 아직 선택하지 않은 테넌트는 2026년 12월 9일 모든 사용자에게 Claude가 활성화되고, Microsoft 365 앱에서만 허용하던 기존 옵션도 폐지될 예정입니다.

한국에 본사를 둔 기업이라도 유럽 법인이나 유럽 지역의 별도 테넌트를 운영한다면 살펴볼 만한 공지입니다. 다만 **한국 테넌트 전체에 같은 데이터 경계나 기본 설정이 적용된다는 뜻은 아닙니다.**

---

## 두 가지 변경일을 구분하세요

| 예정 시점 | 변경 내용 |
|---|---|
| 2026년 12월 초 | 적격 테넌트의 Copilot Claude 모델 처리가 EU Data Boundary로 이동 |
| 2026년 12월 9일 | Anthropic 미설정 테넌트에서 기본 활성화, 앱 전용 허용 옵션 폐지 |

원문은 12월 초 이전에는 Claude 모델에 EU Data Boundary 처리 약정이 적용되지 않는다고 명시합니다. 따라서 공지가 나왔다는 이유만으로 이미 처리 위치가 바뀌었다고 판단해서는 안 됩니다.

## 현재 설정에 따라 영향이 달라집니다

| 현재 Anthropic 설정 | 공지에서 안내한 결과 |
|---|---|
| 선택한 적 없음 | 12월 9일 **All users**로 활성화 |
| 이미 Claude 사용 허용 | 기존 사용자·그룹 할당 유지, 제공 시점에 처리 위치 자동 전환 |
| Copilot in Microsoft 365 apps에서만 허용 | 해당 옵션 폐지 후 **All users**로 전환 |
| **No users**로 비활성화 | 기존 선택 유지 |
| **Specific users and groups**로 제한 | 기존 선택 유지 |

특히 앱 전용 허용 옵션을 사용하던 조직은 주의해야 합니다. 사용 범위를 제한하려던 설정이 모든 사용자 허용으로 바뀌므로, 같은 정책 의도를 유지하려면 변경일 전에 **No users** 또는 **Specific users and groups**를 명시적으로 선택해야 합니다.

영향 범위에는 해당 테넌트의 Microsoft Copilot 경험과 Microsoft Copilot Studio에서의 Claude 접근이 포함됩니다.

## 관리자가 확인할 경로와 권한

접근을 차단하거나 제한하려면 12월 9일 전에 다음 경로를 확인합니다.

1. Microsoft 365 admin center에서 **Copilot > Settings > View all**로 이동합니다.
2. **AI providers operating as Microsoft subprocessors > Anthropic**을 엽니다.
3. 전체 차단은 **No users**, 제한 허용은 **Specific users and groups**를 선택합니다.
4. **Save**로 저장합니다.

이 설정을 변경하려면 **AI Administrator 또는 Global Administrator** 역할이 필요합니다. 미설정 상태에서 전체 활성화를 원하는 조직은 별도 조치가 필요 없고, 12월 9일 이후에도 관리자는 비활성화하거나 접근을 제한할 수 있습니다.

## 데이터 경계 변경과 별도로 확인할 사항

Anthropic은 계속 Microsoft의 하위 처리자(subprocessor)로 동작합니다. 원문은 Claude 모델에 Microsoft의 enterprise data protection이 적용되며, Microsoft Learn에 별도 고지된 경우를 제외하고 Product Terms와 Data Protection Addendum이 적용된다고 설명합니다.

다만 **Anthropic models with Data Retention은 별도 설정으로 관리되며 이번 변경에 포함되지 않습니다.** 데이터 경계 이동과 데이터 보존 옵션을 하나의 정책으로 혼동하지 않는 것이 중요합니다.

도입 담당자는 테넌트의 EU Data Boundary 적격 여부, 현재 Anthropic 선택값, 허용 사용자·그룹을 먼저 확인하는 편이 좋습니다. 이후 보안·컴플라이언스 팀과 헬프데스크에 적용 시점과 사용자에게 보일 변화를 공유하세요.

## 마무리

이번 공지의 핵심은 처리 지역의 변화뿐 아니라 **기존 설정을 유지하는 경우와 All users로 전환되는 경우를 구분하는 것**입니다. 유럽 테넌트를 운영한다면 12월 9일 전에 현재 선택값을 점검하고 조직의 모델 사용 정책과 일치시키는 것이 우선입니다.

> 출처: [MC1546438 — Action may be required: Claude models in Copilot are coming into the EU Data Boundary and will be enabled by default](https://mc.merill.net/message/MC1546438)
>
> 참고: [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap) · [Microsoft 공식 발표](https://www.microsoft.com/en-us/copilot/blog/2026/11/05/bringing-claude-models-in-microsoft-copilot-into-the-eu-data-boundary) · [Anthropic 모델 관리 문서](https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-subprocessor)
>
> 이 공개 공지에는 개별 Roadmap ID가 제시되어 있지 않습니다. 일정과 설정 설명은 원문 공지 시점 기준이며, 실제 출시 일정·기능은 변경될 수 있습니다.
