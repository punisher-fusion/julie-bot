import discord
from discord.ext import commands
import random
import time
import datetime
COLOUR = 0x008080

class roll():
	def __init__(self, client):
		self.client = client

	@commands.command(aliases=['moeda'])
	async def roll (self, ctx):
		moedinha = ['Cara:grinning:', 'Coroa:crown:']
		escolha = random.choice(moedinha)
		moeda = discord.Embed(
			title='Cara ou coroa?', 
			color=COLOUR, 
			timestamp=datetime.datetime.utcnow(),
			description=f'**{ctx.author.name}**, a **moeda** caiu na **{escolha}**'
			)
		moeda.set_thumbnail(url='http://marketingcomdigital.com.br/lp/wp-content/uploads/2015/08/um-real.png')
		await ctx.send(embed=moeda)

def setup(client):
	print('[Comando Roll] Carregada!')
	client.add_cog(roll(client))