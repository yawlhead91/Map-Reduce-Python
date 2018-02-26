#!/usr/bin/python

# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import re
import sys
import codecs
from itertools import groupby

def get_key_value(line):

    # Return dic
    rtn = dict()

    line = line.replace('\n', '')
    # 1. Get rid of the end of line at the end of the string
    for ch in ['(',')']:
     line = line.replace(ch, '')

    # Remove the last comma deliter as in some cases the page
    # title holds a comma delitier
    line = line[::-1].replace(',', '\t', 1)[::-1]

    # 2. Split the string by the tabulator delimiter
    tokens = line.split('\t')

    rtn['lang'] = tokens[0]
    rtn['page'] = tokens[1]
    rtn['view'] = tokens[2]

    return rtn


# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(input_stream, num_top_entries, output_stream):

    rtn = []
    records = []

     # Here we get the tokenized dict for each
    # line
    for line in input_stream:
        records.append(get_key_value(line))

    # Sort langs to be group for the groupby function
    records.sort(key=lambda x:x['page'])

    # Sort line first by grouping by langs which return a new 
    # list for each then runing sorted lambda on the new list
    # on view finally appending to return list
    # for k, v in groupby(records,key=lambda x:x['page']):
    #     for key in v:
    #         print key['view']
        #s = sum(int(item['view']) for item in list(v))


    # # Write field to output4 stream
    # for i in rtn:
    #     res = i['lang'] + '\t' + '(' + i['page'] + ',' + i['view'] + ')' + '\n'
    #     output_stream.write(res)
    

    pass

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(debug, i_file_name, o_file_name, num_top_entries):
    # We pick the working mode:

    # Mode 1: Debug --> We pick a file to read test the program on it
    if debug == True:
        my_input_stream = codecs.open(i_file_name, "r", encoding='utf-8')
        my_output_stream = codecs.open(o_file_name, "w", encoding='utf-8')
    # Mode 2: Actual MapReduce --> We pick std.stdin and std.stdout
    else:
        my_input_stream = sys.stdin
        my_output_stream = sys.stdout

    # We launch the Map program
    my_reduce(my_input_stream, num_top_entries, my_output_stream)

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. Input parameters
    debug = True

    i_file_name = "sort_simulation.txt"
    o_file_name = "reduce_simulation.txt"

    num_top_entries = 5

    my_main(debug, i_file_name, o_file_name, num_top_entries)
