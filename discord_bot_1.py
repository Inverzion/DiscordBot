import discord
#id = 832113653758427146
client = discord.Client()

@client.event
async def on_message(message):
    id = client.get_guild(832113653758427146)
    channels = {"testing-and-bot-commands"}
    valid_users = {"Inverzion#1167", "ArtisticSloth#6223", "yeetedon#1458"}
    bullying_list = {"Inverzion#1167"}
    import random
    bully = ("Honestly, fuck off.", "It's a beautiful day in the neighbourhood.", "haha, funny guy, haha...")
    luck = random.randint(0,2)

    if str(message.author) in bullying_list and luck == 1:
        await message.channel.send(random.choice(bully))

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("bazzas command") != -1:
            await message.channel.send("Oi, Aids Monkey. Bazza wanted me to give you this message. YOU'RE A FUCKING BITCH! *cough cough*")
        if message.content.find("!hello") != -1:
            await message.channel.send("Hey! I'm a self designed bot.")
        elif message.content.find("!game") != -1:
            await message.channel.send("...I'm not designed for that")
        elif message.content.find("!help") != -1:
            await message.channel.send("List of commands: (!hello, !hey, !game)")
        elif message.content =="!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")

client.run("ODMyMDc4ODYxNjEzMDA2ODcw.YHej0w.a14W0YJkeKWcjzids74BvQyTsI4")
