# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from huggingface_hub.inference._generated.types import text_to_speech
from openai import OpenAI
import json
import os
import requests
from pypdf import PdfReader
import gradio as gr


load_dotenv(override=True)

BACKEND_URL = "https://sandeep-patel-personal-profile-backend.hf.space/ask"
#BACKEND_URL = "http://127.0.0.1:9010/ask"


class Me:

    def call_backend(self, msg, history):
        print("Calling backend")        
        payload = {
            "message": msg,
            "history": history
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}"
        }
    
        response = requests.post(BACKEND_URL, json=payload, headers=headers, timeout=10)
        print(response.json())

        
        data = response.json()
        return data
        
                

    def chat(self, message, history):
        return self.call_backend(message, history)


if __name__ == "__main__":
    me = Me()

    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column(scale=1):
                gr.Image(
                    value="https://media.licdn.com/dms/image/v2/C5603AQHCfBuc1-Axzw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1653002394774?e=1756339200&v=beta&t=No6J7RbxVJ-eOjLgh3bbgp-iPVjO2ekjH7LQe8OspbQ",
                    width=150,
                    height=150,
                    show_label=False,
                    show_download_button=False,
                    container=False
                )
            with gr.Column(scale=3):
                gr.Markdown("## Sandeep Patel")
                gr.Markdown("**Engineering Manager @ Gumtree Australia** | [LinkedIn Profile](https://www.linkedin.com/in/sandeepnpatel)")
                gr.Markdown("Engineering Manager focused on building scalable backend systems, empowering high-performing teams, and leveraging AI to drive innovation, productivity, and impactful software solutions.")
                

        gr.Markdown("---")
        gr.Markdown("### Ask me anything")

        gr.ChatInterface(me.chat, type="messages", title="Sandeep Patel", description="Ask me anything about my career, background, skills and experience",text_to_speech=True)
        demo.launch()


    