import os
import sys
import time

from webwhatsapi import WhatsAPIDriver

driver = 0
def numtoname(lst):
    namelst = []
    numberlst = []
    for i in lst:
        namelst.append(' '.join(str(i).split()[1:-1]))
        numberlst.append(str(i).split()[-1].rstrip('>)').lstrip('('))
    for i in range(len(namelst)):
        if namelst.count(namelst[i]) > 1:
            namelst[i] = namelst[i]+' ('+numberlst[i].rstrip('@.qwertyuiopasdfghjklzxcvbnm')+')'
    f = {numberlst[i]:namelst[i] for i in range(len(namelst))}
    return f
    
def run():
    global driver
    driver = WhatsAPIDriver()
    print("Waiting for QR")
    driver.wait_for_login()
    print("Bot started")

    driver.subscribe_new_messages(NewMessageObserver())
    print("Waiting for new messages...")

    """ Locks the main thread while the subscription in running """
    while True:
        time.sleep(60)


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
            else:
                print(
                    "New message of type '{}' received from number {}".format(
                        message.type, message.sender.id
                    )
                )


if __name__ == "__main__":
    run()
