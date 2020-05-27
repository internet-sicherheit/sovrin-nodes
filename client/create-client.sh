#!/bin/bash

if [ "$1" != "-d" ]
then 
	echo "unvalid parameter, first parameter must be '-d'"
	exit
fi

if [ -z "$2" ]
then 
	echo "missing parameter, secound parameter must be set and reference the DID"
	exit
fi

path=$2 

# Docker build by dockerfile with setting up the indy wallet.
docker build -t validator:client . 

# docker run with presenting the keys for the wallet
docker run --name validator-client -d -it -v $2:/workspace/keys validator:client

# docker exec with loading the importet key data into the wallet
docker exec validator-client indy-cli --config ./cliconfig.json indy-commands-setup

