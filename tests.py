"""Unit test cases"""
import util
from book_file_reader import BookFileReader


def test_cases():
    """
    Unit test cases
    """
    #
    # arguments for each test case
    # NOTE: Order is critical as the expected results & test names
    #       must match the arguments
    #
    args = [
        # unit test case for: python books.py --filter 199 --reverse
        {'filter': '199', 'year_sort': None, 'reverse_sort': True},
        {'filter': 'er', 'year_sort': True, 'reverse_sort': None},
        {'filter': 'er', 'year_sort': False, 'reverse_sort': True},
        {'filter': '199', 'year_sort': True, 'reverse_sort': None},
        {'filter': None, 'year_sort': None, 'reverse_sort': None}
    ]

    expected_results = [
        ['McConnell, Steve, Code Complete, 1993',
         'Fowler, Martin, Refactoring, 1999'],

        ['Fowler, Martin, Refactoring, 1999',
         'Fowler, Martin, Patterns of Enterprise Application Architecture, 2002',
         'Beck, Kent, Implementation Patterns, 2007',
         'Martin, Robert, Clean Code, 2008'],

        ['Martin, Robert, Clean Code, 2008',
         'Fowler, Martin, Refactoring, 1999',
         'Fowler, Martin, Patterns of Enterprise Application Architecture, 2002',
         'Beck, Kent, Implementation Patterns, 2007'],

        ['McConnell, Steve, Code Complete, 1993',
         'Fowler, Martin, Refactoring, 1999'],

        ['Beck, Kent, Test-Driven Development, 2002',
         'Beck, Kent, Implementation Patterns, 2007',
         'Brooks, Fred, The Mythical Man-Month, 1975',
         'Crockford, Douglas, Javascript: The Good Parts, 2008',
         'Fowler, Martin, Refactoring, 1999',
         'Fowler, Martin, Patterns of Enterprise Application Architecture, 2002',
         'Martin, Robert, Clean Code, 2008',
         'McConnell, Steve, Code Complete, 1993',
         'Shore, James, The Art of Agile Development, 2008']
    ]

    test_names = [
        'test_filter_199_rev_sort',
        'test_filter_er_year',
        'test_filter_er_rev_sort',
        'test_filter_199_year',
        'test_show_all'
    ]

    # run each test case (args, expected results and test name)
    for i, _ in enumerate(args):
        run_test(args[i], expected_results[i], test_names[i])


def run_test(args, expected_results, test_name):
    """
    Using the input arguments (args) run the test and compare
    agains expected results (expected_results)
    :param  args               Simulated command line arguments
    :param  expected_results   Expected output results
    :param  test_name          Name of this test
    """
    app_name = __file__.split('.')[0]
    test_logger = util.start_logger(app_name, test_name)

    reader_obj = BookFileReader(test_logger, util.FILE_META_DATA, args)

    # Read input files & filter
    books = reader_obj.read_files()

    # 2 books should be returned
    assert len(books) == len(expected_results)

    # we want to check the order along with the contents
    # so, need to iterate over range-len
    for i, _ in enumerate(books):
        book = books[i]
        result = '{0}, {1}, {2}, {3}'.format(
            book['last_name'],
            book['first_name'],
            book['title'],
            book['publication_date'])

        assert result == expected_results[i]
