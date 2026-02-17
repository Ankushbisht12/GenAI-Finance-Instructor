const BASE_URL = "http://127.0.0.1:8000";

// ===============================
// General Financial Advice
// ===============================
async function getGeneral() {
    const resultDiv = document.getElementById("generalResult");
    resultDiv.innerText = "Loading...";

    try {
        const response = await fetch(`${BASE_URL}/explain/general`);

        const data = await response.json();

        if (!response.ok) {
            resultDiv.innerText = data.detail || "Server error occurred.";
            return;
        }

        resultDiv.innerText = data.response || "No response received.";

    } catch (error) {
        resultDiv.innerText = "Backend not reachable.";
        console.error("Error:", error);
    }
}


// ===============================
// Explain Financial Text
// ===============================
async function explainText() {
    const text = document.getElementById("textInput").value;
    const resultDiv = document.getElementById("textResult");

    if (!text.trim()) {
        resultDiv.innerText = "Please enter some text.";
        return;
    }

    resultDiv.innerText = "Loading...";

    try {
        const response = await fetch(`${BASE_URL}/explain/text`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();

        if (!response.ok) {
            resultDiv.innerText = data.detail || "Server error occurred.";
            return;
        }

        resultDiv.innerText = data.response || "No response received.";

    } catch (error) {
        resultDiv.innerText = "Backend not reachable.";
        console.error("Error:", error);
    }
}


// ===============================
// Ask Financial Question
// ===============================
async function askQuestion() {
    const question = document.getElementById("questionInput").value;
    const resultDiv = document.getElementById("questionResult");

    if (!question.trim()) {
        resultDiv.innerText = "Please enter a question.";
        return;
    }

    resultDiv.innerText = "Loading...";

    try {
        const response = await fetch(`${BASE_URL}/ask`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question: question })
        });

        const data = await response.json();

        if (!response.ok) {
            resultDiv.innerText = data.detail || "Server error occurred.";
            return;
        }

        resultDiv.innerText = data.response || "No response received.";

    } catch (error) {
        resultDiv.innerText = "Backend not reachable.";
        console.error("Error:", error);
    }
}
