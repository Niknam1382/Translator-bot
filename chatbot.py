from googletrans import Translator
from flask import Flask, request, jsonify
from flask import send_from_directory
import os
from flask_cors import cross_origin

app = Flask(__name__)
translator = Translator()

@app.route('/chat', methods=['POST'])
@cross_origin()
def chat():
    user_message = request.json.get('message')
    user_language = request.json.get('language')
    if str(user_language) != 'en':
        user_message = translator.translate(user_message, dest='en').text
    response_message = f"{user_message}"
    response_message = translator.translate(response_message, dest=user_language).text
    return jsonify({'response': response_message})

@app.route('/chat-ui', methods=['GET'])
def chat_ui():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'chat.html')

if __name__ == '__main__':
    app.run(debug=False)

# for run the project, Enter:
# python chatbot.py