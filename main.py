from discord.ext import commands
from discord import Intents
from cogs.music.player import MusicPlayer
from config.development import CONFIG

intents = Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


bot.add_cog(MusicPlayer(bot))
bot.run(CONFIG["BOT_TOKEN"])
