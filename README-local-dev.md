# 🛠️ Lumenze SDLC AI Agent — Local Development Guide

Welcome to the local development setup for the SDLC AI Agent Orchestrator service. This backend service converts feature requirements into structured Jira tickets using LLMs like GPT-4.

---

## 🚀 Project Structure (Overview)

```
sdlc-ai-agent-orchestrator/
├── docker-compose.yml
├── Dockerfile
├── requirements/            # Sample requirement .md files
├── templates/               # Prompt templates
├── src/
│   ├── api/                 # FastAPI entrypoint and route handlers
│   ├── core/                # LLM client, logger
│   ├── config/              # Environment & settings
│   ├── utils/               # Markdown → CSV helper, cache
│   └── services/            # (Optional future service layer)
```

---

## 📦 Setup Instructions

### 1. 🔁 Clone Repo & Create Virtual Env

```bash
git clone https://github.com/your-org/sdlc-ai-agent-orchestrator.git
cd sdlc-ai-agent-orchestrator

python3 -m venv .venv
source .venv/bin/activate
```

---

### 2. 📄 Install Dependencies

```bash
pip install -r requirements.txt
```

If you're using file upload via FastAPI:
```bash
pip install python-multipart
```

---

### 3. 🔐 Environment Variables

Create a `.env` file in the root of the repo:

```dotenv
OPENAI_API_KEY=sk-xxx-your-key-here
```

---

### 4. ▶️ Run the API Server (Dev)

```bash
uvicorn src.api.main:app --reload
```

- Open browser: [http://localhost:8000/docs](http://localhost:8000/docs) to access Swagger UI

---

## 📤 Using the API (cURL)

Upload a Markdown file and download Jira ticket CSV:

```bash
curl -X POST http://localhost:8000/generate-tickets   -F "requirements_file=@requirements/samples/login_dashboard.md"   --output generated_tickets.csv
```

---

## 🧪 Running Tests

```bash
pytest tests/
```

---

## 🐳 Docker (Optional)

### 1. Build & Run API Container

```bash
docker build -t sdlc-api .
docker run -p 8000:8000 sdlc-api
```

Or use `docker-compose`:

```bash
docker-compose up --build
```

---

## 🗃️ Caching (Local)

Responses are cached in `.cache/` folder to reduce GPT token usage.

- Clear cache: `rm -rf .cache/`

---

## 🔍 Logs

Logs are output to the console with timestamp and log level using a centralized logger (`src/core/logger.py`).

---

## 🤝 Contributing

1. Fork repo
2. Create feature branch
3. Push PR with context and test coverage

---

## 📬 Questions?

Contact: [Sharon Bose](mailto:bose@lumenze.com)  
Project: [Lumenze AI Orchestrator](https://github.com/your-org/sdlc-ai-agent-orchestrator)

---