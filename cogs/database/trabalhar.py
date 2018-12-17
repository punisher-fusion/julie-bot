import discord
from discord.ext import commands
COLOUR = 0x008080
import pymongo
from pymongo import MongoClient
import random
tempo = []
import asyncio
url = 'mongodb+srv://admin:estareli21@flamers-3s8th.mongodb.net/test?retryWrites=true'

class trabalhar():
	def __init__(self, client):
		self.client = client

	@commands.command(aliases=['job'])
	async def trabalhar(self, ctx):
		if ctx.author.id in tempo:
			embed1 = discord.Embed(colour=0xFF0000, description=f'<:xx:520666345474621451>**{ctx.author.mention}, você precisa esperar 2 horas!**')
			await ctx.send(embed=embed1)
			return
		try:
			mongo = MongoClient(url)
			flamers = mongo['flamers']
			rpg = flamers['rpg']
			rpg = flamers.rpg.find_one({'_id':str(ctx.author.id)})
			coins = random.randint(100, 500)
			moedas = int(rpg["coins"])+ int(coins)
			flamers.rpg.update_one({"_id":str(ctx.author.id)},{"$set":{"coins":int(moedas)}})
			embed = discord.Embed(
			colour=COLOUR,
			)
			embed.set_thumbnail(url='https://i.imgur.com/G8hSMjF.png')
			embed.add_field(name='Quem:', value=f'**{ctx.author.name}**')
			embed.add_field(name='Ação:', value='**Trabalhar**')
			embed.add_field(name='Ganhos:', value=f'**{coins}**')
			embed.add_field(name='Saldo Atual:', value=f'**{moedas}**')
			embed.add_field(name='Geral:', value=f'**Olá {ctx.author.name}, você trabalhou e conseguiu {coins} moedas!\nSeu saldo atual: R${moedas}.**')
			await ctx.send(embed=embed)
			tempo.append(ctx.author.id)
			await asyncio.sleep(7200)
			tempo.remove(ctx.author.id)
		except:
			erro = discord.Embed(colour=0xFF0000, description=f'<:xx:520666345474621451> **{ctx.author.name}, você não está registrado(a), digite k.registrar**')
			await ctx.send(embed=erro)


def setup(client):
	print('[Comando Trabalhar] Carregada!')
	client.add_cog(trabalhar(client))