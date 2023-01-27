#!/bin/bash
set -euo pipefail

SOURCE_KV="nke-test"
DEST_KV="nke-finali"

SOURCE_SECRETS=$(az keyvault secret list --vault-name $SOURCE_KV --query "[].id" -o tsv | cut -d "/" -f5)
DEST_SECRETS=$(az keyvault secret list --vault-name $DEST_KV --query "[].id" -o tsv | cut -d "/" -f5)
MISSING_SECRETS=$(echo "${SOURCE_SECRETS} ${DEST_SECRETS}" | tr ' ' '\n' | sort | uniq -u)

for MISSING_SECRET in $MISSING_SECRETS
do
    MISSING_VALUE=$(az keyvault secret show --vault-name $SOURCE_KV -n $MISSING_SECRET --query "value" -o tsv)
    az keyvault secret set --vault-name $DEST_KV -n $MISSING_SECRET --value "$MISSING_VALUE"
done





SOURCE_SECRETS=$(az keyvault secret list --vault-name nke-test --query "[].id" -o tsv | cut -d "/" -f5)
echo $SOURCE_SECRETS
DEST_SECRETS=$(az keyvault secret list --vault-name nke-finali --query "[].id" -o tsv | cut -d "/" -f5)
echo $DEST_SECRETS
MISSING_SECRETS=$(echo "${SOURCE_SECRETS} ${DEST_SECRETS}" | tr ' ' '\n' | sort | uniq -u)
echo $MISSING_SECRETS