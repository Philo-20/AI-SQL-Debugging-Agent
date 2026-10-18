const sqlQuery = document.getElementById("sqlQuery");

const debugBtn = document.getElementById("debugBtn");
const clearBtn = document.getElementById("clearBtn");

const status = document.getElementById("status");

const consoleEmpty = document.getElementById("consoleEmpty");
const resultGrid = document.getElementById("resultGrid");

const errorResult = document.getElementById("errorResult");
const correctedResult = document.getElementById("correctedResult");
const explanationResult = document.getElementById("explanationResult");
const suggestionResult = document.getElementById("suggestionResult");

const lineNumbers = document.getElementById("lineNumbers");

const historyList = document.getElementById("historyList");
const historyEmpty = document.getElementById("historyEmpty");
const clearHistoryBtn = document.getElementById("clearHistoryBtn");


// ---------------------------------------------------
// BACKEND URL
// ---------------------------------------------------

const API_URL = "http://127.0.0.1:5000";


// ---------------------------------------------------
// LINE NUMBERS
// ---------------------------------------------------

function updateLineNumbers() {

    const lines = sqlQuery.value.split("\n").length;

    let output = "";

    for (let i = 1; i <= lines; i++) {
        output += `<span>${i}</span>`;
    }

    lineNumbers.innerHTML = output;
}


// ---------------------------------------------------
// DEBUG SQL
// ---------------------------------------------------

async function debugSQL() {

    const query = sqlQuery.value.trim();

    if (query === "") {

        alert("Please enter a SQL query.");

        sqlQuery.focus();

        return;
    }


    // Busy state

    status.textContent = "analyzing";
    status.className = "window-status is-busy";

    debugBtn.disabled = true;

    debugBtn.innerHTML = "Analyzing...";


    try {

        const response = await fetch(
            `${API_URL}/api/debug`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    query: query
                })
            }
        );


        const data = await response.json();


        if (!response.ok || !data.success) {

            throw new Error(
                data.error || "Backend error occurred."
            );
        }


        displayResult(
            data.error,
            data.correctedQuery,
            data.explanation,
            data.suggestion,
            data.hasError
        );


        saveHistory(
            query,
            data.hasError
        );


    } catch (error) {

        console.error(error);

        status.textContent = "backend error";

        status.className =
            "window-status is-error";


        consoleEmpty.hidden = false;

        resultGrid.hidden = true;


        alert(
            "Unable to connect to the SQL Debugging Agent backend.\n\n" +
            "Make sure Flask is running on port 5000."
        );


    } finally {

        debugBtn.disabled = false;

        debugBtn.innerHTML =
            '<span class="btn-icon">▶</span> Debug SQL';
    }
}


// ---------------------------------------------------
// DISPLAY RESULT
// ---------------------------------------------------

function displayResult(
    error,
    correctedQuery,
    explanation,
    suggestion,
    hasError
) {

    consoleEmpty.hidden = true;

    resultGrid.hidden = false;


    errorResult.textContent = error;

    correctedResult.textContent =
        correctedQuery;


    explanationResult.textContent =
        explanation;


    suggestionResult.textContent =
        suggestion;


    if (hasError) {

        status.textContent =
            "error detected";

        status.className =
            "window-status is-error";

    } else {

        status.textContent =
            "query looks good";

        status.className =
            "window-status is-good";
    }
}


// ---------------------------------------------------
// CLEAR EDITOR
// ---------------------------------------------------

function clearEditor() {

    sqlQuery.value = "";

    updateLineNumbers();

    consoleEmpty.hidden = false;

    resultGrid.hidden = true;

    status.textContent = "ready";

    status.className =
        "window-status";

    sqlQuery.focus();
}


clearBtn.addEventListener(
    "click",
    clearEditor
);


// ---------------------------------------------------
// KEYBOARD SHORTCUT
// Ctrl + Enter
// ---------------------------------------------------

sqlQuery.addEventListener(
    "keydown",
    function(event) {

        if (
            event.ctrlKey &&
            event.key === "Enter"
        ) {

            event.preventDefault();

            debugSQL();
        }
    }
);


// ---------------------------------------------------
// LINE NUMBER UPDATE
// ---------------------------------------------------

sqlQuery.addEventListener(
    "input",
    updateLineNumbers
);


// ---------------------------------------------------
// DEBUG BUTTON
// ---------------------------------------------------

debugBtn.addEventListener(
    "click",
    debugSQL
);


// ---------------------------------------------------
// LOCAL HISTORY
// ---------------------------------------------------

function saveHistory(query, hasError) {

    const history =
        JSON.parse(
            localStorage.getItem(
                "sqlDebugHistory"
            )
        ) || [];


    const item = {

        query: query,

        hasError: hasError,

        time: new Date().toLocaleString()
    };


    history.unshift(item);


    // Keep latest 10

    if (history.length > 10) {

        history.pop();
    }


    localStorage.setItem(
        "sqlDebugHistory",
        JSON.stringify(history)
    );


    displayHistory();
}


// ---------------------------------------------------
// DISPLAY HISTORY
// ---------------------------------------------------

function displayHistory() {

    const history =
        JSON.parse(
            localStorage.getItem(
                "sqlDebugHistory"
            )
        ) || [];


    historyList.innerHTML = "";


    if (history.length === 0) {

        historyEmpty.style.display =
            "block";

        return;
    }


    historyEmpty.style.display =
        "none";


    history.forEach(
        function(item) {

            const historyItem =
                document.createElement(
                    "div"
                );


            historyItem.className =
                "history-item";


            const statusClass =
                item.hasError
                    ? "error"
                    : "ok";


            const statusText =
                item.hasError
                    ? "error found"
                    : "checked";


            historyItem.innerHTML = `

                <div class="history-item-top">

                    <div class="history-query">
                        ${escapeHTML(item.query)}
                    </div>

                    <div class="history-time">
                        ${item.time}
                    </div>

                </div>

                <span class="history-badge ${statusClass}">
                    ${statusText}
                </span>
            `;


            historyList.appendChild(
                historyItem
            );
        }
    );
}


// ---------------------------------------------------
// CLEAR HISTORY
// ---------------------------------------------------

clearHistoryBtn.addEventListener(
    "click",
    function() {

        localStorage.removeItem(
            "sqlDebugHistory"
        );

        displayHistory();
    }
);


// ---------------------------------------------------
// PREVENT HTML INJECTION
// ---------------------------------------------------

function escapeHTML(text) {

    return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}


// ---------------------------------------------------
// INITIAL SETUP
// ---------------------------------------------------

updateLineNumbers();

displayHistory();

sqlQuery.focus();