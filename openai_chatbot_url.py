from openai import OpenAI
import gradio

OpenAI.api_key = "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"

messages = [{"role": "system", "content": "You are a financial expert"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = OpenAI.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")

demo.launch(share=True)