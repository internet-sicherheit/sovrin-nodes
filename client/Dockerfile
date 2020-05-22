# Dockerfile to build a Container for a sovrin client node

# container will base on ubuntu 16.04
FROM ubuntu:16.04

# update and upgrade node first
RUN apt update -y 
RUN apt upgrade -y

# install node packages
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys CE7709D068DB5E88
RUN apt install -y software-properties-common python-software-properties
RUN add-apt-repository "deb https://repo.sovrin.org/sdk/deb/xenial stable"
RUN apt update -y
RUN apt upgrade -y 
RUN apt install -y indy-cli


# add accpetance_mechanism
RUN mkdir /workspace
WORKDIR /workspace
COPY accpetance_mechanism ./cliconfig.json
RUN indy-cli --config ./cliconfig.json


# get genesis files
RUN curl -O https://raw.githubusercontent.com/sovrin-foundation/sovrin/master/sovrin/pool_transactions_builder_genesis
RUN curl -O https://raw.githubusercontent.com/sovrin-foundation/sovrin/stable/sovrin/pool_transactions_sandbox_genesis
RUN curl -O https://raw.githubusercontent.com/sovrin-foundation/sovrin/stable/sovrin/pool_transactions_live_genesis


