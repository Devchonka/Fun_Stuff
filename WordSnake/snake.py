class Snake(object):
    def __init__(self, words):  # class initializer (like constructor)
        self._words = words
        self._orientation = ['R', 'D', 'R', 'D', 'L', 'D', 'L']
        self._shape = zip(self._words, self._orientation)
        self._charLocationIn2D = [0, 0]  # The origin (0,0) is denoting the lefthand upper corner
                                         # down & right is positive sign

    def printShape(self):
        print(self._words[0])
        self._charLocationIn2D[0] += len(self._words[0])-1 # -1 for cutting off overlapping letter

        for word, orientation in list(self._shape)[1:]:
            # print(word, orientation)
            if orientation == 'R':  # right
                print(' ' * self._charLocationIn2D[0]+ word[1:])
                #import pdb; pdb.set_trace()
                self._charLocationIn2D[0] += len(word)-2
                # print(self._charLocationIn2D)
            elif orientation == 'D':  # down
                for letter in word[1:]:
                    print(' ' * self._charLocationIn2D[0]+ letter)
                self._charLocationIn2D[1] += len(word)-1
                # print(self._charLocationIn2D)
            elif orientation == 'L':
                print(' ' * (self._charLocationIn2D[0]-len(word)+1)+ word[:0:-1])
                self._charLocationIn2D[0] -= len(word)-1