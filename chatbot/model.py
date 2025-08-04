
import os
import requests
from datetime import datetime
from sympy import sympify, N

class ChatModel:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found. Check .env file or environment variable.")

        self.model = "gpt-3.5-turbo"
        self.endpoint = "https://openrouter.ai/api/v1/chat/completions"

    def is_math_expression(self, text):
        try:
            sympify(text)
            return True
        except:
            return False

    def is_date_or_time_request(self, text):
        text = text.lower()
        return any(keyword in text for keyword in ["date", "time", "current time", "today", "what time", "what's the time"])

    def get_response(self, user_input):
        if self.is_date_or_time_request(user_input):
            now = datetime.now().strftime("%A, %d %B %Y at %I:%M %p")
            return f"The current date and time is: {now}"

        elif self.is_math_expression(user_input):
            try:
                result = N(sympify(user_input))
                return f"The answer is {result}"
            except Exception as e:
                return f"Math error: {e}"

        else:
            try:
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "http://localhost",  
                    "X-Title": "My Chatbot"
                }
                payload = {
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": user_input}
                    ],
                    "max_tokens": 500,
                    "temperature": 0.7
                }
                response = requests.post(self.endpoint, json=payload, headers=headers)
                data = response.json()

                if "choices" in data:
                    return data['choices'][0]['message']['content'].strip()
                elif "error" in data:
                    return f"API Error: {data['error']['message']}"
                else:
                    return f"Unexpected response: {data}"

            except Exception as e:
                return f"OpenRouter Exception: {str(e)}"

