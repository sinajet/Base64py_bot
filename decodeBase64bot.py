import base64
from telegram import Update , InlineKeyboardButton , InlineKeyboardMarkup
from telegram.constants import ParseMode as Pmode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes , MessageHandler , filters
from TokenBase64 import *
import logging
#login============================================================
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
#startDef=========================================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""
*Engilsh Description*
Welcome to Base64 Bot!
for encoding to base64 ،Type your Text between `[ ]`
Like This:
        `[www.Google.com]`
for decoding from Base64 Type your Text between `{ }`
Like This:
        `{d3d3Lkdvb2dsZS5jb20=}`
...................................................................
*توضیحات فارسی*
به ربات رمزنگاری متن به Base64 خوش آمدید
جهت رمزنگاری کردن متن خود آن را بین `[ ]` قرار دهید.
برای مثال:
`[www.Google.com]`
جهت گشایی کردن متن خود آن را بین`{ }` قرار دهید!
برای مثال:
`{d3d3Lkdvb2dsZS5jb20=}`
""",parse_mode=Pmode.MARKDOWN)
#txtDef============================================================
async def txt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
   try:
    x=str(update.message.text)
    if x[0]=="[" and x[-1]=="]":
        x=x.replace(x[0],"")
        x=x.replace(x[-1],"")
        m = str(base64.b64encode(x.encode('utf-8')))
        m=m.replace(m[0],"")
        m=m.replace(m[-1],"")
        await update.message.reply_text(f"`{m}`",parse_mode=Pmode.MARKDOWN)
    elif x[0]=="{" and x[-1]=="}":
        x=x.replace(x[0],"")
        x=x.replace(x[-1],"")
        m = base64.b64decode(x).decode('utf-8')
        await update.message.reply_text(m)    
   except base64.binascii.Error:
       await update.message.reply_text("Please Send a __Correct Base64 encoded Text__",parse_mode=Pmode.MARKDOWN_V2)
#aboutDef============================================================
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    keyboard = [
        [InlineKeyboardButton('Telegram Channel!', url='https://t.me/sinajet')],
        [InlineKeyboardButton('YouTube Channel!', url='https://www.youtube.com/c/SinaJet')],
        [InlineKeyboardButton('Bot Source On my Github!', url='https://github.com/sinajet/')]
    ]
    reply_markup = InlineKeyboardMarkup (keyboard)
    await update.message.reply_text("Hi, My name is Sina!\nYou can Follow me on these Social Media Sites!!", reply_markup=reply_markup)
def main():
    app = ApplicationBuilder().token(tkn()).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(CommandHandler("aboutme", about))
    app.add_handler(MessageHandler(filters.TEXT,txt))
    app.run_polling()
if __name__ == "__main__":
    main()