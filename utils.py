import json

modulos = [
#'cogs.help',
'cogs.avatar',
'cogs.fun.dado', 
'cogs.fun.roll', 
'cogs.fun.numero',
'cogs.fun.arremessar',
'cogs.database.registrar', 
'cogs.database.trabalhar', 
'cogs.moderação.descarregar', 
'cogs.moderação.recarregar', 
'cogs.moderação.eval',
'cogs.fun.futuro',
'cogs.APIs.filme',
'cogs.database.aviãozinho',
'cogs.educação.transformação',
'cogs.educação.transformação2',
'cogs.fun.say',
'cogs.database.saldo',
'cogs.img.perfil',
'cogs.database.apostar',
'cogs.database.mendigar',
'cogs.database.assaltar',
'cogs.APIs.news',
'cogs.APIs.dicionario',
'cogs.info.ping',
'cogs.webhook.bolsoweb',
'cogs.educação.numberinfo',
'cogs.educação.medidas',
'cogs.educação.tabuada',
'cogs.APIs.cotação'



]
with open('token.json')as algo:
	carregar = json.load(algo)
	token = carregar['token']