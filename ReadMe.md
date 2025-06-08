# 🚉 Train Station Alert App

A web-based Python application that allows users to:

- Enter a **Train Number or PNR** and **Travel Date**
- Select a **station** from the route
- Receive a **loud alarm alert** when the train reaches the selected station

Built using **Flask**, **HTML/JavaScript**, and **RapidAPI** for real-time train status.

---

## 📸 Demo

> Coming soon — you can record a short GIF or video once deployed.

---

## 📦 Features

✅ Fetch train route by Train Number  
✅ Select a station for alert  
✅ Live train status monitoring (polling)  
✅ Audio alarm when selected station is reached  
✅ RapidAPI integration  
✅ Easy to run locally  

---

## 🛠 Tech Stack

- Python (Flask)
- HTML + JavaScript
- RapidAPI (live train tracking)
- dotenv (secure API credentials)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Vjalaj/RailPal.git
cd RailPal

pip install -r requirements.txt

cp .env.example .env

RAPIDAPI_KEY=your_rapidapi_key
RAPIDAPI_HOST=your_rapidapi_host
RAPIDAPI_URL=https://your_rapidapi_url


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
