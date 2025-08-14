<!-- # 🎙️ AI Voice Agent — 30 Days of AI Voice Agents (Day 13)

## 📌 Project Overview
This project is part of the **30 Days of AI Voice Agents** challenge.  
It’s a **fully functional conversational AI agent** that listens to voice input, processes it using an LLM, and responds back in natural speech — all while remembering context from previous conversations.

---

## 🛠️ Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, FastAPI
- **AI Services:**
  - Speech-to-Text (STT) — Converts voice input to text
  - Large Language Model (LLM) — Generates intelligent responses
  - Text-to-Speech (TTS) — Converts AI responses back into speech
- **Datastore:** In-memory / custom datastore for chat history

---

## ⚙️ Architecture
1. **Voice Input** → User speaks into the microphone.
2. **STT Service** → Audio is transcribed into text.
3. **LLM API** → Processes user query along with previous chat history.
4. **TTS Service** → AI-generated text response is converted to audio.
5. **UI Playback** → Audio response is played back to the user.
6. **Loop** → Conversation continues with remembered context.

---

## ✨ Features
✅ Real-time voice-to-voice AI conversation  
✅ Chat history to maintain conversation context  
✅ Error handling with fallback responses  
✅ Fully responsive, interactive UI  
✅ Single-button recording system with animations  

---

## 📸 Screenshots
*(Add screenshots here of your UI and terminal responses)*

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME -->

# AI Voice Agent – 30 Days Challenge

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


---

## Setup & Installation

### 1. Clone the repository
bash
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>

---



### 2. Create a virtual environment
bash
python -m venv venv
# Activate virtual environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate


### 3. Install dependencies
bash
pip install -r requirements.txt

### 4. Create .env file in project root
MURF_API_KEY=your_murf_api_key
ASSEMBLY_API_KEY=your_assemblyai_api_key
GEMINI_API_KEY=your_gemini_api_key


Important: Do not commit .env to GitHub. Ensure it’s listed in .gitignore.

5. Run the FastAPI server
uvicorn app:app --reload

6. Open the frontend

Open index.html in your browser.

Recommended browsers: Chrome or Edge for microphone support.

Screenshots

Include screenshots of your updated UI.

Capture recording button animations and audio playback.

Usage

Click the 🎙️ Start Recording button to speak to the AI.

Stop recording by clicking the ⏹️ Stop Recording button.

The AI will transcribe your speech, generate a response, and play audio automatically.

Your conversation history is displayed in the transcript box.
