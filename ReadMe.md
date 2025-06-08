# 🚆 Train Station Alert App (Python + HTML + RapidAPI)

This app allows users to enter a **PNR or Train Number** and a **Date**, select a station, and receive a **loud alarm** when the train reaches the selected station.

---

## 🛠 Tech Stack

- **Frontend**: HTML + JavaScript
- **Backend**: Python (Flask)
- **API**: RapidAPI for live train status
- **Sound**: Plays an alert sound when train reaches selected station

---

## 📁 Project Structure

train-alert-app/
├── app.py                 # Flask backend
├── templates/
│   └── index.html         # Frontend
├── static/
│   └── alarm.mp3          # Alarm sound
├── .env                   # API keys
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
