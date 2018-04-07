#! /usr/bin/env python
###################################

# MapReduce Job in Python
# Bring in Google Search console
# & Google Analytics data
# save raw file in HDFS
# process the file with MR-Job
# send o to HIVE data store

# Mr-Job features

####################################

from mrjob.job import MRJob        # MRJob library
import re                          #regular expression library
import gscquery
import subprocess

####################################



####################################
## Check if Hadoop is runnning
##

# hadoop_on = subprocess.run("hdfs ")
if (!hadoop_on):
    ## run this if hadoop is off
else:
    ## run this if hadoop is on

    ####################################
    ## Download Unsampled Google Search Console Data
    ## onto the HDFS
    ##

    #execute gscquery.main
    #need to pass ENV varibals for arguments
    bashCMD = "${HOME}/"
    def push_GSC_onto_HDFS(gscquery.main(), bashCMD)
        "save file to commane"

        return
