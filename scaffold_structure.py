import os

# Define folder and file structure
structure = {
    "src": {
        "api": {
            "__init__.py": "",
            "main.py": "",  # FastAPI entrypoint
            "routes": {
                "__init__.py": "",
                "health.py": "",
                "requirements.py": ""
            },
            "models": {
                "__init__.py": "",
                "schemas.py": ""
            }
        },
        "core": {
            "__init__.py": "",
            "llm_client.py": "",
            "orchestrator.py": ""
        },
        "services": {
            "__init__.py": "",
            "github_service.py": "",
            "jira_service.py": "",
            "story_generator.py": ""
        },
        "utils": {
            "__init__.py": "",
            "helpers.py": ""
        },
        "config": {
            "__init__.py": "",
            "settings.py": ""
        }
    },
    "tests": {
        "__init__.py": "",
        "test_health.py": "",
        "test_story_generator.py": ""
    },
    ".env": "",
    "README.md": "# Lumenze SDLC AI Agent\n",
    "requirements.txt": "",
    ".gitignore": "__pycache__/\n.env\n*.pyc\n.venv/\n"
}

def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w') as f:
                f.write(content)

if __name__ == "__main__":
    create_structure(".", structure)
    print("✅ Project structure scaffolded successfully.")