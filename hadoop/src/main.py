#!/usr/bin/env python
"""
# Author:  Bryan Dieudonne

"""

from mrjob.job import MRJob        # MRJob library
import re                          #regular expression library
import gscquery
import subprocess
import os
import psycopg2

#returns string of current directory of file
dir_path = os.path.dirname(os.path.realpath(__file__))

def check_hadoop():
    """ Check if hadoop is on. Turn on hadoop if off"""

    ## Check if Hadoop is runnning <-- fix this later April 7th, 2018 2:30 pm
    hadoop_status = False
    #add  do while to this after
    #check_hadoop = subprocess.check_output(["hadoop version"]) # fix logic

    while(!hadoop_status): #<-- when do I implement exception handling?
        #process this ouput for a string in the stdout"
        subprocess.run("../run_hadoop.sh")
        return True
        break
    if (!hadoop_status):
        ## run this if hadoop is off
    else:
        ## run this if hadoop is on:

def push_GSC_onto_HDFS(program,URI,start_date,end_date):
    """
    Download Unsampled Google Search Console Data onto HDFS.
    Parameters:
    @Program    - file path of python script
    @URI        - the domain for Google Search Console
    @start_date - date string
    @end_date   - date string
    """
    create_hdfs_dir = "hadoop fs -mkdir /csv_web"
    copyTohadoop = "hadoop fs -copyFromLocal ./%s /web_data"  %(dir_path)# fix this <-- add user input

    #Pull GSC data into local file
    subprocess.run([program,URI,start_date,end_date])
    ## check if filepath exits
        # if filepath does not exist create the file PATH
    subprocess.run(create_hdfs_dir)
    subprocess.run(copyTohadoop)

def postgres_process():
    """ Insert data into PostGres & transform the data using psycopg2 """

    host = "localhost"
    db   = "postgres"
    usr  = "postgres"
    server = psycopg2.connect("host=%s dbname=%s user=%s") %(host,db,usr)  # insert host dbname & user for Postgres instance

    ## create a table in PostGres





    obj = server.cursor
    with open('##csv file name##','r') as file:
        next(file)
        obj.copy_from(file,)


def main():
    """ Implement Rhea's data transformation- One-time use """

    ## Set the parameeters ##
    program = "python ./gscquery.py"  # filepath = "${HOME}/antimoz/hadoop"
    domain = "outspokenmedia.com"     # <-- make user input ?
    start_date = "2018-01-01"         # prompt CMD line input / sample <- complete later
    end_date = "2018-03-30"           #

    hadoop_on = check_hadoop()        # debug this
    if (!hadoop_on):
        ## run this is hadoop is not on
    else:
        push_GSC_onto_HDFS(program,URI,start_date,end_date) ## Pull GSC  data & push csv file into HDFS
        postgres_process()                                  ## Import CSV file into postgres

if __name__ == '__main__':
    main()
