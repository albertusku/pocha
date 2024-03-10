from matplotlib import pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt=pyplot

def plot_player(player,lista_rondas,lista_jugadores,ventana):
    plt.close()
    for element in ventana.winfo_children():
            if str(element).find("canvas")!=-1:
                element.destroy()
    if player!="full":
        for cont in range(len(lista_rondas)):
            if player=="T" or player=="Teo":
                plt.plot(lista_rondas[cont],lista_jugadores[0].acumulado[cont])
            if player=="V" or player=="Visi":
                plt.plot(lista_rondas[cont],lista_jugadores[1].acumulado[cont])
            if player=="A" or player=="Alberto":
                plt.plot(lista_rondas[cont],lista_jugadores[2].acumulado[cont])
    else:
        if player=="full":
            for cont in range(len(lista_jugadores)):
                plt.figure()
                for i in range(len(lista_rondas)):
                    plt.plot(lista_rondas[i],lista_jugadores[cont].acumulado[i])
                plt.title(lista_jugadores[cont].nombre)
                
    canvas = FigureCanvasTkAgg(plt.gcf(), master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()
    # plt.show()

def plot_multiplayer(x,y1,y2,y3,title):
    plt.plot(x,y1,label="T")
    plt.plot(x,y2,label="V")
    plt.plot(x,y3,label="A")
    plt.axvline(x=len(x)/2, color='r', linestyle='--')
    plt.title(title)
    plt.legend()
    plt.show()



