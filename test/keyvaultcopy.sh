#!/bin/bash
Source_Kv_Name="nke-test"
Dest_Kv_Name="nke-finali"
MAINSCRETE="newsecret21"
SECRETS+=($(az keyvault secret list --vault-name $Source_Kv_Name --query "[].id" -o tsv | cut -d "/" -f5))
for SECRET in "${SECRETS[@]}"; do
SECRETNAME=$(echo "$SECRET" | sed 's|.*/||')
SECRET_CHECK=$(az keyvault secret list --vault-name $Dest_Kv_Name --query "[?name=='$SECRETNAME']" -o tsv)
if [ -n "$SECRET_CHECK" ]
then
    echo "$SECRETNAME already exists in $Dest_Kv_Name"
else
  for nkem in $SECRETNAME ; do
   if [[ "$nkem"  == "$MAINSCRETE" ]]; then
    echo $nkem
    echo "coping the match"
    echo "Copying $SECRETNAME from Source KeyVault: $Source_Kv_Name to Destination KeyVault: $Dest_Kv_Name"
    SECRET=$(az keyvault secret show --vault-name $Source_Kv_Name -n $SECRETNAME --query "value" -o tsv)
    az keyvault secret set --vault-name $Dest_Kv_Name -n $SECRETNAME --value "$SECRET" >/dev/null
    echo "secret copied"
  
    else
       echo "looping through plesase be patient"
    fi
    done
fi
done