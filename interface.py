import tkinter as tk
import sys
import stats
import graphics


ventana=tk.Tk()
def pantalla_init():
    ventana.title("POCHA")
    but1=tk.Button(ventana,text="Crear partida",command=lambda: but_click(1))
    but2=tk.Button(ventana,text="Ver datos",command=lambda: but_click(2))
    but1.pack()
    but2.pack()
    ventana.mainloop()


def but_click(id):
    for element in ventana.winfo_children():
            element.destroy()
    if id==-1:
        pantalla_init()
    if id==1:
        pantalla_partida()
    if id==2:
        pantalla_datos()
    if id==5:
       nombre,lista_rondas,lista_jugadores=stats.pre_graphics_1p("T")
       graphics.plot_player(nombre,lista_rondas,lista_jugadores,ventana)
       pantalla_datos_player("T",lista_jugadores)
    if id==6:
       nombre,lista_rondas,lista_jugadores=stats.pre_graphics_1p("V")
       graphics.plot_player(nombre,lista_rondas,lista_jugadores,ventana)
       pantalla_datos_player("V",lista_jugadores)
    if id==7:
       nombre,lista_rondas,lista_jugadores=stats.pre_graphics_1p("A")
       graphics.plot_player(nombre,lista_rondas,lista_jugadores,ventana)
       pantalla_datos_player("A",lista_jugadores)




def pantalla_partida():
    but3=tk.Button(ventana,text="Atras",command=lambda: but_click(-1))
    but3.pack()


def pantalla_datos():
    but3=tk.Button(ventana,text="Atras",command=lambda: but_click(-1))
    but4=tk.Button(ventana,text="Partidas Teo",command=lambda: but_click(5))
    but5=tk.Button(ventana,text="Partidas Visi",command=lambda: but_click(6))
    but6=tk.Button(ventana,text="Partidas Alberto",command=lambda: but_click(7))
    but3.pack()
    but4.pack()
    but5.pack()
    but6.pack()

def pantalla_datos_player(nombre,lista_jugadores):
    but3=tk.Button(ventana,text="Atras",command=lambda: but_click(2),width=20,bg="white")
    but3.pack()
    partidas=list(lista_jugadores[0].data_partida.keys())
    for partida in partidas:
        n_but=tk.Button(ventana,text=partida,command=lambda: but_click(-1))
        n_but.pack(side="left")
    


if __name__ == "__main__":
    stats.main()
    pantalla_init()

        





    
