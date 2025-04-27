# File: commands/question4.py

async def run(message):
    content = message.content.strip()
    parts = content.split()

    if len(parts) != 2 or not parts[1].isdigit():
        await message.channel.send("❌ Usage: !age <your age> (example: !age 25)")
        return

    age = int(parts[1])

    if age < 13:
        category = "Child"
    elif age <= 17:
        category = "Teen"
    elif age <= 64:
        category = "Adult"
    else:
        category = "Senior"

    await message.channel.send("You are a " + category + ".")


