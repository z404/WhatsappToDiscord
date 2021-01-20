import discord, threading, pyrebase, json
client = discord.Client()
with open('config.txt') as file:
    config = json.load(file)
with open('creds.txt') as file:
    bot_token = file.read().rstrip("\n ")

firebase = pyrebase.initialize_app(config)

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
