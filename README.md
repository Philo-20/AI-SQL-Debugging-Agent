# 🤖 AI SQL Debugging Agent

### Intelligent SQL Error Detection, Correction & Explanation System

---

## 📖 1. Project Overview

AI SQL Debugging Agent is a web-based application designed to help users identify and understand SQL query errors.

The system analyzes SQL queries, detects common syntax and structural problems, suggests corrected queries, explains the detected error, and provides useful debugging suggestions.

The project combines a JavaScript-based frontend with a Python Flask backend and SQLite database.

---

## ✨ 2. Features

| Feature | Description |
|---|---|
| 🔍 SQL Error Detection | Detects common SQL syntax and structural errors |
| 🛠️ Query Correction | Generates corrected versions for supported errors |
| 💡 Error Explanation | Explains why the SQL query is incorrect |
| 📌 Suggestions | Provides recommendations for fixing the query |
| ▶️ SQL Execution | Executes SQL queries against the sample database |
| 🗄️ SQLite Database | Uses SQLite for local database operations |
| 🕘 Debugging History | Stores recent debugging queries in the browser |
| 🌐 Web Interface | Provides a simple interactive SQL editor |

---

## 🏗️ 3. System Architecture

```text
                  USER
                   │
                   ▼
          ┌─────────────────┐
          │   SQL Editor    │
          │ HTML/CSS/JS     │
          └────────┬────────┘
                   │
                   │ HTTP POST
                   ▼
          ┌─────────────────┐
          │   Flask API     │
          │     app.py      │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │  SQL Analyzer   │
          │sql_analyzer.py  │
          └────────┬────────┘
                   │
          ┌────────┴────────┐
          ▼                 ▼
   Error Detection     Query Correction
          │                 │
          └────────┬────────┘
                   ▼
          Explanation & Tip
                   │
                   ▼
          ┌─────────────────┐
          │  Debug Console  │
          └─────────────────┘