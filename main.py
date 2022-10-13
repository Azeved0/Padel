import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title('Courts review')

df = pd.read_csv(r'padel.csv', sep=',')

court = st.selectbox(
        'Qual o campo que deseja consultar?: ',
        options=df['nome'])

df2 = df.loc[df['nome'] == court]
df2.reset_index(level=None, drop=True, inplace=True)
st.header(df2['nome'][0])
st.write(df2['zona'][0])
col1, col2, col3 = st.columns(3)
col1.metric('Preço do Campo [€/h]',df2['preco do campo [euros/h]'][0])
col2.metric('Aluguer das raquetes [€]',df2['aluguer das raquetes [euros]'][0])
col3.metric('Compra-se as bolas?',df2['paga-se bolas?'][0])

st.title('')


with st.expander('Adicionar um campo'):
    
    z = st.text_input('Zona')
    n = st.text_input('Nome')
    p = st.number_input('Preço do campo [€/h]')
    a = st.number_input('Aluguer das raquetes [€]')
    b = st.selectbox(
        'Paga-se bolas?',
        ('sim', 'nao'))
    c = st.text_input('Condições do campo')
    
    if len(z) != 0 and len(n) != 0 and len(c) != 0:
        if st.button('Clique para adicionar campo'):
            st.write('Campo adicionado - ' + n)        
            df.loc[len(df)] = [z,n,p,a,b,c]
            df.reset_index()

st.write(df)

df.to_csv(r'padel.csv', index=False)
