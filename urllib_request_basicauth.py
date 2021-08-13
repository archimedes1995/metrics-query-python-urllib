#!/usr/bin/env python3

import urllib.request
import getpass
import os
import json
import pandas as pd

jq = pd.read_csv('jenkins_queries.csv')

url = jq.loc[3,'URL']

auth_user = "ericnelson"
auth_token = os.environ['JENKINS_TOKEN']

#HTTPBasicAuthHandler setup
passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, url, auth_user, auth_token)
authhandler = urllib.request.HTTPBasicAuthHandler(passman)
opener = urllib.request.build_opener(authhandler)
urllib.request.install_opener(opener)

#request for response
res = urllib.request.urlopen(url)
res_body = res.read()
print(res_body.decode('utf-8'))
