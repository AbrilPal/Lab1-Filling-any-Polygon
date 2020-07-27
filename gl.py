# Andrea Abril Palencia Gutierrez, 18198
# Lab1: Filling any Polygon --- Graficas por computadora, seccion 20
# 20/07/2020 - 27/07/2020

# libreria
import struct

# para especificar cuanto tamaño quiero guardar en bytes de cada uno
def char(c):
    # solo un byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    # solo 2 bytes
    return struct.pack('=h', w)

def dword(d):
    # solo 4 bytes
    return struct.pack('=l', d)

def convertir(co):
    # 1 ------ 255
    # x ------ y
    color_r = co * 255
    return int(color_r)
    
def color(r, g, b):
    return bytes([b, g, r])

# colores predeterminados
rosado = color(250,229,251)
negro = color(0,0,0)
blanco = color(255,255,255)

# clase principal
class Render(object):
    # inicializa cualquier objeto dentro de la clase Render
    def __init__(self, ancho, alto):
        # ancho de la imagen
        self.ancho = ancho
        # alto de la imagen
        self.alto = alto
        # color predeterminado del punto en la pantalla
        self.punto_color = negro
        # color de fondo de la imagen
        self.glClear()

    def glViewPort(self, x, y, ancho, alto):
        self.viewport_x = x
        self.viewport_y = y
        self.viewport_ancho = ancho
        self.viewport_alto = alto

    # fondo de toda la imagen
    def glClear(self):
        # color de fondo
        #color_fondo = color_f
        self.pixels = [[rosado for x in range(self.ancho)] for y in range(self.alto)]

    # crear un punto en cualquier lugar de la pantalla 
    def glvertice(self, x, y):
       # xw = int((x + 1) * (self.viewport_ancho/2) + self.viewport_x)
       # yw = int((y + 1) * (self.viewport_alto/2) + self.viewport_y)
        self.pixels[x][y] = self.punto_color

    # permite cambiar el color del punto
    # def glColor(self, color_p):
       # self.punto_color = color_p

    # hacer lineas
    def  glLine( self , x0 , y0 , x1 , y1 ):
        # coordenasdas en pixeles
        # x0 = int((x0 + 1) * (self.viewport_ancho/2) + self.viewport_x)
        # y0 = int((y0 + 1) * (self.viewport_alto/2) + self.viewport_y)
        # x1 = int((x1 + 1) * (self.viewport_ancho/2) + self.viewport_x)
        # y1 = int((y1 + 1) * (self.viewport_alto/2) + self.viewport_y)

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        inclinado = dy > dx

        if inclinado:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        desplazamiento = 0
        limit = 0.5
        
        # si es division por cero el programa no ejecuta nada
        try:
            m = dy/dx
            y = y0

            for x in range(x0, x1 + 1):
                if inclinado:
                    self.glvertice(y, x)
                else:
                    self.glvertice(x, y)

                desplazamiento += m
                if desplazamiento >= limit:
                    y += 1 if y0 < y1 else -1
                    limit += 1
        except ZeroDivisionError:
            pass

    # dibujar los poligonos
    def Poligonos(self, vertices):
        self.vertices = vertices
        for vertice in range(0, len(self.vertices)):
            x0 = self.vertices[vertice][0]
            y0 = self.vertices[vertice][1] 
            if vertice + 1 < len(self.vertices):
                x1 = self.vertices[vertice + 1][0]
            else:
                 self.vertices[0][0]
            if vertice + 1 < len(self.vertices):
                y1 = self.vertices[vertice + 1][1] 
            else:
                 self.vertices[0][1]
            self.glLine(x0, y0, x1, y1)
            for x in range(self.ancho):
                for y in range(self.alto):
                    if self.Regla(x, y): self.glvertice(x, y)

    # regla impar-par
    def Regla(self, x, y):
        num = len(self.vertices) - 1
        si = False
        for i in range(len(self.vertices)):
            x0 = self.vertices[i][0]
            y0 = self.vertices[i][1]
            x1 = self.vertices[num][0]
            y1 = self.vertices[num][1]
            if ((y0 > y) != (y1 > y)) and (x < x0 + (x1 - x0) * (y - y0) / (y1 - y0)):
                si = not si
            num = i
        return si

    # escribe el archivo
    def glFinish(self, name):
        imagen = open(name, 'wb')
        imagen.write(bytes('B'.encode('ascii')))
        imagen.write(bytes('M'.encode('ascii')))
        imagen.write(dword(14 + 40 + self.ancho * self.alto * 3))
        imagen.write(dword(0))
        imagen.write(dword(14 + 40))
        imagen.write(dword(40))
        imagen.write(dword(self.ancho))
        imagen.write(dword(self.alto))
        imagen.write(word(1))
        imagen.write(word(24))
        imagen.write(dword(0))
        imagen.write(dword(self.ancho * self.alto * 3))
        imagen.write(dword(0))
        imagen.write(dword(0))
        imagen.write(dword(0))
        imagen.write(dword(0))

        for x in range(self.alto):
            for y in range(self.ancho):
                imagen.write(self.pixels[x][y])

        imagen.close()
