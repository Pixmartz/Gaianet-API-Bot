import requests

def ask_question(question):
    url = "https://0x8606ab7d93dcf9f92fb78a33ccf6bee45988a7c5.us.gaianet.network/v1/chat/completions"
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful, respectful, and honest assistant. Always answer accurately, while being safe."},
            {"role": "user", "content": question}
        ],
        "model": "stablelm-2-zephyr-1_6b-Q5_K_M"
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

def save_response_to_file(response, filename):
    try:
        # Extract the assistant's answer from the response
        answer = response['choices'][0]['message']['content']
        with open(filename, 'w') as file:
            file.write(answer)
        print(f"Response saved to {filename}")
    except Exception as e:
        print(f"Failed to save response to file: {e}")

def read_questions_from_file(filename):
    try:
        with open(filename, 'r') as file:
            questions = [line.strip() for line in file.readlines()]
        return questions
    except Exception as e:
        print(f"Failed to read questions from file: {e}")
        return []

if __name__ == "__main__":
    questions = read_questions_from_file("questions.txt")
    if questions:
        for i, question in enumerate(questions):
            response = ask_question(question)
            if response:
                filename = f"response_{i+1}.txt"
                save_response_to_file(response, filename)
            else:
                print(f"Failed to get a response for question {i+1}.")
    else:
        print("No questions to process.")
