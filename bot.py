import discord
from discord.ext import commands

import json
import os

with open("config.json", 'r') as f:
    config = json.load(f)

bot = commands.Bot(command_prefix=config['prefix'])

TOKEN = config['token']


@bot.event
async def on_ready():
    print("--------------------")
    print("Bot is online!")
    print(f"Logged in as {bot.user}")
    print(f"ID: {bot.user.id}")
    print("--------------------")

    # channel = bot.get_channel(756221377035501618)
    # await channel.send('Yes master, I am here now')

for filename in os.listdir('cogs'):
    try:
        if filename.endswith('.py'):
            cog = f"cogs.{filename.replace('.py','')}"
            bot.load_extension(cog)
            # bot.load_extension(cog)
    except Exception as e:
        print(f'{cog} could not be loaded')
        raise e

bot.run(TOKEN)