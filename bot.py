import os
import time
import discord

time.sleep(1)
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f"目前登入身份 --> {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        await message.channel.send("Hello, world!")

# token 改放在環境變數
client.run(os.environ['DISCORD_BOT_TOKEN'])
