# Dockerfile to build a Container for a sovrin client node

# container will base on ubuntu 16.04
FROM ubuntu:16.04

# install node packages
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys CE7709D068DB5E88
RUN apt-get update \
  && apt-get install -y software-properties-common python-software-properties apt-transport-https ca-certificates pwgen \
  && rm -rf /var/lib/apt/lists/*

RUN add-apt-repository "deb https://repo.sovrin.org/sdk/deb xenial stable"
RUN apt-get update  \
  && apt-get install -y indy-cli \
  && rm -rf /var/lib/apt/lists/*

# add accpetance_mechanism
RUN mkdir /workspace
WORKDIR /workspace
COPY acceptance_mechanism.json ./cliconfig.json
COPY indy-commands-setup ./indy-commands-setup
RUN indy-cli --config ./cliconfig.json


# get genesis files
ADD https://raw.githubusercontent.com/sovrin-foundation/sovrin/master/sovrin/pool_transactions_builder_genesis pool_transactions_builder_genesis
ADD https://raw.githubusercontent.com/sovrin-foundation/sovrin/stable/sovrin/pool_transactions_sandbox_genesis pool_transactions_sandbox_genesis
ADD https://raw.githubusercontent.com/sovrin-foundation/sovrin/stable/sovrin/pool_transactions_live_genesis pool_transactions_live_genesis

# running indy cli with the commands in indy-command file
#RUN indy-cli --config ./cliconfig.json indy-commands-setup
#ENTRYPOINT [ "indy-cli" ]
#CMD [ "--config", "./cliconfig.json", "indy-commands-setup" ]
