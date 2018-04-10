#!/usr/bin/env python
"""
# Author:  Bryan Dieudonne

# MapReduce Job in Python
# Bring in Google Search console
# & Google Analytics data
# save raw file in HDFS
# process the file with MR-Job
# send to HIVE data store
# process data
"""

from mrjob.job import MRJob        # MRJob library
import re                          #regular expression library
import gscquery
import subprocess
import os

#returns
dir_path = os.path.dirname(os.path.realpath(__file__))

def push_GSC_onto_HDFS(program,URI,start_date,end_date):
    """
    Download Unsampled Google Search Console Data onto HDFS.
    Parameters:
    @Program    - file path of python script
    @URI        - the domain for Google Search Console to use
    @start_date - date string
    @end_date   - date string
    """
    create_hdfs_dir = "hadoop fs -mkdir /web_data"
    copyTohadoop = "hadoop fs -copyFromLocal ./(downloaded) /web_data" # fix this <-- add user input

    #Pull GSC data into local file
    subprocess.run([program,URI,start_date,end_date])
    ## check if filepath exits
        # if filepath does not exist create the file PATH
    subprocess.run(create_hdfs_dir)
    subprocess.run(copyTohadoop)

def hive_process():
    """
    This function will
    """

def postgres_process():
    """
    Insert data into PostGres & transform the data
    """

def

def main():
    """ implement Rhea's data transformation""" 


    ## Check if Hadoop is runnning <-- fix this later April 7th, 2018 2:30 pm
    bool hadoop_on = False
    #add  do while to this after
    check_hadoop = subprocess.check_output(["hadoop version"]) # fix logic
    while(!hadoop_on):
        ## check if hadoop on
        #process this ouput for a string in the stdout"
        subprocess.run("../run_hadoop.sh")
        break

    if (!hadoop_on):
        ## run this if hadoop is off
    else:
        ## run this if hadoop is on

        program = "python ./gscquery.py"
        #filepath = "${HOME}/antimoz/hadoop"
        domain = "outspokenmedia.com"
        #prompt CMD line input / sample <- complete later
        start_date = "2018-01-01"
        end_date = "2018-03-30"

        ## Get web data from GSC & store csv file in HDFS
        push_GSC_onto_HDFS(program,URI,start_date,end_date)
        #run hive command to add data to to Hive metadata
        postgres_process()

if __name__ == '__main__':
    main()
