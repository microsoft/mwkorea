---
title: "영업 AI는 교육만으로 정착하지 않습니다: Microsoft Sales Agent의 역할별 도입 전략"
date: 2026-09-25T00:00:00 KST
categories:
  - Copilot
tags:
  - SalesAgent
  - Microsoft365Copilot
  - CopilotStudio
  - MCP
  - ChangeManagement
  - CustomerZero
excerpt: "Microsoft는 Sales Agent 도입을 위해 영업 업무 자체를 다시 설계하고 약 20개 현장 역할에 맞춘 시나리오를 만들었습니다. 최대 25개 시스템을 연결하는 실행 중심 에이전트와 사용량을 넘어선 성과 측정 방식을 살펴봅니다."
header:
  overlay_image: assets/images/header/Microsoft365-Copilot-KeyArt-Productivity-6K-01.png
  overlay_filter: 0.5
toc: true
toc_sticky: true
classes: wide
author: 최정우
---

# 영업 AI는 교육만으로 정착하지 않습니다: Microsoft Sales Agent의 역할별 도입 전략

영업 담당자에게 새 AI 도구를 배포하고 기능 교육까지 했는데, 업무 방식은 그대로라면 무엇을 바꿔야 할까요? Microsoft Inside Track은 사내 Sales Agent 도입 사례를 통해 **기술 배포와 실제 업무 정착은 하나의 구현 과제**라고 설명합니다.

이 사례의 출발점은 정보 검색이 아니라 영업 담당자가 고객에게 쓰지 못하는 시간이었습니다. 내부 조사에서는 영업 시간의 약 **70%가 고객을 직접 대면하지 않는 활동**에 쓰였고, 직원들은 매일 최소 **15개 도구**를 오가고 있었습니다.

이 글은 Microsoft의 사내 Customer Zero 경험을 정리한 것입니다. 여기에 등장하는 시스템 연결 수와 내부 워크플로를 모든 고객에게 기본 제공되는 제품 사양으로 해석해서는 안 됩니다.

---

## 에이전트를 얹기 전에 업무를 분해했습니다

계정 조사, 미팅 준비, 후속 조치, 팀 간 조율, 제안서·견적 작성 등은 서로 다른 데이터와 도구에 걸쳐 있습니다. Microsoft 팀은 기존 흐름 위에 챗봇 하나를 추가하는 대신, 영업 워크플로를 단계별로 나눴습니다.

각 단계에서 AI가 맡을 일, 아예 없앨 일, 회수한 시간을 고객 활동에 사용할 방법을 검토했습니다. 목표는 영업 담당자가 하나의 작업 공간에서 맥락을 확인하고 업무를 완료하면서, 공식 기록 시스템도 최신으로 유지하는 것이었습니다.

![업무 프로세스 재설계를 설명한 Microsoft의 Rene Vejlby](/mwkorea/assets/images/2026-09-25-SalesAgentRoleBasedAdoption/image1.png)

이 사례의 **70%는 도입 전 업무 시간 구성에 대한 조사**입니다. AI로 시간을 70% 절감했다는 성과 수치가 아닙니다.

## 정보 검색에서 업무 완료로 역할을 바꿨습니다

초기 Sales Agent는 CRM과 여러 데이터 원천을 하나의 대화 경험에 모으는 데 초점을 두었습니다. 이후 Cowork와 다른 Copilot 에이전트도 정보 검색을 잘 수행하게 되면서, Sales Agent는 영업 직무에 맞는 **전체 워크플로 실행**으로 차별화 방향을 바꿨습니다.

현재 사내 구현은 최대 **25개 시스템 오브 레코드**를 대상으로 업데이트와 워크플로를 수행한다고 설명합니다. 예를 들면 대화 안에서 CRM 영업 기회를 만들거나, 투자 요청을 제출하거나, 거래 자료집을 구성하는 일입니다.

![Sales Agent의 사내 엔지니어링을 담당하는 Ajay Nair](/mwkorea/assets/images/2026-09-25-SalesAgentRoleBasedAdoption/image2.png)

기술적으로는 **Copilot Studio와 Model Context Protocol(MCP)** 등을 활용해 다른 Microsoft 팀이 이미 만든 에이전트 서비스를 하나의 진입점에 연결했습니다. 사용자가 프롬프트를 입력하면 Sales Agent가 호출할 에이전트를 선택하므로, 사용자는 개별 서비스의 연결 구조를 모두 알 필요가 없습니다.

## 약 20개 현장 역할에 맞춰 “내 일”을 보여줬습니다

범용 기능 소개와 프롬프트 교육은 인지도를 높일 수 있지만, 영업 담당자의 첫 질문인 “그래서 내 업무에 어떻게 도움이 되는가”에는 충분하지 않았습니다.

