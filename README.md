# sovrin-validator-client

## Preparation

**P1: Build and Run**  
`docker build -t clienti /path/to/sovrin-validator-client/`  
`docker build -t nodei /path/to/sovrin-validator-node/`  
Build the docker images by using the dockerfiles and run them.  
Remember of using easy names for your containers! ! !  

**P2: Inspect network**  
`docker network inspect bridge`  
Find out the IP-Adresses of your client and node container for later commands.  

## Setup the containers

C = steps to do at the client
N = steps to do at the node

**C1: Create seed**  
`pwgen -s 32 -1 >> client_seed.txt`  
If it does not already exist, create a new seed for generating your did and safe it for later use.  
Copy the content of client_seed.txt in you clipboard. 

**C2: Start indy-cli**   
`indy-cli --config ./cliconfig.json`  
Run indy-cli with cliconfig.json as parameter for session management.  
Run the following Steps inside the indy-cli

C2.1: create pool  
`pool create buildernet gen_txn_file=pool_transactions_builder_genesis`  
Create the pool your validator will the working in later.  

C2.2: create wallet
`wallet create buildernet_wallet key=<key_for_wallet>`  
Create the wallet your date will be stored in. Feel to use a different name for you wallet, but only lower cases are accepted.  
The key for your wallet you will need to create and everytime you open the wallet. So it will be better to save it anywhere.  

C2.3: Connect pool
`pool connect buildernet`  
Connect to the pool you created in C2.1  

C2.4: Open wallet  
`wallet open buildernet_wallet key=<key_for_wallet>`  
Open the wallet to use it in the pool. Here you need the key your set in C2.2 for the wallet. 

C2.5: Create did  
`did new seed=<seed_client>`  
Create a did to store in your opened wallet. Create based on the client_seed. If you did not create a new seed, because you alread had one, your previous did will be recreated.  


**SWITCH TO VALIDATOR NODE**

**N1: init indy node**  
`init_indy_node <ALIAS> <node_ip> <node_port> <client_ip> <client_port>`  
Init your indy node. Replace the placeholder by the real values and press ENTER.  
Save the output for later use.  

**N2: check sovrin version**  
`apt update`  
`apt-cache policy sovrin`  
Update apt packages and check the installed version of sovrin.  

`apt install sovrin=<version_number>`  
If current version is not installed, do that explicitly.  


**SWITCH TO CLIENT**

**C3: reopen indy-cli**  
`indy-cli --config ./cliconfig.json`  
`pool connect buildernet`  
`wallet open buildernet_wallet key=<key_of_wallet>`  
If you are not inside the indy-cli anymore, switch inside and open pool and wallet again.  

**C4: config client**  
`ledger node target=<node_identifier> node_ip=<node_ip> node_port=<node_port> client_ip=<client_ip> client_port=<client_port> alias=<node_alias> services=VALIDATOR blskey=<node_bls_key> blskey_pop=<node_bls_key_pop>`  
Config the client for communicating with the node. 
<node_identifier> = Verification key copied from the output of init_indy_node command
<node_bls_key>, <node_bls_key_pop> although copied from output of init_indy_node command 

<!-- 

## Introduction
A sovrin validator client is an instance the human interacts with. It presents a UI (GUI / CLI) to the user, an communicats the users input to the sovrin validator node. 
In our case the client runs inside a docker container to be able to run it on nealy every host. 

## Components



## Usage
Für Linux-Anwender soll ein Skript die Steuerung des Build- und Run-Prozesses übernehmen. Somit muss dieses lediglich ausgeführt werden. Alle benötigten Informationen werden anschließend abgefragt, oder können direkt als Parameter beim Aufruf übergeben werden. 

client to communicate with a sovrin validator node

-->
