# Andrea Abril Palencia Gutierrez, 18198
# Lab1: Filling any Polygon --- Graficas por computadora, seccion 20
# 20/07/2020 - 27/07/2020

from gl import Render, color, convertir

imagen = Render(800, 460)
print("Esto suele tardar un poco!!!")
pol1 = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]
imagen.glColor(color(215, 189, 226))
imagen.Poligonos(pol1)
pol2 = [(321, 335), (288, 286), (339, 251), (374, 302)]
imagen.glColor(color(171, 235, 198))
imagen.Poligonos(pol2)
pol3 = [(377, 249), (411, 197), (436, 249)]
imagen.glColor(color(249, 231, 159))
imagen.Poligonos(pol3)
pol4 = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52), (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180)]
imagen.glColor(color(248, 201, 251))
imagen.Poligonos(pol4)
pol5 = [(682, 175), (708, 120), (735, 148), (739, 170)]
imagen.glColor(color(248,249,249))
imagen.Poligonos(pol5)
imagen.glFinish('poligonos.bmp')
print("¡Listo! La imagen esta creada con el nombre de 'poligonos.bmp'.")
