import asyncio
import telegram

# Replace with your bot token and chat ID
TELEGRAM_TOKEN = '8122031392:AAH6FGluVx9Ac7eI_9lpO1I3JcyRnK2o6Vc'
CHAT_ID = '7116762256'

# Create a bot instance
bot = telegram.Bot(token=TELEGRAM_TOKEN)

async def send_message():
    await bot.send_message(chat_id=CHAT_ID, text="🚀 Telegram bot is working!")

# Run the async function
asyncio.run(send_message())
