import os
from dotenv import load_dotenv
from termcolor import colored
import prompt

""" 
    Enhance a prompt using OpenAI's API. (See prompt.py for more details.)
    Usage: python main.py
    
    Environment variables:
    - OPENAI_API_KEY: OpenAI API key
    - OPENAI_MODEL: OpenAI model to use
    - TEMPERATURE: Temperature to use (optional)
"""


def main():
    load_dotenv(".env")
    openai_key = os.environ.get("OPENAI_API_KEY")
    openai_model = os.environ.get("OPENAI_MODEL")
    temperature = os.environ.get("TEMPERATURE")
    temperature = float(temperature) if temperature is not None else 0.5

    if openai_key is None:
        raise Exception("OPENAI_API_KEY environment variable not found.")
    if openai_model is None:
        raise Exception("OPENAI_MODEL environment variable not found.")

    while True:
        try:
            user_input = input("Enter a prompt (CTRL + C to exit):\n")
            print(colored(f"\nEnhancing your prompt...\n", 'green', attrs=['bold']))

            response = prompt.enhance_prompt(openai_key, user_input, openai_model, temperature)

            print(colored('Original prompt score: ', 'yellow', attrs=['bold']), end="")
            print(f"{response['original_prompt_score']}/10")

            print(colored('Reason for score: ', 'yellow', attrs=['bold']), end="")
            print(f"{response['reason_for_score']}")

            print(colored('Enhanced prompt: ', 'yellow', attrs=['bold']), end="")
            print(f"{response['enhanced_prompt']}")

            print(colored('List of enhancements:\n', 'yellow', attrs=['bold']), end="")
            for idx, enhancement in enumerate(response['list_of_enhancements']):
                print(f"{idx+1}. {enhancement}")
            print("\n")

        except KeyboardInterrupt:
            print("\nExiting program.")
            break


if __name__ == "__main__":
    main()
