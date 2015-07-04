# canvas classes for pile of paper problem

import numpy


class Canvas(object):
    def __init__(self, x_canvas_dim, y_canvas_dim):
        self._colors2areas = {0: x_canvas_dim * y_canvas_dim}
        self._masterpiece = numpy.zeros(shape=(x_canvas_dim, y_canvas_dim))

    def add_paper(self, color, y_coord, x_coord, width, height):
        # self._masterpiece[x_coord: 1 + width+x_coord][y_coord: 1 + height + y_coord] = color
        # self._colors2areas[color] +=1
        # self._colors2areas[self._masterpiece[x_coord: 1 + width+x_coord][y_coord: 1 + height + y_coord]] -= 1
        if color not in self._colors2areas:
                self._colors2areas[color] = 0

        for i in range(x_coord, 1 + width + x_coord):
            for j in range(y_coord, 1 + height + y_coord):
                self._colors2areas[self._masterpiece[j][i]] -= 1
                self._colors2areas[color] += 1
                self._masterpiece[j][i] = color


    def showCanvas(self):
        print(self._masterpiece)

    def show_color_counts(self):
        print(self._colors2areas)