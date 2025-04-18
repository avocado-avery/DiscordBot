#!/usr/bin/env python3

# commands/question4.py

async def run(message):
    text = "abracadabra"
    result = []

    for ch in text:
        if ch == 'a':
            continue
        if ch == 'd':
            result.append("🚫 Found 'd', stopping.")
            break
        result.append(ch)

    # Separate result letters from stop message if needed
    letters = [ch for ch in result if len(ch) == 1]
    status = next((ch for ch in result if len(ch) > 1), "")

    response = "**Q3.2 Result:**\n"
    response += "Processed letters: `" + "".join(letters) + "`\n"
    if status:
        response += status

    await message.channel.send(response)

