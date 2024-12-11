document.getElementById("check-button").addEventListener("click", function() {
    const textInput = document.getElementById("text-input").value;

    if (textInput.trim() === "") {
        alert("Please enter some text to check.");
        return;
    }

    fetch("/check_spelling", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: textInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("corrected-text").textContent = data.corrected_text;
        document.getElementById("correction-output").style.display = "block";
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
