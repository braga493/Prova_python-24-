import pandas as pd
import openpyxl
import plotly.express as px
import streamlit as st


df = pd.read_excel("dados-educacao.xlsx")


df_mestrado = df[df["escolaridade"] == "Mestrado"]



contagem = df_mestrado["genero"].value_counts().reset_index()
contagem.columns = ["genero", "quantidade"]


st.title("Painel da Escolaridade — Pessoas com Mestrado")


opcao = st.sidebar.radio(
    "Escolha a visualização:",
    ["Tabela", "Gráfico"]
)


if opcao == "Tabela":
    st.header("Pessoas com Mestrado por Gênero (Tabela)")
    st.dataframe(contagem, use_container_width=True, hide_index=True)


elif opcao == "Gráfico":
    st.header("Pessoas com Mestrado por Gênero (Gráfico)")
    fig = px.bar(
        contagem,
        x="genero",
        y="quantidade",
        color="genero",
        labels={"genero": "Gênero", "quantidade": "Número de Pessoas"},
        title="Quantidade de Homens e Mulheres com Mestrado"
    )
    st.plotly_chart(fig, use_container_width=True)

