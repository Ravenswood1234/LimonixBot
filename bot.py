#imports
from discord.ext import commands, tasks
from itertools import cycle 
from datetime import datetime
from pymongo import MongoClient
import datetime
import io
import discord
import os
import traceback
cluster = MongoClient("mongodb+srv://limonix:1q234567wE@cluster0.tthbn.mongodb.net/lim?retryWrites=true&w=majority")
collection = cluster.lim.post
prefix = MongoClient("mongodb+srv://limonix:1q234567wE@cluster0.tthbn.mongodb.net/Guild?retryWrites=true&w=majority")
prefixes = prefix.Guild.prefixes
users = MongoClient("mongodb+srv://limonix:1q234567wE@cluster0.tthbn.mongodb.net/member?retryWrites=true&w=majority")
userinfo = users.member.information


stats = cycle(['!help', 'https://discord.gg/YkA5ft9'])
def get_prefix_gg(client, message):
	prefix_server = prefixes.find_one({"_guild_id": message.guild.id})["prefix"]
	return str(prefix_server)



client = commands.Bot(command_prefix = get_prefix_gg, intents = discord.Intents.all())   
client.remove_command("help")
@client.event
async def on_ready():
	for guild in client.guilds:
		post = {
			"_guild_id": guild.id,
			"prefix": "!",
			"welcome": 0
		}
		if prefixes.count_documents({"guild_id": guild.id}) == 0:
			prefixes.insert_one(post)
		for member in guild.members:

			user={
				'id':member.id,
				'guild_id':guild.id,
				'cash':0,
				'rep':0,
				'limoncoin':0,
				'xp':0,
				'lvl':0,
				'nummessage':0
			}
			member = {
				'id':member.id,
				'info': f'Расскажите о себе {get_prefix_gg}осебе',
				'second_half': 'Нету'
				}
			if collection.count_documents({'id':member.id, "guild_id":guild.id})==0:
				collection.insert_one(user)
			if userinfo.count_documents({'id':member.id})==0:
				userinfo.insert_one(member)
			
	print("Bot connected to the server")
	change_stats.start()
@tasks.loop(seconds = 10)
async def change_stats():
	await client.change_presence( status = discord.Status.do_not_disturb, activity = discord.Game(name = next(stats)))
@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send(embed=discord.Embed(
			title=':x:Ошибка',
			description=f"""Недостаточно прав для использования команды!""", 
			colour=discord.Color.red()),
			delete_after=10
			)
@client.event
async def on_voice_state_update(member, before, after):
	guild = member.guild
	if after.channel.id == 784086781342515260:
		
		mainCategory = discord.utils.get(guild.categories, id=784086661335744552)
		channel2 = await guild.create_voice_channel(name=f"{member}",category=mainCategory)
		await member.move_to(channel2)
		await channel2.set_permissions(member,mute_members=True,move_members=True,manage_channels=True)
		def check(a,b,c):
			return len(channel2.members) == 0
		await client.wait_for('voice_state_update', check=check)
		await channel2.delete()
	if after.channel.id == 784355319022223412:
		
		mainCategory = discord.utils.get(guild.categories, id=769093361533190164)
		channel2 = await guild.create_voice_channel(name=f"⛏║{member}",category=mainCategory)
		await member.move_to(channel2)
		await channel2.set_permissions(member,mute_members=True,move_members=True,manage_channels=True)
		def check(a,b,c):
			return len(channel2.members) == 0
		await client.wait_for('voice_state_update', check=check)
		await channel2.delete()
	if after.channel.id == 784355652600463360:
		
		mainCategory = discord.utils.get(guild.categories, id=769081221539037205)
		channel2 = await guild.create_voice_channel(name=f"🔮║{member}",category=mainCategory)
		await member.move_to(channel2)
		await channel2.set_permissions(member,mute_members=True,move_members=True,manage_channels=True)
		def check(a,b,c):
			return len(channel2.members) == 0
		await client.wait_for('voice_state_update', check=check)
		await channel2.delete()
	if after.channel.id == 784355798419636284:
		
		mainCategory = discord.utils.get(guild.categories, id=768864090759233547)
		channel2 = await guild.create_voice_channel(name=f"🔪║{member}",category=mainCategory)
		await member.move_to(channel2)
		await channel2.set_permissions(member,mute_members=True,move_members=True,manage_channels=True)
		def check(a,b,c):
			return len(channel2.members) == 0
		await client.wait_for('voice_state_update', check=check)
		await channel2.delete()
	if after.channel.id == 784356312641306655:
		
		mainCategory = discord.utils.get(guild.categories, id=769098923377688606)
		channel2 = await guild.create_voice_channel(name=f"💀║{member}",category=mainCategory)
		await member.move_to(channel2)
		await channel2.set_permissions(member,mute_members=True,move_members=True,manage_channels=True)
		def check(a,b,c):
			return len(channel2.members) == 0
		await client.wait_for('voice_state_update', check=check)
		await channel2.delete()
	else:
		pass

@client.event
async def on_guild_join(guild):
	post = {
		"_guild_id": guild.id,
		"prefix": "!",
		"welcome": 0
	}
	
	prefixes.insert_one(post)

		
@client.event
async def on_guild_remove(guild):
	prefixes.delete_one({"_guild_id": guild.id})

@client.command(
	name="Загрузить",
	aliases=["load"],
	brief="Загрузить ког",
	usage="load <namecog>"
	)
async def load(ctx, extension):
	if ctx.author.id == 618488298804871218:#id developers 
		client.load_extension(f"cogs.{extension}")#загрузка кога
		emb=discord.Embed(
			title="Загрузка кога",
			description="Вы успешно загрузили ког ``{}``".format(extension),
			colour=discord.Color.green()
			)
		await ctx.send(embed=emb)#отправка сообщения об успешной загрузки бота
		
	else:
		await ctx.send("Вы не разработчик и не владелец бота!")
@client.command(
	name="Отключить",
	aliases=["unload"],
	brief="Выгрузить ког",
	usage="unload <namecog>"
	)
async def unload(ctx, extension):
	if ctx.author.id == 618488298804871218:#id developers
		client.unload_extension(f"cogs.{extension}")#отгрузка кога(отключение)
		emb=discord.Embed(
			title="Загрузка бота",
			description="Вы успешно отключили ког ``{}``".format(extension),
			colour=discord.Color.green()
			)
		await ctx.send(embed=emb)#сообщение о успешном выполнении
		
	else:
		await ctx.send("Вы не разработчик и не владелец бота!")
@client.command(
	name="Перезагрузить",
	aliases=["reload"],
	brief="Перезагрузить ког",
	usage="reload <namecog>"
	)
async def reload(ctx, extension):
	
	if ctx.author.id == 618488298804871218:#id developers
		client.unload_extension(f"cogs.{extension}")#отгрузка кога(отключение)
		client.load_extension(f"cogs.{extension}")#loaded cog
		emb=discord.Embed(
			title="Перезагрузить ког",
			description="Вы успешно перезагрузили ког ``{}``".format(extension),
			colour=discord.Color.green()
			)
		await ctx.send(embed=emb)#сообщение о успешном выполнении
	else:
		await ctx.send("Вы не разработчик и не владелец бота!")
		
for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

token = os.environ.get('BOT_TOKEN')
client.run(str(token))