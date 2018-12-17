import discord
from discord.ext import commands
import time
import datetime
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import requests
from discord import Webhook, RequestsWebhookAdapter
COLOUR = 0x008080

class webhook():
	def __init__(self, client):
		self.client = client

	@commands.command(name='bolso',aliases=['bolsonaro', 'bolsola','naro'])
	async def bolso(self, ctx):
		arg = ctx.message.content.split(' ')
		msg = " ".join(arg[1:])
		async with aiohttp.ClientSession() as session:
			hook = Webhook.from_url('https://discordapp.com/api/webhooks/494674745187500053/mD1jQsUvVrnkuNYsOB7l7gpRJV1FbDyjZgdXI-3t8O2wH-iYT31W3kW1Me9lwD8u3jA-', adapter=AsyncWebhookAdapter(session))
			await hook.send(msg, username='Bolsonaro')

def setup(client):
	print('[Comando BolsoWeb] Carregada!')
	client.add_cog(webhook(client))