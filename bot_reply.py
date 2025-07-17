from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import asyncio

# Replace with your actual bot token
BOT_TOKEN = '7825581087:AAHwBuUtbRHJfHEYYuu5tuNCbxQ4x3-SPEQ'

# Your custom reply message
REPLY_TEXT = (
    "Please provide the correct movie/series name from Google with release year and required language.\n"
    "We don't share theatre print movies, only HD after OTT release.\n"
    "Thank you."
)

# Handle all text messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type != 'supergroup':
        return  # Only reply in supergroups

    # Send auto reply
    reply = await update.message.reply_text(REPLY_TEXT)
    
    # Wait for 5 minutes (300 seconds)
    await asyncio.sleep(300)

    # Delete bot's message
    try:
        await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=reply.message_id)
    except Exception as e:
        print(f"Could not delete message: {e}")

# Main function
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Respond to all non-command text messages
    msg_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    app.add_handler(msg_handler)

    print("Bot is running...")
    app.run_polling()
