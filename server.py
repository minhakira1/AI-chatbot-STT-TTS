import base64
import json
from flask import Flask, render_template, request
from flask_cors import CORS
import os
from worker import speech_to_text, text_to_speech, chatbot_process_message
import whisper
from gtts import gTTS
import io
import wave
import tempfile
from pydub import AudioSegment

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Load Whisper model
WHISPER_MODEL = whisper.load_model("base")


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    if 'audio' not in request.files:
        return {"error": "No audio file provided."}, 400
    audio_file = request.files['audio']
    audio_bytes = audio_file.read()
    audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
        audio.export(temp_audio.name, format='wav')
        result = WHISPER_MODEL.transcribe(temp_audio.name)
        text = result.get('text', '')
        os.unlink(temp_audio.name)
    return {"text": text.strip()}


@app.route('/process-message', methods=['POST'])
def process_message_route():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return {"error": "No text provided."}, 400
    # Use chatbot logic to generate response
    bot_reply = chatbot_process_message(text)
    tts = gTTS(bot_reply)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_audio:
        tts.save(temp_audio.name)
        temp_audio.seek(0)
        audio_bytes = temp_audio.read()
        os.unlink(temp_audio.name)
    audio_b64 = base64.b64encode(audio_bytes).decode('utf-8')
    return {"text": bot_reply, "audio": audio_b64}


if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')
