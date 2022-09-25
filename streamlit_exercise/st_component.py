# streamlit支持非常丰富的交互式输入控件。
# 值得注意的是，当改变任何一个输入时，整个网页会重新计算和渲染。
# button：按钮
# download_button：文件下载
# file_uploader：文件上传
# checkbox：复选框
# radio：单选框
# selectbox：下拉单选框
# multiselect：下拉多选框
# slider：滑动条
# select_slider：选择条
# text_input：文本输入框
# text_area：文本输入区域
# number_input：数字输入框，支持加减按钮
# date_input：日期选择框
# time_input：时间选择框
# color_picker：颜色选择器
import streamlit as st
import plotly.express as px
import time
import pandas as pd
import numpy as np


st.title('streamlit控件范例')

st.header("1，button")

# button常用于启动一段费时代码的执行
if st.button("Start count sheep"):
    msg = st.empty()  # st.empty可以作为占位符
    for i in range(1, 11):
        msg.write("{} sheep...".format(i))
        time.sleep(0.3)
else:
    pass  # st.stop

st.header("2，selectbox")
# 下拉选择框
stock = st.selectbox(label="Choose a stock", options=["GOOG", "AAPL", "AMZN", "FB"])

st.write('You selected:', stock)

fig = px.line(data_frame=px.data.stocks(), x="date", y=[stock])

st.plotly_chart(fig)

st.header("3，number_input")

st.write("input x and y to eval x+y:")
x = st.number_input("x", min_value=-10000, max_value=10000)
y = st.number_input("y", min_value=0, max_value=8)
st.write('x+y=', x + y)

st.header("4，slider")

st.write("slide to choose your age:")
age = st.slider(label="age", min_value=0, max_value=120)

st.write('your age is ', age)

st.header("5，text_input")

st.write("what's your name")
name = st.text_input(label="name", max_chars=100)
st.write("your name is ", name)

st.header("6，text_area")

st.write("give an introduction of  yourself")
name = st.text_area(label="introduction", max_chars=1024)

st.header("7，download_button")


@st.cache
def save_csv():
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    df = px.data.stocks()
    return df.to_csv().encode('utf-8')


csv = save_csv()

st.download_button(
    label="Download stock data",
    data=csv,
    file_name='stocks.csv',
    mime='text/csv',
)

st.header("8，file_uploader")

csv_file = st.file_uploader("Choose a csv file")

if csv_file is not None:
    try:
        dfstocks = pd.read_csv(csv_file)
        st.table(dfstocks)
    except Exception as err:
        st.write(err)

image_file = st.file_uploader("choose a image file(jpg/png)")
if image_file is not None:
    try:
        st.image(image_file)
    except Exception as err:
        st.write(err)

# 日期选择器
date = st.date_input('Pick a date')
# 颜色选择器
color = st.color_picker('Pick a color')
# 显示json
st.json({
    "code": 0,
    "data": {
        "sex": "female",
        "age": 18,
        "score": 100
    }
})
# 显示代码
code = """
    def func():
        print('Hello streamlit.')
"""
st.code(code, language='python')

# 显示pandas中的dataframe
df = pd.DataFrame(np.random.randn(50, 5), columns=(
    'col %d' % i for i in range(5)))
# st.dataframe(df)
st.write(df)
# 显示表格
st.table(df)
# 指标性数据显示, 安装另一个库streamlit-metrics，执行安装命令pip install streamlit-metrics
# from streamlit_metrics import metric_row
# st.write("一周数据统计")
# metric_row(
#     {
#         "关注人数": 100,
#         "点赞人数": 200,
#         "在看人数": 300,
#         "分享人数": 400
#     }
# )

# https://docs.streamlit.io/library/get-started
# https://docs.streamlit.io/library/api-reference/widgets/st.camera_input
# https://docs.streamlit.io/library/api-reference/widgets/st.color_picker
# https://share.streamlit.io/whitphx/streamlit-stt-app/main/app_deepspeech.py
# st.balloons()
# st.spinner()
# st.progress()
# st.snow()
# st.error()
# st.warning()




