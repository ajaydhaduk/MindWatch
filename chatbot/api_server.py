from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot.rag_chatbot import RAGChatbot

app = Flask(__name__)
CORS(app)

bot = RAGChatbot()  # loads FAISS index on startup

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"reply": "Please send a message."}), 400
    reply = bot.get_response(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(port=8502, debug=False)