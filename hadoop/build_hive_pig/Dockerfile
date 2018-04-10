# Author: Bryan Dieudonne


# Build pseudo-distrubuted Hadoop 2.9
FROM harisekhon/hadoop:2.9
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

#add PostGres datastore & Python --> test this
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update -qy
RUN apt-get install -y python3.5 python3.5-dev python3-pip python-dev python3-dev postgresql postgresql-server-dev-all sudo


#add Psycopg library <--processing csv files into PostGres.
RUN pip install psycopg2-binary
