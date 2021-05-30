from telethon import TelegramClient, events
import time

# gunakan api id hash punya anda sendiri, atau cari aja punya orang lain
api_id = 4861943
api_hash = 'ce9b761f8627a68cc5c475e838d04f34'
phone= '+6285862276137'


client = TelegramClient('session', api_id, api_hash)

# Isi pesan
message = "Punten nuju offline, antosan wae dugi ka online, nuju UMROH, GAYA PAAAAN?"

@client.on(events.NewMessage)
async def handle_new_message(event):

    from_user = await event.client.get_entity(event.from_id)
    if from_user.phone == phone:
        print(time.asctime(), '-', event.message)
        # diuji pada gadis sungguhan, dia menemukan jawabannya pada jawaban kedua 
        # jadi pilih balasan secara acak dalam 5 - 59 detik 
# jadi pilih balasan secara acak dalam 5 - 59 detik 
        await asyncio.sleep(random.randrange(5, 59))
        if random.choice([True, False]):
            i, s = random.randrange(2, 5), random.choice(greetings)
            # mengetik 2 - 5 detik 
            async with client.action(phone, 'typing'):
                await asyncio.sleep(i)
                await client.send_message(phone, s)


    print(time.asctime(), '-', 'Auto-replying...')
    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')
