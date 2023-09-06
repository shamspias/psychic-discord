from discord.ext import commands
from config.development import CONFIG


class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='invite')
    async def send_invite(self, ctx):
        invite_link = f"https://discord.com/oauth2/authorize?client_id={CONFIG['DISCORD_CLIENT_ID']}&scope=bot&permissions=3148800"
        await ctx.author.send(f"Here's the invite link for the bot: {invite_link}")

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")


def setup(bot):
    bot.add_cog(BasicCommands(bot))
