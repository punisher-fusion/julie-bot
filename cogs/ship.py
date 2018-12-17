import discord
from discord.ext import commands
COLOUR = 0x008080
import random
import time
import datetime
import requests
from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO

class fun():
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def ship(self, ctx):
		#try:
			ship = random.randint(0, 100)
			user = ctx.message.mentions[0]
			user1 = ctx.message.mentions[1]
			url = requests.get(user1.avatar_url)
			avatar = Image.open(BytesIO(url.content))
			avatar = avatar.resize((130, 110))
			bigavatar = (avatar.size[0] * 3, avatar.size[1] * 3)
			mascara = Image.new('L', bigavatar, 0)
			recortar = ImageDraw.Draw(mascara)
			recortar.ellipse((0, 0) + bigavatar, fill=255)
			mascara = mascara.resize(avatar.size, Image.ANTIALIAS)
			avatar.putalpha(mascara)
			url1 = requests.get(user.avatar_url)
			avatar1 = Image.open(BytesIO(url1.content))
			avatar1 = avatar1.resize((130, 110))
			bigavatar1 = (avatar1.size[0] * 3, avatar1.size[1] * 3)
			mascara1 = Image.new('L', bigavatar1, 0)
			recortar1 = ImageDraw.Draw(mascara1)
			recortar1.ellipse((0, 0) + bigavatar, fill=255)
			mascara1 = mascara1.resize(avatar1.size, Image.ANTIALIAS)
			avatar1.putalpha(mascara1)
			saida1 = ImageOps.fit(avatar1, mascara1.size, centering=(0.5, 0.5))
			saida1.putalpha(mascara1)
			saida1.save('avatar3.png')
			saida = ImageOps.fit(avatar, mascara.size, centering=(0.5, 0.5))
			saida.putalpha(mascara)
			saida.save('avatar.png')
			img = Image.open('Ship.png')
			fonte = ImageFont.truetype('BebasKai.ttf', 30)
			gg = str(ship) + '%'
			texto = ImageDraw.Draw(img)
			texto.text(xy=(117, 60), text=gg, fill=(255, 255, 255), font=fonte)
			img.paste(avatar, (42, 99), avatar)
			img.paste(avatar1, (681, 101), avatar1)
			img.save('shiptt.png')
			await ctx.send(file=discord.File('shiptt.png', filename='ship.png'))
		#except:
			#Embed = discord.Embed(color=COLOUR, description="**<:nook:518495958128918558> É necessário mencionar 2 usuários pra o comando funcionar corretamente**")
			#Embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			#Embed.set_footer(text="RadioOfficial© 2018")
			#await ctx.send(embed=Embed)

def setup(client):
	print('[Foiiii]')
	client.add_cog(fun(client))