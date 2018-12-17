import discord
from discord.ext import commands
import time
import datetime
COLOUR = 0x008080

class ping():
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def ping(self, ctx):
		aa = time.perf_counter()
		bb = time.perf_counter()

		a = discord.Embed(color=COLOUR)
		a.add_field(name='<a:cursor:507925560333434890>Shard 0:', value=round(self.client.latencies[0][1]*1000))
		a.add_field(name='<a:cursor:507925560333434890>Shard 1:', value=round(self.client.latencies[1][1]*1000))
		a.set_thumbnail(url='https://cdn.icon-icons.com/icons2/1633/PNG/128/52744pingpong_109378.png')
		await ctx.send(embed=a)

def setup(client):
	print('[Comando Ping] Carregada!')
	client.add_cog(ping(client))

