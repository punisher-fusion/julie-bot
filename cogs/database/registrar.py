import discord
from discord.ext import commands
COLOUR = 0x008080
import pymongo
from pymongo import MongoClient
url = 'mongodb+srv://admin:estareli21@flamers-3s8th.mongodb.net/test?retryWrites=true'

class registrar():
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def registrar(self, ctx):
		mongo = MongoClient(url)
		flamers = mongo['flamers']
		rpg = flamers['rpg']
		rpg = flamers.rpg.find_one({"_id":str(ctx.author.id)})
		if rpg is None:
			usuario = {"_id":str(ctx.author.id), "usuario":str(ctx.author.name),"coins":0, "itens:":"nenhum"}
			flamers.rpg.insert_one(usuario).inserted_id
			await ctx.send(f'**Olá {ctx.author.name} você foi registrado no Gbanco com Sucesso!**')
		else:
			await ctx.send(f'**Olá {ctx.author.name}, você já está registrado no Gbanco!**')
		
def setup(client):
	print('[Comando Database] Carregada!')
	client.add_cog(registrar(client))	
