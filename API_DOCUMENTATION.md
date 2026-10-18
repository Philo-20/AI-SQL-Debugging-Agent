
# 🔌 API Documentation

## Overview

This document describes the REST API used by the AI SQL Debugging Agent.

## 🌐 Base URL

```text
http://127.0.0.1:5000
```

## 1. Health Check

**Method:** `GET`

**Endpoint:** `/`

Checks whether the backend server is running.

### Example Response

```json
{
  "success": true,
  "message": "AI SQL Debugging Agent Backend is Running"
}
```

## 2. SQL Debugging

**Method:** `POST`

**Endpoint:** `/api/debug`

Analyzes a SQL query and returns debugging information.

### Request Body

```json
{
  "query": "SELECT name FORM users;"
}
```

### Example Response

```json
{
  "success": true,
  "hasError": true,
  "error": "Invalid SQL keyword: FORM",
  "correctedQuery": "SELECT name FROM users;",
  "explanation": "FORM is an incorrect keyword. Use FROM to specify the table.",
  "suggestion": "Check SQL keyword spelling."
}
```

## 3. SQL Execution

**Method:** `POST`

**Endpoint:** `/api/execute`

Executes a query against the configured database.

### Request Body

```json
{
  "query": "SELECT * FROM users;"
}
```

### Example Response

```json
{
  "success": true,
  "columns": ["id", "name", "email", "age"],
  "rows": []
}
```

## ⚠️ Important

The endpoint names, JSON fields, and response examples above are illustrative. Confirm them against your actual `backend/app.py` before publishing this document.
