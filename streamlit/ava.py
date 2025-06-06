import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard Financeiro")

# Carrega o CSV
df = pd.read_csv("ms_financial_sample.csv", sep=';', on_bad_lines='skip')

st.subheader("Tabela de Dados")
st.dataframe(df)

st.subheader("Gráfico de Barras - Vendas por País")
fig, ax = plt.subplots()
ax.bar(df['Country'], df['Sales'])
plt.xlabel("País")
plt.ylabel("Vendas")
st.pyplot(fig)

