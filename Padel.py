import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title('Courts review')

df = pd.read_csv(r'/home/spyder/Padel.csv', sep=',')

with st.expander('Adicionar um campo'):
    
    z = st.text_input('Zona')
    n = st.text_input('Nome')
    p = st.number_input('Preço do campo [€/h]')
    a = st.number_input('Aluguer das raquetes [€]')
    b = st.selectbox(
        'Paga-se bolas?',
        ('sim', 'não'))
    c = st.text_input('Condições do campo')
    
    if len(z) != 0 and len(n) != 0 and len(c) != 0:
        if st.button('Clique para adicionar campo'):
            st.write('Campo adicionado - ' + n)        
            df.loc[len(df)] = [z,n,p,a,b,c]
            df.reset_index()

st.write(df)

df.to_csv(r'/home/spyder/Padel.csv', index=False)