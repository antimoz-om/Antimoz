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
# Download and Install Divolte
#
RUN curl -o divolte-collector-0.7.0.tar.gz http://divolte-releases.s3-website-eu-west-1.amazonaws.com/divolte-collector/0.7.0/distributions/divolte-collector-0.7.0.tar.gz && \
    tar zxpf divolte-collector-0.7.0.tar.gz -C /opt/divolte

#
# Configuration changes using divolte-collector.conf
#
ADD conf/divolte-collector.conf /opt/divolte/divolte-collector-0.7.0/conf/divolte-collector.conf
RUN chown root:root /opt/divolte/divolte-collector-0.7.0/conf/divolte-collector.conf

#
# Expose the Divolte Collector click simulation web page
#
EXPOSE 8290

CMD ["/opt/divolte/divolte-collector-0.7.0/bin/divolte-collector"]
