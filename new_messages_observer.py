import os
import sys
import time

from webwhatsapi import WhatsAPIDriver

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
    
driver = WhatsAPIDriver()#client="remote")
print("Waiting for QR")
driver.wait_for_login()
print("Bot started")
d = driver.get_my_contacts()

contact_dict = numtoname(d)

driver.subscribe_new_messages(NewMessageObserver())
while True:
    time.sleep(60)
    
class NewMessageObserver:
    def on_message_received(self, new_messages):
        for message in new_messages:
            if message.type == "chat":
                print(
                    "New message '{}' received from number {}".format(
                        message.content, message.sender.id
                    )
                )
            else:
                print(
                    "New message of type '{}' received from number {}".format(
                        message.type, message.sender.id
                    )
                )
