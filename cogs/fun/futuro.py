import discord
from discord.ext import commands
COLOUR = 0x008080
import random
import time
import datetime

class futuro():
	def __init__(self, client):
		self.client = client

	@commands.command(aliases=['fut'])
	async def futuro(self, ctx, *, user: discord.Member=None):
		if user is None:	
			c = ['Em Gázni', 'Em Buraydah', 'Em NewYork', 'Em Orlando', 'Em São Paulo', 'Em Berlim', 'Em Auburn', 'Em Belo Horizonte', 'Em Sierra Vista', 'No Rio Tietê', 'No Esgoto']
			cidade = random.choice(c)
			idade = random.randint(0, 100)
			cc = ['Casado', 'Solteiro', 'Namorando', 'Ninguém te quer', 'Namora um Cachorro']
			status = random.choice(cc)
			f = ['Rico', 'Perdeu Tudo', 'Ganha um salário mínimo', 'Mora na rua', 'Falido', 'Mora na casa de Amigos']
			financeiro = random.choice(f)
			filhos = random.randint(0, 6)
			futuro = discord.Embed(
			color= COLOUR,
			description= f'**{ctx.author.name} Qual será seu Futuro?**',
			timestamp= datetime.datetime.utcnow()
			)
			futuro.add_field(name='Mora:', value=cidade)
			futuro.add_field(name='Idade', value=idade)
			futuro.add_field(name='Status:', value=status)
			futuro.add_field(name='Condição Financeira:', value=financeiro)
			futuro.add_field(name='Filho(s):', value=filhos)
			futuro.add_field(name='Geral:', value=f'**{ctx.author.name}, você vai morar {cidade} com {idade} anos, {status} e {financeiro} com {filhos} Filhos.**')
			futuro.set_thumbnail(url='https://cdn.pixabay.com/photo/2013/07/12/17/59/association-152746_960_720.png')
			await ctx.send(embed=futuro)
		else:
			c = ['Em Gázni', 'Em Buraydah', 'Em NewYork', 'Em Orlando', 'Em São Paulo', 'Em Berlim', 'Em Auburn', 'Em Belo Horizonte', 'Em Sierra Vista', 'No Rio Tietê', 'No Esgoto']
			cidade = random.choice(c)
			idade = random.randint(0, 100)
			cc = ['Casado', 'Solteiro', 'Namorando', 'Ninguém te quer', 'Namora um Cachorro']
			status = random.choice(cc)
			f = ['Rico', 'Perdeu Tudo', 'Ganha um salário mínimo', 'Mora na rua', 'Falido', 'Mora na casa de Amigos']
			financeiro = random.choice(f)
			filhos = random.randint(0, 6)
			porcentagem = random.randint(0, 100)
			futuro1 = discord.Embed(
			color= COLOUR,
			description= f'**{user} Qual será seu Futuro?**',
			timestamp= datetime.datetime.utcnow()
			)
			futuro1.add_field(name='Mora:', value=cidade)
			futuro1.add_field(name='Idade', value=idade)
			futuro1.add_field(name='Status:', value=status)
			futuro1.add_field(name='Financeiro:', value=f'{financeiro}%')
			futuro1.add_field(name='Filho(s):', value=filhos)
			futuro1.add_field(name='Chance de ser Verdade:', value=porcentagem)
			futuro1.add_field(name='Geral:', value=f'**{user}, você vai morar {cidade} com {idade} anos, {status}, e(é) {financeiro}, com {filhos} Filhos.**')
			futuro1.set_thumbnail(url='https://cdn.pixabay.com/photo/2013/07/12/17/59/association-152746_960_720.png')
			await ctx.send(embed=futuro1)

def setup(client):
	print('[Comando Futuro] Carregada!')
	client.add_cog(futuro(client))