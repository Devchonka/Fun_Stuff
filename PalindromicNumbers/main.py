# this file contains how to count number of iterations for palindromic numbers
# Reddit daily programmer challenge link is below:
# http://www.reddit.com/r/dailyprogrammer/comments/38yy9s/20150608_challenge_218_easy_making_numbers/

#!/usr/bin/env

def read_file(fname):
    with open(fname) as inputFile:  # file gets closed automatically
        numbers = [int(line.strip('\n')) for line in inputFile.readlines()]
    return numbers

def add_reverse(num):
    return num + int(str(num)[::-1])

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def iterate_palindrome(num):  # iterative repetition till palindrome, keeping number of iterations
    num_iter = 0
    while not is_palindrome(num):
        num = add_reverse(num)
        num_iter+=1
    return num_iter, num

def main():
    fname = 'palindromic_numbers.csv'
    numbers = read_file(fname)

    for num in numbers:
        num_iter, resulting_palindrome = iterate_palindrome(num)
        print('After {} iterations of number {}, resulting palindrome is {}.'.\
              format(num_iter, num, resulting_palindrome))
    return

if __name__ == '__main__':
    main()

