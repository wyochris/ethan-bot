from dotenv import load_dotenv
import os
import discord

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=discord.Intents.all())

# List of forbidden words
forbidden_words = ["mas", "christmas", "santa", "tree"]
admin_log_channel = 800890929296834561

# set up bot
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='!ethan help!'))

# bot main loop
@client.event
async def on_message(message):
    
    # Ignore messages sent by the bot
    if message.author == client.user:
        return
    
@client.event
async def on_member_update(before, after):
    if "mas" in after.display_name.lower():
        try:
            # Replace 'mas' with 'sigiving' in the nickname
            new_nickname = after.display_name.replace("mas", "sigiving")
            await after.edit(nick=new_nickname)
            print(f"Updated nickname for {after.name} from {after.display_name} to {new_nickname}")
            if admin_log_channel:
                await admin_log_channel.send(f"Changed nickname for {after.name} from '{after.display_name}' to '{new_nickname}'")
        except discord.Forbidden:
            print(f"Do not have permission to change nickname for {after.name}")
    if any(forbidden_word in after.display_name.lower() for forbidden_word in forbidden_words):
        try:
            new_nickname = after.display_name.replace(before.name, before.name + "sigiving")
            await after.edit(nick=new_nickname)
            if admin_log_channel:
                await admin_log_channel.send(f"Changed nickname for {after.name} from '{after.display_name}' to '{new_nickname}'")
            print(f"Changed nickname for {after.name}")
        except discord.Forbidden:
            print(f"Do not have permission to change nickname for {after.name}")

def run():
    try:
        client.run(discord_token)
    except Exception as e:
        # let's me know if client.run() doesn't work
        print(f'Chris broke the bot: {e}')

run()