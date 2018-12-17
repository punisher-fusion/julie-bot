import discord
from discord.ext import commands
COLOUR = 0x008080

class unload():
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def unload(self, ctx, ext: str):
		try:
			self.client.unload_extension(ext)
			embed = discord.Embed(description=f'<a:carregando:509840579316940800> **{ext} foi Descarregada!**',
				color =COLOUR
				)
			await ctx.send(embed=embed)
		except:
			await ctx.send('Deu erro, Punisher!')




def setup(client):
	print('[Comando Descarregar] Carregada!')
	client.add_cog(unload(client))