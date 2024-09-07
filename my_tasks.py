from crewai import Task
import streamlit as st


def criar_task_recomendar(guia_turistico):
    recomendar = Task(
        description=(
             "Usar a ferramenta de busca para pesquisar no site {url} sobre {destino} na {continente}, na regiao {regiao}"
             "Numa escala de 0 a 10, onde 0 é a menor importância e 10 a maior importância."
             "Critérios de classificação: beleza natural e a infraestrutura turística entre os turistas."             
             "Classificar apenas os destinos {destino} na regiao {regiao} importância numa escala 8 de importância."
             "Listar os resultados mais acessos na regiao {regiao}."
             "Apresentar os critérios usados na classificação final."
             "Faça comentários em Português do Brasil (pt-br)."
             "Resposta final deve estar em Português do Brasil (pt-br)."
             ) ,
        expected_output=
             "Lista com links  dos lugares encontrados. incluir a url para do link."
         ,
         agent=guia_turistico,
         output_file='lista_resultado'
     )
    st.write("Tasks recomendar criada.")
    st.write("Objetivo: " + str(guia_turistico.goal))
    return recomendar
