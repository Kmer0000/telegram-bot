import os
from telegram.ext import ApplicationBuilder, ContextTypes
import datetime

TOKEN = os.getenv("TOKEN", "7928038935:AAHKS23g8AarVYlb64qYI-z9zfpQdgD3czE")
CHAT_ID = "-1002038009783"

async def invia_sondaggio(context):
    poll_message = await context.bot.send_poll(
        chat_id=CHAT_ID,
        question="Commander oggi?",
        options=["Ci sono", "Non ci sono"],
        is_anonymous=False,
        allows_multiple_answers=False
    )
    await context.bot.pin_chat_message(
        chat_id=poll_message.chat_id,
        message_id=poll_message.message_id,
        disable_notification=False
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    ora_invio = date.time(hour=18, minute=0)
    app.job_queue.run_daily(invia_sondaggio, ora_invio)
    app.run_polling()

if __name__ == "__main__":
    main()
