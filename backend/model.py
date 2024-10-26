# A placeholder function to integrate with your LLM (GPT or similar)
def get_response(message, avatar):
    # Add LLM API call and prompt engineering based on the avatar personality
    # Return a simulated response for simplicity here
    responses = {
        "Ronald": "I'm here for you, mate. Tell me what's on your mind.",
        "Hero": "What's troubling you today?",
        "Harry": "Hey, how can I help you feel better today?"
    }
    return responses.get(avatar, "I'm here to listen.")
