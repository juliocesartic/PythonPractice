import turtle;

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()
    makeSquare(dave)
    turtle.mainloop()

def makeSquare(dave):
    length = int(raw_input('Square size??'))

    for i in range(4):
        makeLineAndTurn(dave, length)

def makeLineAndTurn(dave, length):
    dave.forward(length)
    dave.left(90)

if __name__ == '__main__':
    main()
