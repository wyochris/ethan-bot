import random
from discord import Guild
from discord.ext import commands

class RandomCapsCog:
    def __init__(self, client):
        self.client = client

    async def random_goob(self, message):
        user_id = 676990484123615243  # Replace with the target user's ID
        user = message.guild.get_member(user_id)
        random_message = ""
        channels_iter = [737353891867262987, 777394396411985920, 737415182841675806, 844035237981585448,
                              1164264650276356248, 936026601609658399, 737354586146471956]
        if user:
            caps_messages = []
            for channel_id in channels_iter:
                async for msg in self.client.get_channel(channel_id).history(limit=100):
                    if "goob" in msg.content.lower() and not msg.content.startswith('!'):
                        caps_messages.append(msg.content)

            if caps_messages:
                random_message = random.choice(caps_messages)

        if random_message:
            await message.channel.send(random_message)
        else:
            await message.channel.send("Error: TOO MUCH GOOBNESS")

    async def random_caps_gabe(self, message):
        user_id = 676990484123615243  # Replace with the target user's ID
        user = message.guild.get_member(user_id)
        random_message = ""
        if user:
            caps_messages = []
            channels_iter = [737353891867262987, 777394396411985920, 737415182841675806, 844035237981585448,
                              1164264650276356248, 936026601609658399, 737354586146471956]
            for channel_id in channels_iter:
                async for msg in self.client.get_channel(channel_id).history(limit=100):
                    if msg.content.replace(" ", "").isalpha() and msg.content.replace(" ", "").isupper() and msg.author == user and not msg.content.startswith('!'):
                        caps_messages.append(msg.content)
                        print(msg.content)

            if caps_messages:
                random_message = random.choice(caps_messages)

        if random_message:
            await message.channel.send(random_message)
        else:
            await message.channel.send("Error: Science says 2008 is the worst year.")

    async def random_chup(self, message):
        user_id = 694383907667181650  # Replace with the target user's ID
        user = message.guild.get_member(user_id)
        random_message = ""
        if user:
            caps_messages = []
            channels_iter = [737353891867262987, 777394396411985920, 737415182841675806, 844035237981585448,
                              1164264650276356248, 936026601609658399, 737354586146471956]
            for channel_id in channels_iter:
                async for msg in self.client.get_channel(channel_id).history(limit=100):
                    if msg.author == user and not msg.content.startswith('!'):
                        caps_messages.append(msg.content)
                        print(msg.content)

            if caps_messages:
                random_message = random.choice(caps_messages)

        if random_message:
            await message.channel.send(random_message)
        else:
            await message.channel.send("Error: sad meow")



