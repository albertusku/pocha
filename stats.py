import openpyxl
import matplotlib

excel=openpyxl.load_workbook("pocha.xlsx")

lista_hojas=excel.sheetnames
data_puntos=[]
euros_totales=0

class Jugador:
    
    def __init__(self,nombre):
        self.nombre=nombre
        self.n_vic=0 
        self.n_pos2=0
        self.n_pos3=0
        self.p_max=0
        self.p_min=0
        self.max_par=0
        self.min_par=0
        self.euros=0
        
        self.data_partida={}
        self.total_partida=[]

    def carga_data_jug(self,partida,puntos):
        self.data_partida[partida]=puntos
    
    def set_n_vic(self,n):
        self.n_vic+=n
    def set_n_pos2(self,n):
        self.n_pos2+=n
    def set_n_pos3(self,n):
        self.n_pos3+=n
    def set_parcial_max(self,n):
        self.p_max=n
    def set_parcial_min(self,n):
        self.p_min=n
    def set_max_partida(self,n):
        self.max_par=n
    def set_min_partida(self,n):
        self.min_par=n
    def set_total_partida(self,lista):
        self.total_partida=lista
    def set_euros(self):
        global euros_totales
        self.euros=self.n_pos2*3+self.n_pos3*5
        euros_totales+=self.euros
    def print_jugador(self):
        global euros_totales
        print("")
        print("Jugador:",self.nombre)
        print("Maximo partida:",self.max_par," Minimo partida:",self.min_par)
        print("Maximo parcial:",self.p_max," Minimo parcial:",self.p_min)
        print("Victorias:",self.n_vic,", 2ª Posicion:",self.n_pos2,", 3ª Posicion:",self.n_pos3)
        print("Euros aportados:",self.euros, "de un total de:",euros_totales,"->",round((self.euros/euros_totales)*100,2),"%")

        

def carga_excel(jugador):
    global lista_hojas
    global data_puntos
    for partida in lista_hojas:
        data_partida=excel[partida]
        for columna in data_partida.iter_cols(values_only=True):
            for celda in columna:
                if celda == "T" or celda == "V" or celda == "A":
                    jugador_act=celda
                if not isinstance(celda,str):
                    data_puntos.append(celda)
                    if jugador_act==jugador.nombre:
                        jugador.carga_data_jug(partida,data_puntos.copy())
            data_puntos.clear()

def stats(lista_jugadores):

    for jugador in lista_jugadores:
        create_stats(jugador)
    victories_counter(lista_jugadores)
    for jugador in lista_jugadores:
        jugador.set_euros()
    
    
            

def create_stats(jugador):
    data=jugador.data_partida
    lista_maximos=[]
    lista_minimos=[]
    lista_suma=[]
    total=0
    for partida in data:
        max_=max(data[partida])
        min_=min(data[partida])
        for puntos in data[partida]:
            total+=puntos
        lista_suma.append(total)
        lista_maximos.append(max_)
        lista_minimos.append(min_)
        total=0
    jugador.set_parcial_max(max(lista_maximos))
    jugador.set_parcial_min(min(lista_minimos))
    jugador.set_max_partida(max(lista_suma))
    jugador.set_min_partida(min(lista_suma))
    jugador.set_total_partida(lista_suma)
    
def victories_counter(lista_jugadores):
    lista_todas_sumas=[]
    puntos_n_partida=[]
    for jugador in lista_jugadores:
        lista_todas_sumas.append(jugador.total_partida)
    for cont in range(len(lista_todas_sumas[0])):
        puntos=[sublista[cont] for sublista in lista_todas_sumas]
        puntos_n_partida.append(puntos.copy())
    print(puntos_n_partida)
    for puntuaciones in puntos_n_partida:
        if max(puntuaciones) == puntuaciones[0]:
            lista_jugadores[0].set_n_vic(1)
            if puntuaciones[1]>puntuaciones[2]:
                lista_jugadores[1].set_n_pos2(1)
                lista_jugadores[2].set_n_pos3(1)
            else:
                lista_jugadores[2].set_n_pos2(1)
                lista_jugadores[1].set_n_pos3(1)
        if max(puntuaciones) == puntuaciones[1]:
            lista_jugadores[1].set_n_vic(1)
            if puntuaciones[0]>puntuaciones[2]:
                lista_jugadores[0].set_n_pos2(1)
                lista_jugadores[2].set_n_pos3(1)
            else:
                lista_jugadores[2].set_n_pos2(1)
                lista_jugadores[0].set_n_pos3(1)
        if max(puntuaciones) == puntuaciones[2]:
            lista_jugadores[2].set_n_vic(1)
            if puntuaciones[0]>puntuaciones[1]:
                lista_jugadores[0].set_n_pos2(1)
                lista_jugadores[1].set_n_pos3(1)
            else:
                lista_jugadores[1].set_n_pos2(1)
                lista_jugadores[0].set_n_pos3(1)


        
  
if __name__ == "__main__":
    Teo=Jugador("T")
    Visi=Jugador("V")
    Alberto=Jugador("A")
    lista_jugadores=[Teo,Visi,Alberto]
    for jugador in lista_jugadores:
        carga_excel(jugador)
    stats(lista_jugadores)
    for jugador in lista_jugadores:
        jugador.print_jugador()