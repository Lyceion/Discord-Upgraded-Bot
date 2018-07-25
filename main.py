#-*-coding:utf-8-*-
#DISCORD BOT BY SEPTILLIONER & CYLOPS
import discord
import asyncio
import youtube_dl
from discord.ext.commands import Bot
from discord.ext import commands
import random
from difflib import SequenceMatcher
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

client = Bot(description="Sepy", command_prefix="./", pm_help = True)
@client.event
async def on_ready():
    #for i in client.get_all_members():
    #    print(i)
    hello_messages = ["Selamün aleyküm beyler keyifler nasıl?",
                      "Sa beyler",
                      "Ya nabıyonuz ayolll :D",
                      "Selam kızlar",
                      "ulan asdfgalşsfljşasfas nabıyonuz",
                      "sa yine napıyonuz"]
    main_channel = "KANAL_ID_SI"
    #await client.send_message(discord.Object(id=main_channel),"CySep-Alpha is Ready To Test Himself For You Mr Admin :)")
    #await client.send_message(discord.Object(id=main_channel),random.choice(hello_messages))
    await client.change_presence(game=discord.Game(name='BOT BY SEPTILLIONER & MRCYLOPS'))
    print('Logged in as '+client.user.name+'  With (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected with '+str(len(set(client.get_all_members())))+' users\n------------------------\nCoded By Septillioner and Cylops\n-------------------------')
    Break_Varaible = "ext-msg"
    #while True:
        #msg = input("\nMessage To Send Server:")
        #if(msg[0:len(Break_Varaible)] == Break_Varaible):
            #break
        #await client.send_message(discord.Object(id=main_channel),msg)
        #print("Sent!")
async def on_message(message):
    print(message.content)
    #await client.send_message(message.channel, message.content)
@client.command(pass_context = True)
async def clear(ctx, number):
    try:
        number = int(number)
        counter = 0
        async for x in client.logs_from(ctx.message.channel, limit = number):
            if counter < number:
                await client.delete_message(x)
                counter += 1
    except MissingRequiredArgument:
        await client.say("Invaild Argument. Please Use With This Pattern [./clear messagecount]")
@client.command()
async def hello():
    await client.say("Sana da Hello Gülüm :))")
@client.command()
async def whois(*args):
    from lib import whois

    usage = "Whois sorgu komudunun kullanımı:\n\t./whois <www.example.com/example.com>"
    if(len(args) == 1):
        responses = ["Buluyom az beklee",
                 "Hay amk kullana kullana bu komutumu kullanıcan neysee",
                 "Tamamdır hacı 2 dk bekle",
                 "NE İŞİN VAR SENİN %s LE "%(args[0]),
                 "Üff işin gücün yokmu senin?",
                 "Ok."]
        answer_responses = ["Al knk sana whois sorgusu",
                            "Artık bi teşşekür edersin bro",
                            "buyur kanka sana taşşaklı bir %s sorgusu"%(args[0]),
                            "Buyur yarrak kalkmaz beton yetmez bir sorgu"]
        await client.say(random.choice(responses))
        #await client.say("%s bağlantılı sitenin whois sorgusu yapılıyor biraz bekleyin :)"%(args[0]))
        try:
            query_result = whois.whois_query(args[0])
            await client.say("%s\n%s"%(random.choice(answer_responses),query_result.decode('utf-8')))
        except KeyboardInterrupt:
            await client.say(usage)
    else:
        await client.say(usage)
    
client.run('BOT_TOKEN')
client.say("Selamun aleyküm beyler.")

