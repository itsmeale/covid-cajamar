import streamlit as st
import altair as alt

import pandas as pd

from covid_cajamar.config import settings

# load data
covid_data_df = pd.read_csv(settings.interim_covid_data_dataset["path"])
covid_data_pre_disease_df = pd.read_csv(settings.interim_covid_data_pre_disease_dataset["path"])

# page header
st.title("Acompanhamento de algumas métricas sobre COVID-19 em cidades do estado de São Paulo")

# page sidebar options
city_options = st.sidebar.selectbox("Selecione uma cidade...", list(set(covid_data_df.nome_munic)))

# filtered dataframes
filtered_covid_data_df = covid_data_df[covid_data_df.nome_munic == city_options]
filtered_covid_data_pre_disease_df = covid_data_pre_disease_df[covid_data_pre_disease_df.nome_munic == city_options]

# Data visualizations

# header metrics
with st.beta_container():
    st.title(f"Dados para {city_options}")
    col1, col2, col3 = st.beta_columns(3)

    with col1:
        st.markdown(f"""### Casos: {filtered_covid_data_df.casos.max()}""")
    
    with col2:
        st.markdown(f"""### Óbitos: {filtered_covid_data_df.obitos.max()}""")
    
    with col3:
        st.markdown(f"""### Letalidade: {round(filtered_covid_data_df.letalidade.max(), 2)}% """)

# média movel de casos (7d)
with st.beta_container():
    st.write("Média móvel de novos casos (7d)")
    linechart = (
        alt
        .Chart(filtered_covid_data_df)
        .mark_line()
        .encode(
            x=alt.X('datahora:T', timeUnit="yearmonthdate", title="Data"),
            y=alt.Y('casos_mm7d', title="Média móvel de novos casos (7d)"),
            color=alt.value("#f33"),
        )
    )
    st.altair_chart(linechart, use_container_width=True)

    # média movel de óbitos (7d)
    st.write("Número de óbitos")
    linechart = (
        alt
        .Chart(filtered_covid_data_df)
        .mark_line()
        .encode(
            x=alt.X('datahora:T', timeUnit="yearmonthdate", title="Data"),
            y=alt.Y('obitos', title="Obitos"),
            color=alt.value("#000"),
        )
    )
    st.altair_chart(linechart, use_container_width=True)
