from karel.stanfordkarel import *

# Here is a place to program your Section problem

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    # Check if front is clear
    while front_is_clear():
        # If there are no beepers, move forward
        while no_beepers_present():
            move()
            # If a beeper is found, build a hospital
            if(beepers_present()):
                build_hospital()
        # Prevent Karel from hitting a wall
        if(front_is_clear()):
                move()
            

def turn_right():
    # Karel turns right
    for i in range(3):
        turn_left()

def build_hospital():
    # Karel builds the first half
    turn_left()
    for i in range(2):
        move()
        put_beeper()
    turn_right()

    # Karel builds the second half
    move()
    put_beeper()
    turn_right()
    for i in range(2):
        move()
        put_beeper()

    # Karel turns left to face East
    turn_left()

if __name__ == '__main__':
    main()