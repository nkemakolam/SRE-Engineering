#!/bin/bash
pip install --upgrade pip
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install  flask
pip install requests
pip freeze > requirements.txt
pip install -r requirements.txt
pip install virtualenvwrapper
brew install direnv
# deactivate the virtual env
#deactivate
rmvirtualenv venv
# y ref https://docs.python-guide.org/dev/virtualenvs/

# to run a python you can perform the following
export FLASK_APP=<flaskfilename.py>
export FLASK_ENV=development
flask run or 
flask -m flask run if the export refuse to find the python module