#imports
from bs4 import BeautifulSoup
from discord.ext import commands, tasks
from itertools import cycle #pip install more-itertools
from discord import Spotify, Embed, Role, Color
from datetime import datetime
from requests import get
import io
import aiohttp
import datetime
import discord #pip install discord.py
import datetime
import json
import random
import requests
import wikipedia
import asyncio
import os
import youtube_dl
"""
wiki 'вики', 'wiki', "wikipedia", "википедия"+
userinfo "userinfo", "user", "юзер"+
server "сервер", "serverinfo"+
roleinfo "roleinfo", "role", "рольинфо"+
spotify "spotify", "спотифай"+
ping +
ava 'ava', 'avatar'+
weather "погода" +
google +
"""
class Utilite(commands.Cog):
	"""docstring for User"""
	def __init__(self, client):
		self.client = client
	@commands.command(
		name="Аватар",
		aliases=['ava', 'avatar'],
		brief="Увеличеный аватар пользователя",
		usage="ava <@user>"
		)
	async def avatar(self, ctx, member:discord.Member = None):
		try:
			if member is None:
				member = ctx.author
			emb = discord.Embed(
				title=f"Увеличеный аватар пользователя {member.name}",
				colour=discord.Color.purple()
				)
			emb.set_image(url=member.avatar_url)
			await ctx.send(embed=emb)
		except:
			await ctx.send(
				embed=discord.Embed(
					title="Аватар пользователя",
					description="Что то не получилось .-.",
					colour=discord.Color.red()
					)
				)
	@avatar.error
	async def avatar_error(self, ctx, error):
		if isinstance(error, commands.UserInputError):
			await ctx.send(
				embed=discord.Embed(
					title="Аватар пользователя",
					description="Вы не правильно указали имя пользователя!",
					colour=discord.Color.red()
					)
				)
	@commands.command()
	async def ping(self, ctx):
		ping = self.client.latency
		ping_emoji = "🟩🔳🔳🔳🔳"
		
		ping_list = [
			{"ping": 0.10000000000000000, "emoji": "🟧🟩🔳🔳🔳"},
			{"ping": 0.15000000000000000, "emoji": "🟥🟧🟩🔳🔳"},
			{"ping": 0.20000000000000000, "emoji": "🟥🟥🟧🟩🔳"},
			{"ping": 0.25000000000000000, "emoji": "🟥🟥🟥🟧🟩"},
			{"ping": 0.30000000000000000, "emoji": "🟥🟥🟥🟥🟧"},
			{"ping": 0.35000000000000000, "emoji": "🟥🟥🟥🟥🟥"}]
		
		for ping_one in ping_list:
			if ping > ping_one["ping"]:
				ping_emoji = ping_one["emoji"]
				break

		message = await ctx.send("Пожалуйста, подождите. . .")
		emb = Embed(
			title="Понг!",
			colour=Color.blue()
		)
		emb.add_field(
			name="Пинг бота",
			value=f"{ping * 1000:.0f}mc"
			)
		emb.set_footer(text=f"{ping_emoji}")
		await message.edit(embed=emb)
	@commands.command(
		name="Spotify",
		aliases=["spotify", "спотифай"],
		usage="spotify <@user>",
		brief="Узнать доп информацию о музыке которую слушает пользователь"
		)
	async def spotify(self, ctx, member: discord.Member = None):
		def strfdelta(tdelta, fmt):
			d = {"days": tdelta.days}
			d["hours"], rem = divmod(tdelta.seconds, 3600)
			d["minutes"], d["seconds"] = divmod(rem, 60)
			return fmt.format(**d)
		member = member or ctx.author

		spot = next((activity for activity in member.activities if isinstance(activity, discord.Spotify)), None)

		if not spot:
			return await ctx.send(f"{member.mention}, не слушает Spotify :mute:")
		starttime = spot.created_at
		endttime = spot.end
		start = spot.start
		starts = start.strftime('%H:%M %d.%m.%Yг')
		endtime = endttime.strftime('%H:%M %d.%m.%Yг')
		sttime = starttime.strftime('%H:%M %d.%m.%Yг')
		embed = discord.Embed(title = f"{member} слушает Spotify :notes:", color = spot.color)

		embed.add_field(
			name = "Песня", 
			value = spot.title, 
			inline=False)
		embed.add_field(
			name = "Исполнитель", 
			value = spot.artist, 
			inline=False)
		embed.add_field(
			name = "Альбом", 
			value = spot.album, 
			inline=False)
		embed.add_field(
			name = "Пати айди", 
			value = spot.party_id[8:], 
			inline=False)
		embed.add_field(
			name = "Трек айди", 
			value = spot.track_id, 
			inline=False)
		embed.add_field(
			name = "Длительность аудио", 
			value = strfdelta(spot.duration, '{hours:02}:{minutes:02}:{seconds:02}'), inline=False)
		embed.add_field(
			name="Начал слушать песню",
			value='{}'.format(starts), 
			inline=False)
		embed.add_field(
			name="Закончит слушать песню", 
			value='{}'.format(endtime), 
			inline=False)
		embed.add_field(
			name="Начал слушать", 
			value='{}'.format(sttime), inline=False)
		embed.set_thumbnail(url = spot.album_cover_url)

		await ctx.send(embed = embed)
	@commands.command(name="Роль инфо",
		aliases=["roleinfo", "role", "рольинфо"],
		usage="roleinfo <@role>",
		brief="Инфа о роли"
		)
	async def roleinfo(self, ctx, role: discord.Role=None):
		date = role.created_at
		dates = date.strftime('%d.%m.%Y')
		if role is None:
			await ctx.send(embed=discord.Embed(
				title="Информация о роли",
				description="Вы не указали роль!",
				colour=discord.Color.red()))
		else:
			try:
				guild=ctx.guild
				emb=discord.Embed(
					title='Информация о роли {}'.format(role.name),
					colour=role.color)
				emb.add_field(
					name='Роль создана',
					value='{}'.format(dates)
					)
				emb.add_field(name='Название роли', 
					value=role.name, 
					inline=False)
				emb.add_field(name='Айди роли', 
					value=role.id, 
					inline=False)
				emb.add_field(name="Количество пользователей с этой ролью",
					value=len(role.members),
					inline=False)
				emb.add_field(name='Позиция роли', value=role.position)
				await ctx.send(embed=emb)
			except:
				await ctx.send(
					embed=discord.Embed(
						title="Информация о роли",
						description="Упс, похоже что то пошло не так",
						colour=discord.Color.red()
						)
					)
	@roleinfo.error
	async def roleinfo_error(self, ctx, error):
		if isinstance(error, commands.UserInputError):
			await ctx.send(
				embed=discord.Embed(
					title="Информация о роли",
					description="Вы не правильно указали роль!",
					colour=discord.Color.red()
					)
				)
	@commands.command(aliases=["сервер", "serverinfo"])
	async def server(self, ctx):
		online = len(list(filter(lambda m: m.status == discord.Status.online, ctx.guild.members)))
		offline = len(list(filter(lambda m: m.status == discord.Status.offline, ctx.guild.members)))
		dnd = len(list(filter(lambda m: m.status == discord.Status.do_not_disturb, ctx.guild.members)))
		idle = len(list(filter(lambda m: m.status == discord.Status.idle, ctx.guild.members)))
		voice = len(ctx.guild.voice_channels)
		textchans = len(ctx.guild.text_channels) 
		channels = len(ctx.guild.channels)
		allmembers = ctx.guild.member_count
		date = ctx.guild.created_at
		dates = date.strftime('%H:%M %d.%m.%Yг')
		reg = {
			"russia":"🇷🇺 Россия",
			"brazil":"🇧🇷 Бразилия",
			"europe":"🇪🇺 Европа",
			"hongkong":"🇭🇰 Гонконг",
			"india":"🇮🇳 Индия",
			"japan":"🇯🇵 Япония",
			"singapore":"🇸🇬 Сингапур",
			"sydney":"🇦🇺 Сидней",
			"southafrica":"🇿🇦 Южно-Африканская республика",
			"us-central":"🇺🇸 Центр США",
			"us-east":"🇺🇸 Восток США",
			"us-south":"🇺🇸 Юг США",
			"us-west":"🇺🇸 Запад США"
		}
		emb = discord.Embed(
			title=f"Информация о сервере {ctx.guild.name}",
			colour=discord.Color.red()
			)
		emb.add_field(
			name="Создатель",
			value=f"{ctx.guild.owner}"
			)
		emb.add_field(
			name="Имя сервера",
			value=ctx.guild.name
			)
		emb.add_field(
			name="Айди сервера",
			value=ctx.guild.id,
			inline=False
			)
		emb.add_field(
			name = "Участники",
			value= f"""Всех: {allmembers}
Ботов: {len(list(filter(lambda m: m.bot, ctx.guild.members)))}
Участников: {len(list(filter(lambda m: not(m.bot), ctx.guild.members)))}""")
		emb.add_field(
			name = "По статусам",
			value= f"""<:online:780463989019901992>Онлайн: {online}
<:idle:780464095899811840>Не активен: {idle}
<:dnd:780464026143555644>Не беспокоить: {dnd}
<:offline:780464057390989322>Оффлайн: {offline}"""
			)
		emb.add_field(
			name="Каналы:",
			value=f"""Текстовых: {textchans}
Голосовых: {voice}
Всего: {channels}""",
		inline=False
			)
		

		emb.add_field(
			name="Регион сервера",
			value=reg[str(ctx.guild.region)]
		)
		system_channel = ctx.guild.system_channel
		if str(ctx.guild.system_channel) == "None":
			system_channel = "Неуказано"
			
		emb.add_field(
			name="Системный канал",
			value=system_channel
		)		
		emb.add_field(
			name="Бустов на сервере",
			value=len(ctx.guild.premium_subscribers)
			)
		emb.add_field(
			name="Всего ролей на сервере ",
			value=len(ctx.guild.roles)
			)
		verlvl = {
			"low":"Низкий",
			"medium":"Средний",
			"high":"Высокий",
			"extreme":"Самый высокий",
			"none":"Нету"
		}

		emb.add_field(
			name="Уровень проверки",
			value=verlvl[str(ctx.guild.verification_level)]
			)
		emb.set_footer(text="Дата создания {}".format(dates))
		emb.set_thumbnail(url=ctx.guild.icon_url)
		await ctx.send(embed=emb)
	@commands.command(
		name="Инфа о пользователе",
		aliases=["userinfo", "user", "юзер"],
		usage="userinfo <@user>",
		brief="Инфа о пользователе" 
		)
	async def userinfo(self, ctx, member:discord.Member=None):
		
		
		member = member or ctx.author
		joined = member.joined_at
		cr = member.created_at
		created = cr.strftime('%H:%M %d.%m.%Yг')
		join = joined.strftime('%H:%M %d.%m.%Yг')
		try:
			emb = Embed(
				title=f"Инфа о пользователе {member}",
				colour=member.color
				)
			emb.set_thumbnail(url=member.avatar_url)
			stik = {
				"dnd":"<:dnd:780464026143555644>Не беспокоить",
				"idle":"<:idle:780464095899811840>Не активен",
				"offline":"<:offline:780464057390989322>Оффлайн",
				"online":"<:online:780463989019901992>Онлайн"
			}
			emb.add_field(
				name="Статус пользователя",
				value=stik[str(member.status)],
				inline=False
				)
			emb.add_field(
				name="Имя пользователя",
				value=str(member.name)
				)
			emb.add_field(
				name="Тег пользователя",
				value=str(member.discriminator)
				)
			emb.add_field(
				name="Имя на сервере",
				value=str(member.display_name)
				)
			emb.add_field(
				name="Даты",
				value=f"""👋 Зашел: {join}
😎 Создал аккаунт: {created}""",
				inline=False)
			emb.add_field(name="Высшая роль", 
				value=f"{member.top_role.mention}")
			emb.add_field(
				name="Всего ролей",
				value=len(member.roles)
				)
			emb.set_footer(text=f"ID: {member.id}")
			await ctx.send(embed=emb)

		except:
			await ctx.send(
				embed= discord.Embed(
					title="Информация о пользователе",
					description="Мы не смогли собрать информацию о пользователе :(",
					colour=Color.red()
					)
				)
	@userinfo.error
	async def userinfo_error(self, ctx, error):
		if isinstance(error, commands.UserInputError):
			await ctx.send(
				embed=discord.Embed(
					title="Информация о пользователе",
					description="Вы не правильно указали имя пользователя!",
					colour=discord.Color.red()
					))
	@commands.command(
		aliases=['вики', 'wiki', "wikipedia", "википедия"],
		description='узнать информацию на вики',
		usage='вики <информация>'
	)
	async def _wiki(self, ctx, *, text=None):
		if text is None:
			await ctx.send(
				embed=discord.Embed(
					title="Найти в википедии",
					description="Вы не указали запрос который хотите найти",
					color=0x00ffff
					)
				)
		else:
			try:
				wikipedia.set_lang("ru")
				new_page = wikipedia.page(text)
				summ = wikipedia.summary(text)
				emb = Embed(
					title= new_page.title,
					description= summ,
					color = 0x00ffff
				 )
				emb.set_author(name= 'Больше информации тут!', url= new_page.url, icon_url= 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png%27')

				await ctx.send(embed=emb)
			except:
				await ctx.send(
					embed=Embed(
						title="Найти в википедии",
						description="Мы не смогли найти ничего по вашему запросу :(",
						color=0x00ffff
						)
					)

	@commands.command(aliases=["погода"])
	async def weather(self, ctx,  *, place = None):
		try:
			if place is None:
				await ctx.send(
					embed = Embed(
						title="🌤️Погода",
						description="Вы не указали город!",
						colour=Color.red()
						)
					)
			else:
				data = get(f"http://api.openweathermap.org/data/2.5/weather?q={place}&units=metric&APPID=fb9df86d9c484eba8a69269cfb0beac9&lang=ru").json()
				cleared_data = {
					'Место': data['name'],
					'Погода': f"{data['weather'][0]['description']}",
					'Температура': f"{data['main']['temp']}°C",
					'Ощущаеться как': f"{data['main']['feels_like']}°C",
					'Минимальная температура': f"{data['main']['temp_min']}°C",
					'Макисмальная температура': f"{data['main']['temp_max']}°C",
					'Влажность': f"{data['main']['humidity']}%",
					'Облака': f"{data['clouds']['all']}%",
					'Ветер': f"{data['wind']['speed']} м/с",
				}
				embed = Embed(
					title = f"🌤️ Погода в {cleared_data['Место']}", 
					color = 0x3498db
					)
				for key, value in cleared_data.items():
					embed.add_field(
						name = key, 
						value = value
						)
				await ctx.send(embed = embed)
		except:
			await ctx.send(
				embed=Embed(
					title="🌤️Погода",
					description=f'Мы несмоли найти данные о погоде в городе "{place}"',
					colour=Color.red()
					)
				)
	@commands.command()
	async def google(self, ctx, *, question = None):
		if question is None:
			await ctx.send('Введите запрос!')
		else:
			await ctx.send('Подождите!')

			url = f'https://www.google.com/search?b-d&q=' + str(question).replace(' ', '+')
			headers = {
				'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
				'accept': '*/*'
			}

			r = requests.get(url, headers = headers)
			soup = BeautifulSoup(r.content, 'html.parser')
			items = soup.findAll('div', class_ = "rc")

			comps = []

			for item in items:
				comps.append({
						'link': item.find('a').get('href'),
						'title': item.find('h3', class_ = 'LC20lb DKV0Md').get_text(strip = True)
					})
				await asyncio.sleep(3)

			emb = discord.Embed(colour=Color.blue())
			
			counter = 0
			for comp in comps:
				counter += 1

				emb.add_field(
						name = f'[{counter}]	> #'  + comp['title'],

						value =  '| ' + comp['link'],
						inline = False
					)


			emb.set_author(name = '{}'.format(ctx.author), icon_url = '{}'.format(ctx.author.avatar_url))
			await ctx.send(embed = emb)
	@commands.command(aliases=['сказать'])
	@commands.has_permissions(manage_messages=True)
	async def say(self, ctx, *, arg=None):
		await ctx.message.delete()
		try:
			if arg is None:
				await ctx.send(
					embed=Embed(
						title="Сказать",
						description="Вы не ввели сообщение",
						colour=Color.red()
						)
					)
			else:
				files = []
				for file in ctx.message.attachments:
					fp = io.BytesIO()
					await file.save(fp)
					files.append(discord.File(fp, filename = file.filename, spoiler = file.is_spoiler()))
				await ctx.send(files = files, content=arg)
		except:
			await ctx.send(
				embed=Embed(
					title="Сказать",
					description="Что то пошло не так...",
					colour=Color.red()
					)
				)
	@say.error
	async def say_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send(embed=discord.Embed(
				title=':x:Ошибка',
				description=f"""Недостаточно прав для использования команды say
	Нужные права: Управлять сообщениями""", 
				colour=discord.Color.red()),
				delete_after=10
				)
	@commands.command()
	@commands.has_permissions(manage_channels=True)
	async def slowmode(self, ctx, value:int=None):
		if value is None:
			embed = discord.Embed(title="Слоумод",
				description=f"Укажите кол-во секунд `{ctx.prefix}slowmode <value>`", 
				color=discord.Color.red())
			await ctx.send(embed=embed)
		elif value > 21600:
			embed = discord.Embed(title="Ошибка", description="Максимальное кол-во секунд: 21600", color=discord.Color.red())
			await ctx.send(embed=embed)
		else:
			channel = ctx.channel
			await channel.edit(slowmode_delay=value)

			if value == 1:
				sec = 'секунду'
			elif value == 2 or value == 3 or value == 4:
				sec = 'секунды'
			else:
				sec = 'секунд'

			embed = discord.Embed(title="Слоумод", description=f"Поставлен слоумод на **{value}** {sec}, в {ctx.channel.mention}", color=discord.Color.green())
			await ctx.send(embed=embed)
	@commands.command()
	async def bot(self, ctx):
		emb = discord.Embed(
			colour=discord.Color.gold()
			)
		emb.add_field(
			name="Меня зовут LimonixBot",
			value=f"""Я основан на языке: Python
Меня создал: {self.client.owner},
Я состою на {len(self.client.guilds)}
Всего пользователей: {len(set(self.client.get_all_members()))}
			"""
			)
		emb.set_thumbnail(url=self.client.user.avatar_url)
		await ctx.send(embed=emb)

	# @commands.command()
	# async def test(self, ctx):

	# 	file = discord.File("./fortnite.jpg", filename="fortnite.jpg")
	# 	embed = discord.Embed(
	# 		title="gg"
	# 		)
	# 	embed.set_image(url="attachment://fortnite.jpg")
	# 	await ctx.send(file=file, embed=embed)
def setup(client):
	client.add_cog(Utilite(client))