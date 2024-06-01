def main():
    words = load_words_from_file("words.txt")
    listOfWords = ["mama", "dada", "baba", "bye-bye", "hi", "no", "juice", "please", "apple"]
    
    #Declare variables
    tempCount = 0;

    #Loop to cycle through words
    for i in range(len(listOfWords)):
        #Reset count value
        tempCount = 0;

        #Cycle through loop for a specific word
        for j in range(len(words)):
            if(words[j] == listOfWords[i]):
                tempCount += 1

        #Print histogram bars
        print_histogram_bar(listOfWords[i], tempCount)

def print_histogram_bar(word, count):
    """
    Prints one bar in the histogram.
    
    Uses formatted strings to do so. The 
        {word : <8}
    adds white space after a string to make
    the string take up 8 total characters of space.
    This makes all of our words on the left of the 
    histogram line up nicely. On the other end,
        {'x' * count}
    takes the 'x' string and duplicates it by 'count'
    number of times. So 'x' * 5 would be 'xxxxx'.
    
    Calling print_histogram_bar("mom", 7) would print:
        mom     : xxxxxxx
    """
    print(f"{word : <8}: {'x' * count}")

def load_words_from_file(filepath):
    """
    Loads words from a file into a list and returns it.
    We assume the file to have one word per line.
    Returns a list of strings. You should not modify this
    function.
    """
    words = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                words.append(cleaned_line)
    
    return words


if __name__ == '__main__':
    main()
