import discord
from discord import app_commands
from discord.ext import commands
import os
import responses as rs
from uptime import keep_alive

#LEGIT_IDS = {server_id1:command_channel_id2, server_id1:command_channel_id2}
LEGIT_IDS  = {828417721745014784:1098827341515464765, 1092836175405928478:1098683625622470796}

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
  print(f"The bot started in {len(bot.guilds)} servers")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)
      
#Creating an app_commands.check
class NotLegitServer(app_commands.CheckFailure):
  pass
def legit_guilds():
  async def predicate(ctx):
    if ctx.guild_id not in list(LEGIT_IDS.keys()):
      raise NotLegitServer("Sorry to tell that you need to be in the legit servers' list to use this bot... Please, contact <@583461272046141585> to add your discord server in the legit list")
    return True
  return app_commands.check(predicate)

def legit_channels():
  async def predicate(ctx):
    if ctx.channel_id not in list(LEGIT_IDS.values()):
      raise NotLegitServer(f"Execute your command in <#{LEGIT_IDS.get(ctx.guild_id)}>")
    return True
  return app_commands.check(predicate)
    
@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError) -> None:
  await interaction.response.send_message(str(error), ephemeral=True)

async def displayResponse(ctx: discord.Interaction, players: str, mode : str):
  if mode == "tdm":
    rsp_fct = rs.tdm
  elif mode == "ctl":
    rsp_fct = rs.ctl
  elif mode == "gr":
    rsp_fct = rs.gr
  playerslist = players.split()
  await ctx.response.send_message(rsp_fct(playerslist))

    
# Discord slash command /team_death_match
@bot.tree.command(name="team_death_match", description = "Shuffle It!")
@app_commands.describe(players = "Delimit the players name with a simple space [min=6, max=12]")
@legit_channels()
@legit_guilds()
async def team_death_match(ctx: discord.Interaction, players: str):
  await displayResponse(ctx, players, "tdm")

# Discord slash command /control
@bot.tree.command(name="control", description = "Shuffle It!")
@app_commands.describe(players = "Delimit the players name with a simple space [min=6, max=18]")
@legit_channels()
@legit_guilds()
async def control(ctx: discord.Interaction, players: str):
  await displayResponse(ctx, players, "ctl")
 
# Discord slash command /gun_run
@bot.tree.command(name="gun_run", description = "Shuffle It!")
@app_commands.describe(players = "Delimit the players name with a simple space [min=6, max=12]")
@legit_channels()
@legit_guilds()
async def gun_run(ctx: discord.Interaction, players: str):
  await displayResponse(ctx, players, "gr")

# Discord slash command /help
@bot.tree.command(name="help", description = "The help command")
@legit_channels()
@legit_guilds()
async def help(ctx: discord.Interaction):
  await ctx.response.send_message(rs.help(), ephemeral=True)

keep_alive()
bot.run(os.environ['TOKEN'])
