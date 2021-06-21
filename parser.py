import sys


from parser.parser_factory import TypeFactory
from .file_operation import FileOperation


def main():

    format_ = sys.argv[1]
    files = sys.argv[2:]
    parser_type = TypeFactory(format_)
    parser = parser_type.get_parser()

    parser_files_objects = FileOperation(files)


if __name__ == '__main__':
    main()
