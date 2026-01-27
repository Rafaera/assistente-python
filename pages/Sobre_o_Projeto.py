import streamlit as st

st.set_page_config(
    page_title="Sobre o Projeto",
    page_icon="💻",
    layout="centered", # elemento da página usa toda a largura da tela 
    initial_sidebar_state="expanded" # a barra lateral é exibida inicialmente
    )

st.title("Sobre o projeto")

st.markdown(" Este projeto foi desenvolvido como parte integrante do processo de aprendizagem do curso *Fundamentos de Linguagem Python: do Básico a Aplicações de IA*, da [Data Science Academy](https://www.datascienceacademy.com.br), com foco na aplicação prática dos conceitos e na exploração do uso de IA, incorporando adaptações e decisões próprias ao longo do desenvolvimento. ")

st.markdown("**Links:**")
st.markdown(""" 
- [Repositório no GitHub](https://github.com/Rafaera/assistente-python)
- [LinkedIn](https://www.linkedin.com/in/rafaela-santos-924508322/)
""")

st.divider()

st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: 0.85rem;">
       · Autora: Rafaela Santos · 
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: 0.85rem;">
        Projeto educacional para fins de aprendizado e demonstração.
    </div>
    """,
    unsafe_allow_html=True
)