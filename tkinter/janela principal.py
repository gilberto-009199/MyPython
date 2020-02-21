from Tkinter import *

home = Tk()

home.title("programa")

home["background"]="blue"
# backgraund = bg

#largura x altura + a distancia da esquerda do monitor em que
#a janela sera upada + a distancia do topo do monitor em que sera upada
#LxA+E+T
# mediada em pixel
home.geometry("500x400+300+100")
home.mainloop()