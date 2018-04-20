#
# Author: Bryan Dieudonne
#
#



# Build pseudo-distrubuted Hadoop 2.3
FROM harisekhon/hadoop:2.3
MAINTAINER bdieu178

ARG PIG_VERSION=0.16.0
ARG HIVE_VERSION=2.3.3

# hadoop-common fixes
ENV PATH $PATH:$HADOOP_PREFIX/bin

# Add pig layer MR Jobs
RUN curl -s http://apache.mirror.anlx.net/pig/pig-${PIG_VERSION}/pig-${PIG_VERSION}.tar.gz | tar -xz -C /usr/local
ENV PIG_HOME /usr/local/pig-${PIG_VERSION}/
RUN ln -s $PIG_HOME /usr/local/pig
ENV PATH $PATH:$PIG_HOME/bin

# Add hive layer for SQL Queries on Hadoop
RUN curl -s http://apache.mirror.anlx.net/hive/hive-${HIVE_VERSION}/apache-hive-${HIVE_VERSION}-bin.tar.gz  | tar -xz -C /usr/local
ENV HIVE_HOME /usr/local/apache-hive-${HIVE_VERSION}-bin/
RUN ln -s $HIVE_HOME /usr/local/hive
ENV PATH $PATH:$HIVE_HOME/bin

#add PostGres datastore & Python --> test this
RUN yum -y update
RUN yum -y install postgresql-server postgresql-contrib
#RUN postgresql-setup initdb
RUN yum -y install yum-utils
RUN yum -y groupinstall development
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm
RUN yum -y install python36u
#(insert assert function here)

RUN apt-get install -y python3.5 python3.5-dev python3-pip python-dev python3-dev postgresql postgresql-server-dev-all sudo


#add Psycopg library <--processing csv files into PostGres.
RUN pip install -U pip
RUN pip install psycopg2-binary
