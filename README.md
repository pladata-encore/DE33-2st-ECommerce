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
<img src="https://github.com/user-attachments/assets/844df965-1363-476b-8a49-c88da5ac50a9" width="400px">

## ERD
<img src="https://github.com/user-attachments/assets/936ff6c7-8d4c-45a7-911d-b2d2e3e0ccef" width="800px">

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

#### 데이터 전처리
- 이상치 및 결측치 처리
	- 주문 취소 데이터 제거 : InvoiceNo에 "C"가 포함된 행(취소된 주문)을 필터링하여 제거
	- 유효한 주문 필터링 : Quantity가 0이 아닌 주문만 남김
 	- 상하위 극단값 정제
- 총 판매 금액 생성 : Quantity와 UnitPrice를 곱하여 TotalPrice 열 추가

#### BG/NRD 모델
- 고객의 미래 구매 행동을 예측하기 위한 확률 모델로 고객의 구매 횟수와 구매 중단 가능성을 추정하여 고객 생애 가치(LTV, LifeTime Value)를 계산하는 데 활용
- 위 프로젝트에서는 예측 구매 횟수 시각화 진행
