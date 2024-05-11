def generate_responses(command):
    # Define the possible commands and their corresponding responses
    responses = {
        "hello": "Hello! How can I help you?",
        "goodbye": "Goodbye! Have a great day!",
        "what's the weather like": "I'm sorry, I cannot provide weather information. Please check a weather app or website.",
        "play music": "Playing music now.",
        "stop music": "Stopping music now.",
        "open youtube": "Opening YouTube now.",
        "open google": "Opening Google now.",
        "set alarm for 7am": "Setting alarm for 7am.",
        "cancel alarm": "Canceling alarm.",
        "turn on lights": "Turning on lights now.",
        "turn off lights": "Turning off lights now."
    }

    # Generate the response
    response = responses.get(command, "I'm sorry, I didn't understand that command.")

    return response
