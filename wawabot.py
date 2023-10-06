from discord.ext import commands
import discord
import os
from dicecommand import diceroll
import numberconverter
import dotenv
import wawaresources
import datetime

# LINK FOR INVITES: https://discord.com/api/oauth2/authorize?client_id=1152464515905114192&permissions=8&scope=bot%20applications.commands

dotenv.load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
DEBUG_CHANNEL = 1152659130058817548
KENZIE_CHANNEL = 1125824297974366240

bot = commands.Bot()


@bot.event
async def on_ready():
    print("Successfully connected.")
    channel = bot.get_channel(DEBUG_CHANNEL)
    await channel.send("alo im awake")


#  =============== Slash Commands ===============

@bot.slash_command(name="bark", description="woof..")
async def bark(ctx):
    await ctx.respond("WOOF")

@bot.slash_command(name="dice", description="Rolls a 6 sided die.")
async def dice(ctx):
    await ctx.respond(f"```{diceroll()}```")

@bot.slash_command(name="routine", description="Mol's workout routine")
async def routine(ctx):
    await ctx.respond(wawaresources.workoutroutine())

@bot.slash_command(name="modulo", description="Finds the modulus of two integers.")
async def modulus(ctx, number_x: int, number_y: int):
    modulus = number_x % number_y
    await ctx.respond(f"{number_x} % {number_y} = {modulus}")


convert = bot.create_group("convert", "Convert numbers into other numbers")

# Convert base ten numbers to binary
@convert.command(name="to_binary", description="Convert base ten integers to binary")
async def dec_to_bin(ctx, decimal_number):
    await ctx.respond(numberconverter.convertDecimal(decimal_number))

@convert.command(name="to_base_ten", description="Convert binary numbers to base ten")
async def bin_to_dec(ctx, binary_number):
    await ctx.respond(numberconverter.convertBinary(binary_number))

bot.run(BOT_TOKEN)

