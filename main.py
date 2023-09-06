import discord
from discord.ext import commands
from cogs.music.player import MusicPlayer
from config import development as config

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


bot.add_cog(MusicPlayer(bot))
bot.run(config.CONFIG["BOT_TOKEN"])
