from flask import Flask, render_template, request
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from src.prompt import system_prompt
import os

app = Flask(__name__)
load_dotenv()

GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

# ✅ Use the correct Groq model name
chatModel = ChatGroq(model="llama3-8b-8192", api_key=GROQ_API_KEY)

# Prompt template (optional, if you want structured messages)
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])
    return str(response["answer"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)