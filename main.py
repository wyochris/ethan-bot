from dotenv import load_dotenv
import os
import discord
import random
from gabe import RandomCapsCog

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
client = discord.Client(intents=discord.Intents.all())

def setup(bot):
    bot.add_cog(RandomCapsCog(bot))

# set up bot
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    setup(client)
    await client.change_presence(activity=discord.Game(name='!ethan help!'))

# bot main loop
@client.event
async def on_message(message):
    
    # Ignore messages sent by the bot
    if message.author == client.user:
        return
    

def run():
    try:
        client.run(discord_token)
    except Exception as e:
        # let's me know if client.run() doesn't work
        print(f'Chris broke the bot: {e}')

run()