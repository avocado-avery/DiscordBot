#!/usr/bin/env python3

# commands/question7.py

async def run(message):
    inventory = { 'apple': 5, 'banana': 2, 'orange': 0 }

    lines = []

    for item in inventory:
        qty = inventory[item]
        if qty > 0:
            lines.append(f"{item}: in stock ✅")
        else:
            lines.append(f"{item}: out of stock ❌")

    result = "**Q4.3: Inventory Status**\n" + "\n".join(lines)
    await message.channel.send(result)

