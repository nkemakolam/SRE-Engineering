#!/bin/bash
docker container run ubuntu ps aux
docker container run ubuntu uptime
docker container run ubuntu uname -accept
docker container run ubuntu free
docker ps -l
docker  ps -n 3
docker  ps -a 
# to keep you docker running 
docker container run -it ubuntu bash

# Monitoring the sytem event on docker
docker system events

# setting up in a container

# first run this command on your terminal to install the container
docker container run -it ubuntu bash
    1  ls
    2 python --version
    3  apt update
    4  apt install python3
    5  python3
    6  pip install pandas
   7  apt install pip
   8  pip install pandas
   9  apt install curl
   10  curl -O https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?accessType=DOWNLOAD > Chicago.csv
  9  history

  # downloading sample csv file
  curl -O https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?accessType=DOWNLOAD > Chicago.csv
## installing matlibplot using pip
python -m pip install -U pip
python -m pip install -U matplotlib
## installing matlibplot using conda
conda install matplotlib
conda install -c conda-forge matplotlib