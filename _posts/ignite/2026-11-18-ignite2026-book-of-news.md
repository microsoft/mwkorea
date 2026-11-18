---
title: "Ignite 2026 Book of News 한눈에 보기: AI 에이전트가 프로덕션으로 이동하는 7개 방향"
date: 2026-11-18T08:30:00+09:00
categories:
  - ignite
tags:
  - AI
  - Microsoft Ignite
  - Copilot
  - Azure
  - Agent365
  - Security
excerpt: "Microsoft Ignite 2026 Book of News를 Azure, Foundry, GitHub, Copilot, Microsoft IQ, Security, Windows의 7개 영역으로 재구성했습니다. 모델과 에이전트를 실제 업무 환경에 배포·운영하기 위해 무엇이 달라지는지 인포그래픽과 함께 살펴봅니다."
header:
  overlay_image: /assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
---

Microsoft Ignite 2026의 [Book of News](https://news.microsoft.com/events/ignite/2026/book-of-news/)는 행사에서 발표한 주요 기능과 제품 업데이트를 모아 둔 공식 안내서입니다. 개별 발표가 워낙 많아 처음부터 순서대로 읽기보다, 서로 어떤 역할로 연결되는지 먼저 보는 편이 효과적입니다.

올해 발표를 한 줄로 정리하면 다음과 같습니다.

> **AI 모델을 만드는 경쟁에서, 에이전트를 기업 환경에서 실행·연결·통제·운영하는 경쟁으로 이동하고 있습니다.**

아래 인포그래픽은 Book of News를 **Azure, Microsoft Foundry, GitHub, Microsoft Copilot, Microsoft IQ, Security, Windows**의 7개 영역으로 재구성한 것입니다.

![Microsoft Ignite 2026 Book of News 7개 영역 인포그래픽](/mwkorea/assets/images/2026-11-18-IgniteBookOfNews/ignite-2026-book-of-news.png)

---

## 1. Azure: 에이전트가 프로덕션에서 실행될 기반

Azure 발표는 모델을 실행하는 데 필요한 칩·인프라부터 데이터, 복원력, 운영까지 연결합니다.

- **Azure Cobalt 200:** 에이전트 워크로드 주변의 CPU 중심 작업을 빠르게 처리하는 Arm 기반 VM이 일반 제공
- **Azure Catalyst:** 애플리케이션·데이터·인프라의 현대화를 탐색부터 실행까지 연결
- **Agentic operations:** Azure Monitor, Azure Copilot, Azure SRE Agent가 운영 맥락과 조사, 복구를 지원
- **Azure AI infrastructure:** Foundry에서 AKS까지 배포 경로를 확장하고 에이전트 격리, 정책, 상태 관리를 강화
- **데이터 서비스:** HorizonDB, Cosmos DB, DocumentDB, PostgreSQL, Redis, Fabric 데이터 앱에 AI와 개발자 기능 추가
- **Windows Server 2028:** 보안 강화와 하이브리드 AI 추론을 위한 차세대 서버 플랫폼 프리뷰

데이터베이스와 모델만 따로 선택하는 방식에서, **업무 데이터·인프라·운영 정책을 하나의 시스템으로 설계해야 한다는 점**이 중요합니다.

## 2. Microsoft Foundry: 모델 선택과 지속 개선

Foundry는 새로운 모델을 제공하는 것뿐 아니라, 에이전트를 만들고 개선하고 운영하는 수명 주기를 맡습니다.

- Microsoft-Decision-1.1 일반 제공
- 코딩·이미지·보안 분야의 새 AI 모델
- 프로덕션 실행 경험을 활용해 에이전트의 행동을 개선
- 환경과 업무에 따라 가장 적절한 모델을 선택하는 구조

Ignite 2026에서 모델은 하나의 정답이 아니라 **업무마다 경제성과 품질 기준이 다른 선택지**로 제시됩니다. 일상적인 코딩, 이미지 처리, 보안 분석, 실시간 음성처럼 요구가 다른 작업에 모델과 도구를 함께 최적화하는 접근이 핵심입니다.

## 3. GitHub: 개발 경험에 에이전트를 연결

GitHub 영역에서는 보안과 규모를 갖춘 AI 애플리케이션 개발, 현대화 워크플로, 에이전트 도구 통합이 강조됐습니다.

- Microsoft Copilot SDK 2.0
- GitHub Copilot을 통한 코드 작성과 현대화
- 애플리케이션과 데이터베이스를 함께 검토하는 마이그레이션
- 모델·도구·거버넌스 규칙을 개발 과정에 포함

코드를 작성하는 행위 자체보다, **에이전트가 개발 환경에서 어떤 도구와 권한을 사용하고 어떻게 배포되는지**를 함께 다룬다는 점이 달라진 부분입니다.

## 4. Microsoft Copilot: 업무 경험을 한곳으로

Copilot 발표는 사용자가 업무를 시작하고, 에이전트와 협업하고, 앱과 외부 시스템을 연결하는 경험을 넓힙니다.

- Home과 Today를 업무의 시작점으로 강화
- Copilot Workspaces에서 사람과 에이전트가 공동의 맥락으로 협업
- Frontier 고객을 위한 Autopilot
- Copilot Code에서 안전한 앱 생성
- Dynamics 365 CRM·ERP 플러그인과 Salesforce 연결
- Agent 365 Business Analytics로 AI 지출과 업무 가치 연결

Copilot은 이제 단순한 대화창이 아니라, **업무·도구·데이터·에이전트를 연결하는 실행 경험**으로 확장되고 있습니다.

## 5. Microsoft IQ: 조직의 맥락을 모델에 전달

Microsoft IQ는 모델 외부에서 조직의 지식과 업무 맥락을 연결하고 유지하려는 계층입니다.

| 영역 | 역할 |
|---|---|
| Microsoft IQ | 조직 AI를 위한 공통 기업 맥락 플랫폼 |
| Foundry IQ | 비정형 데이터에서 검색·추론할 지식 연결 |
| Fabric IQ | 신뢰할 수 있는 비즈니스 의미와 데이터 맥락 |
| Web IQ | 웹 정보와 외부 지식 활용 |
| Work IQ | 사람, 관계, 문서, 회의, 업무 이벤트, 실행 도구 |
| Continuous Improvement | 프로덕션에서 관측한 결과로 에이전트 개선 |

좋은 모델만으로는 회사의 고객, 프로젝트, 승인 기준, 이전 결정을 알 수 없습니다. IQ 계층은 이 정보를 **에이전트가 안전한 방식으로 활용하고 반복해서 학습하는 데 필요한 업무 맥락**으로 정리합니다.

## 6. Security: 에이전트도 신원과 도구가 필요하다

에이전트가 권한을 갖고 업무를 실행하면, 사용자와 애플리케이션을 보호하던 방식도 에이전트까지 확장돼야 합니다.

- Agent 365의 에이전트 발견, 등록, 위험, 관리 인사이트
- Entra Agent ID를 통한 신원과 접근 제어
- Defender의 로컬 에이전트·런타임 보호
- Purview의 데이터 보호와 Copilot 배포 지원
- Intune의 엔드포인트 위험 감소
- Perception의 에이전틱 보안 기능

핵심 질문은 “어떤 에이전트가 있는가”에서 끝나지 않습니다. **누가 만들었고, 어떤 도구와 데이터에 접근하며, 무엇을 실행했고, 비용과 위험이 어느 정도인지**를 함께 확인해야 합니다.

## 7. Windows: 에이전트가 실제 컴퓨터를 사용하는 환경

Windows 발표는 Copilot 기능 개선뿐 아니라, 에이전트가 데스크톱 앱과 파일을 다루는 관리형 실행 환경까지 포함합니다.

- Copilot on Windows의 파일 작업과 검색 개선
- Windows 365 관리 기능과 운영 보조 기능
- Windows 365 for Agents를 통한 Cloud PC 기반 실행
- 로컬·하이브리드 AI 실행 기능
- Intune 기반 보안과 에이전트 격리·거버넌스

API 연결이 충분하지 않은 업무라면 화면과 앱을 사용하는 실행 환경도 필요합니다. Windows 365 for Agents는 이런 작업에 **관리되는 Cloud PC, 신원, 장치 정책, 관측 가능성**을 제공하려는 방향입니다.

## 꼭 봐야 할 발표 12선

1. Azure Cobalt 200 일반 제공
2. Azure Catalyst 일반 제공
3. Azure SRE Agent와 Agentic operations 확장
4. Foundry의 새 모델과 Decision 1.1
5. Copilot Workspaces
6. Copilot Code
7. Dynamics 365와 Salesforce 연결
8. Microsoft IQ 플랫폼
9. Work IQ의 실행·맥락·통제 확장
10. Agent 365의 FinOps와 거버넌스
11. Perception의 에이전틱 보안
12. Windows 365 for Agents와 Windows Server 2028

## 제품 상태는 반드시 기능 단위로 확인하기

Book of News의 발표에는 일반 제공, 프리뷰, 제한 접근, Frontier 고객 대상 기능이 함께 포함됩니다. 같은 제품이라도 기능마다 제공 상태와 지원 플랫폼이 다를 수 있습니다.

도입 검토에서는 다음 순서로 확인하면 좋습니다.

1. 필요한 기능이 정확히 어떤 이름인지 확인
2. GA·Preview·Frontier·제한 접근 여부 확인
3. 대상 테넌트·지역·라이선스 확인
4. 관리자 권한과 데이터 정책 확인
5. 원문의 최신 일정과 제한 사항 다시 확인

> 이 글은 Book of News의 방향과 연결 관계를 설명하는 안내 글입니다. 가격, 출시 일정, 지역 지원, 성능 수치와 제공 조건은 제품별 원문 및 문서를 최종 기준으로 삼아야 합니다.

## 역할별 추천 읽기 경로

| 역할 | 먼저 볼 영역 | 이어서 읽을 글 |
|---|---|---|
| 업무 혁신·도입 담당자 | Copilot, Microsoft IQ, Agent 365 | [Ignite 2026 특집 개요]({{ '/ignite/ignite2026-overview/' | relative_url }}) |
| 에이전트 거버넌스 담당자 | Agent 365, Entra, Purview, Defender | [Ignite 2026의 Agent 365]({{ '/copilot/Agent365IgniteUpdates/' | relative_url }}) |
| Copilot 개발자 | Foundry, Work IQ, Copilot Code | [Ignite 2026 Work IQ 업데이트]({{ '/copilot/WorkIQIgniteUpdates/' | relative_url }}) |
| AI 모델 담당자 | Foundry와 MAI 모델 | [Ignite 2026 MAI 모델 발표]({{ '/copilot/MAIIgniteModelLineup/' | relative_url }}) |
| 엔드포인트·업무 자동화 담당자 | Windows, Windows 365 for Agents | [Windows 365 for Agents 활용]({{ '/copilot/Windows365AgentComputers/' | relative_url }}) |
| 영상을 먼저 보고 싶은 독자 | 한국어 키노트 하이라이트와 풀버전 | [키노트 한국어 더빙 영상]({{ '/ignite/ignite2026-korean-keynote-videos/' | relative_url }}) |

## 마무리

Ignite 2026 Book of News는 제품 목록처럼 보이지만, 전체를 함께 읽으면 명확한 설계도가 보입니다.

- **Azure**가 실행 기반을 제공하고
- **Foundry와 GitHub**가 모델과 애플리케이션을 만들며
- **Copilot**이 업무의 시작점이 되고
- **Microsoft IQ**가 조직 맥락을 연결하고
- **Security**가 신원·권한·위험·데이터를 통제하며
- **Windows**가 실제 업무 화면과 도구로 이어 줍니다

AI 에이전트 도입을 준비하는 조직이라면 단일 기능의 사용법보다 이 연결 구조를 먼저 살펴보는 것이 좋습니다. 어떤 영역부터 검토할지는 기존 인프라와 업무 과제에 따라 다르지만, **만들기 → 연결하기 → 통제하기 → 운영하기**의 흐름은 공통 출발점이 될 수 있습니다.

**출처:** [Microsoft Ignite 2026 Book of News](https://news.microsoft.com/events/ignite/2026/book-of-news/) (2026년 11월 17일 발표 기준)
