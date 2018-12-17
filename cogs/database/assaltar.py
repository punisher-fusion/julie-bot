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

	@commands.command(aliases=['roubar'])
	async def assaltar(self, ctx, membro: discord.Member):
		#try:
			user = ctx.message.mentions[0].name
			mongo = MongoClient(url)
			flamers = mongo['flamers']
			rpg = flamers['rpg']
			rpg = flamers.rpg.find_one({'_id':str(ctx.author.id)})
			coins = random.randint(0, 350)
			moedas = int(rpg['coins']) + int(coins)
			dolar = int(rpg['coins']) - int(moedas)
			flamers.rpg.update_one({"_id":str(ctx.author.id)},{"$set":{"coins":int(moedas)}})
			flamers.rpg.update_one({"_id":str(membro.id)}, {"$set":{"coins":int(dolar)}})
			embed = discord.Embed(color=COLOUR)
			a = ['Faquinha de Cortar Pão', 'Facão', 'Glock', 'Pistolinha', 'Ak-47', 'Nenhuma', 'Na porrada', 'M4', 'M16', 'Faca AK-45']
			arma = random.choice(a)
			embed.add_field(name='Ladrão:', value=f'{ctx.author.name}')
			embed.add_field(name='Assaltado:', value=f'{membro}')
			embed.add_field(name='Dinheiro Roubado:', value=f'{coins}') 
			embed.add_field(name='Arma usada:', value=f'{arma}')
			embed.set_thumbnail(url='https://i.imgur.com/ZWu3VLC.png')
			await ctx.send(embed=embed)
		#except:
			#erro = discord.Embed(colour=0xFF0000, description=f'<:xx:520666345474621451> **{ctx.author.name}, você não está registrado(a), digite k.registrar**')
			#await ctx.send(embed=erro)



def setup(client):
    print('[Comando Assaltar] Carregada!')
    client.add_cog(database(client))
