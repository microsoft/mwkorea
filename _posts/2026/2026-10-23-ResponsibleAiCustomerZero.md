---
title: "에이전트가 늘어날수록 거버넌스도 확장해야 합니다: Microsoft Customer Zero의 책임 있는 AI"
date: 2026-10-23T00:00:00 KST
categories:
  - Copilot
tags:
  - ResponsibleAI
  - CustomerZero
  - Agent
  - Governance
  - AzureOpenAI
  - MicrosoftDigital
excerpt: "Microsoft가 공급망·법무·고객 지원에서 AI를 확장하며 배운 책임 있는 AI 운영 원칙을 공개했습니다. 2,000건 이상의 내부 도구 검토 경험을 바탕으로 에이전트의 범위 제한, 검증 가능한 근거, 지속적인 운영 통제를 어떻게 설계하는지 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트가 늘어날수록 거버넌스도 확장해야 합니다: Microsoft Customer Zero의 책임 있는 AI

Copilot과 에이전트의 시범 도입이 성공하면 다음 질문이 찾아옵니다. 여러 부서가 각자의 에이전트를 만들기 시작할 때, 안전성과 책임을 유지하면서 어떻게 조직 전체로 확장할 수 있을까요?

Microsoft Inside Track은 **Customer Zero**, 즉 Microsoft가 자사 기술을 먼저 사용하고 배운 점을 제품 조직에 되돌려 주는 과정에서 얻은 운영 경험을 소개했습니다. 핵심은 책임 있는 AI(Responsible AI, RAI)를 마지막에 통과하는 심사로만 보지 않고, **안전하게 확장하기 위한 설계·운영 체계**로 다루는 것입니다.

이 글은 2026년 10월 22일 16:00 UTC에 게시된 원문을 한국 시간인 **10월 23일** 기준으로 정리합니다. 공급망·법무·고객 지원의 내부 사례이며, 별도 제품의 신규 기능 출시나 모든 고객에게 동일한 성과를 보장하는 발표는 아닙니다.

---

## 2,000건 이상의 검토를 일관된 운영으로 연결하기

Microsoft의 Office of Responsible AI는 표준화된 정책과 절차를 만들고 적용합니다. 개별 팀이 매번 다른 방식으로 심사받기보다, 공통 기준과 과거 사례를 활용해 일관성 있게 검토하는 접근입니다.

원문에 따르면 EMEA의 RAI 리더인 **Alberto Carrozzo**와 팀은 지금까지 **2,000건 이상의 내부 도구 검토**를 마쳤고, 추가로 수천 건의 검토 대상을 다루기 위해 그 경험을 활용하고 있습니다. 이 수치는 승인된 에이전트 수나 전사 전체 에이전트 수가 아니라 해당 팀의 내부 도구 검토 실적입니다.

![Microsoft EMEA에서 책임 있는 AI 운영 경험을 설명한 Alberto Carrozzo](/mwkorea/assets/images/2026-10-23-ResponsibleAiCustomerZero/image1.png)

처음부터 책임 있는 AI, 개인정보 보호, 보안을 설계에 반영하면 뒤늦게 구조를 바꾸는 부담을 줄일 수 있다는 것이 팀의 설명입니다. 과거 검토에서 반복된 패턴은 새 검토 중 더 면밀히 살펴야 할 위험을 찾는 데도 쓰입니다.

