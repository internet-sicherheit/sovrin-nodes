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
echo "given path is:"  $path

# deleting a maybe existing old Dockerfile with maybe old paths
rm -f Dockerfile/Dockerfile 
