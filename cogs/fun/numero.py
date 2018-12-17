import discord
from discord.ext import commands
import random
import time
import datetime
COLOUR = 0x008080

class numero():
	def __init__(self, client):
		self.client = client

	@commands.command(aliases=['n'])
	async def numero(self, ctx):
		escolha1 = random.randint(1,9)
		escolha2 = random.randint(1,9)
		escolha3 = random.randint(1,9)
		escolha4 = random.randint(1,9)
		escolha5 = random.randint(1,9)
		escolha6 = random.randint(1,9)
		numero = discord.Embed(
			title='Veja os Números sorteados:',
			color=COLOUR,
			timestamp=datetime.datetime.utcnow()
			)
		numero.add_field(name='Números:',value=f'{escolha1} {escolha2} {escolha3} {escolha4} {escolha5} {escolha6}')
		await ctx.send(embed=numero)


def setup(client):
	print('[Comando Número] Carregada!')
	client.add_cog(numero(client))