#imports
from discord.ext import commands, tasks
from itertools import cycle 
from datetime import datetime
import datetime
import io
import discord
import os
import traceback

client = commands.Bot(command_prefix = "!",intents = discord.Intents.all())
client.remove_command("help")
stats = cycle(['!help', 'https://discord.gg/YkA5ft9'])
@client.event
async def on_ready():
	print("Bot connected to the server")
	change_stats.start()
@tasks.loop(seconds = 10)
async def change_stats():
	await client.change_presence( status = discord.Status.do_not_disturb, activity = discord.Game(name = next(stats)))
@client.event
async def on_command_error(ctx, exception):
	if isinstance(error, commands.MissingPermissions):
			await ctx.send(embed=discord.Embed(
				title=':x:Ошибка',
				description=f"""Недостаточно прав для использования команды!""", 
				colour=discord.Color.red()),
				delete_after=10
				)
	else:
	    channel = client.get_channel(770904950879682560)#вставьте свой айди канала
	    embed = discord.Embed(title=':x: Ошибка Команды(Command)', colour=0xe74c3c)
	    embed.add_field(name='Введённая команда', value=ctx.command)
	    embed.description = f"""```py
	{traceback.format_exception(type(exception), exception, exception.__traceback__)}
	```"""
	    embed.timestamp = datetime.datetime.utcnow()
	    await channel.send(embed=embed)
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
async def on_error(event, *args, **kwargs): # для остальных ошибок   
    channel = client.get_channel(770904950879682560)#вставьте свой айди канала
    embed = discord.Embed(title=':x: Ошибка События(Event)', colour=0xe74c3c) #Red
    embed.add_field(name='Событие', value=event)
    embed.description = f"""```py
{traceback.format_exc()}
```"""
    embed.timestamp = datetime.datetime.utcnow()
    await channel.send(embed=embed)
@client.event
async def on_member_join(member):
	channel=client.get_channel(758599386653261844)
	emb=discord.Embed(title=f"Добро пожаловать на сервер {member.guild.name}", colour=discord.Color.blue())
	emb.add_field(name="Не забудь прочитать правила в канале: ", value="<#758706739008503849>", inline=False)
	emb.add_field(name="Когда прочитал правила, можете идти общаться в канал: ", value="<#758599939151495180>", inline=False)
	emb.set_thumbnail(url='https://i.pinimg.com/originals/01/fb/2c/01fb2cb2cf0855514cf1df69f46acda8.gif')
	emb.set_image(url='https://i.pinimg.com/originals/af/80/39/af8039261a387be71514bb4c2e5e54b5.gif')
	
	
	await member.send(embed=emb)
	embb = discord.Embed(
		title=f"{member.name}, обро пожаловать!",
		colour=discord.Color.gold(), 
		description=f"""**Поприветствуем** нового участника сервера. Его зовут {member.mention},
Он уже {member.guild.member_count} участник нашего сервера!""")
	embb.set_footer(text=f"Сервер: {member.guild.name}")
	embb.set_thumbnail(url=member.avatar_url)

	await channel.send(embed=embb)
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