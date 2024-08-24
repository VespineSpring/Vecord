from vecord import Bot
import discord

command_prefix = "!"
intents = discord.Intents.all()

bot = Bot(command_prefix=command_prefix, intents=intents)

bot.run("TOKEN")
