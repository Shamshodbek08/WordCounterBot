# Simple Text Analysis Telegram Bot

This is a simple Telegram bot that analyzes text sent by a user and provides the following information:
- Character, word, sentence, and paragraph counts.
- Estimated reading time at slow, average, and fast speeds.
- A word frequency analysis showing the top 5 most common words.
- A simple readability score based on the average word length.
- The output is formatted with emojis for a fun and engaging experience.

## Setup and Installation

Follow these steps to get the bot running.

### 1. Prerequisites

- Python 3.7+
- A Telegram account

### 2. Install Dependencies

You need to install the `python-telegram-bot` library. You can do this using pip:

```bash
pip install python-telegram-bot
```

### 3. Get a Telegram Bot Token

1.  Open Telegram and search for the **BotFather** user.
2.  Start a chat with BotFather and send the `/newbot` command.
3.  Follow the instructions to choose a name and username for your bot.
4.  BotFather will provide you with a unique **token**. Copy this token.

### 4. Configure the Bot

1.  Open the `telegram_bot.py` file.
2.  Find the line that says:
    ```python
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
    ```
3.  Replace `"YOUR_TELEGRAM_BOT_TOKEN"` with the token you received from BotFather.

### 5. Run the Bot

Once you have installed the dependencies and configured the token, you can run the bot with the following command:

```bash
python telegram_bot.py
```

Your bot is now running! You can open a chat with it on Telegram and send it any text to see the analysis.
