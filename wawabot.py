from discord.ext import commands
import discord
import os
from dicecommand import diceroll
import numberconverter
import dotenv
import datetime
from getters import github
from resources import wawaresources

dotenv.load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
DEBUG_CHANNEL = int(os.getenv('DEBUG_CHANNEL'))

bot = commands.Bot()


@bot.event
async def on_ready():
    print("Successfully connected.")
    channel = bot.get_channel(DEBUG_CHANNEL)
    await channel.send("alo im awake")


#  =============== Slash Commands ===============

# Miscellaneous commands for testing the functionality of Discord's API and the bot 
@bot.slash_command(name="bark", description="woof..")
async def bark(ctx):
    await ctx.respond("WOOF")

@bot.slash_command(name="dice", description="Rolls a 6 sided die.")
async def dice(ctx):
    await ctx.respond(f"```{diceroll()}```")

@bot.slash_command(name="routine", description="Mol's routine")
async def routine(ctx):
    await ctx.respond(wawaresources.dailyroutine())

@bot.slash_command(name="modulo", description="Finds the modulus of two integers.")
async def modulus(ctx, number_x: int, number_y: int):
    modulus = number_x % number_y
    await ctx.respond(f"{number_x} % {number_y} = {modulus}")

@bot.slash_command(name="github_search", description="Grab information about a specific user")
async def github_search(ctx, username: str):
    profile = github.profileParser(username)
    embed = discord.Embed(
        title=f"{username}'s profile",
        description=profile[0],
        color=discord.Colour.blurple(),
    )
    embed.set_image(url=profile[1])
    await ctx.respond("Here you go:", embed=embed)

# Creates a slash command group for the convert commands

convert = bot.create_group("convert", "Convert numbers into other numbers")

# Convert base ten numbers to binary
@convert.command(name="to_binary", description="Convert base ten integers to binary")
async def dec_to_bin(ctx, decimal_number):
    await ctx.respond(numberconverter.convertDecimal(decimal_number))

# Convert binary numbers to base ten
@convert.command(name="to_base_ten", description="Convert binary numbers to base ten")
async def bin_to_dec(ctx, binary_number):
    await ctx.respond(numberconverter.convertBinary(binary_number))

bot.run(BOT_TOKEN)