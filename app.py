from flask import Flask, request, jsonify
from flask_cors import CORS

from database import create_database, execute_sql
from sql_analyzer import analyze_sql

app = Flask(__name__)
CORS(app)


# ---------------------------------------------------
# HOME
# ---------------------------------------------------

@app.route("/")
def home():
    return jsonify({
        "success": True,
        "message": "AI SQL Debugging Agent Backend is Running"
    })


# ---------------------------------------------------
# DEBUG SQL
# ---------------------------------------------------

@app.route("/api/debug", methods=["POST"])
def debug_sql():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "error": "No request data received."
            }), 400

        query = data.get("query", "").strip()

        if not query:
            return jsonify({
                "success": False,
                "error": "SQL query is empty."
            }), 400

        # Analyze query
        analysis = analyze_sql(query)

        return jsonify({
            "success": True,
            "query": query,
            "error": analysis["error"],
            "correctedQuery": analysis["correctedQuery"],
            "explanation": analysis["explanation"],
            "suggestion": analysis["suggestion"],
            "hasError": analysis["hasError"]
        })

    except Exception as error:

        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


# ---------------------------------------------------
# EXECUTE SQL
# ---------------------------------------------------

@app.route("/api/execute", methods=["POST"])
def execute_query():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "error": "No request data received."
            }), 400

        query = data.get("query", "").strip()

        if not query:
            return jsonify({
                "success": False,
                "error": "SQL query is empty."
            }), 400

        result = execute_sql(query)

        if "error" in result:

            return jsonify({
                "success": False,
                "error": result["error"]
            })

        return jsonify({
            "success": True,
            "result": result
        })

    except Exception as error:

        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


# ---------------------------------------------------
# START SERVER
# ---------------------------------------------------

if __name__ == "__main__":

    create_database()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )