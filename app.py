from flask import Flask, render_template, request, jsonify
import joblib
import sqlite3
import os
from datetime import datetime
from chatbot.responses import get_response

app = Flask(__name__)
 
# Load model
data = joblib.load('model/model.pkl') 
model = data['model']
features = data['features']  

RISK = {0: 'Low', 1: 'Medium', 2: 'High'}
RISK_COLOR = {0: 'green', 1: 'orange', 2: 'red'} 

SUGGESTIONS = {
    0: [
        "Great job maintaining a healthy lifestyle!",
        "Keep up your sleep schedule (7-8 hrs recommended).",
        "Continue your physical activity routine.",
        "Stay socially connected with friends and family.",
    ],
    1: [
        "Try to get at least 7 hours of sleep daily.",
        "Reduce social media usage to under 2 hours/day.",
        "Add 20-30 mins of physical activity to your routine.",
        "Talk to a friend or counselor if feeling overwhelmed.",
        "Use Pomodoro technique to manage study sessions.",
    ],
    2: [
        "Please reach out to a counselor or trusted person immediately.",
        "🆘 Tele-MANAS Helpline: 14416 (Free, 24x7, Govt. of India)",
        "iCall Helpline: 9152987821",
        "Prioritize sleep - it directly affects mental health.",
        "Reduce academic load if possible, talk to your professor.",
        "Take breaks every 25 minutes while studying.",
        "You are not alone - help is always available.",
    ],
}

# ── Database ───────────────────────────────────────────────────────────────────
def init_db():
    conn = sqlite3.connect('database/checkins.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS checkins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        sleep REAL,
        study REAL,
        social_media REAL,
        physical REAL,
        attendance REAL,
        acad_pressure INTEGER,
        fin_stress INTEGER,
        social_int INTEGER,
        gender INTEGER,
        risk_level INTEGER,
        risk_label TEXT
    )''')
    conn.commit()
    conn.close()

def save_checkin(inputs, risk):
    conn = sqlite3.connect('database/checkins.db')
    conn.execute('''INSERT INTO checkins 
        (date, sleep, study, social_media, physical, attendance,
         acad_pressure, fin_stress, social_int, gender, risk_level, risk_label)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',
        (datetime.now().strftime('%Y-%m-%d'),
         inputs[0], inputs[1], inputs[2], inputs[3], inputs[4],
         inputs[5], inputs[6], inputs[7], inputs[8],
         risk, RISK[risk]))
    conn.commit()
    conn.close()

def get_trend():
    conn = sqlite3.connect('database/checkins.db')
    rows = conn.execute(
        'SELECT date, risk_level FROM checkins ORDER BY id DESC LIMIT 7'
    ).fetchall()
    conn.close()
    rows.reverse()
    return rows

# ── Routes ─────────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        vals = [
            float(request.form['sleep']),
            float(request.form['study']),
            float(request.form['social_media']),
            float(request.form['physical']),
            float(request.form['attendance']),
            int(request.form['acad_pressure']),
            int(request.form['fin_stress']),
            int(request.form['social_int']),
            int(request.form['gender']),
        ]
        prediction = int(model.predict([vals])[0])
        save_checkin(vals, prediction)
        return render_template('result.html',
            risk=RISK[prediction],
            color=RISK_COLOR[prediction],
            suggestions=SUGGESTIONS[prediction],
            inputs=vals)
    except Exception as e:
        return f"Error: {e}", 400

@app.route('/trend')
def trend():
    rows = get_trend()
    dates = [r[0] for r in rows]
    levels = [r[1] for r in rows]
    return render_template('trend.html', dates=dates, levels=levels)

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.json.get('message', '')
    reply = get_response(msg)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    os.makedirs('database', exist_ok=True)
    init_db()
    app.run(debug=True)