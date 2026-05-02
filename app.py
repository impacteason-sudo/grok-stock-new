import streamlit as st
from openai import OpenAI

st.title("Grok 股票分析工具")

api_key = st.text_input("Grok API Key", type="password")
ticker = st.text_input("股票代碼", "NVDA")

if st.button("分析"):
    if api_key:
        try:
            client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")
            response = client.chat.completions.create(
                model="grok-4.1-fast",
                messages=[{"role": "user", "content": f"請分析股票 {ticker}"}]
            )
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(str(e))
    else:
        st.error("請輸入 API Key")
