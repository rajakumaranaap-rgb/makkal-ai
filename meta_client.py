"""
Meta Model API Client (Meta Muse AI Platform)
Supports:
- Chat & Reasoning (muse-spark-1.3 & muse-wonder-1.0)
- Image Segmentation (sam-3.1)
- Voice Transcription (muse-voice-transcribe-1.0)
- Image Generation (muse-image-1.0)
"""

import os
import json
import requests
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("META_MODEL_API_KEY", "")
BASE_URL = os.environ.get("META_API_BASE", "https://api.meta.ai/v1")

DEFAULT_CHAT_MODEL = os.environ.get("DEFAULT_CHAT_MODEL", "muse-spark-1.3")
REASONING_MODEL = os.environ.get("REASONING_MODEL", "muse-wonder-1.0")
SEGMENT_MODEL = os.environ.get("SEGMENT_MODEL", "sam-3.1")
AUDIO_MODEL = os.environ.get("AUDIO_TRANSCRIBE_MODEL", "muse-voice-transcribe-1.0")


class MetaModelClient:
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        self.api_key = api_key or API_KEY
        self.base_url = (base_url or BASE_URL).rstrip("/")
        if not self.api_key:
            raise ValueError("META_MODEL_API_KEY must be provided or set in environment variables.")

    @property
    def headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def list_models(self) -> List[Dict[str, Any]]:
        """Lists all models available on the Meta Model API."""
        url = f"{self.base_url}/models"
        resp = requests.get(url, headers=self.headers, timeout=15)
        resp.raise_for_status()
        return resp.json().get("data", [])

    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: float = 0.4,
        max_tokens: Optional[int] = 4096
    ) -> Dict[str, Any]:
        """
        Calls Meta Muse Chat Completion.
        Default model: muse-spark-1.3 (fast, colloquial Tamil reasoning).
        Note: muse-spark and muse-wonder generate internal reasoning tokens,
        so a generous max_tokens (e.g. 4096) is essential to avoid truncation.
        """
        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": model or DEFAULT_CHAT_MODEL,
            "messages": messages,
            "temperature": temperature
        }
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens

        resp = requests.post(url, headers=self.headers, json=payload, timeout=60)
        resp.raise_for_status()
        return resp.json()

    def deep_reasoning(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.2,
        max_tokens: Optional[int] = 6144
    ) -> Dict[str, Any]:
        """Calls Meta muse-wonder-1.0 for deep policy verification and multi-step eligibility reasoning."""
        return self.chat_completion(
            messages=messages,
            model=REASONING_MODEL,
            temperature=temperature,
            max_tokens=max_tokens
        )

    def transcribe_audio(self, audio_bytes: bytes, filename: str = "voice.mp3") -> Dict[str, Any]:
        """Transcribes Tamil audio voice notes using muse-voice-transcribe-1.0."""
        url = f"{self.base_url}/audio/transcriptions"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        files = {
            "file": (filename, audio_bytes, "audio/mpeg"),
            "model": (None, AUDIO_MODEL),
            "language": (None, "ta")
        }
        resp = requests.post(url, headers=headers, files=files, timeout=45)
        resp.raise_for_status()
        return resp.json()

    def segment_image(self, image_base64: str) -> Dict[str, Any]:
        """Calls Meta SAM 3.1 (Segment Anything) to segment document boundaries, seals, and signatures."""
        url = f"{self.base_url}/images/segment"
        payload = {
            "model": SEGMENT_MODEL,
            "image": image_base64
        }
        resp = requests.post(url, headers=self.headers, json=payload, timeout=60)
        resp.raise_for_status()
        return resp.json()


# Global client instance
meta_client = MetaModelClient()
