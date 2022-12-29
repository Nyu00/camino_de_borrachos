# We call al the modules that we need 
from borracho import BorrachoTradicional, Drogado
from campo import Campo 
from coordenada import Coordenada 

# Module of grafication 
from bokeh.plotting import figure, show



def caminata(campo, borracho, pasos):
    #This works to know where was the last time the borracho
    inicio = campo.obtener_coordenada(borracho)


    # For how many pasos the borracho will run the funtion
    # mover_borracho
    
    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    # Make a instance of the class "tipo_de_borracho"
    borracho = tipo_de_borracho(nombre='David')

    # Define the origin, where our borracho will start his walk
    origen = Coordenada(0, 0)

    # Make a list that will save all the data about the walk
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)

        # We add a borracho to the canva starting at the origin
        # Using the function "anadir_borracho" that is in the 
        # module campo.py

        # Run the simulation by using the function "caminata"
        simulacion_caminata = caminata(campo, borracho, pasos)

        # And the result of that walk save it in the distancias list   
        distancias.append(round(simulacion_caminata, 1))

    return distancias

def graficar(x, y):
    grafica = figure(title='Camino de borrachos', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x, y, legend='distancia media')

    show(grafica)

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []

    for pasos in distancias_de_caminata:

        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)       
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)

        # We show this in the console:

        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')

        ###


    graficar(distancias_de_caminata, distancias_media_por_caminata)

if __name__ == '__main__':

    nunn = [a for a in range(300)]

#    distancias_de_caminata = [10, 100, 1000, 10000]
    distancias_de_caminata = nunn
    numero_de_intentos = 100
 
    main(distancias_de_caminata, numero_de_intentos, Drogado)