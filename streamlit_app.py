import streamlit as st

st.title("🎈 2025 미적분")
st.info(
    "안녕하세요. 오늘 불금인데 비옵니다."
)

st.write("첫 연습")

# st.markdown(): 마크다운 문법 지원 (굵게, 기울임, 목록 등)
st.markdown("**굵은 텍스트**, *기울임 텍스트*")
st.markdown("""- 첫 번째 항목
- 두 번째 항목
- 여러 줄을 쓸 때""")

# 페이지 구조용 제목 출력
st.title("메인 제목입니다")
st.header("중간 제목입니다")
st.subheader("하위 제목입니다")

# 수평선 (구분선) 출력
st.markdown("---")  # 또는
st.divider()        # Streamlit >= 1.22 이상에서 가능