import discord

client = discord.Client()
@client.event
async def on_ready():
    print("BOT ONLINE ~~ OLÁ MULA")
    print(client.user.name)
    print(client.user.id)
    print('-------NOIA------')

    client.run('OTIwMDg5OTczNzE2Mjk1NzEw.YbfSkA.kCXs3iT9j1obvyihfJHp7blWXgM')

