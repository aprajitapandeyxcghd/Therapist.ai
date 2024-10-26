from flask import Flask, request, jsonify
from model import get_response
from text_to_speech import generate_voice_response

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message")
    avatar = data.get("avatar")

    response_text = get_response(message, avatar)
    audio_url = generate_voice_response(response_text, avatar)

    return jsonify({"response": response_text, "audioUrl": audio_url})

if __name__ == "__main__":
    app.run(debug=True)

