#!/usr/bin/python
"""
This is my solution to the puzzle for one of Google Python Eng Ed classes.
Fragments of an imagine are thrown across the web, and the idea of this puzzle is to
put the pieces together and discover the complete image.

The idea is to learn about the urllib module.

Google's Python Class:
http://code.google.com/edu/languages/google-python-class/

Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images to reconstruct an original image.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
import os
import re
import sys
import urllib.request


def read_urls(fname):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""

    puzzle_urls = []

    with open(fname, 'rU') as html:
        text = html.read()
        puzzle_urls = sorted(set(re.findall('GET\s(\S+/puzzle/\S+)\sHTTP', text)))
        puzzle_urls = ['http://code.google.com' + url for url in puzzle_urls]

    return puzzle_urls


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print('Created new folder for images.')
    else:
        print('Adding images to existing folder')

    # retrieve images and download them into newly created folder
    with open(os.path.join(dest_dir, 'index.html'), 'w') as merged_file:
        merged_file.write('<html><body>\n')
        for counter, url in enumerate(img_urls):
            try:
                local_name = dest_dir + '/img' + str(counter) + '.jpg'
                urllib.request.urlretrieve(url, local_name)
                print('Retrieving image #', counter)
                merged_file.write('<img src = "%s"' %(local_name) +">")
            except ValueError:
                print('Skipping un-retrievable URL image.')

        merged_file.write('\n</body></html>\n')

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
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()