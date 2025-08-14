from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
import assemblyai as aai
from fastapi import UploadFile, File
import google.generativeai as genai


# Load environment variables
load_dotenv()
MURF_API_KEY = os.getenv("MURF_API_KEY")
ASSEMBLY_API_KEY = os.getenv("ASSEMBLY_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Setup AssemblyAI # Configure APIs
aai.settings.api_key = ASSEMBLY_API_KEY
transcriber = aai.Transcriber()

genai.configure(api_key=GEMINI_API_KEY)  # ✅ Setup Gemini


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Serve frontend
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# # Handle file upload and transcribe audio
# @app.post("/transcribe")
# async def transcribe_audio(file: UploadFile = File(...)):
#     try:
#         audio_data = await file.read()
#         transcript = transcriber.transcribe(audio_data)
#         return {
#             "filename": file.filename,
#             "transcription": transcript.text
#         }
#     except Exception as e:
#         return {"error": str(e)}



# Voice API endpoint,Handle Text-to-Speech generation using Murf API
class TTSRequest(BaseModel):
    text: str

# Generate voice from text using Murf API
@app.post("/generate-voice")
def generate_voice(data: TTSRequest):
    headers = {
        "api-key": MURF_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "voiceId": "en-US-miles",
        "text": data.text,
    }

    try:
        response = requests.post("https://api.murf.ai/v1/speech/generate", json=payload, headers=headers, timeout=10)

        if response.status_code == 200:
            result = response.json()
            return {"audio_url": result.get("audioFile")}
        else:
            return {"error": response.text}
    except Exception as e:
            return {"error": str(e)}

# Echo Bot v2 Endpoint — Upload, Transcribe, TTS, Return Voice
@app.post("/echo")
async def echo_audio(file: UploadFile = File(...)):
    try:
        # Read audio
        audio_data = await file.read()
        
        # Transcribe audio
        transcript = transcriber.transcribe(audio_data)
        if not transcript.text:
            return {"error": "Could not transcribe audio."}
        
        # Send text to Murf for TTS
        headers = {
            "api-key": MURF_API_KEY,
            "Content-Type": "application/json"
        }

        payload = {
            "voiceId": "en-US-miles",  # You can change this voice ID if needed
            "text": transcript.text,
        }

        response = requests.post("https://api.murf.ai/v1/speech/generate", json=payload, headers=headers)

        if response.status_code == 200:
            result = response.json()
            return {
                "transcription": transcript.text,
                "audio_url": result.get("audioFile")
            }
        else:
            return {"error": response.text}

    except Exception as e:
        return {"error": str(e)}     
    

# #llm query Endpoint
# class LLMRequest(BaseModel):
#     text: str

# @app.post("/llm/query")
# async def llm_query(data: LLMRequest):
#     try:
#         # Create model instance
#         model = genai.GenerativeModel("gemini-2.5-flash") #model

#         # Generate response
#         response = model.generate_content(data.text)

#         return {"response": response.text}
#     except Exception as e:
#         return {"error": str(e)}


# Store chat history in memory (one FastAPI worker only!)
chat_histories = {}  # { session_id: [ {"role": "user"/"assistant", "content": "..."} ] }

FALLBACK_AUDIO_URL = "/static/fallback.mp3"  # <--  fallback.mp3 in the static folder


@app.post("/agent/chat/{session_id}")
async def agent_chat(session_id: str, file: UploadFile = File(...)):
    try:
        # Step 1: Read audio
        audio_data = await file.read()

        # Step 2: STT (Speech-to-Text)
        try:
            transcript = transcriber.transcribe(audio_data)
            if not transcript.text:
                raise ValueError("Empty transcription from STT.")
            user_text = transcript.text
        except Exception as e:
            return {
                "transcription": "",
                "llm_response": "I'm having trouble hearing you right now.",
                "audio_url": FALLBACK_AUDIO_URL
            }

        # Step 3: Initialize chat history
        if session_id not in chat_histories:
            chat_histories[session_id] = []
        chat_histories[session_id].append({"role": "user", "content": user_text})

        # Step 4: LLM (Gemini)
        try:
            conversation_text = "\n".join(
                f"{msg['role'].capitalize()}: {msg['content']}"
                for msg in chat_histories[session_id]
            )
            model = genai.GenerativeModel("gemini-2.5-flash")
            llm_response = model.generate_content(conversation_text)
            llm_text = llm_response.text
        except Exception as e:
            return {
                "transcription": user_text,
                "llm_response": "I'm having trouble thinking right now.",
                "audio_url": FALLBACK_AUDIO_URL
            }

        chat_histories[session_id].append({"role": "assistant", "content": llm_text})

        # Step 5: TTS (Murf)
        try:
            headers = {
                "api-key": MURF_API_KEY,
                "Content-Type": "application/json"
            }
            payload = {
                "voice_id": "it-IT-giorgio",
                "style": "Narration",
                "multiNativeLocale": "en-US",
                "text": llm_text,
            }
            murf_res = requests.post(
                "https://api.murf.ai/v1/speech/generate",
                json=payload,
                headers=headers,
                timeout=10
            )
            if murf_res.status_code == 200:
                audio_url = murf_res.json().get("audioFile")
            else:
                raise ValueError(f"Murf API error: {murf_res.text}")
        except Exception as e:
            audio_url = FALLBACK_AUDIO_URL

        # Step 6: Return final result
        return {
            "transcription": user_text,
            "llm_response": llm_text,
            "audio_url": audio_url
        }

    except Exception as e:
        # Major failure catch-all
        return {
            "error": str(e),
            "llm_response": "Something went wrong. Please try again later.",
            "audio_url": FALLBACK_AUDIO_URL
        }
