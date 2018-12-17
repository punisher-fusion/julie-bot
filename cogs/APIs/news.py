import discord
from discord.ext import commands
import json
import requests
COLOUR = 0x008080

class news():
	def __init__(self, client):
		self.client = client

	@commands.command(aliases=['noticia', 'not'])
	async def news(self, ctx):
		api_url = requests.get("https://newsapi.org/v2/top-headlines?sources=globo&apiKey=ab17916ced664de282b468260159c883")
		a = json.loads(api_url.text)
		autor = (str(a['articles'][0]['author']))
		titulo = (str(a['articles'][0]['title']))
		descrição = (str(a['articles'][0]['description']))
		publicado = (a['articles'][0]['publishedAt'])
		conteudo = (str(a['articles'][0]['content']))
		url = (a['articles'][0]['url'])
		capa = (str(a['articles'][0]['urlToImage']))

		e = discord.Embed(color=COLOUR, description=f'**Noticia do Dia!**')
		e.add_field(name='Autor:', value=autor)
		e.add_field(name='Titulo:', value=titulo)	
		e.add_field(name='Descrição:', value=descrição)
		e.add_field(name='Data:', value=publicado)
		e.add_field(name='Conteúdo:', value=conteudo)
		e.add_field(name='Noticia Completa:', value='**[Link]('+ url +')**')
		e.set_thumbnail(url=capa)
		await ctx.send(embed=e)

	@commands.command(name='bbc', aliases=['sports', 'esportes', 'BBC', 'bbcsports'])
	async def bbc(self, ctx):
		api = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-sport&apiKey=ab17916ced664de282b468260159c883")
		ba = json.loads(api.text)
		a = (str(ba['articles'][0]['author']))
		b = (str(ba['articles'][0]['title']))
		c = (str(ba['articles'][0]['description']))
		d= (ba['articles'][0]['publishedAt'])
		e = (str(ba['articles'][0]['content']))
		f = (ba['articles'][0]['url'])

		h = discord.Embed(color=COLOUR)
		h.add_field(name='Autor:', value=a)
		h.add_field(name='Titulo:', value=b)
		h.add_field(name='Descrição:', value=c)
		h.add_field(name='Data:', value=d)
		h.add_field(name='Conteúdo:', value=e)
		h.add_field(name='Noticia Completa:', value='**[Link]('+ f + ')\n**')
		
		await ctx.send(embed=h)



def setup(client):
	print('[Comando Noticias] Carregada!')
	client.add_cog(news(client))
