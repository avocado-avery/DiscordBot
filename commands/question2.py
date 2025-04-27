# File: commands/question2.py

import random

async def run(message):
    count = 0
    roll = 0
    text = "Rolling a die until we get a 6:\n"

    while roll != 6:
        roll = random.randint(1, 6)
        count = count + 1
        text = text + "Roll " + str(count) + " → " + str(roll) + "\n"

    text = text + "\nIt took " + str(count) + " roll(s) to get a 6!"

    await message.channel.send(text)

