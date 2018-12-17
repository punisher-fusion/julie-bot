import discord
from discord.ext import commands
COLOUR = 0x008080

class load():
	def __init__(self, client):
		self.client = client

	@commands.command(name='reload', aliases=['recarregar', 'rld'])
	async def load(self, ctx, ext:str):
		try:
			self.client.load_extension(ext)
			embed = discord.Embed(
				color=COLOUR,
				description=f'{ext} recarregada com Sucesso!'
				)
			await ctx.send(embed=embed)
		except:
			await ctx.send('Erro 190')

def setup(client):
	print('[Comando Recarregar] Carregada!')
	client.add_cog(load(client))

