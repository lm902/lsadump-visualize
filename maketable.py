#!/usr/bin/env python3
import json
import sys
print("Reading log file")
with open(sys.argv[1]) as jsonfile:
    creds = json.loads(jsonfile.read())
print(str(len(creds)) + " entries found. Converting")
table = "<table><tr><th>Identifier</th><th>Username</th><th>LM Hash</th><th>NTLM Hash</th></tr>"
for cred in creds:
    table += "<tr><td>{rid!s}</td><td>{user}</td><td>{lm}</td><td>{ntlm}</td></tr>".format(**cred)
table += "</table>"
with open(sys.argv[2], "w") as tablefile:
    tablefile.write(table)

