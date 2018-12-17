import discord
from discord.ext import commands
import asyncio
import pymongo
from pymongo import MongoClient
import time
import datetime
url = 'mongodb+srv://admin:estareli21@flamers-3s8th.mongodb.net/test?retryWrites=true'
tempo = []
COLOUR = 0x008080

class database():
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def saldo(self, ctx, *, user: discord.Member=None):
		if user is None:
			user = ctx.author
		try:	
			mongo = MongoClient(url)
			flamers = mongo['flamers']
			rpg = flamers['rpg']
			rpg = flamers.rpg.find_one({'_id':str(user.id)})
			moedas = int(rpg['coins'])
			embed = discord.Embed(
				color=COLOUR,
				timestamp= datetime.datetime.utcnow()
				)
			embed.add_field(name='Saldo Atual:', value=f'**R${moedas}**')
			embed.add_field(name='Geral:', value=f'**Olá {user.name}, você tem R${moedas} Moedas!**')
			embed.set_thumbnail(url='https://i.imgur.com/ZznnFsQ.png')
			tempo.append(ctx.author.id)
			await asyncio.sleep(5)
			tempo.remove(ctx.author.id)
			await ctx.send(embed=embed)
		except:
			erro = discord.Embed(
				color=0xFF0000,
				description=f'<:xx:520666345474621451> **{ctx.author.name}, você não está Registrado(a), digite "k.registrar"!**'
				)
			await ctx.send(embed=erro)

def setup(client):
	print('[Comando Saldo] Carregada!')
	client.add_cog(database(client))