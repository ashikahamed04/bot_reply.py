import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.getenv("7825581087:AAHwBuUtbRHJfHEYYuu5tuNCbxQ4x3-SPEQ")

REPLY_TEXT = (
    "Please provide the correct movie/series name from Google with release year and required language.\n"
    "We don't share theatre print movies, only HD after OTT release.\n"
    "Thank you."
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type != 'supergroup':
        return  # Only reply in supergroups

    reply = await update.message.reply_text(REPLY_TEXT)
    await asyncio.sleep(300)

    try:
        await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=reply.message_id)
    except Exception as e:
        print(f"Could not delete message: {e}")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    msg_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    app.add_handler(msg_handler)

    print("Bot is running...")
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
