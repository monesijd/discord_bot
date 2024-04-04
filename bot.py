import os
import discord

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

    # 1. 將使用者丟進來的訊息寫入檔案
    python_file = open('/tmp/my_python.py', 'w')
    python_file.write(message.content)
    python_file.close()


# token 改放在環境變數
client.run(os.environ['DISCORD_BOT_TOKEN'])
