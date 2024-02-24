import openpyxl

excel=openpyxl.load_workbook("pocha.xlsx")

lista_hojas=excel.sheetnames
dict_T={}
dict_V={}
dict_A={}
data_puntos=[]
lista_jugadores=["T","V","A"]

def carga_excel():
    global lista_jugadores
    global dict_A,dict_V,dict_T
    global lista_hojas
    global data_puntos
    for partida in lista_hojas:
        data_partida=excel[partida]
        for columna in data_partida.iter_cols(values_only=True):
            for celda in columna:
                if celda == "T" or celda == "V" or celda == "A":
                    jugador=celda
                if not isinstance(celda,str):
                    data_puntos.append(celda)
            if jugador=="T":
                dict_T[partida]=data_puntos.copy()
            if jugador=="V":
                dict_V[partida]=data_puntos.copy()
            if jugador=="A":
                dict_A[partida]=data_puntos.copy()
            data_puntos.clear()

def stats():

    for jugador in lista_jugadores:
        if jugador == "T":
            print(jugador)
            create_stats(dict_T)
        if jugador == "V":
            print(jugador)
            create_stats(dict_V)
        if jugador == "A":
            print(jugador)
            create_stats(dict_A)
            

def create_stats(data):
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
    max_max=max(lista_maximos)
    min_min=min(lista_minimos)
    max_suma=max(lista_suma)
    min_suma=min(lista_suma)
    print(max_max,min_min,max_suma,min_suma)
    
if __name__ == "__main__":
    carga_excel()
    stats()