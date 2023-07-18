import os
from os import system
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import requests
import json
#from keep_alive import keep_alive

#Access
intents = nextcord.Intents.default()
intents.members = True
client=nextcord.Client(intents=intents)



#IDS
main_server=327101420664913935
role_check="<Permissions value=-1>"


#Buttons
#Place discord_buttons code here#
name_quote={
  "Dimitri":"KILL DIMITRI",
  "Nifty":"ABSOLUTELY NUCLEAR",
  "Dan":"\U0001F474",
  "Celina":"\U0001F474",
  "Louise":"\U0001F474",
  "Adrian":"\U0001F604",
  "Lavin":"loves to smash!",
  "Kiki":"Do you love me? Are you riding? Say you'll never ever leave from beside me",
  "Cynthia":"is a great and merciful person!",
  "Charles":"would like you to pay Lavin and breathe air. In that order",
  "Yiming":"TypeError: 2D object existing in a 3D place",
  "Annie":"Are you okay?, Will you tell us that you're okay?",
  "Alex":"Loves the trunk!"
}
keys_tuple=tuple(list(name_quote.keys()))
name_tourney=["|Imbecile|","Nifty","Mzy",
"𝓥𝓪𝓵𝔂𝓷𝓭𝓻𝓪𝓲",
"Phiend",
"Chrysle",
"Hypha",
"Vida",
"NO NEED WHY BOTHER",
"Snopes",
"Nobeel ",
"Aphelium",
"kydrei",
"Riliane",
"apache",
"Raymond",
"raymond",
"macc",
"Kaii",
"SirStingy",
"SpinMan",
"KrackerJack",
"lieslieslies",
"૮ ・ﻌ・ა sammich",
"Nifty",
"snsdǝɔʇ",
"FumaK",
"Shachi",
"Coffee",
"Ahmed (Dameon)",
"bryant",
"martinren24",
"Adrius au Augustus",
"jisue",
"lKaida",
"adda",
"IoanBoy",
"Vi",
"incellord",
"Anthonious",
"Sybr",
"Caboose",
"Jango",
"Palagenie",
"ogopa",
"Cafer",
"Savrs",
"garbageman",
"Hakuiin",
"peregrine",
"Animated",
"M*",
"berbie",
"democratoide",
"tapioca flower",
"Luke Klassen",
"JJJJ",
"Sosa",
"General Miles",
"yeee",
"1412",
"Sybr",
"soruo",
"IsoLatioN",
"Rush",
"Mistaek",
"sahand",
"p1geon",
"Krozoid",
"lesbo",
"Zed",
"LITERALLY H",
"Lewdi",
"Upom",
"Skyy",
"FumaK",
"AOC T3 SUB",
"Mehseenbetter",
"Snowby624",
"hip",
"Tsuki",
"yeee ",
"ShieldLoL",
"Im ExeCUTE",
"JackPot",
"stevooooo",
"Dolt",
"Nick17",
"=)",
"young rich jugga",
"keruru",
"Wolf",
"EvenAndOdd",
"Willy",
"ahusalmon",
"fivetarlted",
"MacSnitch",
"Omishio",
"General Miles ",
"Primal96",
"Sluggy",
"Janet",
"Wilson",
"spagh_eddy",
"Prish480",
"kelllyyy",
"Ririka",
"appl3",
"sk",
"᲼᲼᲼",
"Sea Dragon",
"iciclearms",
"vrag",
]


