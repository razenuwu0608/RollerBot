import random
import re

# Função que calcula o bônus de sorte com base no nível do personagem
def get_luck_bonus(nickname):
    level_pattern = re.compile(r'LVL\s*(\d+)')
    match = level_pattern.search(nickname)
    if match:
        level = int(match.group(1))
        return level // 10  # Bônus de 1% para cada 10 níveis
    return 0  # Sem bônus se não encontrar o padrão

# Função para rolar dados com sorte
def roll_dice(number_of_dice, number_of_sides, modifier=0, operation=None, luck_bonus=0):
    rolls = [random.randint(1, number_of_sides) for _ in range(number_of_dice)]
    total = sum(rolls)

    # Aplicar bônus de sorte
    if luck_bonus > 0:
        for i in range(len(rolls)):
            if random.random() < luck_bonus / 100:
                rolls[i] = random.randint((number_of_sides // 2), number_of_sides)  # Sorte faz o dado vir mais alto
        total = sum(rolls)

    if operation == '+':
        total += modifier
    elif operation == '-':
        total -= modifier
    elif operation == '*':
        total *= modifier
    elif operation == ':':
        if modifier != 0:
            total /= modifier
        else:
            total = 'Divisão por zero não é permitida'

    return total
