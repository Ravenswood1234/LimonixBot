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

def setup(client):
	client.add_cog(Econom(client))