#!/usr/bin/env python3
import json
import sys
print("Reading log file")
with open(sys.argv[1]) as logfile:
    log = logfile.read()
entries = log.split("RID  : ")
del entries[0]
print(str(len(entries)) + " entries found. Converting")
creds = []
for entry in entries:
    creds.append({"rid": int(entry.split("(")[1].split(")")[0]),
                  "user": entry.split("User : ")[1].split("\n")[0],
                  "lm": entry.split("LM   : ")[1].split("\n")[0],
                  "ntlm": entry.split("NTLM : ")[1].split("\n")[0]})
credsjson = json.dumps(creds)
with open(sys.argv[2], "w") as jsonfile:
    jsonfile.write(credsjson)

