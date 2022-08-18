import adal
import requests

tenant = "contoso.com"
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

# this user must not have mfa or concent
username = "foo@contoso.com"
password = "mypassword"

authority = "https://login.microsoftonline.com/" + tenant
RESOURCE = "https://graph.microsoft.com"

context = adal.AuthenticationContext(authority)

# Use this for Client Credentials
#token = context.acquire_token_with_client_credentials(
#    RESOURCE,
#    client_id,
#    client_secret
#    )

# Use this for Resource Owner Password Credentials (ROPC)  
token = context.acquire_token_with_username_password(RESOURCE, username, password, client_id);

graph_api_endpoint = 'https://graph.microsoft.com/v1.0{0}'

# /me only works with ROPC, for Client Credentials you'll need /<UsersObjectId/
request_url = graph_api_endpoint.format('/me')
headers = { 
'User-Agent' : 'python_tutorial/1.0',
'Authorization' : 'Bearer {0}'.format(token["accessToken"]),
'Accept' : 'application/json',
'Content-Type' : 'application/json'
}

response = requests.get(url = request_url, headers = headers)
print (response.content)