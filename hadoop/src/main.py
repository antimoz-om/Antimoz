#!/usr/bin/env python
"""

# Author:  Bryan Dieudonne

# MapReduce Job in Python
# Bring in Google Search console
# & Google Analytics data
# save raw file in HDFS
# process the file with MR-Job
# send to HIVE data store

"""

from mrjob.job import MRJob        # MRJob library
import re                          #regular expression library
import gscquery
import subprocess
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def push_GSC_onto_HDFS(program,URI,start_date,end_date):
    """
    Download Unsampled Google Search Console Data onto HDFS.
    Parameters:
    @Program
    @URI
    @start_date
    @end_date
    """
    #Pull GSC data
    subprocess.run([program,URI,start_date,end_date])

    ## check if filepath exits
        # if filepath does not exist create the file PATH

    copyTohadoop = "hadoop fs -copyFromLocal ${localfile}" # fix this
    subprocess.run(copyTohadoop)


def main():

    ## Check if Hadoop is runnning <-- fix this later April 7th, 2018 2:30 pm
    bool hadoop_on = False
    #add  do while to this after
    check_hadoop = subprocess.check_output(["hadoop version"]) # fix logic
    while(!hadoop_on):
        ## check hadoop
        #process this ouput for a string in the stdout"
        #hadoop_on = True
        subprocess.run("../run_hadoop.sh")
        break

    if (!hadoop_on):
        ## run this if hadoop is off
    else:
        ## run this if hadoop is on
        program = "python ./gscquery.py"
        #filepath = "${HOME}/antimoz/hadoop"
        domain = "outspokenmedia.com"

        #prompt CMD line input
        start_date = "2018-01-01"
        end_date = "2018-03-30"

        ## add request for command line

        push_GSC_onto_HDFS(program,URI,start_date,end_date)
        #run hive command
        subprocess.run()

        break




if __name__ == '__main__':
    main()
