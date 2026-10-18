# 🤖 AI SQL Debugging Agent

<p align="center">
  <b>A Web-Based SQL Query Debugging Assistant</b>
  <br>
  Identify SQL errors, understand debugging suggestions, and improve your queries.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Backend-Flask-black?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-orange" alt="Frontend">
  <img src="https://img.shields.io/badge/Database-SQLite%20%7C%20MySQL-blue" alt="Database">
  <img src="https://img.shields.io/badge/Project-Academic-purple" alt="Academic Project">
</p>

---

## 📌 About the Project

The **AI SQL Debugging Agent** is a web-based application designed to help users identify SQL query errors and understand possible solutions.

The application uses a web frontend connected to a Python Flask backend. Users can submit SQL queries and receive debugging feedback based on the implemented query analysis logic.

The project aims to make SQL debugging easier for students, beginners, and developers.

## ✨ Features

- 🔍 SQL query analysis
- 🐞 Identification of supported SQL errors
- 💡 Helpful debugging suggestions
- 🖥️ Simple web-based user interface
- ⚙️ Python Flask backend
- 🗄️ SQLite and configurable MySQL support
- 🔗 Frontend and backend integration

> Note: Available features depend on the implementation in the current version.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| HTML | Web page structure |
| CSS | User interface styling |
| JavaScript | Frontend interaction |
| Python | Backend programming |
| Flask | Backend API |
| SQLite | Local database support |
| MySQL | Optional database support |
| GitHub | Source code hosting |

## 🏗️ System Architecture

```text
              USER
                |
                v
       WEB USER INTERFACE
       HTML / CSS / JS
                |
                v
        FLASK BACKEND API
                |
                v
       SQL QUERY ANALYZER
                |
                v
       ERROR ANALYSIS
                |
                v
     DEBUGGING SUGGESTIONS
                |
                v
        RESULTS DISPLAYED
          TO THE USER
