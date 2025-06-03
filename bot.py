from dotenv import load_dotenv
import discord
from discord.ext import commands
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
channel_id = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()  # basic intents, might customise later
bot = commands.Bot(command_prefix='!', intents=intents)
intents.message_content = True

@bot.event
async def on_ready():

    print("Hello World! Bot is ready and connected.") # confirmation in terminal
    
     
    channel = bot.get_channel(channel_id)

    if channel:
        await channel.send("Foz-Bot is now online! 🤖")
    else:
        print("⚠️ Channel not found. Check the channel ID.")

@bot.command()
async def test(ctx, *, arg): # basic echo test
    await ctx.send(arg)


def run_bot():
    bot.run(token)
    ctx.send("Foz-Bot is now online")


if __name__ == "__main__":
    run_bot()

