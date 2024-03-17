import tkinter as tk
from tkinter import ttk
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


def but_click(id,player="",n_partida=0):
    if id!=3 or id!=1 or id!=2:
        nombre,lista_rondas,lista_jugadores=stats.pre_graphics_1p(player)
        graphics.plot_player(nombre,lista_rondas,lista_jugadores,ventana)
    for element in ventana.winfo_children():
            element.destroy()
    if id==1:
        pantalla_partida()
    if id==2:
        pantalla_datos()
    if id==3:
        pantalla_init()
    if id==5:
       nombre,lista_rondas,lista_jugadores=stats.pre_graphics_1p(player)
       graphics.plot_player(nombre,lista_rondas,lista_jugadores,ventana)
       pantalla_datos_player(player,lista_jugadores)
    if id==6:
       nombre,lista_rondas,lista_jugadores=stats.pre_graphics_1p(player)
       graphics.plot_player(nombre,lista_rondas,lista_jugadores,ventana)
       pantalla_datos_player(player,lista_jugadores)
    if id==7:
       nombre,lista_rondas,lista_jugadores=stats.pre_graphics_1p(player)
       graphics.plot_player(nombre,lista_rondas,lista_jugadores,ventana)
       pantalla_datos_player(player,lista_jugadores)
    if id==8:
        if nombre=="T":
            graphics.plot_player(nombre,lista_rondas[n_partida],lista_jugadores[0].acumulado[n_partida],ventana)
        if nombre=="V":
            graphics.plot_player(nombre,lista_rondas[n_partida],lista_jugadores[1].acumulado[n_partida],ventana)
        if nombre=="A":
            graphics.plot_player(nombre,lista_rondas[n_partida],lista_jugadores[2].acumulado[n_partida],ventana)
        pantalla_datos_player(player,lista_jugadores)
    if id==9:
        pantalla_datos_multiplayer(lista_jugadores)
    if id==10:
        graphics.plot_multiplayer(lista_rondas[n_partida],lista_jugadores[0].acumulado[n_partida],lista_jugadores[1].acumulado[n_partida],lista_jugadores[2].acumulado[n_partida],ventana)
        pantalla_datos_multiplayer(lista_jugadores)
    if id==11:
        stats.manage_punt()
        

def pantalla_partida():
    container2=tk.Frame(ventana,padx=50)
    but3=tk.Button(container2,text="Atras",command=lambda: but_click(3))
    but8=tk.Button(container2,text="T",command=lambda: but_click(11,"T"),width=20,bg="white")
    but9=tk.Button(container2,text="V",command=lambda: but_click(11,"V"),width=20,bg="white")
    but10=tk.Button(container2,text="A",command=lambda: but_click(11,"A"),width=20,bg="white")
    but3.pack()
    but8.pack(side="left")
    but9.pack(side="left")
    but10.pack(side="left")
    container2.pack()
    for ronda in stats.lista_ronda:
        container1 = tk.Frame(ventana)
        container1.pack(anchor="w")

        label_ronda = tk.Label(container1, text=str(ronda))
        if ronda>=10:
            label_ronda.pack(side="left", padx=306)
        else:
            label_ronda.pack(side="left", padx=310)

        for _ in range(3):
            texto = tk.Text(container1, width=5, height=1)
            texto.pack(side="left", padx=65)

    

def pantalla_datos():
    but3=tk.Button(ventana,text="Atras",command=lambda: but_click(3))
    but4=tk.Button(ventana,text="Partidas Teo",command=lambda: but_click(5,"T"))
    but5=tk.Button(ventana,text="Partidas Visi",command=lambda: but_click(6,"V"))
    but6=tk.Button(ventana,text="Partidas Alberto",command=lambda: but_click(7,"A"))
    but7=tk.Button(ventana,text="Datos conjuntos",command=lambda: but_click(9))
    but3.pack()
    but4.pack()
    but5.pack()
    but6.pack()
    but7.pack()

def pantalla_datos_player(player,lista_jugadores):
    but3=tk.Button(ventana,text="Atras",command=lambda: but_click(2),width=20,bg="white")
    but3.pack()
    container3=tk.Frame(ventana)
    partidas=list(lista_jugadores[0].data_partida.keys())
    for n,partida in enumerate(partidas):
        n_but=tk.Button(container3,text=partida,command=lambda p=player, idx=n: but_click(8, p, idx))
        n_but.pack(side="left")
    container3.pack()

def pantalla_datos_multiplayer(lista_jugadores):
    text_data=""
    for jugador in lista_jugadores:
        text_data+=jugador.print_jugador()+'\n'    
    label1=tk.Label(ventana,text=text_data)
    label1.pack()
    container4=tk.Frame(ventana)
    but3=tk.Button(ventana,text="Atras",command=lambda: but_click(2),width=20,bg="white")
    but3.pack()
    partidas=list(lista_jugadores[0].data_partida.keys())
    player=""
    for n,partida in enumerate(partidas):
        n_but=tk.Button(container4,text=partida,command=lambda p=player, idx=n: but_click(10, p, idx))
        n_but.pack(side="left")
    container4.pack()



if __name__ == "__main__":
    stats.main()
    pantalla_init()

        





    
