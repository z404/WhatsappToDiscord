import os
import sys
import time

from webwhatsapi import WhatsAPIDriver
contact_dict = {}

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
##    print("Environment", os.environ)
##    try:
##        os.environ["SELENIUM"]
##    except KeyError:
##        print("Please set the environment variable SELENIUM to Selenium URL")
##        sys.exit(1)
    global driver
    driver = WhatsAPIDriver()#client="remote")
    print("Waiting for QR")
    driver.wait_for_login()
    #d = driver.get_my_contacts()
    #global contact_dict
    #contact_dict = numtoname(d)
    #chats = driver.get_all_chat_ids()
    #print(chats)
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
                print(driver.get_chat_from_id(message.chat_id),message.content,driver.get_contact_from_id(message.sender.id))
            else:
                print(
                    "New message of type '{}' received from number {}".format(
                        message.type, message.sender.id
                    )
                )


if __name__ == "__main__":
    run()
