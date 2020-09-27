from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['hello]'])
    async def hello(self, ctx):
        await ctx.send("Hey There!\nI am working!")

    @commands.command(aliases=['ping]'])
    async def ping(self, ctx):
        await ctx.send(f"Latency: {round(self.bot.latency * 1000)}ms")
    

def setup(bot):
    bot.add_cog(General(bot))