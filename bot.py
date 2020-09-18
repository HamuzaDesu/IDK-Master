import discord
import json
import os


with open("config.json", 'r') as f:
    config = json.load(f)

bot = discord.Client(command_prefix=config['prefix'])

TOKEN = config['token']
print(TOKEN)
print(config)

@client.event
async def on_ready():
    print("--------------------")
    print("Bot is online!")
    print(f"Logged in as {bot.user}")
    print(f"ID: {bot.user.id}")
    print("--------------------")

for filename in os.listdir('cogs'):
    try:
        if filename.endswith('.py'):
            cog = f"cogs.{filename.replace('.py','')}"
            bot.load_extension(cog)
    except Exception as e:
        print(f'{cog} could not be loaded')
        raise e

bot.run(TOKEN)