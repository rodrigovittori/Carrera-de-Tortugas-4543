"""
# [M4.L1] Carrera de tortugas - Actividad # 3 "Campo de carrera"

# NOTA: Esta es la primera actividad práctica del Proyecto, (1 y 2 son teoría)

# Objetivo: Crear una tortuga que dibujará la pista de carreras

Paso Nº 1) Importar turtle y crear nuestra tortuga
Paso Nº 2) Dibujar nuestra pista de carreras
            -> Definir la cant. de carriles
            -> Definir el ancho de cada carril
            *entre ambos valores van a definir la lognitud de la pista*

            -> Definir espacio para corredores
            *tener en cuenta la cantidad de tortugas que correrán y dejar espacio entre ellas*
"""

import turtle

# Tortuga que dibuja el tablero (t)
t = turtle.Turtle()
t.up()
t.goto(-200,100)
t.pendown()
t.speed(0)

# Pista de carreras
cant_secciones_pista = 15
ancho_secciones_pista = 20
# Distancia de carrera = cant_secciones_pista * ancho_secciones_pista

long_secciones_pista = 150

t.color(0, 0, 0)  # Setea el color a negro

# Bucle que dibuja la pista:
for pista in range(1, (1 + cant_secciones_pista)):
    t.write(str(pista))         # Escribe el Nº de la sección (1~15)
    t.right(90)                 # Gira 90º (mirando hacia abajo)
    t.fd(long_secciones_pista)  # Dibuja la línea de la sección
    t.bk(long_secciones_pista)  # Retrocede y "vuelve" arriba
    t.seth(0)                   # Acomoda la tortuga para que quede mirando a la dcha
    t.fd(ancho_secciones_pista) # Avanza el ancho hasta la próxima sección


# Colorín colorado el código ha terminado :D