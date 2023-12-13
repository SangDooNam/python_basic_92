import sys
import argparse


args = sys.argv

print('Useage: -h | --help | -f | --fast ')
if  '-h' in args[1:] or '--help' in args[1:]:
    sys.stdout.write('112 for fire department 110 for police in Germany\n')

if '-f' in args[1:] or '--fast' in args[1:]:
    sys.stdout.write("fast mode enabled\n")

elif args[1:] and (not '-f' in args[1:] or not '--fast' in args[1:]):
    sys.stdout.write("slow mode enabled\n")



