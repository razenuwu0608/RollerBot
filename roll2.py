import random
import re

def roll_dice(number_of_dice, number_of_sides):
    """
    Função para rolar os dados.
    :param number_of_dice: Quantidade de dados a serem rolados.
    :param number_of_sides: Número de lados de cada dado.
    :return: Uma lista com os resultados das rolagens e a soma total.
    """
    rolls = [random.randint(1, number_of_sides) for _ in range(number_of_dice)]
    total = sum(rolls)
    return rolls, total

async def handle_roll_sessions(message):
    content = message.content.strip()

    # Verifica se o conteúdo é válido para rolagem de dados com sessões
    dice_pattern = re.compile(r'(\d*)#(\d*)d(\d+)([\+\-]?\d*)')
    match = dice_pattern.match(content)

    if match:
        number_of_sessions = int(match.group(1)) if match.group(1) else 1  # Default: 1 sessão se não houver número
        number_of_dice = int(match.group(2)) if match.group(2) else 1  # Default: 1 dado se não houver número
        number_of_sides = int(match.group(3))
        modifier_str = match.group(4)

        # Limita o número de sessões a 30
        number_of_sessions = min(number_of_sessions, 30)

        # Realiza as rolagens e mostra os resultados
        response = ""
        for _ in range(number_of_sessions):
            rolls, total = roll_dice(number_of_dice, number_of_sides)

            # Aplica modificadores
            modifier = 0
            if modifier_str:
                modifier = int(modifier_str)
                total += modifier

            # Prepara a resposta para exibição
            rolls_str = ' + '.join(map(str, rolls))
            response += f'` {total} ` ⟵ [{rolls_str}] {number_of_dice}d{number_of_sides}\n'

        # Envia a resposta
        await message.reply(response)
