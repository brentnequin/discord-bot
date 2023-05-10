import os
from dotenv import load_dotenv

import random

import discord
from discord.ext import commands

from fortnite import landing_spots

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
  
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

fornite_season_chapter = (4, 2)

@bot.command(name='fn')
async def fortnite_choose_random_landing_spot(ctx):
    await ctx.send(random.choice(landing_spots(*fornite_season_chapter)))

bot.run(token)
