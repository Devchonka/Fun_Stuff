# Pile of Paper

# Challenge #214 Reddit Daily Programmer
# https://www.reddit.com/r/dailyprogrammer/comments/35s2ds/20150513_challenge_214_intermediate_pile_of_paper/

import CanvasClasses

def read_file(fname):
    with open(fname, 'r') as fileText:
        lines = [line.strip('\n') for line in fileText.readlines()]
    return lines

def main():
    fname_in = "colors.txt"
    fname_out = "output.txt"
    lines = read_file(fname_in)

    artistic_work = CanvasClasses.Canvas(int(lines[0].split(' ')[1]), int(lines[0].split(' ')[0]))

    for line in lines[1:]:
        parts = line.split(' ')
        artistic_work.add_paper(int(parts[0]), int(parts[1]), int(parts[2]),\
                                int(parts[3]), int(parts[4])) # +1 to get coordinate
    artistic_work.write_output(fname_out)
    artistic_work.showCanvas()


if __name__ == '__main__':
    main()