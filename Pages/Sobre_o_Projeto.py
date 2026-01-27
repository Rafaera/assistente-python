import streamlit as st

st.set_page_config(
    page_title="Sobre",
    page_icon="💻",
    layout="centered",
    )

st.title("Sobre o projeto")

st.markdown(" Este projeto foi desenvolvido como parte integrante do processo de aprendizagem do curso *Fundamentos de Linguagem Python: do Básico a Aplicações de IA*, da [Data Science Academy](https://www.datascienceacademy.com.br), com foco na aplicação prática dos conceitos e na exploração do uso de IA, incorporando adaptações e decisões próprias ao longo do desenvolvimento. ")

st.markdown("**Links:**")
st.markdown(""" 
- [GitHub](https://github.com)
- [LinkedIn](https://www.linkedin.com)
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