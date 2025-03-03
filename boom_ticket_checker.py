import requests
from bs4 import BeautifulSoup
import asyncio
import telegram

# Replace with your actual bot token and chat ID
TELEGRAM_TOKEN = '8122031392:AAH6FGluVx9Ac7eI_9lpO1I3JcyRnK2o6Vc'
CHAT_ID = '7116762256'

# Telegram bot setup
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# URL of the Boom Festival resale page
URL = 'https://tickets.boomfestival.org/resale.html'

async def send_telegram_message(message):
    """Send a message to Telegram."""
    await bot.send_message(chat_id=CHAT_ID, text=message)

def check_tickets():
    """Check for ticket availability on the resale page."""
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise error if request fails
        soup = BeautifulSoup(response.text, 'html.parser')

        # Look for ticket availability (this may need adjustment)
        ticket_section = soup.find('div', class_='ticket-status')

        if ticket_section and 'Available' in ticket_section.text:
            message = '🚀 Boom Festival tickets are now available! Grab them here: ' + URL
            print(message)  # Debugging
            asyncio.run(send_telegram_message(message))  # Send notification
        else:
            print("No tickets available yet.")  # Debugging

    except Exception as e:
        print(f"Error checking tickets: {e}")

# Run the check
if __name__ == '__main__':
    check_tickets()
