# 🎙️ AI Voice Agent — 30 Days of AI Voice Agents (Day 13)

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

<!-- ## 📸 Screenshots
*(Add screenshots here of your UI and terminal responses)*

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME -->
