# File: commands/question6.py

async def run(message):
    text = "abracadabra"
    processed_letters = ""
    found_d = False

    for letter in text:
        if letter == 'a':
            continue   
        if letter == 'd':
            found_d = True
            break      
        processed_letters += letter  

    response = "**Question 6 Result:**\n"
    response += "Processed letters: `" + processed_letters + "`\n"

    if found_d:
        response += "🚫 Found 'd', stopping."

    await message.channel.send(response)


