# 🧠 JARVIS AI Voice Agent (Python)

An **AI-powered, voice-interactive assistant** inspired by Marvel's *Iron Man* movies. This real-time system is built in **Python**, using:

* **LiveKit** for audio/video session management (via WebRTC)
* **Deepgram** for real-time **speech-to-text (STT)**
* **Large Language Models (LLMs)** for AI reasoning (e.g., OpenAI or Gemini Realtime for multimodal support)
* **Cartesia TTS** for natural, responsive **text-to-speech (TTS)**

---

## ⚙️ Key Features

* 🎙️ **Conversational Voice Interface**
* 🔁 **Real-Time Streaming via LiveKit**
* 🧠 **LLM-Driven Reasoning** (Text or Vision-Language)
* 📹 **Video Input Support** (via Gemini Realtime)
* 🔊 **Instant AI Speech Responses with Cartesia**

---

## 🛠️ System Architecture

<img width="747" height="151" alt="image" src="https://github.com/user-attachments/assets/c4450e0f-90ad-4381-9b6d-6c561c374a4f" />



---

## 📦 Tech Stack

| Component          | Technology                               |
| ------------------ | ---------------------------------------- |
| Language           | Python 3.9+                              |
| STT                | [Deepgram](https://deepgram.com)         |
| LLM                | OpenAI / Gemini / Local                  |
| TTS                | [Cartesia](https://cartesia.ai)          |
| Session Manager    | [LiveKit](https://livekit.io)            |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/JARVIS-AI.git
cd JARVIS-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
LIVEKIT_API_KEY=your_livekit_key
LIVEKIT_API_SECRET=your_livekit_secret
DEEPGRAM_API_KEY=your_deepgram_key
LLM_API_KEY=your_openai_or_gemini_key
CARTESIA_API_KEY=your_cartesia_key
```

---

## 🧪 Run the App

```bash
python main.py
```

Make sure your microphone is enabled and accessible.

---

## 🧠 Supported Modes

| Mode               | Description                                        |
| ------------------ | -------------------------------------------------- |
| 🎤 Voice Mode      | Continuous STT and response loop                   |
| 📹 Multimodal Mode | Feed video frames to Gemini Realtime               |
| 🧑‍💻 CLI Mode     | Text-only fallback interface for testing/debugging |
| 🎧 Audio Out       | Low-latency TTS responses using Cartesia           |

---

---

## 📹 Gemini Realtime: Video Support (Optional)

If you enable video input:

* Capture webcam frames (e.g., via OpenCV)
* Send to Gemini Realtime endpoint
* Process vision + language context in unified model

---

## 📌 Notes

* **Low Latency**: Optimized for real-time audio feedback (< 300ms round-trip)
* **Modular**: Easily swap LLMs or TTS engines

---

## 🧰 Development Notes

* STT and TTS use streaming endpoints for lowest latency.
* LLM requests can use asyncio to maintain responsiveness.
* LiveKit handles multiple peer sessions — useful for shared agents or public demos.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for more info.

---

## 📣 Credits

* Voice: [Deepgram](https://deepgram.com)
* AI: OpenAI / Gemini
* Voice Out: [Cartesia](https://cartesia.ai)
* Streaming: [LiveKit](https://livekit.io)
* Inspired by: *J.A.R.V.I.S. – Just A Rather Very Intelligent System*
