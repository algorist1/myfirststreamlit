import streamlit as st

st.title("👋🏻 연수 실습 페이지(1023)!!")
st.subheader("처음 실습입니다. 좋아요~")
st.info("반갑습니다. moon입니다^^")

st.write("오른쪽 상단의 'fork' 버튼을 눌러주세요. 이 페이지와 앱이 그대로 복사됩니다.")
st.write("https://docs.google.com/spreadsheets/d/1MDhQpSf110rcR3bSjZ8yEBoMByLZ6Yxs-hQRsC6to1g/edit?usp=sharing")
st.link_button("학교홈피입니다^^", "https://sangmyung-agh.sen.hs.kr/")

st.success("초록색 창")
st.error("빨간색 창")
st.info("파란색 창")
st.warning("노란색 창") # ctrl+/ : 주석처리

st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeDN1b3RsaW9pNnF6cDd2dDhhYWx4eHZkZzFyaGltYWZkOXd5OWp4aSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/xT8qBsOjMOcdeGJIU8/giphy.gif") 
st.video("https://www.youtube.com/watch?v=FRHGtAvU03Q&t=440s")