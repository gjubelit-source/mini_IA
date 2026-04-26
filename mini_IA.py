def calcular_nivel(python, matematicas):
    return (python + matematicas) / 2

def evaluar(nivel, experiencia):
    if nivel >= 85 and experiencia:
        return "Acceso Total"
    elif nivel >= 70:
        return "Acceso Limitado"
    else:
        return "Acceso Denegado"


def sistema_ia(nombre, python, matematicas, experiencia=False):
    nivel = calcular_nivel(python, matematicas)
    decision = evaluar(nivel, experiencia)
    
    return f"Nombre: {nombre} \nNivel: {nivel} \nResultado: {decision}"


resultado = sistema_ia(
    nombre="Grissel",
    python=90,
    matematicas=80,
    experiencia=True
)

print(f"Hola: {resultado}")