from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
from jumpstart import JumpstartCog

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
channel_id = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()  # basic intents, might customise later to clean up scope
intents.message_content = True # toggles the bots ability to look in chat
bot = commands.Bot(command_prefix='!', intents=intents) # sets the modifier the bots looking for


@bot.event # functions the bot runs regardless of commands, think daemon
async def on_ready(): # does this everytime the bot is loaded

    print("Hello World! Bot is ready and connected.") # confirmation in terminal
    
     
    channel = bot.get_channel(channel_id)

    if channel:
        await channel.send("Foz-Bot is now online! 🤖") # confirmation in discord channel
    else:
        print("⚠️ Channel not found. Check the channel ID.") # need a test case to make sure this works


@bot.command()
async def test(ctx, *, arg): # basic echo test
    await ctx.send(arg)


async def run_bot():
    await bot.add_cog(JumpstartCog(bot))
    await bot.start(token)
 


