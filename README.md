# DiscordBot – CS1 Final Project

This is a simple Discord bot built for my Computer Science 1 class project.  
It responds to interactive commands like `!menu`, `!select`, `!grade`, and `!age`.

The bot is designed to run basic Python programs through Discord, demonstrating loops, conditionals, data structures, and more.

---

## 📦 Setup Instructions

### 1. Clone the project or download the files

```bash
git clone https://github.com/avocado-avery/DiscordBot.git ~/DiscordBot && cd DiscordBot
```

### 2. Create a .env file in the root directory

Inside the file, add your Discord bot token:

DISCORD_TOKEN=your-bot-token-here

    ⚠️ Do not commit your .env file. It contains your private token.


### 3. Install dependencies
```bash
pip install -r requirements.txt
```

Or, if you don’t have a requirements.txt, install manually:
```bash
pip install discord.py python-dotenv
```

### 4. Run the bot
```bash
python3 bot.py
```
💬 Bot Commands
!menu

Shows the available question options:

1️⃣  Question 1
2️⃣  Question 2
...
9️⃣  Question 9

!select <number>

Run a specific question (e.g., !select 3).

Each number runs a different Python program demonstrating loops, conditionals, or data structures.
!grade <score>

Calculate a letter grade from a numeric score:

> !grade 87
You got a B!

!age <number>

Categorize your age:

> !age 18
You are a Adult.

📝 Notes

    Each question is implemented in its own file in the commands/ folder.

    All logic is inside clean, beginner-friendly async def run(message) functions.

    This project is designed to showcase CS1-level programming using a real-world chat bot.

🔒 .env Reminder

Make sure you do not commit your .env file.
If you're sharing this on GitHub, add .env to your .gitignore.


Once set up, the bot connects to Discord and responds to your commands from any server where it's invited.


