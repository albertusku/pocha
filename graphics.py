from matplotlib import pyplot

plt=pyplot

def plot_player(x,y,title):
    print("Cargando graphics")
    plt.plot(x,y)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title(title)
    plt.show()

def plot_multiplayer(x,y1,y2,y3,title):
    plt.plot(x,y1,label="T")
    plt.plot(x,y2,label="V")
    plt.plot(x,y3,label="A")
    plt.axvline(x=len(x)/2, color='r', linestyle='--')
    plt.title(title)
    plt.legend()
    plt.show()