#!/usr/bin/env python

from random import randrange, choice, randint
import discord
import asyncio
import time
from requests import get

TOKEN_AUTH = "" # YOUR TOKEN HERE
ip = "" # YOUR IP HERE, LEAVE BLANK IF YOU DONT USE A VPN
username = "" # YOUR USERNAME HERE, THE THING PEOPLE CALL U

client = discord.Client()
@client.event
async def on_ready():
    print(client.guilds)
    
ban = []
ty = ["yo","thanks","Thank you","thank you"]

class c:
    cache = ""
    sent = []
    can = False
    
@client.event
async def on_reaction_add(reaction, user):
    print("Someone reacted")
    if reaction.message.channel.id == 699702250531979325 or reaction.message.channel.id == 755024910023131167 or reaction.message.channel.id == 639195586070839316:
        if reaction.emoji == "🎉":
            if reaction.message.id not in ban:
                if "bot" not in reaction.message.content.lower():
                    if reaction.message.author.id == 617037497574359050:
                        print(f"Detected giveaway, sleeping")
                        await asyncio.sleep(round(randint(5,10)))
                        await reaction.message.add_reaction("🎉")
                        ban.append(reaction.message.id)
                        print(f"Reacted!")
                else:
                    print(f"PanicSleep: {reaction.message.content.lower()}")
                    time.sleep(60)
                    print("PanicSleepEnd")
                    return
            else:
                print(f"Already reacted!")
@client.event
async def on_message(message):
    if "bot" in message.content.lower():
        print(f"PanicSleep: {message.content.lower()}")
        time.sleep(60)
        print("PanicSleepEnd")
        return

    if username in message.content.lower():
        print(f"PanicSleep: {message.content.lower()}")
        time.sleep(600)
        print("PanicSleepEnd")
        return

    if message.content.startswith("$phrasedrop"):
        c.can = True
        await asyncio.sleep(60)
        c.can = False

    if message.content.startswith("$airdrop"):
        val = randrange(21)
        if val == 7:
            await asyncio.sleep(randint(5,15))
            await message.channel.send(choice(ty))

    if str(c.cache) not in c.sent:
        if message.author.id != 0:
            if c.cache == message.content.lower():
                if str(c.cache) not in c.sent:
                    await asyncio.sleep(randint(0,3))
                    if c.cache != None and c.cache != "":
                        if c.can:
                            print(f"c.cache = {c.cache}")
                            c.can = False
                            await message.channel.send(f"{c.cache}")
                            print(f"Sent c.cache")
                            time.sleep(10)
                            c.sent.append(c.cache)
                            c.cache = None
                            return


    if message.author.id != 1:
        if message.author.id != 0:
            if message.content.lower().startswith("$") == False:
                await asyncio.sleep(0.5)
                if message.reactions != []:
                    c.cache = message.content.lower()
                    print(f"c.cache = {c.cache}")
                else:
                    try:
                        x = float(message.content)
                    except:
                        pass
                    else:
                        c.cache = message.content

if get('https://api.ipify.org').text != str(ip):
    client.run(TOKEN_AUTH, bot=False)
else:
    print("HOME IP")
    quit()
