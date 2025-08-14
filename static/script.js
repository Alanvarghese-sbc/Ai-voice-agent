document.addEventListener("DOMContentLoaded", () => {
  // Unique session per page load
  let sessionId = crypto.randomUUID();

  // DOM references
  const recordBtn = document.getElementById("recordBtn");
  const audioPlayback = document.getElementById("audioPlayback");
  const transcriptionResult = document.getElementById("transcriptionResult");

  // Recording state
  let recording = false;
  let mediaRecorder;
  let recordedChunks = [];
  let audioStream = null;

  // =====================
  // RECORD BUTTON HANDLER
  // =====================
  recordBtn.addEventListener("click", async () => {
    if (!recording) {
      // Start recording
      recordedChunks = [];
      try {
        audioStream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(audioStream, { mimeType: "audio/webm" });

        mediaRecorder.ondataavailable = (e) => {
          if (e.data.size > 0) recordedChunks.push(e.data);
        };

        mediaRecorder.onstop = () => {
          stopAllTracks(audioStream);
          const audioBlob = new Blob(recordedChunks, { type: "audio/webm" });
          sendForTranscription(audioBlob);
        };

        mediaRecorder.start();
        recording = true;
        recordBtn.textContent = "⏹️ Stop Recording";
        recordBtn.classList.add("recording"); // for animation
      } catch (err) {
        alert("Microphone access denied or unavailable.");
        console.error(err);
      }
    } else {
      // Stop recording
      mediaRecorder.stop();
      recording = false;
      recordBtn.textContent = "🎙️ Start Recording";
      recordBtn.classList.remove("recording");
    }
  });

  // Stop all tracks utility
  function stopAllTracks(stream) {
    if (stream) stream.getTracks().forEach((track) => track.stop());
  }

  // =====================
  // PLAY AUDIO UTILITY
  // =====================
  function playAudioFromUrl(url) {
    audioPlayback.src = url;
    audioPlayback.style.display = "none"; // hide player
    audioPlayback.load();
    audioPlayback.play().catch((err) => console.warn(err));

    audioPlayback.onended = () => {
      recordBtn.click(); // auto start recording after bot speaks
    };
  }

  // =====================
  // SEND AUDIO TO SERVER
  // =====================
  async function sendForTranscription(audioBlob) {
    const formData = new FormData();
    formData.append("file", audioBlob, "recording.webm");

    try {
      const response = await fetch(`http://127.0.0.1:8000/agent/chat/${sessionId}`, {
        method: "POST",
        body: formData,
      });

      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const result = await response.json();

      transcriptionResult.value += `\nYou: ${result.transcription || "[Transcription failed]"}\nBot: ${result.llm_response || "No response"}\n`;
      transcriptionResult.scrollTop = transcriptionResult.scrollHeight;

      const audioUrl = result.audio_url || "/static/fallback.mp3";
      playAudioFromUrl(audioUrl);
    } catch (err) {
      console.error("Error calling /agent/chat:", err);
      transcriptionResult.value += "\n[Error contacting server]\n";
      playAudioFromUrl("/static/fallback.mp3");
    }
  }
});
