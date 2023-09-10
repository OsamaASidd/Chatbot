from flask import Flask, redirect, render_template, request, session, url_for
from dotenv import load_dotenv
import os
import openai
import uuid
import secrets

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("Secret_key")

openai_api_key = os.getenv("OPENAI_API_KEY")

# speech_config.speech_recognition_language = "en-US"
conversation = """The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.
        Human: Hello, who are you?
        AI: I am Goku created by OsamaASidd. How can I help you today?
    """

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.chat_history = conversation
        
users = {}

@app.route("/", methods=("GET", "POST"))
def text():
    if "user_id" not in session:
        # Generate a unique user ID and store it in the session
        user_id = str(uuid.uuid4())
        session["user_id"] = user_id
        # Create a new User object and store it in the users dictionary
        users[user_id] = User(user_id)

    user_id = session["user_id"]
    user = users[user_id]

    result = ""
    if request.method == "POST":
        human = request.form["human"]
        user.chat_history += "\nHuman:" + human + "\nAI:"

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user.chat_history,
            temperature=0.1,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["\n", " Human:", " AI:"]
        )
        

        user.chat_history += str(response.choices[0].text)
        return redirect(url_for("text", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result, UID=user.user_id , chat_history=user.chat_history)

