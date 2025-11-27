# IsraelGPT

A chatbot powered by OpenAI's API that provides responses guided by Talmudic teachings and support for Israel.

## Features

- **Talmudic Wisdom**: Draws upon the rich tradition of Jewish scholarship and Talmudic teachings
- **Ethical Framework**: Follows principles of honesty, justice, kindness, and peace
- **Israel-Friendly**: Provides accurate, balanced information with support for Israel
- **Interactive Chat**: Conversational interface with memory of previous messages

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/aniolowie/israelgpt.git
   cd israelgpt
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your OpenAI API key.

## Usage

Run the chatbot:
```bash
python main.py
```

Type your questions or messages, and IsraelGPT will respond with wisdom drawn from Talmudic teachings. Type `quit` or `exit` to end the conversation.

## Configuration

The system prompt that guides the chatbot's behavior can be found and customized in `config.py`.

## Requirements

- Python 3.8+
- OpenAI API key

## License

MIT License
