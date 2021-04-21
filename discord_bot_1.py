import discord
import time
import asyncio
import random
#id = 832113653758427146
client = discord.Client()

@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the shitshow {member.mention}""")

@client.event
async def on_message(message):
    global message
    message += 1
    id = client.get_guild(832113653758427146)
    channels = {"testing-and-bot-commands"}
    valid_users = {"Inverzion#1167", "ArtisticSloth#6223", "yeetedon#1458"}
    bullying_list = {"Inverzion#1167"}
    bully = ("Honestly, fuck off.", "It's a beautiful day in the neighbourhood.", "haha, funny guy, haha...")
    luck = random.randint(0,2)
    bullymessage = ("You are so dumb, I bet you couldnt drink booze out of a boot if the isntructions were written on the sole.", "That is it, whatever you just said provoked me to call the cops on you.", "Woah, that is *not* very nice, it is almost as offensive as the kids in my basement.", "Come to think of it, I have fucked both of your moms.", "Shit bro, if I knew you were single, I would have been clapping those cheeks.")

    if str(message.author) in bullying_list and luck == 1:
        await message.channel.send(random.choice(bully))
    elif message.content == "!help":
        embed = discord.Embed(title = "Help on BOT", description = "Some neglected commands")
        embed.add_field(name="!hello", value = "Bots description and greeting.")
        embed.add_field(name="!users", value = "Shows the count of members.")
        embed.add_field(name="!game", value = "Faulty programming bug.")
        await message.channel.send(content=None, embed=embed)

    elif str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("bazzas command") != -1:
            await message.channel.send("Oi, Aids Monkey. Bazza wanted me to give you this message. YOU'RE A FUCKING BITCH! *cough cough*")
        elif message.content.find("!hello") != -1:
            await message.channel.send("Hey! I'm a self designed bot.")
        elif message.content.find("!game") != -1:
            await message.channel.send("...I'm not designed for that")
        elif message.content.find("!users") != -1:
            await message.channel.send(f"""# of Members: {id.member_count}""")

client.run("ODMyMDc4ODYxNjEzMDA2ODcw.YHej0w.a14W0YJkeKWcjzids74BvQyTsI4")
