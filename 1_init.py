import os
from dotenv import load_dotenv
import discord

load_dotenv()
token = os.getenv("BOT_DISCORD")

intents = discord.Intents.all()
client = discord.Client(intents=intents)

client.run(token=token)