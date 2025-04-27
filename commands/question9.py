# File: commands/question9.py

async def run(message):
    inventory = { 'apple': 5, 'banana': 2, 'orange': 0 }
    text = "Question 9: Inventory Status\n"

    for item in inventory:
        qty = inventory[item]
        if qty > 0:
            text = text + item + ": in stock ✅\n"
        else:
            text = text + item + ": out of stock ❌\n"

    await message.channel.send(text)


