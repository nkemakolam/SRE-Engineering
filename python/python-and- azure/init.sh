pip install --upgrade pip     
pip install virtualenv
pip install --upgrade pip 
virtualenv venv
source venv/bin/activate
pip install python-decouple  
pip install azure-identity
pip install azure-keyvault
pip freeze >> requirements.txt