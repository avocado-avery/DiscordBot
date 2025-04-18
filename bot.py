import os
import discord
from dotenv import load_dotenv
from commands import (
    question1, question2, question3, question4, question5,
    question6, question7, question8, question9,
)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# menu
MENU = (
    "**Please choose an option:**\n"
    "1️⃣  Question 1\n"
    "2️⃣  Question 2\n"
    "3️⃣  Question 3\n"
    "4️⃣  Question 4\n"
    "5️⃣  Question 5\n"
    "6️⃣  Question 6\n"
    "7️⃣  Question 7\n"
    "8️⃣  Question 8\n"
    "9️⃣  Question 9\n"
    "\nType `!select <number>` (e.g. `!select 3`) to run that question."
    "\nType `!grade <number>` (e.g. `!grade 85`) to run that question."
    "\nType `!age <number>` (e.g. `!age 18`) to run that question."
)

# Map numbers to modules
HANDLERS = {
    1: question1,
    2: question2,
    3: question3,
    4: question4,
    5: question5,
    6: question6,
    7: question7,
    8: question8,
    9: question9,
}

@client.event
async def on_ready():
    print(f"{client.user} connected!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower().strip()

    # !grade and !age commands 
    if content.startswith("!grade"):
        await question3.run(message)
        return

    if content.startswith("!age"):
        await question4.run(message)
        return

    # Show the menu
    if content == "!menu":
        await message.channel.send(MENU)
        return

    # Handle a numbered selection
    if content.startswith("!select"):
        parts = content.split()
        if len(parts) != 2 or not parts[1].isdigit():
            await message.channel.send("❌ Usage: `!select <1–9>`.")
            return

        choice = int(parts[1])
        handler = HANDLERS.get(choice)
        if not handler:
            await message.channel.send("❌ Invalid choice. Type `!menu` to see valid options.")
            return

        await handler.run(message)
        return

    # Unknown command fallback
    if content.startswith("!"):
        await message.channel.send("❌ Unknown command. Type `!menu` for options.")

client.run(TOKEN)
