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

| Component       | Technology                       |
| --------------- | -------------------------------- |
| Language        | Python 3.9+                      |
| STT             | [Deepgram](https://deepgram.com) |
| LLM             | OpenAI / Gemini / Local          |
| TTS             | [Cartesia](https://cartesia.ai)  |
| Session Manager | [LiveKit](https://livekit.io)    |

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

```
LIVEKIT_API_KEY=your_livekit_key  
LIVEKIT_API_SECRET=your_livekit_secret  
DEEPGRAM_API_KEY=your_deepgram_key  
LLM_API_KEY=your_openai_or_gemini_key  
CARTESIA_API_KEY=your_cartesia_key  
```

---

## 🧪 Run the App

```bash
python agent.py console
```

or via LiveKit playground (for Video Input)

```bash
python agent.py dev
```

Make sure your microphone is enabled and accessible.

---

## 🧠 Supported Modes

| Mode           | Description                                        |
| -------------- | -------------------------------------------------- |
| 🎤 Voice Mode  | Continuous STT and response loop                   |
| 📹 Multimodal  | Feed video frames to Gemini Realtime               |
| 🧑‍💻 CLI Mode | Text-only fallback interface for testing/debugging |
| 🎧 Audio Out   | Low-latency TTS responses using Cartesia           |

---

## 🧩 Function Calling with Tools

JARVIS supports **function tools**, enabling the system to interact with **real-world APIs** and retrieve **up-to-date information** dynamically during conversations. These tools are invoked automatically by the LLM to enhance responses with real-time data.

### ✅ Supported Tools

| Tool Type       | Description                                               |
| --------------- | --------------------------------------------------------- |
| 🌦️ Weather API | Get current weather based on location (e.g., OpenWeather) |
| 🔍 Web Search   | Perform real-time queries using web search APIs           |
| 📅 Calendar API | Access events or manage scheduling *(optional)*           |
| 🧾 Custom APIs  | Easily extendable to support any HTTP-based APIs          |

### 🔄 How It Works

1. User prompt triggers a query (e.g., *"What's the weather in Tokyo?"*)
2. The LLM detects intent and chooses an appropriate function tool
3. Function is executed via a defined schema
4. The result is parsed and included in the LLM’s response
5. **Cartesia TTS** speaks the final enriched answer

### 🧠 Example Interaction

```
User: What's the temperature in New York right now?  
JARVIS (calls weather API):  
JARVIS (spoken): The current temperature in New York is 82°F with clear skies.
```

---

## 📹 Gemini Realtime: Video Support (Optional)

If you enable video input:

* Capture webcam frames (e.g., via OpenCV)
* Send to Gemini Realtime endpoint
* Process vision + language context in a unified model

---

## 📌 Notes

* ⚡ **Low Latency**: Optimized for sub-300ms audio feedback
* 🔧 **Modular**: Easily swap LLMs, TTS, or tool plugins

---

## 🧰 Development Notes

* STT and TTS use streaming endpoints for lowest latency
* LiveKit handles multiple peer sessions — ideal for shared or public agents

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for more info.

---

## 📣 Credits

* Voice Recognition: [Deepgram](https://deepgram.com)
* AI Reasoning: OpenAI / Gemini
* Voice Output: [Cartesia](https://cartesia.ai)
* Streaming Infra: [LiveKit](https://livekit.io)
* Inspiration: *J.A.R.V.I.S. – Just A Rather Very Intelligent System*
