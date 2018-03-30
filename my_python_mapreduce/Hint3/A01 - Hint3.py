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

def process_line(line):
    
    # Tokenize words
    tokens = line.split(' ')

    # Check for the arabic case, thus the tokens
    # will be entered in a opposite index
    if tokens[0].isdigit():
        tokens = tokens[::-1]
        
    # Return dic
    rtn = ((tokens[0], tokens[1]), tokens[2])

    return rtn
  
# Filter function to check if the record
# is a member of the required langs set
def my_filter_function(key, languages):
    res = False
    
    for l in languages:
      if key.startswith(l):
        res = True
        break
        
    return res

def my_top_entries(t, data, n):
    res = []
    d = list(data)
    d = sorted(d, key=lambda x: int(x[1]))
    d = d[-n:]
    for i in d:
      res.append((t, i[0], i[1]))
    
    
    return res
    
    
  
  
# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(dataset_dir, o_file_dir, languages, num_top_entries):
  
  inputRDD = sc.textFile(dataset_dir)
  allWordsRDD = inputRDD.map(lambda x: process_line(x))
  reducedRDD = allWordsRDD.filter(lambda (x, y): my_filter_function(x[0], languages))\
               .reduceByKey(lambda x, y: x[1] + y[1])\
               .map(lambda (x, y): (x[0], (x[1], y)))\
               .groupByKey()\
               .flatMap(lambda x: my_top_entries(x[0], x[1], num_top_entries))\
               .map(lambda x: (x[0], (x[1], x[2]) ))\
               .sortBy(lambda a: a[0])
               

  reducedRDD.saveAsTextFile(o_file_dir)
  return


# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    dataset_dir = "/FileStore/tables/A01_my_dataset"
    o_file_dir = "/FileStore/tables/A01_my_result/"

    languages = ["en", "es", "fr"]
    num_top_entries = 5
    
    dbutils.fs.rm(o_file_dir, True)
  

    my_main(dataset_dir, o_file_dir, languages, num_top_entries)
