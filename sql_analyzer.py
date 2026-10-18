import re


# ---------------------------------------------------
# MAIN SQL ANALYZER
# ---------------------------------------------------

def analyze_sql(query):

    original_query = query
    corrected_query = query

    # Default response
    result = {
        "hasError": False,
        "error": "No common SQL error detected.",
        "correctedQuery": query,
        "explanation": "The SQL query passed the basic debugging checks.",
        "suggestion": "The query looks structurally correct. You can execute it."
    }

    # ------------------------------------------------
    # 1. EMPTY QUERY
    # ------------------------------------------------

    if not query.strip():

        return {
            "hasError": True,
            "error": "SQL query is empty.",
            "correctedQuery": "",
            "explanation": "A SQL statement is required for debugging.",
            "suggestion": "Enter a SELECT, INSERT, UPDATE, DELETE, or other SQL statement."
        }

    # ------------------------------------------------
    # 2. FORM → FROM
    # ------------------------------------------------

    if re.search(r"\bFORM\b", corrected_query, re.IGNORECASE):

        corrected_query = re.sub(
            r"\bFORM\b",
            "FROM",
            corrected_query,
            flags=re.IGNORECASE
        )

        return {
            "hasError": True,
            "error": "Invalid SQL keyword: FORM",
            "correctedQuery": corrected_query,
            "explanation":
                "FORM is not a valid SQL keyword for specifying a table. "
                "The correct keyword is FROM.",
            "suggestion":
                "Check the spelling of SQL keywords carefully."
        }

    # ------------------------------------------------
    # 3. SELEC → SELECT
    # ------------------------------------------------

    if re.search(r"\bSELEC\b", corrected_query, re.IGNORECASE):

        corrected_query = re.sub(
            r"\bSELEC\b",
            "SELECT",
            corrected_query,
            flags=re.IGNORECASE
        )

        return {
            "hasError": True,
            "error": "Invalid SQL keyword: SELEC",
            "correctedQuery": corrected_query,
            "explanation":
                "SELEC is an incomplete SQL keyword. "
                "SELECT is used to retrieve data.",
            "suggestion":
                "Check SQL keyword spelling."
        }

    # ------------------------------------------------
    # 4. SELCT → SELECT
    # ------------------------------------------------

    if re.search(r"\bSELCT\b", corrected_query, re.IGNORECASE):

        corrected_query = re.sub(
            r"\bSELCT\b",
            "SELECT",
            corrected_query,
            flags=re.IGNORECASE
        )

        return {
            "hasError": True,
            "error": "Invalid SQL keyword: SELCT",
            "correctedQuery": corrected_query,
            "explanation":
                "SELCT is a misspelled SELECT keyword.",
            "suggestion":
                "Use SELECT when retrieving records."
        }

    # ------------------------------------------------
    # 5. UPDATE WITHOUT WHERE
    # ------------------------------------------------

    if re.match(
        r"^\s*UPDATE\s+",
        query,
        re.IGNORECASE
    ) and not re.search(
        r"\bWHERE\b",
        query,
        re.IGNORECASE
    ):

        return {
            "hasError": True,
            "error": "UPDATE query does not contain a WHERE condition.",
            "correctedQuery": query,
            "explanation":
                "An UPDATE statement without WHERE can modify every row "
                "in the table.",
            "suggestion":
                "Add a WHERE condition to update only the required records."
        }

    # ------------------------------------------------
    # 6. DELETE WITHOUT WHERE
    # ------------------------------------------------

    if re.match(
        r"^\s*DELETE\s+FROM\s+",
        query,
        re.IGNORECASE
    ) and not re.search(
        r"\bWHERE\b",
        query,
        re.IGNORECASE
    ):

        return {
            "hasError": True,
            "error": "DELETE query does not contain a WHERE condition.",
            "correctedQuery": query,
            "explanation":
                "DELETE without WHERE can remove all records from a table.",
            "suggestion":
                "Add a WHERE condition before executing the DELETE query."
        }

    # ------------------------------------------------
    # 7. SELECT WITHOUT FROM
    # ------------------------------------------------

    if re.match(
        r"^\s*SELECT\b",
        query,
        re.IGNORECASE
    ) and not re.search(
        r"\bFROM\b",
        query,
        re.IGNORECASE
    ):

        # Allow SELECT 1, SELECT 5+5, etc.
        if not re.search(
            r"^\s*SELECT\s+[\d\+\-\*\/\s]+;?\s*$",
            query,
            re.IGNORECASE
        ):

            return {
                "hasError": True,
                "error": "SELECT statement may be missing a FROM clause.",
                "correctedQuery": query,
                "explanation":
                    "A SELECT statement retrieving table data normally "
                    "requires a FROM clause.",
                "suggestion":
                    "Check whether the table name and FROM keyword are present."
            }

    # ------------------------------------------------
    # 8. MISSING SELECT COLUMNS
    # ------------------------------------------------

    if re.match(
        r"^\s*SELECT\s+FROM\b",
        query,
        re.IGNORECASE
    ):

        corrected_query = re.sub(
            r"^\s*SELECT\s+FROM\b",
            "SELECT * FROM",
            query,
            flags=re.IGNORECASE
        )

        return {
            "hasError": True,
            "error": "SELECT is missing a column list.",
            "correctedQuery": corrected_query,
            "explanation":
                "The SELECT keyword must be followed by columns or *.",
            "suggestion":
                "Use SELECT column_name FROM table_name or SELECT * FROM table_name."
        }

    # ------------------------------------------------
    # 9. DOUBLE COMMA
    # ------------------------------------------------

    if ",," in query:

        corrected_query = query.replace(",,", ",")

        return {
            "hasError": True,
            "error": "Extra comma detected.",
            "correctedQuery": corrected_query,
            "explanation":
                "Two consecutive commas are not valid in a normal SQL column list.",
            "suggestion":
                "Remove the extra comma."
        }

    # ------------------------------------------------
    # 10. UNBALANCED BRACKETS
    # ------------------------------------------------

    if query.count("(") != query.count(")"):

        return {
            "hasError": True,
            "error": "Unbalanced parentheses detected.",
            "correctedQuery": query,
            "explanation":
                "The number of opening and closing parentheses does not match.",
            "suggestion":
                "Check function calls, conditions, and subqueries."
        }

    # ------------------------------------------------
    # 11. UNBALANCED SINGLE QUOTES
    # ------------------------------------------------

    if query.count("'") % 2 != 0:

        return {
            "hasError": True,
            "error": "Unclosed single quote detected.",
            "correctedQuery": query,
            "explanation":
                "A text value starts with a single quote but does not have "
                "a matching closing quote.",
            "suggestion":
                "Make sure every text value has opening and closing quotes."
        }

    # ------------------------------------------------
    # 12. MISSING SQL KEYWORD
    # ------------------------------------------------

    first_word_match = re.match(
        r"^\s*([A-Za-z]+)",
        query
    )

    if first_word_match:

        first_word = first_word_match.group(1).upper()

        valid_keywords = {
            "SELECT",
            "INSERT",
            "UPDATE",
            "DELETE",
            "CREATE",
            "DROP",
            "ALTER",
            "WITH"
        }

        if first_word not in valid_keywords:

            return {
                "hasError": True,
                "error": f"Unknown SQL command: {first_word}",
                "correctedQuery": query,
                "explanation":
                    "The first word of the query is not recognized as a "
                    "common SQL command.",
                "suggestion":
                    "Start the query with a valid SQL command such as SELECT, "
                    "INSERT, UPDATE, or DELETE."
            }

    # ------------------------------------------------
    # 13. BASIC SELECT STRUCTURE
    # ------------------------------------------------

    if re.match(
        r"^\s*SELECT\b",
        query,
        re.IGNORECASE
    ):

        if not re.search(
            r"\bFROM\b",
            query,
            re.IGNORECASE
        ):

            if not re.search(
                r"^\s*SELECT\s+[\d\+\-\*\/\s]+;?\s*$",
                query,
                re.IGNORECASE
            ):

                return {
                    "hasError": True,
                    "error": "FROM clause is missing.",
                    "correctedQuery": query,
                    "explanation":
                        "The query starts with SELECT but no FROM clause "
                        "was found.",
                    "suggestion":
                        "Add FROM followed by the table name."
                }

    # ------------------------------------------------
    # QUERY LOOKS VALID
    # ------------------------------------------------

    return result