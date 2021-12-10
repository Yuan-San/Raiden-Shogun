from discord.ext import commands
import discord
import random


class Tips(commands.Cog):
    """Commands for providing tips about using the bot."""

    def __init__(self, bot, config):
        self.bot = bot
        self.config = config[__name__.split(".")[-1]]
        self.tips = ["You dont need to vote to skip songs- Everyone can skip!",
                     f"You can check out my source code here: {self.config['github_url']}", "I can't verify this bot, Means that this bot cant be invited when reaching 100 Servers because i don't have an ID or passport. If you guys want to support this bot, you can DM me to be one of the staff and helping me verify this bot.", "Play songs from this bot for free! I just avoiding google taking down this bot, hehe :v .", "Creating a Roleplay server? DM me to create private bots exclusive for you!", "You can type `;clearqueue` to stop all songs from the queue and clears it without disconnecting!"]

    @commands.command()
    async def tip(self, ctx):
        """Get a random tip about using the bot."""
        index = random.randrange(len(self.tips))
        await ctx.send(f"**Tip #{index+1}:** {self.tips[index]}")

    @commands.command()
    async def invite(self, ctx):
        """Get a random tip about using the bot."""
        embed=discord.Embed(title="Invite the bot", description="Invite Raiden Shogun Here, or You can invite the backup instead, Raiden Mei.", color=0x850ae9)
        embed.add_field(name="Raiden Shogun (Python)", value="https://discord.com/api/oauth2/authorize?client_id=887551771805876237&permissions=8&scope=bot", inline=False)
        embed.add_field(name="Raiden Mei (Node.JS)", value="https://discord.com/api/oauth2/authorize?client_id=918739176852172880&permissions=8&scope=bot", inline=False)
        embed.set_footer(text="Yuan Mizuna!#9666")
        await ctx.send(embed=embed)