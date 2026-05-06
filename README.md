# 🎙️ AI Voice Assistant

An AI-powered voice assistant web application that converts text to natural-sounding speech and transcribes audio files to text using state-of-the-art AI models.

---

## 🚀 Live Demo

👉 [stt-tts-app.streamlit.app](https://stt-tts-app.streamlit.app)

---

## 📌 Features

- 🔊 **Text to Speech** — Convert any text into natural-sounding audio instantly
- 🎤 **Speech to Text** — Transcribe uploaded audio files to text with high accuracy
- 🌐 **Multilingual Support** — Works with multiple languages for both TTS and STT
- 💻 **Microphone Recording** — Record and transcribe speech directly (local deployment)
- 📁 **Audio File Upload** — Upload MP3, WAV, M4A files for transcription
- 🎨 **Clean UI** — Intuitive horizontal navigation with a modern dark theme

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| [Streamlit](https://streamlit.io) | Web application framework |
| [Groq - Whisper Large V3](https://groq.com) | Audio transcription (Speech to Text) |
| [gTTS](https://pypi.org/project/gTTS/) | Text to Speech conversion |
| [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) | Microphone audio capture |
| [streamlit-option-menu](https://github.com/victoryhb/streamlit-option-menu) | Navigation bar |
| [Python Dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## 📂 Project Structure

```
stt-tts-app/
├── app.py                  # Main application & navigation
├── pages/
│   ├── __init__.py         # Pages module
│   ├── home.py             # Home page
│   ├── tts.py              # Text to Speech page
│   ├── stt.py              # Speech to Text page
│   └── about.py            # About page
├── requirements.txt        # Python dependencies
├── runtime.txt             # Python version
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/piya-b31/stt-tts-app.git
cd stt-tts-app
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys

Create a `.streamlit/secrets.toml` file:
```toml
GROQ_API_KEY = "your_groq_api_key"
```

Or create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key
```

> **Get your Groq API Key (Free)** → [console.groq.com](https://console.groq.com)

### 4. Run the App
```bash
streamlit run app.py
```

---

## 🔑 Environment Variables

| Variable | Description | Where to Get |
|---|---|---|
| `GROQ_API_KEY` | Groq API Key for Whisper transcription | [Groq Console](https://console.groq.com) |

---

## 📖 How It Works

### Text to Speech
```
User enters text
      ↓
gTTS converts text to audio
      ↓
Audio plays in browser & available for download
```

### Speech to Text
```
Upload audio file (MP3/WAV/M4A)
      ↓
Groq Whisper Large V3 transcribes audio
      ↓
Transcribed text displayed instantly
```

---

## 💡 Usage

### Text to Speech
1. Navigate to **Text to Speech** tab
2. Enter your text in the input box
3. Click **Convert** to generate audio
4. Play or download the generated audio

### Speech to Text
1. Navigate to **Speech to Text** tab
2. Upload an audio file (MP3, WAV, M4A)
3. Click **Transcribe Audio**
4. View the transcribed text instantly

---

## 📦 Requirements

```
streamlit
speechrecognition
gtts
requests
streamlit-option-menu
groq
```

---

## 🖥️ Deployment

### Streamlit Cloud
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Add `GROQ_API_KEY` in **Settings → Secrets**
5. Deploy!

---

## 🙋‍♀️ Author

**Piya** — BCA Student, Avantika University, Ujjain

[![GitHub](https://img.shields.io/badge/GitHub-piya--b31-black?logo=github)](https://github.com/piya-b31)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
