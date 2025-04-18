#!/usr/bin/env python3

# commands/question2.py

import random

async def run(message):
    count = 0
    roll = 0
    rolls = []

    while roll != 6:
        roll = random.randint(1, 6)
        count += 1
        rolls.append(f"Roll {count} → {roll}")

    result = "\n".join(rolls)
    result += f"\n\n🎯 It took {count} roll(s) to get a 6."

    await message.channel.send(result)

