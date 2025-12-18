import numpy as np
import pandas as pd

Tamaño = 100

Fecha = np.datetime64('2025-05-05')
Dias_Random = np.random.randint(0,365, size= Tamaño)
Fecha_Despacho = Fecha + Dias_Random

Tipo_Envio = [ 'Flash', 'Normal', 'Correo Argentino']
Columna = np.random.choice(Tipo_Envio, size = Tamaño, p= [0.2, 0.5, 0.3])

Condiciones = [
    Columna == 'Flash',
    Columna == 'Normal',
    Columna == 'Correo Argentino'
]


Condiciones_dias= [
    np.random.randint(1, 3, size=Tamaño), 
    np.random.randint(3, 7, size=Tamaño),
    np.random.randint(5, 12, size=Tamaño)   
]

Dia_Por_Entrega= np.select(Condiciones, Condiciones_dias)
Dia_Entrega_Estimado = Dia_Por_Entrega.astype('timedelta64[D]') + Fecha_Despacho

Desvio = np.random.randint(-5,10, size = Tamaño)
Fecha_Real = Desvio.astype('timedelta64[D]') + Dia_Entrega_Estimado

Estado = np.where( Desvio > 7, 'Perdido', 'Entregado')

data = {
    'ID_Envio' : range(1, Tamaño + 1),
    'ID_Venta' : range(1, Tamaño + 1),
    'Transportista' : Columna,
    'Fecha_Despacho' : Fecha_Despacho,
    'Fecha_Estimada' : Dia_Entrega_Estimado,
    'Fecha_Real' : Fecha_Real,
    'Estado': Estado
}

df = pd.DataFrame(data)

df.to_csv('Mercado Libre.csv' , index= False)
