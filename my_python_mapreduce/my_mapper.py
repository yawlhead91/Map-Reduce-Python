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

import sys
import codecs
from itertools import groupby

def process_line(line):
    # Return dic
    rtn = dict()
    # Tokenize words
    tokens = line.split(' ')

    # Check for the arabic case, thus the tokens
    # will be entered in a opposite index
    if tokens[0].isdigit():
        tokens = tokens[::-1]

    rtn['lang'] = tokens[0]
    rtn['page'] = tokens[1]
    rtn['view'] = tokens[2]

    return rtn



# ------------------------------------------
# FUNCTION my_map
# ------------------------------------------
def my_map(input_stream, languages, num_top_entries, output_stream):

    # This is an array of records in regards to
    # languages provided
    rtn = []
    records = []

    # Here we get the tokenized dict for each
    # line
    for line in input_stream:
        r = process_line(line)

        # Here we check to see if the record
        # is one of the languages provided
        for l in languages:
            if r['lang'].startswith(l):
                records.append(r)

    # Sort langs to be group for the groupby function
    records.sort(key=lambda x:x['lang'])

    # Sort line first by grouping by langs which return a new 
    # list for each then runing sorted lambda on the new list
    # on view finally appending to return list
    for k,v in groupby(records,key=lambda x:x['lang']):
        r = []
        t = sorted(v, key=lambda k: k['view'])
        if len(t) > 5:
            r = t[-5:]
        else:
            r = t[-len(t):]
        
        rtn = rtn + r[::-1]


    # Write field to output4 stream
    for i in rtn:
        res = i['lang'] + '\t' + '(' + i['page'] + ',' + i['view'] + ')' + '\n'
        output_stream.write(res)
    
    

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(debug, i_file_name, o_file_name, languages, num_top_entries):
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
    my_map(my_input_stream, languages, num_top_entries, my_output_stream)

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

    i_file_name = "../my_dataset/pageviews-20180219-100000_0.txt"
    o_file_name = "mapResult.txt"

    languages = ["en", "es", "fr"]
    num_top_entries = 5

    # 2. Call to the function
    my_main(debug, i_file_name, o_file_name, languages, num_top_entries)
