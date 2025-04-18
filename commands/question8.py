#!/usr/bin/env python3

# commands/question6.py

async def run(message):
    scores = [
        [85, 92, 78, 90],   # Student 1
        [88, 79, 85, 87],   # Student 2
        [90, 91, 89, 93]    # Student 3
    ]

    lines = []
    for i in range(len(scores)):
        total = 0
        for score in scores[i]:
            total += score
        average = total / len(scores[i])
        lines.append(f"Student {i + 1} average: {average:.2f}")

    result = "**Q4.2: Student Averages**\n" + "\n".join(lines)
    await message.channel.send(result)

