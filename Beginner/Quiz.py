
questions = [
{
    "prompt": "What is Mickey Mouses dog called?",
    "options":[ "A. Pluto","B. Bruce","C. Jude","D. Prick"],
    "answer": "A"

},
{
    "prompt":"What is the name of the largest planet in the Solar System?",
    "options":["A. Jupiter", "B. Earth", "C. Mars", "D. Venus"],
    "answer": "A"
},
{
    "prompt":"In which city is the Disney movie Ratatouille based?",
    "options":["A. Paris", "B. Copenhagen", "C. Dublin", "D. London"],
    "answer": "A"
},
{
    "prompt":"What are Santa’s little helpers called?",
    "options":["A. Elves", "B. Fairy’s", "C. Gremlins", "D. Little People"],
    "answer": "A"
},
{
    "prompt":"Which Italian city is famous for its leaning tower?",
    "options":["A.Pisa","B. San Michele degli Scalzi","C. San Nicola","D. Venice"],
    "answer": "A"
},
{
    "prompt":"In the following which one food Giant Pandas normally eat?",
    "options":["A. Bamboo","B. Corn","C. Fish","D. Bananas"],
    "answer": "A"
},
{
    "prompt":"In the movie Finding Nemo, which country has Nemo been taken to?",
    "options":["A. Australia","B. England","C. Japan","D. New Zealand"],
    "answer": "A"
},
{
    "prompt":"What type of animals pull Santa/’s sleigh?",
    "options":["A. Reindeer","B. Dogs","C. Horses","D. Cats","E. Green"],
    "answer": "A"
},
{
    "prompt":"What color is the Grinch, who stole Christmas?",
    "options":["A. Green","B. Blue","C. Purple","D. Brown"],
    "answer": "A"
},
{
    "prompt":"What is the name of the boy who owns Buzz Lightyear in the movie Toy Story?",
    "options":["A. Andy","B. Woody","C. Jeremy","D. Jack"],
    "answer": "A"
},
{
    "prompt":"In Jungle Book what is the name of bear?",
    "options":["A. Baloo","B. Dabloo","C. Chang","D. Mushu"],
    "answer": "A"
},
{
    "prompt":"In Disney’s Frozen, what is the name of the kingdom where Elsa and Anna live?",
    "options":["A. Arendelle","B. Caprica","C. Kalyyk","D. Laoag"],
    "answer": "A"
},
{
    "prompt":"Which color do you find at the top of a rainbow?",
    "options":["A. Red","B. Blue","C. Purple","D. Green"],
    "answer": "C"
}


]


def run(questions):
    score=0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        while True:
            answer = input("Your answer (A,B,C or D):").upper()
            if answer in ['A','B','C','D']:
                break
            else:
                print("Invalid Answer. Enter A,B,C or D")

        if answer == question["answer"]:
            print("Correct!\n")
            score+=1
        else: 
            print("Wrong! Correct answer:",question["answer"],"\n")

    
    print(f"Your Score is {score} out of {len(questions)} questions")

run(questions)
