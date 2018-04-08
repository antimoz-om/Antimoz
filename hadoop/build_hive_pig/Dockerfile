# Author: Bryan Dieudonne


# Build pseudo-distrubuted Hadoop 2.9
FROM harisekhon/hadoop:latest
MAINTAINER bdieu178

ARG PIG_VERSION=0.16.0
ARG HIVE_VERSION=2.3.3

# hadoop-common fixes
ENV PATH $PATH:$HADOOP_PREFIX/bin

# pig
RUN curl -s http://apache.mirror.anlx.net/pig/pig-${PIG_VERSION}/pig-${PIG_VERSION}.tar.gz | tar -xz -C /usr/local
ENV PIG_HOME /usr/local/pig-${PIG_VERSION}/
RUN ln -s $PIG_HOME /usr/local/pig
ENV PATH $PATH:$PIG_HOME/bin

# hive
RUN curl -s http://apache.mirror.anlx.net/hive/hive-${HIVE_VERSION}/apache-hive-${HIVE_VERSION}-bin.tar.gz  | tar -xz -C /usr/local
ENV HIVE_HOME /usr/local/apache-hive-${HIVE_VERSION}-bin/
RUN ln -s $HIVE_HOME /usr/local/hive
ENV PATH $PATH:$HIVE_HOME/bin
