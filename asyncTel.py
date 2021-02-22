import asyncio
from telethon import TelegramClient, events

import time
from matplotlib.pyplot import plot
from binance.client import Client
clientBinance = Client(binance-API-ID, binance-API-HASH)

api_id = Telegram-API-ID
api_hash = Telegram-API-HASH
group_username = Telegram-Group-Name

client = TelegramClient(Telegram-Session-Name, api_id, api_hash)


thecoin = ""

# asynchronous event handler for new messages
@client.on(events.NewMessage(chats = group_username, incoming = True))
async def handler(event):
    chats = await client.get_messages(group_username, 1)
    global thecoin
    themsg = chats[0].message
    print("The received message is: " + themsg)
    
    # A very basic algorithm to check the coin name
    if(themsg[0:9]=='COIN IS :'):
        coinlen = len(themsg)
        counter = 9
        while(not themsg[counter].isalpha()):
            counter = counter + 1
        thestarter = counter
        print("Founded counter value is: " + str(counter))    
        while (themsg[counter].isalpha()):
            counter = counter + 1
            if (counter == coinlen):
                break
        thecoin = themsg[thestarter:counter].upper()
        print("Possible coin name is: " + thecoin)
        await client.disconnect()

client.start()
client.run_until_disconnected()

# print the founded symbol
thesymbol = str(thecoin) + "BTC"
print("The founded symbol is: " + thesymbol)

# track symbol in binance
start = time.time()
thefile = open("thepricedata.txt","w") 
ticker = clientBinance.get_orderbook_ticker(symbol=thesymbol)
firstprice = float(ticker['askPrice'])
thetime = 0
while(thetime < 1200):
    ticker = clientBinance.get_orderbook_ticker(symbol=thesymbol)
    lastprice = float(ticker['askPrice'])
    thetime = time.time() - start
    thefile.write(str(thetime) + "\t" + str(lastprice) + "\n")
    firstprice = lastprice

thefile.close()
print("end")