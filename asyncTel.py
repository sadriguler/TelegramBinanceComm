import asyncio
from telethon import TelegramClient, events

api_id = --TheId--
api_hash = --TheHash--
group_username = --groupname--

client = TelegramClient(--sessionName--, api_id, api_hash)


themsg = ""

@client.on(events.NewMessage(chats = group_username, incoming = True))
async def handler(event):
    chats = await client.get_messages(group_username, 1)
    global themsg
    themsg = chats[0].message
    #if(themsg[0:8]=='The coin'):
    if(themsg):
        counter = 0
        while(themsg[counter]!=':'):
           counter = counter + 1
           if(themsg[counter+2]=='$'):
              thecoin = themsg[counter+3:counter+6]
           else:
              thecoin = themsg[counter+2:counter+5]
        await client.disconnect()
    # Say "!pong" whenever you send "!ping", then delete both messages
    # m = await event.respond('!pong')
    # await asyncio.sleep(5)
    # sawait client.delete_messages(event.chat_id, [event.id, m.id])  

client.start()
client.run_until_disconnected()

print(themsg)