#!/usr/bin/env python
###################################

# Author:  Bryan Dieudonne

# MapReduce Job in Python
# Bring in Google Search console
# & Google Analytics data
# save raw file in HDFS
# process the file with MR-Job
# send o to HIVE data store

####################################

from mrjob.job import MRJob        # MRJob library
import re                          #regular expression library
import gscquery
import subprocess
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    ####################################
    ## Check if Hadoop is runnning
    bool hadoop_on = False
    #add  do while to this after
    while(!hadoop_on):
        ## check hadoop
        if this runs true <-- (subprocess.run(["hadoop version"]))
        hadoop_on = True
        break

    ####################################
    ##
    if (!hadoop_on):
        ## run this if hadoop is off
    else:
        ## run this if hadoop is on
        program = "python ${HOME}/antimoz/hadoop/gscquery.py"
        filepath = "${HOME}/antimoz/hadoop"
        domain = "outspokenmedia.com"
        start_date = "2018-01-01"
        end_date = "2018-03-30"

        def push_GSC_onto_HDFS(program,URI,start_date,end_date):
            """
            Download Unsampled Google Search Console Data onto HDFS.
            Parameters:
            @Program
            @URI
            @start_date
            @end_date
            """
            #launch bash CMD
            subprocess.run([program,URI,start_date,end_date])

            ## check if filepath exits
                # if filepath does not exist create the file PATH

            copyTohdfs = "hdfs f -CopyToLocal {file path..}" # fix this



        #run hive command
        subprocess.run()




if __name__ == '__main__':
    main()
