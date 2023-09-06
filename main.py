import discord
import asyncio
from discord.ext import commands
from config import CONFIG

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix=CONFIG["COMMAND_PREFIX"], intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.command()
async def test(ctx):
    await ctx.send("Test command is working!")


def load_cogs():
    print("Test")
    bot.load_extension("cogs.music.player")
    bot.load_extension("cogs.basic_commands")


# If you have a token in your CONFIG
bot.run(CONFIG["BOT_TOKEN"])
