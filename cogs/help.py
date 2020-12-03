from discord.ext import commands
import discord
class Help(commands.Cog):
	"""docstring for User"""
	def __init__(self, client):
		self.client = client
	@commands.command()
	async def help(self, ctx):
		emb = discord.Embed(
			title="Список комманд",
			colour=discord.Color.blue()
			)
		emb.add_field(
			name="Утилиты",
			value="wiki, userinfo, server, roleinfo, spotify, ping, ava, weather, google, say",
			inline=False
			)
		emb.add_field(
			name="Модерация",
			value="clear, say, poll, mute, unmute, ban, kick",
			inline=False
			)
		emb.add_field(
			name="Фан",
			value="8ball, img, anekdot, fox, cat, dog"
			)
		emb.set_footer(text="При баге !bugs <bug>, при новой идеии !idea <idea>")
		emb.set_author(name="Префикс: !")
		await ctx.send(embed=emb)

def setup(client):
	client.add_cog(Help(client))