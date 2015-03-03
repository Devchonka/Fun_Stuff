#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...
"""


def extract_names(fname):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """

    try:
        html = open(fname, 'rU')
    except IOError:
        print('Cannot open the file. \n')
    else:
        with html:
            text = html.read()
            match = re.search('Popularity\sin\s\d\d\d\d', text)
            year = match.group()[-4:]
            match = re.findall('(\d+)</td><td>(\w+)</td><td>(\w+)', text)

            rank = []
            boy = []
            girl = []
            for i in range(len(match)):
                rank.append(match[i][0])
                boy.append(match[i][1])
                girl.append(match[i][2])

            names_dict = {'rank' : rank, 'boy': boy, 'girl': girl}
    return year, names_dict


def write_summary_file(sum_fname):
    print (sum_fname)

def print_vals(year, names_dict):
    print(year)

    for iterable in range(len(names_dict['girl'])):
        print(names_dict['rank'][iterable],names_dict['boy'][iterable],names_dict['girl'][iterable])



def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('Wrong input, usage: [--summaryfile] baby_file_name.html [summary_file_name.txt]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
        if args[2]:
            sum_fname = args[2]
            del args[2]

    (year, names_dict) = extract_names(args[0])

    if summary:
        write_summary_file(sum_fname)
    else:
        print_vals(year,names_dict)


if __name__ == '__main__':
    main()