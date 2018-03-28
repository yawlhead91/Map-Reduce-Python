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

    rtn['item'] = tokens[0]
    rtn['views'] = tokens[1]
    rtn['percentage'] = tokens[2]

    return rtn


# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(input_stream, target, output_stream):

    rtn = {}

     # Here we get the tokenized dict for each
    # line
    for line in input_stream:
        k = get_key_value(line)

        # Add the return data fields
        if k['item'] not in rtn:
            rtn[k['item']] = (0.0,0.0)
        
        views = float(rtn[k['item']][0]) + float(k['views'])
        percentage = float(rtn[k['item']][1]) + float(k['percentage'])
        rtn[k['item']] = (int(views), percentage)

    
    # Write field to output4 stream
    # To sort the list in place...
    r = []
    for item in rtn:
        t = {}
        t['item'] = item
        t['view'] = rtn[item][0]
        t['perc'] = rtn[item][1]
        r.append(t)

    r = sorted(r, key=lambda x: x['perc'], reverse=True) 
    for i in r:
        res = i['item'] + '\t' + '(' + str(i['view']) + ', ' + str(i['perc']) + '%)' + '\n'
        output_stream.write(res)
    

    return

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
    my_reduce(my_input_stream, target, my_output_stream)

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
    o_file_name = "reduce_simulation_projects.txt"

    calc = ['project', 'lang']

    for target in calc:
        ii_file_name = target + '_' + i_file_name
        oo_file_name = target + '_' + o_file_name
        my_main(debug, ii_file_name, oo_file_name, target)


    
