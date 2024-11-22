document.getElementById("loginForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:5001/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
    });

    const result = await response.json();
    const messageDiv = document.getElementById("message");

    if (response.ok) {
        messageDiv.textContent = "Login successful!";
        messageDiv.style.color = "green";
    } else {
        messageDiv.textContent = result.message || "An error occurred.";
    }
});
