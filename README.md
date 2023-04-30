# Telegram Search Assistant

A search assistance bot built with Telegram, FastAPI, and ChatGPT to handle natural language queries and generate responses.

## Installation

1. Clone the repository.
2. Install the required packages: `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory with your Telegram and OpenAI API keys:

4. Run the FastAPI server: `uvicorn app.main:app --host 0.0.0.0 --port 8000`.

## Usage

Interact with the Telegram bot by sending natural language queries. The bot will generate responses using ChatGPT.



telegram_search_assistant/
│
├── app/
│   ├── main.py
│   ├── chatgpt.py
│   └── utils.py
│
├── config/
│   └── settings.py
│
├── tests/
│   └── test_app.py
│
├── .env
├── Procfile
├── README.md
└── requirements.txt



