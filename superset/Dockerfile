FROM ubuntu
MAINTAINER Tyler Fowler <tylerfowler.1337@gmail.com>

# Superset setup options
ENV SUPERSET_HOME /superset
ENV SUP_ROW_LIMIT 5000
ENV SUP_WEBSERVER_THREADS 8
ENV SUP_WEBSERVER_PORT 8088
ENV SUP_WEBSERVER_TIMEOUT 60
ENV SUP_SECRET_KEY 'thisismysecretkey'
ENV SUP_META_DB_URI "sqlite:///${SUPERSET_HOME}/superset.db"
ENV SUP_CSRF_ENABLED True

# admin auth details
ENV ADMIN_USERNAME admin
ENV ADMIN_FIRST_NAME admin
ENV ADMIN_LAST_NAME user
ENV ADMIN_EMAIL admin@nowhere.com
ENV ADMIN_PWD superset

ENV RUNTIME_DEPS python-dev python-pip
ENV BUILD_DEPS npm git build-essential libssl-dev libffi-dev libsasl2-dev libldap2-dev nodejs-legacy

RUN apt-get update \
&& apt-get install -y $BUILD_DEPS $RUNTIME_DEPS \
&& pip install --upgrade setuptools pip \
&& npm install -g npm@'>=5.0.3' \
&& git clone https://github.com/Fokko/incubator-superset.git $SUPERSET_HOME \
&& cd $SUPERSET_HOME/superset/assets \
&& npm install \
&& npm run build \
&& cd $SUPERSET_HOME \
&& python setup.py install \
&& apt-get remove -y $BUILD_DEPS \
&& apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/* && rm -rf ~/.npm/

COPY superset-init.sh /superset-init.sh
RUN chmod +x /superset-init.sh

VOLUME $SUPERSET_HOME
EXPOSE 8088

# since this can be used as a base image adding the file /docker-entrypoint.sh
# is all you need to do and it will be run *before* Superset is set up
ENTRYPOINT [ "/superset-init.sh" ]
