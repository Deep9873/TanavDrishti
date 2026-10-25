# TanavDrishti 🧠 (तनाव दृष्टि)

**A student mental-wellness check-in app.** Answer a short daily questionnaire about sleep, study, screen time and stress, and TanavDrishti estimates your stress risk (Low / Medium / High), suggests what to do next, tracks your last 7 check-ins, and offers a friendly chatbot, *TanavBot*, for quick support.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)

> ⚠️ **Disclaimer:** TanavDrishti is an educational project. It is **not** a medical or diagnostic tool. If you are struggling, please talk to a counsellor or someone you trust. In India, **Tele-MANAS** offers free, 24×7 support on **14416**.

---

## Features

- 📝 **Daily check-in** using 9 inputs: sleep hours, study hours, social-media hours, physical activity, attendance %, academic pressure, financial stress, social interaction, and gender.
- 🤖 **ML risk prediction:** a scikit-learn model classifies each check-in as Low, Medium or High risk.
- 💡 **Personalised suggestions** for each risk level, including helpline numbers for high-risk results.
- 📈 **Trend view** of your last 7 check-ins, saved locally in SQLite.
- 💬 **TanavBot:** a rule-based chatbot with ~30 topics (stress, anxiety, panic, sleep, exams, focus, loneliness, motivation, helplines and more).

## How it works

1. `model/train_model.py` trains three classifiers (Random Forest, Logistic Regression, Decision Tree) on `data/student_mental_health.csv` (600 rows) and keeps the best one as `model/model.pkl`.
2. The Flask app loads that model, predicts on each submitted check-in, stores the result in `database/checkins.db`, and renders the result and trend pages.

In a local training run on the bundled dataset, Logistic Regression scored best (≈ 97.5% test accuracy vs ≈ 79% for Random Forest and ≈ 67% for Decision Tree). The dataset is small, so treat these numbers as a demo of the pipeline, not as clinical accuracy.

## Tech stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| ML | scikit-learn, pandas, NumPy, joblib |
| Storage | SQLite |
| Frontend | Jinja2 templates, HTML, CSS, Chart.js |

## Getting started

```bash
git clone https://github.com/Deep9873/TanavDrishti.git
cd TanavDrishti

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 1) Train the model (creates model/model.pkl)
python model/train_model.py

# 2) Run the app
python app.py
```

Open `http://127.0.0.1:5000`.

## Routes

| Route | Description |
|-------|-------------|
| `/` | Check-in form |
| `/predict` (POST) | Runs the model and shows your result and suggestions |
| `/trend` | Risk level over your last 7 check-ins |
| `/chat` (POST) | TanavBot reply for a message |

## Project structure

```text
TanavDrishti/
├── app.py                    # Flask app and routes
├── chatbot/
│   └── responses.py          # Keyword-based chatbot responses
├── data/
│   └── student_mental_health.csv
├── model/
│   └── train_model.py        # Trains and saves the best model
├── templates/                # index, result, trend
├── static/style.css
└── database/                 # SQLite check-ins (created on first run)
```

## Privacy

Check-ins are stored only in a local SQLite file on the machine running the app. There are no accounts and nothing is sent to third parties.

## Ideas for the future

- Real-world dataset and proper validation (cross-validation, confusion matrix)
- Per-user accounts so trends are private to each person
- Smarter chatbot (intent classification or an LLM, with safety guardrails)
- Deploy with a production server (Gunicorn) instead of Flask's debug server

## Author

**Deep Jangid** · [@Deep9873](https://github.com/Deep9873)
