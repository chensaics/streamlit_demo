# 支持常用的markdown展示
# st.markdown: 按照markdown语法呈现内容
# st.header
# st.subheader
# st.code
# st.caption: 注释说明
# st.text
# st.latex
import streamlit as st

# markdown

st.title('streamlit极简教程')

st.markdown('### 一. 安装')

st.text('和安装其他包一样，安装 streamlit 非常简单，一条命令即可')
code1 = '''pip install streamlit'''
st.code(code1, language='bash')
st.caption("需要python3.7以及以上环境")


st.markdown('### 二. 使用')


st.markdown('#### 1 生成 Markdown 文档')

code2 = '''import streamlit as st
st.markdown('Streamlit Demo')
st.header('标题')
st.text('普通文本')
'''
st.code(code2, language='python')


st.markdown('#### 2 生成 图表')

code3 = '''import streamlit as st
import pandas as pd 
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)'''
st.code(code2, language='python')


st.markdown('### 三. 运行')

code4 = '''streamlit run demo.py'''
st.code(code4, language='bash')



