# File: commands/question1.py

async def run(message):
    even_numbers = []

    for num in range(2, 21):
        if num % 2 == 0:
            even_numbers.append(str(num))  

    result = ", ".join(even_numbers)
    await message.channel.send(f"Even numbers from 2 to 20:\n{result}")

