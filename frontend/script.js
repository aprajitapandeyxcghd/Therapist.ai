document.getElementById("avatarName").innerText = localStorage.getItem("selectedAvatar");

async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    displayMessage("You: " + userInput);
    document.getElementById("user-input").value = "";

    const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput, avatar: localStorage.getItem("selectedAvatar") }),
    });

    const data = await response.json();
    displayMessage("AI: " + data.response);
    playVoiceResponse(data.audioUrl);
}

function displayMessage(message) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("p");
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
}

function playVoiceResponse(url) {
    const audio = new Audio(url);
    audio.play();
}

function startVoiceInput() {
    // Implement Web Speech API for voice input
}
