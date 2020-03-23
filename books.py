"""Main entry point"""
import argparse
import sys

import util

from book_file_reader import BookFileReader


def cmd_line_parse():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Display filtered and sorted list of books')

    parser.add_argument(
        '--filter',
        '-f',
        required=False,
        type=str,
        dest='filter',
        help='Show a subset of books, look for argument as a substring in any of the fields',
        default=None)

    parser.add_argument(
        '--year',
        '-y',
        required=False,
        action='store_true',
        dest='year_sort',
        help='Sort books by year, ascending, instead of default sort')

    parser.add_argument(
        '--reverse',
        '-r',
        required=False,
        action='store_true',
        dest='reverse_sort',
        help='Reverse sort')

    args = parser.parse_args()

    return args


def main():
    """
    Main entry point
    """
    # Start logger
    app_name = __file__.split('.')[0]
    module_logger = util.start_logger(app_name, 'controller')

    # Get command line args
    cmd_line_args = cmd_line_parse()

    # Move command line args to dictionary so other methods don't need to import argparse
    args = {
        'filter': cmd_line_args.filter,
        'year_sort': cmd_line_args.year_sort,
        'reverse_sort': cmd_line_args.reverse_sort}

    # Log command line args
    for key, value in args.items():
        msg = '{0} : {1}'.format(key, value)
        module_logger.info(msg)

    # Create book file reader object
    reader_obj = BookFileReader(module_logger, util.FILE_META_DATA, args)

    # Read input files & filter
    books = reader_obj.read_files()

    # display results to log file
    msg = ' '.join(sys.argv)
    module_logger.info(msg)
    print(msg)

    for book in books:
        msg = '{0}, {1}, {2}, {3}'.format(
            book['last_name'],
            book['first_name'],
            book['title'],
            book['publication_date'])
        module_logger.info(msg)
        print(msg)

    module_logger.info('<<<<< Done >>>>>')


if __name__ == '__main__':
    main()
    sys.exit(0)
