import streamlit as st
#st.title('Hello World!')
st.set_page_config(page_title="GA Dashboard",
                   layout="wide",
                   initial_sidebar_state="auto"
)
st.title("지난 달 매출 대시보드")
col1, col2,col3,col4 = st.columns(4)

col1.metric("총매출")
col2.metric("평균주문가치(AOV)")
col3.metric("신규 고객 수")
col4.metric("이탈 고객 수")
col1=57299.0
col2=27.2
col3=772
col4=3247