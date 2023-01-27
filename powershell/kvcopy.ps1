#https://stackoverflow.com/questions/72867701/migrate-az-keyvault-secrets-using-a-filter
# az login
# az account set --subscription "<subscription-id>"

$sourceKvName = "nke-test"
$targetKvName = "baby-vault"

$secretNames = @(
  "newsecret101",
  "newsecret107",
  "sec110",
  "secret104"
)

foreach ($secretName in $secretNames) {
  $existingSecret = az keyvault secret show `
    --vault-name $sourceKvName `
    --name $secretName `
  | ConvertFrom-Json
  
  # Create the secret
  az keyvault secret set `
    --vault-name $targetKvName `
    --name $secretName `
    --value $existingSecret.value `
  | Out-Null

  # Set content type if defined
  if ($existingSecret.contentType) {
    az keyvault secret set-attributes `
      --vault-name $targetKvName `
      --name $secretName `
      --content-type $existingSecret.contentType `
    | Out-Null
  }

  # Set activation date if defined
  if ($existingSecret.attributes.notBefore) {
    az keyvault secret set-attributes `
      --vault-name $targetKvName `
      --name $secretName `
      --not-before ([DateTime]$existingSecret.attributes.notBefore).ToString("yyyy-MM-dd'T'HH:mm:ss'Z'") `
    | Out-Null
  }
  
  # Set expiration date if defined
  if ($existingSecret.attributes.expires) {
    az keyvault secret set-attributes `
      --vault-name $targetKvName `
      --name $secretName `
      --expires ([DateTime]$existingSecret.attributes.expires).ToString("yyyy-MM-dd'T'HH:mm:ss'Z'") `
    | Out-Null
  }

  # Set tags if defined
  if ($existingSecret.tags) {
    $tagArray = @()
    foreach ($prop in $existingSecret.tags.PsObject.Properties) {
      $tagArray += "$($prop.Name)=$($prop.Value)"
    }

    az keyvault secret set-attributes `
      --vault-name $targetKvName `
      --name $secretName `
      --tags $tagArray `
    | Out-Null
  }
}