---
title: "Copilot 메모리를 지워도 기록은 남을 수 있습니다: Purview 보존 지원의 의미"
date: 2026-09-25T00:00:00 KST
categories:
  - Copilot
tags:
  - Microsoft365Copilot
  - MicrosoftPurview
  - CopilotMemory
  - Retention
  - eDiscovery
excerpt: "Microsoft Purview가 수정되거나 삭제된 Copilot 메모리의 비활성 버전 보존을 지원합니다. 개인화 해제와 삭제, 보존의 차이부터 Exchange 저장 위치와 eDiscovery 준비사항까지 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot 메모리를 지워도 기록은 남을 수 있습니다: Purview 보존 지원의 의미

Copilot이 사용자 선호와 업무 맥락을 기억하면 매번 같은 설명을 반복하지 않아도 됩니다. 하지만 조직 입장에서는 사용자가 그 기억을 수정하거나 삭제했을 때, 조사에 필요한 이전 기록을 어떻게 관리할지도 생각해야 합니다.

MC1478965는 **Microsoft Purview Data Lifecycle Management가 Copilot 메모리의 비활성 버전을 보존하는 기능**을 도입한다고 알립니다. 개인화 기능을 끄는 것과 데이터를 삭제하는 것, 조직의 보존 정책에 따라 이력을 남기는 것은 서로 다릅니다.

---

## 무엇을 보존하나요?

원문에서 말하는 Copilot 메모리에는 저장된 기억, 채팅 기록에서 추론한 세부정보, 사용자 지정 지침이 포함됩니다. 이번 변화의 초점은 메모리 항목이 수정되거나 삭제될 때 만들어지는 **이전의 비활성 버전**입니다.

조직은 적용되는 보존 설정에 따라 이 버전을 정해진 기간 동안 유지할 수 있습니다. 이를 통해 컴플라이언스 담당자는 메모리 내용이 시간에 따라 어떻게 바뀌었는지 확인할 수 있습니다. 모든 조직의 메모리가 동일한 기간 동안 무조건 보존된다는 발표는 아닙니다.

## 저장 위치와 조사 방법

메모리 항목은 사용자의 **Exchange 사서함 내 숨겨진 폴더**에 저장되며, 사서함에 적용되는 보안 보호를 상속합니다. 보존되는 비활성 버전도 사용자의 Exchange 사서함에 유지됩니다.

권한이 있는 관리자는 **Microsoft Purview eDiscovery**로 Copilot 개인화 및 메모리 항목을 검색하고 조사할 수 있습니다. 따라서 도입 대상은 Copilot 관리자뿐 아니라 법무·개인정보·보안·기록 관리·eDiscovery 담당자까지 포함합니다.

## 개인화 해제와 삭제는 같지 않습니다

| 사용자 또는 조직의 동작 | 원문이 설명하는 의미 |
|---|---|
| 향상된 개인화 또는 저장된 메모리 끄기 | Copilot이 해당 메모리를 사용하는 것을 막지만, 이미 저장된 메모리를 자동 삭제하지는 않음 |
| 저장된 메모리를 명시적으로 삭제 | 사용자에게 활성 상태로 남는 메모리를 삭제하는 동작 |
| 조직의 보존 설정 적용 | 수정·삭제된 항목의 과거 버전이 설정에 따라 남을 수 있음 |

원문은 이번 업데이트 이전에는 Purview 보존 정책과 보존 레이블이 Copilot 메모리에 적용되지 않는다고 설명합니다. 다만 이 공지는 새 기능의 구체적인 설정 화면이나 모든 정책 조합을 제시하지 않으므로, 기존 사서함 설정만으로 원하는 보존이 구현되었다고 단정하지 말아야 합니다.

## 일정과 도입 준비

글로벌 배포는 **2026년 9월 말 시작, 10월 중순 완료 예정**입니다. 배포 전에 즉시 수행해야 하는 필수 작업은 없지만, 다음 준비를 권고합니다.

1. 법무·개인정보·보안·기록 관리 부서와 메모리 보존 목적 및 기간을 결정합니다.
2. Purview 역할과 eDiscovery 조사 권한을 검토합니다.
3. 내부 조사, 사고 대응, 정보주체 요청 절차에 메모리 이력 보존을 반영합니다.
4. 제공 후 소수 테스트 사용자로 수정·삭제·보존·검색 동작을 검증합니다.

## 사용자 안내 문구도 바꿔야 합니다

실무적으로는 “개인화를 끄면 기존 기억도 모두 지워진다”는 오해를 없애는 것이 중요합니다. 삭제 후에도 조직의 보존 설정에 따라 역사적 버전이 남을 수 있다는 점을 도움말과 지원 절차에 명확히 설명하세요.

> 출처: [MC1478965 — Microsoft Purview: Data Lifecycle Management – Retention for Copilot Memory](https://mc.merill.net/message/MC1478965)  
> [Microsoft 365 Roadmap ID 569612](https://www.microsoft.com/en-us/microsoft-365/roadmap?filters=&searchterms=569612)  
> 실제 출시 일정·기능은 변경될 수 있습니다.
