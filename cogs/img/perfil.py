import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO
COLOUR = 0x008080

class img():
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def perfil(self, ctx, *, user: discord.Member = None):
		if user is None:
			user = ctx.author
		#try:
			img = Image.open('perfil.png')
			fonte = ImageFont.truetype('GODOFWAR.TTF', 91)
			escrever = ImageDraw.Draw(img)
			escrever.text(xy=(30, 5), text=f'{user.name}', fill=(75, 1, 0), font=fonte)
			escrever.text(xy=(880, 14), text=f'#{user.discriminator}', fill=(75, 1, 0), font=fonte)
			escrever.text(xy=(30, 250), text=f'{user.created_at}', fill=(75, 1, 0), font=fonte)
			
			#escrever.text(xy=(30, 140), text=len(ctx.guild.roles), fill=(75, 1, 0), font=fonte)
			img.save('outro.png')
			#img.show()
			await ctx.send(file=discord.File('outro.png', 'perfil.png'))
		#except:
			#await ctx.send('Eu não sei o que ocorreu, mas ocorreu.')
		
def setup(client):
	print('[Comando Perfil] Carregada!')
	client.add_cog(img(client))