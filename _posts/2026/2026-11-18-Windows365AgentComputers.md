---
title: "에이전트에게도 관리되는 PC가 필요하다: Microsoft의 Windows 365 for Agents 활용"
date: 2026-11-18T00:00:00 KST
categories:
  - Copilot
tags:
  - Windows365
  - Agent
  - ComputerUse
  - InsideTrack
  - Governance
excerpt: "Microsoft 사내 IT와 운영 조직이 Windows 365 for Agents로 디지털 워커의 실행 환경을 구성하고 있습니다. BPO AI Toolkit의 구조, 기존 성과와 향후 목표의 차이, 최소 권한·예외 처리·수명 주기 관리 경험을 정리합니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 에이전트에게도 관리되는 PC가 필요하다: Microsoft의 Windows 365 for Agents 활용

API가 없는 레거시 앱이나 화면에서만 가능한 검증이 남아 있다면 에이전트도 컴퓨터 화면을 조작해야 합니다. Microsoft는 Business Operations·Windows 365 제품팀·사내 IT 조직 Microsoft Digital이 함께 **Windows 365 for Agents**를 업무 자동화에 적용하는 사례를 공개했습니다.

핵심은 단순 화면 조작 스크립트가 아니라 **관리 신원과 통제된 PC, 실행 증거, 사람의 예외 처리**를 갖춘 디지털 워커입니다. 현재 한 운영 조직에서 파일럿이 가동 중이며 향후 몇 달에 걸쳐 확대할 계획이라고 설명합니다.

---

## API가 해결하지 못하는 단계에 관리형 Cloud PC 사용

디지털 워커는 자체 관리 신원을 가진 AI 에이전트입니다. 필요할 때 관리형 Cloud PC를 할당받아 데스크톱 앱과 파일을 다루고, 작업이 끝나면 PC를 풀에 반환합니다.

Microsoft 사례는 사람과 유사한 Windows 인터페이스를 사용하되 에이전트에 맞는 인증 모델과 접근 통제를 적용합니다. 장치 상태, 관측 가능성, 지원, 수명 주기를 별도 실험이 아닌 기업 운영 모델에 포함하는 접근입니다.

![Microsoft Digital의 Dave Rodriguez](/mwkorea/assets/images/2026-11-18-Windows365AgentComputers/image1.png)

Dave Rodriguez는 기존 엔터프라이즈 장치 관리·보안·가시성 기반을 활용하면 업무 개발자가 모든 관리·텔레메트리를 새로 만들 필요가 줄어든다는 점을 설명합니다.

## BPO AI Toolkit이 담당하는 것

내부 **BPO AI Toolkit**은 지식·워크플로·에이전트 역량을 제공하고 Windows 365 for Agents는 컴퓨터가 필요한 작업의 실행 환경을 맡습니다. Business Operations는 이를 Dynamics 365와 함께 사용하며 다른 BPO 업무로 재사용할 기반을 만들고 있습니다.

![Commerce Platforms의 Shashi Lanka Venkata](/mwkorea/assets/images/2026-11-18-Windows365AgentComputers/image2.png)

반복과 규모가 큰 업무를 자동화하되 사람은 판단·예외·개선에 집중하는 방향입니다. 툴킷의 주요 구성은 다음과 같습니다.

### Agentic memory

구성원이 경험으로 알고 있던 절차 지식을 에이전트가 요청 시 활용할 수 있는 구조화된 운영 지식으로 바꿉니다.

![Agentic memory 구성 이미지](/mwkorea/assets/images/2026-11-18-Windows365AgentComputers/image3.png)

### Prebuilt agents

공통 에이전트 역량을 재사용해 업무마다 다시 구현하는 부담을 줄입니다.

![Prebuilt agents 구성 이미지](/mwkorea/assets/images/2026-11-18-Windows365AgentComputers/image4.png)

### Agentic UI

운영자가 화면 사이를 전환하는 부담을 줄이고 결정과 예외에 집중하도록 돕습니다.

![Agentic UI 구성 이미지](/mwkorea/assets/images/2026-11-18-Windows365AgentComputers/image5.png)

### Digital twins

실제 전체 프로세스 성과를 측정하고 지속적 개선을 지원합니다.

![Digital twins 구성 이미지](/mwkorea/assets/images/2026-11-18-Windows365AgentComputers/image6.png)

### Agent Desktop

디지털 워커에게 보안이 적용된 컴퓨터 실행 환경을 제공합니다.

![Agentic desktop 구성 이미지](/mwkorea/assets/images/2026-11-18-Windows365AgentComputers/image7.png)

## 이미 달성한 수치와 앞으로의 목표

