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
	@commands.Cog.listener()
	async def on_ready(self):
		print("Event cog connect")
	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel=self.client.get_channel(758599386653261844)
		emb=discord.Embed(title=f"Добро пожаловать на сервер {member.guild.name}", colour=discord.Color.blue())
		emb.add_field(name="Не забудь прочитать правила в канале: ", value="<#758706739008503849>", inline=False)
		emb.add_field(name="Когда прочитал правила, можете идти общаться в канал: ", value="<#758599939151495180>", inline=False)
		emb.set_thumbnail(url='https://i.pinimg.com/originals/01/fb/2c/01fb2cb2cf0855514cf1df69f46acda8.gif')
		emb.set_image(url='https://i.pinimg.com/originals/af/80/39/af8039261a387be71514bb4c2e5e54b5.gif')
		
		
		await member.send(embed=emb)
		file = discord.File("./hello.gif", filename="hello.gif")
		embb = discord.Embed(
			title=f"{member.name}, добро пожаловать!",
			colour=discord.Color.gold(), 
			description=f"""**Поприветствуем** нового участника сервера.
Его зовут {member.mention}.
Он уже {member.guild.member_count} участник нашего сервера!""")
		embb.set_footer(text=f"Сервер: {member.guild.name}")
		embb.set_thumbnail(url=member.avatar_url)
		embb.set_image(url="attachment://hello.gif")
		await channel.send(file=file, embed=embb)
	# @commands.Cog.listener()
	# async def on_typing(self, channel, user, when):
	# 	date = when.strftime("%d/%m/%Y %H:%M %p")

	# 	await channel.send(f"\nThe user is typing. . .\n\n"
	# 					   f"User - {user}\n"
	# 					   f"Channel - {channel.mention}\n"
	# 					   f"When - {date}")
def setup(client):
	client.add_cog(Eve(client))