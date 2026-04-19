# 🚀 Log Intelligence System

An AI-powered **Log Intelligence System** that analyzes large-scale system logs to detect anomalies and perform **Root Cause Analysis (RCA)**. This project demonstrates how machine learning can automate log monitoring, reduce manual debugging, and improve system reliability.

---

## 🧠 Overview

Modern systems generate massive amounts of logs, making manual analysis inefficient and error-prone. This project builds an intelligent pipeline that:

* Parses raw logs into structured data
* Detects anomalies using machine learning
* Identifies potential causes of failures
* Visualizes insights via an interactive dashboard

---

## ⚙️ Features

* 📥 **Log Parsing** – Converts unstructured logs into structured format
* 🤖 **Anomaly Detection** – Uses Isolation Forest to detect unusual behavior
* 🔍 **Root Cause Analysis (RCA)** – Identifies frequent error patterns
* 📊 **Dashboard** – Interactive UI using Streamlit
* ⚡ **Lightweight System** – Easy to run and extend

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **Streamlit**
* **Machine Learning (Isolation Forest)**

---

## 📂 Project Structure

```
log-intelligence-system/
│
├── logs/
│   └── system.log
├── parser.py
├── model.py
├── rca.py
├── app.py
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/your-username/log-intelligence-system.git
cd log-intelligence-system
```

### 2. Install dependencies

```
pip install pandas numpy scikit-learn streamlit
```

### 3. Run the application

```
streamlit run app.py
```

### 4. Open in browser

```
http://localhost:8501
```

---

## 📊 Sample Workflow

1. Load logs from `system.log`
2. Parse logs into structured format
3. Train ML model on log messages
4. Detect anomalies
5. Perform root cause analysis
6. Display results in dashboard

---

## 💡 Use Cases

* System monitoring and debugging
* Security log analysis
* Failure detection in backend systems
* Infrastructure health monitoring

---

## 🚀 Future Improvements

* Real-time log streaming
* Advanced NLP-based log analysis
* Integration with cloud platforms
* Better RCA using event correlation

---

## 🧾 Resume Highlight

> Built an AI-powered Log Intelligence System to analyze large-scale logs using machine learning for anomaly detection and automated root cause analysis, with real-time visualization using Streamlit.

---

## 🤝 Contributing

Feel free to fork this repo, raise issues, or submit pull requests to improve the system.

---

## 📬 Contact

For queries or collaboration:

* GitHub: https://github.com/srishtiseema
* LinkedIn: https://www.linkedin.com/in/srishti-18479b281/

---

✨ *If you found this useful, consider giving it a star!*
