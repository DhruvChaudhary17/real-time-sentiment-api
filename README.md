Sure! Here's a complete and clean `README.md` file for your **Real-Time Sentiment Analysis API with MLOps features (FastAPI + Docker + Prometheus + Grafana + GitHub Actions)** project:

---

```markdown
# 🧠 Real-Time Sentiment Analysis API 🚀

This project is a production-ready **NLP pipeline** that performs real-time sentiment analysis on text using FastAPI. It includes:

- 📊 Prometheus metrics for model monitoring
- 📈 Grafana dashboards for visualization
- 🐳 Docker & Docker Compose for containerization
- ⚙️ GitHub Actions CI/CD for automated workflow

---

## 📦 Features

- 🔍 Real-time sentiment classification (Positive, Negative, Neutral)
- ⚡ FastAPI backend for quick predictions
- 📈 Prometheus monitoring + Grafana dashboard
- 🐳 Dockerized app with `docker-compose`
- 🔄 CI/CD pipeline with GitHub Actions
- ✅ Exposes `/predict`, `/docs`, and `/metrics` endpoints

---

## 📁 Project Structure

```

sentiment-api/
├── app/
│   └── main.py               # FastAPI app
├── model/
│   ├── model.joblib          # Trained ML model
│   └── label\_encoder.joblib  # Label encoder
├── .github/
│   └── workflows/
│       └── ci-cd.yml         # GitHub Actions CI/CD
├── Dockerfile                # Docker image definition
├── docker-compose.yml        # Multi-container orchestration
├── prometheus.yml            # Prometheus configuration
├── requirements.txt          # Python dependencies
├── train.py                  # Model training script
├── .gitignore
└── README.md

````

---

## 🚀 Getting Started (Development)

### 🔧 Step 1: Clone the repo

```bash
git clone https://github.com/DhruvChaudhary17/real-time-sentiment-api.git
cd real-time-sentiment-api
````

### 🔒 Step 2: Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
```

### 📦 Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Step 4: Run locally

```bash
uvicorn app.main:app --reload
```

Now visit:

* Swagger UI: `http://localhost:8000/docs`
* Metrics: `http://localhost:8000/metrics`

---

## 🐳 Running with Docker Compose

Make sure Docker Desktop is running.

```bash
docker compose up --build
```

Then open:

* FastAPI App: `http://localhost:8000`
* Prometheus: `http://localhost:9090`
* Grafana (if configured): `http://localhost:3000`

---

## 📈 Prometheus & Grafana

### 📍 Prometheus Endpoint

* Scrapes metrics from `/metrics` on the FastAPI app

### 📊 Grafana Dashboard (optional)

You can import the Prometheus dashboard into Grafana. Use the Prometheus data source pointing to `http://prometheus:9090`.

---

## 🤖 CI/CD with GitHub Actions

This project includes a `.github/workflows/ci-cd.yml` file that:

* ✅ Checks code formatting and linting
* 🔍 Runs tests (if added)
* 🐳 Optionally builds Docker images

CI/CD runs automatically on every push to `main`.

---

## 🧠 Model

Trained using `train.py` on sentiment-labeled text. The model and label encoder are stored as `.joblib` files inside the `model/` directory.

---

## ✅ Endpoints

* `POST /predict` — Sentiment prediction
* `GET /docs` — Interactive Swagger docs
* `GET /metrics` — Prometheus-compatible metrics

---

## 🙌 Author

**Dhruv Chaudhary**
GitHub: [@DhruvChaudhary17](https://github.com/DhruvChaudhary17)

---






