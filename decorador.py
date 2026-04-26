import time

def decorador(funcion):
    def nueva_funcion():
        inicio = time.time()
        print(f"Inicio: {time.ctime(inicio)}")
        
        funcion()
        
        fin = time.time()
        print(f"Tiempo de Fin: {time.ctime(fin)}")
        print(f"Tiempo de Duración: {fin - inicio:.6f} segundos")
        
    return nueva_funcion


@decorador
def saludar():
    print("Hola")
    time.sleep(2)  # Simula que la función tarda


saludar()