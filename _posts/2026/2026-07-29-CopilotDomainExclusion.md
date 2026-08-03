---
title: "Copilot이 참고하면 안 되는 사이트, 이제 관리자가 정한다 — Domain Exclusion"
date: 2026-07-29T00:00:00 KST
categories:
  - Copilot
tags:
  - M365Copilot
  - CopilotChat
  - WebGrounding
  - DomainExclusion
  - Governance
  - Compliance
  - PowerShell
excerpt: "Microsoft 365 Copilot의 웹 그라운딩에서 특정 도메인을 제외할 수 있는 Domain Exclusion이 공개되었습니다. 웹 검색을 통째로 끄지 않고도 조직 정책에 맞지 않는 외부 사이트만 골라낼 수 있으며, 최대 1,000개 도메인까지 PowerShell 스크립트로 설정합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Copilot이 참고하면 안 되는 사이트, 이제 관리자가 정한다 — Domain Exclusion

![Domain Exclusion for Microsoft 365 Copilot](/mwkorea/assets/images/2026-07-29-CopilotDomainExclusion/image1.png)

Microsoft 365 Copilot을 도입한 조직에서 관리자들이 자주 던지는 질문이 있습니다. **"Copilot이 웹에서 정보를 가져오는 건 좋은데, 아무 사이트나 참고해도 되는 건가요?"**

지금까지 선택지는 사실상 두 가지였습니다. 웹 검색(웹 그라운딩)을 **켜거나**, **끄거나**. 켜면 최신 정보를 활용할 수 있지만 어떤 외부 사이트가 답변 근거로 쓰이는지 통제하기 어려웠고, 끄면 Copilot의 활용도가 크게 떨어졌습니다. 그 중간이 없었던 셈입니다.

이번에 발표된 **Domain Exclusion for Microsoft 365 Copilot**은 바로 그 중간 지점을 채웁니다. 웹 검색 자체는 유지하면서, **조직이 원하지 않는 특정 도메인만 그라운딩 대상에서 제외**할 수 있게 하는 기능입니다.

---

## Domain Exclusion이란

Domain Exclusion은 관리자가 **Copilot 웹 그라운딩에서 제외할 도메인 목록**을 정의할 수 있게 해 주는 기능입니다. 한 번 설정하면, 해당 도메인은 웹 그라운딩을 사용하는 Copilot 응답에서 근거로 활용되지 않습니다.

핵심 사양을 정리하면 다음과 같습니다.

| 항목 | 내용 |
|------|------|
| 적용 범위 | Microsoft 365 Copilot 및 Copilot Chat의 웹 그라운딩 시나리오 |
| 최대 도메인 수 | **1,000개** |
| 기본 설정 | **기본 비활성화** — 관리자가 직접 구성해야 동작 |
| 설정 방법 | 제공되는 **PowerShell 스크립트** |
| 필요 권한 | **Search Administrator** 또는 **Global Administrator** |

기본값이 꺼져 있다는 점이 중요합니다. 조직의 거버넌스 요구사항에 따라 **필요한 곳만 선택적으로 도입**할 수 있도록 설계되었습니다.

---

## 왜 필요한가

웹 그라운딩은 Copilot이 최신 정보를 반영해 더 시의적절한 답변을 만들도록 돕습니다. 문제는 "웹 전체"가 대상이라는 점입니다. 원문에서는 Domain Exclusion이 특히 유용한 상황으로 다음을 언급합니다.

- **엄격한 컴플라이언스 의무**가 있는 조직
- **브랜드 안전성(brand safety)** 요구사항이 있는 경우
- **지역별 콘텐츠 고려사항**이 있는 경우
- 승인된 소스만 사용하도록 하는 **내부 정책**이 있는 경우

예를 들어 금융·의료·공공처럼 규제가 강한 산업에서는 "출처가 어디였는가"가 답변 품질만큼이나 중요합니다. 경쟁사 사이트나 신뢰도가 낮은 콘텐츠 사이트가 사내 Copilot 답변의 근거로 등장하는 상황을 원하지 않는 조직도 많습니다.

Domain Exclusion은 **"웹 검색 전면 허용"과 "웹 검색 전면 차단" 사이에 놓이는 정밀한 통제 수단**입니다. 가치 있는 영역에서는 웹 기반 답변을 계속 활용하면서, 우리 환경에 적절하지 않은 도메인만 걸러낼 수 있습니다.

---

## 사용자에게는 어떻게 보이나

사용자 입장에서 별도의 조작은 없습니다. 다만 답변 하단의 정보 아이콘(Sources 영역)에서 **관리자 정책이 일부 소스를 제한할 수 있다는 안내**를 확인할 수 있습니다.

![관리자 정책으로 특정 소스가 제한될 수 있음을 안내하는 정보 팁](/mwkorea/assets/images/2026-07-29-CopilotDomainExclusion/image2.png)

같은 안내 문구에는 웹 검색 쿼리가 **익명화되어 별도로 처리**되며, 응답에서 **24시간 후 제거**된다는 내용도 함께 담겨 있습니다. 즉 Domain Exclusion은 기존 웹 검색 프라이버시 처리 위에 **소스 통제 계층을 하나 더 얹는** 구조입니다.

