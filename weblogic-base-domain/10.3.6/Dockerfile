# LICENSE MIT License 2015
#
# GIBAHOLMS DOCKERFILES PROJECT (https://gibaholms.wordpress.com/)
# -----------------------------------------
# This Dockerfile extends a Oracle WebLogic Server image by creating a sample domain.
# 
# The domain name will be 'base_domain', created with the default versions for JEE APIs.
# The admin server listens port 7001.
#
# HOW TO BUILD THIS IMAGE
# -----------------------------------------
# Put all downloaded files in the same directory as this Dockerfile
# Run: 
#      $ sudo docker build -t gibaholms/weblogic-base-domain:10.3.6 . 
#
# AUTHOR
# -----------------------------------------
# Gilberto Holms <gibaholms85@gmail.com>
# https://gibaholms.wordpress.com/
# -----------------------------------------

# Pull base image
# ---------------
FROM gibaholms/weblogic:10.3.6

# Maintainer
# ----------
MAINTAINER Gilberto Holms <gibaholms85@gmail.com>

# WLS Configuration
# -------------------------------
ENV ADMIN_PASSWORD welcome01
ENV ADMIN_PORT 7001
ENV NM_PORT 5556
ENV USER_MEM_ARGS -Xms256m -Xmx512m -XX:MaxPermSize=1024m
ENV EXTRA_JAVA_PROPERTIES $EXTRA_JAVA_PROPERTIES -Djava.security.egd=file:///dev/urandom

# Add files required to build this image
COPY create-wls-domain.py /u01/oracle/

# Root commands
USER root
RUN echo ". /u01/oracle/weblogic/user_projects/domains/base_domain/bin/setDomainEnv.sh" >> /root/.bashrc && \
    echo "export PATH=$PATH:/u01/oracle/weblogic/wlserver_10.3/common/bin:/u01/oracle/weblogic/user_projects/domains/base_domain/bin" >> /root/.bashrc

# Configuration of WLS Domain
USER oracle
WORKDIR /u01/oracle/weblogic
RUN /u01/oracle/weblogic/wlserver_10.3/common/bin/wlst.sh -skipWLSModuleScanning /u01/oracle/create-wls-domain.py && \
    mkdir -p /u01/oracle/weblogic/user_projects/domains/base_domain/servers/AdminServer/security && \
    echo "username=weblogic" > /u01/oracle/weblogic/user_projects/domains/base_domain/servers/AdminServer/security/boot.properties && \ 
    echo "password=$ADMIN_PASSWORD" >> /u01/oracle/weblogic/user_projects/domains/base_domain/servers/AdminServer/security/boot.properties && \
    echo ". /u01/oracle/weblogic/user_projects/domains/base_domain/bin/setDomainEnv.sh" >> /u01/oracle/.bashrc && \ 
    echo "export PATH=$PATH:/u01/oracle/weblogic/wlserver_10.3/common/bin:/u01/oracle/weblogic/user_projects/domains/base_domain/bin" >> /u01/oracle/.bashrc 

# Expose Node Manager default port, and also default http/https ports for admin console
EXPOSE $NM_PORT $ADMIN_PORT 

# Final setup
WORKDIR /u01/oracle

ENV PATH $PATH:/u01/oracle/weblogic/wlserver_10.3/common/bin:/u01/oracle/weblogic/user_projects/domains/base_domain/bin:/u01/oracle

# Define default command to start bash. 
CMD ["startWebLogic.sh"]
