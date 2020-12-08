from requests import get
from random import choice, randint
from datetime import datetime
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
import discord
import datetime
import socket
import json
import traceback
import requests
import asyncio
import re
import io
import time


class Fun(commands.Cog, name="Фан"):
	"""docstring for User"""
	def __init__(self, client):
		self.client = client
	@commands.Cog.listener()
	async def on_ready(self):
		print("Fun cog connect")
		#rrussian_roulette
	
	@commands.command(
		name='предсказание',
		aliases=['8ball', '8BALL'],
		brief='Шар предсказаний',
		usage='8ball <question>'
		)
	async def _8ball(self, ctx, *, question=None):
		
		if question is None:
			
			await ctx.send("Укажите вопрос который хотите задать!", delete_after=10)
		else:
			
			emb=discord.Embed(title=f'Предсказание', colour=discord.Color.blue())
			emb.set_thumbnail(url='https://img.favpng.com/16/1/13/magic-8-ball-eight-ball-billiard-balls-billiards-png-favpng-8gMB1c885n0n97L2PfJSpdwSP.jpg')
			emb.add_field(name='Вопрос:', value=f'\n {question}', inline=False)
			emb.add_field(name='Ответ', value=f'\n {choice(ballsend)}', inline=False)
			emb.set_footer(text=f'{ctx.author.name} ', icon_url=ctx.author.avatar_url)
			await ctx.send(embed=emb)

	@commands.command(
		name='изображение',
		aliases=['img'],
		brief="Отправить рандомное изображение",
		usage='img'
		)
	async def random_img(self, ctx):
		random_img=['cat','dog', 'panda', 'koala', 'red_panda', "birb"]
		response = requests.get(f'https://some-random-api.ml/img/{choice(random_img)}') # Get-запрос
		json_data = json.loads(response.text) # Извлекаем JSON
		
		emb = discord.Embed(color = 0x800000, title = f'Рандомное изображение по вашему запросу') # Создание Embed'a
		emb.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
		await ctx.send(embed = emb) # Отправляем Embed
	@commands.command(
		name='лиса',
		aliases=['fox'],
		brief='Отправит рандомное изображение лисы/лиса',
		usage='fox'
		)
	async def img_fox(self,ctx):

		response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
		json_data = json.loads(response.text) # Извлекаем JSON

		embed = discord.Embed(color = 0x00FF00, title = 'Лисица по вашему запроcy') # Создание Embed'a
		embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
		
		await ctx.send(embed = embed) # Отправляем Embed
	@commands.command(
		name='собака',
		aliases=['dog'],
		brief='Отправит рандомное изображение собаки',
		usage='dog')
	async def img_dog(self,ctx):

		response = requests.get('https://some-random-api.ml/img/dog') # Get-запрос
		json_data = json.loads(response.text) # Извлекаем JSON

		embed = discord.Embed(color = 0x808000, title = 'Собака по вашему запроcy') # Создание Embed'a
		embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
		
		await ctx.send(embed = embed) # Отправляем Embed
	@commands.command(
		name='анекдот',
		aliases=['ak', 'anekdot'],
		brief='Расскажет рандомный анекдот',
		usage='ak')
	async def anekdot(self, ctx):
		emb=discord.Embed(title='', colour=discord.Color.purple())
		emb.add_field(name='😂Анекдот', value=choice(anek))

		
		await ctx.send(embed=emb)
	@commands.command(
		name='кот',
		aliases=['cat'],
		brief='Отправит рандомное изображение кота',
		usage='cat')
	async def _cat(self, ctx):
		response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
		json_data = json.loads(response.text) # Извлекаем JSON

		embed = discord.Embed(colour = 0xFF8000, title = 'Кот/кошка по вашему запроcy') # Создание Embed'a
		embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
		
		await ctx.send(embed = embed) # Отправляем Embed
	
ballsend=[
	'духи говорят "да"',
	'духи говорят "нет"',
	"может быть",
	"так точно",
	"нет",
	"я думаю нет",
	"сомневаюсь в ответе",
	"извини я не могу ответить",
	"я не знаю",
	"спроси позже",
	"ответ положительный",
	"так точно",
]
anek=[
	'Никак не можем определиться, где провести отпуск- в гостиной, в спальне или на балконе. На кухне очень дорого, очень. ',
	'Бог создавал всех людей разными, но когда дошёл до Китая, это ему надоело.',
	'– До нас жили ПРЕДки. После нас будут жить ПОТОМки. Кто мы? ТЕПЕРЬки? СЕЙЧАСки?',
	'Если у каждого врача есть свое кладбище, то у каждого преподавателя ВУЗа есть свой взвод!',
	' — Моня, я отдала твои джинсы Хаиму.\n — Это ещё в честь чего?! \n— Они же тебе всё равно не нравятся.\n — Так отдай ему ещё и свою маму!',
	'Мне кажется, что при Порошенко украинцам жилось лучше, чем сейчас. Да и россиянам тоже.',
	'Таксист клиенту: \n– Не беспокойтесь из-за запаха, это у меня просто в машине вчера пролилось кое-что. \nКлиент: \n– Ничего страшного, я уже пару дней запахов вообще не чувствую. '
	'Близкие отношения нужны только по той причине, что некоторые части тела не удается намазать фастум-гелем самостоятельно. ',
	'Аккордеон – это маленькое грустное пианино, которое надо обнимать.',
	'В баре попросили паспорт. Умилилась. Потом дошло — бармен проверяет не то, что мне уже 21, а то, что мне ещё не 65…',
	'Если ваш мужчина: \n1. Не грубит. \n2. Не пьет. \n3. Не бесит. \n4. Не сидит за компом. \n5. Не ходит с друзьями в баню. \nПотыкайте в него палкой… Походу он […]'
]
def setup(client):
	client.add_cog(Fun(client))