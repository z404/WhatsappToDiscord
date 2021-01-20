import asyncio, discord, time, threading, asyncio, pyrebase
client = discord.Client()

with open('creds.txt') as file:
    bot_token = file.read().rstrip("\n ")
    
config = {
    'apiKey': "AIzaSyBqjdapVjCIDPdMa4kHXdQ7-Z9ZL5vxYIk",
    'authDomain': "watodiscord.firebaseapp.com",
    'databaseURL': "https://watodiscord-default-rtdb.firebaseio.com",
    'projectId': "watodiscord",
    'storageBucket': "watodiscord.appspot.com",
    'messagingSenderId': "819150139392",
    'appId': "1:819150139392:web:c66bd99b705e88c61568e5",
    'measurementId': "G-B4DGC2M0V0"
}

firebase = pyrebase.initialize_app(config)
#client.run('Nzk0MjA4MjE3MjY5Nzk2ODg1.X-3eCg.yZeNNyqqFYVtXza6TEH_tPx9DqI')

msg = ''
flag = False
count = 0

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
            await chan.send(msg)



db = firebase.database()
def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}qq
    global count,msg,flag
    msg=message['data']
    if count == 0:
        count+=1
    else:
        flag = True

my_stream = db.stream(stream_handler)
