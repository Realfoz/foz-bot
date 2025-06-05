from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.ui import View, Button
from discord import Embed, Interaction, ButtonStyle
import os
from jumpstart import generate_decks
from player import Player


load_dotenv()
token = os.getenv("DISCORD_TOKEN") # gets the stored bot token
channel_id = int(os.getenv("CHANNEL_ID")) # gets the stored channel id

intents = discord.Intents.default()  # basic intents, might customise later to clean up scope
intents.message_content = True # toggles the bots ability to look in chat
bot = commands.Bot(command_prefix='!', intents=intents) # sets the modifier the bots looking for to "!"


@bot.event # functions the bot runs regardless of commands
async def on_ready(): # does this everytime the bot is loaded

    print("Hello World! Bot is ready and connected.") # confirmation in terminal
    
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send("WallCat is now online! 🤖") # confirmation in discord channel
    else:
        print("⚠️ Channel not found. Check the channel ID.") # need a test case to make sure this works


@bot.command()
async def test(ctx, *, arg): # basic echo test
    await ctx.send(arg)


@bot.command()
async def jumpstart(ctx): # the !jumpstart command that begins the player selection and deck selection process
    player1 = Player(ctx.author) # creates player object and set the user as the player field
    player2 = {'player': None}

    embed = Embed(
        title=f"{player1.name} wants to play jumpstart!", # this is the box that pops in chat
        description="Click the button below to play!",
        color=0x00ff00 # change this to a better colour, please god
    )

    button = Button(label="Click me!", style=ButtonStyle.green) # check for other color options

    async def button_callback(interaction: Interaction):
        if player2['player'] is None:
            if interaction.user == player1.user:
                await interaction.response.send_message(
                    "You absolute chucklefuck. You know you're player 1 but you just had to press the button didn't you...", 
                    # they know what they did. We all know this has to be here
                    ephemeral=True
                )
                return

            player2['player'] = Player(interaction.user) # creation of player2 object with user name
            deck1_codes, deck2_codes = generate_decks() #begins the deck creation from jumpstart.py 

            player1.deck_types = deck1_codes
            player2['player'].deck_types = deck2_codes

        elif interaction.user == player1.user:
            await interaction.response.send_message(
                "You absolute chucklefuck. You know you're player 1 but you just had to press the button didn't you...",
                ephemeral=True
            )
        else:
            await interaction.response.send_message(
                "Sorry! Player 2 has already been selected :( ", ephemeral=True
            )

    button.callback = button_callback

    view = View()
    view.add_item(button)

    await ctx.send(embed=embed, view=view)

async def run_bot():
    await bot.start(token)
 


