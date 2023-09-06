from discord.ext import commands
from config.development import CONFIG


class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def _ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command(name='invite')
    async def _invite(self, ctx):
        client_id = CONFIG.get("DISCORD_CLIENT_ID")
        invite_link = f"https://discord.com/oauth2/authorize?client_id={client_id}&scope=bot"
        await ctx.author.send(f"Invite me to your server using this link: {invite_link}")


async def setup(bot):
    await bot.add_cog(BasicCommands(bot))
