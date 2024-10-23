import streamlit as st

st.title("형성 평가를 봅시다!")

option = st.radio("정답은 무엇일까요?", ["1", "2", "3","4","5"])
option = st.selectbox("정답은 무엇일까요?", ["강남역", "역삼", "서초","교대","합정"])
if option:
   st.write("성공")
   st.balloons()
else:
    st.error("실패")


agree = st.checkbox("동의하시나요?")
st.write(agree)

if agree:
    st.write("동의하셨군요")
else:
    st.write("동의버튼을 눌러요")
    st.snow()

name = st.text_input("이름을 입력해주세요")
if name:
    st.error(f"{name}님 환영합니다.")
