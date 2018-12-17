import discord
from discord.ext import commands
import time
import datetime
import random   
import pymongo
from pymongo import MongoClient
tempo = []
import asyncio
url = 'mongodb+srv://admin:estareli21@flamers-3s8th.mongodb.net/test?retryWrites=true'
COLOUR = 0x008080

class database():
	def __init__(self, client):
		self.client = client

	@commands.command(name='silvio',aliases=['silviosantos', 'santos', 'aviaozinho', 'aviãozinho'])
	async def silvio(self, ctx):
		if ctx.author.id in tempo:
			embed1 = discord.Embed(color=COLOUR, description=f'<:xx:520666345474621451> **Não é toda hora que tem programa do Silvio Santos, né?\nEspere 5 horas.**')
			await ctx.send(embed=embed1)
			return
		try:
			mongo = MongoClient(url)
			flamers = mongo['flamers']
			rpg = flamers['rpg']
			rpg = flamers.rpg.find_one({'_id':str(ctx.author.id)})
			coins = random.randint(1, 5)
			v = [30, 40, 50, 100]
			valor = random.choice(v)
			resultado = int(coins)* int(valor)
			moedas = int(rpg['coins'] + int(resultado))
			embed = discord.Embed(
				color=COLOUR
				)
			embed.add_field(name='Quem:', value=f'**{ctx.author.name}**')
			embed.add_field(name='Ação:', value='**Ir no Silvio Santos!**')
			embed.add_field(name='Aviões(ão):', value=f'**{coins}**')
			embed.add_field(name='Ganhos:', value=f'**R${valor}**')
			embed.add_field(name='Saldo Atual:', value=f'**R${moedas}**')
			embed.add_field(name='Geral:', value=f'💰** {ctx.author.mention}, você foi no Programa do Silvio Santos e, pegou {coins} aviões(ão) valendo {valor} moedas. Ganhou: R${resultado} moedas.\n Seu saldo é de R${moedas}!**')
			embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/5/51/Programa_Silvio_Santos_Logo_2015.png')
			await ctx.send(embed=embed)
			tempo.append(ctx.author.id)
			await asyncio.sleep(18000)
			tempo.remove(ctx.author.id)
		except:
			erro = discord.Embed(
					color=COLOUR,
					description=f'<:xx:520666345474621451> **{ctx.author.mention}** **Você não está registrado, por favor, digite "k.registrar"**')
			await ctx.send(embed=erro)

def setup(client):
	print('[Comando Aviãozinho] Carregada!')
	client.add_cog(database(client))