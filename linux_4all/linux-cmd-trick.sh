#!/usr/bin/env bash

#it prints the execution process
set -x
whoami
hostname
uname
find
export PATH=$PATH:/home/nkem

which <command> # tells you where a command is stored on the file system

#nginx tricks


#it prints the execution process
set -x
nginx -v
nginx -t
nginx -T
nginx -s reload