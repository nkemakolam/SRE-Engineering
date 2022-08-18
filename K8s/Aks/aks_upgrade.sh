#!/usr/bin/env bash
set -ex

az login
s2=''
az account set -s ${s2}

az account set -s UNICEF_ICTD_APPS
az aks get-upgrades --resource-group rs-uni-apps-aks-dev --name uni-apps-aks-dev --output table


az aks nodepool update \
  --resource-group rs-uni-apps-aks-dev \
  --cluster-name uni-apps-aks-dev \
  --name default \
  --enable-cluster-autoscaler \
  --min-count 5\
  --max-count 8

  
az aks upgrade \
    --resource-group rs-uni-apps-aks-dev \
    --name uni-apps-aks-dev \
    --kubernetes-version 1.21.7