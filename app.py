import streamlit as st
from openai import OpenAI

st.title("Grok 股票分析工具 - 除錯版")

api_key = st.text_input("輸入 Grok API Key (xai-m91leapVPv0xMbjQdh6YkctH3zenQ3C81PJ07pYIx0yxXGefIG9emK1oWrloLwVrguCgfMvlk4ElQB9d)", type="password")
ticker = st.text_input("股票代碼", "NVDA")

if st.button("開始分析"):
    if not api_key:
        st.error("請輸入 Grok API Key")
    else:
        st.info("正在呼叫 Grok API...")   # 測試用
        try:
            client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")
            
            response = client.chat.completions.create(
                model="grok-4.1-fast",
                messages=[{"role": "user", "content": f"請用繁體中文簡單分析股票 {ticker} 的投資價值"}]
            )
            
            st.success("成功呼叫 Grok！")
            st.subheader("分析結果")
            st.markdown(response.choices[0].message.content)
            
        except Exception as e:
            st.error(f"API 呼叫失敗: {str(e)}")
