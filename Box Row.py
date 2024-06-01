from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    for i in range(N_BOXES):
        canvas.create_rectangle(
            i * BOX_SIZE,
            CANVAS_HEIGHT - BOX_SIZE,
            (i * BOX_SIZE) + BOX_SIZE,
            CANVAS_HEIGHT,
            "white",
            "black"
        )


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
    