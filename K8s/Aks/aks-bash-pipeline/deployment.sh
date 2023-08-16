#!/usr/bin/env bash

#it prints the execution process
set -x
kubectl version
kubectl run nginx-prod --image=nginx  -n  atrium
kubectl get rolebindings,clusterrolebindings -n atrium
kubectl get pod -n atrium
  
