FROM java:8

WORKDIR /usr/local/

RUN wget http://divolte-releases.s3-website-eu-west-1.amazonaws.com/divolte-collector/0.7.0/distributions/divolte-collector-0.7.0.tar.gz
RUN tar -xzvf divolte-collector-*.tar.gz --strip-components=1 
RUN rm divolte-collector-*.tar.gz

ADD conf/divolte-collector.conf /usr/local/conf/

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

EXPOSE 8290

ENTRYPOINT ["divolte-collector"]
