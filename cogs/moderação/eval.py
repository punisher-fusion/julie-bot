import discord
from discord.ext import commands
COLOUR = 0x008080

class Moderação():
	def __init__(self ,client):
		self.client = client

	@commands.command()
	async def evap(self, ctx):
		if not ctx.author.id == 296428519947370499:
			return await ctx.send(':warning: **Somente o Punisher pode usar esse Comando!**')
		try:
			embedeval = discord.Embed(color=COLOUR)
			embedeval.add_field(name='**:inbox_tray: Entrada**', value='`'+ ctx.message.content[7:] + '`')
			embedeval.add_field(name='**:outbox_tray: Saída**', value='`' + str(eval(ctx.message.content[7:]))+ '`')
			await ctx.send(embed=embedeval)
		except Exception as e:
			embedeval1 = discord.Embed(color=0xFF0000)
			embedeval1.add_field(name='**:inbox_tray: Entrada**', value='`' + ctx.message.content[7:] + '`')
			embedeval1.add_field(name='**:outbox_tray: Saída**', value='`' + repr(e) + '`')
			await ctx.send(embed=embedeval1)

def setup(client):
	print('[Comando Eval] Carregada!')
	client.add_cog(Moderação(client))