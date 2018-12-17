import discord
from discord.ext import commands
import time
import datetime
COLOUR = 0x008080

class medidas():
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def conversao(self, ctx):
		try:
			arg = ctx.message.content.split(' ')
			msg = " ".join(arg[1:])
			a = discord.Embed(color=COLOUR)

			a.add_field(name='1-Quilômetro(s):',value=float(msg)/1000)
			a.add_field(name='2-Hectômetro(s):',value=float(msg)/100)
			a.add_field(name='3-Decâmetro(s):',value=float(msg)/10)
			a.add_field(name='4-Metro(s):', value=float(msg))
			a.add_field(name='5-Decímetro(s):',value=float(msg)*10)
			a.add_field(name='6-Centímetro(s):', value=float(msg)*100)
			a.add_field(name='7-Milímetro(s):', value=float(msg)*1000)
			a.set_thumbnail(url='https://i.imgur.com/Segqv0s.png')
			await ctx.send(embed=a)
		except:
			erro = discord.Embed(color=0xFF0000, description=f'<:xx:520666345474621451> **{ctx.author.name}, você não pode Escrever uma Letra ou usar vírgulas! (Obs: Use Pontos ao invés de vírgulas! Ex: 1.5)**')
			await ctx.send(embed=erro)

def setup(client):
	print('[Comando Conversão] Carregada!')
	client.add_cog(medidas(client))