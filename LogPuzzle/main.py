#!/usr/bin/python
"""
This is my solution to the puzzle for one of Google Python Eng Ed classes.
Fragments of an imagine are thrown across the web, and the idea of this puzzle is to
put the pieces together and discover the complete image.

The idea is to learn the urllib module.

Google's Python Class:
http://code.google.com/edu/languages/google-python-class/

Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
import os
import re
import sys
import urllib


def read_urls(fname):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""

    puzzle_urls = []

    try:
        html = open(fname, 'rU')
    except IOError:
        print('Cannot open the file. \n')
        exit(1)
    else:
        with html:
            text = html.read()
            puzzle_urls = re.findall('GET\s(\S+/puzzle/\S+)\sHTTP', text)

            import pdb
            pdb.set_trace()

    return puzzle_urls


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    pass


def main():
    args = sys.argv[1:]

    if not args:
        print('Incorrect command line args. Usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        pass
        # print ('\n'.join(img_urls))


if __name__ == '__main__':
    main()