import streamlit as st

pages = {
        "데이터 분석": [
                st.Page("page3.py", title="RFM"),
            ],    
        "고객별 구매 횟수 예측": [
                st.Page("page1.py", title="1주일"), 
                st.Page("page2.py",title="1개월")
            ]
        }

pg = st.navigation(pages)
pg.run()

