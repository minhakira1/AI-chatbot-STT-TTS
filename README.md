# Voice and Text Chatbot

A simple but powerful chatbot that can interact through both voice and text, using state-of-the-art speech recognition and synthesis.

## Features

- 💬 Text chat interface
- 🎤 Voice input support
- 🔊 Voice output for all responses
- 🌓 Light/Dark mode toggle
- ⚡ Real-time speech-to-text using Whisper
- 🗣️ Natural-sounding responses using Google Text-to-Speech

## Prerequisites

- Python 3.11 or higher
- FFmpeg (required for Whisper)

### Installing FFmpeg

**On macOS:**
```bash
brew install ffmpeg
```

**On Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**On Windows:**
Download from [FFmpeg website](https://ffmpeg.org/download.html)

## Quick Start

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd <project-directory>
```

2. **Create a virtual environment (recommended):**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the application:**
```bash
python server.py
```

5. **Open in browser:**
Visit http://localhost:8000

## How to Use

### Text Chat
1. Type your message in the input box
2. Press Enter or click Send
3. The bot will respond with text and voice

### Voice Chat
1. Click the microphone icon 🎤
2. Speak your message
3. Click the microphone again to stop recording
4. The bot will:
   - Show your transcribed message
   - Respond with text
   - Speak its response

### Example Commands
- "Hello" - Get a greeting
- "What can you do?" - Learn about capabilities
- "Tell me a joke" - Hear a programming joke
- Ask any question - Get an engaging response

## Technical Details

- **Frontend:** HTML, CSS, JavaScript with jQuery
- **Backend:** Python with Flask
- **Speech Recognition:** OpenAI Whisper
- **Text-to-Speech:** Google Text-to-Speech (gTTS)
- **Audio Processing:** pydub

## Using Docker

Build and run using Docker:

```bash
# Build the image
docker build -t voice-chatbot .

# Run the container
docker run -p 8000:8000 voice-chatbot
```

## Project Structure

```
├── server.py           # Main Flask application
├── worker.py          # Chatbot logic and response handling
├── requirements.txt   # Python dependencies
├── Dockerfile        # Docker configuration
├── static/          # Static assets
│   ├── script.js   # Frontend JavaScript
│   └── style.css   # CSS styles
└── templates/       # HTML templates
    └── index.html  # Main chat interface
```

## License

MIT License - Feel free to use and modify for your own projects!
