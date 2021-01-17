import os
import sys
import time
import threading

from webwhatsapi import WhatsAPIDriver
import discord

driver = 0
client = 0

new_msg_list = []
old_msg_len = 0

def run():
    global driver
    driver = WhatsAPIDriver()
    print("Waiting for QR")
    driver.wait_for_login()
    print("Bot started")

    driver.subscribe_new_messages(NewMessageObserver())
    print("Waiting for new messages...")
    global client
    global new_msg_list
    client = discord.Client()

    @client.event
    async def on_ready():
        global client
        global new_msg_list
        global old_msg_len
        await client.wait_until_ready()
        while True:
            if len(new_msg_list) != old_msg_len:
                old_msg_len+=1
                print(client.guilds)
                for guild in client.guilds:
                    for channel in guild.text_channels:
                        await channel.send('lol')
            else: print('Nope..',len(new_msg_list),old_msg_len)
    #mythread = threading.Thread(target=client.run,args=[client_key])
    #mythread.daemon = True
    #mythread.start()

    client.run(client_key)
class NewMessageObserver:
    
    #client.run('Nzk0MjA4MjE3MjY5Nzk2ODg1.X-3eCg.KNlVZ-L_6BqTVtyPO3WZkOM73UM')
    
    def on_message_received(self, new_messages):
        global new_msg_list
        for message in new_messages:
            if message.type == "chat":
                global contact_dict
                global driver
                if 'Group chat' in str(driver.get_chat_from_id(message.chat_id)):
                    name = str(driver.get_chat_from_id(message.chat_id))[14:].split(':')[0]
                    new_msg_list.append(name,message.content,contact)
                else:
                    name = str(driver.get_chat_from_id(message.chat_id))[13:].split(':')[0]
                contact = str(driver.get_contact_from_id(message.sender.id))[9:].split('(')[0]
                print(name,message.content,contact)
            else:
                print(
                    "New message of type '{}' received from number {}".format(
                        message.type, message.sender.id
                    )
                )


if __name__ == "__main__":
    run()
