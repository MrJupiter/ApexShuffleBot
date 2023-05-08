import random

def shuffleIt(list, num_teams):
  random.shuffle(list)
  teams = [[] for i in range(num_teams)]
  for i, player in enumerate(list):
    teams[i % num_teams].append(player)
  ts = ""
  for i, team in enumerate(teams):
    ts = ts + f"\n**Team {str(i+1)} : **\n`{', '.join(team)}`"
  return ts

def gr(list):
  players_count = len(list)
  if players_count < 13 and players_count > 5:
    num_teams = 4
    return shuffleIt(list, num_teams)
  else: 
    return "You must select at least 6 players and max 12 players"
    
def tdm(list):
  players_count = len(list)
  if players_count < 13 and players_count > 5:
    num_teams = 2
    return shuffleIt(list, num_teams)
  else: 
    return "You must select at least 6 players and max 12 players"

def ctl(list):
  players_count = len(list)
  if players_count < 19 and players_count > 5:
    num_teams = 2
    return shuffleIt(list, num_teams)
  else: 
    return "You must select at least 6 players and max 18 players"

def help():
  return "\n__ꜱʜᴜꜰꜰʟᴇ ꜰᴏʀ ᴛᴇᴀᴍ ᴅᴇᴀᴛʜ ᴍᴀᴛᴄʜ:__\n> /team_death_match ᴘʟᴀʏᴇʀ1 ᴘʟᴀʏᴇʀ2 ... ᴘʟᴀʏᴇʀ12 \n__ꜱʜᴜꜰꜰʟᴇ ꜰᴏʀ ᴄᴏɴᴛʀᴏʟ:__\n> /control ᴘʟᴀʏᴇʀ1 ᴘʟᴀʏᴇʀ2 ... ᴘʟᴀʏᴇʀ18 \n__ꜱʜᴜꜰꜰʟᴇ ꜰᴏʀ ɢᴜɴ ʀᴜɴ:__\n> /gun_run ᴘʟᴀʏᴇʀ1 ᴘʟᴀʏᴇʀ2 ... ᴘʟᴀʏᴇʀ12 \n__ᴛᴏ ᴘᴜʀɢᴇ ᴄʜᴀɴɴᴇʟ:__\n> /purge_channel \n__ᴛᴏ ʟɪꜱᴛ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅꜱ:__\n> /help"
