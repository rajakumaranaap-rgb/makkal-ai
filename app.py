"""
Makkal AI (மக்கள் AI) - FastAPI Server & Interactive Web UI
Powered by Meta Model API (Muse & SAM 2)
"""

import os
import json
from pathlib import Path
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

from meta_client import meta_client, DEFAULT_CHAT_MODEL, REASONING_MODEL
from knowledge_base import SERVICES_CATALOG, get_service_info

app = FastAPI(
    title="Makkal AI (மக்கள் AI)",
    description="Voice & Vision Digital Citizen Services for Tamil Nadu powered by Meta Model API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SYSTEM_PROMPT = """
You are 'Makkal AI' (மக்கள் AI), an intelligent, compassionate, and highly authoritative Digital Citizen Assistant for the state of Tamil Nadu, India.
Your mission is to empower citizens (farmers, daily wage workers, students, senior citizens, and families) to navigate government portals effortlessly.

Guidelines:
1. Always respond in natural, friendly, respectful colloquial Tamil (மரியாதையான எளிய தமிழ்). If the user asks in English, reply in bilingual Tamil & English.
2. Provide exact, actionable advice:
   - எளிய விளக்கம் (Simple summary in 1-2 lines)
   - தேவையான ஆவணங்கள் (Clear bulleted list of required documents)
   - அரசு கட்டணம் & கால அளவு (Official government fee & delivery timeframe)
   - அதிகாரப்பூர்வ இணையதளம் (Official government portal link)
3. Never invent fake rules or fees. Always protect citizens from paying excess broker/middleman charges.
4. Keep tone warm, patient, and empowering (like a trusted village administrative friend / VAO தோழன்).
"""


class ChatRequest(BaseModel):
    message: str
    history: Optional[List[dict]] = []
    use_deep_reasoning: Optional[bool] = False


@app.get("/api/services")
async def list_services():
    """Returns catalog of all supported Tamil Nadu digital public services."""
    return {"status": "success", "count": len(SERVICES_CATALOG), "services": SERVICES_CATALOG}


@app.post("/api/chat")
async def chat_endpoint(req: ChatRequest):
    """
    Core conversational service endpoint powered by Meta muse-spark-1.3 or muse-wonder-1.0.
    Injects Tamil Nadu e-Governance knowledge context into Meta's prompt.
    """
    try:
        user_msg = req.message.strip()
        if not user_msg:
            raise HTTPException(status_code=400, detail="Message cannot be empty.")

        # 1. Fetch relevant service knowledge
        matched_services = get_service_info(user_msg)
        kb_context = json.dumps(matched_services, ensure_ascii=False, indent=2)

        # 2. Build conversation with context injection
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT + f"\n\n[OFFICIAL TAMIL NADU E-GOVERNANCE CONTEXT]:\n{kb_context}"}
        ]
        
        # Include history if any
        if req.history:
            messages.extend(req.history[-6:])  # Keep last 3 turns
            
        messages.append({"role": "user", "content": user_msg})

        # 3. Call Meta Model API
        target_model = REASONING_MODEL if req.use_deep_reasoning else DEFAULT_CHAT_MODEL
        res = meta_client.chat_completion(messages=messages, model=target_model)
        reply_text = res["choices"][0]["message"]["content"]

        return {
            "status": "success",
            "model_used": target_model,
            "reply": reply_text,
            "matched_services": [s["title_ta"] for s in matched_services]
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})


@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    """Interactive, mobile-first Tamil Citizen Chat & Service Portal."""
    html_content = """
<!DOCTYPE html>
<html lang="ta">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Makkal AI (மக்கள் AI) - Tamil Nadu Citizen Services</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Mukta+Malar:wght@400;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Mukta Malar', 'Inter', sans-serif; }
        .markdown-body h1, .markdown-body h2, .markdown-body h3 {
            font-weight: 700;
            color: #34d399;
            margin-top: 0.75rem;
            margin-bottom: 0.35rem;
            font-size: 1.05rem;
        }
        .markdown-body h1 { font-size: 1.2rem; }
        .markdown-body p { margin-bottom: 0.6rem; line-height: 1.6; }
        .markdown-body ul, .markdown-body ol {
            margin-left: 1.25rem;
            margin-bottom: 0.6rem;
            list-style-type: disc;
        }
        .markdown-body ol { list-style-type: decimal; }
        .markdown-body li { margin-bottom: 0.25rem; }
        .markdown-body a {
            color: #38bdf8;
            text-decoration: underline;
            font-weight: 500;
        }
        .markdown-body strong { color: #f1f5f9; font-weight: 600; }
        .markdown-body blockquote {
            border-left: 3px solid #10b981;
            padding-left: 0.75rem;
            color: #cbd5e1;
            background: rgba(16, 185, 129, 0.08);
            border-radius: 0 0.5rem 0.5rem 0;
            margin: 0.5rem 0;
            padding-top: 0.25rem;
            padding-bottom: 0.25rem;
        }
        .markdown-body hr {
            border: 0;
            border-top: 1px solid #334155;
            margin: 0.75rem 0;
        }
    </style>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen flex flex-col items-center justify-between p-2 sm:p-4">

    <!-- Header -->
    <header class="w-full max-w-2xl bg-slate-800/80 backdrop-blur-md border border-slate-700/80 rounded-2xl p-4 mb-3 shadow-xl flex items-center justify-between">
        <div class="flex items-center space-x-3">
            <div class="w-12 h-12 rounded-xl bg-gradient-to-tr from-emerald-500 to-teal-400 flex items-center justify-center text-2xl shadow-lg shadow-emerald-500/20">
                🏛️
            </div>
            <div>
                <h1 class="text-xl font-bold bg-gradient-to-r from-emerald-400 to-teal-200 bg-clip-text text-transparent">மக்கள் AI (Makkal AI)</h1>
                <p class="text-xs text-slate-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                    Powered by Meta Model API (Muse & SAM 2)
                </p>
            </div>
        </div>
        <div class="text-right">
            <span class="text-xs bg-emerald-500/10 text-emerald-300 border border-emerald-500/30 px-2.5 py-1 rounded-full font-medium">தமிழ்நாடு e-Sevai</span>
        </div>
    </header>

    <!-- Quick Service Badges -->
    <div class="w-full max-w-2xl flex gap-2 overflow-x-auto pb-2 scrollbar-none text-xs">
        <button onclick="sendQuickPrompt('பட்டா சிட்டா நில ஆவணம் எப்படி எடுப்பது?')" class="whitespace-nowrap bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 px-3 py-1.5 rounded-full transition shadow-sm">📜 பட்டா / சிட்டா</button>
        <button onclick="sendQuickPrompt('ரேஷன் கார்டில் குழந்தை பெயர் சேர்க்க தேவையானவை என்ன?')" class="whitespace-nowrap bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 px-3 py-1.5 rounded-full transition shadow-sm">👶 ரேஷன் பெயர் சேர்க்க</button>
        <button onclick="sendQuickPrompt('சாதி சான்றிதழ் ஆன்லைனில் விண்ணப்பிப்பது எப்படி?')" class="whitespace-nowrap bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 px-3 py-1.5 rounded-full transition shadow-sm">🏷️ சாதி சான்றிதழ்</button>
        <button onclick="sendQuickPrompt('கலைஞர் மகளிர் உரிமைத் திட்டம் 1000 ரூபாய் தகுதி என்ன?')" class="whitespace-nowrap bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 px-3 py-1.5 rounded-full transition shadow-sm">💰 மகளிர் உரிமை ₹1,000</button>
        <button onclick="sendQuickPrompt('முதலமைச்சரின் 5 லட்சம் இலவச மருத்துவ காப்பீடு அட்டை எப்படி பெறுவது?')" class="whitespace-nowrap bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 px-3 py-1.5 rounded-full transition shadow-sm">🏥 CMCHIS மருத்துவ அட்டை</button>
    </div>

    <!-- Chat Message Container -->
    <main id="chatBox" class="w-full max-w-2xl flex-1 bg-slate-800/40 border border-slate-700/60 rounded-2xl p-4 overflow-y-auto space-y-4 my-2 shadow-inner">
        <!-- Welcome Message -->
        <div class="flex items-start space-x-3">
            <div class="w-8 h-8 rounded-lg bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-sm">
                🏛️
            </div>
            <div class="bg-slate-800 border border-slate-700/80 rounded-2xl rounded-tl-none p-3.5 max-w-[85%] text-slate-200 text-sm leading-relaxed shadow-md">
                <p class="font-semibold text-emerald-400 mb-1">வணக்கம்! நான் மக்கள் AI (Makkal AI).</p>
                <p>தமிழ்நாடு அரசு இ-சேவை (e-Sevai), பட்டா/சிட்டா நில ஆவணங்கள், ரேஷன் கார்டு, சாதி/வருமான சான்றிதழ்கள் மற்றும் நலத்திட்டங்கள் பற்றி உங்களுக்கு என்ன உதவி வேண்டும்? கீழே கேளுங்கள்!</p>
            </div>
        </div>
    </main>

    <!-- Input Footer -->
    <div class="w-full max-w-2xl px-2 py-1 flex items-center justify-between text-xs text-slate-400">
        <label class="flex items-center space-x-2 cursor-pointer select-none hover:text-emerald-300 transition">
            <input type="checkbox" id="reasoningToggle" class="rounded bg-slate-800 border-slate-700 text-emerald-500 focus:ring-0 accent-emerald-500">
            <span>🧠 ஆழ்ந்த கொள்கை ஆய்வு (muse-wonder-1.0 Deep Reasoning)</span>
        </label>
        <span class="text-[11px] text-slate-400">Meta Model API</span>
    </div>
    <footer class="w-full max-w-2xl bg-slate-800/80 backdrop-blur-md border border-slate-700/80 rounded-2xl p-2.5 shadow-xl flex items-center space-x-2">
        <input id="userInput" type="text" placeholder="உங்கள் கேள்வியை தமிழில் அல்லது ஆங்கிலத்தில் கேட்கவும்..." 
               class="flex-1 bg-slate-900/90 border border-slate-700 text-slate-100 placeholder-slate-500 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 transition"
               onkeypress="handleKeyPress(event)">
        <button id="sendBtn" onclick="sendMessage()" 
                class="bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-bold px-5 py-3 rounded-xl transition shadow-lg shadow-emerald-500/20 flex items-center justify-center text-sm">
            அனுப்பு
        </button>
    </footer>

    <script>
        const chatBox = document.getElementById('chatBox');
        const userInput = document.getElementById('userInput');
        const sendBtn = document.getElementById('sendBtn');
        const reasoningToggle = document.getElementById('reasoningToggle');
        let chatHistory = [];

        function handleKeyPress(e) {
            if (e.key === 'Enter') sendMessage();
        }

        function sendQuickPrompt(text) {
            userInput.value = text;
            sendMessage();
        }

        async function sendMessage() {
            const query = userInput.value.trim();
            if (!query) return;

            // Render User Bubble
            appendMessage(query, 'user');
            userInput.value = '';
            userInput.disabled = true;
            sendBtn.disabled = true;

            const useDeepReasoning = reasoningToggle ? reasoningToggle.checked : false;

            // Render Loading indicator
            const loadingId = appendLoading(useDeepReasoning);

            try {
                const res = await fetch('/api/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        message: query, 
                        history: chatHistory,
                        use_deep_reasoning: useDeepReasoning 
                    })
                });
                const data = await res.json();
                
                removeLoading(loadingId);
                if (data.status === 'success') {
                    appendMessage(data.reply, 'assistant', data.model_used);
                    chatHistory.push({ role: 'user', content: query });
                    chatHistory.push({ role: 'assistant', content: data.reply });
                } else {
                    appendMessage('மன்னிக்கவும், தகவல் பெறுவதில் சிறிய தாமதம். மீண்டும் முயற்சிக்கவும்: ' + (data.message || ''), 'assistant');
                }
            } catch (err) {
                removeLoading(loadingId);
                appendMessage('தகவல் தொடர்பு பிழை: ' + err.message, 'assistant');
            } finally {
                userInput.disabled = false;
                sendBtn.disabled = false;
                userInput.focus();
            }
        }

        function appendMessage(text, role, model) {
            const div = document.createElement('div');
            div.className = role === 'user' ? 'flex justify-end' : 'flex items-start space-x-3';

            if (role === 'user') {
                const escapedText = text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/\\n/g, '<br>');
                div.innerHTML = `
                    <div class="bg-gradient-to-r from-emerald-600 to-teal-600 text-white rounded-2xl rounded-tr-none p-3.5 max-w-[85%] text-sm shadow-md">
                        ${escapedText}
                    </div>
                `;
            } else {
                let formattedHtml = '';
                try {
                    formattedHtml = marked.parse(text);
                } catch (e) {
                    formattedHtml = text.replace(/\\n/g, '<br>');
                }
                div.innerHTML = `
                    <div class="w-8 h-8 rounded-lg bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-sm flex-shrink-0 mt-1">
                        🏛️
                    </div>
                    <div class="bg-slate-800 border border-slate-700/80 rounded-2xl rounded-tl-none p-4 max-w-[85%] text-slate-200 text-sm leading-relaxed shadow-md space-y-2">
                        <div class="markdown-body">${formattedHtml}</div>
                        ${model ? `<div class="text-[10px] text-emerald-400/80 font-mono pt-1.5 border-t border-slate-700/50 flex items-center justify-between"><span>⚡ Meta Model: ${model}</span><span class="text-slate-400">தமிழ்நாடு e-Sevai வழிகாட்டி</span></div>` : ''}
                    </div>
                `;
            }
            chatBox.appendChild(div);
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        function appendLoading(isDeep) {
            const id = 'load_' + Date.now();
            const div = document.createElement('div');
            div.id = id;
            div.className = 'flex items-start space-x-3';
            const loadingText = isDeep ? 'Meta muse-wonder ஆழ்ந்த கொள்கை ஆய்வு செய்கிறது...' : 'Meta AI ஆய்வு செய்கிறது...';
            div.innerHTML = `
                <div class="w-8 h-8 rounded-lg bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-sm flex-shrink-0">
                    🏛️
                </div>
                <div class="bg-slate-800 border border-slate-700/80 rounded-2xl rounded-tl-none p-3.5 text-slate-400 text-sm flex items-center space-x-2">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-bounce"></span>
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-bounce [animation-delay:0.2s]"></span>
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-bounce [animation-delay:0.4s]"></span>
                    <span class="text-xs text-slate-400 pl-1 font-tamil">${loadingText}</span>
                </div>
            `;
            chatBox.appendChild(div);
            chatBox.scrollTop = chatBox.scrollHeight;
            return id;
        }

        function removeLoading(id) {
            const el = document.getElementById(id);
            if (el) el.remove();
        }
    </script>
</body>
</html>
    """
    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
