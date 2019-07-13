import math

phi = (1 + 5**.5)/2 #golden ratio


class Icosahedron:
    '''
    Icosahedron Vertice List:
    [+-1,   +-phi,       0]
    [0,       +-1,   +-phi]
    [+-phi,     0,     +-1]
    '''
    def __init__(self, scale):
         self.vertice_list = [
                             (1.0, phi, 0),
                             (-1.0, phi, 0),
                             (-1.0, -phi, 0),
                             (1.0, -phi, 0),
                             (0, 1.0, phi),
                             (0, -1.0, phi),
                             (0, -1.0, -phi),
                             (0, 1.0, -phi),
                             (phi, 0, 1.0),
                             (phi, 0, -1.0),
                             (-phi, 0, -1.0),
                             (-phi, 0, 1.0)
                            ]

if __name__ == "__main__" :
    ico = Icosahedron(1)
    print ico.vertice_list
