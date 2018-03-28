#! /bin/bash

# remove any existing containers named hadoop
docker rm -f -v hadoop

# run Hadoop 2.8.3 mapped to host local filesystem on file
# path ~/hadoop_container/shared_files.
# The Hadoop container will map this folder to file path /shared_files within
# the container.

docker run -d --name=hadoop -v ${HOME}/hadoop_container/shared_files:/shared_files/ -p 6000:6000 docker.io/harisekhon/hadoop:latest

#start the terminal within the hadoop container
docker exec -it hadoop /bin/bash
