# Streamlit支持如下状态范例。
# st.progress：进度条，如游戏加载进度
# st.spinner：等待提示
# st.info：显示常规信息
# st.warning：显示报警信息
# st.success：显示成功信息
# st.error：显示错误信息
# st.exception：显示异常信息
# st.balloons：页面底部飘气球，表示庆祝
# st.snow: 页面飘雪，表示庆祝
import time

import streamlit as st

if st.button("Start count sheep"):
    with st.spinner('Wait for it...'):
        bar = st.progress(0)
        msg = st.empty()  # st.empty可以作为占位符
        max_num = 20
        for i in range(1, max_num + 1):
            msg.write("{} sheep...".format(i))
            time.sleep(0.3)
            bar.progress((i * 100) // max_num)
    time.sleep(1)
    st.success("You count 20 sheep! congratulations")
    st.balloons()
    time.sleep(1)
    st.snow()
else:
    pass





