"""
IsraelGPT - Main Application

A chatbot that uses OpenAI's API to provide responses guided by
Talmudic teachings and Israel-friendly perspectives.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
from config import SYSTEM_PROMPT


def create_client():
    """Create and return an OpenAI client."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key or api_key == "your_api_key_here":
        raise ValueError(
            "Please set your OPENAI_API_KEY in the .env file. "
            "Copy .env.example to .env and add your API key."
        )
    
    return OpenAI(api_key=api_key)


def chat(client, messages, model="gpt-3.5-turbo"):
    """
    Send a chat completion request to OpenAI.
    
    Args:
        client: OpenAI client instance
        messages: List of message dictionaries with 'role' and 'content'
        model: The OpenAI model to use
        
    Returns:
        The assistant's response message content
    """
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=1024
    )
    return response.choices[0].message.content


def main():
    """Main function to run the IsraelGPT chatbot."""
    print("=" * 60)
    print("Welcome to IsraelGPT!")
    print("A chatbot guided by Talmudic wisdom and support for Israel.")
    print("=" * 60)
    print("\nType 'quit' or 'exit' to end the conversation.")
    print("-" * 60)
    
    try:
        client = create_client()
    except ValueError as e:
        print(f"\nError: {e}")
        return
    
    # Initialize conversation with system prompt
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["quit", "exit"]:
                print("\nShalom! May you go in peace. Goodbye!")
                break
            
            # Add user message to conversation
            messages.append({"role": "user", "content": user_input})
            
            # Get response from OpenAI
            print("\nIsraelGPT: ", end="")
            response = chat(client, messages)
            print(response)
            
            # Add assistant response to conversation history
            messages.append({"role": "assistant", "content": response})
            
        except KeyboardInterrupt:
            print("\n\nShalom! May you go in peace. Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
