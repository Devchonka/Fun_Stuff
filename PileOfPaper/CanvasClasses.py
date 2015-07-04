
# canvas classes for pile of paper problem

#sample input: 1 5 5 10 3

import numpy

class Canvas(object):
    def __init__(self, x_canvas_dim, y_canvas_dim):
        self._colors_areas = None
        self._masterpiece = numpy.zeros(shape=(x_canvas_dim, y_canvas_dim))

    def add_paper(self, color, y_coord, x_coord, width, height):
        #import pdb; pdb.set_trace()

        #for i in range(x_coord, 1 + width+x_coord):
            #for j in range(y_coord, 1 + height + y_coord):
                #self._masterpiece[j][i] = color

        # self._masterpiece[y_coord: 1 + height + y_coord][x_coord: 1 + width+x_coord] = color
        self._masterpiece[x_coord: 1 + width+x_coord][y_coord: 1 + height + y_coord] = color

    def showCanvas(self):
        print(self._masterpiece)

    def count_areas(self):
        num = numpy.bincount(self._masterpiece)
        count = numpy.nonzero(num)[0]
        self._colors_areas = zip(num, count)

    def write_output(self, fname):
        self.count_areas()
        with open(fname, 'w') as colorsOutput:
            colorsOutput.write(self._colors_areas)
