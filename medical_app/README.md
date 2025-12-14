🩺 Medical Image Analysis App (Qwen + Bytez + Streamlit)
🔍 Project Overview

Ye project ek AI-powered medical image analysis web app hai, jo users ko medical images upload karne deta hai aur AI ke through structured medical-style analysis generate karta hai.

App Streamlit par bana hai aur Qwen/Qwen3-4B-Instruct-2507 language model ko Bytez API ke through use karta hai.

⚠️ Ye app educational aur demonstration purpose ke liye hai, real medical diagnosis ke liye nahi.

---

🎯 Project Objective

   - To enable easy uploading of medical images
   - To generate medical-style reports using AI
   - To demonstrate real-world integration of modern AI models
   - To follow secure API usage and maintain a clean project architecture


🧱 Project Architecture :- 
      User uploads image
            ↓
      Streamlit UI (app.py)
            ↓
      Prompt + image metadata
            ↓
      Qwen AI Model (via Bytez API)
            ↓
      Structured medical-style text output
            ↓
      Displayed to user
 

## 🚀 Features

- 📸 Upload medical images (X-ray, MRI, CT, etc.)
- 🧠 AI-powered image analysis using **Qwen 3 (4B)**
- ⚡ Fast inference via **Bytez API**
- 🎨 Clean and simple **Streamlit UI**
- 🔐 Secure API key handling using `.env`

---

## 🧱 Project Structure

medical_app/
│
├── app.py                # Streamlit UI logic
├── requirements.txt      # Python dependencies
├── .env                  # API key (local only)
│
├── models/
│   ├── __init__.py       # Makes folder a package
│   └── bytez_qwen.py     # Qwen + Bytez integration
│
└── README.md


🛠️ Tech Stack Used

🔹 Frontend / UI
   - Streamlit
   - Image upload
   - Button click
   - Output display

🔹 Backend / AI
   - Qwen/Qwen3-4B-Instruct-2507
   - Large Language Model (Text-based)
   - Bytez SDK
   - Connects app to Qwen model

🔹 Other Tools
   - Python
   - Pillow (PIL) – image handling
   - python-dotenv – secure API key handling



## 🔑 Environment Variables

Create a '.env' file in the root folder:

```env
BYTEZ_API_KEY=your_bytez_api_key_here


🧠 How the App Works (Step-by-Step)

1️⃣ Image Upload
   -User uploads a medical image (JPG / PNG) using Streamlit’s file uploader.

2️⃣ Image Display
   -The uploaded image is displayed back to the user using Pillow.

3️⃣ Prompt Creation
The app does not directly analyze image pixels
(because Qwen is a text-only model).

Instead:
   -Image metadata (type, resolution)

   -Medical context
   are used to create a structured prompt.

4️⃣ AI Processing (Qwen via Bytez)
Prompt is sent to Qwen model using Bytez SDK:
The model generates:
   - Possible imaging modality
   - Common findings
   - Example abnormalities
   - Patient-friendly explanation
   - Medical disclaimer

5️⃣ Output Display
AI-generated medical-style report is shown on the UI.

---

🔐 API Key Security
   - API key is stored in .env file
   - Loaded using python-dotenv
   - Never hard-coded
   - Not pushed to GitHub
   - Streamlit Cloud uses Secrets Manager"# medical-AI-Image-Analyzer" 
"# Medical-AI-Image-Analyzer" 
