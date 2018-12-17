import discord
from discord.ext import commands
import random
import time
import datetime
import asyncio
COLOUR = 0x008080

class arremessar():
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def arremessar(self, ctx):
		try:
			distancia = random.randint(0, 250)
			arg = ctx.message.content.split(" ")
			msg = " ".join(arg[1:])
			gg = ['Centimetros', 'Metros', 'Quilômetros']
			km = random.choice(gg)
			vel = random.randint(5, 190)
			arremesso = discord.Embed(color=COLOUR, timestamp=datetime.datetime.utcnow())
			arremesso.add_field(name='Quem:',value=f'{ctx.author.name}')
			arremesso.add_field(name='Unidade:',value=km)
			arremesso.add_field(name='Distancia',value=distancia)
			arremesso.add_field(name='Objeto:',value=f"{msg}")
			arremesso.add_field(name='Velocidade:', value=f'{vel}Km/h')
			arremesso.add_field(name='Geral:',value=f'{ctx.author.name} arremessou um(a) {msg} em {distancia} {km} a uma velocidade de {vel}km/h. Incrível!.')
			arremesso.set_thumbnail(url='https://images.vexels.com/media/users/3/153394/isolated/preview/0179e4dff69168e1bb794d704ab7070f-personagem-de-v-ndalo-jogando-molotov-by-vexels.png')
			await ctx.send(embed=arremesso)
		except:
			user = ctx.author.name
			erro = discord.Embed(
				title='**Erro Encontrado!**\nCausas: Não escreveu um objeto ou digitou um **"Espaço"**',
				color=0xFF0000,
				description='**Como usar Digite: ``k.arremessar <Objeto>`` caso não for Constate um erro no nosso Servidor Discord**'
				)
			convite = "https://discord.gg/EfgkXdJ"
			erro.add_field(name='⚙| **Servidor:**', value='➡ [**Link**](' + convite + ')\n')
			erro.add_field(name='📌| **Usuário:**', value=user)
			erro.set_thumbnail(url='https://i.imgur.com/SGzaxRE.png')
			f = await ctx.send(embed=erro)
			await asyncio.sleep(30)
			await f.delete()
			s = await ctx.send('**[A mensagem de ERRO foi apagada!**]')
			await asyncio.sleep(5) 
			await s.delete()

def setup(client):
	print('[Comando Arremessar] Carregada!')
	client.add_cog(arremessar(client))