| 구분 | 원문이 제시한 내용 |
|---|---|
| BPO AI Toolkit 기존 성과 | 사람 개입 75% 감소 |
| 기존 처리 주기 | 25시간에서 10.3시간으로 감소 |
| 처리 결과 | 수천 건 주문을 재작업 없이 완료했다고 보고 |
| Windows 365 for Agents 결합 후 지향점 | 사람 개입 최대 95% 감소, 처리 시간 4시간으로 추가 단축할 경로 |

**95%와 4시간은 이미 달성한 전체 운영 성과가 아닙니다.** 기존 툴킷 성과와 향후 확장 가능성을 구분해야 합니다. 수만 행 주문을 여러 Cloud PC로 분산하는 고처리량 시나리오도 탐색 중이라고 설명합니다.

## 먼저 프로세스를 개선하고 그다음 자동화

![Operations Service Center의 James O'Connor](/mwkorea/assets/images/2026-11-18-Windows365AgentComputers/image8.png)

Microsoft는 이를 **CI + AI**, 즉 지속적 개선과 AI의 결합으로 설명합니다. 복잡하고 비효율적인 절차·불량 데이터·잘못된 정책을 그대로 확장하지 않도록 먼저 프로세스를 점검합니다.

준비된 업무에서는 전문가가 수행 방법을 기록하고, 툴킷이 이를 절차 지침·정책·재사용 역량·실행 계획으로 구성합니다. 트랜잭션이 큐에 들어오면 오케스트레이터가 필요한 스킬을 호출하며 데스크톱·브라우저가 필요할 때 Cloud PC를 사용합니다.

에이전트는 실행 증거를 남기고 예외를 맥락과 함께 전달합니다. 검토자는 처음부터 다시 조사하기보다 완료 단계·막힌 이유·재개 후 동작을 파악할 수 있어야 합니다.

## Customer Zero에서 드러난 운영 과제

![Microsoft Digital의 Dan Kaufman](/mwkorea/assets/images/2026-11-18-Windows365AgentComputers/image9.png)

확대 전에 소유자, 프로비저닝, 신원·라이선스, 비용 배부, 모니터링, 지원, 폐기까지 정의해야 합니다. Cloud PC 추가·삭제의 테넌트 관리자 수작업은 한 팀에서는 가능해도 수십 팀에서는 병목이 됩니다.

Microsoft는 테넌트 관리팀과 프로비저닝 문제를 해결하고 M365 FinOps와 사용 한도·비용 배부를 검토 중입니다. 최소 권한 예시로 주문 생성은 허용하되 취소·삭제는 허용하지 않는 모델을 제시합니다.

한 구현에서는 Global Secure Access를 사람이 쓰는 광범위한 접근이 아니라 필요한 엔드포인트로만 제한했습니다. 단계별 감사 기록의 플랫폼 기본 제공과 지원 담당자를 위한 역할 기반 관리는 제품팀에 요청한 사항이므로 **이미 모든 기본 기능으로 제공된다고 해석하면 안 됩니다**.

![Windows 365 for Agents의 Phil Gerity](/mwkorea/assets/images/2026-11-18-Windows365AgentComputers/image10.png)

## 한국 조직의 도입 순서와 공식 데모

API나 커넥터로 안정적으로 처리할 수 있으면 그것을 먼저 사용하세요. 화면 기반 검증, 데스크톱·온프레미스·인증 웹 앱 때문에 컴퓨터가 필요한 단계에 관리형 PC를 적용하는 것이 원문의 권고입니다.

작게 시작하되 최소 권한, 사람의 예외 책임, 비용, 감사 증거, 종료 시 정리 절차는 처음부터 포함하는 편이 좋습니다. 이 글은 Microsoft 내부 파일럿 경험이며 제품 전체의 GA·지역·가격 조건을 확정하는 발표가 아닙니다.

{% include video id="4bfWVo4lseo" provider="youtube" %}

[Windows 365 for Agents 문서](https://learn.microsoft.com/en-us/windows-365/agents/?OCID=InsideTrack_Product_10958)와 영상에서 소개한 [Microsoft Marketplace의 CUA Record and Replay 작업대](https://marketplace.microsoft.com/en-us/product/microsoft_labs.recordandplay-cua?OCID=InsideTrack_Product_10958)에서 상세 정보를 확인할 수 있습니다.

> **출처**: [When digital workers need a computer: How we’re using Windows 365 for Agents at Microsoft](https://www.microsoft.com/insidetrack/blog/when-digital-workers-need-a-computer-how-were-using-windows-365-for-agents-at-microsoft/), Microsoft Inside Track Blog. 자세한 내용은 원문 참조.
