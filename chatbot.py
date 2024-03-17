# Import required libraries
from googletrans import Translator
from flask import Flask, request, jsonify

app = Flask(__name__)
translator = Translator()

@app.route('/chat', methods=['POST'])
def chat():
    # Get the message from the user
    user_message = request.json.get('message')
    user_language = request.json.get('language', 'en')  # Default to English

    # Translate the message to English if necessary
    if user_language != 'en':
        user_message = translator.translate(user_message, dest='en').text

    # Here you can implement your AI model to generate a response
    # For now, we will just echo the message back
    response_message = f"Echo: {user_message}"

    # Translate the response back to the user's language
    response_message = translator.translate(response_message, dest=user_language).text

    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/chat-ui', methods=['GET'])
# def chat_ui():
#     return app.send_static_file('chat.html')

from flask import send_from_directory
import os

@app.route('/chat-ui', methods=['GET'])
def chat_ui():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'chat.html')

# python chatbot.py