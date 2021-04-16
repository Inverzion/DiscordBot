import discord
#id = 832113653758427146
client = discord.Client()

@client.event
async def on_message(message):
    id = client.get_guild(832113653758427146)
    channels = {"testing-and-bot-commands"}
    valid_users = {"Inverzion#1167", "ArtisticSloth#6223", "yeetedon#1458"}
    bullying_list = {"yeetedon#1458", "Inverzion#1167"}
    import random
    bully = ("new", "something", "let's try")

    if str(message.author) in bullying_list:
        await message.channel.send(random.choice(bully))

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
