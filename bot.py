import os
from telegram.ext import ApplicationBuilder, ContextTypes
from datetime import time
import asyncio
from aiohttp import web

TOKEN = os.getenv("TOKEN", "7928038935:AAHKS23g8AarVYlb64qYI-z9zfpQdgD3czE")
CHAT_ID = "-1002038009783"
PORT = int(os.getenv("PORT", 8080))

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

async def health_check(request):
    return web.Response(text="Bot is alive")
    
async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    ora_invio = datetime.time(hour=9, minute=0)
    app.job_queue.run_daily(invia_sondaggio, ora_invio)

web_app = web.Application()
    web_app.add_routes([web.get('/', health_check)])
    runner = web.AppRunner(web_app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()

    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    print(f"Bot avviato, ascoltando su porta {PORT}")

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
