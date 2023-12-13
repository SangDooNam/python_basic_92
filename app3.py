import argparse


parser = argparse.ArgumentParser(description='Display first name, last name and age',
                            formatter_class=argparse.ArgumentDefaultsHelpFormatter
                            )

parser.add_argument('first_name', nargs='?', type=str, help='first_name to print first name', default='Larry')
parser.add_argument('last_name',nargs='?', type=str, help='last_name to print last name', default='Hanson')
parser.add_argument('age', nargs='?', type=int, help='age to print age', default= 100)

parser.add_argument('--fast', action='store_true', help='Enable fast mode')

args = parser.parse_args()

first_name = args.first_name
last_name = args.last_name
age = args.age
if args.fast:
    print('Fast mode enabled')

print(f'Hello {first_name} {last_name}! I see that you have had {age + 1} birthdays.')