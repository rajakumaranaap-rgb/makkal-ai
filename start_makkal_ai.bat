@echo off
title Makkal AI - Tamil Nadu Citizen Digital Services
chcp 65001 >nul
echo ========================================================
echo   🏛️ Makkal AI (மக்கள் AI) - Meta AI Hackathon 2026
echo   Powered by Meta Model API (Muse & SAM 2)
echo ========================================================
echo.
echo Starting FastAPI Web Server at http://127.0.0.1:8000 ...
echo.

cd /d "D:\api\makkal-ai"
start http://127.0.0.1:8000/

"D:\api\arcreel\.venv\Scripts\python.exe" -m uvicorn app:app --host 127.0.0.1 --port 8000 --reload
pause
