import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎵 Musiqalar", callback_data="music")],
        [InlineKeyboardButton("ℹ️ Bot haqida", callback_data="about")]
    ]

    await update.message.reply_text(
        "🎵 Carrozeria Music Bot'ga xush kelibsiz!\n\n"
        "Kerakli bo‘limni tanlang:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "music":
        await query.edit_message_text(
            "🎵 Hozircha musiqalar qo‘shilmagan.\n"
            "Tez orada yangi musiqalar qo‘shiladi."
        )

    elif query.data == "about":
        await query.edit_message_text(
            "🎵 Carrozeria Music Bot\n\n"
            "Musiqa botimizga xush kelibsiz!"
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    app.run_polling()

if __name__ == "__main__":
    main()