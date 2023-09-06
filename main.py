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


async def load_cogs():
    print("Loading cogs...")
    await bot.load_extension("cogs.music.player")
    await bot.load_extension("cogs.basic_commands")
    print("Cogs loaded successfully!")


# Load the cogs before running the bot
asyncio.get_event_loop().run_until_complete(load_cogs())

# Run the bot
bot.run(CONFIG["BOT_TOKEN"])
