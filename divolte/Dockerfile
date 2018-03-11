FROM java:8

WORKDIR /usr/local/

RUN wget http://divolte-releases.s3-website-eu-west-1.amazonaws.com/divolte-collector/0.6.0/distributions/divolte-collector-0.6.0.tar.gz && \
    tar -xzvf divolte-collector-0.6.0.tar.gz --strip-components=1 && \
    rm divolte-collector-0.6.0.tar.gz
 

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

EXPOSE 8290

ENTRYPOINT ["divolte-collector"]
