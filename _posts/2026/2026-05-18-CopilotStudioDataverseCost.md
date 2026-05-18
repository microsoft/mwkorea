---
title: "Copilot Studio Agent와 Dataverse File Capacity: 놓치기 쉬운 비용과 거버넌스 이야기"
date: 2026-05-18T00:00:00 KST
categories:
  - Copilot
tags:
  - CopilotStudio
  - Dataverse
  - Microsoft365Copilot
  - RAG
  - Governance
  - Cost
  - SharePoint
excerpt: "Copilot Studio Agent에 파일을 업로드해 지식 원본으로 쓸 때, 문서는 단순히 참조되는 것이 아니라 Dataverse에 저장됩니다. PoC를 넘어 조직 전반으로 Agent를 확산하기 전에 반드시 짚어야 할 Dataverse File Capacity의 구조와 비용 거버넌스 관점의 설계 포인트를 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 안젤라정
---

# Copilot Studio Agent와 Dataverse File Capacity: 놓치기 쉬운 비용과 거버넌스 이야기

Copilot Studio와 Microsoft 365 Copilot의 도입이 본격화되면서, 많은 기업들이 사내 문서를 기반으로 답변하는 RAG(Retrieval-Augmented Generation) 형태의 Agent 구축을 검토하고 있습니다. 특히 OneDrive나 SharePoint에 존재하는 문서, 혹은 로컬 파일을 손쉽게 업로드하여 지식 원본으로 활용할 수 있다는 점은, 초기 PoC나 빠른 업무 적용 관점에서 매우 매력적인 접근 방식입니다.

오늘 이야기할 주제는 바로 이 지점에서 출발합니다. **Copilot Studio Agent에서 "참조 자료 추가 → 파일 업로드" 탭을 사용할 때** 내부적으로 어떤 일이 벌어지는지, 그리고 그 결과가 비용과 거버넌스에 어떤 영향을 주는지에 대한 이야기입니다.

![Copilot Studio Agent의 참조 자료 추가 > 파일 업로드 탭](/assets/images/2026-05-18-CopilotStudioDataverseCost/image1.png)
*▲ Copilot Studio Agent에서 참조 자료를 추가할 때 등장하는 파일 업로드 탭*

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a;">
  <strong>이 글의 한 줄 요약</strong><br/>
  Copilot Studio Agent에 파일을 업로드하면 그 파일은 Dataverse에 저장되고, 이는 곧 <strong>Dataverse File Capacity</strong>를 직접 소모합니다. Agent 확산 전에 반드시 용량과 거버넌스를 함께 설계해야 합니다.
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">놓치기 쉬운 한 가지: Dataverse File Capacity</h2>

Agent 설계와 확산 과정에서 비교적 간과되기 쉬운 중요한 요소가 하나 있습니다. 바로 **Dataverse Capacity**, 그중에서도 파일 저장소에 해당하는 **Dataverse File Capacity** 입니다.

