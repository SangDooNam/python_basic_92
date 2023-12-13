import sys
import getopt



def test_command(argv):
    sys.stdout.write('Useage -h | --help | -n: type in name here | --n: type in name here\n')
    short = 'hn:'
    long = ['help', 'name=']
    
    name_provided = False
    name = None
    
    try:
        opts, args = getopt.getopt(argv[1:], short, long)
    except getopt.GetoptError:
        sys.stdout.write('Useage -h | --help | -n: type in name here | --n: type in name here\n')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ['-h', '--help']:
            sys.stdout.write('112 for fire department 110 for police in Germany\n')

        if opt in ['-n', '--name']:
            name_provided = True
            name = arg
            
    if name_provided:
        sys.stdout.write(f'Good Morning {name}!\n')
    else:
        sys.stdout.write('Morning folks!\n')
        
    sys.exit(0)
    

argv = sys.argv
test_command(argv)