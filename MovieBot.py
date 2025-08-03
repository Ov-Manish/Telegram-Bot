# from telegram import Update
# from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# BOT_TOKEN = "8111198260:AAHTH3uOxp1EWsCKZiIgQVl-O8_qvJv-3N0"

# # Map of keywords to message info from the storage channel
# MOVIE_STORAGE = {
#     "hi": {"chat_id": -1002465484511, "message_id": 6},
#     "oppenheimer": {"chat_id": -1002465484511, "message_id": 8},
#     "saiyaara": {"chat_id": -1002465484511, "message_id": 10},
#     "spiderman": {"chat_id": -1002465484511, "message_id": 9},
#     # Add more keyword-message_id mappings here
# }

# async def handle_movie_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if not update.message or not update.message.text:
#         return

#     keyword = update.message.text.lower().strip()

#     if keyword in MOVIE_STORAGE:
#         movie = MOVIE_STORAGE[keyword]
#         try:
#             await context.bot.copy_message(
#                 chat_id=update.effective_chat.id,
#                 from_chat_id=movie["chat_id"],
#                 message_id=movie["message_id"]
#             )
#         except Exception as e:
#             await update.message.reply_text(f"⚠️ Error sending movie: {e}")
#     else:
#         await update.message.reply_text("❌ Movie not found. Please try a different keyword.")

# if __name__ == "__main__":
#     app = ApplicationBuilder().token(BOT_TOKEN).build()
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_movie_request))
#     print("🤖 Movie bot is running...")
#     app.run_polling()


# [[[]]]




# import json
# import os
# from telegram import Update
# from telegram.ext import (
#     ApplicationBuilder,
#     ContextTypes,
#     MessageHandler,
#     filters,
# )

# BOT_TOKEN = "8111198260:AAHTH3uOxp1EWsCKZiIgQVl-O8_qvJv-3N0"
# FILENAME = "movies.json"
# FUZZY_MATCHING = False

# def load_movies():
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(base_dir, FILENAME)
#     if os.path.exists(file_path):
#         with open(file_path, "r", encoding="utf-8") as f:
#             return json.load(f)
#     return {}

# MOVIE_STORAGE = load_movies()

# async def delete_message_job(context: ContextTypes.DEFAULT_TYPE):
#     job_data = context.job.data
#     chat_id = job_data["chat_id"]
#     message_id = job_data["message_id"]
#     try:
#         await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
#         print(f"🗑 Deleted message {message_id} in chat {chat_id}")
#     except Exception as e:
#         print(f"⚠️ Failed to delete message {message_id}: {e}")

# async def handle_movie_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if not update.message or not update.message.text:
#         return

#     keyword = update.message.text.lower().strip()
#     print(f"🔍 Received request: '{keyword}' from chat {update.effective_chat.id}")

#     matches = []

#     if keyword in MOVIE_STORAGE:
#         matches = MOVIE_STORAGE[keyword]
#     elif FUZZY_MATCHING:
#         for movie_name in MOVIE_STORAGE:
#             if keyword in movie_name:
#                 matches.extend(MOVIE_STORAGE[movie_name])

#     if matches:
#         for version in matches:
#             try:
#                 # Send the copied message
#                 sent_message = await context.bot.copy_message(
#                     chat_id=update.effective_chat.id,
#                     from_chat_id=version["chat_id"],
#                     message_id=version["message_id"]
#                 )
#                 # Schedule deletion after 30 seconds using job queue
#                 context.application.job_queue.run_once(
#                     delete_message_job,
#                     when=30,
#                     data={
#                         "chat_id": update.effective_chat.id,
#                         "message_id": sent_message.message_id
#                     }
#                 )
#             except Exception as e:
#                 await update.message.reply_text(f"⚠️ Error sending movie version: {e}")
#     else:
#         await update.message.reply_text("❌ Movie not found. Please try a different keyword.")

# if __name__ == "__main__":
#     print("🚀 Starting MovieBot...")
#     app = ApplicationBuilder().token(BOT_TOKEN).build()

#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_movie_request))

#     print("🤖 MovieBot is now running and listening for messages...")
#     app.run_polling()


# [[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]

