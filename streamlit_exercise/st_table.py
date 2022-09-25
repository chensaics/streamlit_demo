# 支持以下图表展示：
# st.table
# st.dataframe
# st.metric
# st.json
# st.line_chart
# st.bar_chart
# st.area_chart
# st.map_chart
# st.pyplot : matplotlib 的 figure
# st.plotly_chart: plotly 的 figure
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.title('streamlit图表范例')

st.header("一，Table/DataFrame示范")

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('第%d列' % (i + 1) for i in range(5))
)

# st.table(df)
st.dataframe(df.style.highlight_max(axis=0))

st.header("二，metric监控指标")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.header("三，内置图表")

st.subheader("1，折线图")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.subheader("2，面积图")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)

st.subheader("3，柱形图")

chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])
st.bar_chart(chart_data)

st.subheader("4，地图")

chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(chart_data)

st.header("四，plotly图表")

fig = px.line(data_frame=px.data.stocks(), x="date", y=["GOOG", "AAPL", "AMZN", "FB"])

st.plotly_chart(fig)
