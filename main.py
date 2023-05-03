import interactions
import os
import responses as rs
from uptime import keep_alive

bot = interactions.Client(token=os.environ['TOKEN'])
servers_id = [828417721745014784, 1092836175405928478]
player_enumerate12 = [
        interactions.Option(
            name="players",
            description=
            "Delimit the players name with a simple space [min=6, max=12]",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
player_enumerate18 = [
        interactions.Option(
            name="players",
            description=
            "Delimit the players name with a simple space [min=6, max=18]",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]

async def is_legit(ctx: interactions.CommandContext):
    return ctx.channel.id == 1098683625622470796 or ctx.channel.id == 1098827341515464765

async def isnt_legit_message(ctx: interactions.CommandContext):
  guildid = ctx.guild_id 
  if guildid == 828417721745014784:
    await ctx.send(f"You must execute the command in <#1098827341515464765>", ephemeral = True) 
  if guildid == 1092836175405928478:
    await ctx.send(f"You must execute the command in <#1098683625622470796>", ephemeral = True)

async def displayResponse(ctx: interactions.CommandContext, players: str, mode : str):
  if mode == "tdm":
    rsp_fct = rs.tdm
  elif mode == "ctl":
    rsp_fct = rs.ctl
  elif mode == "gr":
    rsp_fct = rs.gr
  if await is_legit(ctx):
    playerslist = players.split()
    await ctx.send(rsp_fct(playerslist))
  else :
    await isnt_legit_message(ctx)
    
# Discord slash command /team_death_match
@bot.command(
    name="team_death_match",
    description="Shuffle It!",
    scope=servers_id,
    options=player_enumerate12,
)
async def team_death_match(ctx: interactions.CommandContext, players: str):
  await displayResponse(ctx, players, "tdm")

# Discord slash command /control
@bot.command(
    name="control",
    description="Shuffle It!",
    scope=servers_id,
    options=player_enumerate18,
)
async def control(ctx: interactions.CommandContext, players: str):
  await displayResponse(ctx, players, "ctl")
 
# Discord slash command /gun_run
@bot.command(
    name="gun_run",
    description="Shuffle It!",
    scope=servers_id,
    options=player_enumerate12,
)
async def gun_run(ctx: interactions.CommandContext, players: str):
  await displayResponse(ctx, players, "gr")

# Discord slash command /help
@bot.command(
    name="help",
    description="Help",
    scope=servers_id,
)
async def help(ctx):
    if await is_legit(ctx):
      await ctx.send(rs.help(), ephemeral=True)
    else:
      await isnt_legit_message(ctx) 

keep_alive()
bot.start()
