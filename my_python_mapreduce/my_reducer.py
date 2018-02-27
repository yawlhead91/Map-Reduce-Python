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
    _lang_sorted_records = []


     # Here we get the tokenized dict for each
    # line
    for line in input_stream:
        _lang_sorted_records.append(get_key_value(line))

    # Sort langs to be group for the groupby function
    _lang_sorted_records.sort(key=lambda x:x['lang'])
    #print _lang_sorted_records

    
    # Sort line first by grouping by langs which return a new 
    # list for each then runing sorted lambda on the new list
    # on view finally appending to return list
    for k,v in groupby(_lang_sorted_records,key=lambda x:x['lang']):

        _page_group_sum = []

        l = list(v) # convert group interator
        l.sort(key=lambda x:x['page']) # sort again for next group

        for i, m in groupby(l,key=lambda x:x['page']):
            a = list(m)
            s = sum(int(item['view']) for item in a)

            _page_group_sum.append({
                'lang': k,
                'page': i,
                'view': s
            })
        
        r = []
        t = sorted(_page_group_sum, key=lambda k: k['view'])
        if len(t) > 5:
            r = t[-5:]
        else:
            r = t[-len(t):]
        
        rtn = rtn + r[::-1]

    
    # Write field to output stream
    for i in rtn:
        res = i['lang'] + '\t' + '(' + i['page'] + ',' + str(i['view']) + ')' + '\n'
        output_stream.write(res)
    

    return

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
