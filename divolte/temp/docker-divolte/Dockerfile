# Divolte
#
# Divolte Documentation:
# www.divolte.io
#

FROM java:8-jre

#
# Prerequisite: Create some folders for later usage
#
RUN mkdir -p /opt/divolte

#
# Configuration
#
ENV DIVOLTE_VERSION 0.7.0

#
# Download and Install Divolte
#
RUN curl -o divolte-collector-${DIVOLTE_VERSION}.tar.gz http://divolte-releases.s3-website-eu-west-1.amazonaws.com/divolte-collector/${DIVOLTE_VERSION}/distributions/divolte-collector-${DIVOLTE_VERSION}.tar.gz && \
    tar zxpf divolte-collector-${DIVOLTE_VERSION}.tar.gz -C /opt/divolte && \
    mv /opt/divolte/divolte-collector-${DIVOLTE_VERSION}/ /opt/divolte/divolte-collector

#
# Configuration changes using divolte-collector.conf
#
ADD conf/divolte-collector.conf /opt/divolte/divolte-collector/conf/divolte-collector.conf
ADD conf/logback.xml /opt/divolte/divolte-collector/conf/logback.xml
RUN chown root:root /opt/divolte/divolte-collector/conf/divolte-collector.conf && \
    chown root:root /opt/divolte/divolte-collector/conf/logback.xml

ENV DEBIAN_FRONTEND=noninteractive

COPY start.sh /opt/divolte/

#
# Expose the Divolte Collector click simulation web page
#
EXPOSE 8290

CMD ["/opt/divolte/start.sh"]
