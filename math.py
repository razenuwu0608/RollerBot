import re

async def handle_math(message):
    math_pattern = re.compile(r'r(\d+([+\-*:]\d+)*)')
    match = math_pattern.match(message.content)
    if match:
        expression = match.group(1).replace(':', '/')
        try:
            total = eval(expression)
            response = f'` {total} ` ⟵ [{", ".join(match.group(1).split("+*-:"))}]'
        except ZeroDivisionError:
            response = 'Divisão por zero não é permitida'
        await message.reply(response)
