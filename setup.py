import discord
from discord.ext import commands
import asyncio
import utils
import json

prefix = ['julie ', 'j ', 'j.', 'J.', 'j!', 'k.']

client = commands.AutoShardedBot(command_prefix=prefix, shard_count=2, shard_ids=(0,1))
client.remove_command("help")

modulos = utils.modulos

@client.event
async def on_ready():
	print('___'*20)
	print(f'Nome: {client.user.name}')
	print(f'Id: {client.user.id}')
	print('Bot Online!')
	print('___'*20)
	await client.change_presence(activity=discord.Streaming(name='Olá, sou a Julie!',url='https://www.twitch.tv/gamebotbr'))
	await asyncio.sleep(180)
	await client.change_presence(activity=discord.Streaming(name='Estou sendo Desenvolvida pelo Punisher!',url='https://www.twitch.tv/gamebotbr'))

if __name__ == "__main__":
 try:
   for modulo in modulos:
   	 client.load_extension(modulo)
 except Exception as e:
 	print(f'[Erro] {modulo} - {e}')

client.run(utils.token)