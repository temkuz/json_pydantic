from argparse import ArgumentParser

from .conventer import run


def parse_args():
    default_parser = ArgumentParser()

    default_parser.add_argument('-i', '--input', help='Input file', required=True)
    default_parser.add_argument('-o', '--output', help='Output file', required=True)
    default_parser.add_argument('-n', '--name', help='First class name. Default "Root"', default='Root')

    return default_parser.parse_args()


def main():
    args = parse_args()
    run(args.input, args.output, args.name)


if __name__ == '__main__':
    main()
