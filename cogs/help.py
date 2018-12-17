import discord
from discord.ext import commands
import time
import datetime
COLOUR = 0x008080

class help():
	def __init__(self, client):
		self.client = client

	@commands.command(alises=['ajuda', 'hlp'])
	async def help(self, ctx):
		convite = 'https://flamers.glitch.me/comandos.html'
		embed = discord.Embed(
		title='Abaixo você verá o link do Site do Flamers!',
		color=COLOUR,
		description='**No site, vai estar todos os Comandos Disponíveis do Flamers!**',
		timestamp = datetime.datetime.utcnow()
		)
		embed.add_field(name='Link:', value=f'[Clique Aqui.]('+ convite +')\n')
		await ctx.send(embed=embed)

def setup(client):
	print('[Comando Help] Carregado!')
	client.add_cog(help(client))