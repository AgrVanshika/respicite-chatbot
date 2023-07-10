import streamlit as st
import openai

user_input = st.text_input("Enter your key")
#openaikey = "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"
openai.api_key = user_input

#messages=[]
question = st.text_input("Hi! What is your question?")
#messages.append("role":"system", "content": question)
if question != "":
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",        
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
    st.markdown(response['choices'][0]['message']['content'])