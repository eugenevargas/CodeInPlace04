def main():
    #Load numbers from file
    number_list = load_numbers_from_file("numbers.txt")
    
    #Variable declaration
    sumOfNumbers = 0
    average = 0.0
    listLength = len(number_list)

    #Loop to get sum of values
    for i in range(listLength):
        sumOfNumbers += number_list[i]

    #Compute average
    average = sumOfNumbers / listLength

    #Print output
    print(f"Average: {average}")

def load_numbers_from_file(filepath):
    """
    Loads numbers from a file into a list and returns it.
    We assume the file to have one number per line.
    Returns a list of numbers. You should not modify this
    function.
    """
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(float(cleaned_line))
    
    return numbers 


if __name__ == '__main__':
    main()