[Microsoft의 책임 있는 AI 안내](https://www.microsoft.com/en-us/ai/responsible-ai)에서는 관련 도구·관행·정책을 확인할 수 있습니다.

![원문에서 책임 있는 AI 안내와 함께 사용한 일러스트](/mwkorea/assets/images/2026-10-23-ResponsibleAiCustomerZero/image2.png)

## 공급망: 더 많은 기능보다 명확한 업무 경계

Microsoft의 클라우드 공급망 조직은 최근 수년간 **업무 규모가 5배**로 늘었지만 인력은 같은 수준을 유지했다고 설명합니다. 이 조직은 서비스에 필요한 하드웨어의 조달·공급·유지보수·최종 폐기까지 담당하며, 현재 **100개 이상의 엔터프라이즈급 AI 에이전트**를 운영 환경에서 사용하고 있습니다.

여러 사람이 며칠씩 모으던 분석을 자동으로 준비하고 계속 갱신해, 계획 담당자가 최신 자료를 출발점으로 판단할 수 있게 되었습니다. 다만 이를 모든 공급망 업무의 처리 시간이나 인력 절감률로 일반화해서는 안 됩니다.

![Cloud Supply Chain의 에이전트 업무 범위 제한을 설명한 Jeevan Pathuri](/mwkorea/assets/images/2026-10-23-ResponsibleAiCustomerZero/image3.png)

확산 과정에서 드러난 문제는 **기반 모델의 일반 능력이 업무용 에이전트에 필요 이상으로 노출될 수 있다**는 점입니다. 예를 들어 계획 수립용 에이전트가 업무와 무관한 날씨 질문까지 처리한다면, 목적 밖의 행동 가능성도 커집니다.

이 팀은 내부 책임 있는 AI 절차에서 **OneRAI**를 활용해 AI 기능을 등록하고, 모델과 평가를 문서화하며, 승인을 추적합니다. **Red Team Agent**로 정해진 업무 경계를 벗어나는 동작도 시험합니다.

여기서 배울 점은 “에이전트가 무엇을 할 수 있는가”뿐 아니라 **무엇을 하지 않아야 하는가**도 먼저 정의해야 한다는 것입니다. 추천은 의사결정의 입력이며, 결과에 대한 책임은 사용하는 사람에게 남습니다. OneRAI와 이 내부 구성 요소를 고객이 즉시 사용할 수 있는 공개 제품으로 해석해서는 안 됩니다.

## 법무: 결론마다 확인 가능한 근거를 남기기

Microsoft의 Corporate, External and Legal Affairs(CELA) 부서는 소송과 규제 조사에 필요한 대량의 문서를 검토합니다. 검색과 머신러닝으로 대상을 줄인 뒤에도 변호사가 문서 수만 건을 개별적으로 읽어야 하는 상황이 생깁니다.

생성형 AI는 사건별 지침에 따라 문서를 분류·요약하고, 각 판단의 이유를 기록하는 데 쓰일 수 있습니다. 하지만 민감한 법무 업무에서는 답변만으로 충분하지 않습니다. 담당자가 **원문과 연결해 결론을 검증**할 수 있어야 합니다.

![CELA의 검증 가능한 AI 문서 검토 원칙을 설명한 EJ Bastien](/mwkorea/assets/images/2026-10-23-ResponsibleAiCustomerZero/image4.png)

원문에서 소개한 시스템의 특징은 다음과 같습니다.

- **Azure와 Azure OpenAI 기반의 내부 구성**으로 문서를 처리합니다.
- 광범위한 검색 대신 **선별된 문서 집합** 안에서 에이전트가 동작하도록 제한합니다.
- 문서의 관련성 등 판단에 대해 **기록된 설명과 출처**를 남깁니다.
- 변호사가 근거 자료와 해석을 확인한 뒤 법적 판단을 내립니다.

출처 표시는 단순히 답변의 신뢰감을 높이는 장식이 아닙니다. 내용을 검증하고, 추가로 보존·수집해야 할 저장소를 발견하는 데에도 도움이 됩니다. 다만 Azure OpenAI를 사용한다는 이유만으로 모든 보안·법적 요건이 자동 충족되는 것은 아니며, 이 사례에서도 데이터 범위 제한과 사람의 검토가 함께 적용됩니다.

## 고객 지원: 출시 후에도 가드레일을 갱신하기

Microsoft 고객 지원은 **약 200개 국가, 60개 이상의 언어**에 걸친 고객 문의를 다룹니다. 특정 문제를 해결할 전문가가 소수이고 영어만 사용하더라도, AI 번역 플랫폼을 통해 고객이 선택한 언어로 소통할 수 있다고 설명합니다.

이처럼 AI가 고객과 고객 데이터에 직접 닿으면, 보안·개인정보 보호·거버넌스 기준을 배포 전에 한 번만 확인하는 것으로 끝낼 수 없습니다.

![고객 지원의 지속적인 보안·개인정보·거버넌스 반영을 설명한 Josh Wong](/mwkorea/assets/images/2026-10-23-ResponsibleAiCustomerZero/image5.png)

Customer Zero Engineering 팀은 기술이나 요구사항이 바뀌면 이를 AI 솔루션에 계속 반영합니다. 초기 문의 해결과 부분 자율 지원 같은 시나리오에서도 **통제를 먼저 마련하고 지속적으로 유지**하는 것이 원칙입니다.

향후 방향으로는 문의 라우팅, 초기 문제 해결, 자율 지원 기능 등을 탐색하고 있습니다. 이 탐색 계획을 고객 지원의 모든 업무가 이미 완전 자율화되었다는 의미로 읽어서는 안 됩니다.

## 한국 조직이 도입 전에 정할 운영 기준

원문은 배포 전 위험 평가, 권한 기반 데이터 접근, 지속적인 텔레메트리·모니터링, 보안 및 RAI 위험의 자동 탐지를 강조합니다. 이를 국내 Copilot·에이전트 도입에 연결하면 다음과 같은 점검표를 만들 수 있습니다.

| 운영 영역 | 먼저 정할 내용 |
|---|---|
| 목적과 범위 | 지원할 업무와 거절할 요청, 사람에게 넘길 조건 |
| 데이터 | 접근 가능한 저장소와 권한, 민감정보 처리 범위 |
| 평가 | 업무 성공 기준과 범위 이탈·근거 오류를 시험할 사례 |
| 검토와 승인 | 위험도별 검토 절차, 배포 승인자, 결과 책임자 |
| 근거와 기록 | 원문 출처, 검토 가능한 설명, 변경·승인 기록 |
| 운영 중 관리 | 감시 지표, 요구사항 변경 시 재평가, 문제 발생 시 대응 |

이 표는 원문을 바탕으로 정리한 실무 제안입니다. Microsoft 내부 시스템을 그대로 도입해야 한다는 뜻도, 특정 라이선스에 이 절차가 자동으로 포함된다는 뜻도 아닙니다.

특히 법무·공급망·고객 지원을 동일한 위험 수준으로 다루기보다는, 데이터의 민감도와 외부에 미치는 영향에 따라 검토 강도를 정하는 편이 합리적입니다.

## 시작하기와 마무리

관련 원칙을 확인하려면 [책임 있는 AI 도구와 관행](https://www.microsoft.com/en-us/ai/tools-practices), [책임 있는 AI 원칙과 접근법](https://www.microsoft.com/en-us/ai/principles-and-approach), [2026 Responsible AI Transparency Report 안내](https://www.microsoft.com/en-us/corporate-responsibility/responsible-ai-transparency-report/)를 참고할 수 있습니다.

Microsoft의 Customer Zero 사례가 주는 메시지는 간단합니다. 에이전트를 안전하게 늘리려면 심사를 없애는 것이 아니라, **범위·근거·책임·지속적인 피드백이 반복 가능하게 작동하는 체계**를 만들어야 합니다. 책임 있는 AI는 혁신 뒤에 붙는 제동 장치가 아니라, 조직이 안심하고 확장하도록 돕는 운영 기반입니다.

> **출처**: [Scaling AI responsibly at Microsoft: Lessons from our Customer Zero journey — Microsoft Inside Track](https://www.microsoft.com/insidetrack/blog/scaling-ai-responsibly-at-microsoft-lessons-from-our-customer-zero-journey/)
>
> 원문 게시 시각: 2026년 10월 22일 16:00 UTC, 한국 시간 10월 23일 01:00. 수치와 내부 운영 상태는 원문 시점 기준입니다. 자세한 내용은 원문 참조.
