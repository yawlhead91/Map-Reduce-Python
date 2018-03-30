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


def process_line(line, l_p):
    # Return dic
    rtn = ()
    # Tokenize words
    tokens = line.split(' ')

    # Check for the arabic case, thus the tokens
    # will be entered in a opposite index
    if tokens[0].isdigit():
        tokens = tokens[::-1]

    
    split = tokens[0].rsplit('.')
    lang = split[0]
    
    if len(split) > 1:
        proj = split[-1]
    else:
        proj = 'Wikipedia'
     
    
    if l_p == True:
      rtn = (lang, float(tokens[2]))
    else:
      rtn = (proj, float(tokens[2]))

    return rtn

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(dataset_dir, o_file_dir, per_language_or_project):
    # 1. We remove the solution directory, to rewrite into it
    inputRDD = sc.textFile(dataset_dir)
    flatWordsRDD = inputRDD.map(lambda x: process_line(x, per_language_or_project))
    
    flatWordsRDD.persist()
    total_views = flatWordsRDD.map(lambda x : x[1]).sum()
    print(total_views)
    reducedRDD = flatWordsRDD.reduceByKey(lambda x, y: x + y)\
                             .mapValues(lambda x: (int(x), (x/float(total_views)*100)))\
                             .sortBy(lambda a: a[0])
                                        
    reducedRDD.saveAsTextFile(o_file_dir)
	# Complete the Spark Job

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    dataset_dir = "/FileStore/tables/A01_my_dataset/"
    o_file_dir = "/FileStore/tables/A01_my_result/"

    per_language_or_project = True  # True for language and False for project
    
    dbutils.fs.rm(o_file_dir, True)
    my_main(dataset_dir, o_file_dir, per_language_or_project)
