import streamlit as st
import openai

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

st.write("""
# I am here to help!
""")

user_input = st.text_input("Enter your key")
openai.api_key = user_input

#messages=[]
question = st.text_input("Hi! What is your question?")
#messages.append("role":"system", "content": question)
if question != "":
    with st.spinner("Generating your response"):
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",  
            max_tokens = 500,
            temperature=0.7,
            messages=[
                {
                    "role":"system", "content":'''
                    you are a chatbot that answers questions to cognitive abilities
                    like improve numerical ability, 
                    verbal ability, spatial abilty, computations, clerical perception and Form perception 
                    or critical workplace abilities like leading and influencing, helping and facilitating, and 
                    organizing and closing.
                    '''
                },
                {"role": "system", "content": question}
            ]
           
    )        
    st.success("Done!")
    #st.markdown(response['choices'][0]['message']['content'])
    st.markdown(
        f'<div style="height: 600px; overflow-y: auto;">'
        f'{response["choices"][0]["message"]["content"]}'
        f'</div>',
        unsafe_allow_html=True
    )
