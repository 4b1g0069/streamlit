import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="網路攻擊日誌分析", layout="centered")

st.title("網路攻擊日誌分析")
st.write("請上傳一個 log 檔案，系統將判斷是否為攻擊")

# 檔案上傳
uploaded_file = st.file_uploader("請選擇一個 Log 檔案", type="csv")

if uploaded_file is not None:
    # 顯示資料內容
    df = pd.read_csv(uploaded_file)
    st.subheader("資料預覽")
    st.dataframe(df.head())

    # 模擬預測按鈕
    if st.button("開始分析"):
        st.info("模型正在分析中...")
        
        # 模擬模型結果（這裡你可以換成自己的模型函數）
        attack_predictions = []
        for _ in range(len(df)):
            is_attack = random.choice([True, False])
            confidence = round(random.uniform(0.6, 0.99), 2)
            attack_predictions.append({
                "預測結果": "攻擊" if is_attack else "正常",
                "信心分數": confidence
            })

        # 顯示結果
        results_df = pd.DataFrame(attack_predictions)
        full_df = pd.concat([df, results_df], axis=1)
        st.subheader("預測結果")
        st.dataframe(full_df)

        st.success("分析完成！請查看預測結果。")
