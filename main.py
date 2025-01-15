import discord
import re
import asyncio
from commands import roll  # Comando de rolagem simples
from commands import roll2  # Comando de rolagem com sessões
from commands import narration  # Comando de narração
from commands import math  # Comando de matemática
from commands import effects  # Comando de efeitos
from commands import utils  # Utilitários (como bônus de sorte e rolagem de dados)

# Insira o token do seu bot aqui
TOKEN = 'OTkzMjczNDc3NzU2ODg3MTAw.Gmjf9G.ogvcvfwVuI3N6-8f1vDs1GGkp4e4PJFYhIZmPo'

# Configurar o cliente do bot
intents = discord.Intents.default()
intents.message_content = True  # Ativar a leitura do conteúdo das mensagens
client = discord.Client(intents=intents)

# Variáveis de narração
narration_enabled = True
narration_users = set()  # Conjunto de usuários que têm a narração ativada

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.event
async def on_message(message):
    global narration_enabled
    global narration_users

    if message.author == client.user:
        return

    # Verifique se a mensagem corresponde ao comando de rolagem simples (roll.py)
    if re.match(r'^\d*d\d+(\+?\-?\d+)?$', message.content.strip()):
        await roll.handle_roll(message)
        return

    # Verifique se a mensagem corresponde ao comando de rolagem com sessões (roll2.py)
    if re.match(r'^\d+#\d*d\d+(\+?\-?\d+)?$', message.content.strip()):
        await roll2.handle_roll_sessions(message)
        return

    # Verifique se a mensagem corresponde ao comando de matemática (math.py)
    if re.match(r'^r(\d+([+\-*:]\d+)*)$', message.content.strip()):
        await math.handle_math(message)
        return

    # Verifique se a mensagem corresponde ao comando de efeitos (effects.py)
    if re.match(r'^E\s*=\s*(\d+),\s*(\d+)$', message.content.strip()):
        await effects.handle_effects(message)
        return

    # Comando de desativar narração (durante 5 segundos)
    if message.content == '!desativar':
        narration_users.add(message.author.id)
        await message.reply(f"Narração desativada para você, {message.author.mention}. A narração será reativada em 5 segundos.")

        # Esperar 5 segundos antes de reativar a narração para o usuário
        await asyncio.sleep(5)

        narration_users.discard(message.author.id)
        await message.reply(f"Narração reativada para você, {message.author.mention}.")
        return

    # Passar os dados para o comando de narração
    await narration.handle_narration(message, narration_enabled, narration_users)

# Rodar o bot
client.run(TOKEN)
