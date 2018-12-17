import discord
from discord.ext import commands
import time
import datetime
COLOUR = 0x008080

class dimensão():
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def parede(self, ctx):
		msg = ctx.message.content.split(' ')[1]
		arg = ctx.message.content.split(' ')
		msg1 = " ".join(arg[2])

		embed = discord.Embed(color=COLOUR)
		embed.add_field(name='Valores:')
		await ctx.send(embed=embed)

def setup(client):
	print('[Comando Dimensão] Carregada!')
	client.add_cog(dimensão(client))