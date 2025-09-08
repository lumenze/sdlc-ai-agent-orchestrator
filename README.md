# 🧠 Lumenze SDLC AI Agent

An intelligent AI Agent as a Service that integrates deeply with the Lumenze software development lifecycle (SDLC). It streamlines the end-to-end developer workflow — from transforming requirements into Jira stories, generating scaffolds, providing IDE assistance, and integrating with CI/CD pipelines.

---

## 📁 Project Structure

```bash
sdlc-ai-agent-orchestrator/
├── src/
│   ├── api/              # FastAPI app entrypoint, routes, and request/response models
│   │   ├── main.py
│   │   ├── routes/       # API endpoints (e.g., /health, /requirements)
│   │   └── models/       # Pydantic request/response schemas
│   ├── core/             # Core AI logic: LLM clients and orchestration logic
│   ├── services/         # Business logic: GitHub, Jira integration, story generation
│   ├── utils/            # Shared helper functions
│   └── config/           # Pydantic settings, env loader
├── tests/                # Unit and integration tests
├── .env                  # Environment variables (not committed)
├── requirements.txt      # Python dependencies
├── .gitignore
└── README.md             # You are here

⚙️ Key Features
	•	🧠 Centralized LLM Agent (Claude, GPT, Gemini – API routed)
	•	📦 Converts requirement templates into actionable Jira stories
	•	🛠️ Scaffolds technical tasks and code suggestions
	•	🧩 Plugin-ready architecture for GitHub, IDEs, CI/CD
	•	🔐 API key/token control (centralized; no client-side exposure)
	•	📊 Scalable microservice-ready design

🚧 Phase 1: MVP Milestones

Task
Status
🔹 Setup FastAPI skeleton✅ Done
🔹 Health + LLM API routes⬜ TODO
🔹 Env + Pydantic config⬜ TODO
🔹 Claude / GPT LLM routing⬜ TODO
🔹 Req → Jira story pipeline⬜ TODO
🔹 CI/CD starter integration⬜ TODO

🧑‍💻 Local Development
# 1. Create a virtual environment
python3 -m venv venv && source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the FastAPI server
uvicorn src.api.main:app --reload

🔒 Notes on Secrets and Keys

All LLM API keys and config settings are loaded via .env.
A sample .env.template is provided for onboarding new devs.

---

## 🧠 Architecture Overview

The Lumenze SDLC AI Agent is a **modular, scalable AI agent-as-a-service** that supports:

- Intelligent SDLC automation (PM → Stories → Code)
- Developer-side LLM copiloting (bug fixing, code suggestions)
- IDE plugins + secure backend inference
- Centralized usage tracking, token control, and API security

### 🔌 Key Components

| Module             | Description |
|--------------------|-------------|
| `src/api/`         | FastAPI app entry, routes, request/response contracts |
| `src/core/llm_client.py` | Unified LLM abstraction over Claude, GPT, Gemini |
| `src/core/orchestrator.py` | Coordinates requirement → story → code generation |
| `src/services/`    | Integrations (Jira, GitHub, IDE, etc.) |
| `src/utils/`       | Shared helpers |
| `src/config/`      | Settings via `pydantic-settings` |

---

## 🧪 Design Principles

1. **Modularity:** Each component (API, LLM, GitHub, Jira) is decoupled and pluggable.
2. **Testability:** All services and agents support async unit testing via `pytest-asyncio`.
3. **Security:** LLM API keys are backend-only (not exposed to client/IDE).
4. **Scalability:** Designed to run on EC2 with future Docker/K8s deploy targets.
5. **Observability:** Future support for logging, tracebacks, token/cost tracking.
6. **Developer UX:** IDE plugins and FastAPI frontend for PM/Eng interaction.

---

## ⚙️ Technology Stack

| Layer           | Tooling                  |
|-----------------|--------------------------|
| Language        | Python 3.12              |
| API             | FastAPI + Uvicorn        |
| LLMs            | OpenAI GPT-4, Claude, Gemini |
| HTTP            | `httpx`, `python-multipart` |
| Config          | `pydantic`, `.env` via `pydantic-settings` |
| Testing         | `pytest`, `pytest-asyncio` |
| CI/CD (future)  | GitHub Actions, auto-deploy pipelines |
| IDE Integration | VS Code, JetBrains (via plugin) |
| Hosting Target  | EC2 (with future ECS/K8s options) |

---

## 🔁 AI Inference Routing

LLM calls are routed based on:
- Model strengths (e.g., Claude for planning, GPT-4 for reasoning, Gemini for coding)
- Task type (e.g., story generation, code fix)
- Cost vs token limits

Future enhancements:
- Centralized router service with token-based usage quota
- Feedback loop for model tuning via structured prompts

---

## 📊 SDLC Use Case Flow
PM/BA submits requirements via UI
↓
Agent generates tech stories, epics
↓
Jira integration to create tickets
↓
Engineer picks up ticket from UI/IDE
↓
Agent generates scaffold, helper code
↓
Developer edits, tests, commits to GitHub
↓
CI/CD pipeline runs validations

---

## 🔐 Future Enhancements
- CI/CD GitHub Action support (auto-format, lint, test)
- Cost control by LLM + model-level quotas
- Intelligent feedback collection for agent learning
- Slack + SharePoint integrations for collaboration
- Prompt templating + prompt chaining
