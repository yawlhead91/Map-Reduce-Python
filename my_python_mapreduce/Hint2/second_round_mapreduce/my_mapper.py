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


total_views = 21996631

def process_line(line):
    # Return dic
    rtn = dict()
    # Tokenize words
    tokens = line.split(' ')

    # Check for the arabic case, thus the tokens
    # will be entered in a opposite index
    if tokens[0].isdigit():
        tokens = tokens[::-1]

    
    split = tokens[0].rsplit('.')
    rtn['lang'] = split[0]
    if len(split) > 1:
        rtn['project'] = split[-1]
    else:
        rtn['project'] = 'Wikipedia'
     
    rtn['page'] = tokens[1]
    rtn['view'] = tokens[2]

    return rtn 



# ------------------------------------------
# FUNCTION my_map
# ------------------------------------------
def my_map(input_stream, target, output_stream):

    # This is an array of records in regards to
    # languages provided
    rtn = {}

    # Here we get the tokenized dict for each
    # line
    for line in input_stream:
        r = process_line(line)
        
        # Add the return data fields
        if r[target] not in rtn:
            rtn[r[target]] = (0.0,0.0) 

        
        views = float(rtn[r[target]][0]) + float(r['view'])
        percentage = (views/total_views)*100
        rtn[r[target]] = (int(views), percentage)
    

    # Write field to output4 stream
    for i in rtn:
        res = i + '\t' + '(' + str(rtn[i][0]) + ', ' + str(rtn[i][1]) + ')' + '\n'
        output_stream.write(res)
    

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(debug, i_file_name, o_file_name, target):
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
    my_map(my_input_stream, target, my_output_stream)

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

    calc = ['project', 'lang']

    i_file_name = "../../../my_dataset/pageviews-20180219-100000_0.txt"
    o_file_name = "mapResult.txt"

    for target in calc:
        o_file_name = target + '_' + o_file_name
        my_main(debug, i_file_name, o_file_name, target)
