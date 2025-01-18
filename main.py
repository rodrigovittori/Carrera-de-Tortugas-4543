"""
# [M4.L1] Carrera de tortugas - Actividad # 5 "Tercer Jugador"

Objetivo: Agregar nuestra tercer participante

"""

import turtle

# VARIABLES GLOBALES
velocidad_corredores = 5 # Controla la velocidad de la animación (no a la que "corren", sino a la que las dibujamos)
cant_tortugas = 0 #contador con la cantidad de corredores
distancia_entre_tortugas = 40
y_inicial_tortugas = 80
x_inicial_tortugas = -230

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

###################################

# CREAR CORREDORES:

# PRIMERA
cant_tortugas += 1
primera = turtle.Turtle() # ROJA
primera.color("crimson")
primera.shape("turtle")
primera.speed(0)
primera.penup()
#primera.goto(-230, 80)
primera.goto(x_inicial_tortugas, (y_inicial_tortugas - (distancia_entre_tortugas * (cant_tortugas - 1))))
primera.speed(velocidad_corredores)

# SEGUNDA
cant_tortugas += 1
segunda = turtle.Turtle() # AZUL
segunda.color("navy")
segunda.shape("turtle")
segunda.speed(0)
segunda.penup()
#segunda.goto(-230, 40)
segunda.goto(x_inicial_tortugas, (y_inicial_tortugas - (distancia_entre_tortugas * (cant_tortugas - 1))))
segunda.speed(velocidad_corredores)

# TERCERA
cant_tortugas += 1
tercera = turtle.Turtle() # AMARILLA
tercera.color("gold")
tercera.shape("turtle")
tercera.speed(0)
tercera.penup()
#tercera.goto(-230, 0)
tercera.goto(x_inicial_tortugas, (y_inicial_tortugas - (distancia_entre_tortugas * (cant_tortugas - 1))))
tercera.speed(velocidad_corredores)

# Colorín colorado el código ha terminado :D