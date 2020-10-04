import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Aspiradora")
wn.setup(700 , 700)

class Pen1(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

class Pen2(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Pen3(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("grey")
        self.penup()
        self.speed(0)

class Pen4(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Pen5(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

niveles = []

#Definimos plantilla 1

nivel_0 = [
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZXA____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
]

nivel_1 = [
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZXAX________X__________XZ",
    "ZX_X________X__________XZ",
    "ZX__________X__________XZ",
    "ZX____B_____X__________XZ",
    "ZX_____XXXXXXXXXXX_____XZ",
    "ZX_____________________XZ",
    "ZX_____XXXXXXXXXXX_____XZ",
    "ZX__________X__________XZ",
    "ZX__________X_B________XZ",
    "ZX__________X__________XZ",
    "ZX_____XXXXXXXXXXX_____XZ",
    "ZX_____________________XZ",
    "ZX____B_____X__________XZ",
    "ZX__________X__B_______XZ",
    "ZX__________X__________XZ",
    "ZX_____XXXXXXXXXXX_____XZ",
    "ZX________B_X__________XZ",
    "ZX__________X______B___XZ",
    "ZX__________X__________XZ",
    "ZX_____B_______________XZ",
    "ZX_____________________XZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
]

nivel_2 = [
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZXA_________X______B___XZ",
    "ZX__________X__________XZ",
    "ZX__________X__________XZ",
    "ZX____B_____X__________XZ",
    "ZX__XXXXXXXXX__XXXXXXXXXZ",
    "ZX_____________________XZ",
    "ZX_____XXXX___XXXX_____XZ",
    "ZX_____X_________x_____XZ",
    "ZX_____X____B____x_____XZ",
    "ZX_____X_________x_____XZ",
    "ZX_____XXXXXXXXXXX_____XZ",
    "ZX_____________________XZ",
    "ZX_____X_________X_____XZ",
    "ZX_____________________XZ",
    "ZX______________B______XZ",
    "ZXxxxxxXXXX___XXXXxxxxxXZ",
    "ZX_________________B___XZ",
    "ZX_____XXXXXXXXXXX_____XZ",
    "ZX_____X_________X_____XZ",
    "ZX_____________________XZ",
    "ZX___B_____XXX_________XZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
]

nivel_3 = [
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZXA___________________BXZ",
    "ZX_____________________XZ",
    "ZX_____________B_______XZ",
    "ZX_____________________XZ",
    "ZX__B__________________XZ",
    "ZX_____________________XZ",
    "ZX___________________B_XZ",
    "ZX_____________________XZ",
    "ZX______B______________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX_____B_______________XZ",
    "ZX_____________________XZ",
    "ZX_________________B___XZ",
    "ZX_____________________XZ",
    "ZX_____________________XZ",
    "ZX____B________________XZ",
    "ZX__________B__________XZ",
    "ZXB___________________BXZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
]

nivel_4 = [
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZXA__X_____________X___XZ",
    "ZX___X___X_____X___X___XZ",
    "ZX___X_B_X_____X_B_X___XZ",
    "ZX___XXXXX_____XXXXX___XZ",
    "ZX___________________B_XZ",
    "ZXXXXXXXXXXX_XXXXXXXXXXXZ",
    "ZX________________B____XZ",
    "ZX_______B_____________XZ",
    "ZX_____________________XZ",
    "ZX_____XXXXXXXXXXX_____XZ",
    "ZX____________B________XZ",
    "ZXB____XXXXXXXXXXX_____XZ",
    "ZX_____________________XZ",
    "ZX_____XXXXXXXXXXX_____XZ",
    "ZX_______B_____________XZ",
    "ZX__________________B__XZ",
    "ZX_____XXXXXXXXXX______XZ",
    "ZX_____X_B______X______XZ",
    "ZX_____X___XX___X______XZ",
    "ZX_________XX__________XZ",
    "ZXB________XX_B________XZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
]

nivel_5 = [
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZXA_________B__________XZ",
    "ZX________________XXXX_XZ",
    "ZX___B________B________XZ",
    "ZX_XX__XX__XX__XX__XX__XZ",
    "ZX________________B____XZ",
    "ZX_XX__XX__XX__XXB_XX__XZ",
    "ZX_B______B____________XZ",
    "ZX_XX__XX__XX__XX__XX__XZ",
    "ZX______B______________XZ",
    "ZX_XXB_XX__XX__XXB_XX__XZ",
    "ZX_________B___________XZ",
    "ZX_XX__XX__XX__XXB_XX__XZ",
    "ZX___B_____________B___XZ",
    "ZX_XX__XX__XX__XXB_XX__XZ",
    "ZX___________B_________XZ",
    "ZX_XX__XX__XX__XX__XX__XZ",
    "ZX________B________B___XZ",
    "ZXBXX__XX__XX__XX__XX__XZ",
    "ZX_____________________XZ",
    "ZX_XX__XX__XX__XX__XX__XZ",
    "ZX_______B_________B___XZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
]

nivel_6 = [
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZXA___BX_____B______B__XZ",
    "ZX_____X___XXXXX___X___XZ",
    "ZX_____XB__X_B_X___X___XZ",
    "ZX_____X___X___X___X___XZ",
    "ZX_____X___X___X___X___XZ",
    "ZX_____X___X___X___X___XZ",
    "ZX_____X___X___X___X___XZ",
    "ZX_____X___X___X___X___XZ",
    "ZX_____X___X___X___X___XZ",
    "ZX_____X___X___X_B_X___XZ",
    "ZX___B_X___X___X___X___XZ",
    "ZX_____X___X___X___X___XZ",
    "ZX_____X___X___X___X___XZ",
    "ZX_____X___X___X___X___XZ",
    "ZX_____X___X___X___X___XZ",
    "ZX_____X___X___X___X___XZ",
    "ZX_____X___X___X___X___XZ",
    "ZX_____X___X___X___X___XZ",
    "ZX_____X_B_X___X_B_X___XZ",
    "ZX_____XXXXX_B_XXXXX___XZ",
    "ZX_B________________B__XZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
]

nivel_7 = [
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZXA____________________XZ",
    "ZXXXXXXXXXXXXXXXXXXXX__XZ",
    "ZX_____________________XZ",
    "ZX__XXXXXXXXXXXXXXXXXXXXZ",
    "ZX_____________________XZ",
    "ZXXXXXXXXXXXXXXXXXXXX__XZ",
    "ZX_____________________XZ",
    "ZX__XXXXXXXXXXXXXXXXXXXXZ",
    "ZX_____________________XZ",
    "ZXXXXXXXXXXXXXXXXXXXX__XZ",
    "ZX_____________________XZ",
    "ZX__XXXXXXXXXXXXXXXXXXXXZ",
    "ZX_____________________XZ",
    "ZXXXXXXXXXXXXXXXXXXXX__XZ",
    "ZX_____________________XZ",
    "ZX__XXXXXXXXXXXXXXXXXXXXZ",
    "ZX_____________________XZ",
    "ZXXXXXXXXXXXXXXXXXXXX__XZ",
    "ZX_____________________XZ",
    "ZX__XXXXXXXXXXXXXXXXXXXXZ",
    "ZX____________________BXZ",
    "ZXXXXXXXXXXXXXXXXXXXXXXXZ",
    "ZZZZZZZZZZZZZZZZZZZZZZZZZ",
]


niveles.append(nivel_0)
niveles.append(nivel_1)
niveles.append(nivel_2)
niveles.append(nivel_3)
niveles.append(nivel_4)
niveles.append(nivel_5)
niveles.append(nivel_6)
niveles.append(nivel_7)

def iniciar_lab(nivel):
    for fila in range(len(nivel)):
        for column in range(len(nivel[fila])):

            letra_x = nivel[fila][column]
            screen_x = -288 + (column * 24)
            screen_y = 288 - (fila * 24)

            if letra_x == "X":
                pen1.goto(screen_x , screen_y)
                pen1.stamp()

            if letra_x == "_":
                pen2.goto(screen_x , screen_y)
                pen2.stamp()
            
            if letra_x == "Z":
                pen3.goto(screen_x , screen_y)
                pen3.stamp()

            if letra_x == "A":
                pen4.goto(screen_x , screen_y)
                pen4.stamp()
            
            if letra_x == "B":
                pen5.goto(screen_x , screen_y)
                pen5.stamp()

pen1 = Pen1()
pen2 = Pen2()
pen3 = Pen3()
pen4 = Pen4()
pen5 = Pen5()

iniciar_lab(niveles[7])

turtle.done()
turtle.bye()