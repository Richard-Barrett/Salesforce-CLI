#!/usr/bin/env python

import json

# example dictionary that contains data like you want to have in json
details = {
  "user": {
    "username": "INSERT_USERNAME",
    "password": "INSERT_PASSWORD",
    "salesforce_token": "INSERT_TOKEN"
  }
}

with open('secrets.json', 'w') as json_file:
    json.dump(details, json_file, indent=4)

# get json string from that dictionary
json = json.dumps(details, indent=4)
print("JSON will be STD.OUT to secrets.json")
print("Please check the current working directory for the file.")
print json
