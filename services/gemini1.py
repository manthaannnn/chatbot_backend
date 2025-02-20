import os
from dotenv import load_dotenv
import google.generativeai as genai


def initialize_genai():
    """Initialize and configure the Generative AI model."""
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve the API key from environment variables
    api_key = os.getenv("GOOGLE_AI_API_KEY")

    if not api_key:
        raise EnvironmentError("API key not found. Make sure it's set in the .env file.")

    # Configure the API with the key
    genai.configure(api_key=api_key)

    # Define generation configuration
    generation_config = {
        "temperature": .5,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
    }

    # Create and return a model instance
    return genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

def get_response_from_ai(user_prompt: str, system_prompt: str) -> str:
    """Function that takes a user prompt and system prompt, then returns a response from the AI."""
    
    # Initialize the AI model
    model = initialize_genai()

    # Start a chat session
    chat_session = model.start_chat(
        history=[]
    )

    # Send the system prompt to set the context
    chat_session.send_message(system_prompt)

    # Send the user prompt and get the response
    response = chat_session.send_message(user_prompt)

    # Return the text of the response
    return response.text


# Example code to test and print the AI response
if __name__ == "__main__":
    # Define a user prompt and system prompt
    user_prompt = "Tell me a fun fact about space."
    system_prompt = "You are a helpful AI assistant that answers questions."

    # Get the response from the AI model
    response = get_response_from_ai(user_prompt, system_prompt)

    # Print the response
    print(f"AI Response: {response}")
