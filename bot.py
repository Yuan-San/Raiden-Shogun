import discord
import logging
import sys
from discord.ext import commands
from cogs import music, error, meta, tips
import config
import os
import platform

cfg = config.load_config()

bot = commands.Bot(command_prefix=cfg["prefix"])
bot.remove_command('help')


@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user.name}")
    print('Bot logged in as')
    print('Username: ' + bot.user.name)
    print('Id: ' + str(bot.user.id))
    print('--------')
    print(
        f'| Connected to {str(len(bot.guilds))} servers | Connected to {str(len(set(bot.get_all_members())))} users |'
    )
    print(' Servers include:')
    for item in bot.guilds:
        print('  - {}'.format(item.name))
    print('--------')
    print(
        f'Current Discord.py Version: {discord.__version__} | Current Python Version: {platform.python_version()}'
    )
    print('--------')
    print(f'Use this link to invite {bot.user.name}:')
    print(
        f'https://discordapp.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8'
    )
    print('--------')

    return await bot.change_presence(activity=discord.Game(
        name='Loops ;help'))


COGS = [music.Music, error.CommandErrorHandler, meta.Meta, tips.Tips]


def add_cogs(bot):
    for cog in COGS:
        bot.add_cog(cog(bot, cfg))  # Initialize the cog and add it to the bot


def run():
    add_cogs(bot)
    bot.run(os.getenv('TOKEN'))