---

## 관리자 설정 절차

설정은 Microsoft가 제공하는 **Configure Tenant Domain Exclusions PowerShell 스크립트**로 진행합니다. 이 스크립트는 다음 작업을 지원합니다.

- CSV 파일을 이용해 **새 제외 목록 생성**
- 기존 구성 **업데이트**
- 현재 구성 **내보내기(export)**
- 구성 **삭제**
- **템플릿 CSV 파일 생성**

원문이 권장하는 진행 순서는 다음과 같습니다.

1. **제외할 도메인 정리** — 조직이 Copilot 웹 그라운딩에서 빼고 싶은 도메인을 검토합니다.
2. **CSV 파일 준비** — 필요한 도메인 정보를 담은 CSV를 만듭니다. 템플릿 생성 기능을 활용하면 편리합니다.
3. **스크립트 실행** — Search Administrator 또는 Global Administrator 권한으로 PowerShell 스크립트를 실행합니다.
4. **검증 및 유지관리** — 구성이 의도대로 반영되었는지 확인하고, 조직 정책이 바뀌면 목록을 갱신합니다.

관련 리소스는 다음과 같습니다.

- 문서: [aka.ms/copilot/DomainExclusion](https://aka.ms/copilot/DomainExclusion)
- 스크립트: [aka.ms/Copilot/DomainExclusionScript](https://aka.ms/Copilot/DomainExclusionScript)
- 웹 검색 데이터·프라이버시·보안: [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access)
- 사용자용 안내: [How web search works in Microsoft 365 Copilot Chat and agents](https://support.microsoft.com/en-us/microsoft-365-copilot/how-web-search-works-in-microsoft-365-copilot-chat-and-agents)

---

## 도입 담당자를 위한 체크포인트

**1. 제외 목록은 "정책 문서"로 관리하세요**
1,000개까지 등록할 수 있지만, 목록이 커질수록 왜 제외했는지 근거를 추적하기 어려워집니다. 도메인별로 제외 사유(컴플라이언스·브랜드·지역 규정 등)를 함께 기록해 두면 나중에 감사·검토 대응이 훨씬 수월합니다.

**2. 제외는 "차단"이 아니라 "그라운딩 배제"입니다**
Domain Exclusion은 Copilot이 응답 근거로 해당 도메인을 쓰지 않도록 하는 기능입니다. 네트워크 차단이나 웹 필터링과는 성격이 다릅니다. 사용자가 브라우저로 해당 사이트에 접속하는 것과는 별개의 통제 수단이라는 점을 관계 부서에 명확히 설명하세요.

**3. 기본 비활성화라는 점을 잊지 마세요**
설정하지 않으면 아무 변화가 없습니다. 반대로 말하면, "우리는 도메인 제외 정책이 있다"고 문서에만 적어 두고 실제 구성은 하지 않은 상태가 생길 수 있습니다. 구성 후 **export 기능으로 현재 상태를 주기적으로 확인**하는 절차를 운영에 포함하는 것을 권합니다.

**4. 사용자 커뮤니케이션을 준비하세요**
정보 팁에 "Admin policy may restrict certain sources"가 표시되므로, 사용자가 "왜 이런 문구가 뜨나요?"라고 문의할 수 있습니다. 헬프데스크에 배경을 미리 공유해 두면 불필요한 문의를 줄일 수 있습니다.

**5. 권한 분리를 검토하세요**
설정에 Global Administrator까지 필요하지 않습니다. **Search Administrator** 역할로도 가능하므로, 최소 권한 원칙에 맞춰 담당자를 지정하는 편이 안전합니다.

---

## 마무리

AI 거버넌스 논의는 흔히 "쓸 것인가, 막을 것인가"의 이분법으로 흐르기 쉽습니다. 하지만 실제 조직에 필요한 것은 **켜고 끄는 스위치가 아니라 조절 가능한 다이얼**입니다.

Domain Exclusion은 그런 다이얼을 하나 더 제공합니다. 웹 그라운딩의 생산성 이점은 유지하면서, 조직의 정책·규제·리스크 성향에 맞게 외부 소스의 영향 범위를 좁힐 수 있습니다.

Copilot을 업무 핵심 워크플로에 넣으려는 단계에 있다면, 이번 기능은 보안·법무 부서를 설득하는 실질적인 근거가 되어 줄 것입니다.

---

> **출처**: *More control over web grounding with Domain Exclusion for Microsoft 365 Copilot* — Microsoft Tech Community, Microsoft 365 Copilot Blog
> - 원문: [https://techcommunity.microsoft.com/t5/microsoft-365-copilot-blog/more-control-over-web-grounding-with-domain-exclusion-for/ba-p/4540151](https://techcommunity.microsoft.com/t5/microsoft-365-copilot-blog/more-control-over-web-grounding-with-domain-exclusion-for/ba-p/4540151)
>
> 자세한 내용은 원문 참조.