# import json
# import os
# from telegram import Update
# from telegram.ext import (
#     ApplicationBuilder,
#     ContextTypes,
#     MessageHandler,
#     filters,
# )

# BOT_TOKEN = "8111198260:AAHTH3uOxp1EWsCKZiIgQVl-O8_qvJv-3N0"
# FILENAME = "movies.json"
# FUZZY_MATCHING = False
# DELETE_DELAY = 600  

# def load_movies():
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(base_dir, FILENAME)
#     if os.path.exists(file_path):
#         with open(file_path, "r", encoding="utf-8") as f:
#             return json.load(f)
#     return {}

# MOVIE_STORAGE = load_movies()

# async def delete_message_job(context: ContextTypes.DEFAULT_TYPE):
#     job_data = context.job.data
#     chat_id = job_data["chat_id"]
#     message_id = job_data["message_id"]
#     try:
#         await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
#         print(f"🗑 Deleted message {message_id} in chat {chat_id}")
#     except Exception as e:
#         print(f"⚠️ Failed to delete message {message_id}: {e}")

# async def handle_movie_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if not update.message or not update.message.text:
#         return

#     keyword = update.message.text.lower().strip()
#     print(f"🔍 Received request: '{keyword}' from chat {update.effective_chat.id}")

  
#     if keyword in MOVIE_STORAGE:
#         matches = MOVIE_STORAGE[keyword]
#     else:
        
#         return

#     for version in matches:
#         try:
          
#             sent_message = await context.bot.copy_message(
#                 chat_id=update.effective_chat.id,
#                 from_chat_id=version["chat_id"],
#                 message_id=version["message_id"]
#             )

            
#             context.application.job_queue.run_once(
#                 delete_message_job,
#                 when=DELETE_DELAY,
#                 data={
#                     "chat_id": update.effective_chat.id,
#                     "message_id": sent_message.message_id
#                 }
#             )
#         except Exception as e:
#             await update.message.reply_text(f"⚠️ Error sending movie version: {e}")
#             return

#     try:
#         info_msg = await update.message.reply_text(
#             f":🚫 The movie message(s) will be deleted after {DELETE_DELAY // 60} minutes. Due to Copyright issues"
#         )
        
#         context.application.job_queue.run_once(
#             delete_message_job,
#             when=DELETE_DELAY,
#             data={
#                 "chat_id": info_msg.chat_id,
#                 "message_id": info_msg.message_id,
#             }
#         )
#     except Exception as e:
#         print(f"⚠️ Failed to send deletion info message: {e}")

# if __name__ == "__main__":
#     print("🚀 Starting MovieBot...")
#     app = ApplicationBuilder().token(BOT_TOKEN).build()

    
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_movie_request))

#     print("🤖 MovieBot is now running and listening for messages...")
#     app.run_polling()


# [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]


# import json
# import os
# from telegram import Update
# from telegram.ext import (
#     ApplicationBuilder,
#     ContextTypes,
#     MessageHandler,
#     filters,
# )

# BOT_TOKEN = "8111198260:AAHTH3uOxp1EWsCKZiIgQVl-O8_qvJv-3N0"
# FILENAME = "movies.json"
# FUZZY_MATCHING = False  # Set to True if you want partial keyword match
# DELETE_DELAY = 600  # Time in seconds (10 minutes)

# # Load movie data
# def load_movies():
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(base_dir, FILENAME)
#     if os.path.exists(file_path):
#         with open(file_path, "r", encoding="utf-8") as f:
#             return json.load(f)
#     return {}

# MOVIE_STORAGE = load_movies()

# # Job to delete messages
# async def delete_message_job(context: ContextTypes.DEFAULT_TYPE):
#     job_data = context.job.data
#     try:
#         await context.bot.delete_message(
#             chat_id=job_data["chat_id"],
#             message_id=job_data["message_id"]
#         )
#         print(f"🗑 Deleted message {job_data['message_id']} from chat {job_data['chat_id']}")
#     except Exception as e:
#         print(f"⚠️ Could not delete message: {e}")

# # Handle movie requests
# async def handle_movie_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if not update.message or not update.message.text:
#         return

