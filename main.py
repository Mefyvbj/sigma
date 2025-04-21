import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("ADOPT ME", url="https://roblox.tg/games/920587237/FESTIVAL-Adopt-Me?privateServerLinkCode=93774278871181662135661139449501")],
        [InlineKeyboardButton("PLS DONATE",
                              url="https://roblox.tg/games/8737602449/PLS-DONATE?privateServerLinkCode=93774278871181662135661139449501")],
        [InlineKeyboardButton("BLOX FRUITS",
                              url="https://roblox.tg/games/2753915549/Blox-Fruits?privateServerLinkCode=93774278871181662135661139449501")],
        [InlineKeyboardButton("MURDER MYSTERY 2",
                              url="https://roblox.tg/games/142823291/Murder-Mystery-2?privateServerLinkCode=93774278871181662135661139449501")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "АКТУАЛЬНЫЕ СЕРВЕРА С РАЗДАЧАМИ",
        reply_markup=reply_markup
    )

def main():
    application = Application.builder().token(os.getenv("BOT_TOKEN")).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
