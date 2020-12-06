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
			value="wiki, userinfo, server, bot, roleinfo, spotify, ping, ava, weather, google, say,  report",
			inline=False
			)
		emb.add_field(
			name="Модерация",
			value="clear, say, poll, mute, slowmode, unmute, ban, kick, prefix, report-channel, welcome",
			inline=False
			)
		emb.add_field(
			name="Фан",
			value="8ball, img, anekdot, fox, cat, dog",
			inline=False
			)
		emb.add_field(
			name="Экономиика",
			value="balance, award, take",
			inline=False
			)
		emb.set_footer(text=f"При баге {ctx.prefix}bugs <bug>, при новой идеии {ctx.prefix}idea <idea>")
		emb.set_author(name=f"Префикс: {ctx.prefix}")
		await ctx.send(embed=emb)

def setup(client):
	client.add_cog(Help(client))