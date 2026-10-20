import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = "8961872954:AAFP-TdjhTDWG_Sff7L77Imc8FXFgNdlpKw"
OWNER_USERNAME = "pptkkkk"

# -------------------------------------------------------------
# Main Menu (ပင်မ စာမျက်နှာ ခလုတ်များ)
# -------------------------------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 MLBB Diamond စျေးကြည့်ရန်", callback_data='menu_mlbb')],
        [InlineKeyboardButton("🎮 Magic Chess GoGo စျေးကြည့်ရန်", callback_data='menu_mcgg')],
        [InlineKeyboardButton("💬 Admin ထံ တိုက်ရိုက် ဆက်သွယ်ရန်", url=f"https://t.me/{OWNER_USERNAME}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "👋 **ကြိုဆိုပါတယ်။**\n\n"
        "ကြည့်ရှုလိုသည့် ဝန်ဆောင်မှုကို အောက်ပါ ခလုတ်များမှတစ်ဆင့် ရွေးချယ်နိုင်ပါတယ်။"
    )
    
    if update.message:
        await update.message.reply_text(text=welcome_text, parse_mode="Markdown", reply_markup=reply_markup)
    elif update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(text=welcome_text, parse_mode="Markdown", reply_markup=reply_markup)

# -------------------------------------------------------------
# ခလုတ်တစ်ခုချင်းစီအတွက် စာသားနှင့် လုပ်ဆောင်ချက်များ
# -------------------------------------------------------------
async def button_click_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # 1. MLBB Diamond စျေး
    if data == 'menu_mlbb':
        text = (
            "Today(17.10.2026) 💎 MLBB Diamond Price List\n\n"
            "Global Server (Except Malay, Phili, Sing, Indo)\n\n"
            "🎫 Pass\n"
            "Weekly Pass – 6,900 Ks 📌\n"
            "Twilight Pass – 37,900 Ks\n"
            "Elite Bundle – 3,900 Ks\n"
            "Epic Bundle – 19,500 Ks\n\n"
            "💎 Double Diamond list\n"
            "50×50 - 4200 Ks\n"
            "150×150 - 11500 Ks\n"
            "250×250 - 18000 Ks\n"
            "500×500 - 35500 Ks\n\n"
            "💎 Diamond Price List\n"
            "14 – 1500 Ks\n"
            "28 – 2900 Ks\n"
            "42 – 4000 Ks\n"
            "86 – 5,700 Ks\n"
            "172 – 11,300 Ks\n"
            "257 – 16,500 Ks\n"
            "343 – 22,200 Ks\n"
            "429 – 27,200 Ks\n"
            "514 – 33,300 Ks\n"
            "600 – 38,500 Ks\n"
            "706 – 43,900 Ks\n"
            "878 – 55,300 Ks\n"
            "963 – 59,500 Ks\n"
            "1049 – 66,500 Ks\n"
            "2195 – 131,500 Ks\n"
            "3688 – 215,400 Ks\n"
            "5532 – 324,500 Ks\n"
            "9288 – 531,900 Ks\n\n"
            "💳 Payment (KBZPay ,Wave Pay, AYA Pay)\n"
            "09680633603 (Ye Yan Naing ✅)\n"
            "09967598086 (Phyu Phyu Thant Khine ✅)\n\n"
            "(Note - Shop ) ‼️\n"
            "‼️ငွေမလွှဲခင် ဖုန်းနံပါတ်နဲ့ နာမည်ကို သေချာစစ်ဆေးပါ‼️\n"
            "⚠️Note ကို ပြထားတဲ့အတိုင်း သေချာစွာ ထည့်ပေးပါ⚠️"
        )

    # 2. Magic Chess GoGo စျေး
    elif data == 'menu_mcgg':
        text = (
            "🤩🎮🎮 Magic Chess Go Go Topup Prices\n\n"
            "👍 Mcgg Wp – 9000 Ks\n\n"
            "86 dia — 5700 Ks\n"
            "172 dia — 11300 Ks\n"
            "257 dia — 16700 Ks\n"
            "344 dia — 22500 Ks\n"
            "516 dia — 33500 Ks\n"
            "706 dia — 44700 Ks\n"
            "1346 dia — 83200 Ks\n"
            "1825 dia — 112000 Ks\n"
            "2195 dia — 134000 Ks\n"
            "3688 dia — 225000 Ks\n"
            "5532 dia — 335000 Ks\n"
            "9288 dia — 555000 Ks\n\n"
            "✨ **2X First Recharge**\n"
            "🤩 50+50 (55) – 3800 Ks\n"
            "🤩 150+150 (165) – 11000 Ks\n"
            "🤩 250+250 (275) – 18400 Ks\n"
            "🤩 500+500 (565) – 35800 Ks\n\n"
            "💳 Payment (KBZPay ,Wave Pay, AYA Pay)\n"
            "09680633603 (Ye Yan Naing ✅)\n"
            "09967598086 (Phyu Phyu Thant Khine ✅)"
        )

    # အောက်ခြေ ခလုတ်များ (ဝယ်ယူရန် Admin ဆီသွားမည့် ခလုတ် နှင့် ပင်မစာမျက်နှာပြန်သွားမည့် ခလုတ်)
    keyboard = [
        [InlineKeyboardButton("🛒 ဝယ်ယူလို၍ Admin ထံသို့", url=f"https://t.me/{OWNER_USERNAME}")],
        [InlineKeyboardButton("⬅️ ပင်မ Menu သို့ ပြန်သွားရန်", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=text,
        reply_markup=reply_markup
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(start, pattern='^main_menu$'))
    app.add_handler(CallbackQueryHandler(button_click_handler, pattern='^menu_'))

    print("Bot စတင်လည်ပတ်နေပါပြီ...")
    app.run_polling()

if __name__ == "__main__":
    main()