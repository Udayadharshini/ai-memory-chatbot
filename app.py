
import os
import uuid
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("GEMINI_API_KEY")

SYSTEM_PROMPT = """
You are a friendly AI Memory Chatbot.
Answer clearly and helpfully.
Remember details from earlier messages in the conversation.
If you do not know an answer, say so honestly.
"""

# Create the Gemini client
client = genai.Client(
    api_key=API_KEY,
    http_options=types.HttpOptions(timeout=120000)
) if API_KEY else None

# Store conversation history separately for each conversation
conversations = {}

from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    if not client:
        return jsonify({
            "error": "Gemini API key is missing. Check your .env file."
        }), 500

    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()
    conversation_id = data.get("conversation_id") or str(uuid.uuid4())

    if not message:
        return jsonify({"error": "Please enter a message."}), 400

    history = conversations.setdefault(conversation_id, [])

    # Keep only the last 10 messages for context
    recent_history = history[-10:]

    contents = []

    for item in recent_history:
        contents.append(
            types.Content(
                role=item["role"],
                parts=[types.Part.from_text(text=item["text"])]
            )
        )

    contents.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=message)]
        )
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=contents,
            config=types.GenerateContentConfig(
    system_instruction=SYSTEM_PROMPT
)
        )

        answer = response.text

        if not answer:
            raise ValueError("The AI returned an empty response.")

        # Save messages only after a successful response
        history.append({"role": "user", "text": message})
        history.append({"role": "model", "text": answer})

        return jsonify({
            "conversation_id": conversation_id,
            "reply": answer
        })

    except Exception:
        app.logger.exception("Gemini API request failed")
        return jsonify({
            "error": "Sorry, I couldn't get an AI response. Please try again."
        }), 502

if __name__ == "__main__":
    app.run(debug=True)
