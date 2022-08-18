#!/bin/bash
#variable declaration

set -xe

az group create -n ${rgname} -l ${location}

az appservice plan create -n ${appservname}  --is-linux -g ${rgname}  -l ${location} --sku ${skutype} --number-of-worker ${numberofworker}

az webapp create -n ${webappname} -p  ${appservplanname}  -i ${imagereponame}:${tag}


#Scale 
az appservice -n ${appservname}  -g ${rgname}  --number-of-worker ${numberofworker}
