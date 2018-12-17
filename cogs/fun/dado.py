import discord
from discord.ext import commands
import random
import time
import datetime
COLOUR = 0x008080

class dado():
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def dado(self, ctx):
	    escolha = random.randint(1, 6)
	    embebb = discord.Embed(
	    	title='🎲Dado!',
	    	color=COLOUR,
	    	timestamp=datetime.datetime.utcnow()) 
	    embebb.add_field(name='Resultado:', value=f'{escolha}')
	    embebb.add_field(name='Geral:', value=f'{ctx.author.name} Jogou o Dado e caiu no **{escolha}**')   	
	    embebb.set_thumbnail(url='https://cdn.pixabay.com/photo/2012/04/24/13/17/dice-40019_960_720.png')
	    await ctx.send(embed=embebb)

def setup(client):
	print('[Comando Dado] Carregada!')
	client.add_cog(dado(client))