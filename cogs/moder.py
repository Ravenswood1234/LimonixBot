#imports
from requests import get
from datetime import datetime
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from urllib.parse import urlparse
from discord import utils
import pip
import os
import discord
import datetime
import socket
import json
import requests
import random
import asyncio
import re
import io
import time
client = commands.Bot(command_prefix = "!")
client.remove_command('help')
answer5 = ['Вы не можете выгнать пользователя с такой же ролью!', 'Ваши роли одинаковы, я не могу так сделать!', 'Вы не можете выгнать такого же модератора как и вы!']
answer4 = ['Это невозможно сделать, так как выгнать меня может только основатель сервера!', 'Это может сделать только основатель сервера', 'Так сделать невозможно!', 'Увы, меня нельзя так остранить...']
answer3 = ['У вас не хватает прав!', 'Его роль стоит выше вашей!', 'Это нельзя сделать!', 'Ваша роль менее значима, чем этого пользователя!']
answer2 = ['Ты быканул на основателя сервера, или мне показалось?', 'Что он такого плохого тебе сделал?', 'При всём уважении к тебе я так не могу сделать!', 'Ах если бы я так мог...', 'Я не буду этого делать!', 'Сорян, но не в моих это силах!']
answer = ['Самоубийство не приведёт ни к чему хорошему!', 'Напомню: суицид - не выход!', 'Увы, я не могу этого сделать!', 'Самоубийство - не выход!', 'Не надо к себе так относиться!', 'Я не сделаю этого!', 'Я не буду это делать!', 'Я не выполню это действие', 'Не заставляй меня это сделать!']
class Moderator(commands.Cog):
	"""docstring for User"""
	def __init__(self, client):
		self.client = client
		
	@commands.Cog.listener()
	async def on_ready(self):
		print("Moderator cog connect")
	@commands.command(
		name='голосование',
		aliases=['Poll', 'POLL', 'poll'],
		brief='Создаст голосование',
		usage='poll <tema>')
	@commands.has_permissions( manage_messages = True )
	async def _poll(self, ctx, *, tema=None):
		
		
		if tema is None:
			await ctx.send("Укажите тему голосования!", delete_after=10)
		else:
			emb=discord.Embed(title='📢 Голосование:', 
				description=f'{tema}', 
				colour=0x00FFFF, 
				timestamp=ctx.message.created_at)
			
			msg=await ctx.send(embed=emb)
			await msg.add_reaction('👍')
			await msg.add_reaction('👎')
	@commands.command(
		name='очистка',
		aliases=['clear', 'clean'],
		brief='Удалит определеное кол-во сообщений',
		usage='clear <amount>'
		)
	@commands.has_permissions(manage_messages=True)
	async def clean(self, ctx, amount : int):
		
		if amount is None:
			await ctx.send(embed=discord.Embed(
				description="Укажите число удаляемых сообщений!", 
				colour=discord.Color.red()),
				delete_after=10)
		else:
			
			deleted = await ctx.channel.purge( limit = amount )
			emb = discord.Embed(description=f'Очищено сообщений: {len(deleted)}',colour=discord.Color.green())
			await ctx.send( embed = emb, delete_after = 30 )
	@commands.command(
		name='идея',
		aliases=['idea'],
		brief='Кинет идею создателю',
		usage='idea <idea>')
	async def _idea(self, ctx, *, idea=None):
		
		if idea is None:
			embed = discord.Embed(title="Ошибка", description="Укажите идею {}idea <idea>".format(ctx.command), color=discord.Color.red())
			await ctx.send(embed=embed)
		else:
			member = await self.client.fetch_user(user_id=618488298804871218)#айди
			embed = discord.Embed(title="Новая Идея!", description=f"**Отправитель:\n**{ctx.author}\n**Айди:**\n{ctx.author.id}\n**Идея:**\n{idea}", color=discord.Color.green())
			embed2 = discord.Embed(title="Успешно!", description=f"Идея была успешно отправлена создатаелю\n**Содержимое:**\n{idea}", color=discord.Color.green())
			await member.send(embed=embed)
			await ctx.send(embed=embed2)
	@commands.command(
		name='баг',
		aliases=['bugs'],
		brief='Кинет баг создателю',
		usage='bugs <bug>'
		)
	async def bug(self, ctx, *, idea=None):
		await ctx.message.delete()
		if idea is None:
			embed = discord.Embed(title="Ошибка", description="Укажите идею {}idea <idea>".format(ctx.command), color=discord.Color.red())
			await ctx.send(embed=embed)
		else:
			member = await self.client.fetch_user(user_id=618488298804871218)#айди
			embed = discord.Embed(title="Новый баг!", description=f"**Отправитель:\n**{ctx.author}\n**Айди:**\n{ctx.author.id}\n**Идея:**\n{idea}", color=discord.Color.green())
			embed2 = discord.Embed(title="Успешно!", description=f"Баг был успешно отправлен создатаелю\n**Содержимое:**\n{idea}", color=discord.Color.green())
			await member.send(embed=embed)
			await ctx.send(embed=embed2)

	# @commands.command()
	# @commands.has_permissions(manage_messages=True)
	# async def say(self, ctx, channel: discord.TextChannel = None):
	# 	if channel is None:
	# 		await ctx.send("Укажите канал для отправке")
	# 	else:
	# 		emb=discord.Embed(
	# 			title="Выбирете вид say",
	# 			colour=discord.Color.gold()
	# 			)
	# 		emb.add_field(
	# 			name="1. - 1️⃣",
	# 			value='[Заголовок] | [Описание] (картинка)',
	# 			inline=False
	# 			)
	# 		emb.add_field(
	# 			name="2. - 2️⃣",
	# 			value='[Заголовок] | (картинка)',
	# 			inline=False
	# 			)
	# 		emb.add_field(
	# 			name="3. - 3️⃣",
	# 			value='[Описание] | (картинка)',
	# 			inline=False
	# 			)
	# 		emb.add_field(
	# 			name="4. - 4️⃣",
	# 			value='[Заголовок] | [Описание]',
	# 			inline=False
	# 			)
	# 		msg = await ctx.send(embed=emb)
	# 		await msg.add_reaction('1️⃣')
	# 		await msg.add_reaction('2️⃣')
	# 		await msg.add_reaction('3️⃣')
	# 		await msg.add_reaction('4️⃣')
	# 		def check(reaction, user):
	# 			return user == ctx.author
	# 		reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check = check)
	# 		if str(reaction.emoji) == '1️⃣':
	# 			await ctx.send("Теперь киньте заголовок")
	# 			def check(m):
	# 				return m.author.id == ctx.author.id
	# 			try:
	# 				h = await self.client.wait_for('message',timeout=30.0, check=check)
	# 			except asyncio.TimeoutError:
	# 				await ctx.send('Вы не кинули заголовок!', delete_after=10)
	# 			else:

	# 				await ctx.send("Теперь киньте описание")
	# 				def check(m):
	# 					return m.author.id == ctx.author.id
	# 				try:
	# 					r = await self.client.wait_for('message',timeout=30.0, check=check)
	# 				except asyncio.TimeoutError:
	# 					await ctx.send('Вы не кинули описание!', delete_after=10)
	# 				else: 
	# 					await ctx.send("Теперь киньте ссылку на картинку")
	# 					def check(m):
	# 						return m.author.id == ctx.author.id
	# 					try:
	# 						a = await self.client.wait_for('message',timeout=30.0, check=check)
	# 					except asyncio.TimeoutError:
	# 						await ctx.send('Вы не кинули ссылку на картинку!', delete_after=10)
	# 					else:
	# 						emb = discord.Embed(title=h.content,
	# 							description=r.content,
	# 							colour=discord.Color.orange())
	# 						emb.set_image(url=a.content)
	# 						await channel.send(embed=emb)
	# 		if str(reaction.emoji) == '2️⃣':	
	# 			await ctx.send("Теперь киньте заголовок")
	# 			def check(m):
	# 				return m.author.id == ctx.author.id
	# 			try:
	# 				h = await self.client.wait_for('message',timeout=30.0, check=check)
	# 			except asyncio.TimeoutError:
	# 				await ctx.send('Вы не кинули заголовок!', delete_after=10)
	# 			else:
	# 				emb = discord.Embed(title=h.content,
	# 					colour=discord.Color.orange())
	# 				await ctx.send("Теперь киньте ссылку на картинку")
	# 				def check(m):
	# 					return m.author.id == ctx.author.id
	# 				try:
	# 					a = await self.client.wait_for('message',timeout=30.0, check=check)
	# 				except asyncio.TimeoutError:
	# 					await ctx.send('Вы не кинули ссылку на картинку!', delete_after=10)
	# 				else:
	# 					emb.set_image(url=a.content)
	# 					await channel.send(embed=emb)
	# 		if str(reaction.emoji) == '3️⃣':
	# 			await ctx.send("Теперь киньте описание")
	# 			def check(m):
	# 				return m.author.id == ctx.author.id
	# 			try:
	# 				h = await self.client.wait_for('message',timeout=30.0, check=check)
	# 			except asyncio.TimeoutError:
	# 				await ctx.send('Вы не кинули описание!', delete_after=10)
	# 			else:
	# 				emb = discord.Embed(description= h.content,
	# 					colour=discord.Color.orange())
	# 				await ctx.send("Теперь киньте ссылку на картинку")
	# 				def check(m):
	# 					return m.author.id == ctx.author.id
	# 				try:
	# 					a = await self.client.wait_for('message',timeout=30.0, check=check)
	# 				except asyncio.TimeoutError:
	# 					await ctx.send('Вы не кинули ссылку на картинку!', delete_after=10)
	# 				else:
	# 					emb.set_image(url=a.content)
	# 					await channel.send(embed=emb)
	# 		if str(reaction.emoji) == '4️⃣':
	# 			await ctx.send("Теперь киньте заголовок")
	# 			def check(m):
	# 				return m.author.id == ctx.author.id
	# 			try:
	# 				h = await self.client.wait_for('message',timeout=30.0, check=check)
	# 			except asyncio.TimeoutError:
	# 				await ctx.send('Вы не кинули заголовок!', delete_after=10)
	# 			else:

	# 				await ctx.send("Теперь киньте описание")
	# 				def check(m):
	# 					return m.author.id == ctx.author.id
	# 				try:
	# 					a = await self.client.wait_for('message',timeout=30.0, check=check)
	# 				except asyncio.TimeoutError:
	# 					await ctx.send('Вы не кинули описание!', delete_after=10)
	# 				else:
	# 					emb = discord.Embed(title=h.content, 
	# 						description = a.content,
	# 						colour=discord.Color.orange())
	# 					await channel.send(embed=emb)
	@commands.command(
		name='кик',
		aliases=["kick"],
		usage = "kick <@user>",
		brief = "Кикнуть пользователя")
	@commands.has_permissions( kick_members = True )
	@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.guild )
	async def kicks(self, ctx, member : discord.Member, *, reason=None):
		
 
		if ctx.author.top_role == member.top_role:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':leg: Кик:', value = random.choice(answer5))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
 
		elif member == ctx.bot.user:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':leg: Кик:', value = random.choice(answer4))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
		elif ctx.author.top_role < member.top_role:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':leg: Кик:', value = random.choice(answer3))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
		elif member == ctx.author:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':leg: Кик:', value = random.choice(answer))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
		elif member == ctx.guild.owner:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':leg: Кик:', value = random.choice(answer2))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
		emb = discord.Embed(color=discord.Color.red())
		emb.add_field(name=':leg: Кик:', value = f'Вы уверены, что хотите кикнуть `{member.name}`?')
		emb.set_footer(text='Если это ошибка нажми на крестик')
		msg = await ctx.send(embed=emb, delete_after = 30)
		await msg.add_reaction('✅')
		await msg.add_reaction('❌')
		def check(reaction, user):
			return user == ctx.author 
		
		reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check = check)
		if str(reaction.emoji) == '❌':
			await ctx.send(embed=discord.Embed(title="Отменено✅", colour=discord.Color.red()))
		elif str(reaction.emoji) == '✅':
			if reason == None:
				try:
					await member.kick(reason=reason)
				except:
					success = False
				else:
					success = True
 
				emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
				emb.add_field( name = ':leg: Кик:', value = f'`{member.name}` кикнут!', inline = False)
				emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
				await ctx.send(embed=emb)
 
				return
			try:
				await member.kick(reason=reason)
			except:
				success = False
			else:
				success = True
 
			emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
			emb.add_field( name = ':leg: Кик:', value = f'`{member.name}` кикнут!', inline = False)
			emb.add_field( name = 'По причине:', value = reason, inline = False)
			emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
			await ctx.send(embed=emb)
	@commands.command(
		name='бан',
		aliases=["ban"],
		usage = "ban <@user>",
		brief="Забанить пользователя"
		)
	@commands.has_permissions( ban_members = True )
	@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.guild )
	async def ban(self, ctx, member : discord.Member, *, reason=None):
		
		if ctx.author.top_role == member.top_role:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':leg: Кик:', value = random.choice(answer5))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
 
		elif member == ctx.bot.user:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':hammer: Бан:', value = random.choice(answer4))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
		elif ctx.author.top_role < member.top_role:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':hammer: Бан:', value = random.choice(answer3))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
		elif member == ctx.author:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':hammer: Бан:', value = random.choice(answer))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
		elif member == ctx.guild.owner:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':hammer: Бан:', value = random.choice(answer2))
			await ctx.send(embed=emb, delete_after=30)
 
			return
		emb = discord.Embed(colour=discord.Color.red())
		emb.add_field(name=':hammer: Бан:', value = f'Вы уверены, что хотите забанить `{member.name}`?')
		emb.set_footer(text='Нажимайте на крестик, если это ошибка!')
		msg = await ctx.send(embed=emb, delete_after = 30)
		await msg.add_reaction('✅')
		await msg.add_reaction('❌')
		def check(reaction, user):
			return user == ctx.author 
		
		reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check = check)
		if str(reaction.emoji) == '❌':
			await ctx.send(embed=discord.Embed(title="Отменено✅", colour=discord.Color.red()))
		elif str(reaction.emoji) == '✅':
 
			if reason == None:
 
				try:
 
					await member.ban(reason=None)
				except:
					success = False
				else:
					success = True
 
				emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
				emb.add_field( name = ':hammer: Бан:', value = f'Участник `{member.name}` забаннен!', inline = False)
				emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
 
				await ctx.send(embed=emb)
 
				return
 
			try:
 
				await member.ban(reason=reason)
			except:
				success = False
			else:
				success = True
 
			emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
			emb.add_field( name = ':hammer: Бан:', value = f'Участник `{member.name}` забаннен!', inline = False)
			emb.add_field( name = 'По причине:', value = reason, inline = False)
			emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
 
			await ctx.send(embed=emb)

	@commands.command(
		name='мут',
		aliases=["mute"],
		usage="mute <@user>",
		brief="Замьютить пользователя")
	@commands.has_permissions( kick_members = True )
	@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.guild )
	async def muted(self, ctx, member:discord.Member, duration=None, *, reason=None):
		
		if ctx.author.top_role == member.top_role:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':shushing_face: Мут:', value = random.choice(answer5))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
 
		elif member == ctx.bot.user:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':shushing_face: Мут:', value = random.choice(answer4))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
		elif ctx.author.top_role < member.top_role:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':shushing_face: Мут:', value = random.choice(answer3))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
		elif member == ctx.author:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':shushing_face: Мут:', value = random.choice(answer))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
		elif member == ctx.guild.owner:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':shushing_face: Мут:', value = random.choice(answer2))
			await ctx.send(embed=emb, delete_after=30)
 
			return
		emb = discord.Embed(colour=discord.Color.red())		
		emb.add_field(name=':shushing_face: Мут', value="Потвердите действие!")
		emb.set_footer(text="Нажмите на крестик, если это ошибка!")
		msg = await ctx.send(embed=emb, delete_after = 30)
		await msg.add_reaction('✅')
		await msg.add_reaction('❌')
		def check(reaction, user):
			return user == ctx.author 
		
		reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check = check)
		if str(reaction.emoji) == '❌':
			await ctx.send(embed=discord.Embed(title="Отменено✅", colour=discord.Color.red()))
		elif str(reaction.emoji) == '✅':
 
			if duration == None:
				if reason == None:
					try:
						progress = await ctx.send('Мьючу пользователя!', delete_after = 5)
 
						emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
						emb.add_field( name = ':shushing_face: Мут:', value = f'Участник `{member.name}` замучен!\nОн не выйдет из мута, пока его не размутят!', inline = False)
						emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
						await ctx.send( embed = emb)
   
 
						for channel in ctx.guild.text_channels:
							await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(send_messages = False), reason=reason)
	
						for channel in ctx.guild.voice_channels:
							await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(speak=False), reason=reason)
					except:
						success = False
					else:
						success = True
 
					emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
					emb.add_field( name = ':shushing_face: Мут:', value = f'Вы, `{member.name}` замучены на сервере `{ ctx.guild.name }`!\nВы не выйдете из мута, пока вас не размутят!', inline = False)
					emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
					await member.send( embed = emb)
 
 
					return
 
 
				try:
					progress = await ctx.send('Мьючу пользователя!', delete_after = 5)
 
					emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
					emb.add_field( name = ':shushing_face: Мут:', value = f'Участник `{member.name}` замучен!\nОн не выйдет из мута, пока его не размутят!', inline = False)
					emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
					await ctx.send( embed = emb)
  
 
					for channel in ctx.guild.text_channels:
						await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(send_messages = False), reason=reason)
   
					for channel in ctx.guild.voice_channels:
						await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(speak=False), reason=reason)
				except:
					success = False
				else:
					success = True
 
				emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
				emb.add_field( name = ':shushing_face: Мут:', value = f'Вы, `{member.name}` замучены на сервере `{ ctx.guild.name }`!\nВы не выйдете из мута, пока вас не размутят!', inline = False)
				emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
				await member.send( embed = emb)
 
				return
 
 
			unit = duration[-1]
			if unit == 'с':
				time = int(duration[:-1])
				longunit = 'секунд'
			elif unit == 's':
				time = int(duration[:-1])
				longunit = 'секунд'
			elif unit == 'м':
				time = int(duration[:-1]) * 60
				longunit = 'минуту/минут'
			elif unit == 'm':
				time = int(duration[:-1]) * 60
				longunit = 'минуту/минут'
			elif unit == 'ч':
				time = int(duration[:-1]) * 60 * 60
				longunit = 'час/часов'
			elif unit == 'h':
				time = int(duration[:-1]) * 60 * 60
				longunit = 'час/часов'
			elif unit == 'д':
				time = int(duration[:-1]) * 60 * 60 *24
				longunit = 'день/дней'
			elif unit == 'd':
				time = int(duration[:-1]) * 60 * 60 *24
				longunit = 'день/дней'
			else:
				await ctx.send('Неправильное написание времени!', delete_after = 30)
				return
 
			if reason == None:
				try:
					progress = await ctx.send('Мьючу пользователя!', delete_after = 5)
 
					emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
					emb.add_field( name = ':shushing_face: Мут:', value = f'Участник `{member.name}` замучен!\nОн выйдет из мута через: {str(duration[:-1])} {longunit}', inline = False)
					emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
					await ctx.send( embed = emb)
 
  
					for channel in ctx.guild.text_channels:
						await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(send_messages = False), reason=reason)
 
					for channel in ctx.guild.voice_channels:
						await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(speak=False), reason=reason)
				except:
					success = False
				else:
					success = True
 
				emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
				emb.add_field( name = ':shushing_face: Мут:', value = f'Вы, `{member.name}` замучены на сервере `{ ctx.guild.name }`!\nВы выйдете из мута через: {str(duration[:-1])} {longunit}', inline = False)
				emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
				await member.send( embed = emb)
	
				await asyncio.sleep(time)
				try:
					for channel in ctx.guild.channels:
						await channel.set_permissions(member, overwrite=None, reason=reason)
				except:
					pass
 
				return
  
			try:
				progress = await ctx.send('Мьючу пользователя!', delete_after = 5)
 
				emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
				emb.add_field( name = ':shushing_face: Мут:', value = f'Участник `{member.name}` замучен!\nОн выйдет из мута через: {str(duration[:-1])} {longunit}', inline = False)
				emb.add_field( name = 'По причине:', value = reason, inline = False)
				emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
				await ctx.send( embed = emb)
 
 
				for channel in ctx.guild.text_channels:
					await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(send_messages = False), reason=reason)
 
				for channel in ctx.guild.voice_channels:
					await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(speak=False), reason=reason)
			except:
				success = False
			else:
				success = True
 
			emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
			emb.add_field( name = ':shushing_face: Мут:', value = f'Вы, `{member.name}` замучены на сервере `{ ctx.guild.name }`!\nВы выйдете из мута через: {str(duration[:-1])} {longunit}', inline = False)
			emb.add_field( name = 'По причине:', value = reason, inline = False)
			emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
  
			await member.send( embed = emb)
	
			await asyncio.sleep(time)
			try:
				for channel in ctx.guild.channels:
					await channel.set_permissions(member, overwrite=None, reason=reason)
			except:
				pass
	@commands.command(
		name='размут', 
		aliases=["unmute"],
		brief="Размьтить пользователя", 
		usage="unmute <@muteduser>")
	@commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.guild )
	@commands.has_permissions( kick_members = True )
	async def unmuted(self, ctx, member:discord.Member, *, reason=None):
		
 
		if ctx.author.top_role == member.top_role:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':smiley: Размут:', value = random.choice(answer5))
			await ctx.send(embed=emb, delete_after=30)
 
			return
		elif member == ctx.bot.user:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':smiley: Размут:', value = random.choice(answer4))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
		elif ctx.author.top_role < member.top_role:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':smiley: Размут:', value = random.choice(answer3))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
		elif member == ctx.author:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':smiley: Размут:', value = random.choice(answer))
			await ctx.send(embed=emb, delete_after=30)
 
			return
 
		elif member == ctx.guild.owner:
			emb = discord.Embed(colour=discord.Color.red())
			emb.add_field(name=':smiley: Размут:', value = random.choice(answer2))
			await ctx.send(embed=emb, delete_after=30)
 
			return
		emb = discord.Embed(description="Потвердите действие!", colour=discord.Color.red())
		msg = await ctx.send(embed=emb, delete_after = 30)
		await msg.add_reaction('✅')
		def check(reaction, user):
			return user == ctx.author 
		
		reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check = check)
		if str(reaction.emoji) == '❌':
			await ctx.send(embed=discord.Embed(title="Отменено✅", colour=discord.Color.red()))
		elif str(reaction.emoji) == '✅':
			await ctx.send('Размучиваю пользователя', delete_after = 5)
			try:
				for channel in ctx.message.guild.channels:
					await channel.set_permissions(member, overwrite=None, reason=reason)
			except:
				success = False
			else:
				success = True
 
			if reason == None:
				emb = discord.Embed( colour = discord.Color.green(), timestamp = ctx.message.created_at)
				emb.add_field( name = ':smiley: Размут:', value = f'Вы, `{member.name}` размучены на сервере `{ ctx.guild.name }`!', inline = False)
				emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
				await member.send( embed = emb)
			
				emb = discord.Embed( colour = discord.Color.green(), timestamp = ctx.message.created_at)
				emb.add_field( name = ':smiley: Размут:', value = f'Участник `{member.name}` размучен!', inline = False)
				emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
				await ctx.send( embed = emb)
 
				return
 
			emb = discord.Embed( colour = discord.Color.green(), timestamp = ctx.message.created_at)
			emb.add_field( name = ':smiley: Размут:', value = f'Вы, `{member.name}` размучены на сервере `{ ctx.guild.name }`!', inline = False)
			emb.add_field( name = 'По причине:', value = reason, inline = False)
			emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
  
			await member.send( embed = emb)
			
			emb = discord.Embed( colour = discord.Color.green(), timestamp = ctx.message.created_at)
			emb.add_field( name = ':smiley: Размут:', value = f'Участник `{member.name}` размучен!', inline = False)
			emb.add_field( name = 'По причине:', value = reason, inline = False)
			emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
			await ctx.send( embed = emb)

def setup(client):
	client.add_cog(Moderator(client))	