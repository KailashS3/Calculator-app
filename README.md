# 🧮 Simple Calculator Web App (Python + Flask)

A lightweight calculator web application built with **Python (Flask)**.  
It provides a simple browser interface to perform basic arithmetic operations.

---

## 📂 Project Structure
```
calculator-app/
      ├─ calculator.py
      ├─ requirements.txt
      └─ templates/
           └─ calculator.html
```
---

## ⚙️ Requirements
- Python 3.11+
- Flask (installed via `requirements.txt`)
- Docker (optional, for containerized deployment)

---

## ▶️ Run Locally

1. Install dependencies:
   pip install -r requirements.txt

2. Start the app:
   python calculator.py

3. Open your browser at:
   http://localhost:8080/

🐳 Run with Docker

1. Build the Docker image:
   docker build -t python-calculator .

2. Run the container:
   docker run -p 8080:8080 python-calculator

3. Access the app in your browser:
   http://localhost:8080/
