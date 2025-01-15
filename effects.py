import re
import discord

effects = [
    "sangrar", "queimar", "drenar", "cegar", "paralisar", "explodir", "enxarcar"
]
effects_emojis = {
    "sangrar": "🩸",
    "queimar": "🔥",
    "drenar": "🧛",
    "cegar": "👁️‍🗨️",
    "paralisar": "⚡",
    "explodir": "💥",
    "enxarcar": "💧"
}

async def handle_effects(message):
    effect_pattern = re.compile(r'E\s*=\s*(\d+),\s*(\d+)')
    match = effect_pattern.match(message.content)
    if match:
        effect_index = int(match.group(1)) - 1
        times = int(match.group(2))

        if 0 <= effect_index < len(effects):
            effect = effects[effect_index]
            emoji = effects_emojis[effect]
            description = f"{emoji} {effect.capitalize()} {times} vezes"
            embed = discord.Embed(title="Efeito de RPG", description=description, color=0x00FF00)
            await message.channel.send(embed=embed)
