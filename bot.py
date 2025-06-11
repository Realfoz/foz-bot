from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.ui import View, Button
from discord import Embed, Interaction, ButtonStyle
from skullclamp import get_card_price
import os
from jumpstart import generate_decks, format_deck
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
        await channel.send("WallCat is now online! :cat: ") # confirmation in discord channel
    else:
        print("⚠️ Channel not found. Check the channel ID.") # need a test case to make sure this works


@bot.command()
async def test(ctx, *, arg): # basic echo test
    await ctx.send(arg)

@bot.command()
async def skullclamp(ctx):
    price_msg = get_card_price("skullclamp")
    await ctx.send(f"{price_msg} :skullclamp:")


@bot.command()
async def jumpstart(ctx):
    player1 = Player(ctx.author)
    player2 = None

    embed = Embed(
        title=f"{player1.name} wants to play jumpstart!",
        description="Click the button below to play as player 2!",
        color=0x1abc9c  # look into colour options, maybe do all 5 magic colors somehow?
    )

    button = Button(label="Join Game As Player 2", style=ButtonStyle.green)

    async def button_callback(interaction: Interaction):
        nonlocal player2  # let us reassign the outer variable
        if player2 is None:
            player2 = Player(interaction.user)
            generate_decks(player1)
            generate_decks(player2) #as its here after the player2 selection now it will kick off deck creation for each player
            

            await interaction.response.send_message(
                "You're Player 2!, sending decks!", # player 2 confirmation message
                ephemeral=True
            )

            await send_dm_or_fallback(interaction, player1) # calls the deck send function for each player
            await send_dm_or_fallback(interaction, player2)



           
        elif interaction.user == player1.user:
            await interaction.response.send_message(
                "You absolute chucklefuck. You know you're player 1 but you just had to press the button didn't you...",
                ephemeral=True
            )
        else:
            await interaction.response.send_message(
                "Sorry! Player 2 has already been selected :( ",
                ephemeral=True
            )

    button.callback = button_callback

    view = View()
    view.add_item(button)

    await ctx.send(embed=embed, view=view)


async def send_dm_or_fallback(interaction, player):
    try:
        await player.user.send(f"**Your deck:**\n```{player.full_deck}```")
    except discord.Forbidden:
        # DM failed, fallback to button they can push to be sent the deck as an ephemeral post
        view = View()

        async def resend_callback(resend_interaction):
            await resend_interaction.response.send_message(
                f"**Your deck:**\n```{player.full_deck}```",
                ephemeral=True
            )

        button = Button(label="Show My Deck", style=discord.ButtonStyle.primary)
        button.callback = resend_callback
        view.add_item(button)

        await interaction.followup.send(
            "Couldn't DM you. Click below to see your deck privately.",
            view=view,
            ephemeral=True
        )

async def run_bot():
    await bot.start(token)
 


