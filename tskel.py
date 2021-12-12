#!/usr/bin/python2.7

#import subprocess

def writeToFile(path, content):
  file = open(path, "w")
  file.write(content)
  file.close()
  
  
PATH_TO_MY_FILE = './Note.md'
CONTENT_FOR_MY_FILE = '# RECON\n---\n- To have more information we can start with ping and then an nmap\n### ping\n> Linux -> 64 TTL\n> Windows -> 128 TTL\n```shell\nping -c 1 IP\n```\n\n#### nmap\n*Noisy*\n```shell\nsudo nmap -p- --open -T5 -v -n IP\n```\n*Recommended*\n```shell\nsudo nmap -p- -sS --min-rate 5000 --open -vvv -n -Pn IP -oG allPorts\nextract allPorts\nnmap -sCV -pPORTS IP -Pn -oN targeted\n```\n\n# DISCOVER'

writeToFile(PATH_TO_MY_FILE, CONTENT_FOR_MY_FILE)

#subprocess.check_output('obsidian Note.md&', shell=True)
