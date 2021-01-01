import discord
import asyncio
import random

client = discord.Client()

async def background_loop():
    await client.wait_until_ready()
    while not client.is_closed:
        channel = client.get_channel(794208812944588863)
        print('hi')
        messages = ["Hello!", "How are you doing?", "Howdy!"]
        await client.send_message(channel, random.choice(messages))

client.loop.create_task(background_loop())
#client.loop.create_task(background_loop())
client.run("Nzk0MjA4MjE3MjY5Nzk2ODg1.X-3eCg.pGua6Qvl69Htw2RvNNwCP86ILG8")
