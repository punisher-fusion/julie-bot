import discord
from discord.ext import commands
import requests
import json
import time
import datetime
COLOUR = 0x008080

class APIs():
	def __init__(self, client):
		self.client = client

	@commands.command(aliases=['filmes', 'buscfilme'])
	async def filme(self, ctx):
		try:
			msg = ctx.message.content[8:]
			api = f'http://www.omdbapi.com/?apikey=3adede76&t={msg}'
			api_url = requests.get(api)
			filme = json.loads(api_url.text)
			embed = discord.Embed(
			color=COLOUR,
			timestamp= datetime.datetime.utcnow(),
			description=f'**Vamos ver as informações do filme {msg}!**'
)
			embed.add_field(name='Título:', value=str(filme['Title']))
			embed.add_field(name='Ano:', value=str(filme['Year']))
			embed.add_field(name='Avaliação:', value=str(filme['Rated']))
			embed.add_field(name='Lançado:', value=(filme['Released']))
			embed.add_field(name='Duração:', value=(filme['Runtime']))
			embed.add_field(name='Diretor:', value=str(filme['Director']))
			embed.add_field(name='Escritor:', value=str(filme['Writer']))
			embed.add_field(name='WebSite:', value=str(filme['Website']))
			embed.add_field(name='Atores:', value=str(filme['Actors']))
			embed.add_field(name='Linguagem:', value=str(filme['Language']))
			embed.add_field(name='País:', value=str(filme['Country']))
			embed.add_field(name='Prêmios:', value=str(filme['Awards']))
			embed.add_field(name='Classificações:', value=str(filme['imdbRating']))
			embed.add_field(name='Votos:', value=(filme['imdbVotes']))
			embed.add_field(name='Ganhos:', value=(filme['BoxOffice']))
			embed.add_field(name='Produção:', value=str(filme['Production']))
			embed.add_field(name='Genêro:', value=str(filme['Genre']))
			embed.set_thumbnail(url=str(filme['Poster']))
			await ctx.send(embed=embed)
		except:
			await ctx.message.delete()

def setup(client):
	print('[Comando Filme] Carregada!')
	client.add_cog(APIs(client))