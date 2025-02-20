let step = 0;
let botResponse = '';
let registrationDetails = {};  // Temporary storage for walk-in registration details

// Map video commands to the video URLs
const videoMap = {
    "abcd": "../videos/lang.mp4",
    "language_selection": "../videos/first.mp4",
    "production_services": "../videos/second.mp4",
    "four": "../videos/four.mp4",
    "five": "../videos/five.mp4",
    "production_services1": "../videos/third.mp4",
    "three": "../videos/third.mp4",
    "confirmation": "/videos/last.mp4",
    "appointment_confirmed": "/videos/appointment_confirmed.mp4",
    "doctor_selection": "/videos/doctor_selection.mp4",
    "upi_payment": "/videos/upi.mp4"
};

async function playVideosSequentially() {
    await playVideo("production_services");  // Play first video
    await new Promise(resolve => setTimeout(resolve));  // Wait for 5 seconds after the first video
    await playVideo("production_services1");   // Play second video
}

function startRecognition() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (SpeechRecognition) {
        const recognition = new SpeechRecognition();
        recognition.lang = 'en-US';
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        recognition.start();

        recognition.onresult = function(event) {
            const speechResult = event.results[0][0].transcript;
            console.log('Recognized: ' + speechResult);
            document.getElementById('user-input').value = speechResult;
            sendMessageFromInput();  // Optionally, send the message right away
        };

        recognition.onerror = function(event) {
            console.error('Speech recognition error', event.error);
        };

        recognition.onend = function() {
            console.log('Speech recognition service disconnected');
        };
    } else {
        alert("This browser does not support speech recognition. Please use Google Chrome.");
    }
}

function startChat() {
    document.getElementById("start-chat-btn").style.display = "none";
    document.getElementById("chat-container").style.display = "block";
    document.getElementById("user-input").disabled = false;
    document.getElementById("welcome-message").style.display = "block";
    playVideo("abcd");
}

function displayMessage(message, sender) {
    const chatBox = document.getElementById("chat-box");
    
     if (!chatBox) {
        console.error("Error: chat-box element not found.");
        return; // Exit the function if element not found
    }
    const messageContainer = document.createElement("div");
    messageContainer.classList.add(sender === "user" ? "user-message" : "bot-message", "message");
    messageContainer.innerHTML = `<p>${message}</p>`;
    chatBox.appendChild(messageContainer);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function playVideo(videoId) {
    return new Promise((resolve) => {
        const videoContainer = document.getElementById("video-container");
        const responseVideo = document.getElementById("response-video");

        const videoURL = videoMap[videoId];
        if (videoURL) {
            responseVideo.src = videoURL;
            videoContainer.style.display = "flex";
            responseVideo.play();
            responseVideo.onended = resolve;
        } else {
            videoContainer.style.display = "none";
            resolve();
        }
    });
}

function sendMessageFromInput() {
    const userInput = document.getElementById("user-input").value.trim();
    if (userInput) {
        document.getElementById("user-input").value = ""; // Clear the input field
        sendMessage(userInput); // Pass the input to the chatbot logic
    } else {
        alert("Please enter a message before sending!");
    }
}

async function sendMessage(userMessage) {
    const chatBox = document.getElementById("chat-box");
    displayMessage(userMessage, "user");

    try {
        switch (step) {
            case 0:
                botResponse = await fetchResponse("/select_lang", { user_string: userMessage });
                displayMessage(`You selected ${botResponse.selected_language}. We provide 3 services: 
                    <ul>
                      <li>Step Digital</li>
                      <li>Step Production</li>
                      <li>Step Tech</li>
                    </ul>`, "bot");
                playVideo("language_selection");
                step = 1;
                break;
            case 1:
                botResponse = await fetchResponse("/select_type", { user_string: userMessage });

                if (botResponse.selected_service === "Digital") {
                    displayMessage(`Okay, you selected Step Digital. Which area are you interested in? 
                        <ul>
                            <li>1. Performance Marketing</li>
                            <li>2. Search Engine Optimisation</li>
                            <li>3. Social Media Management</li>
                        </ul>`, "bot");
                    playVideo("digital_services");
                } else if (botResponse.selected_service === "Production") {
                    displayMessage(`Okay, you selected Step Production. What specific service are you looking for? 
                        <ul>
                            <li>1. Video Production </li>
                            <li>2. Ad Shoot</li>
                            <li>3. Video Editing</li>
                            <li>5. Product and Fashion Shoot</li>
                        </ul>`, "bot");
                    playVideosSequentially();  // Play production videos sequentially with a delay
                    step = 2;
                } else if (botResponse.selected_service === "Tech") {
                    displayMessage(`Okay, you selected Step Tech. Please choose the service you need help with:
                        <ul>
                            <li>1. Mobile or Web App Development</li>
                            <li>2. Custom Software Development</li>
                            <li>3. Data Analytics Service</li>
                            <li>4. Automation Solutions</li>
                        </ul>`, "bot");
                    playVideo("tech_services");
                } else {
                    displayMessage("Sorry, I didn't understand that. Please select a valid service category.", "bot");
                    step = 1;
                    break;
                }
                break;

            case 2:
                displayMessage("Thanks for choosing Video Editing. Can you please tell me your name?", "bot");
                playVideo("four");
                step = 3;
                break;
            case 3:
                botResponse = await fetchResponse("/extract_name", { user_string: userMessage });
                if (botResponse.name) {
                    registrationDetails.name = botResponse.name;
                    displayMessage(`Thanks, ${botResponse.name}. Please Share your phone number so we contact you.`, "bot");
                    step = 4;
                    playVideo("five")
                } else {
                    displayMessage("I'm sorry, I couldn't find a name in your response. Could you please state your name again?", "bot");
                    step = 3;
                }
                break;
            case 4:
                registrationDetails.contactNumber = userMessage;
                displayMessage(`Thank you, ${registrationDetails.name}. We will contact you shortly. Have a great day!`, "bot");
                playVideo("confirmation");

                step = 0;
                break;
        }
    } catch (error) {
        displayMessage("There was an error processing your request. Please try again.", "bot");
        console.error("Error:", error);
    }
}

async function fetchResponse(url, data) {
    const response = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });
    return await response.json();
}