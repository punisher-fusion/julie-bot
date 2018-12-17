import discord
from discord.ext import commands
COLOUR = 0x008080
import pymongo
from pymongo import MongoClient
import random
tempo = []
import asyncio
url = 'mongodb+srv://admin:estareli21@flamers-3s8th.mongodb.net/test?retryWrites=true'

class database():
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def apostar(self, ctx):
		try:
			msg = ctx.message.content.split(' ')[1]
			msg2 = len(msg)
			a = await ctx.send(msg2)
			if (msg2) >= 7:
				await ctx.message.delete()
				await a.delete()
				await msg.delete() 
			else:
				mongo = MongoClient(url)
				flamers = mongo['flamers']
				rpg = flamers['rpg']
				rpg = flamers.rpg.find_one({'_id':str(ctx.author.id)})
				coins = int(rpg['coins'])
				result = int(msg)+100
				result2 = int(msg)-50
				moeda = int(rpg['coins']+int(result))
				moedas2 = int(rpg['coins']-int(result2))
				flamers.rpg.update_one({'_id':str(ctx.author.id)}, {'$set':{'coins':int(moeda)}})
				flamers.rpg.update_one({'_id':str(ctx.author.id)}, {'$set':{'coins':int(moedas2)}})
				e = [f'**Você conseguiu R${result} Moedas!**', f'**Você perdeu R${result2} Moedas!**']
				escolha = random.choice(e)
				embed = discord.Embed(color = COLOUR)
				embed.add_field(name='Jogador:', value=f'**{ctx.author.name}**')
				embed.add_field(name='Resultado:', value=f'{escolha}')
				embed.add_field(name='Geral:', value=f'**Olá {ctx.author.name}**, {escolha}')
				embed.set_thumbnail(url='https://i.imgur.com/eWVdl7D.png')
				await ctx.send(embed=embed)
		except:
			erro = discord.Embed(color=0xFF0000, description=f'<:xx:520666345474621451> **{ctx.author.name}, você não está registrado(a), digite "k.registrar"!**')
			await ctx.send(embed=erro)


def setup(client):
	print('[Comando Apostar] Carregada!')
	client.add_cog(database(client))
