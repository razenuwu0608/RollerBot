import re

async def handle_narration(message, narration_enabled, narration_users):
    # A narração deve funcionar para todos os usuários que não estão em `narration_users`
    if narration_enabled and message.author.id not in narration_users:
        narration_pattern = re.compile(r'([^:]+):(.+)')
        match = narration_pattern.match(message.content)
        if match:
            title = match.group(1).strip()
            narration = match.group(2).strip()
            response = f'**{title}**\n{narration}'
            await message.delete()  # Apaga a mensagem original
            await message.channel.send(response)  # Envia a narração

            # Adicionar o usuário à lista de narradores para garantir que ele continue recebendo narrativas
            if message.author.id not in narration_users:
                narration_users.add(message.author.id)
