from telethon import TelegramClient, events
from telethon.tl.types import InputPeerChat
import os

# Secrets
api_id = os.getenv("TELE_API_ID")
api_hash = os.getenv("TELE_API_HASH")
bot_token = os.getenv("TELE_BOT_TOKEN")

# Instance
botInstance = TelegramClient('bot', api_id, api_hash)

# Constants
KOL_MEI_MEI = 1094212803
kol_ids = [KOL_MEI_MEI]

LOGS_GROUP_ID = 842020756
CALLS_GROUP_ID = 891088681

keywords = ["buy", "sell", "sl"]

# Start
botInstance.start(bot_token=bot_token)


@botInstance.on(events.NewMessage)
async def newMessage(event):
  print(event.message)
  if (event.sender_id in kol_ids):
    await botInstance.forward_messages(InputPeerChat(LOGS_GROUP_ID),
                                       event.message)
    if (event.raw_text != None
        and any(s in event.raw_text.lower() for s in keywords)):
      await botInstance.forward_messages(InputPeerChat(CALLS_GROUP_ID),
                                         event.message)


# Stop
botInstance.run_until_disconnected()
