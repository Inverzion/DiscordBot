import discord
import random
import games.py
games = open('games.py', 'x')
#id = 832113653758427146
client = discord.Client()

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send(f"""Aye, you're a cunt waffle {member.mention}""")

@client.event
async def on_message(message):
    id = client.get_guild(832113653758427146)
    channels = {"testing-and-bot-commands"}
    valid_users = {"Inverzion#1167", "ArtisticSloth#6223", "yeetedon#1458"}
    bullying_list = {"yeetedon#1458", "Inverzion#1167"}
    bully = random.randint(0, 4)
    bully1 = bully
    0 = ("Oh, so now you's the bitch I hate")
    1 = ("This isn't harassment lil hoe, this be trolling")
    2 = ("Fucking SHUT UP already... thanks")
    3 = ("I may be stupid, but god damn you're retarded. Like getting dropkicked by the angel of dumb and hitting every single stupid branch down the retard tree")
    4 = ("On behalf of all of my bot friends, you are the worst")
    bully_init = bully1

    if str(message.author) in bullying_list:
        await message.channel.send(bully_init)
    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hey") != -1:
            await message.channel.send("Oi, Aids Monkey")
        if message.content.find("!hello") != -1:
            await message.channel.send("HEY! I'M A FUCKING ROBOT")
        elif message.content.find("!game") != -1:
            await message.channel.send(games)
        elif message.content.find("!help") != -1:
            await message.channel.send("List of commands: (!hello, !hey, !game)")
        elif message.content =="!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")

client.run("ODMyMDc4ODYxNjEzMDA2ODcw.YHej0w.a14W0YJkeKWcjzids74BvQyTsI4")
