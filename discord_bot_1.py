import discord
import time
import asyncio
import random
id = 832078861613006870
client = discord.Client()

@client.event
async def on_message(message):
    id = client.get_guild(832113653758427146)
    channels = {"newage-botcommands", "the-gate📱"}
    valid_users = {"Inverzion#1167", "ArtisticSloth#6223", "yeetedon#1458"}
    bullying_list = {"Inverzion#1167"}
    bully = ("Honestly, fuck off.", "It's a beautiful day in the neighbourhood.", "haha, funny guy, haha...")
    luck = random.randint(0,2)

    if str(message.author) in bullying_list and luck == 1:
        await message.channel.send(random.choice(bully))
    if message.content == "!help":
        embed = discord.Embed(title = "Help on BOT", description = "Some neglected commands")
        embed.add_field(name="!hello", value = "Bots description and greeting.")
        embed.add_field(name="!users", value = "Shows the count of members.")
        embed.add_field(name="!game", value = "Faulty programming bug.")
        embed.add_field(name="!bullyme", value = "Insulting yourself? really?")
        embed.add_field(name="secret", value = "unknown")
        await message.channel.send(content=None, embed=embed)

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!bullyme") != -1:
            bullymessage = (f"""@{message.author} you are so dumb, I bet you couldnt drink booze out of a boot if the isntructions were written on the sole.""", f"""That is it, whatever @{message.author} just said, provoked me to call the cops on you.""", f"""Woah, @{message.author}, that is *not* very nice, it is almost as offensive as the kids in my basement.""", f"""Come to think of it, I have fucked both of @{message.author} moms.""", f"""Shit @{message.author}, if I knew you were single, I would have been clapping those cheeks.""")
            await message.channel.send(random.choice(bullymessage))
        if message.content.find("bazzas command") != -1:
            await message.channel.send("Oi, Aids Monkey. Bazza wanted me to give you this message. YOU'RE A FUCKING BITCH! *cough cough*")
        if message.content.find("!hello") != -1:
            await message.channel.send("Hey! I'm a self designed bot.")
        if message.content.find("!game") != -1:
            await message.channel.send("...I'm not designed for that")
        if message.content.find("!users") != -1:
            await message.channel.send(f"""# of Members: {id.member_count}""")

client.run("ODMyMDc4ODYxNjEzMDA2ODcw.YHej0w.a14W0YJkeKWcjzids74BvQyTsI4")
