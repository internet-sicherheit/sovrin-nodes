# Dockerfile to build a Container for a Sovrin Validator Node

# based on ubuntu 16.04
FROM ubuntu:16.04

# Login with a root priviliged user, but not root or indy

# Exposing only needed Ports
EXPOSE 9701/tcp
EXPOSE 9702/tcp


# install sovrin packages and update
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CE7709D068DB5E88
RUN sudo apt-get install -y software-properties-common
RUN sudo add-apt-repository "deb https://repo.sovrin.org/deb xenial stable"
RUN sudo apt update -y 
RUN sudo apt upgrade -y 
RUN sudo apt install -y sovrin

