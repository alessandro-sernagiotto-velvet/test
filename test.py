import streamlit as st
#https://blog.profession.ai/streamlit-creare-web-app-analitiche-con-python/

print("ciao")


st.title('Hello World')
st.write('Prima app in streamlit')

#https://docs.streamlit.io/library/api-reference


variabile1 = st.text_input("dato1")
variabile2 = st.text_input("dato2")

supervariabile="ho elaborato " + variabile1 + variabile2

cliccato = st.button("cliccami")

if((variabile1 != "") and  (variabile2 != "")):
  if(cliccato):
    st.write(supervariabile)
