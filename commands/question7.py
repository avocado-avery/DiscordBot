# File: commands/question7.py

async def run(message):
    foods = ["Pizza", "Tacos", "Sushi", "Pasta", "Ice Cream"]
    text = "Question 7: My Favorite Foods\n"

    i = 1
    for food in foods:
        text = text + str(i) + ". " + food + "\n"
        i = i + 1

    await message.channel.send(text)