def get_quote(member):
  response=requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote=json_data[0]["q"]+"-"+json_data[0]["a"]
  
  
  
  return(quote)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
    return

  if (message.content.startswith(keys_tuple)) and (message.guild.id != main_server):
    await message.channel.send(name_quote[message.content.split()[0]])
  if message.content.startswith("!sigmagrindset"):
    member = nextcord.utils.get(message.guild.members)
    quote = get_quote(member)
    
    await message.channel.send(quote)
  if message.content.startswith("!event_roles"):
    
    #member = nextcord.utils.get(message.guild.members)
    role=nextcord.utils.get(message.guild.roles, name="LOL Summer Showdown Participant")
    #s=[]
    for x in name_tourney:
      #user_id=message.guild.get_member_named(x)
      user_id=nextcord.utils.get(message.guild.members, name=x)
      if user_id != None:
        user_id2=user_id.id
        assign=message.guild.get_member(user_id2)
        await message.channel.send("Assigned role to: "+x)
        #s.append(assign.name+"#"+str(assign.discriminator))
        await assign.add_roles(role)
      
        
    await message.channel.send("Roles Assigned")
    
    
  if (message.content.startswith("!roles")) and (message.guild.id == main_server) and (role_check==str(message.author.guild_permissions)):
    embedVar = nextcord.Embed(title="General Roles", description="<:MEL:751634095674490901> = Guest\n<:controller:751634116004413460> = Game Nights\n<:blueheart:751634126490042509> = Tournament", color=0x33B2FF)
    await message.channel.send(embed=embedVar)
    embedVar2= nextcord.Embed(title="Specialty Roles", description="<:antoneko:751634139446378576> = Meet ups\n<:twitch:751634157741801493> = Streamer\n<:disgustedtanjiro:751634174242324503> = Anime\n<:fingerheart:751634189085835334> = K-Pop\n🏅 = Sports",color=0x33B2FF)
    await message.channel.send(embed=embedVar2)
    embedVar3= nextcord.Embed(title="Casual Games", description="<:jackbox:751634221151289344> = Jackbox\n<:skribblio:751634240680100011> = Skribbl.io\n<:fallguys:751634254407925770> = Fall Guys\n<:amongus:751634273517174864> = Among Us\n<:tabletop:751634289702994021> = Tabletop Simulator",color=0x33B2FF)
    await message.channel.send(embed=embedVar3)
    embedVar4= nextcord.Embed(title="FPS", description="<:rainbowsix:751634850884354068> = Rainbow Six Siege\n<:callofduty:751634864112926751> = Call of Duty\n<:valorant:751634923726831636> = Valorant\n<:csgo:751634933390377050> = CSGO\n<:overwatch:751634886250725427> = Overwatch\n<:fortnite:751634896560193637> = Fortnite",color=0x33B2FF)
    await message.channel.send(embed=embedVar4)
    embedVar5= nextcord.Embed(title="Strategy and MOBAs", description="<:pengu:751634955330912276> = Teamfight Tactics\n<:leagueoflegends:751635117021331487> = League of Legends\n<:runeterra:751635027972063243> = Legends of Runeterra\n<:dota:751635137480884265> = DOTA",color=0x33B2FF)
    await message.channel.send(embed=embedVar5)
    embedVar6= nextcord.Embed(title="Creative", description="<:minecraft:751635153364713542> = Minecraft\n<:roblox:751635163510997014> = Roblox",color=0x33B2FF)
    await message.channel.send(embed=embedVar6)
    embedVar7= nextcord.Embed(title="Nintendo", description="<:powerup:751635279991013496> = Nintendo\n<:pokeball:751635300555685929> = Pokemon\n<:smash:751635323297071165> = Smash",color=0x33B2FF)
    await message.channel.send(embed=embedVar7)
    embedVar8= nextcord.Embed(title="MMOs", description="<:maplestory:751635176706015333> = MapleStory\n<:worldofwarcraft:751635261569499236> = World of Warcraft\n<:genshin:762484433654644768> = Genshin Impact",color=0x33B2FF)
    await message.channel.send(embed=embedVar8)
    embedVar9= nextcord.Embed(title="Others", description="<:rate_up_is_a_lie:751635358411653200> = Gacha\n<:futaba:751635369384083507> = JRPG",color=0x33B2FF)
    await message.channel.send(embed=embedVar9)



