import sys


from parser.parser_factory import TypeFactory
from operation.file_operation import FileOperation
from operation.database_operation import Database


def main():

    format_ = sys.argv[1]
    files = sys.argv[2:]
    parser_type = TypeFactory(format_)
    parser = parser_type.get_parser()

    parser_files_objects = FileOperation(files)
    parsed_content = parser(parser_files_objects.get_content())
    parser_files_objects.save(parsed_content.get_content(), format_)

    mongo_database = Database()
    mongo_database.insert(parsed_content.get_content(), format_)


if __name__ == '__main__':
    main()
