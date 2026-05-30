@echo off
echo Starting MindWatch...

start "RAG API" cmd /k "cd /d %~dp0 && venv\Scripts\activate && python -m chatbot.api_server"

timeout /t 4

start "Streamlit" cmd /k "cd /d %~dp0 && venv\Scripts\activate && streamlit run streamlit_app.py"

echo Done! Open http://localhost:8501
```

---

### `requirements.txt`
```
streamlit
flask
flask-cors
langchain
langchain-community
langchain-core
sentence-transformers
faiss-cpu
pandas