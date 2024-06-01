from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    "Loop to create the initialized number of circles (N_CIRCLES)"
    for i in range(N_CIRCLES):
        create_circle(CIRCLE_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT, canvas)

"Function to create a random circle"
def create_circle(CIRCLE_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT, canvas):
    "Initialize X and Y of circle start point"
    x_start = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
    y_start = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)

    "Initialize X and Y of circle end point"
    x_end = x_start + CIRCLE_SIZE
    y_end = y_start + CIRCLE_SIZE

    "Generate random color for circle"
    randColor = random_color()

    "Draw a random-colored circle graphic"
    canvas.create_oval(x_start, y_start, x_end, y_end, randColor)

def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()