#!/usr/bin/env python3

async def run(message):
    content = message.content.strip()
    parts = content.split()

    if len(parts) != 2 or not parts[1].isdigit():
        await message.channel.send("❌ Usage: !grade <score> (e.g. !grade 84)")
        return

    score = int(parts[1])

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    await message.channel.send(f"You got a **{grade}**!")
