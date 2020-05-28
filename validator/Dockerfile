# Dockerfile to build a Container for a Sovrin Validator Node

# based on ubuntu 16.04
FROM ubuntu:16.04

# Login with a root priviliged user, but not root or indy

# Exposing only needed Ports
EXPOSE 9701/tcp
EXPOSE 9702/tcp


# install sovrin packages and update
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CE7709D068DB5E88 \
  && apt-get update \
  && apt-get install -y software-properties-common apt-transport-https ca-certificates \ 
  && add-apt-repository "deb [arch=amd64] http://repo.sovrin.org/deb xenial stable" \
  && apt-get update \
  && apt-get install -y sovrin
ADD indy_config.py /etc/indy/indy_config.py

USER indy
RUN mkdir /var/lib/indy/net3
WORKDIR /var/lib/indy/net3
ADD https://raw.githubusercontent.com/sovrin-foundation/sovrin/master/sovrin/domain_transactions_builder_genesis domain_transactions_genesis
ADD https://raw.githubusercontent.com/sovrin-foundation/sovrin/master/sovrin/pool_transactions_builder_genesis pool_transactions_genesis

