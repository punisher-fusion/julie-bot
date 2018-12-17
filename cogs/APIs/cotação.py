import discord
from discord.ext import commands
import time
import datetime
import requests
import json
COLOUR = 0x008080

class api():
	def __init__(self, client):
		self.client = client

	@commands.command(name='dolar', aliases=['dol', 'do', 'dolr', 'euro', 'bitcoin', 'bit'])
	async def valor(self, ctx):
		api_url = requests.get('https://api.hgbrasil.com/finance?key=e87e079e')
		a = json.loads(api_url.text)

		dol = (str(a['results'][0]['buy']))

		e = discord.Embed(color=COLOUR)
		e.add_field(name='Dolar:', value=dol)
		await ctx.send(embed=e)

def setup(client):
	print('[Comando Cotação] Carregada!')
	client.add_cog(api(client))
