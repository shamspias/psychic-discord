from discord import Intents
from discord.ext import commands

from config.development import CONFIG

intents = Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


bot.load_extension("cogs.music.player")
bot.load_extension("cogs.basic_commands")
bot.run(CONFIG["BOT_TOKEN"])
