
# 🏗️ System Architecture

<div align="center">

# AI SQL Debugging Agent
### System Architecture & Data Flow

</div>

---

## 📐 Architecture Diagram

```text
┌──────────────────────────────────────┐
│                 USER                 │
│          Enters SQL Query            │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│             FRONTEND                 │
│          HTML • CSS • JS             │
│                                      │
│  SQL Editor  │  Debug Console        │
└──────────────────┬───────────────────┘
                   │
              HTTP Request
                   │
                   ▼
┌──────────────────────────────────────┐
│             FLASK API                │
│               app.py                 │
│                                      │
│       Request & Response Handler     │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│            SQL ANALYZER               │
│          sql_analyzer.py             │
│                                      │
│  Error Detection • Query Analysis    │
└──────────────────┬───────────────────┘
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
      Detection Correction Explanation
          │        │        │
          └────────┼────────┘
                   ▼
┌──────────────────────────────────────┐
│           DEBUG RESPONSE             │
│                                      │
│   Error • Corrected Query • Tips     │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│          FRONTEND OUTPUT             │
│       Displays Debugging Results     │
└──────────────────────────────────────┘

           DATABASE MODULE
        SQLite Query Execution
```

---

## ⚙️ Component Description

| Component | Responsibility |
|---|---|
| Frontend | Accepts SQL input and displays results |
| Flask API | Handles requests from the frontend |
| SQL Analyzer | Checks queries for supported errors |
| Correction Module | Suggests fixes for supported errors |
| Explanation Module | Explains detected issues |
| SQLite Database | Supports local SQL query execution |

## 🔄 Data Flow

1. The user enters an SQL query.
2. JavaScript sends the query to the Flask API.
3. The backend analyzes the query.
4. The analyzer detects supported errors.
5. The system prepares corrections and explanations.
6. The response is returned to the frontend.
7. The debug console displays the results.

---

## 🛠️ Technology Stack

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python, Flask, Flask-CORS
- **Database:** SQLite
- **Development:** Visual Studio Code, GitHub