확인은 어렵지 않습니다. [Power Platform Admin Center](https://admin.powerplatform.microsoft.com/) > **라이선싱 > 용량(Capacity)** > **Dataverse** 항목에서 현재 테넌트의 File / Database / Log Capacity 사용 현황을 한눈에 볼 수 있습니다.

![Power Platform Admin Center > 라이선싱 > Dataverse 용량 화면 예시](/assets/images/2026-05-18-CopilotStudioDataverseCost/image2.png)
*▲ (예시) Power Platform Admin Center > 라이선싱 > Dataverse 용량 화면*

Copilot Studio에서 파일을 지식 원본으로 추가하면, 해당 문서는 단순히 외부 위치를 참조하는 것이 아니라 **Dataverse에 저장된 뒤**, semantic index와 vector embedding을 거쳐 검색 및 생성형 응답에 활용됩니다. 즉, 파일은 "연결"되는 것이 아니라 실제로 Dataverse 내부에 **복사되어 저장되고 처리**되는 구조이며, 이 과정에서 Dataverse 스토리지 용량을 직접적으로 소비합니다.

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">"SharePoint에 있으니까 괜찮겠지"라는 오해</h2>

이 특성은 특히 OneDrive나 SharePoint를 활용할 때 오해를 불러일으키기 쉽습니다. 많은 고객이 *"문서가 이미 SharePoint에 있으니 Dataverse 용량과는 무관할 것"* 이라고 생각합니다. 하지만 Copilot Studio의 **파일 업로드 방식(Upload files > OneDrive 또는 SharePoint)** 을 사용할 경우, 해당 문서는 Dataverse로 **가져와져 저장되고 인덱싱** 됩니다. 결과적으로 기존 위치와는 별개로 Dataverse File Capacity가 소모됩니다.

이러한 구조는 초기에는 크게 문제로 보이지 않을 수 있으나, Agent 활용이 조직 전반으로 확산되기 시작하면 빠르게 용량 이슈로 이어질 수 있습니다.

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #fef3c7; border: 1px solid #fcd34d; color: #78350f;">
  <strong>현실적인 시나리오</strong><br/>
  테넌트에 할당된 Dataverse File Capacity가 약 <strong>20GB</strong> 수준이라고 가정해 봅시다. 최대 <strong>512MB</strong> 크기의 파일을 반복적으로 업로드하는 경우, 비교적 적은 수의 파일만으로도 용량 한도에 근접할 수 있습니다. 실 사용 환경에서는 파일 유형과 인덱싱 방식에 따라 차이가 있지만, 핵심은 <strong>예상보다 빠르게 File Capacity가 소진될 수 있다</strong>는 점입니다.
</div>

![Dataverse File Capacity 소진 예시 화면](/assets/images/2026-05-18-CopilotStudioDataverseCost/image3.png)
*▲ 파일 업로드가 누적되며 Dataverse File Capacity가 빠르게 소모되는 예시*

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">"파일 업로드"와 "SharePoint Connector"는 다릅니다</h2>

이 상황을 정확히 이해하려면, Copilot Studio에서 파일 기반 지식 원본을 추가하는 **두 가지 방식의 차이** 를 명확히 구분할 필요가 있습니다. 동일하게 SharePoint를 활용하는 경우라도 동작은 전혀 다릅니다.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 1rem 0 1.4rem;">
  <div style="padding: 1rem 1.1rem; border-radius: 16px; background: #fef2f2; border: 1px solid #fecaca; color: #7f1d1d;">
    <strong>📥 파일 업로드 방식</strong><br/>
    <span style="font-size: 0.95em;">문서가 Dataverse로 <strong>복사·저장</strong>되어 인덱싱됩니다. → <strong>Dataverse File Capacity 소모</strong></span>
  </div>
  <div style="padding: 1rem 1.1rem; border-radius: 16px; background: #ecfdf5; border: 1px solid #a7f3d0; color: #065f46;">
    <strong>🔗 SharePoint Connector 방식</strong><br/>
    <span style="font-size: 0.95em;">파일을 Dataverse로 복사하지 않고, <strong>SharePoint의 검색 인프라를 직접 활용</strong>합니다. → Dataverse 용량 소모 없음</span>
  </div>
</div>

이 차이는 곧 Dataverse 용량 사용 여부로 이어지며, **대규모 문서 라이브러리나 지속적으로 변경되는 콘텐츠** 를 다룰 때 설계 단계에서 매우 중요한 고려 사항이 됩니다.

흥미로운 점도 있습니다. 동일한 환경(Environment) 내에서 **여러 Agent가 같은 SharePoint 폴더를 지식 원본으로 사용** 할 경우, Dataverse는 이를 단일 인스턴스로 관리할 수 있습니다. 같은 데이터를 반복해서 중복 저장하지 않고, 일정 수준 재사용 구조가 존재한다는 의미입니다. (관련 문서: [Unstructured data as a knowledge source - Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-unstructured-data))

다만 이 동작은 **환경 단위로 제한** 됩니다. 다른 Power Platform 환경에서는 동일한 데이터라 하더라도 별도로 저장되고 인덱싱될 수 있다는 점은 함께 기억해야 합니다.

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">설계 단계에서 반드시 던져야 할 4가지 질문</h2>

따라서 Copilot Studio Agent를 설계하는 단계에서는 단순히 "기능 구현이 가능한가"를 넘어, **데이터 저장 방식과 용량 소비 구조** 까지 함께 고려해야 합니다. 실제 고객 환경에서는 다음 질문이 반드시 선행되어야 합니다.

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #f8fafc; border: 1px solid #cbd5e1; color: #0f172a;">
  <ol style="margin: 0; padding-left: 1.2rem;">
    <li>현재 테넌트의 <strong>Dataverse File Capacity</strong>가 충분한가?</li>
    <li>Agent에서 활용하려는 파일의 <strong>총량</strong>은 어느 정도인가?</li>
    <li>동일 문서가 <strong>여러 팀에서 반복적으로 업로드</strong>되고 있지는 않은가?</li>
    <li>이 시나리오가 정말로 <strong>Dataverse에 저장해야 하는 시나리오</strong>인가?</li>
  </ol>
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">용량을 어떻게 관리할 것인가</h2>

그렇다면 이미 업로드된 파일이나 앞으로 예상되는 용량 증가는 어떻게 관리해야 할까요. 가장 현실적이고 효과적인 접근은 **Dataverse에 저장되기 이전, 즉 업로드 단계 이전에서의 관리** 입니다.

### 1. 문서 자체를 최적화하기

가장 직접적이고 안정적인 방법입니다.

- **PDF 압축** 으로 파일 크기 줄이기
- **불필요한 이미지 제거**
- **고해상도 콘텐츠의 해상도 축소**
- 동일/유사 문서 **중복 제거**

### 2. 구조적으로는 SharePoint Connector 우선 검토

대용량 문서나 변경이 잦은 콘텐츠라면 **SharePoint Connector 기반 접근** 을 우선 검토하는 것이 바람직합니다. Dataverse 스토리지 소비를 발생시키지 않으면서도 기존 SharePoint 권한과 검색 체계를 그대로 활용할 수 있어, **운영 안정성과 비용 효율성** 양쪽 모두에서 유리합니다.

### 3. 이미 업로드된 파일은 Agent / 지식 원본 단위로 정리

이미 업로드된 파일은 Agent 또는 지식 원본을 삭제함으로써 일정 수준 용량을 회수할 수 있습니다. 다만 **동일한 지식 원본이 여러 Agent에서 공유** 되고 있을 경우, 일부만 제거해도 완전히 삭제되지 않을 수 있으므로 **실제 제거 여부를 확인하는 운영 절차** 가 필요합니다.

<div style="margin: 1rem 0 1.4rem; padding: 1rem 1.1rem; border-radius: 16px; background: #fef2f2; border: 1px solid #fecaca; color: #7f1d1d;">
  <strong>⚠️ 권장하지 않는 접근</strong><br/>
  Dataverse 내부 테이블을 직접 조작하거나, 관리자 스크립트로 데이터를 강제 삭제하는 방식은 권장되지 않습니다. Copilot Studio가 내부적으로 사용하는 지식 원본 및 인덱스 구조에 영향을 줄 수 있고, Agent 동작의 안정성을 저해할 가능성이 있기 때문입니다.
</div>

<hr/>

<h2 style="margin-top: 1.4rem; padding: 0.55rem 0.85rem; border-left: 6px solid #2563eb; background: #f8fafc;">결국 중요한 것은 "얼마나 빨리"가 아니라 "어떻게 운영할 것인가"</h2>

Copilot Studio Agent 도입이 확장되는 시점에서는, 단순히 *"Agent를 얼마나 빨리 만들 수 있느냐"* 가 아니라, **그 기반이 되는 데이터가 어떻게 저장되고 관리되는가** 가 더 중요한 문제로 이어집니다.

- **Dataverse Capacity 관리**
- **지식 원본 설계 전략**
- **파일 업로드에 대한 거버넌스**

이 세 가지는 비용 최적화와 안정적 운영을 위해 **반드시 함께 고려되어야 하는 요소** 입니다.

Copilot Studio는 강력한 도구이지만, 그 효과를 지속적으로 유지하기 위해서는 **기술적 기능뿐 아니라 데이터 관리 구조에 대한 이해와 사전 설계** 가 함께 이루어져야 합니다. 초기 PoC 단계에서부터 이러한 기준을 명확히 세우는 것이, 이후 조직 전반으로 확산되는 과정에서 **불필요한 비용 증가와 운영 리스크를 줄이는 가장 현실적인 접근** 이라 할 수 있습니다.

<hr/>

<div style="margin: 1.4rem 0; padding: 1.1rem 1.2rem; border-radius: 16px; background: #eff6ff; border: 1px solid #bfdbfe; color: #1e3a8a;">
  <strong>참고 링크</strong>
  <ul style="margin: 0.4rem 0 0; padding-left: 1.2rem;">
    <li><a href="https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-unstructured-data">Unstructured data as a knowledge source - Microsoft Copilot Studio</a></li>
    <li><a href="https://admin.powerplatform.microsoft.com/">Power Platform Admin Center</a> → 라이선싱 > 용량 > Dataverse</li>
  </ul>
</div>
