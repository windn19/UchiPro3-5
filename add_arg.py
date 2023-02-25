import argparse


parser = argparse.ArgumentParser(description='Выводит сумму или среднее цифр')
parser.add_argument('numbers', nargs='+', type=int, help='111')
parser.add_argument('--avg', action='store_true', help='Выводит среднее, по умолчанию - сумму цифр')
args = parser.parse_args()
print(args)
total = sum(args.numbers)

print(total / len(args.numbers) if args.avg else total)
