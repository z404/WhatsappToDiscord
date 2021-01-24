import os, json
import sys
import time
import threading
import discord
#import pyrebase

from webwhatsapi import WhatsAPIDriver

driver = 0

flag = False
msg = {}

def run():
    global driver
    driver = WhatsAPIDriver()
    print("Waiting for QR")
    driver.wait_for_login()
    print("Bot started")

    driver.subscribe_new_messages(NewMessageObserver())
    print("Waiting for new messages...")

    #with open('config.txt') as file:
    #    config = json.load(file)
    #firebase = pyrebase.initialize_app(config)
    #db = firebase.database()
    #db.set({"hello":"hi"})

    with open('creds.txt') as file:
        bot_token = file.read().rstrip("\n ")
    client = discord.Client()
    mythread = threading.Thread(target=client.run,args=[bot_token])
    mythread.daemon = True
    mythread.start()
    @client.event
    async def on_ready():
        chan = client.get_channel(794208812944588863)
        #print(client.guilds)
        #if flag == True:
        global flag,msg
        while True:
            if flag:
                flag = False
                await chan.send('['+msg['origin']+'] {'+msg['sender'].rstrip('\n ')+'} '+msg['message'])
                print(msg['originid']['_serialized'])
                with open('data.csv','a+') as file:
                    file.write('\n '+msg['originid']['_serialized']+','+msg['origin'])
                
    """ Locks the main thread while the subscription in running """
    global flag, msg
    while True:
        pass


class NewMessageObserver:

    def on_message_received(self, new_messages):
            
        for message in new_messages:
            if message.type == "chat":
                global contact_dict
                global driver
                if 'Group chat' in str(driver.get_chat_from_id(message.chat_id)):
                    name = str(driver.get_chat_from_id(message.chat_id))[14:].split(':')[0]
                    typ = 'group'
                else:
                    name = str(driver.get_chat_from_id(message.chat_id))[13:].split(':')[0]
                    typ = 'dm'
                contact = str(driver.get_contact_from_id(message.sender.id))[9:].split('(')[0]
                global msg, flag
                msg.update({'message':message.content,'origin':name,'sender':contact,'originid':message.chat_id,'senderid':message.sender.id,'type':typ})
                flag = True
            else:
                print(
                    "New message of type '{}' received from number {}".format(
                        message.type, message.sender.id
                    )
                )


if __name__ == "__main__":
    run()
