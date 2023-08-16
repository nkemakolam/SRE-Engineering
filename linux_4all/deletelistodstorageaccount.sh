#!/bin/bash

# login
az login
az account set -s  "UNICEF_PD_LEARNING_PASSPORT"

# List of storage account names to delete
storage_accounts=("sapmxprd73581e" "sapmxprdd08475" "sapmxprd816e89" /
 "sapmxprd4828bb" "sapmxprd71df7d" "sapmxprd74f193" "sapmxprd177ab8" "sapmxprd8ee76c" / 
 "sapmxprdbaf696" "sapmxprd09fce6" "sapmxprd857bfb" "sapmxprd16a4ce" "sapmxprd54d659" / 
 "sapmxprd995a81" "sapmxprda5afa5" "sapmxprd788af0" "sapmxprde9055c" "sapmxprd981ba3" / 
 "sapmxprd4c3760" "sapmxprd399f6c" "sapmxprdec472c" "sapmxprdb16f75" "sapmxprd61358e" "sapmxprdf343ba" /
 "sapmxprdf149bf" "sapmxprd974fe5" "sapmxprd649360" "sapmxprd70dc8d" "sapmxprd9ab8f0" "sapmxprd026342" / 
 "sapmxprd83d4cb" "sapmxprda1aca2" "sapmxprd291e9b" "sapmxprd312b71" "sapmxprde48e7f" "sapmxprd0ebf2a" /
 "sapmxprd6503fd" "sapmxprd423258" "sapmxprdf9fc50" "sapmxprd8f4570" "sapmxprd822221" "sapmxprdf4e14b" / 
 "sapmxprd682e2f" "sapmxprd754d0e" "sapmxprd4734d6")

# Loop through the storage account names and delete them
for account_name in "${storage_accounts[@]}"
do
    echo "Deleting storage account: $account_name"
    az storage account delete --name $account_name --yes --resource-group pmx-prd-primero-rg
done