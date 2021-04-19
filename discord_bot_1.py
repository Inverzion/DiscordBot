import discord
import time
import asyncio
#id = 832113653758427146
client = discord.Client()

async def update_stats():
    await client.wait_until_ready()
    global messages, joined
    
    while not client.is_closed():
        try:
            with open("stats.txt", "w") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")
                
            await asyncio.sleep(30)
        except Exception as e:
            print(e)
            await asyncio.sleep(30)

@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the shitshow {member.mention}""")
    

@client.event
async def on_message(message):
    global messages
    messages += 1
    id = client.get_guild(832113653758427146)
    channels = {"testing-and-bot-commands"}
    valid_users = {"Inverzion#1167", "ArtisticSloth#6223", "yeetedon#1458"}
    bullying_list = {"Inverzion#1167"}
    import random
    bully = ("Honestly, fuck off.", "It's a beautiful day in the neighbourhood.", "haha, funny guy, haha...")
    luck = random.randint(0,2)
    bullymemessage = ("You're so dumb, I bet you couldn't drink booze out of a boot if the isntructions were written on the sole.", f"""My god you're retarded, who let you out of the speds class?, was it{random.choice(valid_users)}?""", "That's it, whatever you just said provoked me to call the cops on you.", "Woah, that's not very nice, it's almost as offensive as the kids in my basement.", "Come to think of it, I've fucked both of your moms.", "Shit bro, if I knew you were single, I would've been clapping those cheeks.")

    if str(message.author) in bullying_list and luck == 1:
        await message.channel.send(random.choice(bully))
    if message.content == "!help":
        embed = discord.Embed(title = "Help on BOT", description = "Some neglected commands")
        embed.add_field(name="!hello", value = "Bots description and greeting.")
        embed.add_field(name="!users", value = "Shows the count of members.")
        embed.add_field(name="!game", value = "Faulty programming bug")
        await message.channel.send(content=None, embed=embed)

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("bazzas command") != -1:
            await message.channel.send("Oi, Aids Monkey. Bazza wanted me to give you this message. YOU'RE A FUCKING BITCH! *cough cough*")
        if message.content.find("!hello") != -1:
            await message.channel.send("Hey! I'm a self designed bot.")
        elif message.content.find("!game") != -1:
            await message.channel.send("...I'm not designed for that")
        elif message.content.find("!users") != -1:
            await message.channel.send(f"""# of Members: {id.member_count}""")
        elif message.content.find("!bullyme") != -1:
            await message.channel.send(random.choice(bullymemessage))

client.loop.create_task(update_stats())          
client.run("ODMyMDc4ODYxNjEzMDA2ODcw.YHej0w.a14W0YJkeKWcjzids74BvQyTsI4")
