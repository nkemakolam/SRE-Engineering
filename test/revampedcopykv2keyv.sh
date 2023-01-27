#!/bin/bash
Source_Kv_Name="nke-test"
Dest_Kv_Name="nke-finali"
MAINSCRET=(/secrete.txt)
j=0
SECRETS+=($(az keyvault secret list --vault-name $Source_Kv_Name --query "[].id" -o tsv | cut -d "/" -f5))

for SECRET in "${SECRETS[@]}"; do
SECRETNAME=$(echo "$SECRET" | sed 's|.*/||') 
SECRET_CHECK=$(az keyvault secret list --vault-name $Dest_Kv_Name --query "[?name=='$SECRETNAME']" -o tsv)
 
if [ -n "$SECRET_CHECK" ]
then
    echo "$SECRETNAME already exists in $Dest_Kv_Name"
else
  for nkem in $SECRETNAME ; do
   while read -r $MAINSCRET[$j];do
    if [[ "$nkem"  == "$MAINSCRETE" ]]; then
   
    echo "coping the match"
    echo "Copying $SECRETNAME from Source KeyVault: $Source_Kv_Name to Destination KeyVault: $Dest_Kv_Name"
    SECRET=$(az keyvault secret show --vault-name $Source_Kv_Name -n $SECRETNAME --query "value" -o tsv)
    az keyvault secret set --vault-name $Dest_Kv_Name -n $SECRETNAME --value "$SECRET" >/dev/null
    echo "secret copied"
  
    else
       echo "looping through plesase be patient"
    fi
    done
    done
fi
done

az keyvault secret list --vault-name nke-test --query "[].id" -o tsv | cut -d "/" -f5