import sys


from parser.parser_factory import TypeFactory


def main():

    format_ = sys.argv[1]
    files = sys.argv[2:]
    TypeFactory(format_)


if __name__ == '__main__':
    main()
