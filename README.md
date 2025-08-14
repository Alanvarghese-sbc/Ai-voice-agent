
# AI Voice Agent 

## Overview
This project is part of the **30 Days of AI Voice Agents** challenge.  
It is a **web-based voice assistant** that allows users to interact with an AI through voice. The application can:

- Transcribe your speech in real-time.
- Generate intelligent conversational responses using AI.
- Convert the AI's text responses into natural-sounding audio.
- Provide a seamless, interactive UI for recording, playback, and continuous conversation.

This challenge helped me explore **voice interfaces, AI APIs, and modern frontend-backend integration**.

---

## Key Features

1. **Voice-to-Text (Speech Recognition)**  
   - Users can speak to the agent.  
   - Speech is converted to text using AssemblyAI API.  

2. **Conversational AI Response**  
   - Text from user speech is sent to Gemini AI (or other LLM) for generating context-aware responses.  

3. **Text-to-Speech (TTS)**  
   - AI responses are converted to audio using Murf API.  
   - Fallback audio is played if TTS fails.  

4. **Interactive UI**  
   - Start/Stop Recording using a single toggle button.  
   - Audio playback starts automatically once the AI responds.  
   - Responsive and modern UI with animations for recording state.  

5. **Session Management**  
   - Each page load creates a unique session ID.  
   - Allows multi-turn conversations with context persistence.

---

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python, FastAPI  
- **APIs & Services:**  
  - **Murf API** – Text-to-Speech  
  - **AssemblyAI API** – Speech-to-Text  
  - **Gemini API** – Conversational AI  
- **Other Tools:**  
  - dotenv – Environment variable management  
  - MediaRecorder API – Browser-side audio recording  

---

## Project Architecture
```bash

User (Browser)
│
├─> Record Audio / Input Text
│
Frontend (HTML, CSS, JS)
│
├─> API Request to FastAPI
│
Backend (FastAPI)
│ ├─> AssemblyAI → Transcribe speech to text
│ ├─> Gemini → Generate AI response
│ └─> Murf → Convert AI response to speech
│
└─> Return transcription & audio URL to frontend

```


---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>
```

### 2. Create a virtual environment
```bash
python -m venv venv
# Activate virtual environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```


### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env file in project root
```bash
MURF_API_KEY=your_murf_api_key
ASSEMBLY_API_KEY=your_assemblyai_api_key
GEMINI_API_KEY=your_gemini_api_key
```

### 5. Run the FastAPI server
```bash
uvicorn app:app --reload
```

### 6. Open your browser and visit
```bash
 http://localhost:8000. 

```
---

## 📂 Project Structure
```bash
day-13/
├── app.py                 # Python backend (Flask/FastAPI)
├── templates/
│   └── index.html         # HTML frontend
├── static/
│   ├── style.css          # CSS file for styling
│   ├── script.js          # JavaScript functionality
│   └── fallback.mp3       # Fallback audio file
├── requirements.txt       # Python dependencies
└── .env                   # Environment variables

```

<!-- Screenshots

Include screenshots of your updated UI. -->

<!-- Capture recording button animations and audio playback. -->
---
## Usage

✅Click the 🎙️ Start Recording button to speak to the AI.

✅Stop recording by clicking the ⏹️ Stop Recording button.

✅The AI will transcribe your speech, generate a response, and play audio automatically.

✅Your conversation history is displayed in the transcript box.

---
