import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 데이터베이스에 연결
db_name = 'ec_prj_bk.db3'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# SQL 쿼리 실행 후 데이터 가져오기
query_1m = "SELECT * FROM bgf_1m"
rd_1m = pd.read_sql_query(query_1m, conn)

# page configuration
st.set_page_config(
    page_title="E-commerce Dashboard",
    page_icon="💲 ",
    layout="wide",
    initial_sidebar_state="expanded")

st.title('👑 고객별 구매 횟수 예측')

#alt.themes.enable("dark") 
  
# sidebar config   
#with st.sidebar:
#   st.title('👑 VIP Prediction Dashboard')

# tab
tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

source = rd_1m.sort_values(by="Expected Number of Transactions", ascending=False)
sort = rd_1m.sort_values(by="Expected Number of Transactions", ascending=False).head()

# bar chart
# tab1.bar_chart(source, x="CustomerID", y="Expected Number of Transactions", horizontal=True)

with tab1:
# 최대 값 확인
    max_value = source['Expected Number of Transactions'].max()

# Altair 차트 생성
    chart = alt.Chart(source).mark_bar().encode(
        x=alt.X('CustomerID', title='고객ID', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Expected Number of Transactions', title='예측 거래 횟수'),
        color=alt.condition(
            alt.datum['Expected Number of Transactions'] == max_value,  # 최대 값 조건
            alt.value('orange'),  # 최대 값인 경우 색상
            alt.value('steelblue')  # 기본 색상
        )
    ).properties(
        title="1개월 기준"
    )

# Streamlit에 표시
    st.altair_chart(chart, use_container_width=True)

    
with tab2:
    tab2.write(source)


