import discord
from discord.ext import commands
COLOUR = 0x008080

class avatar():
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def avatar(self, ctx, *, user: discord.Member=None):
		if user is None:
			user = ctx.author.avatar_url
			texto = ('Seu avatar!')
		else:
			usuario = user.avatar_url
			texto = (f'Avatar fresquinho!')
		embed = discord.Embed(title=texto,color=COLOUR)
		embed.set_image(url=user)
		embed.set_footer(text='Flamers 2018.')
		await ctx.send(embed=embed)

def setup(client):
	print('[Comando Avatar] Carregada!')
	client.add_cog(avatar(client))