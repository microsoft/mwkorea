---
title: "Microsoft 365 Copilot 도메인 제외(Domain Exclusion) 기능, 일시 롤백됐습니다"
date: 2026-08-04T00:00:00 KST
categories:
  - Copilot
tags:
  - M365Copilot
  - DomainExclusion
  - WebGrounding
  - Governance
  - Admin
excerpt: "웹 그라운딩 시 특정 도메인을 제외할 수 있게 해 주던 Microsoft 365 Copilot의 Domain Exclusion 기능이 롤백됐습니다. Microsoft는 기능의 중요성을 인지하고 다음 단계를 검토 중이라고 밝혔습니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# Microsoft 365 Copilot 도메인 제외(Domain Exclusion) 기능, 일시 롤백됐습니다

Microsoft 365 Copilot이 웹에서 정보를 가져와 답변에 활용하는 **웹 그라운딩(web grounding)**은 편리하지만, 관리자 입장에서는 통제하고 싶은 영역이기도 합니다. "이 사이트의 내용은 참조하지 않았으면 좋겠다"는 요구가 조직마다 있기 때문입니다.

Microsoft는 이런 요구에 대응해 **Domain Exclusion(도메인 제외)** 기능을 공개했습니다. 관리자가 특정 도메인을 지정하면 Copilot이 웹 그라운딩 시 해당 도메인을 참조하지 않도록 하는 기능입니다.

그런데 Microsoft 365 Copilot 블로그에 후속 공지가 올라왔습니다. **이 기능이 현재 롤백(rollback)되었다**는 내용입니다.

![Domain Exclusion for Microsoft 365 Copilot 업데이트 공지](/mwkorea/assets/images/2026-08-04-DomainExclusionRollback/image1.png)

---

## 공지 내용 요약

Microsoft가 커뮤니티에 전한 내용은 간결합니다.

- 앞서 [*More control over web grounding with Domain Exclusion for Microsoft 365 Copilot*](https://techcommunity.microsoft.com/blog/Microsoft365CopilotBlog/more-control-over-web-grounding-with-domain-exclusion-for-microsoft-365-copilot/4540151) 글에서 소개한 **Domain Exclusion 기능이 현재 롤백되었습니다.**
- Microsoft는 **이 기능의 중요성을 인지하고 있으며, 다음 단계를 적극적으로 검토(actively evaluating next steps) 중**이라고 밝혔습니다.
- 추가 정보가 확보되는 대로 커뮤니티에 업데이트를 공유하겠다고 했습니다.

원문 공지에는 롤백 사유나 재출시 일정에 대한 구체적인 언급은 없습니다. 확인되지 않은 배경을 추측하기보다, **"현재는 사용할 수 없으며 후속 공지를 기다려야 하는 상태"**로 이해하시는 것이 정확합니다.

---

## Domain Exclusion이란 무엇이었나

원래 이 기능은 웹 그라운딩에 대한 관리자 통제권을 넓히는 방향의 기능이었습니다. Copilot이 답변을 구성할 때 웹 검색 결과를 근거로 삼는데, 조직이 원하지 않는 특정 도메인을 그 근거 대상에서 빼는 것이 목적이었습니다.

관리자 입장에서 이런 통제가 필요한 이유는 다양합니다.

- 신뢰도가 낮다고 판단한 정보원 배제
- 업계·업종 특성상 참조가 부적절한 사이트 배제
- 사내 정책상 언급을 피하고자 하는 외부 사이트 관리

즉 **Copilot의 답변 품질을 조직이 직접 손볼 수 있는 몇 안 되는 지렛대** 중 하나였기에, 도입을 준비하던 조직에는 관심이 큰 기능이었습니다.

---

## 한국 고객이 지금 해야 할 일

### 1. 도입 계획에서 일단 제외

Domain Exclusion을 전제로 잡아 둔 거버넌스 설계나 배포 일정이 있다면, **해당 항목을 계획에서 분리**해 두시기 바랍니다. 재출시 시점이 공지되지 않았기 때문에 일정 의존성을 두는 것은 위험합니다.

### 2. 이미 설정해 둔 값이 있는지 점검

기능이 짧게라도 노출된 기간에 도메인 제외 목록을 설정해 두었다면, 현재는 그 설정이 적용되지 않는 상태로 보셔야 합니다. **"설정해 뒀으니 차단되고 있을 것"이라는 전제로 운영하지 않도록** 관련 담당자에게 공유해 주세요.

### 3. 대체 통제 수단 재확인

웹 그라운딩 자체에 대한 통제가 필요하다면, 조직 정책 수준에서 웹 검색 사용 여부를 관리하는 기존 방식이 여전히 대안입니다. 도메인 단위의 세밀한 제어는 당분간 어렵다는 점을 감안해 정책을 다시 정리해 두시길 권합니다.

### 4. 후속 공지 모니터링

Microsoft가 "추가 업데이트를 공유하겠다"고 명시했으므로, Microsoft 365 Copilot 블로그와 메시지 센터를 함께 모니터링하시면 됩니다.

---

## 마무리

기능이 롤백되었다는 소식은 반가운 소식은 아닙니다. 다만 Microsoft가 이를 조용히 넘기지 않고 별도 공지로 알렸다는 점, 그리고 기능의 중요성을 인정하며 다음 단계를 검토 중이라고 밝힌 점은 짚어 둘 만합니다.

Copilot 거버넌스를 준비 중인 조직이라면, **"아직 제공되지 않는 통제 기능"과 "지금 쓸 수 있는 통제 기능"을 구분해 관리하는 습관**이 중요합니다. 이번 사례는 그 필요성을 다시 보여 준 셈입니다.

---

> **출처**: [*Update: Domain Exclusion for Microsoft 365 Copilot*](https://techcommunity.microsoft.com/t5/microsoft-365-copilot-blog/update-domain-exclusion-for-microsoft-365-copilot/ba-p/4543648) (Microsoft Tech Community, Microsoft 365 Copilot Blog)
>
> 자세한 내용은 원문 참조.
