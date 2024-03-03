import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
#async def kick(context, member):
async def kick(context, member: discord.Member):
  #await context.guild.kick(member)
  await context.guild.kick(member, reason="Raison")

@bot.command()
async def ban(context, member):
  pass

@bot.command()
async def unban(context, member):
  pass

token = os.getenv("BOT_DISCORD")
bot.run(token=token)