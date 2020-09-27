from discord.ext import commands
import discord
from discord.utils import get

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['vegetableise]', 'veg]'])
    @commands.has_permissions(administrator=True)
    async def vegetableise(self, ctx, target : discord.Member):
        vegetable_role = get(ctx.author.guild.roles, name="VEGETABLE")

        text_to_send = "What?\n What's this?\n Your hands are... green!?\nFronds sprouting from your head, spreading across the expanse of the flesh, turning all to vegetable.\nIt's covering your eyes now, blinding you, creeping across your worthless face.\nYour transformation is complete.\nYou are now condemned to live your life as a vegetable"

        await target.add_roles(vegetable_role)

        await ctx.send(f"{target.mention} was vegetableised!")
        await target.send(text_to_send)

    @commands.has_permissions(administrator=True)
    @commands.command(aliases=['unvegetableise]', 'unveg]'])
    async def unvegetableise(self, ctx, target : discord.Member):
        vegetable_role = get(ctx.author.guild.roles, name="VEGETABLE")

        text_to_send = "\nFinally.\n You can see the flesh slowly appear.\nGreen is receding, stalks and leaves shrinking.\nYour hair and hands burst through the veg, and stretch out for the first time in eons.\nYou can see again, and stretch your legs to set off."

        await target.remove_roles(vegetable_role)

        await ctx.send(f"{target.mention} was unvegetableised")
        await target.send(text_to_send)

def setup(bot):
    bot.add_cog(Moderation(bot))