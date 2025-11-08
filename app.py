import streamlit as st
import numpy as np
import pandas as pd

st.header('Jogando uma moeda')

# Controle deslizante para número de lançamentos
num_flips = st.slider('Número de lançamentos:', min_value=1, max_value=1000, value=100)

# Botão para iniciar o experimento
if st.button('Lançar moedas!'):
    st.write(f'Lançando a moeda {num_flips} vezes...')