#     keyword = update.message.text.lower().strip()
#     print(f"🔍 Received request: '{keyword}' from chat {update.effective_chat.id}")

#     matches = []

#     if keyword in MOVIE_STORAGE:
#         matches = MOVIE_STORAGE[keyword]
#     elif FUZZY_MATCHING:
#         for movie_title in MOVIE_STORAGE:
#             if keyword in movie_title:
#                 matches.extend(MOVIE_STORAGE[movie_title])

#     if not matches:
#         await update.message.reply_text("❌ Movie not found. Try a different keyword.")
#         return

#     chat_id = update.effective_chat.id

#     for version in matches:
#         try:
#             sent = await context.bot.copy_message(
#                 chat_id=chat_id,
#                 from_chat_id=version["chat_id"],
#                 message_id=version["message_id"]
#             )

#             context.job_queue.run_once(
#                 delete_message_job,
#                 when=DELETE_DELAY,
#                 data={"chat_id": chat_id, "message_id": sent.message_id}
#             )

#         except Exception as e:
#             await update.message.reply_text(f"⚠️ Error sending movie version: {e}")
#             return

#     try:
#         info = await update.message.reply_text(
#             f"🚫 This content will be deleted after {DELETE_DELAY // 60} minutes due to copyright rules."
#         )
#         context.job_queue.run_once(
#             delete_message_job,
#             when=DELETE_DELAY,
#             data={"chat_id": info.chat.id, "message_id": info.message_id}
#         )
#     except Exception as e:
#         print(f"⚠️ Failed to send delete warning message: {e}")

# # Main function
# if __name__ == "__main__":
#     print("🚀 Starting MovieBot...")

#     app = ApplicationBuilder().token(BOT_TOKEN).build()

#     # Add message handler
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_movie_request))

#     print("🤖 MovieBot is running...")
#     app.run_polling()

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
FUZZY_MATCHING = True  # Now enabled
DELETE_DELAY = 600  # Time in seconds (10 minutes)


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
        await context.bot.delete_message(chat_id=job_data["chat_id"],
                                         message_id=job_data["message_id"])
        print(
            f"🗑 Deleted message {job_data['message_id']} from chat {job_data['chat_id']}"
        )
    except Exception as e:
        print(f"⚠️ Could not delete message: {e}")


# Welcome message
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to MovieBot!\n\nSend me the *movie name*, and I’ll fetch all available quality versions for you. 🎥✨",
        parse_mode="Markdown")


# Handle movie requests
async def handle_movie_request(update: Update,
                               context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    keyword = update.message.text.lower().strip()
    print(
        f"🔍 Received request: '{keyword}' from chat {update.effective_chat.id}"
    )

    matches = []

    if keyword in MOVIE_STORAGE:
        matches = MOVIE_STORAGE[keyword]
    elif FUZZY_MATCHING:
        for movie_title in MOVIE_STORAGE:
            if keyword in movie_title:
                matches.extend(MOVIE_STORAGE[movie_title])

    if not matches:
        await update.message.reply_text(
            "❌ Movie not found. Try a different keyword.")
        return

    chat_id = update.effective_chat.id

    for version in matches:
        try:
            sent = await context.bot.copy_message(
                chat_id=chat_id,
                from_chat_id=version["chat_id"],
                message_id=version["message_id"])

            if sent:
                context.job_queue.run_once(delete_message_job,
                                           when=DELETE_DELAY,
                                           data={
                                               "chat_id": chat_id,
                                               "message_id": sent.message_id
                                           })

        except Exception as e:
            await update.message.reply_text(
                f"⚠️ Error sending movie version: {e}")

    try:
        info = await update.message.reply_text(
            f"🚫 This content will be deleted after {DELETE_DELAY // 60} minutes due to copyright rules."
        )
        if info:
            context.job_queue.run_once(delete_message_job,
                                       when=DELETE_DELAY,
                                       data={
                                           "chat_id": info.chat.id,
                                           "message_id": info.message_id
                                       })
    except Exception as e:
        print(f"⚠️ Failed to send delete warning message: {e}")


# Main function
if __name__ == "__main__":
    print("🚀 Starting MovieBot...")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_movie_request))

    print("🤖 MovieBot is running...")
    app.run_polling()
