import streamlit as st
import pandas as pd 


st.set_page_config(page_title="Finanças")

st.markdown("""
# Boas vindas!

## Nosso APP Financeiro!

Espero que você curta a experiência da nossa solução para organização financeira!

""")


#Widget de upload de arquivos
file_uploader = st.file_uploader(label="Faça upload dos dados aqui", type=['csv'])

#Verifica se algum aequivo foi feito upload
if file_uploader:

    #Leitura dos dados
    df = pd.read_csv(file_uploader)
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y").dt.date


    #Exibição dos dados no app
    exp1 = st.expander("Dados Brutos")
    columns_fmt = {"Valor":st.column_config.NumberColumn("Valor", format= "R$ %f" )}
    exp1.dataframe(df,hide_index=True, column_config=columns_fmt)

    #visão Instituição
    exp2 = st.expander("Instituições") 
    df_instituicao = df.pivot_table(index="Data", columns="Instituição", values="Valor")

    #abas para diferentes visualização
    tab_data, tab_history, tab_share = exp2.tabs(["Dados", "Historico", "Distribuição"])

    #exibe Datafreme
    with tab_data:
        st.dataframe(df_instituicao)

    #exibe Histórico
    with tab_history:
        st.line_chart(df_instituicao)
    
    #exibe Distribuição
    with tab_share:

        #filtro de data
        date = st.selectbox("Filtro Data", options=df_instituicao.index)

        #Gráfico de distribuição
        st.bar_chart(df_instituicao.loc[date])