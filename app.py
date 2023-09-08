import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o CSS personalizado
with open("app.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Carregar o DataFrame a partir do arquivo CSV
dataframe = pd.read_csv("dataset.csv", sep=';')

# Calcular o Lucro e a Margem de Lucro
dataframe['Lucro'] = dataframe['faturamento'] - dataframe['custo']
dataframe['Margem-Lucro'] = (dataframe['Lucro'] / dataframe['faturamento']) * 100

# Criar caixas de seleção para a data inicial e final
data_inicial = st.selectbox('Selecione a data inicial:', dataframe['data'].unique())
data_final = st.selectbox('Selecione a data final:', dataframe['data'].unique())

# Filtrar o DataFrame com base nas datas selecionadas
resultado = dataframe[(dataframe['data'] >= data_inicial) & (dataframe['data'] <= data_final)]

# Exibir o Faturamento Geral
with st.container():
    st.metric("Faturamento Geral", resultado["faturamento"].sum())

# Criar um gráfico de linhas interativo com Plotly Express
fig = px.line(resultado, x='data', y=['faturamento', 'custo', 'Lucro'],
              labels={'value': 'Valor', 'variable': 'Tipo'}, title='Desempenho Financeiro ao longo do tempo')
st.plotly_chart(fig)

# Exibir uma tabela com os resultados filtrados
st.table(resultado)
