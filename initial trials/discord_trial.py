import os

import discord

client = discord.Client()

@client.event
async def on_ready():
    await client.wait_until_ready()
    print('h')
    while True:
        k = input()
        print(client.guilds)
        for guild in client.guilds:
            for channel in guild.text_channels:
                await channel.send(k)
client.run('Nzk0MjA4MjE3MjY5Nzk2ODg1.X-3eCg.KNlVZ-L_6BqTVtyPO3WZkOM73UM')
