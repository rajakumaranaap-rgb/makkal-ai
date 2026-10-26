# 🏛️ Makkal AI (மக்கள் AI)
### *Bridging the Digital Divide for 75 Million Citizens of Tamil Nadu with Meta AI*

[![Meta AI Hackathon 2026](https://img.shields.io/badge/Meta%20AI-Hackathon%202026-0668E1?style=for-the-badge&logo=meta&logoColor=white)](https://dev.meta.ai)
[![Meta Model API](https://img.shields.io/badge/Powered%20By-Meta%20Muse%20%26%20SAM%202-0081FB?style=for-the-badge&logo=meta&logoColor=white)](https://dev.meta.ai)
[![Tamil Nadu e-Governance](https://img.shields.io/badge/Focus-Tamil%20Nadu%20e--Sevai-059669?style=for-the-badge)](https://tnesevai.tn.gov.in)
[![Indie Developer Track](https://img.shields.io/badge/Track-Indie%20Dev%20Solo-8B5CF6?style=for-the-badge)](https://github.com/rajakumaranaap-rgb/makkal-ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## 📖 The Story Behind Makkal AI: Why I Built This

I grew up in Tamil Nadu, watching my uncle, elderly neighbors, and daily-wage workers travel hours by bus to the local Taluk and Collectorate offices. 

They weren't looking for favours. They just needed a basic document—a **Patta/Chitta** land record to apply for a small crop loan, a **Community Certificate** for their child's college admission, or adding a newborn baby’s name to their **TNPDS Smart Ration Card**.

On paper, the Tamil Nadu government has done phenomenal work digitizing over 200+ public services on portals like *TNeGA e-Sevai*, *Any-ROR*, and *TNPDS*. **In reality, there is a giant invisible wall:**
- Complex English and bureaucratic legal Tamil menus.
- Confusing CAPTCHA codes and dropdown lists with hundreds of survey sub-divisions.
- Exploitation by local internet broker kiosks charging ₹300 to ₹1,500 for services that are legally free or cost ₹60.

> *"If a grandmother in a village cannot get her health insurance or land certificate without begging a middleman, technology has failed her."*

When Meta announced the **Meta AI Hackathon 2026** and opened the **Meta Model API (Muse & SAM 2)**, I realized we finally had the tools to solve this permanently. 

**Makkal AI (மக்கள் AI)** is a voice-first, vision-verified, bilingual citizen companion. You don't need to know how to use a computer. You just open your phone and talk or snap a photo in your natural mother tongue—**மரியாதையான எளிய தமிழ் (respectful, everyday Tamil)**.

---

## ✨ What Makes Makkal AI Different?

```
┌────────────────────────────────────────────────────────────────────────┐
│                        TRADITIONAL CITIZEN EXPERIENCE                  │
│                                                                        │
│   Citizen ──> Travel to Town ──> Broker Kiosk ──> Pays ₹1,000 ──> Error│
└────────────────────────────────────────────────────────────────────────┘
                                    VS
┌────────────────────────────────────────────────────────────────────────┐
│                           MAKKAL AI EXPERIENCE                         │
│                                                                        │
│   Citizen ──> "பட்டா சிட்டா எடுக்கணும்" ──> Makkal AI ──> Free & Instant │
│               (Voice in Tamil)          (Meta Muse + SAM 2)            │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Voice-First Accessibility (`muse-voice-transcribe-1.0`):**
   Senior citizens and illiterate workers don't need to type. They send voice notes in colloquial Tamil dialects (*மதுரை, கோவை, நெல்லை, சென்னை தமிழ்*), and Makkal AI speaks back warmly.
2. **Visual Document Verification with SAM 2 (`sam-3.1`):**
   Citizens snap photos of wrinkled birth certificates, electricity receipts, or revenue seals on their bed or table. Meta’s **SAM 2** segments and crops the clean document, isolating seals and signatures from camera glare and background clutter.
3. **Deep Reasoning & Eligibility Gate (`muse-wonder-1.0`):**
   Before submitting an application, Meta’s deep reasoning model checks age criteria, income limits, and missing certificates so applications are **never rejected** at the VAO desk.
4. **Zero Middlemen, 100% Transparency:**
   Direct guidance to official government URLs with exact statutory fees (e.g. *"அரசு கட்டணம் ₹60 மட்டுமே, தரகர்களுக்கு பணம் கொடுக்காதீர்கள்!"*).

---

## 🧠 Powered by Meta AI Stack (Direct `dev.meta.ai` Integration)

Makkal AI directly utilizes **4 distinct flagship models** from Meta's Model API:

| Meta Model | Role in Makkal AI | Practical Impact |
| :--- | :--- | :--- |
| **`muse-spark-1.3`** | Core Conversational Agent | Instant, high-speed, bilingual reasoning in colloquial Tamil & English. |
| **`muse-wonder-1.0`** | Deep Policy & Eligibility Reasoning | Multi-step validation of government scheme rules (e.g., KMUT ₹1,000 criteria). |
| **`sam-3.1`** | Segment Anything Model (SAM 2) | Auto-crops skewed document borders, highlights official seals and QR codes. |
| **`muse-voice-transcribe-1.0`** | Regional Voice Transcription | Transcribes raw Tamil audio voice notes with high dialect accuracy. |

---

## 🏛️ Supported Public Digital Services

Makkal AI includes authoritative, pre-verified knowledge for top Tamil Nadu public services:

- **📜 நில ஆவணங்கள் (Land Records):** Any-ROR Patta & Chitta instant free download by Survey No or Patta No.
- **👶 குடும்ப அட்டை (TNPDS Ration Card):** Add newborn baby, add family member, surrender certificate verification.
- **🏷️ சாதிச் சான்றிதழ் (Community Certificate):** e-Sevai revenue application guidelines, parental certificate verification.
- **💼 வருமானச் சான்றிதழ் (Income Certificate):** Annual family income declaration criteria & VAO enquiry process.
- **⚡ மின் நுகர்வோர் சேவை (TANGEDCO EB):** Consumer number linking, 100 units free calculation, Quick Pay bill direct link.
- **🏥 முதலமைச்சர் மருத்துவ காப்பீடு (CMCHIS):** ₹5 Lakhs free cashless hospital treatment eligibility and smart card issuance.
- **💰 கலைஞர் மகளிர் உரிமைத் திட்டம் (KMUT):** ₹1,000 monthly entitlement verification and bank passbook requirements.

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    User(["👤 Tamil Nadu Citizen (Mobile / Desktop)"])
    
    subgraph Frontend ["Front-End Layer"]
        WebUI["📱 Mobile-First Tamil Web Interface (Tailwind + HTML5)"]
        WAChat["💬 WhatsApp Business Interface (Meta Cloud API)"]
    end
    
    subgraph Backend ["FastAPI Gateway Orchestrator"]
        Router["API Gateway (/api/chat, /api/verify-doc, /api/services)"]
        ContextEngine["Tamil Nadu e-Sevai Knowledge Engine"]
    end
    
    subgraph Meta_AI_Cloud ["Meta Model API (dev.meta.ai)"]
        MuseSpark["⚡ muse-spark-1.3 (Tamil Dialogue)"]
        MuseWonder["🧠 muse-wonder-1.0 (Deep Policy Reasoning)"]
        SAM2["🎯 sam-3.1 (Segment Anything Document Isolation)"]
        MuseVoice["🎙️ muse-voice-transcribe-1.0 (Voice Ingestion)"]
    end
    
    User <--> WebUI
    User <--> WAChat
    WebUI <--> Router
    WAChat <--> Router
    Router <--> ContextEngine
    ContextEngine <--> MuseSpark
    ContextEngine <--> MuseWonder
    Router <--> SAM2
    Router <--> MuseVoice
```

---

## 🚀 Quick Start (Run Locally in 2 Minutes)

### 1. Prerequisites
- Python 3.10, 3.11, or 3.12
- A Meta Model API Key from [dev.meta.ai/api-keys](https://dev.meta.ai/api-keys)

### 2. Clone the Repository
```bash
git clone https://github.com/rajakumaranaap-rgb/makkal-ai.git
cd makkal-ai
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Your API Key
Copy `.env.example` to `.env` and add your Meta Model API key:
```bash
cp .env.example .env
```
Edit `.env`:
```env
META_MODEL_API_KEY=LLM_your_secret_meta_api_key_here
META_API_BASE=https://api.meta.ai/v1
DEFAULT_CHAT_MODEL=muse-spark-1.3
REASONING_MODEL=muse-wonder-1.0
```

### 5. Launch Makkal AI
**Windows (One-Click):**
Double-click `start_makkal_ai.bat`

**Or via Terminal:**
```bash
python -m uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

Open your browser at **[http://127.0.0.1:8000](http://127.0.0.1:8000)** and start chatting in Tamil!

---

## 💬 Sample Real-World Conversations

### Example 1: Adding a Newborn Baby to Ration Card
> **Citizen (Tamil):** *"எங்க வீட்டுல புதுசா பாப்பா பொறந்திருக்கு. ரேஷன் கார்டுல பேர் சேர்க்க என்னென்ன வேணும் தம்பி?"*
>
> **Makkal AI:**
> *"வாழ்த்துகள்! உங்கள் குழந்தையின் பெயரை குடும்ப அட்டையில் (Ration Card) ஆன்லைனிலேயே சுலபமாக சேர்க்கலாம்.*
> 
> **தேவையான ஆவணங்கள்:**
> 1. நகராட்சி/பஞ்சாயத்து வழங்கிய குழந்தையின் பிறப்புச் சான்றிதழ் (Birth Certificate).
> 2. பெற்றோரின் ஆதார் அட்டை நகல்.
> 3. தற்போதைய ஸ்மார்ட் குடும்ப அட்டை.
>
> **அரசு கட்டணம்:** முற்றிலும் இலவசம் (Free).  
> **அதிகாரப்பூர்வ தளம்:** [tnpds.gov.in](https://tnpds.gov.in)
>
> *TNPDS இணையதளத்தில் உங்கள் பதிவு செய்யப்பட்ட மொபைல் எண்ணை உள்ளிட்டு OTP மூலம் லாகின் செய்து, 'உறுப்பினர் சேர்க்க' பகுதியில் பிறப்புச் சான்றிதழை பதிவேற்றினால் போதும். வட்ட வழங்கல் அலுவலர் (TSO) ஒப்புதல் அளித்தவுடன் பெயர் சேர்க்கப்பட்டுவிடும்!"*

---

## 📁 Repository Structure

```text
makkal-ai/
├── app.py                  # FastAPI backend & embedded mobile-first Tamil Web UI
├── meta_client.py          # Unified client for Meta Muse, SAM 2, and Voice APIs
├── knowledge_base.py       # Authoritative Tamil Nadu e-Governance rules & service catalog
├── start_makkal_ai.bat     # Windows one-click desktop launcher
├── requirements.txt        # Lightweight production dependencies
├── .env.example            # Environment configuration template
├── .gitignore              # Strict secret and cache exclusions
└── README.md               # Complete project documentation & story
```

---

## 🏆 Hackathon Evaluation Alignment

| Judging Criteria | How Makkal AI Excels |
| :--- | :--- |
| **Technical Innovation (30%)** | Combines 4 official Meta Model APIs (`muse-spark-1.3`, `muse-wonder-1.0`, `sam-3.1`, `muse-voice-transcribe-1.0`) into an asynchronous, low-latency architecture. |
| **Real-World Impact (25%)** | Directly addresses digital exclusion, language barriers, and corruption for 75+ million people in Tamil Nadu. |
| **Completeness & Polish (25%)** | Fully working live prototype with interactive Tamil Web UI, zero mock responses, and pre-verified government data. |
| **Indie Dev Feasibility (20%)** | Built with clean modular Python, minimal dependencies, and cost-efficient execution within Meta's free credit tier. |

---

## 🧑‍💻 Author & Acknowledgements
- **Developer:** Raja Kumar ([@rajakumaranaap-rgb](https://github.com/rajakumaranaap-rgb))
- **Track:** Indie Developer Solo
- **Competition:** Meta AI Hackathon 2026
- **Technology Partner:** Meta AI Platform ([dev.meta.ai](https://dev.meta.ai))

*Dedicated to every ordinary citizen of Tamil Nadu striving for a transparent, accessible digital future.* 🌾🏛️
