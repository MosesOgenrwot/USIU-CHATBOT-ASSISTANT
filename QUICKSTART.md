# 🚀 Quick Start Guide - USIU Chatbot

## For Complete Beginners

This guide will help you get the chatbot running in 5 minutes!

---

## Step 1: Check Prerequisites

**You need:**
- Python 3.10 or newer ([Download here](https://www.python.org/downloads/))
- A terminal/command prompt
- 5 minutes of your time

**Check Python version:**
```bash
python --version
```
Should show: `Python 3.10.x` or higher

---

## Step 2: Setup

### Windows Users:

1. **Extract the ZIP file** to `C:\CHATBOT` (or anywhere you want)

2. **Open Command Prompt:**
   - Press `Windows Key + R`
   - Type `cmd` and press Enter
   - Navigate to folder: `cd C:\CHATBOT`

3. **Create virtual environment:**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```
   You should see `(venv)` at the start of your command line

4. **Install packages:**
   ```cmd
   pip install -r requirements.txt
   ```
   Wait 2-3 minutes for installation

### Mac/Linux Users:

1. **Extract ZIP and open Terminal**

2. **Navigate to folder:**
   ```bash
   cd ~/Downloads/usiu_chatbot_final
   ```

3. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install packages:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Step 3: Start the Chatbot

### Option A: Easy Way (One Command)

**Windows:**
```cmd
run.bat
```

**Mac/Linux:**
```bash
chmod +x run.sh
./run.sh
```

This opens two windows automatically!

### Option B: Manual Way (Recommended for Learning)

**Open TWO terminal windows:**

**Terminal 1 (Backend):**
```bash
# Activate venv first
uvicorn backend.api:app --reload
```

**Terminal 2 (Frontend):**
```bash
# Activate venv first
streamlit run frontend/streamlit_app.py
```

---

## Step 4: Use the Chatbot

1. **Wait for messages:**
   - Terminal 1 should show: `Application startup complete`
   - Terminal 2 should show: `You can now view your Streamlit app`

2. **Open browser:**
   - Frontend: http://localhost:8501
   - Backend API: http://localhost:8000/docs

3. **Try example questions:**
   - "What are the fees for nursing?"
   - "How do I pay via M-Pesa?"
   - "Where is the library?"
   - "What scholarships are available?"

---

## Step 5: Stop the Chatbot

**Windows:**
- Press `Ctrl + C` in both terminal windows

**Mac/Linux:**
- Press `Ctrl + C` in both terminal windows
- Or if using run.sh: `Ctrl + C` once

---

## ❓ Problems?

### "Command not found: python"
Try `python3` instead of `python`

### "Permission denied" on Mac/Linux
Run: `chmod +x run.sh`

### Port already in use
Someone is using port 8000 or 8501. Try:
```bash
# Use different ports
uvicorn backend.api:app --port 8001
streamlit run frontend/streamlit_app.py --server.port 8502
```

### "Module not found"
Your virtual environment isn't activated. Run:
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

---

## 🎯 What's Happening Behind the Scenes?

1. **Backend (Port 8000):**
   - Loads 8 knowledge JSON files
   - Initializes 4 AI agents
   - Waits for questions via API

2. **Frontend (Port 8501):**
   - Shows chat interface
   - Sends questions to backend
   - Displays responses beautifully

3. **Knowledge Base:**
   - 8 JSON files with USIU info
   - No internet needed!
   - 100% offline system

---

## 📖 Next Steps

Once it's working:

1. **Read the full README.md** for advanced features
2. **Try the example queries** in the sidebar
3. **Check API documentation** at http://localhost:8000/docs
4. **Explore the code** in `src/agents/multi_agent_system.py`

---

## 🎓 For Your Assignment

This system demonstrates:
- ✅ Multiple specialized agents
- ✅ Agent coordination (Supervisor)
- ✅ Knowledge retrieval (JSON-based)
- ✅ Tool integration (Knowledge base)
- ✅ Human-in-the-loop (Feedback buttons)
- ✅ Clean documentation
- ✅ Production-ready code

---

## 💡 Pro Tips

**For Development:**
```bash
# Backend with auto-reload
uvicorn backend.api:app --reload

# Frontend with auto-reload (default)
streamlit run frontend/streamlit_app.py
```

**For Testing:**
```bash
# Test backend health
curl http://localhost:8000/health

# Or open in browser
http://localhost:8000/health
```

**For Deployment:**
- See "Deployment Options" in main README.md
- Free options: Render, Railway, Streamlit Cloud

---

## 🆘 Still Stuck?

1. **Check that:**
   - Python is installed
   - Virtual environment is activated (you see `(venv)`)
   - You're in the right folder
   - All files from ZIP are present

2. **Try fresh install:**
   ```bash
   # Delete venv folder
   # Create new one
   python -m venv venv
   # Activate and reinstall
   pip install -r requirements.txt
   ```

3. **Check versions:**
   ```bash
   python --version  # Should be 3.10+
   pip list          # Should show fastapi, streamlit
   ```

---

**You're all set! 🎉**

The chatbot should now be running. Try asking it about USIU fees, programs, facilities, or services!
