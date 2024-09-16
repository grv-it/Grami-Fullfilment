import google.generativeai as ai
import gradio as gr
import gramiprompt as ut
import os
from dotenv import load_dotenv


ai.configure(api_key="AIzaSyCpG1t0")

def get_response(prompt):
    response = chat.send_message(prompt)
    return response.text

model = ai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


context =  ut.content() 

context.append("")
response = get_response(context)

def chatbot(message, history):
  prompt = message
  context.append(prompt)
  response = get_response(context)
  context.append(response)
  return response

# create gradio instance  & launch it
gr.ChatInterface(fn=chatbot, examples=["clothing", "accessories", "Electronics: 0Mobile,Laptop,Trimmer"]).launch(debug=True, share=True)
