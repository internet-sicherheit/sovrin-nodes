# Dockerfile to build a Container for a sovrin client node

# container will base on ubuntu 16.04
FROM ubuntu:16.04

# update and upgrade node first
RUN sudo apt update -y
RUN sudo apt upgrade -y

# install node packages
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --rcv-keys CE7709D068D85E88
RUN sudo apt install -y software-properties-common python-software-properties
RUN sudo add-apt-repository "deb https://repo.sovrin.org/sdk/deb/xenial stable"
RUN sudo apt update -y
RUN sudo apt upgrade -y 
RUN sudo apt install -y indy-cli


# add accpetance_mechanism
RUN mkdir /workspace
WORKDIR /workspace
COPY accpetance_mechanism ./cliconfig.json
RUN indy-cli --config ./cliconfig.json


# get genesis files
RUN curl -O https://raw.githubusercontent.com/sovrin-foundation/sovrin/master/sovrin/pool_transactions_builder_genesis
RUN curl -O https://raw.githubusercontent.com/sovrin-foundation/sovrin/stable/sovrin/pool_transactions_sandbox_genesis
RUN curl -O https://raw.githubusercontent.com/sovrin-foundation/sovrin/stable/sovrin/pool_transactions_live_genesis

# generate steward keys
#RUN sudo apt install -y pwgen
#RUN pwgen -s 32 1
