import discord
import time
import asyncio
import random
id = |CLIENTID|
client = discord.Client()

@client.event
async def on_message(message):
    id = client.get_guild(CLIENTID)
    channels = {"|Channel1|", "|Channel2|"}
    valid_users = {"User1", "User2", "User3"}
    joking_list = {"User1"}
    joke = ("Honestly, go away.", "It's a beautiful day in the neighbourhood.", "haha, funny guy, haha...")
    luck = random.randint(0,2)

    if str(message.author) in joking_list and luck == 1:
        await message.channel.send(random.choice(joke))
    if message.content == "!help":
        embed = discord.Embed(title = "Help on BOT", description = "Some neglected commands.")
        embed.add_field(name="!hello", value = "Bots description and greeting.")
        embed.add_field(name="!users", value = "Shows the count of members.")
        embed.add_field(name="!game", value = "Faulty programming bug.")
        embed.add_field(name="!joke", value = "Tells you a joke.")
        embed.add_field(name="secret", value = "unknown")
        await message.channel.send(content=None, embed=embed)

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!joke") != -1:
            jokemessage = (f"""@{message.author} oh, bless your heart.""", f"""Oh, why, hello @{message.author}, @{message.author} just asked me to say this.""", f"""Woah, @{message.author}, that is *not* very nice, does someone need to be muted?""", f"""Come to think of it, I haven't figured out to really exist as a bot yet.""", f"""@{message.author}, if I knew you were so funny, I would have been clapping these hands from the start.""")
            await message.channel.send(random.choice(jokemessage))
        if message.content.find("bazzas command") != -1:
            await message.channel.send("Oi! |User{x}| wanted me to give you this message. YOU'RE A FUNNY GUY! *cough cough*")
        if message.content.find("!hello") != -1:
            await message.channel.send("Hey! I'm a self designed bot.")
        if message.content.find("!game") != -1:
            await message.channel.send("...I'm not designed for that")
        if message.content.find("!users") != -1:
            await message.channel.send(f"""# of Members: {id.member_count}""")

client.run("[Numbers].[Numerics].[Server-ID]")
