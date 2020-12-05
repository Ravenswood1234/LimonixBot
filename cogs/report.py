from discord.ext import commands, tasks
from itertools import cycle 
from datetime import datetime
from pymongo import MongoClient
import datetime
import io
import discord
import os
import traceback
class Report(commands.Cog):
	"""docstring for User"""
	def __init__(self, client):
		self.client = client
		self.coll = MongoClient("mongodb+srv://limonix:1q234567wE@cluster0.tthbn.mongodb.net/report_system?retryWrites=true&w=majority")
		self.coll3 = self.coll.report_system.system
	@commands.command(aliases=['report-channel', 'reports-channel', 'reports_channel', 'канал-жалоб'])
	@commands.has_permissions(administrator=True)
	async def report_channel(self, ctx, on_off=None, channel: discord.TextChannel=None):
		if on_off is None:
			embed = discord.Embed(title="Ошибка", description=f"Укажите включение/выключение системы жалоб `{ctx.prefix}report-channel <on/off> <channel>`", color=discord.Color.red())
			await ctx.send(embed=embed)
		elif on_off == 'off':
			if not self.coll3.find_one({"guild_id": ctx.guild.id}):
				embed = discord.Embed(title="Ошибка", 
					description=f"Невозможно отключить систему жалоб!\nСистема жалоб не включена", 
					color=discord.Color.red())
				await ctx.send(embed=embed)
			else:
				embed = discord.Embed(title="Система Жалоб", description=f"Система для жалоб успешно выключена на данном сервере!", color=discord.Color.green())
				await ctx.send(embed=embed)
				self.coll3.delete_one({"guild_id": ctx.guild.id})
		elif on_off == 'on':
			if channel is None:
				embed = discord.Embed(title="Ошибка", description=f"Укажите канал для жалоб `{ctx.prefix}report-channel <on/off> <channel>`", color=discord.Color.red())
				await ctx.send(embed=embed)
			else:
				if not self.coll3.find_one({"guild_id": ctx.guild.id}):
					embed = discord.Embed(title="Канал Жалоб", description=f"Канал для жалоб успешно задан - {channel.mention}", color=discord.Color.green())
					await ctx.send(embed=embed)
					self.coll3.insert_one({"guild_id": ctx.guild.id, "channel_id": channel.id})
				else:
					self.coll3.delete_one({"guild_id": ctx.guild.id})
					self.coll3.insert_one({"guild_id": ctx.guild.id, "channel_id": channel.id})
					embed = discord.Embed(title="Канал Жалоб", description=f"Канал для жалоб успешно задан - {channel.mention}", color=discord.Color.green())
					await ctx.send(embed=embed)
		else:
			embed = discord.Embed(title="Ошибка", description=f"Укажите включение/выключение системы жалоб `{ctx.prefix}report-channel <on/off> <channel>`", color=discord.Color.red())
			await ctx.send(embed=embed)
	@commands.command(aliases=['жалобы', 'send-report'])
	async def report(self, ctx, member: discord.Member=None, *, reason=None):
		if not self.coll3.find_one({"guild_id": ctx.guild.id}):
			embed = discord.Embed(title="Ошибка", description=f"Система жалоб на этом сервере не включена!\nЧтобы включить введите - `{ctx.prefix}report-channel <on/off> <channel>`", color=discord.Color.red())
			await ctx.send(embed=embed)
		else:
			if member is None:
				embed = discord.Embed(title="Ошибка", description=f"Укажите пользователя `{ctx.prefix}report <member> <reason>`", color=discord.Color.red())
				await ctx.send(embed=embed)
			elif reason is None:
				embed = discord.Embed(title="Ошибка", description=f"Укажите причину жалобы `{ctx.prefix}report <member> <reason>`", color=discord.Color.red())
				await ctx.send(embed=embed)
			elif member == ctx.author:
				embed = discord.Embed(title="Ошибка", description="Вы не можете отправить жалобу на себя", color=discord.Color.red())
				await ctx.send(embed=embed)
			else:
				if ctx.message.attachments:
					for i in ctx.message.attachments:
						channelid = self.coll3.find_one({"guild_id": ctx.guild.id})["channel_id"]
						channel = ctx.guild.get_channel(channelid)
						embed = discord.Embed(title="Жалоба", description=f"Жалоба была успешно отправлена в канал для жалоб!", color=discord.Color.green())
						await ctx.send(embed=embed)
						embed2 = discord.Embed(title="Новая Жалоба!", description=f"**Отправитель:** {ctx.author.mention}\n**Нарушитель:** {member.mention}\n**Причина:** {reason}", color=discord.Color.green())
						embed2.set_image(url=i.url)
						msg = await channel.send(embed=embed2)
						await msg.add_reaction("✅")
						await msg.add_reaction("❌")
						break
				else:
					channelid = self.coll3.find_one({"guild_id": ctx.guild.id})["channel_id"]
					channel = ctx.guild.get_channel(channelid)
					embed = discord.Embed(title="Жалоба", description="Жалоба была успешно отправлена в канал для жалоб!", color=discord.Color.green())
					await ctx.send(embed=embed)
					embed2 = discord.Embed(title="Новая Жалоба!", description=f"**Отправитель:** {ctx.author.mention}\n**Нарушитель:** {member.mention}\n**Причина:** {reason}", color=discord.Color.green())
					msg = await channel.send(embed=embed2)
					await msg.add_reaction("✅")
					await msg.add_reaction("❌")
def setup(client):
	client.add_cog(Report(client))