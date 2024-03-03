import os
from dotenv import load_dotenv
import discord

load_dotenv()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f"Le bot discord est prêt {client.user}")


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  elif message.content.startswith('!bonjour'):
    await message.channel.send('Bonjour !')


@client.event
async def on_member_join(member):
  welcome_channel_id = os.getenv("WELCOME_CHANNEL_ID")
  channel = client.get_partial_messageable(welcome_channel_id)
  await channel.send(f"Bienvenue {member.name}")


token = os.getenv("BOT_DISCORD")
client.run(token=token)