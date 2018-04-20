# Hadoop Cheat Sheet

## Command Line Interface

*List files within the file system
```
#List files
hadoop fs -ls <args>

#Create directories in HDFS using path
hadoop fs -mkdir <path>

#Copy a file from localhost to HDFS
hadoop fs -copyFromLocal <localsrc> URI
```

## MRJob

[Mr-Job](https://github.com/Yelp/mrjob)

## Hadoop Components

*Name node: directs performance of the cluster
*Data node: stores blocks of data

### Other notes
HCatalog opens up the hive metadata to other mapreduce tools.

"Apache Hive is a data warehouse infrastructure built on top of Hadoop" - [Saggi Neumann](https://www.xplenty.com/blog/hive-vs-hbase/)


Credit: [David Wellman](https://www.slideshare.net/dwellman/practical-hadoop)
