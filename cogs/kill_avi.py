import discord
from discord.ext import commands
from discord.utils import get

import asyncio
import enchant
import json
import string
import requests

class AviKiller(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def vegetable(self, user, channel):
        vegetable_role = get(user.guild.roles, name='VEGETABLE')
        
        await channel.send(f"{user.mention} has been vegetableised for 5 mins!")

        await asyncio.sleep(300) # CHANGE TO 300 LATER

        await user.remove_roles(vegetable_role)

        await channel.send(f"{user.mention} has been unvegetableised!")
    
    def check_URL(self, string_to_check):
        try:
            res = requests.get(string_to_check)
            return True
        except:
            return False


    def check_sentence(self, sentence):
        d = enchant.DictWithPWL("en_GB", "slang.txt")

        if self.check_URL(sentence) == True: return False

        sentence = sentence.translate(str.maketrans('', '', string.punctuation))

        words = sentence.split(" ")
        good_words = []

        for word in words:
            try:
                is_word = d.check(word) 

                if is_word: good_words.append(True)
                else: good_words.append(False)
            except: pass
        
        valid_words = sum(good_words)

        percentage = (valid_words / len(words)) * 100

        if percentage <= 50:
            return True
        else: return False


    async def spam(self, message):

        channel = message.channel

        messages = await channel.history(limit=10).flatten()
        occurences = []

        for i in messages:
            if i.author == message.author and message.author != self.bot.user and len(i.attachments) < 1 and i.content[0].isalpha() == True:
                occurences.append(i.content)
        
        offences = []

        for i in occurences:

            is_spam = self.check_sentence(i)

            if is_spam:
                offences.append(i)
            if len(i) == 1:
                offences.append(i)
        
        if len(offences) >= 5:
            await self.vegetable(message.author, channel)

def setup(bot):
    n = AviKiller(bot)
    bot.add_listener(n.spam, "on_message")
    bot.add_cog(n)