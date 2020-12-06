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
class Econom(commands.Cog):
	"""docstring for User"""
	def __init__(self, client):
		self.client = client
		self.prefix = MongoClient("mongodb+srv://limonix:1q234567wE@cluster0.tthbn.mongodb.net/Guild?retryWrites=true&w=majority")
		self.prefixes = self.prefix.Guild.prefixes
		self.cluster = MongoClient("mongodb+srv://limonix:1q234567wE@cluster0.tthbn.mongodb.net/lim?retryWrites=true&w=majority")
		self.collection = self.cluster.lim.post
		self.users = MongoClient("mongodb+srv://limonix:1q234567wE@cluster0.tthbn.mongodb.net/member?retryWrites=true&w=majority")
		self.userinfo = self.users.member.information

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
	@commands.command(aliases=['баланс'])
	async def balance(self, ctx, member:discord.Member=None):
		if member is None:
			member = ctx.author
		if type(member) == discord.Member:
			emb = discord.Embed(
				colour=discord.Color.gold()
				)
			emb.add_field(
				name=f"Баланс пользователя {member.name}",
				value=f"""Limoncoin: {self.collection.find_one({"id":member.id, "guild_id": ctx.guild.id})['limoncoin']}
KiwiCoin: {self.collection.find_one({'id':member.id, 'guild_id':ctx.guild.id})}"""
				)
			await ctx.send(embed=emb)
		else:

			emb = discord.Embed(
				title=f'Баланс пользователя {ctx.author.name}'
				colour=discord.Color.gold()
				)
			emb.add_field(
				name=f"LimonCoin:",
				value=self.collection.find_one({"id":ctx.author.id, "guild_id": ctx.guild.id})['limoncoin'],
				inline=False
				)
			emb.add_field(
				name="KiwiCoin:",
				value=self.collection.find_one({'id':ctx.author.id, 'guild_id':ctx.guild.id})['cash']
				)
			await ctx.send(embed=emb)
	@commands.command(aliases=['addmoney'])
	@commands.has_permissions(administrator=True)
	async def award(self, ctx, member:discord.Member=None, amount:int = None, val = None):
		lim = self.collection.find_one({"id":ctx.author.id, "guild_id": ctx.guild.id})['limoncoin']
		Kiwi = self.collection.find_one({"id":ctx.author.id, "guild_id": ctx.guild.id})['cash']
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
					self.collection.update_one({"id":member.id, "guild_id": ctx.guild.id}, {"$set": {"coin": Kiwi + amount}})
					await ctx.send(
						embed=discord.Embed(
							title="Успешно",
							description=f"Вы пополнили баланс пользователю {member.name}",
							colour=discord.Member.color
							)
						)
				elif val == 'limoncoin':
					self.collection.update_one({"id":member.id, "guild_id": ctx.guild.id}, {"$set": {"limoncoin": lim + amount}})
					await ctx.send(
						embed=discord.Embed(
							title="Успешно",
							description=f"Вы пополнили баланс пользователю {member.name}",
							colour=discord.Member.color
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
	# @commands.command(aliases=['осебе'])
	# async def osebe(self, ctx, *, text = None):
	# 	members = {
	# 		'member_id':ctx.author.id,
	# 		'info': f'Расскажите о себе',
	# 		'second_half': 'Нету'
	# 		}
	# 	if userinfo.count_documents({'member_id':ctx.author.id})==0:
	# 		userinfo.insert_one(members)
	# 	if text is None:
	# 		await ctx.sned(
	# 			embed=discord.Embed(
	# 				title="О себе",
	# 				description="Вы не указали текст",
	# 				colour=discord.Color.red()
	# 				)
	# 			)
	# 	else:
	# 		if len(text) > 200:
	# 			await ctx.send(
	# 				embed=discord.Embed(
	# 					title="Осебе",
	# 					description="В вашей биографии не может быть больше 200 символов"
	# 					)
	# 				)
	# 		else:
	# 			self.userinfo.update_one({"member_id":ctx.author.id}, {"$set": {"info": text}})
	# 			await ctx.send(
	# 				embed=discord.Embed(

	# 					title="Успешно",
	# 					description="Вы успешно поменяли свою биографию на {}".format(text),
	# 					colour=discord.Color.red()
	# 					)
	# 				)

def setup(client):
	client.add_cog(Econom(client))