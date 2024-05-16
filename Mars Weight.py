"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    earthWeight = float(input("Enter a weight on Earth: "))
    marsWeight = earthWeight * 0.378

    print("The equivalent weight on Mars: " + str(round(marsWeight, 2)))

if __name__ == "__main__":
    main()