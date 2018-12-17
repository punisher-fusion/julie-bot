import discord
from discord.ext import commands
import time
import datetime
COLOUR = 0x008080

class tabuada():
	def __init__(self, client):
		self.client = client

	@commands.command(name='tabuada', aliases=['tabu'])
	async def tabuada(self, ctx):
		try:
			arg = ctx.message.content.split(' ')
			msg = " ".join(arg[1:])
			a = '-'
			emb = discord.Embed(color=COLOUR, description=
			f'{str(a)*13}\n'
			f'**{int(msg)} x 1 =   {int(msg)*1}\n'
			f'{int(msg)} x 2 =  {int(msg)*2}\n'
			f'{int(msg)} x 3 =  {int(msg)*3}\n'
			f'{int(msg)} x 4 =  {int(msg)*4}\n'
			f'{int(msg)} x 5 =  {int(msg)*5}\n'
			f'{int(msg)} x 6 =  {int(msg)*6}\n'
			f'{int(msg)} x 7 =  {int(msg)*7}\n'
			f'{int(msg)} x 8 =  {int(msg)*8}\n'
			f'{int(msg)} x 9 =  {int(msg)*9}\n'
			f'{int(msg)} x 10 = {int(msg)*10}\n**'
			f'{str(a)*13}')
			emb.set_thumbnail(url='https://i.imgur.com/Segqv0s.png')
			await ctx.send(embed=emb)
		except:	
			erro = discord.Embed(color=0xFF0000, description=f'<:xx:520666345474621451> **{ctx.author.name}, você não pode Escrever uma Letra ou usar vírgulas! (Obs: Somente Números Inteiros!)**')
			await ctx.send(embed=erro)

def setup(client):
	print('[Comando Tabuada] Carregada!')
	client.add_cog(tabuada(client))

