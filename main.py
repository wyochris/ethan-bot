from dotenv import load_dotenv
from gabe import RandomCapsCog
from discord.ext import commands
import os
import discord

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=discord.Intents.all())

# set up bot
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='2008'))

# bot main loop
@client.event
async def on_message(message):
    
    # Ignore messages sent by the bot
    if message.author == client.user:
        return
        
    if message.content.startswith('!goob'):
        cog = RandomCapsCog(client)
        await cog.random_goob(message)
    if message.content.startswith('!cabe'):
        cog = RandomCapsCog(client)
        await cog.random_caps_gabe(message)
    if message.content.startswith('!chup'):
        cog = RandomCapsCog(client)
        await cog.random_chup(message)

 
def run():
    try:
        client.run(discord_token)
    except Exception as e:
        # let's me know if client.run() doesn't work
        print(f'Chris broke the bot: {e}')

run()