"""Class to read, filter and sort source data"""
import csv
from operator import itemgetter

class BookFileReader():
    """
    Class to read & parse input files
    """
    def __init__(self, module_logger, file_meta_data, args):
        """
        Constructor

        :param module_lgger     Logging module object
        :param meta_data        List of file dictionaries to read
                file_name   = file name to read
                delimiter   = field delimiter in that file
                col_mapping = mapped column name in solumn number order
                file_meta_data = [
                    {'file_name': 'csv',
                    'delimiter': ',',
                    'col_mapping': ['title', 'last_name', 'first_name', 'publication_date']},
                    {'file_name': 'pipe',
                    'delimiter': '|',
                    'col_mapping': ['first_name', 'last_name', 'title', 'publication_date']},
                    {'file_name': 'slash',
                    'delimiter': '/',
                    'col_mapping': ['publication_date', 'first_name', 'last_name', 'title']}]
         :param args             Command line arguments
                                    args = {
                                        'filter': cmd_line_args.filter,
                                        'year': cmd_line_args.year,
                                        'reverse': cmd_line_args.year}
        """
        self.module_logger = module_logger
        self.file_meta_data = file_meta_data
        self.args = args


    def read_files(self):
        """
        Read files specified by self.file_meta_data and return
        list of dictionaries with results.  Each dictionary
        has the keys: first_name, last_name, title and publication_date
        """
        # return a filtered list of dictionaries
        books = []

        # loop over each file name and delimiter
        for meta_data in self.file_meta_data:

            # map each column name to position in row
            first_name_col = meta_data['col_mapping'].index('first_name')
            last_name_col = meta_data['col_mapping'].index('last_name')
            title_col = meta_data['col_mapping'].index('title')
            pub_date_col = meta_data['col_mapping'].index('publication_date')

            # Read line by line using generator in case of very large file
            for row in self.read_file(meta_data['file_name'],
                                      meta_data['delimiter']):
                if row:
                    # filter this row if a filter was specified
                    keep_this_row = True
                    if self.args['filter']:
                        keep_this_row = self.filter_row(row)

                    # if filter successful or no filter specified, add this
                    # row to results set
                    if keep_this_row:
                        book = {'first_name': row[first_name_col].strip(),
                                'last_name': row[last_name_col].strip(),
                                'title': row[title_col].strip(),
                                'publication_date': row[pub_date_col].strip()}

                        books.append(book)

        # Sort books read from file
        sorted_books = self.sort_books(books)

        return sorted_books


    @staticmethod
    def read_file(file_name, delimiter):
        """
        Use native csv reader to read file line by line using a generator
        in case of large input file
        :param file_name    File to read
        :param delimiter    Field delimiter for this file
        """
        # pylint: disable=stop-iteration-return
        file_hdl = open(file_name)
        reader = csv.reader(file_hdl, delimiter=delimiter)
        while True:
            line = next(reader)
            if not line:
                file_hdl.close()
                break
            yield line

    def filter_row(self, row):
        """
        Return True if a single value in this row matches the filter, else return False
        """
        match = False

        for col in row:
            if self.args['filter'] in col:
                match = True
                break

        return match


    def sort_books(self, books):
        """
        Using command line arguments sort list of books that have
        been read from input files

        Return list of sorted books
        """
        if self.args['year_sort']:
            # sort by year
            if self.args['reverse_sort']:
                # sort desceding by year
                sorted_books = sorted(books, key=itemgetter('publication_date'), reverse=True)
            else:
                # sort ascending by year
                sorted_books = sorted(books, key=itemgetter('publication_date'))
        else:
            # not sort by year, sort by last_name
            if self.args['reverse_sort']:
                # soft descending by last_name
                sorted_books = sorted(books, key=itemgetter('last_name'), reverse=True)
            else:
                # sort ascending by last_name
                sorted_books = sorted(books, key=itemgetter('last_name'))

        return sorted_books
