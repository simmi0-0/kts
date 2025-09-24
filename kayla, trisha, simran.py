def game_of_doom():
    print ("Welcome whores to this quiz to see if you've got brains in that head of yours.")
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "Which hand is on your right?",
            "options": ["A) Your right hand", "B) Your left hand", "C) Your cousin's left ear", "D) Yor granddad's dying right kidney"],
            "answer": "A"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Your Anus"],
            "answer": "B"
        },
        {
            "question": "To pee or not to pee? That is the question🤔",
            "options": ["A) Sometimes", "B) Sure do it", "C) Fuck you asking me for?", "D) 21"],
            "answer": "D"
        },
        {
            "question": "Who made the character Moby Dick?",
            "options": ["A) Yo Mama", "B) Yo Dead Gamgam", "C) Hermy Mermy", "D) Yo Dick"],
            "answer": "C"
        },
        {
            "question": "Spell 'red'",
            "options": ["A) R-E-D", "B) L-G-B-T", "C) L-S-T-E-R", "D)F-O-O-T"],
            "answer": "C"
        },
        {
            "question": "If you dig 6 foot hole, how deep is that hole?",
            "options": ["A) 6 foot duhh", "B) prolly like 20 feet", "C) 30 000 ft in the air", "D) Not 6 foot"],
            "answer": "B"
        }
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Please enter your answer (A, B, C, or D): ").upper()
        
        if answer == q["answer"]:
            print("Oh My God, you're right for once!\n")
            score += 1
        else:
            print(f"Idiot! The correct answer was {q['answer']}.\n")

    print(f"Your final score is {score} out of {len(questions)}.")

    if score == 7:
        print("Don't be too proud of yourself!")
    elif score >= 5:
        print("Wow! Didn't know you had brains!")
    else:
        print("Do better dumbass!")
    return score
result = game_of_doom()
print(f"Final Score: {result}")
