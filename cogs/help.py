from discord.ext import commands
from Cybernator import Paginator as pag
import discord
class Help(commands.Cog):
	"""docstring for User"""
	def __init__(self, client):
		self.client = client
	@commands.command()
	async def help(self, ctx):
		cog = self.client.cogs['Экономиика']
		name = cog.qualified_name
		commands = cog.get_commands()
		embed_all = embed.Embed(
			title="Список команд",
			colour=discord.Color.green()
			)
		if name is not None:
			comm_list = []
			for command in commands:
				if not command.hidden:
					comm_list.append(f"`{ctx.prefix}{command.name}`")

			embed_all.add_field(
				name=f"Экономиика",
				value=f"{', '.join(comm_list)}",
				inline=False)
		await ctx.send(embed=embed_all)

def setup(client):
	client.add_cog(Help(client))