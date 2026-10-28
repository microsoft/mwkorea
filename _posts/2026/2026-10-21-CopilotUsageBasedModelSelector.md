---
title: "Copilot 모델 선택기에 사용량 기반 모델 추가: 라이선스 다음은 크레딧 관리입니다"
date: 2026-10-21T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - UsageBasedBilling
  - CopilotCredits
  - Governance
excerpt: "Microsoft는 Copilot Chat과 Word·Excel·PowerPoint의 모델 선택기에 사용량 기반 과금 모델을 추가한다고 안내했습니다. Microsoft 365 Copilot 라이선스뿐 아니라 UBB 활성화와 크레딧 할당이 필요하며, 2026년 11월 순차 배포 예정입니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 모델 선택기에 사용량 기반 모델 추가: 라이선스 다음은 크레딧 관리입니다

Microsoft 365 Copilot에서 어떤 모델을 사용할지 결정하는 일이 비용 관리와 더 직접적으로 연결됩니다. 2026년 10월 21일 공지 MC1519122는 사용량 기반 과금인 **UBB(usage-based billing)** 모델이 Copilot 앱의 Chat과 Word·Excel·PowerPoint의 Copilot 모델 선택기에 제공될 예정이라고 설명합니다.

이 글은 해당 공지 시점의 계획을 정리한 것입니다. 원문은 GPT-6 Astra와 Claude Fable 5.1을 이번 배포의 UBB 모델로 명시하지만, 모든 Copilot 사용자에게 별도 설정 없이 제공된다는 뜻은 아닙니다.

---

## 어디에서 무엇이 달라지나요?

UBB를 활성화하고 크레딧을 할당받은 사용자는 Copilot Chat 및 Word·Excel·PowerPoint에서 해당 모델을 선택할 수 있게 됩니다. 원문에 명시된 대상 플랫폼은 Desktop과 Web이며, 배포 범위는 Worldwide입니다.

![Copilot의 사용량 기반 모델 선택 관련 원문 화면](/mwkorea/assets/images/2026-10-21-CopilotUsageBasedModelSelector/image1.png)

일반 제공(GA) 배포는 **2026년 11월 초 시작, 11월 중순 완료 예정**입니다. 추가 크레딧을 사용자 스스로 관리자에게 요청하는 기능은 초기 배포 이후 제공할 계획으로, 첫 배포에 포함된 기능과 구분해야 합니다.

## 접근 조건은 세 가지입니다

| 조건 | 관리자가 확인할 내용 |
|---|---|
| 라이선스 | 사용자에게 Microsoft 365 Copilot USL이 할당되어 있는가 |
| 과금 설정 | 해당 사용자에게 UBB가 활성화되어 있는가 |
| 사용 예산 | 사용할 Copilot Credits가 할당되어 있는가 |

**Copilot 라이선스 보유만으로 UBB 모델 접근이 보장되지는 않습니다.** 원문은 기존에 안내된 모델별 자격 요건도 계속 적용된다고 설명합니다.

## 도입 전 비용과 데이터 정책을 함께 점검하세요

관리자는 Microsoft 365 관리 센터의 Agent 365 비용 관리와 연계해 예상 사용량과 크레딧 할당을 검토해야 합니다. 크레딧 소진 후 추가 요청을 어떤 절차로 처리할지도 미리 알리는 것이 좋습니다.

이 모델들은 기존 권한과 구성에 따라 사용자 프롬프트와 Copilot이 접근할 수 있는 Microsoft 365 데이터를 처리합니다. 모델 선택이 데이터 권한을 새로 부여하는 것은 아닙니다. 공지는 Entra ID 그룹으로 접근 범위를 지정할 수 있는지까지는 확정하지 않으므로, 그룹 기반 배포를 전제로 설계하지 않는 편이 안전합니다.

구체적인 구성은 [USL과 UBB 설명](https://learn.microsoft.com/en-us/microsoft-365/copilot/user-subscription-license-usage-based-billing), [Copilot Credits 설정](https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-copilot-credits-setup), [크레딧 관리](https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-manage-copilot-credits)를 확인하세요. 이 글에서 최신 문서의 변경 사항을 별도로 검증한 것은 아니며, 배포 시점의 실제 설정을 우선해야 합니다.

## 마무리

한국 기업의 도입 담당자에게 중요한 변화는 모델 종류의 증가만이 아닙니다. **누가 고급 모델을 선택할 수 있고, 얼마만큼 사용할 수 있는지**를 라이선스·접근 제어·예산의 세 축으로 관리해야 한다는 점입니다.

> **출처**: [MC1519122 — Microsoft Copilot: UBB models in Chat and Word, Excel, and PowerPoint via the model selector](https://mc.merill.net/message/MC1519122) · [Microsoft 365 Roadmap 571400](https://www.microsoft.com/microsoft-365/roadmap?id=571400). 실제 출시 일정·기능은 변경될 수 있습니다.
