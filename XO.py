import tkinter
from tkinter import *

fenetre = Tk()
fenetre.geometry('600x650')
fenetre.title('jeux X/O')
fenetre['bg'] = 'blue'
# fenetre.resizable(height=False, width=False)
# créer affichage
affichage = tkinter.Canvas(fenetre, width=600, height=80)
# créer plateau
plateau = tkinter.Canvas(fenetre, width=600, height=600)
plateau.create_line(200, 0, 200, 600, fill='black', width=4)
plateau.create_line(400, 0, 400, 600, fill='black', width=4)
plateau.create_line(0, 200, 600, 200, fill='black', width=4)
plateau.create_line(0, 400, 600, 400, fill='black', width=4)


def croix(pos):
    plateau.create_line((pos[0]-50), (pos[1]-50), (pos[0]+50), (pos[1]+50), fill='red', width=4)
    plateau.create_line((pos[0]-50), (pos[1]+50), (pos[0]+50), (pos[1]-50), fill='red', width=4)


def cercle(pos):
    plateau.create_oval((pos[0]-50), (pos[1]-50), (pos[0]+50), (pos[1]+50), outline='blue', width=4)


def win(box):
    global label
    if box[0] == 1 and box[3] == 1 and box[6] == 1:
        plateau.create_line(100, 0, 100, 600, fill='black', width=4)
        label['text'] = "PLAYER 1 YOU WON !"
        label['fg'] = "red"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=2)
        plateau.unbind("<Button-1>")
        res = 1
    elif box[0] == 2 and box[3] == 2 and box[6] == 2:
        plateau.create_line(100, 0, 100, 600, fill='black', width=4)
        label['text'] = "PLAYER 2  YOU WON !"
        label['fg'] = "blue"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=5)
        plateau.unbind("<Button-1>")
        res = 1
    elif box[1] == 1 and box[4] == 1 and box[7] == 1:
        plateau.create_line(300, 0, 300, 600, fill='black', width=4)
        label['text'] = "PLAYER 1 YOU WON !"
        label['fg'] = "red"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=5)
        plateau.unbind("<Button-1>")
        res = 1
    elif box[1] == 2 and box[4] == 2 and box[7] == 2:
        plateau.create_line(300, 0, 300, 600, fill='black', width=4)
        label['text'] = "PLAYER 2 YOU WON !"
        label['fg'] = "blue"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=5)
        plateau.unbind("<Button-1>")
        res = 1
    elif box[2] == 1 and box[5] == 1 and box[8] == 1:
        plateau.create_line(500, 0, 500, 600, fill='black', width=4)
        label['text'] = "PLAYER 1 YOU WON !"
        label['fg'] = "red"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=5)
        plateau.unbind("<Button-1>")
        res = 1
    elif box[2] == 2 and box[5] == 2 and box[8] == 2:
        plateau.create_line(500, 0, 500, 600, fill='black', width=4)
        label['text'] = "PLAYER 2 YOU WON !"
        label['fg'] = "blue"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=5)
        plateau.unbind("<Button-1>")
        res = 1
    elif box[0] == 1 and box[1] == 1 and box[2] == 1:
        plateau.create_line(0, 100, 600, 100, fill='black', width=4)
        label['text'] = "PLAYER 1 YOU WON !"
        label['fg'] = "red"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=5)
        plateau.unbind("<Button-1>")
        res = 1
    elif box[0] == 2 and box[1] == 2 and box[2] == 2:
        plateau.create_line(0, 100, 600, 100, fill='black', width=4)
        label['text'] = "PLAYER 2 YOU WON !"
        label['fg'] = "blue"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=5)
        plateau.unbind("<Button-1>")
        res = 1
    elif box[3] == 1 and box[4] == 1 and box[5] == 1:
        plateau.create_line(0, 300, 600, 300, fill='black', width=4)
        label['text'] = "PLAYER 1 YOU WON !"
        label['fg'] = "red"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=5)
        plateau.unbind("<Button-1>")
        res = 1
    elif box[3] == 2 and box[4] == 2 and box[5] == 2:
        plateau.create_line(0, 300, 600, 300, fill='black', width=4)
        label['text'] = "PLAYER 2 YOU WON !"
        label['fg'] = "blue"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=5)
        plateau.unbind("<Button-1>")
        res = 1
    elif box[6] == 1 and box[7] == 1 and box[8] == 1:
        plateau.create_line(0, 500, 600, 500, fill='black', width=4)
        label['text'] = "PLAYER 1 YOU WON !"
        label['fg'] = "red"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=5)
        plateau.unbind("<Button-1>")
        res = 1
    elif box[6] == 2 and box[7] == 2 and box[8] == 2:
        plateau.create_line(0, 500, 600, 500, fill='black', width=4)
        label['text'] = "PLAYER 2 YOU WON !"
        label['fg'] = "blue"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=5)
        plateau.unbind("<Button-1>")
        res = 1
    elif box[0] == 1 and box[4] == 1 and box[8] == 1:
        plateau.create_line(0, 0, 600, 600, fill='black', width=4)
        label['text'] = "PLAYER 1 YOU WON !"
        label['fg'] = "red"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=5)
        plateau.unbind("<Button-1>")
        res = 1
    elif box[0] == 2 and box[4] == 2 and box[8] == 2:
        plateau.create_line(0, 0, 600, 600, fill='black', width=4)
        label['text'] = "PLAYER 2 YOU WON !"
        label['fg'] = "blue"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=5)
        plateau.unbind("<Button-1>")
        res = 1
    elif box[2] == 1 and box[4] == 1 and box[6] == 1:
        plateau.create_line(600, 0, 0, 600, fill='black', width=4)
        label['text'] = "PLAYER 1 YOU WON !"
        label['fg'] = "red"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=5)
        plateau.unbind("<Button-1>")
        res = 1
    elif box[2] == 2 and box[4] == 2 and box[6] == 2:
        plateau.create_line(600, 0, 0, 600, fill='black', width=4)
        label['text'] = "PLAYER 2 YOU WON !"
        label['fg'] = "blue"
        label['font'] = ("Arial", 30, "italic bold")
        label.place(x=70, y=5)
        plateau.unbind("<Button-1>")
        res = 1
    else:
        res = 0
    return res


player = 1
coord = []
case = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def tour(event):
    global player, coord, case, label
    x = event.x
    y = event.y
    position = ([100, 100], [300, 100], [500, 100], [100, 300], [300, 300], [500, 300], [100, 500], [300, 500],
                [500, 500])
    for i in range(0, 9):
        pos = position[i]
        if ((x < pos[0] + 100) and (x > pos[0] - 100)) and ((y < pos[1] + 100) and (y > pos[1] - 100) and
                                                            (pos not in coord)):
            coord.append(pos)
            if player == 1:
                croix(pos)
                player = 2
                label['text'] = "PLAYER 2"
                label['fg'] = "blue"
                label.place(x=120, y=2)
                case[i] = 1
                win(case)
            else:
                cercle(pos)
                player = 1
                label['text'] = "PLAYER 1"
                label['fg'] = "red"
                label.place(x=120, y=2)
                case[i] = 2
                win(case)
            if len(coord) == 9:
                plateau.unbind("<Button-1>")
                gagne = win(case)
                if gagne == 0:
                    label['text'] = " DRAW "
                    label['fg'] = "black"
                    label.place(x=180, y=2)


affichage.pack()
label = tkinter.Label(affichage, text="PLAYER 1", font=("Arial", 50, "italic bold"), fg="red")
label.place(x=120, y=2)
plateau.pack()
plateau.bind("<Button-1>", tour)
fenetre.mainloop()
