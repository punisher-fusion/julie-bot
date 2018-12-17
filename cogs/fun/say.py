import discord
from discord.ext import commands
import requests
import json
import time
import datetime
COLOUR = 0x008080

class fun():
	def __init__(self, client):
		self.client = client

	@commands.command(aliases=['falar'])
	async def say(self, ctx):
		await ctx.message.delete()
		msg = str(ctx.message.content).replace('k.say', "")
		await ctx.send(msg)

def setup(client):
	print('[Comando Say] Carregada!')
	client.add_cog(fun(client))