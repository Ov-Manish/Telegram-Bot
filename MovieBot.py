
import json
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)

BOT_TOKEN = "8111198260:AAHTH3uOxp1EWsCKZiIgQVl-O8_qvJv-3N0"
FILENAME = "movies.json"
FUZZY_MATCHING = True
DELETE_DELAY = 600  # 10 minutes


# Load movie data
def load_movies():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, FILENAME)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


MOVIE_STORAGE = load_movies()


# Job to delete messages
async def delete_message_job(context: ContextTypes.DEFAULT_TYPE):
    job_data = context.job.data
    try:
        await context.bot.delete_message(
            chat_id=job_data["chat_id"],
            message_id=job_data["message_id"]
        )
        print(
            f"🗑 Deleted message {job_data['message_id']} from chat {job_data['chat_id']}"
        )
    except Exception as e:
        print(f"⚠️ Could not delete message: {e}")


# /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to MovieBot!\n\nSend me the *movie name*, and I’ll fetch all available quality versions for you. 🎥✨",
        parse_mode="Markdown"
    )


# Movie request handler
async def handle_movie_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    keyword = update.message.text.lower().strip()
    print(f"🔍 Received request: '{keyword}' from chat {update.effective_chat.id}")

    matches = []

    # Exact match
    if keyword in MOVIE_STORAGE:
        matches = MOVIE_STORAGE[keyword]
    # Fuzzy match (partial)
    elif FUZZY_MATCHING:
        for movie_title in MOVIE_STORAGE:
            if keyword in movie_title:
                matches.extend(MOVIE_STORAGE[movie_title])

    # If no match found, stay silent
    if not matches:
        print("❌ No match found. Ignoring message.")
        return

    chat_id = update.effective_chat.id

    for version in matches:
        try:
            sent = await context.bot.copy_message(
                chat_id=chat_id,
                from_chat_id=version["chat_id"],
                message_id=version["message_id"]
            )

            if sent and context.job_queue:
                context.job_queue.run_once(
                    delete_message_job,
                    when=DELETE_DELAY,
                    data={"chat_id": chat_id, "message_id": sent.message_id}
                )

        except Exception as e:
            print(f"⚠️ Error sending movie version: {e}")

    try:
        info = await update.message.reply_text(
            f"🚫 This content will be deleted after {DELETE_DELAY // 60} minutes due to copyright rules."
        )
        if info and context.job_queue:
            context.job_queue.run_once(
                delete_message_job,
                when=DELETE_DELAY,
                data={"chat_id": info.chat.id, "message_id": info.message_id}
            )
    except Exception as e:
        print(f"⚠️ Failed to send delete warning message: {e}")


# Main entry point
if __name__ == "__main__":
    print("🚀 Starting MovieBot...")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_movie_request))

    print("🤖 MovieBot is running...")
    app.run_polling()
