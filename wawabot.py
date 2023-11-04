from discord.ext import commands
import discord
from discord.commands import Option
import os
import dotenv
import datetime
import asyncio

from commands import dicecommand, github, numberconverter, wawaresources

dotenv.load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
DEBUG_CHANNEL = int(os.getenv('DEBUG_CHANNEL'))

bot = commands.Bot()
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Successfully connected.")
    channel = bot.get_channel(DEBUG_CHANNEL)
    await channel.send("alo im awake")

#this thing not working lol
# @bot.event
# async def on_message(message):
#     print(message.content)
#     if "love" in message.content and "wawa" in message.content:
#         await message.channel.send("i love you too :D")

#  =============== Slash Commands ===============

# Miscellaneous commands for testing the functionality of Discord's API and the bot 
@bot.slash_command(name="bark", description="woof..")
async def bark(ctx):
    await ctx.respond("WOOF")

@bot.slash_command(name="love", description="Tell wawa you love him...")
async def love(ctx):
    await ctx.respond(f"I love you too <@!{ctx.author.id}> :3")

@bot.slash_command(name="dice", description="Rolls a 6 sided die.")
async def dice(ctx):
    await ctx.respond(f"```{dicecommand.diceroll()}```")

@bot.slash_command(name="routine", description="Mol's routine")
async def routine(ctx):
    # If you want this command to only work with your account, you can replace my user ID :] or you can remove this if statement
    if ctx.author.id == 702643363685466163:
        await ctx.respond(wawaresources.dailyroutine())
    else:
        await ctx.respond("You are not authorized to use this command. gooba...")

@bot.slash_command(name="meditate", description="Sets a timer for meditation :)")
async def meditate(ctx, custom_time: Option(int, "Choose a time in minutes", required = False, default = 8)):
    await ctx.respond(f"I've set a timer for {custom_time} minutes.")
    await asyncio.sleep(custom_time * 60)
    await ctx.send(f"<@!{ctx.author.id}> Time is up!")

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