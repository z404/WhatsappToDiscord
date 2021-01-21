import os, json
import sys
import time
import pyrebase

from webwhatsapi import WhatsAPIDriver

driver = 0

flag = False
msg = ''

def run():
    global driver
    driver = WhatsAPIDriver()
    print("Waiting for QR")
    driver.wait_for_login()
    print("Bot started")

    driver.subscribe_new_messages(NewMessageObserver())
    print("Waiting for new messages...")

    with open('config.txt') as file:
        config = json.load(file)
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    db.set({"hello":"hi"})
    
    """ Locks the main thread while the subscription in running """
    global flag, msg
    while True:
        if flag:
            db.set({"hello":msg})
            flag = False


class NewMessageObserver:

    def on_message_received(self, new_messages):
            
        for message in new_messages:
            if message.type == "chat":
                global contact_dict
                global driver
                if 'Group chat' in str(driver.get_chat_from_id(message.chat_id)):
                    name = str(driver.get_chat_from_id(message.chat_id))[14:].split(':')[0]
                else:
                    name = str(driver.get_chat_from_id(message.chat_id))[13:].split(':')[0]
                contact = str(driver.get_contact_from_id(message.sender.id))[9:].split('(')[0]
                print(name,message.content,contact)
                global msg, flag
                msg = message.content
                flag = True
            else:
                print(
                    "New message of type '{}' received from number {}".format(
                        message.type, message.sender.id
                    )
                )


if __name__ == "__main__":
    run()
