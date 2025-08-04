
from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from model import ChatModel
from datetime import datetime
import os
from dotenv import load_dotenv
import time
time.clock= time.time  

load_dotenv()  

app = Flask(__name__)
chatbotFile = "chatbotcontent.txt"
chatbot = ChatModel()  
trainer= ListTrainer(chatbot)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_input = request.json.get("message")
        bot_response = chatbot.get_response(user_input)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return jsonify({"response": bot_response, "timestamp": timestamp})
    except Exception as e:
        return jsonify({"response": f"Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)