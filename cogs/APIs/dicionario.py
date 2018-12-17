import discord
from discord.ext import commands
import json
import requests
COLOUR = 0x008080

class dic():
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def dic(self, ctx):
		msg = ctx.message.content.split(' ')[1:]
		#api = f'http://dicionario-aberto.net/search-json/{msg}'
		api_url = requests.get(f'http://dicionario-aberto.net/search-json/{msg}')
		a = json.loads(api_url.text)
		sig = (str['articles'][0]['def'])
		a = discord.Embed(color=COLOUR)
		a.add_field(name='Significado:', value=sig)
		await ctx.send(embed=a)



def setup(client):
	print('[Comando Dicionário] Carregada!')
	client.add_cog(dic(client))
