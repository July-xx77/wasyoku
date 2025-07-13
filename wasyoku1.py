#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[2]:


wasyoku_df = pd.read_csv("整形・加工後wasyoku.csv")


# In[3]:


st.title("和食店サーチ")

sukininsu_limit =st.slider("好き人数の上限",min_value=0, max_value=8000, step=100, value=6000)
score_limit =st.slider("人気スコアの下限",min_value=0.0, max_value=25.0, step=2.0, value=5.0)


# In[4]:


filtered_df = wasyoku_df.dropna(subset=["好き人数", "pop_score"])
filtered_df = filtered_df[
    (filtered_df['好き人数'] <= sukininsu_limit) &
    (filtered_df['pop_score'] >= score_limit)
]


# In[5]:


fig = px.scatter(
    filtered_df,
    x='pop_score',
    y='好き人数',
    hover_data=['タイトル', '分類', '評価点数'],
    title='人気スコアと好き人数の散布図'
)
st.plotly_chart(fig)


# In[6]:


sort_key = st.selectbox(
    "ランキング基準を選んでください",
    ('評価点数', '評価人数', '好き人数', 'pop_score')
)
ascending = True if sort_key == "pop_score" else False


# In[7]:


st.subheader(f"{sort_key}による和食店ランキング（上位10件）")
ranking_df = filtered_df.sort_values(by=sort_key, ascending=ascending).head(10)

st.dataframe(ranking_df[['タイトル', '分類', '評価点数', '評価人数', '好き人数', 'pop_score']])


# In[7]:





# In[ ]:




