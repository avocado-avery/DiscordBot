#!/usr/bin/env python3

# commands/question5.py

async def run(message):
    foods = ["Pizza", "Tacos", "Sushi", "Pasta", "Ice Cream"]

    lines = []
    for i in range(len(foods)):
        lines.append(f"{i + 1}. {foods[i]}")

    result = "\n".join(lines)
    await message.channel.send("**Q4.1: My Favorite Foods**\n" + result)

