# https://docs.streamlit.io/en/stable/
# https://github.com/ultralytics/yolov5
# https://discuss.streamlit.io/t/streamlit-sharing-importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directory-opencv-error/12367/12
# 会话状态session state
import streamlit as st

st.title('Hello streamlit.')
if 'counter' not in st.session_state:
    st.session_state.counter = 0

increment = st.button('Increment')
if increment:
    st.session_state.counter += 1

st.write('Count= ', st.session_state.counter)
# 回调callbacks:回调(callbacks)是一个python函数，它在输入组件更改时被调用，比如按钮被点击、滑动条被拉拽等。
import streamlit as st


# callbacks
def increment_counter():
    st.session_state.counter += 1


st.title('Callbacks')
if 'counter' not in st.session_state:
    st.session_state.counter = 0

st.button('Increment', on_click=increment_counter)
st.write('Count= ', st.session_state.counter)

# 这是无需传参的示例，如果需要数据交互，可以使用args或kwargs，看下面的示例
st.title('Callbacks with args')
if 'counter' not in st.session_state:
    st.session_state.counter = 0

increment_value = st.number_input('Enter a value', value=0, step=1)


def increment_counter(increment_value):
    st.session_state.counter += increment_value


increment = st.button('Increment', on_click=increment_counter,
                      args=(increment_value, ))

st.write('Count = ', st.session_state.counter)
# kwargs的用法，它接收的是命名参数

st.title('Callbacks with kwargs')
if 'counter' not in st.session_state:
    st.session_state.counter = 0


def increment_counter(increment_value=0):
    st.session_state.counter += increment_value


def decrement_counter(decrement_value=0):
    st.session_state.counter -= decrement_value


st.button('Increment', on_click=increment_counter,
          kwargs=dict(increment_value=5))

st.button('Decrement', on_click=decrement_counter,
          kwargs=dict(decrement_value=1))

st.write('Count = ', st.session_state.counter)










