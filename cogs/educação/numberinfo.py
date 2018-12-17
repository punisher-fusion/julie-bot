import discord
from discord.ext import commands
import time
import datetime
import random
C = [0x800080, 0xFF00FF, 0xFF69B4]
COLOUR = random.choice(C)

class info():
	def __init__(self, client):
		self.client = client

	@commands.command(name='number', aliases=['ninfo','info','numberinfo'])
	async def number(self, ctx):
		try:
			arg = ctx.message.content.split(' ')
			msg = " ".join(arg[1:])

			#ante = int(msg) - 1
			#dps = int(msg) + 1

			escolha = ('Par' if int(msg) % 2 == 0 else 'Impar')

			em = discord.Embed(color=COLOUR)
			em.add_field(name='Número:', value=int(msg))
			em.add_field(name='Antecessor:', value=int(msg)-1)
			em.add_field(name='Sucessor:', value=int(msg)+1)
			em.add_field(name='Dobro:', value=int(msg)*2)
			em.add_field(name='Triplo:', value=int(msg)*3)
			em.add_field(name='Porcentagem:', value=int(msg)%100)
			em.add_field(name='Par ou Impar:', value=escolha)
			#em.add_field(name='Em Decimal:', value='{:.2f}'.format(int(msg)/100))
			em.add_field(name='Raiz Quadrada:', value='{:.2f}'.format(int(msg)**(1/2)))
			em.set_thumbnail(url='https://i.imgur.com/Segqv0s.png')
			em.set_footer(text='Creative Commons Attribution-ShareAlike', icon_url='https://creativecommons.org/images/deed/cc_icon_white_x2.png')
			await ctx.send(embed=em)
		except:	
			erro = discord.Embed(color=0xFF0000, description=f'<:xx:520666345474621451> **{ctx.author.name}, você não pode Escrever uma Letra ou usar vírgulas! (Obs: Somente Números Inteiros!)**')
			await ctx.send(embed=erro)


def setup(client):
	print('[Comando Number] Carregada!')
	client.add_cog(info(client))