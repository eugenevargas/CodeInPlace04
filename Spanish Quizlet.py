def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    #Variable declaration
    numOfItems = len(translations)
    correctAnswers = 0
    answer = ""

    #Loop for questions
    for i in range(numOfItems):
        englishWord = list(translations.keys())[i]
        answer = input(f"What is the Spanish translation for {englishWord}? ")

        #Check answers
        if(answer == list(translations.values())[i]):
            printCorrectAnswer()
            correctAnswers += 1
        else:
            print(f"That is incorrect, the Spanish translation for {englishWord} is {list(translations.values())[i]}.")
            print()

    #Print final score
    print(f"You got {correctAnswers}/8 words correct, come study again soon!")

def printCorrectAnswer():
    print("That is correct!")
    print()

if __name__ == '__main__':
    main()