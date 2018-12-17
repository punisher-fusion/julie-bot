import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO
COLOUR = 0x008080

class img():
	def __init__(self, client):
		self.client = client

	@commands.command(name='procurado', aliases=['procurada'])
	async def procurado(self, ctx, *, user: discord.Member=None):
		#if user is None:
			#user = ctx.author
		#try:
			img = Image.open('procurado.png')
			img.show()
