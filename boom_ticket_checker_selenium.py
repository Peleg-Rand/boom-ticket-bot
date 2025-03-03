from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import asyncio
import telegram

# Replace with your actual bot token and chat ID
TELEGRAM_TOKEN = '8122031392:AAH6FGluVx9Ac7eI_9lpO1I3JcyRnK2o6Vc'
CHAT_ID = '7116762256'

# Telegram bot setup
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# URL of the Boom Festival resale page
URL = "https://tickets.boomfestival.org/resale.html"

async def send_telegram_message(message):
    """Send a message to Telegram."""
    await bot.send_message(chat_id=CHAT_ID, text=message)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_tickets():
    """Check for ticket availability using Selenium."""
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    # Wait for CAPTCHA solving
    input("💡 Solve the CAPTCHA in the opened browser, then press Enter...")

    try:
        # Wait for the iframe and switch to it
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)
        print("✅ Switched to iframe")

        # ✅ PRINT ALL STATUS ELEMENTS TO DEBUG
        print("🔍 Searching for ticket status elements...")
        status_elements = driver.find_elements(By.CLASS_NAME, "wz-event-status")

        if status_elements:
            for elem in status_elements:
                print(f"✅ Status Found: '{elem.text.strip()}'")  # Print the exact text
        else:
            print("⚠️ No status elements found.")

    except Exception as e:
        print("⚠️ Could not check ticket status. Page structure might have changed.")
        print("Error details:", str(e))

    driver.quit()




# Run the check
if __name__ == "__main__":
    check_tickets()
