#!/usr/bin/env python3

# commands/question3.py

async def run(message):
    numbers = [3, 0, 7, 12, -5, 14, 0, 9]
    processed = []
    stop_reason = ""

    for num in numbers:
        if num == 0:
            continue  # skip zeros
        if num < 0:
            stop_reason = f"Negative encountered: {num}"
            break  # stop on first negative
        processed.append(str(num))  # convert to string for display

    response = "**Q3.1 Result:**\n"
    response += "Processed values: " + ", ".join(processed) + "\n"

    if stop_reason:
        response += f"⚠️ {stop_reason}"

    await message.channel.send(response)

