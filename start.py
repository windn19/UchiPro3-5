import argparse


parser = argparse.ArgumentParser(description='Вывод аргументов')
parser.add_argument('arg')
args = parser.parse_args()
print(args)
print(args.arg)
