import random
import re

def roll_dice(number_of_dice, number_of_sides):
    rolls = [random.randint(1, number_of_sides) for _ in range(number_of_dice)]
    total = sum(rolls)
    return rolls, total

async def handle_roll(message):
    content = message.content.strip()

    # Verifica se o conteúdo é válido para rolagem de dados
    dice_pattern = re.compile(r'(\d*)d(\d+)([\+\-]?\d*)')
    match = dice_pattern.match(content)

    if match:
        number_of_dice = int(match.group(1)) if match.group(1) else 1  # 1 dado por padrão
        number_of_sides = int(match.group(2))
        modifier_str = match.group(3)

        # Realiza a rolagem dos dados
        rolls, total = roll_dice(number_of_dice, number_of_sides)

        # Aplica modificadores
        modifier = 0
        if modifier_str:
            modifier = int(modifier_str)
            total += modifier

        # Exibe o resultado
        rolls_str = ' + '.join(map(str, rolls))
        response = f'` {total} ` ⟵ [{rolls_str}] {number_of_dice}d{number_of_sides}'

        # Envia a resposta
        await message.reply(response)
