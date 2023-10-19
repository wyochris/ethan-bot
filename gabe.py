import random
from discord.ext import commands

class RandomCapsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="gabe")
    async def random_caps_gabe(self, ctx):
        # Find a random message from a specific user that's in all caps
        user_id_to_check = 123456789012345678  # Replace with the target user's ID
        random_message = self.find_random_caps_message(ctx.guild, user_id_to_check)

        # Send the random message
        if random_message:
            await ctx.send(random_message)
        else:
            await ctx.send("No matching message found.")

    def find_random_caps_message(self, guild, user_id):
        user = guild.get_member(user_id)

        if user:
            # Filter messages from the specified user that are in all caps
            caps_messages = [msg.content for msg in user.history(limit=100) if msg.content.isupper()]

            # Choose a random message from the filtered list
            if caps_messages:
                return random.choice(caps_messages)

        return None