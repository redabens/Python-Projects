import tkinter
from tkinter import *
from tkinter import ttk
# création page
fenetre = Tk()
fenetre.geometry('650x600')
fenetre.title('memorisation sequence')
fenetre['bg'] = 'white'
fenetre.resizable(height=False, width=False)

# création plateau2
largeur_bouton_px = 10
hauteur_bouton_px = 5
game = tkinter.Frame(fenetre, bg="gray")
level = Label(game, text="Level 1", font=("Outfit", 20, "bold"), fg="black")
level.pack(fill="x")
vert = Label(game,bg="green",width=largeur_bouton_px,height=hauteur_bouton_px)
vert.bind("<Button-1>",)
vert.place(x=200,y=100)
rouge = Label(game,bg="red",width=largeur_bouton_px,height=hauteur_bouton_px)
rouge.bind("<Button-1>",)
rouge.place(x=400,y=100)
jaune = Label(game,bg="yellow",width=largeur_bouton_px,height=hauteur_bouton_px)
jaune.bind("<Button-1>",)
jaune.place(x=200,y=300)
bleu = Label(game,bg="blue",width=largeur_bouton_px,height=hauteur_bouton_px)
bleu.bind("<Button-1>",)
bleu.place(x=400,y=300)
# creation plateau1
pgaccl = tkinter.Frame(fenetre, bg="light blue")
pgaccl.pack(fill="both", expand=True)
titre = Label(pgaccl, text="HOW TO PLAY?", font=("Outfit", 40, "bold"), fg="dark green", bg="light blue")
titre.pack()
ligne1 = Label(pgaccl, text="Simon: Memory, focus, and pattern", font=("Outfit", 20, "bold"), fg="black",
               bg="light blue")
ligne1.pack()
ligne2 = Label(pgaccl, text="recognition are put to the test as you repeat", font=("Outfit", 20, "bold"), fg="black",
               bg="light blue")
ligne2.pack()
ligne3 = Label(pgaccl, text="color and sound sequences accurately,", font=("Outfit", 20, "bold"), fg="black",
               bg="light blue")
ligne3.pack()
ligne4 = Label(pgaccl, text="progressing through progressively", font=("Outfit", 20, "bold"), fg="black",
               bg="light blue")
ligne4.pack()
ligne5 = Label(pgaccl, text="challenging levels in this classic game.", font=("Outfit", 20, "bold"), fg="black",
               bg="light blue")
ligne5.pack()
nom = tkinter.Frame(pgaccl, bg="light blue")
name = Label(nom, text="Name?:", font=("Outfit", 35, "bold"), fg="black", bg="light blue")
name.pack()
s = tkinter.Entry(nom)
s.pack()
nom.pack()
button = Button(pgaccl, text="START", font=("Outfit", 30, "bold"), fg="black", bg="yellow")
button.place(x=240, y=400)


def verifier_saisie():
    global s
    contenu = s.get()
    if contenu.strip() == "":
        return False
    else:
        return True


def click():
    global button
    button.bind("<Button-1>", jeux)


def attendre_saisie():
    if not verifier_saisie():
        fenetre.after(5000, click())


def jeux(event):
    global pgaccl, btsequ, s
    contenu = s.get()
    contenu = contenu.strip()
    pgaccl.pack_forget()
    game.pack(fill="both", expand=True)


attendre_saisie()
fenetre.mainloop()
