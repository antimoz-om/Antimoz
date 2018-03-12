#!/bin/bash

if [ ! -z "$ENABLE_KERBEROS" ]; then
  /opt/divolte/configureKerberosClient.sh
  export DIVOLTE_JAVA_OPTS="-Djava.security.krb5.conf=/etc/krb5.conf -Dsun.security.krb5.debug=true"
fi

/opt/divolte/divolte-collector/bin/divolte-collector
