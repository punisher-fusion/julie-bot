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

	@commands.command(aliases=['mendigar', 'esmolar'])
	async def esmola(self, ctx):	
		if ctx.author.id in tempo:
			embed1 = discord.Embed(colour=0xFF0000, description=f'<:xx:520666345474621451>**{ctx.author.mention}, Cansa muito "Mendigar", não? Espere 1 hora para "Mendigar" novamente!**')
			await ctx.send(embed=embed1)
			return
		try:
			mongo = MongoClient(url)
			flamers = mongo['flamers']
			rpg = flamers['rpg']
			rpg = flamers.rpg.find_one({'_id':str(ctx.author.id)})
			c = ['São Paulo', 'Campinas', 'Rio de Janeiro', 'Fortaleza', 'Salvador', 'Cracolândia', 'Acre']
			escolha = random.choice(c)
			coins = random.randint(0, 27)
			moedas = int(rpg["coins"])+ int(coins)
			flamers.rpg.update_one({'_id':str(ctx.author.id)}, {'$set':{'coins':int(moedas)}})
			embed = discord.Embed(color=COLOUR, description=
				f'**<:update:507490959198519308> {ctx.author.name}, você foi nas ruas de(o)(a) {escolha} e conseguiu R${coins} moedas!**')
			embed.add_field(name='Saldo Atual:', value=f'**Seu saldo atual é de: R${moedas} moedas!**')
			embed.set_thumbnail(url='https://i.imgur.com/vsHcfBa.png')
			await ctx.send(embed=embed)
			tempo.append(ctx.author.id)
			await asyncio.sleep(3600)
			tempo.remove(ctx.author.id)
		except:
			erro = discord.Embed(colour=0xFF0000, description=f'<:xx:520666345474621451> **{ctx.author.name}, você não está registrado(a), digite k.registrar**')
			await ctx.send(embed=erro)

def setup(client):
	print('[Comando Mendigar] Carregada!')
	client.add_cog(database(client))