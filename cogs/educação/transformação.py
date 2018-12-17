import discord
from discord.ext import commands
import time
import datetime
COLOUR = 0x008080

class matematica():
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def transformar(self, ctx):
		try:
			msg = ctx.message.content.split(' ')[1]
			result = int(msg)*60
			embed = discord.Embed(
			color = COLOUR,
			timestamp = datetime.datetime.utcnow(),
			)
			embed.add_field(name='Minuto(s):', value=msg)
			embed.add_field(name='Segundo(s):', value=result)
			embed.set_thumbnail(url='https://i.imgur.com/Segqv0s.png')
			embed.add_field(name='Geral:', value=f'**Olá {ctx.author.name}, {msg} minutos é igual a {result} segundos!**')
			await ctx.send(embed=embed)
		except:
			await ctx.send('**Somente números!**')

def setup(client):
	print('[Comando Transformação] Carregada!')
	client.add_cog(matematica(client))