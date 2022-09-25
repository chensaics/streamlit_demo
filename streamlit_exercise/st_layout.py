# treamlit 是自上而下渲染的，组件在页面上的排列顺序与代码的执行顺序一致。
# 可以应用如下布局组件实现非自上而下的布局。
# st.sidebar：侧边栏
# st.columns：列布局
# st.expander：隐藏
# st.empty：占位符，可以后续更新其中内容。
# st.container: 容器占位符，可以后续往其中添加内容。
import streamlit as st
import time
import pandas as pd


st.title('streamlit布局范例')

st.header("1，sidebar")
st.text("see the left side")
with st.sidebar:
    st.subheader("配置参数")
    optim = st.multiselect(label="optimizer:", options=["SGD", "Adam", "AdamW"])
    lr = st.slider(label="lr:", min_value=1e-5, max_value=0.1)
    early_stopping = st.checkbox(label="early_stopping", value=True)
    batch_size = st.number_input(label="batch_size", min_value=1, max_value=64)

st.header("2，columns")
col1, col2, col3 = st.columns(3)
col1.metric("accuracy", "0.82", "+32%")
col2.metric("AUC", "0.89", "-8%")
col3.metric("recall", "0.92", "+4%")

st.header("3，expander")
st.line_chart(data=[1, 1, 2, 3, 5, 8, 13, 21, 33, 54])
with st.expander(label="see explanation"):
    st.text("This is the Fibonacci sequence")
    st.text("You can see more about it in below link")
    st.markdown(
        "[](https://baike.baidu.com/item/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97/99145?fr=aladdin)")

st.header("4，empty")
# st.empty可以作为占位符
if st.button("Start count sheep"):
    msg = st.empty()  # st.empty可以作为占位符
    for i in range(1, 11):
        msg.write("{} sheep...".format(i))
        time.sleep(0.3)
else:
    pass  # st.stop

st.header("5，container")

container = st.container()
container.write("1:This should in container")
st.write("2:This should out  container")
container.write("3:This should in container too")
container.bar_chart(data=[1, 1, 2, 3, 5, 8, 13, 21, 33, 54])