도입팀은 약 **20개 현장 역할**을 위한 역할별 페이지를 만들고, 실제 업무를 수행하는 직원과 내용을 검증했습니다. 계정 담당자에게 영업 가이드가 적절한지 확인하는 식입니다. 빈번하게 발생하고 효과도 충분한 업무를 골라야 직원의 관심을 얻을 수 있었습니다.

![역할 기반 도입과 업무 사고방식 변화를 설명한 Susan Neece Robien](/mwkorea/assets/images/2026-09-25-SalesAgentRoleBasedAdoption/image3.png)

교육 방식도 일방적인 시연에서 동료 중심 학습으로 바뀌었습니다. 소규모 동료 모임에서 계정 계획 같은 실제 업무 접근법을 비교하고 Sales Agent를 어디에 적용할지 함께 검토했습니다. 챔피언은 실제 고객·영업 기회 데이터로 시나리오를 시험해 신뢰성을 더했고, 지역 도입 리더는 현장의 맥락을 보완했습니다.

![현장 동료 학습과 동기 부여를 설명한 Jacqueline Stein](/mwkorea/assets/images/2026-09-25-SalesAgentRoleBasedAdoption/image4.png)

## Frontier Accelerator가 지향하는 다섯 가지 변화

원문은 역할별 실습과 동료 학습을 활용하는 Frontier Accelerator 프로그램의 방향을 다섯 가지로 제시합니다. 이는 확정된 정량 성과가 아니라 프로그램이 추구하는 효과입니다.

### 고객과 보내는 시간

관리 업무와 준비 작업을 줄여 고객과의 상호작용에 시간을 돌립니다.

![고객과 보내는 시간을 나타내는 원문 아이콘](/mwkorea/assets/images/2026-09-25-SalesAgentRoleBasedAdoption/image5.png)

### 더 강한 팀 협업

동료가 동료를 가르치고 내부 팀 간 협업을 개선합니다.

![팀 협업을 나타내는 원문 아이콘](/mwkorea/assets/images/2026-09-25-SalesAgentRoleBasedAdoption/image6.png)

### 영업 담당자의 에너지

반복적인 부담을 줄이고 고객 대화에 더 많은 에너지와 가치를 투입합니다.

![영업 담당자의 에너지를 나타내는 원문 아이콘](/mwkorea/assets/images/2026-09-25-SalesAgentRoleBasedAdoption/image7.png)

### 직원 참여

일상에서 AI를 사용하는 실천을 눈에 보이게 공유합니다.

![직원 참여를 나타내는 원문 아이콘](/mwkorea/assets/images/2026-09-25-SalesAgentRoleBasedAdoption/image8.png)

### Frontier 사고방식

AI를 업무 혁신과 성장에 활용하는 기본 선택지로 생각합니다.

![Frontier 사고방식을 나타내는 원문 아이콘](/mwkorea/assets/images/2026-09-25-SalesAgentRoleBasedAdoption/image9.png)

## 사용 횟수보다 거래 진행과 업무 부담을 봅니다

초기에는 일간·주간·월간 사용량을 확인했습니다. 하지만 에이전트를 열었다는 사실만으로 거래가 빨라지거나 고객 업데이트에 걸리는 시간이 줄었다고 말할 수는 없습니다.

Microsoft는 **거래 진행 속도와 영업 담당자의 반복 업무 부담 감소** 같은 결과로 측정 방향을 옮기고 있습니다. 이를 위해서는 에이전트 배포 전에 개선하려는 프로세스와 변화의 증거를 정의해야 합니다. 원문에는 거래 속도 개선율 같은 최종 수치가 제시되어 있지 않습니다.

## 한국 조직에 적용할 시작점

이 사례를 도입 계획에 적용한다면, 영업 직무 하나와 반복 업무 하나를 먼저 정해 보세요. 현재 걸리는 시간과 시스템 이동, 결과 기록 방법을 확인한 뒤 에이전트가 실행할 범위를 정합니다. 이후 실제 담당자와 시나리오를 검증하고 동료 학습을 운영하는 순서가 유용합니다.

제품의 공개 라이선스나 연결 기능을 검토하는 일과, 조직의 업무·권한·변화 관리 체계를 설계하는 일은 구분해야 합니다. 사내 사례의 핵심은 더 많은 기능을 보여주는 것이 아니라 **해당 역할이 끝내야 할 일을 중심으로 경험을 설계했다**는 점입니다.

> 출처: [Driving seller adoption of Sales Agent through role-based change management at Microsoft](https://www.microsoft.com/insidetrack/blog/driving-seller-adoption-of-sales-agent-through-role-based-change-management-at-microsoft/) — Microsoft Inside Track Blog, 원문 발행 2026년 9월 24일(UTC), 한국 시간 9월 25일.  
> 자세한 내용은 원문 참조.
