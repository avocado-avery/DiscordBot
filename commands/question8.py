# File: commands/question8.py

async def run(message):
    scores = [
        [85, 92, 78, 90],   
        [88, 79, 85, 87],   
        [90, 91, 89, 93],    
    ]

    text = "Question 8: Student Averages\n"

    student_number = 1
    for student_scores in scores:
        total = 0
        for score in student_scores:
            total = total + score
        average = total / len(student_scores)
        text = text + "Student " + str(student_number) + " average: " + str(round(average, 2)) + "\n"
        student_number = student_number + 1

    await message.channel.send(text)


