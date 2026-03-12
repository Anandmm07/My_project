# Conversational Image recognition Chatbot

An AI-powered web app that lets you **upload an image, ask questions about it, and even use your voice for input**.  
Responses are contextual and powered by **Google Gemini Vision**.

---

## 📸 Overview
This is an interactive multimodal chatbot where you can:

- Upload any image (JPG, PNG, etc.)
- Ask natural language questions about the image
- Use **voice input** 🎤 for prompts
- Get AI-generated answers in real-time
- Continue chatting with **context preserved**
- Export your chat history for later use

It combines **computer vision** with **conversational AI** to make image understanding seamless and interactive.

---

## 🚀 Features

- 📤 **Drag & Drop Upload**: Quickly load your image into the app  
- 📝 **Prompt-Based Interaction**: Ask the AI anything about the uploaded image  
- 🎙️ **Voice Input**: Speak your prompts (via Web Speech API in Chrome/Edge)  
- 💬 **Chat History Context**: Keeps the conversation relevant to the current image  
- 📥 **Export History**: Save conversations as JSON  
- 🔄 **Reset Sessions**: Start fresh anytime  
- 📱 **Responsive UI**: Works on desktop and mobile devices  
- ⚡ **Powered by Gemini Vision**: State-of-the-art multimodal AI  

---

## 🛠️ Project Structure

```

pscs\_256/
├── app.py           # Flask backend serving the app and handling API calls
├── static/
│   ├── styles.css   # UI styles
│   └── script.js    # Frontend logic (chat + voice input)
└── templates/
└── index.html   # Frontend UI template

````

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Adithya140/pscs_256.git
cd pscs_256
````

### 2️⃣ Set up a Python environment

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install flask google-generativeai python-dotenv
```

---

## 🔑 API Key Setup

This app uses **Google Generative AI (Gemini Vision)**. You’ll need to:

1. Get an API key from [Google AI Studio](https://makersuite.google.com/app/apikey).
2. Store it as an environment variable:

```bash
# Mac/Linux
export GOOGLE_API_KEY="your_api_key"

# Windows (cmd)
set GOOGLE_API_KEY="your_api_key"

# Windows (PowerShell)
$env:GOOGLE_API_KEY="your_api_key"
```

---

## ▶️ Running the App

```bash
python app.py
```

By default, the app will be available at:
👉 **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 💡 Usage

1. Open the app in your browser.
2. Drag and drop or select an image to upload.
3. Enter your prompt/question in the text box **or click 🎙️ to use voice**.
4. Click 🚀 **Start Conversation**.
5. Continue chatting — the AI remembers the image and your previous questions.
6. Export your chat history anytime.

---

## 📷 Example Use Cases

* Identify objects, text, or scenes in an image
* Ask for detailed descriptions or summaries
* Compare elements within an image
* Generate captions or creative interpretations
* Hands-free interaction via **voice prompts**

---

## 🙌 Credits

* **Backend**: Flask
* **Frontend**: HTML, CSS, JavaScript
* **Voice Input**: Web Speech API
* **AI Model**: Google Gemini Vision

---
