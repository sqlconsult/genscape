# Genscape Coding Challenge

> Solution for Genscape coding challenge.

> This solution using Python 3.5.2 reads in records from various input files 
> and then outputs the list with command line options to sort or filter them.

## Solution Files

1. books.py
-     Main entry point
      Sample execution command: python books.py or python books.py -f 199 -r
      In addition to writing results to STDOUT this solution also creates a 
      log file with a time stamp in the 'logs' directory.
2. logger.py
-      Logging module
3. book_file_reader.py
-      Class to read, filter and sort source data
4. util.py
-      Input file meta data and method to start logger
5. README.txt
-      Coding challenge statement & requirements
6. tests.py
-      pytest unit test cases
7. run_tests.sh
-      Runs test cases
8. csv, pipe and slash
-      Input files