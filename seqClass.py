#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# if statement that exits function if length is 1

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()                 # Note we just added this line
if re.search('^[ACGTU]+$', args.seq): #if the sequence is only made of characters ACGTU
    if re.search('T', args.seq):
        print ('The sequence is DNA')  #if sequence has a T print 'sequence is DNA'
    elif re.search('U', args.seq):
        print ('The sequence is RNA')  #if sequence has a U prin 'sequence is RNA'
    else:
        print ('The sequence can be DNA or RNA') #if no T or U is present print 'sequence can be RNA or DNA'
else:
    print ('The sequence is not DNA nor RNA')  #if sequence is not DNA or RNA print 'The sequence is not DNA nor RNA'

#if statement that looks for motif

if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("found motif")
    else:
        print("NO motif found")

