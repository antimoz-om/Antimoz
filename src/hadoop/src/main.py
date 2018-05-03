#!/usr/bin/env python
"""
# Author:  Bryan Dieudonne

A script to pull data from Google Search Console (G) & Google Analytics
& push into a Postgres table
"""

import gscquery
import subprocess
import os
import psycopg2

#returns string of current directory of file
dir_path = os.path.dirname(os.path.realpath(__file__))

def run_hadoop():
    """ Check if hadoop is on. Turn on hadoop if off"""

    ## Check if Hadoop is runnning <-- fix this later April 7th, 2018 2:30 pm
    hadoop_status = False
    #add  do while to this after
        check_hadoop = subprocess.check_output(["hadoop version"]) # fix logic

    while(!hadoop_status): #<-- when do I implement exception handling?
        subprocess.run("../run_hadoop.sh")
        # subprocess.run("hadoop") # need to check if hadoop is on
        break

def push_GSC_onto_HDFS(program,URI,start_date,end_date):
    """
    Download Unsampled Google Search Console Data & Push onto HDFS.
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
    # check if filepath exits
        ## if filepath does not exist create the file PATH
    subprocess.run(create_hdfs_dir)
    subprocess.run(copyTohadoop)

def run_postgres_process():
    """ Insert csv file data into PostGres & transform the data using psycopg2 """

    #add in request for user input
    host = "localhost"
    db   = "postgres"
    usr  = "postgres"

    #check if database if represent
    #if db is not present then need to create a table <<-- need to implement

    server = psycopg2.connect("host=%s dbname=%s user=%s") %(host,db,usr)  # insert host dbname & user for Postgres instance
    data = server.cursor
    #cmd = insert execute command here

    ## create a table in Postgres called 'GoogleSearchConsole'
        ## how
    data.execute("""
    CREATE TABLE GSC_URLs (
        id integar PRIMARY KEY
        Date_Time text
        Clicks integer
        Impressions number
        CTR float
        Position float
        )
    """)

    ## add data to table
    with open('output.csv','r') as file:
        next(file)
        next(file)
        # if line in document contains string "totals" skip to next line
        data.copy_from(file, 'GoogleSearchConsole', sep='\t')
        #stop if 'file'
    data.commit()
    #add test code

def main():
    """ Implement Rhea's data transformation- One-time use """

    ## Set the parameeters ##
    program = "python ./gscquery.py"  # filepath = "${HOME}/antimoz/hadoop"
    domain = "outspokenmedia.com"     # <-- make user input ?
    start_date = "2018-01-01"         # prompt CMD line input / sample <- complete later
    end_date = "2018-03-30"           #

    ## Implement this this
    run_hadoop()
    push_GSC_onto_HDFS(program,URI,start_date,end_date)
    run_postgres_process()   #debug this     ## Import CSV file into postgres



if __name__ == '__main__':
    main()
