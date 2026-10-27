# AI Memory Chatbot

## About
An AI chatbot built using Python, Flask, HTML, CSS, JavaScript, and Google's Gemini API.

## Features
- AI-generated responses
- Conversation history
- System prompt
- Recent message context management
- API error handling
- Environment variable for API key

## Requirements
- Python
- Gemini API key

## Installation
1. Install dependencies:
   `pip install -r requirements.txt`
2. Create a `.env` file in the project folder.
3. Add your API key:
   `GEMINI_API_KEY=your_api_key_here`
4. Start the application:
   `python app.py`
5. Open http://127.0.0.1:5000 in your browser.

## Security
Never upload your `.env` file or API key to GitHub.

## Limitation
Conversation history is stored in memory and may be lost when the server restarts.