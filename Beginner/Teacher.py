import random

Greek = [
    { "Greek": "και", "english": "and"},
    { "Greek": "είναι", "english": "is"},
    { "Greek": "το", "english": "the"},
    { "Greek": "σε", "english": "in"},
    { "Greek": "γεια", "english": "hello"},
    { "Greek": "ο", "english": "the (masculine)"},
    { "Greek": "η", "english": "the (feminine)"},
    { "Greek": "έχω", "english": "have"},
    { "Greek": "δέντρο", "english": "tree"},
    { "Greek": "αλλά", "english": "but"}]

French = [
    {"French": "et", "english": "and"},
    {"French": "être", "english": "to be"},
    {"French": "le", "english": "the (masculine)"},
    {"French": "de", "english": "of"},
    {"French": "à", "english": "to"},
    {"French": "un", "english": "a (masculine)"},
    {"French": "avoir", "english": "to have"},
    {"French": "je", "english": "I"},
    {"French": "ne", "english": "not"},
    {"French": "pas", "english": "not (negation)"}]

German = [
    {"German": "und", "english": "and"},
    {"German": "sein", "english": "to be"},
    {"German": "der", "english": "the (masculine)"},
    {"German": "in", "english": "in"},
    {"German": "ein", "english": "a (masculine)"},
    {"German": "haben", "english": "to have"},
    {"German": "ich", "english": "I"},
    {"German": "nicht", "english": "not"},
    {"German": "das", "english": "the (neuter)"},
    {"German": "mit", "english": "with"}]


def greek(Greek):
    random.shuffle(Greek)
    score = 0

    for greek in Greek:
        print(f"Give the English translation of '{greek['Greek']}'?")
        user_answer = input("Answer: ").strip().lower()
        correct_answer = greek['english'].lower()

        if user_answer == correct_answer:
            print("Correct!!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{greek['english']}'")
    
    print(f"Your score: {score}/{len(Greek)}")


def french(French):
    random.shuffle(French)
    score = 0

    for french in French:
        print(f"Give the English translation of '{french['French']}'?")
        user_answer = input("Answer: ").strip().lower()
        correct_answer = french['english'].lower()

        if user_answer == correct_answer:
            print("Correct!!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{french['english']}'")
    
    print(f"Your score: {score}/{len(French)}")


def german(German):
    random.shuffle(German)
    score = 0

    for german in German:
        print(f"Give the English translation of '{german['German']}'?")
        user_answer = input("Answer: ").strip().lower()
        correct_answer = german['english'].lower()

        if user_answer == correct_answer:
            print("Correct!!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{german['english']}'")
    
    print(f"Your score: {score}/{len(German)}")


def main():
    print("Learning Languages Flashcards\n")
    
    while True:
        print("Please select a Language:\n")
        print("1. Greek\n")
        print("2. French\n")
        print("3. German\n")
        print("4. Exit\n")
        Language = input("Enter 1, 2, 3, or 4: ")

        if Language == "1":
            greek(Greek)
        elif Language == "2":
            french(French)
        elif Language == "3":
            german(German)
        elif Language == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid input! Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
