# 🛠️ Lumenze SDLC AI Agent — Local Development Guide

Welcome to the local development setup for the SDLC AI Agent Orchestrator. This backend service converts feature requirements into structured Jira tickets using LLMs like GPT-4o.

---

## 📓 Prerequisites

> These are needed **on the host machine**. Docker will handle the rest.

### Required Tools:

* [Git](https://git-scm.com/downloads)
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)

  * Make sure Docker is installed, running, and you have access to Docker CLI

> **No need to install Python, Redis, or FastAPI** on your host machine.

---

## 🚀 Step 1: Clone the Repository

```bash
git clone https://github.com/your-org/sdlc-ai-agent-orchestrator.git
cd sdlc-ai-agent-orchestrator
```

---

## 🔐 Step 2: Set Up Environment Variables

Create a `.env.dev` file in the root of the project (same directory as `docker-compose.local.yml`):

### Example `.env.dev`

```dotenv
OPENAI_API_KEY=sk-xxx-your-api-key
WEB_PORT=8000
REDIS_PORT=6379
```

If you have additional variables (e.g., Slack webhook, Claude key, etc.), include them here.

---

## 🔄 Step 3: Run Locally with Docker

```bash
docker-compose -f docker-compose.local.yml up --build
```

This will:

* Build the image
* Start FastAPI server at `http://localhost:8000`
* Start Redis cache

### Access the Swagger UI

[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📲 Step 4: API Usage

Use Swagger UI or `curl` to test file upload:

```bash
curl -X POST http://localhost:8000/generate-tickets \
  -F "requirements_file=@requirements/samples/login_dashboard.md" \
  --output generated_tickets.csv
```

---

## 📊 Step 5: Logs & Caching

* Logs: Displayed in terminal with timestamps
* Caching: Stored in `.cache/` folder locally to reduce LLM token usage

  * Clear with: `rm -rf .cache/`

---

## ❌ Step 6: Stop or Cleanup

Stop services (without removing volumes):

```bash
docker-compose -f docker-compose.local.yml down
```

Stop and remove everything including volumes:

```bash
docker-compose -f docker-compose.local.yml down -v
```

Optional global cleanup:

```bash
docker system prune -f
```

---

## 🤝 Common Errors & Fixes

| Error                        | Likely Cause                     | Fix                                            |
| ---------------------------- | -------------------------------- | ---------------------------------------------- |
| `OPENAI_API_KEY must be set` | Missing or unreadable `.env.dev` | Ensure the file exists and is correctly named  |
| `Cannot connect to Redis`    | Redis container failed to start  | Check Docker logs and port conflicts           |
| 404 on `/generate-tickets`   | Wrong route or server not up     | Verify FastAPI server is running and reachable |

---

## 🔧 Debugging Tips

* Confirm containers:

  ```bash
  docker ps
  ```
* Inspect logs:

  ```bash
  docker-compose -f docker-compose.local.yml logs -f
  ```
* Bash into running container:

  ```bash
  docker exec -it <container_name> /bin/bash
  ```

---

## 🙋 Questions?

Contact: [Sharon Bose](mailto:bose@lumenze.com)
Project: [Lumenze AI Orchestrator](https://github.com/your-org/sdlc-ai-agent-orchestrator)
