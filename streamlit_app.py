# import streamlit as st

# st.title("🎈 2025 미적분")
# st.info(
#     "안녕하세요. 오늘 불금인데 비옵니다."
# )

# st.write("첫 연습")

# # st.markdown(): 마크다운 문법 지원 (굵게, 기울임, 목록 등)
# st.markdown("**굵은 텍스트**, *기울임 텍스트*")
# st.markdown("""- 첫 번째 항목
# - 두 번째 항목
# - 여러 줄을 쓸 때""")

# st.image("https://www.readersnews.com/news/photo/202004/98349_64666_155.jpg")

# name=st.text_area("너의 이름은?")
# st.write(name+"님 안녕하세요")

# import openai

# user_api_key=st.text_input("키입력")

# if user_api_key:

#     from openai import OpenAI

#     client = OpenAI(api_key = user_api_key)

#     prompt = st.text_input("프롬프트를 입력해주세요.")

#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     st.markdown("### 💡 GPT의 답변:")
#     st.write(completion.choices[0].message.content)

import streamlit as st
from openai import OpenAI

# 🎨 페이지 설정
st.set_page_config(
    page_title="2025 미적분 GPT",
    page_icon="🎈",
    layout="centered"
)

# 🧠 제목 및 소개
st.title("🎈 2025 미적분 GPT")
st.info("안녕하세요. 오늘 불금인데 비 옵니다 ☔\n\n이 앱은 ChatGPT를 활용한 간단한 텍스트 인터페이스입니다.")

# ✍️ 마크다운 예시
st.header("📌 마크다운 연습")
st.write("첫 연습입니다.")
st.markdown("**굵은 텍스트**, *기울임 텍스트*")
st.markdown("""
- 첫 번째 항목  
- 두 번째 항목  
- 여러 줄을 쓸 때
""")

# 🖼️ 이미지 삽입
st.image("https://www.readersnews.com/news/photo/202004/98349_64666_155.jpg", caption="귀여운 이미지 😊")

# 🧑 사용자 입력
st.header("👤 사용자 정보")
name = st.text_input("너의 이름은?")
if name:
    st.success(f"{name}님, 반가워요! 😊")

# 🔑 API 키 입력
st.header("🔐 OpenAI API 사용하기")
user_api_key = st.secrets["openai"]["api_key"]

if user_api_key:
    client = OpenAI(api_key=user_api_key)

    # 💬 프롬프트 입력
    prompt = st.text_area("✉️ GPT에게 하고 싶은 말을 입력하세요!")

    if prompt:
        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.subheader("💡 GPT의 답변:")
            st.write(completion.choices[0].message.content)
        except Exception as e:
            st.error(f"오류가 발생했어요: {e}")
