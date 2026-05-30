# 🚀 FastAPI for Machine Learning: End-to-End Course

Welcome to the official repository for the **FastAPI for Machine Learning** course! This comprehensive 20–22 hour course walks you through building powerful, production-ready APIs using **FastAPI**, with a special focus on deploying **Machine Learning** models. You’ll learn from API basics to deployment using modern DevOps practices.

---

## 📚 Course Overview

This course is designed to help **data scientists**, **backend developers**, and **AI engineers** build real-world ML-powered APIs using **FastAPI** and deploy them efficiently. We go beyond the basics by incorporating **Redis**, **Docker**, **JWT**, **Prometheus**, **Grafana**, and **Render**.

---

## 🧭 Course Modules

| Module | Title | Description |
|--------|-----------------------------|-------------|
| 1️⃣ | **Introduction to APIs** | What are APIs, how REST works, HTTP methods, status codes, and best practices. |
| 2️⃣ | **Introduction to FastAPI** | FastAPI essentials, comparison with Flask, type hinting, async support, and Pydantic. |
| 3️⃣ | **Building Basic APIs** | Creating routes, Request/Response Models, Query & Path parameters, and Validations. |
| 4️⃣ | **Database Integration** | SQL integration using ORMs/ODMs. |
| 5️⃣ | **Machine Learning Model Integration** | Load and serve ML models. |
| 6️⃣ | **Advanced FastAPI Concepts** | Dependency injection, JWT authentication, API key management, Middlewares, and Error Handling. |
| 7️⃣ | **Testing and Debugging** | Writing unit & integration tests with `pytest`, debugging tips, and FastAPI’s Swagger UI. |
| 8️⃣ | **Performance Optimization and Monitoring** | Caching with Redis and Monitoring with Prometheus & Grafana. |
| 9️⃣ | **Capstone Project** | A complete Car Price Prediction ML API — with auth, caching, logging, monitoring, and deployed using Docker & Render. |

---

## 🛠️ Tech Stack

- 🐍 **Python**
- ⚡ **FastAPI**
- 🔐 **JWT Authentication**
- 🧪 **Pytest**
- 🧠 **Scikit-learn**
- 🛢️ **SQL**
- 🧰 **Docker & Docker Compose**
- 🔁 **Redis**
- 📊 **Prometheus + Grafana**
- ☁️ **Render Deployment**

---

## 💻 Capstone Project

🎯 **Car Price Prediction API** — A fully production-ready API that includes:

- JWT-based login and API key access
- ML prediction endpoint with Redis caching
- Prometheus monitoring & Grafana dashboard
- Custom exception handling
- Modular project structure and Docker deployment
- Deployed on [Render](https://render.com)

👉 Find the project code in [parent repository](https://github.com/MisbahullahSheriff/fastapi-project)

---

## 🚀 Getting Started

### 1. Prerequisites

- Python
- Git
- Docker (optional)

### 2. Clone the Repo

```bash
git clone https://github.com/SamKur/fastapi-advanced-course
cd fastapi-advanced-course
# then venv & pip install
```

## 🧑‍🚒 Helper FastAPI Quick Notes


### 1. Create & Activate Virtual Environment (Recommended)

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

###### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

###### Linux / macOS

```bash
source .venv/bin/activate
```

Install FastAPI and recommended dependencies:

```bash
pip install "fastapi[standard]"
```

---

### 2. Conda Alternative (Optional)

Create a new environment:

```bash
conda create -n myenv python=3.13
```

Or clone the base environment:

```bash
conda create -n newenv --clone base
```

---

### 3. Minimal FastAPI Application

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, FastAPI!"}
```

###### Notes

- `app = FastAPI()` creates the FastAPI application instance.
- `@app.get("/")` creates a **GET** endpoint at the root URL.
- Python dictionaries are automatically returned as **JSON** responses.

---

### 4. Running the Application

General format:

```bash
uvicorn <filename>:<fastapi_object> --reload
```

Examples:

```bash
uvicorn main:app --reload
```

```bash
uvicorn 0_first_app:app --reload
```

Where:

- `main` → `main.py`
- `app` → `app = FastAPI()`
- `--reload` → Auto-restarts the server when code changes

---

### 5. Accessing the Application

Application:

```text
http://127.0.0.1:8000
```

Swagger UI (Interactive API Docs):

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

---

### 6. Running with `python main.py`

To start FastAPI directly using:

```bash
python main.py
```

Add:

```python
import uvicorn
from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
```

###### Format

```text
filename:object
```

Example:

```text
main:app
```

Where:

- `main` → `main.py`
- `app` → `app = FastAPI()`

---

### 7. Other Python Web Frameworks

###### Flask

```bash
flask run app.py
```

###### Streamlit

```bash
streamlit run app.py
```

These frameworks provide their own development servers. For FastAPI projects, use **Uvicorn**.

---

### Quick Reference

```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\Activate.ps1

# Activate (Linux/macOS)
source .venv/bin/activate

# Install FastAPI
# pip install "fastapi[standard]"
pip install -r requirements.txt

# Run FastAPI app
uvicorn main:app --reload

# Run directly as script
python main.py
```