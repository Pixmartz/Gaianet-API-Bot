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
   cd Gaianet-API-Bot
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Usage

1. Add your initial question to `questions.txt`. Ensure it is a single line. This question will be used to start the loop, and subsequent questions will be generated based on the responses. 

2. Run the script:
   ```sh
   python main.py
   ```

3. Files Generated
    - The responses and generated questions will be saved in separate text files within a timestamped folder under the `logs` directory.
    - Response files are named `response_1.txt`, `response_2.txt`, etc.
    - Generated question files are named `generated_question_1.txt`, `generated_question_2.txt`, etc.
    - All these files will be organized into a folder named with the current timestamp (YMDHIS) inside the `logs` directory.

4. This action has a delay time between 1000 and 2000 seconds. You can adjust it according to your preference. 

### Example

Here is an example `questions.txt` file:
```
What can I cook with chicken?
```

When you run the script, it will generate the following files:
- `response_1.txt` with the content:
  ```
  Chicken Enchilada Bake: Cut chicken breasts into bite-sized pieces and set aside...
  ```
- `generated_question_1.txt` with the content:
  ```
  In a skillet or in a casserole dish, mix the chicken with canned enchilada ...
  ```

### Changing the API Endpoint and Model

If you want to change the API endpoint and model, you need to rename `sample.env` file to `.env` then update `API_URL` and `MODEL` to yours.

### How to Run background?
Install `Screen` on Ubuntu:
```
apt install screen
```

Start the bot in background mode with a name (replace `gaianetbot`):
```
screen -S gaianetbot
```

Then run the bot:  
```
python main.py
```

To return back your terminal, press `Ctrl + A` then `D` and finally hit Enter:
```
screen -r gaianetbot
```
### Contributing

Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.
