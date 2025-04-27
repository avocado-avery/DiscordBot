# File: commands/question5.py

async def run(message):
    numbers = [3, 0, 7, 12, -5, 14, 0, 9]
    text = "Queston 5 Result:\nProcessed values: "

    for num in numbers:
        if num == 0:
            continue  # Skip zeros
        if num < 0:
            text = text + "\n⚠️ Negative encountered: " + str(num)
            break  # Stop on first negative
        text = text + str(num) + ", "

    await message.channel.send(text)


