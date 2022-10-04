import streamlit as st
import pandas as pd
import numpy as np

# streamlit run demo.py --server.port=8085
st.title('处理数据')

true_selection = st.checkbox('正确')
false_selection = st.checkbox('错误')

if true_selection:
    st.subheader('标签被标注正确，直接递交即可')
    st.write('用户点击递交即可')
    if st.button('递交更改'):
        st.write('执行递交标签程序：笑脸产生')
        st.write(':smile:' * 20)
elif false_selection:
    st.subheader('标签被标注错误，这里执行更改程序')
    label = st.radio(
        "调用相似度模型，返回top5相似句子的标签，通过st.radio提供用户选择，"
        "返回的可能5个都不是该句子的标签，那么允许用户自定义标签，用户输入标签"
        "相似模型返回了这5个标签，请选择，如果不对请自己输入新标签",
        ('无', '标签1', '标签2', '标签3', '标签4', '标签5'))
    if label == '标签1':
        st.write('You selected 标签1.')
    elif label == '标签2':
        st.write('You selected 标签2.')
    elif label == '标签3':
        st.write('You selected 标签3.')
    elif label == '标签4':
        st.write('You selected 标签4.')
    elif label == '标签5':
        st.write('You selected 标签5.')
    if label == '无':
        new_label = st.text_input('请输入正确的标签：')
        st.write('请输入正确的标签是: ', new_label)
        print("新标签是：", new_label)

else:
    st.write('processing')






