# E-Commerce 데이터 분석 및 시각화

## 🌱 팀원
[😎오현옥](https://github.com/alonee9393)&nbsp;&nbsp;&nbsp;&nbsp;
[🐬유미라](https://github.com/raramii)&nbsp;&nbsp;&nbsp;&nbsp;
[🦄진현석](https://github.com/culown)&nbsp;&nbsp;&nbsp;&nbsp;
[🎸최동현](https://github.com/dh823)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

## 👨‍🏫 프로젝트  개요
- Kaggle의 [CRM 데이터](https://www.kaggle.com/code/sercanyesiloz/crm-analytics/notebook)를 바탕으로 BG/NRD 모델을 사용하여 고객 구매 횟수를 예측하고, Streamlit을 통해 시각화 진행
- 완성된 애플리케이션은 Docker 이미지로 빌드

## 🔨 기술 스택
#### 개발환경
<div align=left>
	<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
	<img src="https://img.shields.io/badge/ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white">
	<img src="https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
	<img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
</div>

#### DB
<div align=left>
<img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
</div>

<!-- <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> -->

## 🔧 시스템 아키텍처
<img src="https://github.com/user-attachments/assets/10ac0ae1-274e-453e-a433-8712a9f213e4" width="350px">

## ERD
<img src="https://github.com/user-attachments/assets/936ff6c7-8d4c-45a7-911d-b2d2e3e0ccef" width="750px">

## 🖥️수행결과
<div align=left>
	<img src="https://github.com/user-attachments/assets/fb098185-e314-413e-af2e-60422fd6c778" width="400px">
	<img src="https://github.com/user-attachments/assets/3594f814-8d47-482a-83ff-d7b2849c0d5c" width="400px">
</div>
<div align=left>
	<img src="https://github.com/user-attachments/assets/eb0b3f44-3c86-40f7-b809-e84297e6c4f1" width="400px">
	<img src="https://github.com/user-attachments/assets/7e5f51ad-e1cf-40d4-82f4-9907f697049e" width="400px">
</div>
<div align=left>
	<img src="https://github.com/user-attachments/assets/fff1a6bb-f9a2-4fa9-8df1-4e1629d88595" width="400px">
	<img src="https://github.com/user-attachments/assets/5871f154-b750-402d-ae06-9e36a8f92854" width="400px">
</div>

### 설명
#### 1. 데이터 전처리
- 이상치 처리 : IQR(Interquartile Range) 기반으로 이상치를 제거하는 함수를 정의하고, Quantity와 UnitPrice의 상·하한선을 벗어난 값을 해당 범위 내 값으로 대체
- 결측치 처리 : Customer ID와 Description의 결측치를 제거
- 주문 취소 데이터 제거 : InvoiceNo에 "C"가 포함된 행(취소된 주문)을 필터링하여 제거
- 유효한 주문 필터링 : Quantity가 0이 아닌 주문만 남김
- 총 판매 금액 생성 : Quantity와 UnitPrice를 곱하여 TotalPrice 열을 추가
- 이상치 제거 (상하위 0.01%) : 상하위 극단값은 이전에 정의한 IQR 기반 함수로 제거하여 데이터 정제
#### 2. BG/NRD 모델
- 고객의 미래 구매 행동을 예측하기 위한 확률 모델입니다. 이 모델은 고객의 구매 횟수와 구매 중단 가능성을 추정하여 고객 생애 가치(LTV, LifeTime Value)를 계산하는 데 활용됩니다.

BG/NBD 모델의 구성 요소:

구매 횟수 예측 (Buy):

고객이 일정 기간 동안 구매를 지속할 것으로 가정하며, 구매 횟수는 포아송 분포를 따릅니다.
고객마다 구매 빈도가 다르기 때문에, 이 구매 빈도는 감마 분포를 따른다고 가정합니다.
구매 중단 예측 (Till You Die):

고객이 어느 시점 이후 구매를 중단할 확률은 기하 분포를 따릅니다.
이 중단 확률은 고객마다 다르며, 베타 분포를 따른다고 가정합니다.
이러한 가정을 통해 BG/NBD 모델은 고객의 미래 구매 횟수를 예측하고, 이를 기반으로 LTV를 산출합니다. 이때, 고객의 평균 구매 금액은 Gamma-Gamma 모델을 통해 추정됩니다.

BG/NBD 모델은 고객의 과거 구매 데이터를 활용하여 미래의 구매 행동을 예측하는 데 유용하며, 마케팅 전략 수립 및 고객 관리에 중요한 지표로 활용됩니다.
