from telethon import TelegramClient, events
import time

# gunakan api id hash punya anda sendiri, atau cari aja punya orang lain
api_id = 4861943
api_hash = 'ce9b761f8627a68cc5c475e838d04f34'
phone= '+6285862276137'


client = TelegramClient('session', api_id, api_hash)

# Isi pesan
message = "Punten nuju offline, antosan wae dugi ka online, nuju UMROH, GAYA PAAAAN?"


    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:  # only auto-reply to private chats
            from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
            if not from_.bot:  # don't auto-reply to bots
                print(time.asctime(), '-', event.message)  # optionally log time and message
                time.sleep(1)  # pause for 1 second to rate-limit automatic replies
                await event.respond(message)


    print(time.asctime(), '-', 'Auto-replying...')
    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')
