#imports
from discord.ext import commands, tasks
from itertools import cycle 
from datetime import datetime
from random import randint
from pymongo import MongoClient
import datetime
import io
import discord
import os
import traceback
import random
class Econom(commands.Cog, name="Экономиика"):
	"""docstring for User"""
	def __init__(self, client):
		self.client = client
		self.prefix = MongoClient("mongodb+srv://limonix:1q234567wE@cluster0.tthbn.mongodb.net/Guild?retryWrites=true&w=majority")
		self.prefixes = self.prefix.Guild.prefixes
		self.cluster = MongoClient("mongodb+srv://limonix:1q234567wE@cluster0.tthbn.mongodb.net/lim?retryWrites=true&w=majority")
		self.collection = self.cluster.lim.post
		self.users = MongoClient("mongodb+srv://limonix:1q234567wE@cluster0.tthbn.mongodb.net/member?retryWrites=true&w=majority")
		self.userinfo = self.users.member.information
		self.s = MongoClient("mongodb+srv://limonix:1q234567wE@cluster0.tthbn.mongodb.net/shop?retryWrites=true&w=majority")
		self.shop = self.s.shop.shopping
	@commands.command(aliases=['setprefix'])
	@commands.has_permissions( administrator = True )
	async def prefix(self, ctx, arg: str = None):
		if arg is None:
			emb = discord.Embed(title = "Изменение префикса", description = "Введите префикс, на какой хотите поменять?", colour = discord.Color.red())
			emb.add_field(name = "Пример использования комманды", value = f"{ctx.prefix}prefix <ваш префикс>")
			await ctx.send(embed = emb)
		elif len(str(arg)) > 5:
			emb = discord.Embed(title = "Изменение префикса", description = "Введите префикс не больше 5-ти символов", colour = discord.Color.red())
			emb.add_field(name = "Пример использования комманды", value = f"{ctx.prefix}prefix <ваш префикс>")
			await ctx.send(embed = emb)
		else:
			self.prefixes.update_one({"_guild_id": ctx.guild.id}, {"$set": {"prefix": arg}})
			
			emb = discord.Embed(title = "Изменение префикса", description = f"Префикс сервера был обновлён на: {arg}", colour = discord.Color.green())
			await ctx.send(embed = emb)
	@commands.command(aliases=['welcome'])
	@commands.has_permissions( administrator = True )
	async def setwelchannel(self, ctx, channel: discord.TextChannel=None):
		
		if channel is None:
			await ctx.send(
				embed=discord.Embed(
					title="Канал приветствия",
					description="Вы не указали канал",
					colour=discord.Color.red()
					)

				)
		else:
			if type(channel) == discord.TextChannel:
				self.prefixes.update_one({"_guild_id": ctx.guild.id}, {"$set": {"welcome": int(channel.id)}})
				await ctx.send(
					embed=discord.Embed(
						title="Успешно",
						description=f"Вы успешно установили канал для приветсвий <#{channel.id}>",
						colour=discord.Color.gold()
						)
					)
			else:
				await ctx.send(
					embed=discord.Embed(
						title="Канал для приветсвий",
						description="Укажите текстовый канал!",
						colour=discord.Color.red()
						)
					)
	@commands.command(aliases=['leave'])
	@commands.has_permissions( administrator = True )
	async def setlevchannel(self, ctx, channel: discord.TextChannel=None):
		
		if channel is None:
			await ctx.send(
				embed=discord.Embed(
					title="Канал прощаний",
					description="Вы не указали канал",
					colour=discord.Color.red()
					)

				)
		else:
			if type(channel) == discord.TextChannel:
				self.prefixes.update_one({"_guild_id": ctx.guild.id}, {"$set": {"leave": int(channel.id)}})
				await ctx.send(
					embed=discord.Embed(
						title="Успешно",
						description=f"Вы успешно установили канал для прощаний <#{channel.id}>",
						colour=discord.Color.gold()
						)
					)
			else:
				await ctx.send(
					embed=discord.Embed(
						title="Канал для прощаний",
						description="Укажите текстовый канал!",
						colour=discord.Color.red()
						)
					)
	@commands.command(aliases=['баланс'])
	async def balance(self, ctx, member:discord.Member=None):
		if member is None:
			member = ctx.author
		if type(member) == discord.Member:
			emb = discord.Embed(
				title=f"Баланс пользователя {member.name}",
				colour=discord.Color.gold()
				)
			emb.add_field(
				name=f"🍋Limoncoin:",
				value=self.collection.find_one({"id":member.id, "guild_id": ctx.guild.id})['limoncoin']
				)
			emb.add_field(
				name="🥝KiwiCoin:",
				value=self.collection.find_one({'id':member.id, 'guild_id':ctx.guild.id})['cash']
				)
			await ctx.send(embed=emb)
		else:

			emb = discord.Embed(
				title=f'Баланс пользователя {ctx.author.name}',
				colour=discord.Color.gold()
				)
			emb.add_field(
				name=f"🍋LimonCoin:",
				value=self.collection.find_one({"id":ctx.author.id, "guild_id": ctx.guild.id})['limoncoin'],
				inline=False
				)
			emb.add_field(
				name="🥝KiwiCoin:",
				value=self.collection.find_one({'id':ctx.author.id, 'guild_id':ctx.guild.id})['cash']
				)
			await ctx.send(embed=emb)
	@commands.command(aliases=['addmoney'])
	@commands.has_permissions(administrator=True)
	async def award(self, ctx, member:discord.Member=None, amount:int = None, val = None):
		lim = self.collection.find_one({"id":member.id, "guild_id": ctx.guild.id})['limoncoin']
		Kiwi = self.collection.find_one({"id":member.id, "guild_id": ctx.guild.id})['cash']
		if member is None:
			await ctx.send(
				embed=discord.Embed(
					title="Пополнить",
					description="Вы не указали пользователя!",
					colour=discord.Color.red()
					)
				)
		elif amount is None:
			await ctx.send(
				embed=discord.Embed(
					title="Пополнить",
					description="Вы неуказали кол-во монет которые хотите выдать пользователю",
					colour=discord.Color.red()
					)
				)
		elif val is None:
			await ctx.send(
				embed = discord.Embed(
					title="Пополнить",
					description="Вы не указали валюту, которую хотите поплнить <limcoin/kiwicoin>"
					)
				)	
		else:
			if type(member) == discord.Member:
				if val == 'kiwicoin':
					self.collection.update_one({"id":member.id, "guild_id": ctx.guild.id}, {"$set": {"cash": Kiwi + amount}})
					await ctx.send(
						embed=discord.Embed(
							title="Успешно",
							description=f"Вы пополнили баланс пользователю {member.name}",
							colour=discord.Color.gold()
							)
						)
				elif val == 'limoncoin':
					self.collection.update_one({"id":member.id, "guild_id": ctx.guild.id}, {"$set": {"limoncoin": lim + amount}})
					await ctx.send(
						embed=discord.Embed(
							title="Успешно",
							description=f"Вы пополнили баланс пользователю {member.name}",
							colour=discord.Color.gold()
							)
						)
				else:
					await ctx.send(
						embed = discord.Embed(
							title="Пополнить",
							description="Вы неправильно указали валюту!",
							colour=discord.Color.red()

							)
						)
			else:
				await ctx.send(
					embed=discord.Embed(
						title="Пополнить",
						description="Укажите **пользователя**!",
						colour=discord.Color.red()
						)
					)
	@award.error
	async def award_error(self, ctx, error):
		if isinstance(error, commands.UserInputError):
			await ctx.send(
				embed=discord.Embed(
					title="Пополнить",
					description="Укажите сумму которую хотите поплони пользователю!",
					colour=discord.Color.red()
					))
	@commands.command()
	@commands.cooldown(1, 7200, commands.BucketType.user)
	async def work(self, ctx):
		Limm = self.collection.find_one({"id":ctx.author.id, "guild_id": ctx.guild.id})['limoncoin']
		KIWW = self.collection.find_one({"id":ctx.author.id, "guild_id": ctx.guild.id})['cash']
		lim = randint(50, 500)
		kiw  = randint(100, 1000)
		val = randint(1, 2)
		if val == 1:
			self.collection.update_one({"id":ctx.author.id, "guild_id": ctx.guild.id}, {"$set": {"cash": KIWW + kiw}})
			emb = discord.Embed(
				title="Работа",
				colour=discord.Color.gold()
				)
			emb.add_field(
				name="Лимонкоинов",
				value=f"Вы заработали: 0"
				)
			emb.add_field(
				name="Кивикоины",
				value=f"Вы заработали: {kiw}"
				)
			emb.set_footer(text="Приходите через 2 часа")
			await ctx.send(
				embed=emb
				)
		elif val == 2:
			self.collection.update_one({"id":ctx.author.id, "guild_id": ctx.guild.id}, {"$set": {"limoncoin": Limm + lim}})
			self.collection.update_one({"id":ctx.author.id, "guild_id": ctx.guild.id}, {"$set": {"cash": KIWW + kiw}})
			emb = discord.Embed(
				title="Работа",
				colour=discord.Color.gold()
				)
			emb.add_field(
				name="Лимонкоинов",
				value=f"Вы заработали: {lim}"
				)
			emb.add_field(
				name="Кивикоины",
				value=f"Вы заработали: {kiw}"
				)
			emb.set_footer(text="Приходите через 2 часа")
			await ctx.send(
				embed=emb
				)
	@work.error
	async def work_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			seconds = error.retry_after
			seconds = seconds % (24 * 3600)
			days = seconds // (60 * 60 * 24)
			hours = seconds // 3600
			seconds %= 3600
			minutes = seconds // 60
			seconds %= 60
			await ctx.send(embed=discord.Embed(
				title=':x:Ошибка',
				description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {hours:.0f} часов {minutes:.0f} минут {seconds:.0f} секунд", 
				colour=discord.Color.red()), delete_after=30)
	@commands.command()
	@commands.has_permissions(administrator=True)
	async def take(self, ctx, member:discord.Member=None, amount:int = None, val = None):
		lim = self.collection.find_one({"id":member.id, "guild_id": ctx.guild.id})['limoncoin']
		Kiwi = self.collection.find_one({"id":member.id, "guild_id": ctx.guild.id})['cash']
		if member is None:
			await ctx.send(
				embed=discord.Embed(
					title="Отнять",
					description="Вы не указали пользователя!",
					colour=discord.Color.red()
					)
				)
		elif amount is None:
			await ctx.send(
				embed=discord.Embed(
					title="Отнять",
					description="Вы неуказали кол-во монет которые хотите отнять у пользователя",
					colour=discord.Color.red()
					)
				)
		elif val is None:
			await ctx.send(
				embed = discord.Embed(
					title="Отнять",
					description="Вы не указали валюту, которую хотите отнять <limcoin/kiwicoin>"
					)
				)
		else:
			if type(member) == discord.Member:
				if val == 'kiwicoin':
					self.collection.update_one({"id":member.id, "guild_id": ctx.guild.id}, {"$set": {"cash": Kiwi - amount}})
					await ctx.send(
						embed=discord.Embed(
								title="Успешно",
								description=f"Вы отняли баланс пользователю {member.name}",
								colour=discord.Color.gold()
								)
							)
				elif val == 'limoncoin':
					self.collection.update_one({"id":member.id, "guild_id": ctx.guild.id}, {"$set": {"limoncoin": lim - amount}})
					await ctx.send(
						embed=discord.Embed(
							title="Успешно",
							description=f"Вы отняли баланс пользователю {member.name}",
							colour=discord.Color.gold()
							)
						)
				else:
					await ctx.send(
						embed = discord.Embed(
							title="Отнять",
							description="Вы неправильно указали валюту!",
							colour=discord.Color.red()
							)
						)
			else:
				await ctx.send(
					embed=discord.Embed(
						title="Пополнить",
						description="Укажите **пользователя**!",
						colour=discord.Color.red()
						)
					)
	@commands.command()
	@commands.cooldown(1, 86400, commands.BucketType.user)
	async def daily(self, ctx):
		kiw = randint(500, 10000)
		k = self.collection.find_one({"id":ctx.author.id, "guild_id": ctx.guild.id})['cash']
		self.collection.update_one({"id":ctx.author.id, "guild_id": ctx.guild.id}, {"$set": {"cash": kiw + k}})
		emb = discord.Embed(
			title="Бонус за день",

			colour=discord.Color.gold()
			)
		emb.add_field(
			name="Кивикоины",
			value=kiw
			)
		emb.set_footer(text="Приходите через 24 часа")
		await ctx.send(embed=emb)
	@daily.error
	async def daily_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			seconds = error.retry_after
			seconds = seconds % (24 * 3600)
			days = seconds // (60 * 60 * 24)
			hours = seconds // 3600
			seconds %= 3600
			minutes = seconds // 60
			seconds %= 60
			await ctx.send(embed=discord.Embed(
				title=':x:Ошибка',
				description=f"У вас еще не прошел кулдаун на команду ``{ctx.command}``!\nПодождите еще {days:.0f} дней {hours:.0f} часов {minutes:.0f} минут {seconds:.0f} секунд", 
				colour=discord.Color.red()), delete_after=10)
	@commands.command()
	@commands.cooldown(1, 30, commands.BucketType.user)
	async def casino(self, ctx):
		l = self.collection.find_one({"id":ctx.author.id, "guild_id": ctx.guild.id})['limoncoin']
		member=ctx.author
		lim = randint(100, 1000)
		r = randint(1, 3)
		if l < 100:
			await ctx.send(
				embed=discord.Embed(
					title="Казино",
					description="Чтобы играть, вам нужно иметь хотя бы 100 лимонкоинов!",
					colour=discord.Color.red()
					)
				)
		
		elif r == 2:
			self.collection.update_one({"id":member.id, "guild_id": ctx.guild.id}, {"$set": {"limoncoin": lim + l}})
			emb = discord.Embed(
				title="Казино",
				colour=member.color
				)
			emb.add_field(
				name="Уху, удача похоже на вашей стороне",
				value=f"Вы выиграли {lim} лимонкоинов"
				)
			emb.set_footer(text=f"Победитель: {member.name}", icon_url=member.avatar_url)
			await ctx.send(embed=emb)
		else:
			self.collection.update_one({"id":member.id, "guild_id": ctx.guild.id}, {"$set": {"limoncoin":l - 100}})
			emb = discord.Embed(
				title="Казино",
				colour=member.color
				)
			emb.add_field(
				name="Уху, удача похоже не на вашей стороне",
				value=f"Вы проиграл 100 лимонкоинов"
				)
			emb.set_footer(text=f"Проигравший: {member.name}", icon_url=member.avatar_url)
			await ctx.send(embed=emb)
	@casino.error
	async def casino_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			seconds = error.retry_after
			
			await ctx.send(embed=discord.Embed(
				title=':x:Ошибка',
				description=f"Подожди, не надо банкротить до конца казино!\nПодождите еще {seconds:.0f} секунд", 
				colour=discord.Color.red()), delete_after=10)
	@commands.command()
	async def shop(self, ctx):
		emb = discord.Embed(title="Магазин ролей")
		for role in self.shop.find_one({"guild_id": ctx.guild.id})['shop']:
			emb.add_field(name=f"Цена: {self.shop.find_one({'guild_id':ctx.guild.id})['shop'][role]['cost']}",
				value=f"<&{role}>", inline=False)
		await ctx.embed(embed=emb)
	@commands.command()
	async def add_role(self, ctx, role:discord.Role=None, cost=None):
		role = {
			"guild_id":ctx.guild.id,
			"shop":role.id,
			"cost":cost
		}
		if role is None:
			await ctx.send(
				embed=discord.Embed(
					title="Добавление ролей",
					description="Вы не указали роль!",
					colour=discord.Color.red()
					)
				)
		elif cost is None:
			await ctx.send(
				embed=discord.Embed(
					title="Добавление ролей",
					description="Вы не указали цену роли!",
					colour=discord.Color.red()
					)
				)
		else:
			if self.shop.count_documents({"guild_id":member.guild.id})==0:
				self.shop.insert_one(role)
				await ctx.send(
					embed=discord.Embed(
						title="Успешно",
						description="Была ддобавлена роль в магазин!",
						colour=discord.Color.gold()
						)
					)
			else:
				await ctx.send(
					embed=discord.Embed(
						title="Добавить роль",
						description="Эта роль уже есть в магазине!",
						colour=discord.Color.gold()

						)
					)
def setup(client):
	client.add_cog(Econom(client))