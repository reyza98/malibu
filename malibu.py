import os

from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon import TelegramClient, events, utils
load_dotenv()

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

client = TelegramClient('badutgalauu', api_id, api_hash)

toggle_auto_reply = False

client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True).start(phone, password)

message = "@client.on(events.NewMessage(pattern='#message'. This Grup has ben hacked by @snowden_id"

@client.on(events.NewMessage(pattern='#message', forwards=False))
async def custom_message(event):
    if event.to_id.user_id == event.from_id:
        global message
        msg = event.message.message.split(" ")
        message = ' '.join(msg[1:])
        await event.message.delete()
        await event.respond("Message set to : "+message)

@client.on(events.NewMessage(pattern='#toggle', forwards=False))
async def toggle_panel(event):
    if event.to_id.user_id == event.from_id:
        global toggle_auto_reply
        if toggle_auto_reply == False:
            toggle_auto_reply = True
        else:
            toggle_auto_reply = False
            pass
        await event.message.delete()
        await event.respond("Toggle set "+str(toggle_auto_reply))

@client.on(events.NewMessage)
async def auto_reply(event):
    global toggle_auto_reply
    if (event.is_private and toggle_auto_reply) and (event.to_id.user_id != event.from_id):
        await event.reply(message)

client.run_until_disconnected()
