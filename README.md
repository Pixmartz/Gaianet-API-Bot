# Gaianet API Bot

This repository contains a simple Python script designed to interact with the GaiaNet API for asking questions and saving the responses to text files. The script is flexible and allows for easy modification to use different API endpoints and models.

## Description

The Gaianet API Bot is a tool for automating queries to the GaiaNet AI API. Users can provide a list of questions in a text file, and the script will send these questions to the API, receive the responses, and save each response in a separate text file. This can be useful for a variety of applications, including research, customer service automation, and more.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Pixmartz/Gaianet-API-Bot.git
   cd gaianet-api-bot
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Usage

1. Add your questions to `questions.txt`, one question per line.

2. Run the script:
   ```sh
   python main.py
   ```

3. The responses will be saved in separate text files named `response_1.txt`, `response_2.txt`, etc.

### Example

Here is an example `questions.txt` file:
```
What is the capital of France?
How does the GaiaNet API work?
```

When you run the script, it will generate the following files:
- `response_1.txt` with the content:
  ```
  The capital of France is Paris.
  ```
- `response_2.txt` with the content:
  ```
  The GaiaNet API is a robust and scalable interface that allows...
  ```

### Changing the API Endpoint and Model

If you want to change the API endpoint and model, you need to update the `ask_question` function in the `main.py` script. 

#### To use the new API endpoint:
```python
url = "https://chemistry.us.gaianet.network/v1/chat/completions"
```

#### To use the new model:
```python
payload = {
    "messages": [
        {"role": "system", "content": "You are a helpful, respectful, and honest assistant. Always answer accurately, while being safe."},
        {"role": "user", "content": question}
    ],
    "model": "Meta-Llama-3-8B-Instruct-Q5_K_M"
}
```

Here is how the updated `ask_question` function should look:
```python
def ask_question(question):
    url = "https://chemistry.us.gaianet.network/v1/chat/completions"
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful, respectful, and honest assistant. Always answer accurately, while being safe."},
            {"role": "user", "content": question}
        ],
        "model": "Meta-Llama-3-8B-Instruct-Q5_K_M"
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
```

### Contributing

Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.