@client.event
async def on_member_join(member):
    role=nextcord.utils.get(member.guild.roles, name="LOL Summer Showdown Participant")
    if member.name in name_tourney:  
        await member.add_roles(role)  
    else:  
        return  
@client.event
async def on_raw_reaction_add(payload):
  general_id=977401408414425148
  specialty_id=977401417545429012
  casual_id=977401418879234058
  fps_id=977401420233981963
  strat_id=977401421148348467
  creative_id=977401430648430592
  nintendo_id=977401431906713680
  mmo_id=977401433513160744
  others_id=977401434784010340
  
  if (payload.message_id==general_id):
    member=payload.member
    guild=member.guild

    emoji=payload.emoji.name
    
    if emoji=="MEL":
      role=nextcord.utils.get(guild.roles, name="Guest")
    elif emoji=="controller":
      role=nextcord.utils.get(guild.roles, name="Game Nights")
    elif emoji=="blueheart":
      role=nextcord.utils.get(guild.roles, name="Tournaments")
    else:
      print (emoji)
  
  if (payload.message_id==specialty_id):
    member=payload.member
    guild=member.guild

    emoji=payload.emoji.name
    
    if emoji=="antoneko":
      role=nextcord.utils.get(guild.roles, name="Meet Ups")

    elif emoji=="twitch":
      role=nextcord.utils.get(guild.roles, name="Streamer")
    elif emoji=="disgustedtanjiro":
      role=nextcord.utils.get(guild.roles, name="Anime")
    elif emoji=="fingerheart":
      role=nextcord.utils.get(guild.roles, name="K-Pop")
    elif emoji=="🏅":
      role=nextcord.utils.get(guild.roles, name="Sports")
    else:
      print (emoji)

  if (payload.message_id==casual_id):
    member=payload.member
    guild=member.guild

    emoji=payload.emoji.name
    
    if emoji=="jackbox":
      role=nextcord.utils.get(guild.roles, name="Jackbox")
    elif emoji=="skribblio":
      role=nextcord.utils.get(guild.roles, name="Skribbl.io")
    elif emoji=="fallguys":
      role=nextcord.utils.get(guild.roles, name="Fall Guys")
    elif emoji=="amongus":
      role=nextcord.utils.get(guild.roles, name="Among Us")
    elif emoji=="tabletop":
      role=nextcord.utils.get(guild.roles, name="Tabletop Simulator")
    else:
      print (emoji)

  if (payload.message_id==fps_id):
    member=payload.member
    guild=member.guild

    emoji=payload.emoji.name
    
    if emoji=="rainbowsix":
      role=nextcord.utils.get(guild.roles, name="Rainbow Six Siege")
    elif emoji=="callofduty":
      role=nextcord.utils.get(guild.roles, name="Call of Duty")
    elif emoji=="valorant":
      role=nextcord.utils.get(guild.roles, name="Valorant")
    elif emoji=="csgo":
      role=nextcord.utils.get(guild.roles, name="CSGO")
    elif emoji=="overwatch":
      role=nextcord.utils.get(guild.roles, name="Overwatch")
    elif emoji=="fortnite":
      role=nextcord.utils.get(guild.roles, name="Fortnite")
    else:
      print (emoji)

  if (payload.message_id==strat_id):
    member=payload.member
    guild=member.guild

    emoji=payload.emoji.name
    
    if emoji=="pengu":
      role=nextcord.utils.get(guild.roles, name="Teamfight Tactics")
    elif emoji=="leagueoflegends":
      role=nextcord.utils.get(guild.roles, name="League of Legends")
    elif emoji=="runeterra":
      role=nextcord.utils.get(guild.roles, name="Legends of Runeterra")
    elif emoji=="dota":
      role=nextcord.utils.get(guild.roles, name="DOTA")
    else:
      print (emoji) 
  
  if (payload.message_id==creative_id):
    member=payload.member
    guild=member.guild

    emoji=payload.emoji.name
    
    if emoji=="minecraft":
      role=nextcord.utils.get(guild.roles, name="Minecraft")
    elif emoji=="roblox":
      role=nextcord.utils.get(guild.roles, name="Roblox")
    else:
      print (emoji)
  
  if (payload.message_id==nintendo_id):
    member=payload.member
    guild=member.guild

    emoji=payload.emoji.name
    
    if emoji=="powerup":
      role=nextcord.utils.get(guild.roles, name="Nintendo")
    elif emoji=="pokeball":
      role=nextcord.utils.get(guild.roles, name="Pokémon")
    elif emoji=="smash":
      role=nextcord.utils.get(guild.roles, name="Smash")
    else:
      print (emoji)

  if (payload.message_id==mmo_id):
    member=payload.member
    guild=member.guild

    emoji=payload.emoji.name
    
    if emoji=="maplestory":
      role=nextcord.utils.get(guild.roles, name="MapleStory")
    elif emoji=="worldofwarcraft":
      role=nextcord.utils.get(guild.roles, name="World of Warcraft")
    elif emoji=="genshin":
      role=nextcord.utils.get(guild.roles, name="Genshin Impact")
    else:
      print (emoji)

  if (payload.message_id==others_id):
    member=payload.member
    guild=member.guild

    emoji=payload.emoji.name
    
    if emoji=="rate_up_is_a_lie":
      role=nextcord.utils.get(guild.roles, name="Gacha")
    elif emoji=="futaba":
      role=nextcord.utils.get(guild.roles, name="JRPG")
    else:
      print (emoji)
  await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
  general_id=977401408414425148
  specialty_id=977401417545429012
  casual_id=977401418879234058
  fps_id=977401420233981963
  strat_id=977401421148348467
  creative_id=977401430648430592
  nintendo_id=977401431906713680
  mmo_id=977401433513160744
  others_id=977401434784010340
 
  if (payload.message_id==general_id):
    guild=await(client.fetch_guild(payload.guild_id))

    emoji=payload.emoji.name
    
    if emoji=="MEL":
      role=nextcord.utils.get(guild.roles, name="Guest")
    elif emoji=="controller":
      role=nextcord.utils.get(guild.roles, name="Game Nights")
    elif emoji=="blueheart":
      role=nextcord.utils.get(guild.roles, name="Tournaments")
    else:
      print (emoji)
    member=await(guild.fetch_member(payload.user_id))
  if (payload.message_id==specialty_id):
    guild=await(client.fetch_guild(payload.guild_id))

    emoji=payload.emoji.name
    
    if emoji=="antoneko":
      role=nextcord.utils.get(guild.roles, name="Meet Ups")
      
    elif emoji=="twitch":
      role=nextcord.utils.get(guild.roles, name="Streamer")
    elif emoji=="disgustedtanjiro":
      role=nextcord.utils.get(guild.roles, name="Anime")
    elif emoji=="fingerheart":
      role=nextcord.utils.get(guild.roles, name="K-Pop")
    elif emoji=="🏅":
      role=nextcord.utils.get(guild.roles, name="Sports")
    else:
      print (emoji)
    member=await(guild.fetch_member(payload.user_id))
  if (payload.message_id==casual_id):
    guild=await(client.fetch_guild(payload.guild_id))

    emoji=payload.emoji.name
    
    if emoji=="jackbox":
      role=nextcord.utils.get(guild.roles, name="Jackbox")
    elif emoji=="skribblio":
      role=nextcord.utils.get(guild.roles, name="Skribbl.io")
    elif emoji=="fallguys":
      role=nextcord.utils.get(guild.roles, name="Fall Guys")
    elif emoji=="amongus":
      role=nextcord.utils.get(guild.roles, name="Among Us")
    elif emoji=="tabletop":
      role=nextcord.utils.get(guild.roles, name="Tabletop Simulator")
    else:
      print (emoji)
    member=await(guild.fetch_member(payload.user_id))
  if (payload.message_id==fps_id):
    guild=await(client.fetch_guild(payload.guild_id))

    emoji=payload.emoji.name
    
    if emoji=="rainbowsix":
      role=nextcord.utils.get(guild.roles, name="Rainbow Six Siege")
    elif emoji=="callofduty":
      role=nextcord.utils.get(guild.roles, name="Call of Duty")
    elif emoji=="valorant":
      role=nextcord.utils.get(guild.roles, name="Valorant")
    elif emoji=="csgo":
      role=nextcord.utils.get(guild.roles, name="CSGO")
    elif emoji=="overwatch":
      role=nextcord.utils.get(guild.roles, name="Overwatch")
    elif emoji=="fortnite":
      role=nextcord.utils.get(guild.roles, name="Fortnite")
    else:
      print (emoji)
    member=await(guild.fetch_member(payload.user_id))
  if (payload.message_id==strat_id):
    guild=await(client.fetch_guild(payload.guild_id))

    emoji=payload.emoji.name
    
    if emoji=="pengu":
      role=nextcord.utils.get(guild.roles, name="Teamfight Tactics")
    elif emoji=="leagueoflegends":
      role=nextcord.utils.get(guild.roles, name="League of Legends")
    elif emoji=="runeterra":
      role=nextcord.utils.get(guild.roles, name="Legends of Runeterra")
    elif emoji=="dota":
      role=nextcord.utils.get(guild.roles, name="DOTA")
    else:
      print (emoji) 
    member=await(guild.fetch_member(payload.user_id))
  if (payload.message_id==creative_id):
    guild=await(client.fetch_guild(payload.guild_id))

    emoji=payload.emoji.name
    
    if emoji=="minecraft":
      role=nextcord.utils.get(guild.roles, name="Minecraft")
    elif emoji=="roblox":
      role=nextcord.utils.get(guild.roles, name="Roblox")
    else:
      print (emoji)
    member=await(guild.fetch_member(payload.user_id))
  if (payload.message_id==nintendo_id):
    guild=await(client.fetch_guild(payload.guild_id))

    emoji=payload.emoji.name
    
    if emoji=="powerup":
      role=nextcord.utils.get(guild.roles, name="Nintendo")
    elif emoji=="pokeball":
      role=nextcord.utils.get(guild.roles, name="Pokémon")
    elif emoji=="smash":
      role=nextcord.utils.get(guild.roles, name="Smash")
    else:
      print (emoji)
    member=await(guild.fetch_member(payload.user_id))
  if (payload.message_id==mmo_id):
    guild=await(client.fetch_guild(payload.guild_id))

    emoji=payload.emoji.name
    
    if emoji=="maplestory":
      role=nextcord.utils.get(guild.roles, name="MapleStory")
    elif emoji=="worldofwarcraft":
      role=nextcord.utils.get(guild.roles, name="World of Warcraft")
    elif emoji=="genshin":
      role=nextcord.utils.get(guild.roles, name="Genshin Impact")
    else:
      print (emoji)
    member=await(guild.fetch_member(payload.user_id))
  if (payload.message_id==others_id):
    guild=await(client.fetch_guild(payload.guild_id))

    emoji=payload.emoji.name
    
    if emoji=="rate_up_is_a_lie":
      role=nextcord.utils.get(guild.roles, name="Gacha")
    elif emoji=="futaba":
      role=nextcord.utils.get(guild.roles, name="JRPG")
    else:
      print (emoji)
    member=await(guild.fetch_member(payload.user_id))
  
  
  

  await member.remove_roles(role)
  

#async def on_member_join(member): 
#	if (member.name) in name_tourney:
#		role=nextcord.utils.get(member.server.roles, name="LOL Summer Showdown Participant")
#	await client.add_roles(member, role)

#keep_alive()
client.run(my_secret)
