from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    CallbackQueryHandler
)

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from functions import get_rates


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("🇺🇸 USD/UZS", callback_data="USD"),
            InlineKeyboardButton("TRY/UZS", callback_data="TRY"),
        ],
        [
            InlineKeyboardButton("EUR/UZS", callback_data="EUR"),
            InlineKeyboardButton("KZT/UZS", callback_data="KZT"),
        ],
         [
            InlineKeyboardButton("RUB/UZS", callback_data="RUB"),
        ],
       
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"Hello,{update.message.from_user.first_name} \nSelect your currency :",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.message.delete()
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🇺🇸 USD/UZS", callback_data="USD"),
            InlineKeyboardButton("TRY/UZS", callback_data="TRY"),
        ],
        [
            InlineKeyboardButton("EUR/UZS", callback_data="EUR"),
            InlineKeyboardButton("KZT/UZS", callback_data="KZT"),
        ],
         [
            InlineKeyboardButton("RUB/UZS", callback_data="RUB"),
        ],
       
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    
    rate = get_rates()[query.data]["Rate"]
    await query.message.reply_text(text=f"1 {query.data} is {rate} UZS", reply_markup=reply_markup)


app = (
    ApplicationBuilder().token("5674542404:AAE9-rqluy8RwvM25WhkawsfhnD3R7fzM_E").build()
)

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()  # bot telegram for usd dolr kursi






# https://animego.org/anime/voshozhdenie-v-teni-2120#video-watch2