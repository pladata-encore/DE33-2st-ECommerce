import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
import altair as alt
import plotly.express as px

# 데이터베이스에 연결
db_name = 'ec_prj_bk.db3'
conn = sqlite3.connect(db_name)

# SQL 쿼리 실행 후 데이터 가져오기
query = "SELECT * FROM rfm"
rd = pd.read_sql_query(query, conn)

# page configuration
st.set_page_config(
    page_title="E-commerce Dashboard",
    page_icon="💲 ",
    layout="wide",
    initial_sidebar_state="expanded")

st.title('📊  고객군 분포')

# tab
tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

# 고객군 분포 바그래프 생성 함수
def plot_segment_distribution(data):
    plt.figure(figsize=(18, 8))
    palette = 'Set2'
    ax = sns.countplot(data=data, x='segment', palette=palette)

    total = len(data.segment)
    for patch in ax.patches:
        percentage = '{:.1f}%'.format(100 * patch.get_height() / total)
        x = patch.get_x() + patch.get_width() / 2 - 0.17
        y = patch.get_y() + patch.get_height() * 1.01
        ax.annotate(percentage, (x, y), size=14)

    plt.title('Number of Customers by Segments', size=16)
    plt.xlabel('Segment', size=14)
    plt.ylabel('Count', size=14)
    plt.xticks(size=12)
    plt.yticks(size=12)

    return plt

with tab1:
    fig = plot_segment_distribution(rd)  # 그래프 생성
    st.pyplot(fig)  # Streamlit에서 Matplotlib 그래프 렌더링

with tab2:
    tab2.write(rd)


