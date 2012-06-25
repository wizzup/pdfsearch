#!/usr/bin/python3
# Copyright 2012 Wisut Hantanong, GPL redistribution is allowed

import os, optparse, fnmatch

# global variables
OPTs = {}

def pdbg(*args):
    print('DBG: ', args)

def parse_args():
    global OPTs
    parser = optparse.OptionParser()

    parser.add_option('-d', '--directory', dest='directory', help='base directory for searching', metavar='DIR')
    parser.add_option('-m', '--match', dest='match', help='string for matching', metavar='MATCH')
    
    (OPTs, args) = parser.parse_args() 

    if args:
        print('Warning: unknown option {}'.format(*args)) 
        print('         --help for list of support options') 

    pdbg(OPTs)
    pdbg(args)

# generator code taken from active state python website
def locate(pattern, root=os.curdir):
    '''Locate all files matching supplied filename pattern in and below
    supplied root directory.'''
    pdbg(pattern, root)
    i = -1
    for path, dirs, files in os.walk(os.path.abspath(root)):
        i += 1
        if i==0: print('-',end='\r')
        if i==1: print('/',end='\r')
        if i==2: print('|',end='\r')
        if i==3: 
                print('\\',end='\r')
                i = -1 
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)

def search_pdf(pdf_file, match):
    print(pdf_file)# TODO: use Popen and grap console output
    os.system('pdftotext {} - | grep -i -c {}'.format(pdf_file, match))
    return 0 # retrun number of match

def main():
    os.system('clear') 
    print('pdfsearch.py version 0.0.1')
    print('Copyright 2012 Wisut Hantanong, GPL redistribution is allowed')

    parse_args()

    # if dir not provide searching for current dir
    search_dir = OPTs.directory

    print('searching for pdf files in {}'.format(search_dir))
    for i in locate('*.pdf', search_dir):
        search_pdf(i, 'fedora') 

if __name__ == '__main__': main()
