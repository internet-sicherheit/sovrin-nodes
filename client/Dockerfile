# Dockerfile to build a Container for a sovrin validatior node

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




