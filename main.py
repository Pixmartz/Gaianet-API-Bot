import requests
import time
import random
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API URL and model from environment variables
API_URL = os.getenv("API_URL")
MODEL = os.getenv("MODEL")

def ask_question(question):
    url = API_URL
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful, respectful, and honest assistant. Always answer accurately, while being safe."},
            {"role": "user", "content": question}
        ],
        "model": MODEL
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response content: {response.content}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    
    return None

def save_response_to_file(response, folder, index):
    try:
        # Extract the assistant's answer from the response
        answer = response['choices'][0]['message']['content']
        filename = os.path.join(folder, f"response_{index}.txt")
        with open(filename, 'w') as file:
            file.write(answer)
        print(f"Response saved to {filename}")
    except Exception as e:
        print(f"Failed to save response to file: {e}")

def read_initial_question(filename):
    try:
        with open(filename, 'r') as file:
            question = file.readline().strip()
        return question
    except Exception as e:
        print(f"Failed to read initial question from file: {e}")
        return None

def extract_question_from_response(response):
    try:
        # Assuming the response is a paragraph or sentence, extract the last sentence to form a new question
        answer = response['choices'][0]['message']['content']
        sentences = answer.split('.')
        if len(sentences) > 1:
            new_question = sentences[-2].strip() + '?'  # Use the second last sentence as the new question
        else:
            new_question = sentences[0].strip() + '?'
        return new_question
    except Exception as e:
        print(f"Failed to extract question from response: {e}")
        return None

def save_individual_question_to_file(question, folder, index):
    try:
        filename = os.path.join(folder, f"generated_question_{index}.txt")
        with open(filename, 'w') as file:
            file.write(question)
        print(f"Individual question saved to {filename}")
    except Exception as e:
        print(f"Failed to save individual question to file: {e}")

if __name__ == "__main__":
    question = read_initial_question("questions.txt")
    if question:
        # Create a directory based on the current timestamp inside 'logs'
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        log_folder = "logs"
        os.makedirs(os.path.join(log_folder, timestamp), exist_ok=True)
        timestamp_folder = os.path.join(log_folder, timestamp)
        
        i = 0
        while True:
            response = ask_question(question)
            if response:
                save_response_to_file(response, timestamp_folder, i + 1)
                # Get the next question from the response
                question = extract_question_from_response(response)
                if not question:
                    print("Failed to extract a new question from the response. Exiting loop.")
                    break
                i += 1
                save_individual_question_to_file(question, timestamp_folder, i)
            else:
                print(f"Failed to get a response for iteration {i}.")
                break
            delay = random.randint(1000, 2000)  # Random time between 1000 to 2000 seconds
            print(f"Sleeping for {delay} seconds.")
            time.sleep(delay)
    else:
        print("No initial question to process.")
