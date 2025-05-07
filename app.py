import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins").dropna()

st.title("Penguin Dataset Histogram Viewer")

numeric_columns = df.select_dtypes(include="number").columns.tolist()
categorical_columns = df.select_dtypes(include=["object", "category"]).columns.tolist()

selected_column = st.selectbox("속성 선택:", numeric_columns)
selected_hue = st.selectbox("색상 그룹(hue) 선택:", ["None"] + categorical_columns)
bin_size = st.slider("bin 크기:", min_value=5, max_value=30, step=1, value=10)
multiple_option = st.radio(
    "그룹 히스토그램 표시 방식 (multiple)",
    options=["layer", "stack", "dodge", "fill"],
    index=0
)

fig, ax = plt.subplots()
sns.histplot(data=df, x=selected_column, bins=bin_size, hue=selected_hue if selected_hue != "None" else None, multiple=multiple_option, ax=ax)
ax.set_title(f"{selected_column} (bins={bin_size})")
st.pyplot(fig)

st.title("페이지 제목")

st.header("첫번째 단락")
st.subheader("첫번째 단락 소제목")
st.write("첫번째 단락 입니다요 ")

st.divider()

st.header("두번째 단락")
st.subheader("두번째 단락 소제목")
st.write("두번째 단락 입니다요 ")

# (1) st.text 예시
st.text("This is text\n[and more text](that's not a Markdown link).")

# (2) st.markdown 예시
st.markdown("*Streamlit* is **really** ***cool***.")

st.markdown('''
:red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]  
:gray[pretty] :rainbow[colors] and :blue-background[highlight] text.
''')

st.markdown("Here's a bouquet &mdash; \
:tuIip::cherry_blossom::rose::hibiscus::sunflower::blossom:")  
