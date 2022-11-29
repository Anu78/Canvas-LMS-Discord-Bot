from dotenv import load_dotenv
import os
import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()

token = str(os.getenv("TOKEN"))

bot = discord.Bot(intents=discord.Intents.default())

@bot.event
async def on_ready():
	logger.info("Bot is ready")
	print("bot is ready")

for f in os.listdir("./cogs"):
	if f.endswith(".py"):
		bot.load_extension("cogs." + f[:-3])

bot.run(os.getenv("TOKEN"))