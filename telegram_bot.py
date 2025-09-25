import logging
import re
from collections import Counter
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define your bot token here
TOKEN = "7258588708:AAH0GFbjjWzFjXauhPj0ux1W4Yi-dYd0PYY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Hi! Send me any text, and I will analyze it for you.")

async def analyze_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Analyzes the user's text message with extended features."""
    text = update.message.text
    
    # 1. Basic Counts
    char_count = len(text)
    words = re.findall(r'\w+', text.lower())
    word_count = len(words)
    char_count_no_spaces = sum(len(word) for word in words)
    
    # 2. Reading Time (Slow: 130 WPM, Avg: 200 WPM, Fast: 260 WPM)
    def calculate_reading_time(wpm):
        minutes = word_count / wpm
        seconds = minutes * 60
        return f"{int(minutes)} min, {int(seconds % 60)} sec"

    slow_time = calculate_reading_time(130)
    avg_time = calculate_reading_time(200)
    fast_time = calculate_reading_time(260)

    # 3. Sentence and Paragraph Count
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len([s for s in sentences if s.strip()])
    paragraphs = text.split('\n\n')
    paragraph_count = len([p for p in paragraphs if p.strip()])

    # 4. Word Frequency Analysis (Top 5)
    word_freq = Counter(words)
    top_words = word_freq.most_common(5)
    top_words_str = "\n".join([f"    - {word}: {count}" for word, count in top_words])

    # 5. Readability (Average Word Length)
    avg_word_length = char_count_no_spaces / word_count if word_count > 0 else 0

    # 6. Emoji-based Formatted Output
    response = (
        f"📊 *Text Analysis Complete!* 📊\n\n"
        f"📝 *Counts*\n"
        f"  - Characters (with spaces): {char_count}\n"
        f"  - Characters (no spaces): {char_count_no_spaces}\n"
        f"  - Words: {word_count}\n"
        f"  - Sentences: {sentence_count}\n"
        f"  - Paragraphs: {paragraph_count}\n\n"
        f"⏱️ *Estimated Reading Time*\n"
        f"  - Slow (130 WPM): {slow_time}\n"
        f"  - Average (200 WPM): {avg_time}\n"
        f"  - Fast (260 WPM): {fast_time}\n\n"
        f"🔍 *Word Frequency (Top 5)*\n{top_words_str}\n\n"
        f"📈 *Readability*\n"
        f"  - Average Word Length: {avg_word_length:.2f} characters\n"
    )
    
    await update.message.reply_text(response, parse_mode='Markdown')

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # on non command i.e message - analyze the message from user
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analyze_text))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()
