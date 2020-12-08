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
class Eve(commands.Cog):
	"""docstring for User"""
	def __init__(self, client):
		self.client = client
		self.prefix = MongoClient("mongodb+srv://limonix:1q234567wE@cluster0.tthbn.mongodb.net/Guild?retryWrites=true&w=majority")
		self.prefixes = self.prefix.Guild.prefixes
	@commands.Cog.listener()
	async def on_ready(self):
		print("Event cog connect")
	@commands.Cog.listener()
	async def on_member_join(self, member):
		idc = self.prefixes.find_one({"_guild_id": member.guild.id})["welcome"]
		if idc == 0:
			pass
		else:
			channel=self.client.get_channel(int(idc))
			
			embb = discord.Embed(
				title=f"{member.name}, добро пожаловать!",
				colour=discord.Color.gold(), 
				description=f"""**Поприветствуем** нового участника сервера.
Его зовут {member}.
Он уже {member.guild.member_count} участник нашего сервера!""")
			embb.set_footer(text=f"Сервер: {member.guild.name}")
			embb.set_thumbnail(url=member.avatar_url)
			embb.set_image(url="https://i.ibb.co/drPZW7d/hello.gif")
			await channel.send( embed=embb)
	@commands.Cog.listener()
	async def on_member_remove(self, member):
		idc = self.prefixes.find_one({"_guild_id": member.guild.id})["leave"]
		if idc == 0:
			pass
		else:
			channel=self.client.get_channel(int(idc))
			
			embb = discord.Embed(
				title=f"{member.name}, прощай:(",
				colour=discord.Color.gold(), 
				description=f"""Нас покинул один человек
Его зовут {member}.
Что ему у нас не понравилось?""")
			embb.set_footer(text=f"Сервер: {member.guild.name}")
			embb.set_thumbnail(url=member.avatar_url)
			
			await channel.send( embed=embb)
	@commands.Cog.listener()
	async def on_member_update(self, member, after, before):
		spot = next((activity for activity in member.activities if isinstance(activity, discord.Spotify)), None)
		if after.status == after.spot:
			await member.add_roles(758558503987445772)
	# @commands.Cog.listener()
	# async def on_typing(self, channel, user, when):
	# 	date = when.strftime("%d/%m/%Y %H:%M %p")

	# 	await channel.send(f"\nThe user is typing. . .\n\n"
	# 					   f"User - {user}\n"
	# 					   f"Channel - {channel.mention}\n"
	# 					   f"When - {date}")
def setup(client):
	client.add_cog(Eve(client))