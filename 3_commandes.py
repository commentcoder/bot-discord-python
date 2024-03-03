import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(context):
  await context.send("Pong")


@bot.command()
async def aide(context):
  embed = discord.Embed(
      title="Commandes",
      description="Une liste des commandes du serveur",
      colour=discord.Colour.random()
  )
  embed.set_thumbnail(url="https://www.commentcoder.com/favicon.ico")
  embed.add_field(name="!ping", value="Répond Pong")
  await context.send(embed=embed)


token = os.getenv("BOT_DISCORD")
bot.run(token=token)